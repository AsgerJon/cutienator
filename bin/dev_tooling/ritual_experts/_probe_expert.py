"""ProbeExpert asks the compiler what it makes of a ritual file before
it is written."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.util import Finalize
from typing import TYPE_CHECKING

from .. import HeaderFolder, HeaderReader, Machine
from . import RitualExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Set, Tuple

  Record = Dict[str, Any]


class ProbeExpert(RitualExpert):
  """
  Asks the compiler what it makes of a ritual file before it is
  written: what it refuses, and, where it refuses nothing, what each
  function the file defines leans on; see 'probeText'. Each compile
  starts from a precompiled header of Qt's own header files, made once
  for the tree; see 'getProbeHeader'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def readCompilerText(text: str) -> Tuple[Dict[str, Set[str]], Set[str]]:
    """
    Reads the text the compiler writes of a file before it makes an
    object file of it, LLVM's IR, which 'clang++ -S -emit-llvm' gives.
    It is the same text on Linux, macOS and Windows, where the object
    files are not: the compiler's own name of each function, as
    '_ZNK7QObject6threadEv', stands in it as it is everywhere, without
    the '_' more that macOS puts in front in an object file.

    Parameters
    ----------

    text : str
      The text, as the compiler wrote it.

    Returns
    -------

    Tuple[Dict[str, Set[str]], Set[str]]
      For each name the file defines, a function, as a ritual, or a
      thing kept in memory, as a table of virtual functions, the names
      it leans on directly; and the names the file only declares, which
      must come from elsewhere.

    The text is read line by line:

      define ... @name(...) ... {   a function the file defines, up to
      }                             the line '}' alone
      declare ... @name(...)        a function from elsewhere
      @name = external global ...   a thing from elsewhere
      @name = ... constant ...      a thing the file defines, leaning
                                    on each name in the rest of the line

    The names of LLVM's own helpers, as 'llvm.memcpy.p0.p0.i64', are
    passed over: the compiler makes them into code of its own.
    """
    #  A name is '@' and the word, or '@' and a text between '"'.
    #  Another text between '"', as that of a 'char' array, may hold
    #  an '@' that is no name, and is passed over whole.
    token = re.compile(r'@"([^"]*)"|"[^"]*"|@([-\w$.]+)')
    escaped = re.compile(r'\\([0-9A-Fa-f]{2})')

    def namesIn(line: str) -> List[str]:
      """Gives each name the line holds, in the order they stand."""
      found = []  # type: List[str]
      for quoted, plain in token.findall(line):
        name = plain or escaped.sub(
            lambda match: chr(int(match.group(1), 16)), quoted)
        #  A leading '\\01' tells the compiler to write the name as it
        #  stands; the name is the rest.
        name = name.lstrip('\x01')
        if name and not name.startswith('llvm.'):
          found.append(name)
      return found

    leans = dict()  # type: Dict[str, Set[str]]
    declared = set()  # type: Set[str]
    inside = None  # type: Optional[str]
    for line in text.split('\n'):
      if inside is not None:
        if line == '}':
          inside = None
        else:
          leans[inside].update(namesIn(line))
        continue
      if line.startswith(('define ', 'declare ')):
        names = namesIn(line)
        if not names:
          continue
        if line.startswith('declare '):
          declared.add(names[0])
          continue
        leans.setdefault(names[0], set()).update(names[1:])
        if line.rstrip().endswith('{'):
          inside = names[0]
        continue
      if not line.startswith('@'):
        continue
      names = namesIn(line)
      if not names:
        continue
      #  The words between '=' and the kind of the thing say whether it
      #  is kept here or elsewhere.
      before = re.split(r' (?:global|constant|alias|ifunc) ', line, 1)[0]
      if re.search(r'= (?:\S+ )*(?:external|extern_weak)\b', before):
        declared.add(names[0])
        continue
      leans.setdefault(names[0], set()).update(names[1:])
    return leans, declared - set(leans)

  @staticmethod
  def findBlamedLines(said: str, fileName: str) -> Set[int]:
    """
    Gives the numbers of the lines of the file of that name that an
    error the compiler printed stands under: the line the error is on,
    or the line of the file the header holding the error was included
    from. The lines a note or a warning stands under are not taken.

    The compiler prints the files a header was included from only when
    they are not those of the message before, so a message without
    them stands under those of the message before.
    """
    blamed, chain = set(), set()  # type: Set[int], Set[int]
    inStack = False
    #  The path before the name ends in '/', or in '\' on Windows.
    place = re.compile(r'(?:^|[/\\])%s:(\d+):' % re.escape(fileName))
    for line in said.splitlines():
      stripped = line.strip()
      if stripped.startswith(('In file included from', 'from ')):
        if not inStack:
          chain, inStack = set(), True
        chain.update(int(number) for number in place.findall(stripped))
        continue
      inStack = False
      if ': error: ' in stripped or ': fatal error: ' in stripped:
        here = place.search(stripped.split(' ')[0])
        if here:
          blamed.add(int(here.group(1)))
        else:
          blamed.update(chain)
    return blamed

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The most rounds 'settle' compiles the ritual file in.
  __settle_rounds__ = 20

  #  Private Variables
  #  The rituals of ours 'settle' took out, with the reason: they stand
  #  for no function of the header by themselves.
  __unwritten_extras__ = None  # type: Optional[List[Tuple[str, str]]]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getNotWrittenExtras(self) -> Tuple[Tuple[str, str], ...]:
    """Gives the rituals of ours 'settle' took out, each with the
    reason."""
    self.getGenerator().getWritten()
    return (*(self.__unwritten_extras__ or ()),)

  def getPrivateArguments(self) -> Tuple[str, ...]:
    """
    Gives the '-I' arguments by which the compiler finds the headers
    Qt calls private for the compiles of the class, or none when no
    part of the tree reads those and no source of Qt was provided.
    They are those of the probe header its compiles start from; see
    '_getProbePart'.
    """
    return self._getPrivateArguments(self._getProbePart())

  def _getPrivateArguments(self, partName: str) -> Tuple[str, ...]:
    """
    Gives the '-I' arguments by which the compiler finds the headers
    Qt calls private: those 'HeaderReader.getPrivateIncludeFolders'
    gives the part of that name, or, for '', those of
    'HeaderReader.getSharedIncludeFolders', in the order of the
    alphabet. None when no part of the tree reads those and no source
    of Qt was provided.
    """
    tree = self.getGenerator().getDependencyTree()
    headerReaders = tree.getHeaderReaders()
    if tree.getSourceReader() is None:
      if not any(reader.hasPrivate() for reader in headerReaders):
        return ()
    folders = HeaderReader.getSharedIncludeFolders()
    for reader in headerReaders:
      if partName and reader.getPartName() == partName:
        folders = reader.getPrivateIncludeFolders()
    return (*('-I%s' % folder for folder in folders),)

  def _getProbePart(self) -> str:
    """
    Gives the part whose folders the compiles of the class are told:
    the part of the class where it has a probe header of its own; else
    '', the folders in the order of the alphabet, which the one of
    every part is made with. A precompiled header serves only a compile
    told the same.
    """
    generator = self.getGenerator()
    kept = generator.getDependencyTree().getKept('probe header')
    if 'path' not in kept:
      self._makeProbeHeaders(kept)
    partName = generator.getPartName()
    return partName if partName in kept['own'] else ''

  def _getProbeCommand(self, partName: str) -> Tuple[str, ...]:
    """Gives the start of the 'clang++' command of 'probeText', which
    the precompiled header of 'getProbeHeader' is made with as well: a
    precompiled header serves only a compile told the same. The folders
    are those of the part of that name, or of the first part of the
    tree for ''; see '_getPrivateArguments'."""
    return (
        'clang++', '-std=c++17', *Machine.getCompilerFlags(), '-O0',
        #  No warning, but a function of the file's own used and defined
        #  nowhere is refused: a library holding it would not load.
        '-Wno-everything', '-Werror=undefined-internal',
        '-fno-access-control', '-DQT_USE_QSTRINGBUILDER',
        '-ffunction-sections', '-ferror-limit=0',
        '-I%s' % HeaderReader.getQtHeaderFolder(),
        *self._getPrivateArguments(partName),
    )

  def getProbeHeader(self) -> str:
    """
    Gives the path of the precompiled header each compile of
    'probeText' starts from: the own list of every part of the tree,
    as '#include <QtCore/QtCore>', read by the compiler once and
    written down as the compiler keeps it. A compile that starts from
    it takes a tenth of the time, since reading Qt's headers is most
    of the work.

    Made for you at the first call, which takes about twenty seconds,
    and kept with the tree. It lies in a folder of its own in the work
    folder of the first part of the tree, about 65 MB, and that folder
    is removed when the Python that made it ends. Call it once before
    handing the tree to other processes, and they all start from the
    one file.

    A part whose line the compiler blames for an error is left out,
    and the header made again without it: Qt's QtGraphs refuses to be
    in one compile with QtCharts or QtDataVisualization, since they
    use the same class names. 'getLeftOutParts' gives those parts,
    with what the compiler said. Each of them gets a header of its
    own, of the part and the parts it needs, as Qt's own build has
    them together, and the compiles of its classes start from that
    one. So does each part of 'HeaderReader.getOwnOrderParts', whose
    folders come in its own order, where the one of every part is made
    with them in the order of the alphabet. A part whose own header the
    compiler refuses has its classes written down as missed, and
    'RitualGenerator.write' refuses them.

    Raises
    ------

    RuntimeError
      The compiler refused to make it, and blamed no line of a part.
      The message holds what it said.

    LookupError
      The part of the class is left out, and the compiler refused its
      own header; see 'getRefusedParts'.
    """
    generator = self.getGenerator()
    kept = generator.getDependencyTree().getKept('probe header')
    if 'path' not in kept:
      self._makeProbeHeaders(kept)
    partName = generator.getPartName()
    if partName in kept['refused']:
      infoSpec = """%s is not written: its part %s is left out of the
      probe header, and the compiler refused its own one: %s"""
      info = infoSpec % (
          generator.getClassName(), partName, kept['refused'][partName])
      raise LookupError(' '.join(info.split()))
    return kept['own'].get(partName, kept['path'])

  def getLeftOutParts(self) -> Dict[str, str]:
    """
    Gives the parts 'getProbeHeader' left out of the header of every
    part, each with what the compiler said of it; an empty dict when it
    left out none. Makes the probe headers when they are not made yet.
    """
    kept = self.getGenerator().getDependencyTree().getKept('probe header')
    if 'path' not in kept:
      self._makeProbeHeaders(kept)
    return dict(kept['left out'])

  def getRefusedParts(self) -> Dict[str, str]:
    """
    Gives the parts left out whose own probe header the compiler
    refused as well, each with what it said: their classes are not
    written. Makes the probe headers when they are not made yet.
    """
    kept = self.getGenerator().getDependencyTree().getKept('probe header')
    if 'path' not in kept:
      self._makeProbeHeaders(kept)
    return dict(kept['refused'])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def settle(
      self,
      written: List[Record],
      unwritten: List[Tuple[str, str]],
  ) -> None:
    """
    Compiles the ritual file as it would be written, and takes out every
    ritual the compiler refuses, with what it said, round by round until
    it refuses none: one ritual the compiler cannot make where the file
    stands, as one naming a type the header spells short and the tree
    does not know, never costs the class the others. What it refuses
    before every ritual, in a line pulling a file in, in code taken from
    Qt's source or in a class of ours, is left for 'CopyExpert.settle'
    and the tester to find.
    """
    from . import CopyExpert, HeldValueExpert, RitualFileExpert
    self.__unwritten_extras__ = []
    generator = self.getGenerator()
    for _ in range(self.__settle_rounds__):
      text = generator.getRitualTextOf(written, unwritten)
      refused = self.probeText(text)[0]
      if not refused:
        return
      lines = text.split('\n')
      dropped = set()  # type: Set[str]
      for lineNumber, said in sorted(refused.items()):
        owner = RitualFileExpert.findRitualAt(lines, lineNumber)
        if not owner or owner in dropped:
          continue
        infoSpec = """the compiler refuses its ritual as it would be
        written here: %s"""
        reason = ' '.join((infoSpec % said).split())
        for plan in [*written]:
          if plan.get('ritualName') != owner:
            continue
          written.remove(plan)
          if CopyExpert.isOursOnly(plan['kind']):
            self.__unwritten_extras__.append((plan['function'], reason))
          else:
            unwritten.append((plan['function'], reason))
        dropped.add(owner)
      if not dropped:
        return
      generator.getExpert(HeldValueExpert).forgetDrops(written)

  def _makeProbeHeaders(self, kept: Dict[str, Any]) -> None:
    """Makes the probe headers 'getProbeHeader' gives, and keeps them
    with what the compiler said of the parts left out."""
    tree = self.getGenerator().getDependencyTree()
    lines = []  # type: List[Tuple[str, str]]
    headerReaders = tree.getHeaderReaders()
    held = dict()  # type: Dict[str, str]
    for headerReader in headerReaders:
      partName = headerReader.getPartName()
      partFolder = headerReader.getPartFolder()
      if os.path.isfile(os.path.join(partFolder, partName)):
        held[partName] = '#include <%s/%s>' % (partName, partName)
        lines.append((partName, held[partName]))
    folder = tempfile.mkdtemp(
        prefix='probe_header_', dir=headerReaders[0].getWorkFolder())
    Finalize(
        None, shutil.rmtree, args=(folder,),
        kwargs=dict(ignore_errors=True), exitpriority=0)
    leftOut = dict()  # type: Dict[str, str]
    while True:
      said, blamed = self._compileProbeHeader(folder, 'probe', lines, '')
      if said is None:
        break
      blamed = {number for number in blamed if number <= len(lines)}
      if not blamed:
        infoSpec = """The compiler refused to make the precompiled
        header the settling compiles start from: %s"""
        info = infoSpec % said[:800]
        raise RuntimeError(' '.join(info.split()))
      for number in sorted(blamed, reverse=True):
        partName = lines.pop(number - 1)[0]
        leftOut[partName] = said[:600]
    own, refused = dict(), dict()  # type: Dict[str, str], Dict[str, str]
    #  A part left out, and a part whose folders come in its own order,
    #  as QtGraphs, whose 'private/qabstractseries_p.h' is its own and
    #  not that of QtCharts; see 'HeaderReader.getOwnOrderParts'.
    apart = [
        *leftOut, *(
            name for name in sorted(HeaderReader.getOwnOrderParts())
            if name in held and name not in leftOut)]

    def makeOwn(partName: str) -> Tuple[str, Optional[str]]:
      """Makes the probe header of one part and every part it needs,
      those first, as Qt's own build reads them for the part."""
      needed, at = [partName], 0
      while at < len(needed):
        try:
          needs = HeaderFolder.getPartNeeds(needed[at])
        except LookupError:
          needs = ()
        needed.extend(need for need in needs if need not in needed)
        at += 1
      ownLines = [
          (one, held[one]) for one in reversed(needed) if one in held]
      said, _ = self._compileProbeHeader(
          folder, 'probe_%s' % partName, ownLines, partName)
      return partName, said

    with ThreadPoolExecutor(os.cpu_count() or 1) as pool:
      for partName, said in pool.map(makeOwn, apart):
        if said is None:
          own[partName] = os.path.join(folder, 'probe_%s.pch' % partName)
        else:
          refused[partName] = said[:600]
    for partName, said in refused.items():
      for className in tree[partName]:
        tree.addMissedClass(
            '%s::%s' % (partName, className),
            'its part is left out of the probe header, and the compiler '
            'refused its own one: %s' % said)
    kept['left out'] = leftOut
    kept['own'] = own
    kept['refused'] = refused
    kept['path'] = os.path.join(folder, 'probe.pch')

  def _compileProbeHeader(
      self,
      folder: str,
      stem: str,
      lines: List[Tuple[str, str]],
      partName: str,
  ) -> Tuple[Optional[str], Set[int]]:
    """Writes the lines into '<stem>.h' in the folder and makes
    '<stem>.pch' of it, with the folders of the part of that name, or of
    the first part of the tree for ''. Gives None when the compiler made
    it; else what it said, and the numbers of the lines it blamed."""
    headerFile = os.path.join(folder, '%s.h' % stem)
    with open(headerFile, 'w') as file:
      file.write('%s\n' % '\n'.join(line for _, line in lines))
    command = (
        *self._getProbeCommand(partName), '-fpch-instantiate-templates',
        '-x', 'c++-header', headerFile,
        '-o', os.path.join(folder, '%s.pch' % stem),
    )
    with Machine.handOver(command) as words:
      done = subprocess.run(
          words, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
          universal_newlines=True)
    if not done.returncode:
      return None, set()
    said = ' '.join(done.stderr.split())
    return said, self.findBlamedLines(done.stderr, '%s.h' % stem)

  def probeText(
      self,
      text: str,
  ) -> Tuple[Dict[int, str], Dict[str, Set[str]], Set[str]]:
    """
    Compiles the text of a ritual file, joining nothing, and says what
    came of it. The compile starts from the precompiled header of
    'getProbeHeader', and ends at the text the compiler would make an
    object file of: see 'readCompilerText'.

    Returns
    -------

    Tuple
      What the compiler refused: for each line it complained of, what
      it said. Then, when it refused nothing: for each name the
      compiled file defines, the names its code leans on directly; and
      the names the compiled file needs from elsewhere.
    """
    with tempfile.TemporaryDirectory() as folder:
      probeFile = os.path.join(folder, 'probe.cpp')
      compiledFile = os.path.join(folder, 'probe.ll')
      with open(probeFile, 'w') as file:
        file.write(text)
      command = (
          *self._getProbeCommand(self._getProbePart()), '-S', '-emit-llvm',
          '-include-pch', self.getProbeHeader(), probeFile,
          '-o', compiledFile,
      )
      with Machine.handOver(command) as words:
        done = subprocess.run(
            words, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True)
      if done.returncode:
        #  Each thing the compiler refuses, with the first line of the
        #  file it names for it: the line of the error itself, or,
        #  where the error lies in a header of Qt, the line of the
        #  file that the compiler says asked for it.
        refused = dict()  # type: Dict[int, str]
        error = re.compile(r':\d+:\d+: (?:fatal )?error: (.*)')
        place = re.compile(r'probe\.cpp:(\d+):\d+: ')
        pulled = re.compile(r'In file included from .*probe\.cpp:(\d+)')
        #  What the compiler said last and has no line of ours for yet,
        #  with the line that pulled in the file it lies in.
        waiting = [None, None]  # type: List[Any]
        asked = None  # type: Optional[int]

        def settle() -> None:
          """What is waiting goes to the line that pulled its file in,
          when the compiler named no line of ours after it."""
          if waiting[0] is not None and waiting[1] is not None:
            refused.setdefault(waiting[1], waiting[0])
          waiting[0], waiting[1] = None, None

        for line in done.stderr.split('\n'):
          #  Above an error in a file that was pulled in, the compiler
          #  names the line of ours that pulled it in.
          through = pulled.search(line)
          if through is not None:
            settle()
            asked = int(through.group(1))
            continue
          match = error.search(line)
          if match is not None:
            settle()
            waiting[0], waiting[1] = match.group(1), asked
            asked = None
          where = place.search(line)
          if waiting[0] is not None and where is not None:
            #  The error itself, or a note under it, names a line of
            #  ours: that line is nearer than the one pulling a file in.
            refused.setdefault(int(where.group(1)), waiting[0])
            waiting[0], waiting[1] = None, None
        settle()
        if not refused:
          refused[0] = ' '.join(done.stderr.split())[:400]
        return refused, dict(), set()

      with open(compiledFile, encoding='utf-8') as file:
        leans, wanted = self.readCompilerText(file.read())
      return dict(), leans, wanted
