"""Exorcist drives the rituals the compiler or the linker refused out of
one ritual file, and leaves every other ritual of it."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  #  An item of a ritual file: its kind, its name, its first and its
  #  last line, the lines counted from 1.
  Item = Tuple[str, str, int, int]
  #  What a linker said of one object file: the function or data that
  #  needs the symbol (None when the linker does not say), the symbol,
  #  and 'undefined' or 'duplicate'.
  Blame = Tuple[Optional[str], str, str]


class Exorcist:
  """
  Reads one ritual file into its items, finds the items a refusal of the
  compiler or of the linker points at, and gives the text of the file
  without them, so that a ritual that fails here is left out of the
  target file and every other ritual of the file stays in it.

    exorcist = Exorcist()
    exorcist.setRitualFile('/here/QtGuiRituals/q_xbm_handler.cpp')
    if not exorcist.blameCompiler(said, '/here/q_xbm_handler.cpp'):
      exorcist.dropWhole('nothing of the file holds the error')
    copyText = exorcist.getCopyText()

  Terms
  -----

  - An item is a part of a ritual file that can go without breaking the
    rest of the text: a ritual; one piece of code taken from Qt's
    source, from its line '//  from ...' to the next such line; the
    Cute class, from 'class Cute...' to its '};'; one function of the
    Cute class, from its comment to its closing brace; one 'typedef' of
    a function the Cute class takes from Python; one '#include' line.
  - To drop an item is to blank its lines in the copy. The lines of
    '#if', '#ifdef', '#ifndef', '#elif', '#else' and '#endif' stay, and
    so do 'QT_BEGIN_NAMESPACE' and 'QT_END_NAMESPACE', so the copy has
    the same conditions and namespaces as the file whatever is dropped.
  - The copy keeps the line numbers of the ritual file: a dropped line
    is an empty line. What the compiler says of the copy is read against
    the items of the ritual file directly.

  You provide
  -----------

  - 'setRitualFile': the ritual file to read.
  - What the compiler or the linker said, through 'blameCompiler' or
    'blameLinker', as many times as it takes: each drops the items it
    points at and says whether it found one not dropped before.

  What to expect
  --------------

  - An error the compiler finds in a header is blamed on the
    '#include' line of the ritual file it came in by, unless a note of
    the compiler names a line of the ritual file that asked for the
    code that failed, as a template used there. So the compiler is to
    be told '-ftemplate-backtrace-limit=0': it otherwise names at most
    ten of the places a template was asked for, and may stop before the
    ritual file.
  - An '#include' line before the first '#if' of the file, or one of a
    header whose name holds 'global' or 'config', is never dropped:
    those say what the system and Qt have, as 'Q_OS_WIN' and
    'QT_CONFIG', and without them the conditions of the file would hide
    rituals without a word. An error blamed on one is blamed on no item.
  - Dropping a piece of Qt's code or the Cute class leaves out no ritual
    at once. The rituals that need it fail when the copy is compiled or
    linked next, and are dropped then. So the rituals left out are
    exactly those that cannot be made here.
  - 'getLeftOut' gives each ritual left out with the function it calls
    and what the compiler or the linker said. Only rituals are left out
    for Python: a dropped '#include' or piece of Qt's code costs Python
    nothing by itself.
  - 'dropWhole' is the last resort, for a refusal no item holds: the
    copy is then empty, and every ritual of the file is left out.
  - 'getRecord' and 'setRecord' keep what was dropped from one build of
    the target file to the next, as JSON.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _getBaseName(path: str) -> str:
    """Gives the last part of a path, split at '/' and at '\\' alike,
    since a compiler on Windows names its files with either."""
    return re.split(r'[\\/]', path.strip())[-1]

  @staticmethod
  def _isKept(line: str) -> bool:
    """Says whether a line stays in the copy when its item is dropped:
    a line of a condition, or of Qt's namespace."""
    if re.match(r'^\s*#\s*(?:if|ifdef|ifndef|elif|else|endif)\b', line):
      return True
    return line.strip() in ('QT_BEGIN_NAMESPACE', 'QT_END_NAMESPACE')

  @staticmethod
  def readCompilerErrors(said: str) -> List[Dict[str, Any]]:
    """
    Reads what 'clang++' said into its errors.

    Returns
    -------

    List[Dict[str, Any]]
      One dict for each error, in the order said: 'path', 'line' and
      'text' of the error; 'included', the '(path, line)' of each line
      'In file included from' before it; 'notes', the '(path, line)' of
      each note after it; 'instantiated', whether a note says the error
      is in a template, where it was worked out for some type.
    """
    location = re.compile(
        r'^(?P<path>.+?):(?P<line>\d+):(?P<column>\d+): '
        r'(?P<kind>fatal error|error|warning|note|remark): (?P<text>.*)$')
    included = re.compile(
        r'^In file included from (?P<path>.+?):(?P<line>\d+)[:,]$')
    errors = []
    pending = []
    current = None
    for line in said.splitlines():
      line = line.rstrip()
      match = included.match(line)
      if match:
        pending.append((match.group('path'), int(match.group('line'))))
        continue
      match = location.match(line)
      if match is None:
        continue
      kind = match.group('kind')
      if kind in ('error', 'fatal error'):
        current = dict(
            path=match.group('path'), line=int(match.group('line')),
            text='%s:%s:%s: %s: %s' % (
                Exorcist._getBaseName(match.group('path')),
                match.group('line'), match.group('column'), kind,
                match.group('text')),
            included=pending, notes=[], instantiated=False)
        errors.append(current)
      elif kind == 'note' and current is not None:
        current['notes'].append(
            (match.group('path'), int(match.group('line'))))
        if re.search(r'instantiation|requested here|substitut|deduction',
                     match.group('text')):
          current['instantiated'] = True
      else:
        current = None
      pending = []
    return errors

  @staticmethod
  def readLinkerRefusal(said: str) -> List[Tuple[str, Blame]]:
    """
    Reads what a linker said into what it missed or found twice, and in
    which object file. It reads GNU's 'ld', LLVM's 'ld.lld' and
    'lld-link', Apple's 'ld' and Microsoft's 'link.exe'.

    Returns
    -------

    List[Tuple[str, Blame]]
      For each refusal, the name of the object file, as 'q_foo.o', and
      what needs what: the function or data that needs the symbol, or
      None where the linker does not say; the symbol; and 'undefined'
      or 'duplicate'.
    """
    found = []
    base = Exorcist._getBaseName
    objectFile = r'(?P<object>(?:[A-Za-z]:)?[^\s:()]+\.o(?:bj)?)'
    gnuWhere = re.compile(r'%s: in function [`\'"](?P<ref>.+)[\'"]:$' % (
        objectFile,))
    gnuData = re.compile(
        r'%s:\((?P<section>[^)]*)\): undefined reference' % objectFile)
    gnuSymbol = re.compile(
        r'undefined reference to [`\'"](?P<symbol>.+)[\'"]$')
    gnuTwice = re.compile(
        r'multiple definition of [`\'"](?P<symbol>.+?)[\'"];')
    lldSymbol = re.compile(
        r'(?:ld\.lld|ld64\.lld|lld-link|lld)(?:\.exe)?: error: '
        r'(?P<what>undefined|duplicate) symbol: (?P<symbol>.+)$')
    lldWhere = re.compile(
        r'^>>>\s+(?:referenced by\s+)?%s:\((?P<ref>.+)\)$' % objectFile)
    appleSymbol = re.compile(
        r'^\s+"?(?P<symbol>.+?)"?, referenced from:$')
    appleWhere = re.compile(r'^\s+(?P<ref>.+?) in %s$' % objectFile)
    appleTwice = re.compile(r"^\s*duplicate symbol '(?P<symbol>.+)' in:$")
    appleObject = re.compile(r'^\s+(?P<object>\S+\.o)$')
    msvcUndefined = re.compile(
        r'^%s : error LNK20(?:19|01): unresolved external symbol '
        r'(?P<symbol>.+?)(?: referenced in function (?P<ref>.+))?$' % (
            objectFile,))
    msvcTwice = re.compile(
        r'^%s : error LNK2005: (?P<symbol>.+?) already defined in ' % (
            objectFile,))
    where = None  # type: Optional[Tuple[str, str]]
    symbol, what = None, 'undefined'
    for line in said.splitlines():
      line = line.rstrip()
      match = msvcUndefined.match(line)
      if match:
        found.append((base(match.group('object')), (
            match.group('ref'), match.group('symbol'), 'undefined')))
        continue
      match = msvcTwice.match(line)
      if match:
        found.append((base(match.group('object')), (
            None, match.group('symbol'), 'duplicate')))
        continue
      match = lldSymbol.search(line)
      if match:
        symbol, what = match.group('symbol'), match.group('what')
        continue
      match = lldWhere.match(line)
      if match and symbol is not None:
        found.append((base(match.group('object')), (
            match.group('ref'), symbol, what)))
        if what == 'duplicate':
          symbol = None
        continue
      if line.startswith(('Undefined symbols for architecture',
                          'ld: Undefined symbols')):
        symbol, what = None, 'undefined'
        continue
      match = appleSymbol.match(line)
      if match:
        symbol, what = match.group('symbol'), 'undefined'
        continue
      match = appleTwice.match(line)
      if match:
        symbol, what = match.group('symbol'), 'duplicate'
        continue
      match = appleWhere.match(line)
      if match and symbol is not None and what == 'undefined':
        found.append((base(match.group('object')), (
            match.group('ref'), symbol, 'undefined')))
        continue
      match = appleObject.match(line)
      if match and symbol is not None and what == 'duplicate':
        found.append((base(match.group('object')), (None, symbol, what)))
        symbol = None
        continue
      match = gnuWhere.search(line)
      if match:
        where = (base(match.group('object')), match.group('ref'))
      match = gnuData.search(line)
      symbolMatch = gnuSymbol.search(line)
      if match and symbolMatch:
        found.append((base(match.group('object')), (
            match.group('section'), symbolMatch.group('symbol'),
            'undefined')))
        continue
      if symbolMatch and where is not None:
        found.append((where[0], (
            where[1], symbolMatch.group('symbol'), 'undefined')))
        continue
      match = gnuTwice.search(line)
      if match and where is not None:
        found.append((where[0], (where[1], match.group('symbol'),
                                 'duplicate')))
    return found

  @staticmethod
  def _readQualifiedName(said: str) -> Optional[str]:
    """
    Gives the qualified name a linker gives a function or a class, as
    'QFoo::helper' of 'QFoo::helper(int) const', of the MSVC way
    '"public: void __cdecl QFoo::helper(int)" (?helper@QFoo@@...)', or
    of the mangled '_ZN4QFoo6helperEi'. None when it cannot tell.
    """
    said = said.strip()
    quoted = re.match(r'^"([^"]+)"', said)
    if quoted:
      said = quoted.group(1)
    stripped = said.lstrip('_')
    if re.match(r'^Z(?:N[rVKRO]*)?\d', stripped):
      #  A mangled name of the Itanium way: the names it is nested in,
      #  each its length and its letters, read up to what follows them.
      names, rest = [], stripped[1:]
      if rest.startswith('N'):
        rest = rest[1:].lstrip('rVKRO')
      while True:
        number = re.match(r'^(\d+)', rest)
        if number is None:
          break
        length = int(number.group(1))
        start = len(number.group(1))
        names.append(rest[start:start + length])
        rest = rest[start + length:]
      return '::'.join(names) if names else None
    for thunk in ('non-virtual thunk to ', 'virtual thunk to ',
                  'covariant return thunk to '):
      if said.startswith(thunk):
        said = said[len(thunk):]
    depth, head = 0, ''
    for letter in said:
      if letter == '<':
        depth += 1
      elif letter == '>':
        depth -= 1
      elif letter == '(' and depth == 0:
        break
      head += letter
    words = head.replace('*', ' ').replace('&', ' ').split()
    return words[-1] if words else None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables

  #  Private Variables
  __ritual_file__ = None
  #  The lines of the ritual file, without their line endings.
  __file_lines__ = None
  #  The items of the ritual file, in the order they begin.
  __file_items__ = None
  #  For each line, counted from 1, the innermost item it is in.
  __line_items__ = None
  #  The name of the Cute class of the file, if it has one.
  __cute_name__ = None
  #  The function each ritual calls, as its comment says it.
  __ritual_functions__ = None
  #  The items dropped, each with why, in the order they were dropped.
  __dropped_items__ = None
  #  The '#include' items that are never dropped; see 'What to expect'.
  __fixed_items__ = None
  #  Why the whole file is dropped, once it is.
  __whole_reason__ = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getRitualFile(self) -> str:
    """
    Gives the ritual file this Exorcist reads. Provided by you, through
    'setRitualFile'.

    Raises
    ------

    MissingVariable
      'setRitualFile' has not been called.
    """
    if self.__ritual_file__ is None:
      raise MissingVariable(self, '__ritual_file__', str)
    return self.__ritual_file__

  def getItems(self) -> Tuple[Item, ...]:
    """
    Gives the items of the ritual file, in the order they begin: each
    as '(kind, name, first line, last line)', the lines counted from 1.
    The kinds are 'include', 'copied', 'typedef', 'cute class', 'cute
    function' and 'ritual'.

    Raises
    ------

    MissingVariable
      'setRitualFile' has not been called.
    """
    self.getRitualFile()
    return self.__file_items__

  def getItemAt(self, line: int) -> Optional[Item]:
    """Gives the innermost item a line of the ritual file is in, the
    lines counted from 1, or None for a line of no item."""
    self.getRitualFile()
    if 0 < line < len(self.__line_items__):
      return self.__line_items__[line]
    return None

  def getDropped(self) -> Dict[Item, str]:
    """Gives each item dropped, with why, in the order they were
    dropped."""
    return dict(self.__dropped_items__ or {})

  def getWholeReason(self) -> Optional[str]:
    """Gives why the whole file is dropped, or None while it is not."""
    return self.__whole_reason__

  def getLeftOut(self) -> Dict[str, Tuple[str, str]]:
    """
    Gives each ritual left out: its name, with the function it calls,
    as the comment above it says it, and why it is left out. When the
    whole file is dropped, that is every ritual of it.
    """
    functions = self.__ritual_functions__ or {}
    if self.__whole_reason__ is not None:
      return {
          name: (functions.get(name, name), self.__whole_reason__)
          for kind, name, first, last in self.getItems()
          if kind == 'ritual'}
    return {
        name: (functions.get(name, name), reason)
        for (kind, name, first, last), reason in self.getDropped().items()
        if kind == 'ritual'}

  def getCopyText(self, *trial: Item) -> str:
    """
    Gives the text of the ritual file without what is dropped: each line
    of a dropped item empty, but for the lines '_isKept' keeps. With the
    whole file dropped, every line is empty, and the copy compiles to
    nothing. The items given are left out as well, for a trial, and are
    not dropped by it.
    """
    lines = list(self.__file_lines__)
    if self.__whole_reason__ is not None:
      return '\n' * (len(lines) - 1)
    for kind, name, first, last in (*self.getDropped(), *trial):
      for number in range(first, last + 1):
        if not self._isKept(lines[number - 1]):
          lines[number - 1] = ''
    return '\n'.join(lines)

  def getCandidates(self, wide: bool = False) -> Tuple[Item, ...]:
    """
    Gives the items not dropped that a trial may leave out to find what
    an error no line is blamed for comes from: the rituals and the
    functions of the Cute class, in the order of the file; with 'wide',
    then also the Cute class, the pieces of Qt's code and the
    '#include' lines that may go.
    """
    kinds = ('ritual', 'cute function')
    if wide:
      kinds = (*kinds, 'cute class', 'copied', 'include')
    return (*(
        item for kind in kinds for item in self.getItems()
        if item[0] == kind and not self._isDropped(item)
        and item not in self.__fixed_items__),)

  def getRecord(self) -> Dict[str, Any]:
    """Gives what is dropped, as 'setRecord' takes it back: plain lists
    and text, to be kept as JSON."""
    return dict(
        dropped=[[kind, name, first, last, reason] for (
            kind, name, first, last), reason in self.getDropped().items()],
        whole=self.__whole_reason__,
        leftOut={name: [function, reason] for name, (
            function, reason) in self.getLeftOut().items()},
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setRitualFile(self, ritualFile: str) -> None:
    """
    Tells this Exorcist which ritual file to read, and reads it. Nothing
    is dropped yet.

    Raises
    ------

    TypeException
      The path is not a 'str'.

    FileNotFoundError
      There is no file at the path.
    """
    if not isinstance(ritualFile, str):
      raise TypeException('ritualFile', ritualFile, str)
    if not os.path.isfile(ritualFile):
      infoSpec = """There is no ritual file at '%s'."""
      raise FileNotFoundError(infoSpec % ritualFile)
    with open(ritualFile, encoding='utf-8') as file:
      text = file.read()
    self.__ritual_file__ = ritualFile
    self.__file_lines__ = (*text.split('\n'),)
    self.__dropped_items__ = dict()
    self.__whole_reason__ = None
    self._readItems()

  def setRecord(self, record: Dict[str, Any]) -> None:
    """
    Drops again what 'getRecord' gave, from an earlier build of the same
    ritual file, unchanged since.

    Raises
    ------

    ValueError
      An item of the record is not an item of the ritual file as it is
      now.
    """
    items = set(self.getItems())
    for kind, name, first, last, reason in record.get('dropped', ()):
      item = (kind, name, first, last)
      if item not in items:
        infoSpec = """The record of '%s' drops the %s '%s' of lines %d to
        %d, which the ritual file does not hold as it is now."""
        info = infoSpec % (self.getRitualFile(), kind, name, first, last)
        raise ValueError(' '.join(info.split()))
      self.__dropped_items__[item] = reason
    self.__whole_reason__ = record.get('whole', None)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _readItems(self) -> None:
    """Reads the items of the ritual file, and which item each line is
    in. The markers are those every ritual file has, as the generator
    writes them and the files written by hand follow."""
    lines = self.__file_lines__
    count = len(lines)
    items = []
    functions = dict()
    #  The rituals: each 'extern "C" Q_DECL_EXPORT' with the comment
    #  lines right above it, to the first '}' at the start of a line.
    ritualStarts = []
    for at, line in enumerate(lines, 1):
      if line.strip() != 'extern "C" Q_DECL_EXPORT':
        continue
      first = at
      while first > 1 and lines[first - 2].startswith('//  ') and not (
          lines[first - 2].startswith('//  from ')
          or re.match(r'^//  -{10,}', lines[first - 2])):
        first -= 1
      last = next((n for n in range(at + 1, count + 1)
                   if lines[n - 1].rstrip() == '}'), None)
      if last is None:
        continue
      head = ' '.join(lines[at:last])
      named = re.search(r'\b(ritual_\w+)\s*\(', head)
      if named is None:
        continue
      items.append(('ritual', named.group(1), first, last))
      ritualStarts.append(first)
      comment = ' '.join(lines[n - 1][2:].strip() for n in range(first, at))
      functions[named.group(1)] = ' '.join(comment.split()) or (
          named.group(1))
    #  The Cute class and its functions, and the 'typedef' lines of
    #  what it takes from Python.
    cuteStarts, typedefs = [], []
    for at, line in enumerate(lines, 1):
      match = re.match(r'^typedef .*\(\*(Cute\w+Call\d+)\)', line)
      if match:
        items.append(('typedef', match.group(1), at, at))
        typedefs.append(at)
        continue
      match = re.match(r'^class (Cute\w+)\b.*\{\s*$', line)
      if match is None:
        continue
      last = next((n for n in range(at + 1, count + 1)
                   if lines[n - 1].rstrip() == '};'), None)
      if last is None:
        continue
      self.__cute_name__ = match.group(1)
      items.append(('cute class', match.group(1), at, last))
      cuteStarts.append(at)
      n = at + 1
      while n < last:
        if lines[n - 1].startswith('  //  ') and not (
            lines[n - 2].startswith('  //')):
          header = n
          while header < last and lines[header - 1].startswith('  //'):
            header += 1
          end = next((m for m in range(header, last)
                      if lines[m - 1].rstrip() == '  }'), None)
          named = re.search(r'(operator\S*?|~?\w+)\s*\(',
                            lines[header - 1] if header < last else '')
          if end is not None and named is not None:
            items.append(('cute function', named.group(1), n, end))
            n = end
        n += 1
    #  The pieces of Qt's code: from each '//  from' line to the next
    #  mark of where something else begins.
    fromLines = [at for at, line in enumerate(lines, 1)
                 if line.startswith('//  from ')]
    dashes = [at for at, line in enumerate(lines, 1)
              if re.match(r'^//  -{20,}\s*$', line)]
    marks = sorted({*fromLines, *dashes, *ritualStarts, *cuteStarts,
                    *typedefs, count + 1})
    for at in fromLines:
      after = next(m for m in marks if m > at)
      items.append(('copied', lines[at - 1][len('//  from '):].strip(),
                    at, after - 1))
    #  The '#include' lines, wherever they are, and those that stay.
    #  A file of no condition at all has nothing a header before its
    #  first condition says for it.
    firstCondition = next((
        at for at, line in enumerate(lines, 1)
        if re.match(r'^\s*#\s*if', line)), 0)
    fixed = set()
    for at, line in enumerate(lines, 1):
      match = re.match(r'^\s*#\s*(?:include|import)\b\s*(.*)$', line)
      if match:
        item = ('include', match.group(1).strip(), at, at)
        items.append(item)
        header = re.split(r'[\\/]', item[1].strip('<>" '))[-1]
        if at < firstCondition or re.search(r'global|config', header):
          fixed.add(item)
    #  Each line is in its innermost item: the order of the kinds, from
    #  the widest to the narrowest.
    order = ('copied', 'cute class', 'cute function', 'typedef', 'ritual',
             'include')
    lineItems = [None] * (count + 2)
    for kind in order:
      for item in items:
        if item[0] != kind:
          continue
        for number in range(item[2], item[3] + 1):
          lineItems[number] = item
    self.__file_items__ = (*sorted(items, key=lambda i: (i[2], i[3])),)
    self.__line_items__ = lineItems
    self.__ritual_functions__ = functions
    self.__fixed_items__ = fixed

  def _isDropped(self, item: Item) -> bool:
    """Says whether an item is dropped, by itself or in an item that
    holds it."""
    if self.__whole_reason__ is not None:
      return True
    for kind, name, first, last in self.__dropped_items__:
      if first <= item[2] and item[3] <= last:
        return True
    return False

  def _drop(self, item: Item, reason: str) -> bool:
    """Drops an item, unless it is dropped already, and says whether it
    was."""
    if self._isDropped(item):
      return False
    self.__dropped_items__[item] = reason
    return True

  def dropWhole(self, reason: str) -> None:
    """Drops the whole ritual file: the copy is empty, and every ritual
    of it is left out, for the reason given."""
    self.getRitualFile()
    self.__whole_reason__ = reason

  def _findLine(self, error: Dict[str, Any], compiledName: str) -> int:
    """Gives the line of the compiled file an error is blamed on: its
    own line there; else the first line there a note names; else, for
    an error in the text of a header itself, the '#include' line it came
    in by. An error in a template worked out for a type, whose notes
    name no line of the file, is blamed on no line: what asked for the
    template fails too, and is blamed for that. 0 when no line is."""
    if self._getBaseName(error['path']) == compiledName:
      return error['line']
    for path, line in error['notes']:
      if self._getBaseName(path) == compiledName:
        return line
    if error.get('instantiated', False):
      return 0
    for path, line in error['included']:
      if self._getBaseName(path) == compiledName:
        return line
    return 0

  def readBlame(
      self,
      said: str,
      compiledFile: str,
      *trial: Item,
  ) -> Tuple[List[Tuple[Item, str]], List[str]]:
    """
    Reads which items the errors of the compiler point at.

    Parameters
    ----------

    said : str
      What 'clang++' said when it refused the file.

    compiledFile : str
      The file 'clang++' compiled: the ritual file, or its copy.

    *trial : Item
      Items left out of the copy for a trial, which count as dropped.

    Returns
    -------

    Tuple[List[Tuple[Item, str]], List[str]]
      Each item an error points at that is not dropped, with why, once;
      and the text of each error that points at no item that may be
      dropped.
    """
    compiledName = self._getBaseName(compiledFile)
    ritualName = self._getBaseName(self.getRitualFile())
    blamed, unblamed = dict(), []
    for error in self.readCompilerErrors(said):
      #  The copy has the lines of the ritual file: the error is told as
      #  of the ritual file.
      text = error['text'].replace(compiledName, ritualName)
      item = self.getItemAt(self._findLine(error, compiledName))
      if item is None or item in self.__fixed_items__:
        unblamed.append(text)
        continue
      if self._isDropped(item) or item in trial or item in blamed:
        continue
      blamed[item] = 'the compiler refused it on this machine: %s' % text
    return list(blamed.items()), unblamed

  def drop(self, item: Item, reason: str) -> bool:
    """
    Drops an item, for the reason given, as a trial found it.

    Returns
    -------

    bool
      False when it was dropped already.
    """
    if item not in self.getItems():
      infoSpec = """The %s '%s' of lines %d to %d is no item of '%s'."""
      info = infoSpec % (*item, self.getRitualFile())
      raise ValueError(' '.join(info.split()))
    return self._drop(item, reason)

  def blameCompiler(self, said: str, compiledFile: str) -> bool:
    """
    Drops each item an error of the compiler points at.

    Parameters
    ----------

    said : str
      What 'clang++' said when it refused the file.

    compiledFile : str
      The file 'clang++' compiled: the ritual file, or its copy.

    Returns
    -------

    bool
      True when an item not dropped before was dropped. False when no
      error points at such an item: the caller then drops the whole
      file, as 'dropWhole' does.
    """
    found = False
    for item, reason in self.readBlame(said, compiledFile)[0]:
      found = self._drop(item, reason) or found
    return found

  def _findClass(self, name: str) -> Optional[Item]:
    """Gives the item that defines a class: the Cute class, or a piece
    of Qt's code holding 'class NAME' or 'struct NAME'."""
    short = name.split('::')[-1]
    for item in self.getItems():
      if item[0] == 'cute class' and item[1] == short:
        return item
    pattern = re.compile(r'^\s*(?:class|struct)\s+%s\b' % re.escape(short))
    for item in self.getItems():
      if item[0] != 'copied':
        continue
      for number in range(item[2], item[3] + 1):
        if pattern.match(self.__file_lines__[number - 1]):
          return item
    return None

  def _findDefinition(self, qualified: str) -> Optional[Item]:
    """Gives the item that defines a function, by its qualified name:
    a function of the Cute class, the Cute class, or a piece of Qt's
    code that defines it."""
    parts = qualified.split('::')
    name, owner = parts[-1], parts[-2] if len(parts) > 1 else None
    if owner is not None and owner == self.__cute_name__:
      for item in self.getItems():
        if item[0] == 'cute function' and item[1] == name:
          return item
      return self._findClass(owner)
    pattern = re.compile(r'^[^\s/#].*?(?<![\w:])%s\s*\(' % re.escape(
        qualified))
    for item in self.getItems():
      if item[0] != 'copied':
        continue
      for number in range(item[2], item[3] + 1):
        if pattern.match(self.__file_lines__[number - 1]):
          return item
    if owner is not None:
      return self._findClass(owner)
    return None

  def _findReferrer(self, referrer: str) -> Optional[Item]:
    """Gives the item a linker names as needing a symbol: a ritual by
    its name, a class by its table of virtual functions or its type
    information, a function by its name or its mangled name."""
    said = referrer.strip()
    quoted = re.match(r'^"([^"]+)"', said)
    if quoted:
      said = quoted.group(1).strip()
    ritual = re.match(r'^_?(ritual_\w+)$', said)
    if ritual:
      for item in self.getItems():
        if item[0] == 'ritual' and item[1] == ritual.group(1):
          return item
      return None
    table = (re.search(r'(?:vtable|typeinfo|typeinfo name|VTT) for (\S+)',
                       said)
             or re.search(r"(\S+)::`vftable'", said)
             or re.search(r'(?:^|\.)_{0,2}ZT[VISTC](?P<name>\d+\w+)', said))
    if table:
      named = table.group(1)
      number = re.match(r'^(\d+)(\w+)$', named)
      if number:
        named = number.group(2)[:int(number.group(1))]
      return self._findClass(named)
    mangled = said.lstrip('_')
    if mangled.startswith('Z'):
      for item in self.getItems():
        if item[0] == 'copied' and item[1].endswith('as _%s' % mangled):
          return item
    qualified = self._readQualifiedName(said)
    if qualified is None:
      return None
    return self._findDefinition(qualified)

  def blameLinker(self, blames: List[Blame]) -> bool:
    """
    Drops each item the linker named as needing a symbol no library
    offers, or as defining a symbol another object file defines too.
    Where the linker names no function, as for what the table of
    virtual functions of a class needs, the Cute class is dropped.

    Parameters
    ----------

    blames : List[Blame]
      What 'readLinkerRefusal' read for the object file of this ritual
      file.

    Returns
    -------

    bool
      True when an item not dropped before was dropped. False when none
      was: the caller then drops the whole file.
    """
    found = False
    for referrer, symbol, what in blames:
      if what == 'duplicate':
        item = self._findReferrer(symbol)
        reason = """the linker refused it on this machine: '%s' is defined
        by another ritual file too""" % symbol
      else:
        item = self._findReferrer(referrer) if referrer else None
        if item is None and referrer is None and self.__cute_name__:
          item = self._findClass(self.__cute_name__)
        reason = """the linker refused it on this machine: it needs '%s',
        which no library of Qt here offers""" % symbol
      if item is None:
        continue
      found = self._drop(item, ' '.join(reason.split())) or found
    return found
