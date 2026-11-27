"""CopyExpert reaches a function of Qt that Qt's library offers under
no name, by a copy of its code from Qt's source."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import platform
import re
import subprocess
from typing import TYPE_CHECKING

from .. import HeaderReader, Machine, SourceReader
from . import ReachExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Set, Tuple

  Record = Dict[str, Any]
  Reasons = Tuple[Tuple[str, str], ...]


class CopyExpert(ReachExpert):
  """
  Reaches a function of Qt that Qt's library offers under no name, by
  a copy of its code from Qt's source, which the ritual file carries.

  'canReach' says whether Qt's source has code for the function that
  can be told from the rest. Whether that code compiles apart from its
  file, and whether what it leans on can be had, only the compiler can
  say: 'settle' compiles the whole ritual file, takes along the code of
  what the copies lean on, and takes out every ritual whose copy
  cannot stand. What it kept is in 'getSourceText', with the lines
  that pull in what it needs in 'getSourceIncludes'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _getCheckedSystem() -> str:
    """Gives what the compiler knows the system by that the generator
    checks its code for, the one it runs on, as 'defined(Q_OS_LINUX)'.
    """
    systems = dict(
        Linux='defined(Q_OS_LINUX)', Darwin='defined(Q_OS_DARWIN)',
        Windows='defined(Q_OS_WIN)')
    system = platform.system()
    if system not in systems:
      infoSpec = """The generator checks code for the system it runs on,
      and knows no name of the compiler for '%s'."""
      raise NotImplementedError(' '.join((infoSpec % system).split()))
    return systems[system]

  @staticmethod
  def _getCheckedProcessor() -> str:
    """Gives what the compiler knows the processor by that the
    generator checks its code for, the one it runs on, as
    'defined(Q_PROCESSOR_X86_64)'."""
    processors = dict(
        x86_64='defined(Q_PROCESSOR_X86_64)',
        AMD64='defined(Q_PROCESSOR_X86_64)',
        aarch64='defined(Q_PROCESSOR_ARM_64)',
        arm64='defined(Q_PROCESSOR_ARM_64)')
    processor = platform.machine()
    if processor not in processors:
      infoSpec = """The generator checks code for the processor it runs
      on, and knows no name of the compiler for '%s'."""
      raise NotImplementedError(' '.join((infoSpec % processor).split()))
    return processors[processor]

  @staticmethod
  def isOursOnly(kind: str) -> bool:
    """Says whether a ritual of that kind is one of ours that stands for
    no function of the header by itself, as the one running just Qt's
    own function ('own') or the one removing a held value ('drop')."""
    return kind in CopyExpert.__ours_only__

  @staticmethod
  def _nameWritten(written: List[Record]) -> Set[str]:
    """Gives the name the compiler has for the function each ritual
    calls: the name of the ritual without 'ritual' in front."""
    return {
        plan.get('ritualName', '')[len('ritual'):] for plan in written
    }

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  An '#if' line of code taken from Qt's source that asks for a
  #  system, or for a processor; see '_findCopiedConditions'.
  __system_asked__ = re.compile(
      r'^[ \t]*#[ \t]*(?:if|ifdef|ifndef|elif)\b[^\n]*'
      r'\b(?:Q_OS_\w+|Q_CC_\w+|_WIN32|_WIN64|__APPLE__|__linux__|'
      r'__ANDROID__|__EMSCRIPTEN__)\b', re.M)
  __processor_asked__ = re.compile(
      r'^[ \t]*#[ \t]*(?:if|ifdef|ifndef|elif)\b[^\n]*'
      r'\bQ_PROCESSOR_\w+', re.M)
  #  The kinds of the rituals of ours that stand for no function of the
  #  header by themselves.
  __ours_only__ = ('own', 'cast', 'take', 'list', 'map', 'drop')

  #  Private Variables
  #  The code taken from Qt's source for the class, and the lines that
  #  pull in what that code needs; see 'settle'.
  __source_text__ = None  # type: Optional[str]
  __source_includes__ = None  # type: Optional[Tuple[str, ...]]
  #  Classes whose header file the compiler showed has to come before
  #  that of the class, found by 'settle'.
  __pulled_first__ = ()  # type: Tuple[str, ...]
  #  The rituals of ours that stand for no function of the header by
  #  themselves, dropped by 'settle', with the reason; see
  #  'getNotWrittenExtras'.
  __unwritten_extras__ = None  # type: Optional[List[Tuple[str, str]]]
  #  The things of a '.cpp' file that code taken from it needs and Qt's
  #  library has no name for, taken along: a 'static' function, a
  #  constant, a type, a '#define'; see '_findFileLocal'.
  __file_locals__ = None  # type: Optional[List[Tuple[str, Record]]]
  #  What '_findFileLocal' read of each '.cpp' file: its things at the
  #  top, outside every function.
  __file_items__ = dict()  # type: Dict[str, List[Record]]
  #  The tables of virtual functions written from copies, by the name
  #  the compiler has for the table, with the names of the functions
  #  copied for it; see '_findTableMakers'.
  __table_members__ = None  # type: Optional[Dict[str, Tuple[str, ...]]]
  #  A line before a thing of a '.cpp' file that belongs to no thing,
  #  as 'QT_BEGIN_NAMESPACE' or 'QT_WARNING_DISABLE_GCC("-Wfoo")'; see
  #  '_readFileItems'.
  __no_thing__ = re.compile(
      r'\s*(?:QT_(?:BEGIN|END|USE)_NAMESPACE|QT_WARNING_\w+'
      r'(?:\s*\([^()]*\))?)\s*;?\s*')
  #  What the compiler says when code needs a thing it does not see,
  #  with the name of that thing.
  __needs_said__ = re.compile(
      r"(?:undeclared identifier|unknown type name|no template named"
      r"|incomplete type) '(?:const )?([A-Za-z_][\w:]*)'")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getSourceText(self) -> str:
    """Gives the code taken from Qt's own source for the class, as C++
    text under a heading saying whose it is, or '' when none was."""
    if self.__source_text__ is None:
      self.getGenerator().getWritten()
    return self.__source_text__ or ''

  def getSourceIncludes(self) -> Tuple[str, ...]:
    """Gives the lines that pull in what the code of 'getSourceText'
    needs, as the files of Qt's source it was taken from have them."""
    if self.__source_includes__ is None:
      self.getGenerator().getWritten()
    return self.__source_includes__ or ()

  def getPulledFirst(self) -> Tuple[str, ...]:
    """Gives the classes whose header file the compiler showed has to
    come before that of the class, as 'settle' found them."""
    return self.__pulled_first__

  def getNotWrittenExtras(self) -> Reasons:
    """
    Gives the rituals of ours that stand for no function of the header
    by themselves, as the one running just Qt's own function, which
    'settle' had to drop, each with the reason.
    """
    self.getGenerator().getWritten()
    return (*(self.__unwritten_extras__ or ()),)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def canReach(self, member: Record) -> bool:
    """Says whether Qt's source has code for the function that can be
    told from the rest; see 'findSourceCode'."""
    return self.findSourceCode(member) is not None

  def getWay(self) -> str:
    """Says what this way does: the ritual file carries Qt's code."""
    return 'be copied'

  def getRefusal(self) -> str:
    """Says why no code of the function can be copied."""
    return "Qt's source has no code for it that could be told from the rest"

  def findSourceCode(
      self,
      member: Record,
      className: Optional[str] = None,
  ) -> Optional[Record]:
    """
    Gives the definition of a function in Qt's own source, as
    'SourceReader.findDefinitions' has it, or None when no source was
    provided or the source has not exactly one definition that takes
    what the function takes. The function is one of the class of the
    generator, or of 'className' where that is given.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    source = tree.getSourceReader()
    if source is None:
      return None
    if className is None:
      className = generator.getClassName()
    name = member.get('name', '')
    if member.get('kind') == 'CXXConstructorDecl':
      name = className.rpartition('::')[2]
    taken = [
        entry['type']['qualType'] for entry in member.get('inner', ())
        if entry.get('kind') == 'ParmVarDecl'
    ]
    whole = member.get('type', dict()).get('qualType', '')
    const = True if re.search(r'\)\s*const\b', whole) else False
    partName = tree.getPartName(className, generator.getPartName())
    fullName = '%s::%s' % (className, name)
    found = [
        self._placeIn(definition, fullName) for definition
        in source.findDefinitions(partName, fullName)
        if len(definition['arguments']) == len(taken)
        and definition['const'] == const
    ]
    if len(found) > 1:
      #  Several forms take as many: the one whose every argument
      #  begins with the type the header declares, as the '.cpp' file
      #  writes it: in full, or without the namespaces and classes in
      #  front that it need not write where it stands, as 'Program *'
      #  for 'QQmlJS::AST::Program *'.
      def squeeze(written: str) -> str:
        return ''.join(written.split())

      def bare(written: str) -> str:
        return re.sub(r'\b(?:[A-Za-z_]\w*::)+', '', squeeze(written))

      def fits(argument: str, cppType: str) -> bool:
        if squeeze(argument).startswith(squeeze(cppType)):
          return True
        return bare(argument).startswith(bare(cppType))

      found = [
          definition for definition in found
          if all(fits(argument, cppType) for argument, cppType
                 in zip(definition['arguments'], taken))
      ]
    return found[0] if len(found) == 1 else None

  @staticmethod
  def _placeIn(definition: Record, fullName: str) -> Record:
    """
    Gives a definition found under a full name with the namespace it
    has to stand in, under 'namespace': the part of the full name that
    Qt's '.cpp' file does not write before the name, as 'QV4' where
    'qv4engine.cpp' writes 'ExecutionEngine::ExecutionEngine' after
    'using namespace QV4;', and '' where it writes the name in full.
    Its code names things as seen from there, and a copy of it standing
    anywhere else would not find them.
    """
    #  Both without blanks, as 'SourceReader' keeps the names.
    written = ''.join(definition['name'].split())
    fullName = ''.join(fullName.split())
    namespace = ''
    if fullName != written and fullName.endswith('::%s' % written):
      namespace = fullName[:-len(written) - 2]
    return dict(definition, namespace=namespace)

  def settle(
      self,
      written: List[Record],
      unwritten: List[Tuple[str, str]],
  ) -> None:
    """
    Decides which functions get their code from Qt's own source, keeps
    that code for 'getSourceText', and takes out every ritual that
    leans on something that cannot be had.

    It does so for a class that has a function 'canReach' let through
    though it cannot be called, for a class of a header Qt calls
    private, and for a class Qt marks nowhere. The whole ritual file is
    compiled to an object file, against the header files made from
    Qt's source. For each ritual it is then looked up what its code
    leans on, through everything the object file holds itself. What
    Qt's source marks for use from outside Qt is fine; see
    'CallExpert.isMarkedName'. For anything else, Qt's source is asked
    for a definition, which is then taken along. A ritual leaning on
    something that cannot be had that way, as the table through which
    C++ looks functions up in an object of a class Qt keeps to itself,
    is moved from 'written' to 'unwritten', with what stood in the way.

    Raises
    ------

    RuntimeError
      The compiler refuses the file for something that is no code
      taken from Qt's source and no line pulling a file in for it: a
      ritual itself does not compile. The message holds what it said.
    """
    from . import (CallExpert, ConditionExpert, ProbeExpert,
                   RitualFileExpert)
    self.__source_text__, self.__source_includes__ = '', ()
    self.__unwritten_extras__ = []
    self.__file_locals__ = []
    self.__table_members__ = dict()
    self.__pulled_first__ = ()
    generator = self.getGenerator()
    callExpert = generator.getExpert(CallExpert)
    probeExpert = generator.getExpert(ProbeExpert)
    tree = generator.getDependencyTree()
    source = tree.getSourceReader()
    if source is None:
      return
    className = generator.getClassName()
    record = generator._readRecord(className)
    #  A function a way asked before this one reaches is not copied.
    reachExperts = generator.getReachExperts()
    earlier = reachExperts[:reachExperts.index(self)]
    chosen = dict()  # type: Dict[str, Record]
    for member in record.get('inner', ()):
      if generator.getFunctionKind(member.get('kind')) is None:
        continue
      if 'mangledName' not in member:
        continue
      if any(expert.canReach(member) for expert in earlier):
        continue
      definition = self.findSourceCode(member)
      if definition is not None:
        chosen[member['mangledName']] = definition
    headerReader = generator.getHeaderReader()
    private = False
    if headerReader.hasPrivate():
      headerPath = tree.getHeaderPath(className, generator.getPartName())
      private = any(
          headerPath.startswith(folder)
          for folder in headerReader.getApartFolders())
    named = self._nameWritten(written)
    #  A class Qt marks nowhere, neither itself nor a class it is
    #  written inside, as 'QOpenGLFunctions_1_0_CoreBackend': Qt's
    #  library offers none of its functions, and code of it in a header
    #  file may call one of them, as its constructor calls 'init()'.
    parts = className.split('::')
    unmarked = not any(
        callExpert.isMarkedForExport('::'.join(parts[:count]))
        for count in range(len(parts), 0, -1))
    if not private and not unmarked and not any(
        name in named for name in chosen):
      #  No ritual calls a function whose code would be taken, so
      #  there is nothing to compile for: every ritual calls what Qt's
      #  source marks or what a header has the code of.
      return
    helpers = dict()  # type: Dict[str, Record]
    lost = set()  # type: Set[str]
    marker = '//  ' + '-' * 71
    #  What the code of each ritual leans on, by the name of the ritual,
    #  as the last round found it.
    reachedBy = dict()  # type: Dict[str, Set[str]]

    def drop(plan: Record, reason: str) -> None:
      written.remove(plan)
      if self.isOursOnly(plan['kind']):
        #  A ritual of ours, as the one running just Qt's own function:
        #  no function of the header by itself, so kept apart.
        self.__unwritten_extras__.append((plan['function'], reason))
      else:
        unwritten.append((plan['function'], reason))

    for _ in range(60):
      #  One round: write the file as it would be, compile it, look at
      #  what each ritual leans on. A round that changes nothing is
      #  the last.
      named = self._nameWritten(written)
      taken = [*helpers.items()]
      taken.extend(
          (name, definition) for name, definition in chosen.items()
          if name in named and name not in helpers)
      compiled = {*helpers}
      self._keepSource(taken, lost, marker)
      text = generator.getRitualTextOf(written, unwritten)
      refused, leans, wanted = probeExpert.probeText(text)
      lines = text.split('\n')
      changed = False
      if refused:
        #  Which line belongs to what: a line pulling a file in, a
        #  definition taken from Qt's source, or a ritual.
        starts = []  # type: List[Tuple[int, str]]
        for number, line in enumerate(lines, 1):
          match = re.match(r'//  from (\S+), line \d+, as (\S+)$', line)
          if match is not None:
            starts.append((number, match.group(2)))
        ends = lines.index(marker) + 1 if marker in lines else 0
        for lineNumber, said in sorted(refused.items()):
          line = ''
          if 0 < lineNumber <= len(lines):
            line = lines[lineNumber - 1]
          pulled = self.__source_includes__
          squeezed = ''.join(line.split())
          if squeezed.startswith('#include') and line in pulled:
            lost.add(line)
            changed = True
            continue
          owner = None  # type: Optional[str]
          if lineNumber <= ends:
            for number, name in starts:
              if number <= lineNumber:
                owner = name
          if owner is None:
            continue
          if owner.startswith('local:'):
            #  A thing of a '.cpp' file taken along that leans on another
            #  thing of a file takes that along too, as code taken from
            #  Qt's source does; one that does not compile here even so
            #  goes again, and what needed it with it.
            local = next((
                one for key, one in self.__file_locals__ if key == owner),
                None)
            if local is not None and self._mendCopy(local, said, lost):
              changed = True
              continue
            self.__file_locals__ = [
                (key, local) for key, local in self.__file_locals__
                if key != owner]
            lost.add(owner)
            changed = True
            continue
          definition = helpers.get(owner) or chosen.get(owner)
          if definition is not None and self._mendCopy(
              definition, said, lost):
            changed = True
            continue
          infoSpec = """Qt's library has no name for it, and its code in
          Qt's source does not compile apart from its file: %s"""
          reason = ' '.join((infoSpec % said).split())
          if owner in helpers:
            del helpers[owner]
            lost.add(owner)
            changed = True
          elif owner in chosen:
            for plan in [*written]:
              if plan.get('ritualName', '')[len('ritual'):] == owner:
                drop(plan, reason)
            del chosen[owner]
            changed = True
        if not changed:
          #  A header file of Qt that does not stand alone, as
          #  'qdbusthreaddebug_p.h', names a class it leaves to the
          #  file pulling it in to declare. Qt's own '.cpp' files pull
          #  the header file of that class in first; so does this one.
          unknown = re.compile(
              r"(?:unknown type name|incomplete type|undeclared "
              r"identifier) '([A-Za-z_][\w:]*)'")
          for said in refused.values():
            for name in unknown.findall(said):
              if self._canPull(name) and (
                  name not in self.__pulled_first__):
                self.__pulled_first__ = (*self.__pulled_first__, name)
                changed = True
          if changed:
            continue
        if not changed:
          #  A ritual the compiler refuses goes, with what it said: one
          #  ritual never costs the class the others.
          for lineNumber, said in sorted(refused.items()):
            owner = RitualFileExpert.findRitualAt(lines, lineNumber)
            if not owner:
              continue
            infoSpec = """the compiler refuses its ritual as it would be
            written here: %s"""
            reason = ' '.join((infoSpec % said).split())
            for plan in [*written]:
              if plan.get('ritualName') == owner:
                drop(plan, reason)
                changed = True
          if changed:
            continue
        if not changed:
          #  The compiler refuses the file for something that is none
          #  of the code taken along and no ritual. Written like this it
          #  would not compile anywhere, so nothing is written.
          infoSpec = """The compiler refuses the ritual file of '%s' as
          it would be written, for what no code taken from Qt's source
          is to blame: %s"""
          shown = '; '.join(
              'line %d: %s' % pair for pair in sorted(refused.items()))
          info = infoSpec % (className, shown[:600])
          raise RuntimeError(' '.join(info.split()))
        continue
      #  What the code leans on is sorted by Qt's source: a thing Qt
      #  marks for use from outside Qt, and writes so that it can be
      #  called from there, can be called. Of anything else the code
      #  is taken along as well, or the ritual goes. No Qt that is
      #  compiled or installed is asked which names it has.
      shownNames = callExpert.demangle(sorted(
          symbol for symbol in wanted if callExpert.isOfQt(symbol)))
      marked = {
          symbol for symbol, shown in shownNames.items()
          if callExpert.isMarkedName(shown, symbol)
      }
      for plan in [*written]:
        ritualName = plan.get('ritualName')
        if ritualName not in leans:
          continue
        reached, waiting = set(), [ritualName]
        while waiting:
          for other in leans.get(waiting.pop(), ()):
            if other not in reached:
              reached.add(other)
              waiting.append(other)
        reachedBy[ritualName] = reached
        for symbol in sorted(reached):
          if symbol not in wanted:
            continue
          if symbol in marked or not callExpert.isOfQt(symbol):
            continue
          found = None
          if symbol in helpers and symbol not in compiled:
            #  Found for a ritual higher up, in this very round.
            continue
          if symbol in helpers:
            #  Its code was in the file that was compiled, and the name
            #  is still not there: what Qt's source has under it is
            #  another function. It is not taken a second time.
            del helpers[symbol]
            lost.add(symbol)
          elif symbol not in lost:
            found = self._findHelper(symbol)
            if found is None:
              found = self._findLoggingCategory(symbol)
          if found is not None:
            helpers[symbol] = found
            changed = True
            continue
          if symbol not in lost:
            #  A table of virtual functions, or what C++ knows of the
            #  type, of a class Qt keeps to itself: written here, from
            #  copies of the class's virtual functions.
            made = self._findTableMakers(symbol)
            new = {
                name: definition for name, definition in made.items()
                if name not in helpers and name not in lost}
            if new:
              helpers.update(new)
              self.__table_members__[symbol] = (*made,)
              changed = True
              continue
            if made and any(name not in compiled for name in made):
              #  Copied in this very round, for the other of the two
              #  tables of the class: the compiler sees them next round.
              continue
            if made:
              #  Copied in a round before, and the compiler wrote the
              #  table even so nowhere here.
              lost.add(symbol)
          said = subprocess.run(
              (*Machine.getDemangler(), symbol), stdout=subprocess.PIPE,
              universal_newlines=True).stdout.strip()
          infoSpec = """leans on '%s', which Qt's source does not
          mark for use from outside Qt and has no code for that could
          be taken"""
          drop(plan, ' '.join((infoSpec % said).split()))
          changed = True
          break
      if not changed:
        break
    named = self._nameWritten(written)
    taken = [*helpers.items()]
    taken.extend(
        (name, definition) for name, definition in chosen.items()
        if name in named and name not in helpers)
    self._keepSource(taken, lost, marker)
    #  A ritual that calls code taken from Qt's source stands between
    #  the '#if' lines that code stands between in its '.cpp' file as
    #  well: where they do not hold, the code is not there to call.
    copied = dict(taken)
    for plan in written:
      if 'bare' not in plan:
        continue
      leaning = [plan.get('compilerName', '')]
      leaning.extend(sorted(reachedBy.get(plan['ritualName'], ())))
      #  A table written here from copies leans on each of them, under
      #  whichever of its names the compiler calls a destructor.
      for symbol in [*leaning]:
        leaning.extend(self.__table_members__.get(symbol, ()))
      conditions = (*plan['conditions'],)
      for symbol in leaning:
        if symbol not in copied:
          continue
        definition = copied[symbol]
        for condition in self._findCopiedConditions(definition):
          if condition not in conditions:
            conditions = (*conditions, condition)
      if conditions != plan['conditions']:
        plan['conditions'] = conditions
        plan['text'] = ConditionExpert.wrapInConditions(
            plan['bare'], conditions)

  def _findCopiedConditions(self, definition: Record) -> Tuple[str, ...]:
    """
    Gives what the '#if' lines around a definition taken from Qt's
    source ask, as 'SourceReader.getConditions' reads them; and, when
    the code itself has '#if' lines that ask for a system or for a
    processor, as '#ifdef Q_OS_MACOS' in
    'QToolBarLayout::updateMacBorderMetrics()', the system and the
    processor the generator checked it for, as 'defined(Q_OS_LINUX)'.
    Elsewhere those lines let in code the compiler here never saw,
    which may call what Qt's library there does not offer, as that one
    calls 'qt_mainwindow_layout' on macOS.
    """
    found = SourceReader.getConditions(
        definition['path'], definition['line'])
    text = definition['text']
    if self.__system_asked__.search(text):
      found = (*found, self._getCheckedSystem())
    if self.__processor_asked__.search(text):
      found = (*found, self._getCheckedProcessor())
    return found

  def _keepSource(
      self,
      taken: List[Tuple[str, Record]],
      lost: Set[str],
      marker: str,
  ) -> None:
    """Writes the code taken from Qt's source, with its heading, and
    the lines pulling in what it needs, where 'getSourceText' and
    'getSourceIncludes' find them."""
    from . import ConditionExpert
    self.__source_text__, self.__source_includes__ = '', ()
    if not taken:
      return
    tree = self.getGenerator().getDependencyTree()
    folder = tree.getSourceReader().getSourceFolder()
    lines = [
        "//  Qt's own code, from here to the line of dashes: taken from",
        "//  Qt's source, because Qt's library carries it under no name.",
    ]
    #  Where the notice of its licenses goes, once the files the code
    #  comes from are known.
    noticeAt = len(lines)
    #  Qt's literals of text, as u"..."_s and "..."_L1, are found only
    #  where their namespace is taken in, as the files of the code did.
    literals = []  # type: List[str]
    for _, definition in taken:
      for one in definition.get('usings', ()):
        if 'Literals' in one and one not in literals:
          literals.append(one)
    if literals:
      lines.append('')
      lines.extend('using namespace %s;' % one for one in literals)
    #  The things of the '.cpp' files the code needs, before the code,
    #  in the order the files have them.
    locals_ = [
        (key, local) for key, local in self.__file_locals__ or ()
        if key not in lost]
    locals_.sort(key=lambda pair: (pair[1]['path'], pair[1]['line']))
    kept, seen = [], set()  # type: List[str], Set[str]
    #  A definition taken under two names, as a destructor under each
    #  name the compiler has for it, is written once.
    written = set()  # type: Set[Tuple[str, int]]
    for name, definition in [*locals_, *taken]:
      if (definition['path'], definition['line']) in written:
        continue
      written.add((definition['path'], definition['line']))
      where = os.path.relpath(definition['path'], folder)
      lines.append('')
      lines.append('//  from %s, line %d, as %s' % (
          where, definition['line'], name))
      text = definition['text']
      local = name.startswith('local:')
      if local and definition.get('function') and re.search(
          r'\b(?:Q_[A-Z0-9_]*_EXPORT|Q_DECL_EXPORT)\b', text.split('{')[0]):
        #  A function of the file that Qt's library offers, as
        #  'Q_CORE_EXPORT void qt_from_latin1(...)' in 'qstring.cpp': it
        #  is declared, and the library's own is called.
        text = '%s;' % text.split('{')[0].rstrip()
      elif definition.get('function') and not re.search(
          r'\b(?:inline|static)\b', text.split('(')[0]):
        text = 'inline %s' % text
      elif not local and not re.search(r'\binline\b', text.split('(')[0]):
        text = 'inline %s' % text
      if definition.get('anonymous'):
        #  Qt keeps it to its file in a namespace without a name; so
        #  does this file.
        text = '\n'.join(('namespace {', text, '}  // namespace'))
      namespace = definition.get('namespace', '')
      if namespace:
        #  Where Qt's '.cpp' file writes the name short, the copy stands
        #  in the namespace that makes it whole, and takes in what that
        #  file took in, so that its code finds what it names; see
        #  '_placeIn'.
        usedHere = [
            'using namespace %s;' % one
            for one in definition.get('usings', ()) if one != namespace]
        text = '\n'.join((
            'namespace %s {' % namespace, *usedHere, text,
            '}  // namespace %s' % namespace))
      #  Between the '#if' lines it stands between in its '.cpp' file.
      lines.append(ConditionExpert.wrapInConditions(
          text, self._findCopiedConditions(definition)))
      if local or definition['path'] in seen:
        #  A thing of a '.cpp' file comes with code of that file, which
        #  brings the lines pulling in what the file needs.
        continue
      #  The lines of each file once, whole and in their order: an
      #  '#if' among them has its '#endif' among them.
      seen.add(definition['path'])
      #  Each as the part of the '.cpp' file sees it, and only once it
      #  is spelled so can it be told whether the compiler refused it.
      spelled = (
          self._spellInclude(line, definition['path'])
          for line in definition['includes'])
      kept.extend(line for line in spelled if line not in lost)
    lines[noticeAt:noticeAt] = self.writeLicenseNotice(
        *dict.fromkeys(path for path, _ in written))
    lines.append(marker)
    self.__source_text__ = '\n'.join(lines)
    self.__source_includes__ = (*kept,)

  #  The license each file of Qt's source gives, read once for each.
  __file_licenses__ = dict()  # type: Dict[str, str]

  @classmethod
  def findLicense(cls, path: str) -> str:
    """
    Gives the license a file of Qt's source gives in its own SPDX line,
    as 'LicenseRef-Qt-Commercial OR GPL-3.0-only'. A file Qt generates,
    as a D-Bus adaptor, may give none: then the files beside it say it,
    the first of them that gives one, in alphabetical order. Where none
    does, it is 'NOASSERTION', SPDX's own word for a license nobody
    says.
    """
    if path in cls.__file_licenses__:
      return cls.__file_licenses__[path]
    found = cls._readLicense(path)
    if found is None:
      folder = os.path.dirname(path)
      names = sorted(os.listdir(folder)) if os.path.isdir(folder) else []
      for name in names:
        if name.endswith(('.cpp', '.h', '.mm')):
          found = cls._readLicense(os.path.join(folder, name))
          if found is not None:
            break
    cls.__file_licenses__[path] = found or 'NOASSERTION'
    return cls.__file_licenses__[path]

  @staticmethod
  def _readLicense(path: str) -> Optional[str]:
    """Gives what the SPDX line of a file says, or None for a file that
    has no such line among its first lines, or is not there."""
    try:
      with open(path, errors='replace') as file:
        head = [file.readline() for _ in range(40)]
    except OSError:
      return None
    for line in head:
      found = re.search(
          r'SPDX-License-Identifier:\s*(.+?)\s*(?:\*/)?\s*$', line)
      if found:
        return found.group(1)
    return None

  @classmethod
  def writeLicenseNotice(cls, *paths: str) -> List[str]:
    """
    Gives the lines of the notice above code taken from Qt's source:
    that it stays under the license of each file it comes from, and
    each of those licenses once, as the files' own SPDX lines have
    them, in the order the files come.
    """
    licenses = [*dict.fromkeys(cls.findLicense(path) for path in paths)]
    lines = [
        '//  Copyright (C) The Qt Company Ltd. It stays under the license',
        '//  of each file it comes from, as its own SPDX line has it:',
    ]
    for one in licenses:
      words, line = one.split(), '//   '
      for word in words:
        if len(line) + len(word) + 1 > 77:
          lines.append(line)
          line = '//     '
        line = '%s %s' % (line, word)
      lines.append(line)
    lines.extend((
        '//  Each function is as Qt wrote it, with the word',
        "//  'inline' put before it where Qt did not write it.",
    ))
    return lines

  def _spellInclude(self, line: str, sourcePath: str) -> str:
    """
    Gives a line of a '.cpp' file of Qt's source that pulls a header
    file in by a name no part is named in, as '#include
    <private/qaction_p.h>' in QtWidgets' 'qmenu.cpp', with the part
    named that has the file, as the part of the '.cpp' file sees it:
    '#include <QtGui/private/qaction_p.h>'. Qt's own build looks in the
    folders of the part itself and of the parts it needs, the nearest
    first; a ritual file is compiled with the folders of every part,
    where QtWidgets would find Qt3DInput's 'qaction_p.h' first. Any
    other line comes back as it is: one naming its part already, one
    of no header file of the parts it sees, and one that is no
    '#include'.
    """
    match = re.match(
        r'^(\s*#\s*include\s*)[<"]([^>"]+)[>"](.*)$', line)
    if match is None:
      return line
    lead, name, rest = match.groups()
    if re.match(r'^Qt\w*/', name):
      return line
    folder = HeaderReader.getHeaderFolder()
    partName = folder.getPartOfPath(sourcePath)
    if partName is None:
      return line
    made, version = folder.getFolder(), HeaderReader.getQtVersion()
    for seen in HeaderReader.getNeededParts(partName):
      inner = os.path.join(made, seen, version, seen)
      if '/' in name:
        #  As 'private/qaction_p.h' or 'qpa/qplatformwindow.h'.
        candidates = [(os.path.join(inner, name), name)]
      elif name.endswith('_p.h'):
        candidates = [(
            os.path.join(inner, 'private', name), 'private/%s' % name)]
      else:
        candidates = [(os.path.join(made, seen, name), name)]
      for path, spelled in candidates:
        if os.path.isfile(path):
          return '%s<%s/%s>%s' % (lead, seen, spelled, rest)
    return line

  def _findHelper(self, symbol: str) -> Optional[Record]:
    """
    Gives the definition, in Qt's source, of a function known only by
    the name the compiler made for it, or None when the source has not
    exactly one that takes as many arguments.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    source = tree.getSourceReader()
    said = subprocess.run(
        (*Machine.getDemangler(), symbol), stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, universal_newlines=True).stdout.strip()
    if '(' not in said or said == symbol:
      return None
    name = said[:said.index('(')].strip()
    inside = said[said.index('(') + 1:said.rindex(')')]
    count = len(source._splitArguments(inside))
    const = said.rstrip().endswith('const')
    #  The code of a function of a class is in the source of the part
    #  that has the class, as the part of the generator sees it: two
    #  parts may each have a class by one name, as QtGraphs and
    #  QtDataVisualization each a 'QBar3DSeriesPrivate', whose functions
    #  the compiler names alike. Of a function of no class the tree
    #  knows, the part and the parts it needs are looked in, the
    #  nearest first.
    seenFrom = generator.getPartName()
    owner = name.rpartition('::')[0]
    if owner and tree.hasClass(owner, seenFrom):
      partNames = (tree.getClassKey(owner, seenFrom)[0],)
    else:
      partNames = tree.getNeededParts(seenFrom)
    for partName in partNames:
      found = [
          self._placeIn(definition, name) for definition
          in source.findDefinitions(partName, name)
          if len(definition['arguments']) == count
          and definition['const'] == const
      ]
      if len(found) == 1:
        return found[0]
    return None

  def _findTableMakers(self, symbol: str) -> Dict[str, Record]:
    """
    Gives the code, in Qt's source, of each virtual function a class
    declares and writes the code of outside of it, its destructor among
    them, by the name the compiler has for each, for a symbol that is
    the table of the class's virtual functions ('vtable for X') or what
    C++ knows of its type ('typeinfo for X'). The compiler writes both
    into the file with the code of the first of those functions, and
    Qt's library keeps them to itself where Qt does not mark the class
    for use from outside Qt. A file holding a copy of each, made
    'inline', has them written into it as well, the way they are for a
    class without such a function: on Apple's processors the compiler
    takes the next function as that first one when the first has an
    'inline' copy, so a copy of the first alone is not enough. What the
    table names beside these, as the functions of a class it is made
    from, is taken along as any code is, or the ritual goes.

    Empty for a symbol that is no such table, for a class of a template
    and one the tree has no record of, and where Qt's source has no code
    of the first of those functions, as of 'metaObject()' of a class
    with 'Q_OBJECT', which Qt's moc writes.
    """
    said = subprocess.run(
        (*Machine.getDemangler(), symbol), stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, universal_newlines=True).stdout.strip()
    match = re.fullmatch(
        r'(?:vtable|typeinfo|typeinfo name|VTT) for ([\w:]+)', said)
    if match is None:
      return dict()
    owner = match.group(1)
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    if not tree.hasClass(owner, generator.getPartName()):
      return dict()
    record = generator._readRecord(owner)
    found = dict()  # type: Dict[str, Record]
    for member in record.get('inner', ()):
      kind = member.get('kind')
      if kind not in ('CXXMethodDecl', 'CXXDestructorDecl'):
        continue
      if 'mangledName' not in member or member.get('isImplicit'):
        continue
      if member.get('pure') or member.get('inline'):
        continue
      if member.get('explicitlyDefaulted') or member.get(
          'explicitlyDeleted') or member.get('constexpr'):
        continue
      marks = [
          child.get('kind') for child in member.get('inner', ())
          if isinstance(child, dict)]
      if 'CompoundStmt' in marks:
        #  Its code is written in the class.
        continue
      #  A destructor is virtual where that of a class it is made from
      #  is, which its record does not say; one that is not is copied
      #  as well, and is code like any other.
      if kind == 'CXXMethodDecl' and not member.get('virtual') and (
          'OverrideAttr' not in marks):
        continue
      definition = self.findSourceCode(member, owner)
      if definition is None:
        if not found:
          #  The first: without its code the table is written nowhere.
          return dict()
        continue
      found[member['mangledName']] = definition
    return found

  def _mendCopy(self, definition: Record, said: str, lost: Set[str]) -> bool:
    """
    Mends code taken from Qt's source that the compiler refused for a
    thing it does not see, as "use of undeclared identifier 'X'": a
    class the tree knows has its header file pulled in first; a thing
    of the '.cpp' file the code was taken from is taken along, as
    '_findFileLocal' finds it. Says whether it took anything new; the
    code is dropped where it did not.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    className, partName = generator.getClassName(), generator.getPartName()
    for name in self.__needs_said__.findall(said):
      if self._canPull(name):
        if name not in self.__pulled_first__:
          self.__pulled_first__ = (*self.__pulled_first__, name)
          return True
        continue
      key = 'local:%s:%s' % (
          os.path.basename(definition['path']), name.split('::')[-1])
      if key in lost or any(one == key for one, _ in self.__file_locals__):
        continue
      found = self._findFileLocal(definition['path'], name.split('::')[-1])
      if found is not None:
        self.__file_locals__.append((key, found))
        if not found['function']:
          #  A type of the file whose functions the file defines apart,
          #  as 'NumericTokenizer::nextToken' in 'qlocale.cpp': they
          #  come with it, or the library made would lack them.
          for member in self._findFileMembers(
              definition['path'], name.split('::')[-1]):
            memberKey = 'local:%s:%s' % (
                os.path.basename(definition['path']), member['name'])
            if memberKey in lost or any(
                one == memberKey for one, _ in self.__file_locals__):
              continue
            self.__file_locals__.append((memberKey, member))
        return True
    return False

  def _canPull(self, name: str) -> bool:
    """
    Says whether the header file of a class the compiler did not see
    may be pulled in first: a class of the tree other than the class
    itself, of its part or of a part that part needs, as Qt's own
    '.cpp' files of the part can pull in, and in a header file Qt
    installs on every system: under no condition, or under Qt's own
    features alone, as 'qquickgraphsitem_p.h' under
    'QT_CONFIG(graphs_3d)', which the ritual file then pulls in as
    plainly as Qt's '.cpp' files do; see 'RitualFileExpert'. Another
    part may hold a class of that name whose header file must never
    stand beside the part's own, as QtCharts beside QtGraphs; and a
    header file installed for one system only, as
    'qquick3dxrinputmanager_visionos_p.h', is not there on the others.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    className, partName = generator.getClassName(), generator.getPartName()
    if name == className or not tree.hasClass(name, partName):
      return False
    if tree.getPartName(name, partName) not in tree.getNeededParts(partName):
      return False
    folder = HeaderReader.getHeaderFolder()
    path = tree.getHeaderPath(name, partName)
    installed = folder.getInstallCondition(path)
    if installed is None:
      #  A condition no compiler knows, or a file of no part.
      return False
    #  What is left of the condition without Qt's features: nothing but
    #  the signs joining them for one that asks for features alone.
    rest = re.sub(r'QT_CONFIG\(\w+\)', '', installed)
    return True if re.fullmatch(r'[\s()!&|]*', rest) else False

  def _findFileMembers(self, path: str, typeName: str) -> List[Record]:
    """Gives the functions of a type of a '.cpp' file that the file
    defines outside of the type, as 'char NumericTokenizer::nextToken()'
    in 'qlocale.cpp', as '_readFileItems' reads them, each with 'name',
    as 'NumericTokenizer::nextToken', and as a function."""
    found = []  # type: List[Record]
    owned = re.compile(
        r'\b%s\s*::\s*(~?\s*[A-Za-z_]\w*|operator\s*[^\s(]+)\s*\('
        % re.escape(typeName))
    for item in self._readFileItems(path):
      squeezed = ' '.join(item['text'].split())
      if squeezed.startswith('#') or '{' not in squeezed:
        continue
      match = owned.search(squeezed.split('{')[0])
      if match is not None:
        member = ''.join(match.group(1).split())
        found.append(dict(
            item, function=True, name='%s::%s' % (typeName, member)))
    return found

  @classmethod
  def _readFileItems(cls, path: str) -> List[Record]:
    """
    Gives the things a '.cpp' file writes at its top, outside every
    function, class and other pair of curly brackets but those of a
    namespace: each declaration or definition up to the ';' or the '}'
    that ends it, and each '#define' line with its continuations; each
    with 'text', 'line' (the first being 1), 'namespace' (the full name
    of the namespace it stands in), 'anonymous' (whether it stands in a
    namespace without a name), 'usings' and 'path'. Read once.
    """
    if path in cls.__file_items__:
      return cls.__file_items__[path]
    with open(path, errors='replace') as file:
      text = file.read()
    blank = SourceReader.__no_code__.sub(
        lambda found: re.sub(r'[^\n]', ' ', found.group(0)), text)
    scopes = SourceReader.findScopes(text)
    starts = [0]
    for line in text.split('\n'):
      starts.append(starts[-1] + len(line) + 1)

    def lineOf(place: int) -> int:
      low, high = 0, len(starts) - 1
      while low < high:
        middle = (low + high + 1) // 2
        if starts[middle] <= place:
          low = middle
        else:
          high = middle - 1
      return low + 1

    items = []  # type: List[Record]
    #  Each open pair of curly brackets: 'space' for a namespace, with
    #  or without a name, and for 'extern "C" {'; 'other' for any other.
    opened = []  # type: List[str]
    mark = re.compile(
        r'\bnamespace(?:\s+[A-Za-z_][\w:]*)?\s*\{|\bextern\s+"C"\s*\{'
        r'|^[ \t]*#[ \t]*define\b[^\n]*(?:\\\n[^\n]*)*|[{};]', re.M)
    start = 0

    def keep(end: int, anonymous: bool) -> None:
      #  Lines pulling files in, '#if' lines, comments, the lines
      #  opening Qt's namespace and those of Qt's words to the compiler
      #  about warnings before the thing belong to no thing, as the
      #  heading of the file and its '#include' lines before the first
      #  thing; they are read with the comments blanked.
      lines = text[start:end].split('\n')
      blanks = blank[start:end].split('\n')
      first = start
      while lines and (
          not blanks[0].strip() or blanks[0].lstrip().startswith('#')
          or cls.__no_thing__.fullmatch(blanks[0])):
        first += len(lines.pop(0)) + 1
        blanks.pop(0)
      piece = '\n'.join(lines).strip()
      if not piece:
        return
      first += len('\n'.join(lines)) - len('\n'.join(lines).lstrip())
      items.append(dict(
          text=piece, line=lineOf(first), path=path, anonymous=anonymous,
          namespace=cls._namespaceAt(scopes, first),
          usings=(*(name for at, till, name in scopes[1]
                    if at <= first < till),)))

    for found in mark.finditer(blank):
      token = found.group(0)
      atTop = all(kind == 'space' for kind, _ in opened)
      anonymous = any(name == '' for kind, name in opened if kind == 'space')
      if token.lstrip().startswith('#'):
        if atTop and re.match(r'\s*#\s*define\b', token):
          piece = text[found.start():found.end()].strip()
          items.append(dict(
              text=piece, line=lineOf(found.start()), path=path,
              anonymous=False, namespace='', usings=()))
        if atTop:
          start = found.end()
        continue
      if token.endswith('{') and token != '{':
        if atTop:
          start = found.end()
        named = re.match(r'namespace\s+([A-Za-z_][\w:]*)', token)
        opened.append(('space', named.group(1) if named else ''))
        continue
      if token == '{':
        opened.append(('other', ''))
        continue
      if token == '}':
        if not opened:
          continue
        kind, _ = opened.pop()
        if kind == 'space':
          start = found.end()
          continue
        if all(one == 'space' for one, _ in opened):
          #  The end of a function, or of a class or enum ended by ';'.
          after = blank[found.end():found.end() + 200].lstrip()
          if not after.startswith(';'):
            keep(found.end(), anonymous)
            start = found.end()
        continue
      if token == ';' and atTop:
        keep(found.end(), anonymous)
        start = found.end()
    cls.__file_items__[path] = items
    return items

  @staticmethod
  def _namespaceAt(scopes: Any, place: int) -> str:
    """Gives the full name of the innermost namespace around a place of
    a file, as 'SourceReader.findScopes' found them, or ''."""
    inner = ''
    for start, end, name in scopes[0]:
      if start <= place < end and len(name) > len(inner):
        inner = name
    return inner

  def _findFileLocal(self, path: str, name: str) -> Optional[Record]:
    """
    Gives the thing of a '.cpp' file of a name, as '_readFileItems'
    reads them, that code taken from the file needs: a function, a
    constant, a type, an enum or one of its values, a second name for a
    type, or a '#define'. None for none, and for data that may change,
    as 'static QBasicMutex mutex;' or 'Q_GLOBAL_STATIC(...)': a copy of
    it would be another, and Qt's code would never see what the copy
    holds. 'function' says whether it is a function.
    """
    word = re.escape(name)
    for item in self._readFileItems(path):
      text = item['text']
      #  A thing whose '#if' lines do not pair up inside it, as one that
      #  stands across an '#else' of the file, is not taken: alone it
      #  would leave the ritual file's own '#if' lines open.
      opened = len(re.findall(r'^\s*#\s*if', text, re.M))
      if opened != len(re.findall(r'^\s*#\s*endif', text, re.M)):
        continue
      squeezed = ' '.join(text.split())
      if squeezed.startswith('#'):
        if re.match(r'#\s*define\s+%s\b' % word, squeezed):
          return dict(item, function=False)
        continue
      head = squeezed.split('{')[0]
      if re.search(r'\bQ_GLOBAL_STATIC\w*\s*\(', squeezed):
        if re.search(r'\b%s\b' % word, head):
          return None
        continue
      if re.search(
          r'\b(?:struct|class|union|enum(?:\s+class)?)\s+%s\b' % word, head):
        return dict(item, function=False)
      named = r'\b(?:using\s+%s\s*=|typedef\b.*\b%s\s*;)' % (word, word)
      if re.search(named, squeezed):
        return dict(item, function=False)
      if head.startswith('enum') and re.search(r'\b%s\b' % word, squeezed):
        return dict(item, function=False)
      #  A function of the file, not one of a class ('QFoo::bar(').
      called = re.search(r'(?:^|[\s*&>])%s\s*\(' % word, head)
      if called is not None and '{' in squeezed and '=' not in (
          head[:called.start()]):
        return dict(item, function=True)
      if called is not None:
        continue
      declared = head + ('{' if '{' in squeezed else '')
      if re.search(r'\b%s\s*(?:\[[^\]]*\]\s*)*(?:=|\{|;)' % word, declared):
        if re.search(r'\b(?:const|constexpr)\b', head):
          return dict(item, function=False)
        return None
    return None

  def _findLoggingCategory(self, symbol: str) -> Optional[Record]:
    """
    Gives the code of a logging category of Qt that Qt's library has no
    name for, as 'lcQpaWindow()': a function Qt writes through
    'Q_LOGGING_CATEGORY', found in the source of the part and of the
    parts it needs, written out as that writes it, 'inline'. A copy of a
    category is another object of the same name, and the rules of what
    is shown go by the name, so it shows what Qt's own would.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    source = tree.getSourceReader()
    said = subprocess.run(
        (*Machine.getDemangler(), symbol), stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, universal_newlines=True).stdout.strip()
    match = re.fullmatch(r'(?:([\w:]+)::)?(\w+)\(\)', said)
    if match is None:
      return None
    owner, name = match.group(1) or '', match.group(2)
    made = re.compile(
        r'\bQ_(?:STATIC_)?LOGGING_CATEGORY\s*\(\s*%s\s*,([^;]*?)\)\s*$'
        % re.escape(name), re.M)
    for partName in tree.getNeededParts(generator.getPartName()):
      for path in source.getSourceFiles(partName):
        with open(path, errors='replace') as file:
          text = file.read()
        if name not in text:
          continue
        found = made.search(text)
        if found is None:
          continue
        scopes = SourceReader.findScopes(text)
        namespace = self._namespaceAt(scopes, found.start())
        if owner and namespace != owner:
          continue
        code = '\n'.join((
            'inline const QLoggingCategory &%s()' % name, '{',
            '    static const QLoggingCategory category(%s);' % (
                found.group(1).strip()),
            '    return category;', '}'))
        return dict(
            name=name, path=path,
            line=text.count('\n', 0, found.start()) + 1,
            text=code, arguments=[], const=False, namespace=namespace,
            usings=(), names=(name,),
            includes=('#include <QtCore/qloggingcategory.h>',))
    return None
