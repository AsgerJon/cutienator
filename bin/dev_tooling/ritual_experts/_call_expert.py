"""CallExpert says whether a ritual can call a function of Qt by the
name Qt's library offers it under."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import re
import subprocess
from typing import TYPE_CHECKING

from .. import HeaderReader, Machine
from . import ReachExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, FrozenSet, List, Set

  Record = Dict[str, Any]


class CallExpert(ReachExpert):
  """
  Says whether a ritual can call a function of Qt by the name Qt's
  library offers it under, going by Qt's source alone. No Qt that is
  compiled or installed is looked at.

  A function can be called in three cases. Its code is written in a
  header file, so the compiler of each machine makes it where the
  ritual is compiled. Or it is virtual, so it is found through the
  object it is called on. Or Qt's source marks it, or the class it
  belongs to, for use from outside, as 'Q_CORE_EXPORT', and writes its
  code so that it can be called from there. Any other function has no
  name by which anything outside Qt could reach it; 'CopyExpert' is
  asked next.

  The marks are read once for the whole tree, from the records of
  every header file, and kept on the tree; see 'getMarkedSymbols'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def plainSymbol(symbol: str) -> str:
    """
    Gives a name the compiler made with the mark of the kind of
    constructor or destructor taken out. The compiler makes two names
    for one constructor, ending its name with 'C1' or 'C2', and three
    for one destructor, 'D0', 'D1' and 'D2'; a record has the first.
    """
    symbol = re.sub(r'C[123](?=E)', 'C1', symbol)
    return re.sub(r'D[012](?=E)', 'D1', symbol)

  @staticmethod
  def hasMark(member: Record) -> bool:
    """Says whether the compiler wrote down Qt's mark for use from
    outside Qt on a function itself, as 'Q_CORE_EXPORT'."""
    return any(
        isinstance(child, dict) and child.get('kind') == 'VisibilityAttr'
        for child in member.get('inner', ()))

  @staticmethod
  def demangle(symbols: List[str]) -> Dict[str, str]:
    """Gives each name the compiler made as C++ writes it, by one run
    of 'c++filt' for all of them."""
    if not symbols:
      return dict()
    said = subprocess.run(
        Machine.getDemangler(), input='\n'.join(symbols),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, universal_newlines=True).stdout
    return dict(zip(symbols, said.split('\n')))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  How the names of the functions begin that Qt declares only for
  #  the compiler to check something, and writes no code for.
  __never_written__ = ('qt_check_for_',)
  #  How 'c++filt' writes the name of what the compiler makes for a
  #  class as a whole, and of what it makes around one function.
  __made_for_class__ = (
      'vtable for ', 'typeinfo name for ', 'typeinfo for ', 'VTT for ',
  )
  __made_for_function__ = (
      'non-virtual thunk to ', 'virtual thunk to ', 'guard variable for ',
  )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getMarkedSymbols(self) -> FrozenSet[str]:
    """
    Gives the compiler's own name of everything Qt marks for use from
    outside Qt, as the compiler wrote the mark down when it read Qt's
    header files.

    Taken are a function or a value carrying a word such as
    'Q_CORE_EXPORT' itself, a function Qt writes inside a class with
    'friend' in front and such a word, and every function and value of
    a class, or of an instance of a template, that carries one, as
    'extern template struct Q_CORE_EXPORT
    QMetaTypeInterfaceWrapper<bool>'. A class written inside a marked
    class adds its own only where it is marked itself. The compiler has
    written out Qt's shorthands by then, so a mark made through one, as
    'QT_DECLARE_EXPORTED_QT_LOGGING_CATEGORY', counts as well. The
    names are kept as 'sameFunction' compares them. Kept on the tree
    after the first call; call it once before handing the tree to
    other processes, and they all start from it.
    """
    tree = self.getGenerator().getDependencyTree()
    kept = tree.getKept('marked symbols')
    if 'names' in kept:
      return kept['names']
    found, declared = set(), set()  # type: Set[str], Set[str]
    recordKinds = ('CXXRecordDecl', 'ClassTemplateSpecializationDecl')

    def walk(node: Any, inMarked: bool) -> None:
      """Takes the names of one record and of what it holds."""
      if not isinstance(node, dict):
        return
      kind = node.get('kind', '')
      marked = self.hasMark(node)
      if 'mangledName' in node:
        declared.add(self.plainSymbol(node['mangledName']))
        if marked or inMarked:
          found.add(self.plainSymbol(node['mangledName']))
      if kind in recordKinds:
        inner = marked
      elif kind in ('FriendDecl', 'NamespaceDecl', 'LinkageSpecDecl'):
        inner = False
      else:
        inner = inMarked
      for child in node.get('inner', ()) or ():
        walk(child, inner)

    for headerReader in tree.getHeaderReaders():
      for headerFile in headerReader.getHeaderFiles():
        if not headerFile.wasRead() or not headerFile.getRecordCount():
          #  Refused by the compiler, or holding no records.
          continue
        #  Read one record at a time and keep none: the records of all
        #  the parts together are more than a process should hold.
        with open(headerFile.getRecordPath()) as file:
          for line in file:
            walk(json.loads(line), False)
    kept['names'] = frozenset(found)
    kept['declared'] = frozenset(declared)
    return kept['names']

  def getDeclaredSymbols(self) -> FrozenSet[str]:
    """
    Gives the compiler's own name of everything Qt's header files
    declare, marked or not, kept as 'sameFunction' compares them.
    Found by the same reading as 'getMarkedSymbols', and kept on the
    tree with those.
    """
    kept = self.getGenerator().getDependencyTree().getKept('marked symbols')
    if 'declared' not in kept:
      self.getMarkedSymbols()
    return kept['declared']

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def canReach(self, member: Record) -> bool:
    """Says whether a ritual can call the function; see 'canBeCalled'."""
    return self.canBeCalled(member)

  def getWay(self) -> str:
    """Says what this way does: the ritual calls the function."""
    return 'be called'

  def getRefusal(self) -> str:
    """Says why a ritual cannot call a function 'canReach' said no to."""
    infoSpec = """no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or
    nowhere"""
    return ' '.join(infoSpec.split())

  def sameFunction(self, first: str, second: str) -> bool:
    """Says whether two names the compiler made stand for one function;
    see 'plainSymbol'."""
    return self.plainSymbol(first) == self.plainSymbol(second)

  def isOfQt(self, symbol: str) -> bool:
    """Says whether a name the compiler made stands for something of
    Qt: a name of the C++ library or of the system does not. It is of
    Qt when a name in it begins with 'Q' or 'q'; when it is of a class
    the tree knows, seen from the part, as the table of virtual
    functions of QtDataVisualization's 'AbstractRenderItem',
    '_ZTV18AbstractRenderItem', or a function of it; or when Qt's
    header files declare it, as the logging category 'lcImageIo' that
    Qt's 'qimage_p.h' declares; see 'getDeclaredSymbols'."""
    if re.search(r'\d+[Qq][A-Za-z_]', symbol):
      return True
    #  The first name the compiler's own name holds: after '_Z', what
    #  it made for a class ('TV', 'TI', 'TS', 'TT'), a scope ('N') and
    #  what qualifies a function of it ('K', 'V', 'r', 'R', 'O').
    first = re.match(r'_Z(?:T[VIST])?(?:N[KVrRO]*)?(\d+)', symbol)
    if first is not None:
      start, length = first.end(), int(first.group(1))
      name = symbol[start:start + length]
      generator = self.getGenerator()
      tree = generator.getDependencyTree()
      if tree.hasClass(name, generator.getPartName()):
        return True
    return self.plainSymbol(symbol) in self.getDeclaredSymbols()

  def isMarkedForExport(self, className: str) -> bool:
    """
    Says whether Qt marks a class for export on its own, as in
    'class Q_CORE_EXPORT QObject'. A class the tree does not know
    counts as not marked.

    It matters for a class written inside another. Qt's library for
    Linux and for macOS offers the functions of such a class when the
    class around it is marked. Qt's library for Windows offers them
    only when the class is marked itself.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    try:
      classKey = generator._keyOf(className)
    except LookupError:
      return False
    kept = tree.getKept('export marks')
    try:
      return kept[classKey]
    except KeyError:
      pass
    record = generator._readRecord(className)
    marked = any(
        isinstance(child, dict) and child.get('kind') == 'VisibilityAttr'
        for child in record.get('inner', ()))
    kept[classKey] = marked
    return marked

  def isMarkedName(self, shown: str, symbol: str) -> bool:
    """
    Says whether Qt's source marks, for use from outside Qt, the thing
    a name of the compiler stands for, and writes it so that it can be
    called from there.

    A function of a class is marked when the class itself is, or the
    function. The class is that very class: one written inside a
    marked class with no mark of its own is not marked. What the
    compiler makes for a class, as its table of virtual functions,
    goes with the class. A function made from a template is not
    marked: its code is in a header file or nowhere. Anything else is
    marked when the compiler wrote Qt's mark down on it, as
    'getMarkedSymbols' has them: a function outside of every class, a
    friend, a value of an instance of a template. A marked function
    that Qt writes 'inline' with its code in no header file counts as
    not marked: see 'isWrittenInline'.

    Parameters
    ----------

    shown : str
      The name as C++ writes it, with what a function takes, as
      'c++filt' gives it.

    symbol : str
      The same name as the compiler made it.
    """
    for start in self.__made_for_class__:
      if shown.startswith(start):
        className = shown[len(start):].split('<')[0].strip()
        return self.isMarkedForExport(className)
    for start in self.__made_for_function__:
      if shown.startswith(start):
        shown = shown[len(start):]
    head, end = shown, shown.rfind(')')
    if end >= 0:
      depth, start = 0, -1
      for index in range(end, -1, -1):
        letter = shown[index]
        depth += 1 if letter == ')' else -1 if letter == '(' else 0
        if depth == 0:
          start = index
          break
      if start < 0:
        return False
      head = shown[:start]
    #  What stands before the name: the type a function made from a
    #  template gives.
    depth, cut = 0, 0
    for index, letter in enumerate(head):
      depth += 1 if letter == '<' else -1 if letter == '>' else 0
      if letter == ' ' and depth == 0:
        cut = index + 1
    name, parts, depth, last = head[cut:], [], 0, 0
    for index, letter in enumerate(name):
      depth += 1 if letter == '<' else -1 if letter == '>' else 0
      if depth == 0 and name[index:index + 2] == '::':
        parts.append(name[last:index])
        last = index + 2
    parts.append(name[last:])
    if '<' in parts[-1] and 'operator' not in parts[-1]:
      return False
    className = '::'.join(part.split('<')[0] for part in parts[:-1])
    bare = parts[-1].split('<')[0]
    markedSymbol = self.plainSymbol(symbol) in self.getMarkedSymbols()
    generator = self.getGenerator()
    if not className or className not in generator._getKnownNames():
      return markedSymbol
    try:
      record = generator._readRecord(className)
    except (ValueError, LookupError):
      return markedSymbol
    members = [
        member for member in record.get('inner', ())
        if isinstance(member, dict) and member.get('name') == bare
    ]
    if not markedSymbol and not self.isMarkedForExport(className):
      if not any(self.hasMark(member) for member in members):
        return False
    for member in members:
      if self.sameFunction(member.get('mangledName', ''), symbol):
        return not self.isWrittenInline(className, member)
    return True

  def isMarked(self, member: Record) -> bool:
    """
    Says whether Qt's source marks a function of the class for use
    from outside Qt: the function carries a word such as
    'Q_CORE_EXPORT' itself, or the class it belongs to does.

    The class it belongs to is that very class. A class written inside
    a marked class, with no mark of its own, counts as not marked:
    only then does every system agree that the function is there.
    """
    if self.hasMark(member):
      return True
    return self.isMarkedForExport(self.getGenerator().getClassName())

  def canBeCalled(self, member: Record) -> bool:
    """
    Says whether a ritual can call this function of Qt, going by Qt's
    source alone. No Qt that is compiled or installed is looked at.

    A function can be called in three cases. Its code is written in a
    header file, so the compiler of each machine makes it where the
    ritual is compiled. Or it is virtual, so it is found through the
    object it is called on. Or Qt's source marks it, or the class it
    belongs to, for use from outside, and writes its code so that it
    can be called from there; see 'isMarked' and
    'isWrittenToBeCalled'. Any other function has no name by which
    anything outside Qt could reach it, and a ritual for it has to
    carry a copy of its code.

    A few functions Qt declares only to have the compiler check
    something, and writes no code for anywhere, as
    'QEvent::qt_check_for_QGADGET_macro()'. They cannot be called
    whatever they are marked.

    Parameters
    ----------

    member : Record
      What the compiler wrote down about the function, with its own name
      for it under 'mangledName'.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    if member.get('name', '').startswith(self.__never_written__):
      return False
    name = member['mangledName']
    if member.get('virtual') or self._isOverride(member):
      return True
    if tree.hasBody(member):
      return True
    if tree.isDefined(name, generator.getPartName()):
      return True
    if not self.isMarked(member):
      return False
    return self.isWrittenToBeCalled(member)

  def _isOverride(self, member: Record) -> bool:
    """
    Says whether a function is virtual by overriding one, as Qt declares
    most: 'override' makes it virtual without the word 'virtual', which
    alone is what the compiler notes as 'virtual'. Called on the object,
    C++ finds it through the object, by no name of the library. Not so
    for a function or class declared 'final': C++ may then call the
    function by its name, which a class Qt does not mark has none for.
    """
    marks = [
        child.get('kind') for child in member.get('inner', ())
        if isinstance(child, dict)]
    if 'OverrideAttr' not in marks or 'FinalAttr' in marks:
      return False
    generator = self.getGenerator()
    record = generator._readRecord(generator.getClassName())
    return not any(
        isinstance(child, dict) and child.get('kind') == 'FinalAttr'
        for child in record.get('inner', ()))

  def isWrittenToBeCalled(self, member: Record) -> bool:
    """
    Says whether Qt's source writes the code of a marked function of
    the class in a way that lets it be called from outside Qt.

    Two things in the source say no, whatever the mark. Qt writes code
    for the function nowhere: it only declares it, as it declares the
    constructor of 'QStandardPaths' so that nobody can make one. Or
    Qt writes it 'inline' with its code in no header file; see
    'isWrittenInline'.

    The source is asked under every name C++ code can give the class,
    as 'DependencyTree.getSpellings' has them: Qt writes the code of
    'QLatin1String::compare_helper' as 'QLatin1StringView::...'. A
    constructor or destructor is named after the class as spelled.
    Without Qt's source at hand the mark alone decides.

    A signal is written by Qt's 'moc', into Qt's library, and never in
    Qt's source: the header declaring it under 'signals:' is all the
    source says, and that says yes.
    """
    if member.get('kind') == 'FunctionDecl':
      #  A function outside of every class, which Qt wrote inside the
      #  class with 'friend' in front: it has no class in its name.
      return True
    place = member.get('loc', dict())
    place = place.get('expansionLoc', place)
    headerPath, line = place.get('file'), place.get('line')
    if headerPath and line:
      if line in HeaderReader.getSignalLines(headerPath):
        return True
    if not self.hasWrittenCode(member):
      return False
    className = self.getGenerator().getClassName()
    return not self.isWrittenInline(className, member)

  def hasWrittenCode(self, member: Record) -> bool:
    """
    Says whether Qt's source writes code under the name of a function
    of the class, in any file of code of the part, under any name C++
    code can give the class; see 'SourceReader.hasCode'. Without Qt's
    source at hand it says yes.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    source = tree.getSourceReader()
    if source is None:
      return True
    className, partName = generator.getClassName(), generator.getPartName()
    name, kind = member.get('name', ''), member.get('kind', '')
    for spelled in tree.getSpellings(className, partName):
      last = spelled.rpartition('::')[2]
      if kind == 'CXXConstructorDecl':
        asked = '%s::%s' % (spelled, last)
      elif kind == 'CXXDestructorDecl':
        asked = '%s::~%s' % (spelled, last)
      else:
        asked = '%s::%s' % (spelled, name)
      if source.hasCode(partName, asked):
        return True
    return False

  def isWrittenInline(self, className: str, member: Record) -> bool:
    """
    Says whether Qt writes a function of a class 'inline' with its code
    in no header file. The compiler then puts the code where Qt calls
    it, and Qt's library keeps no function under its name. Qt writes
    the word in the header file, as
    'inline explicit QJsonDocument(QCborValue data);', or in front of
    the code in the '.cpp' file, as 'QCborStreamReader::preparse()'.

    Parameters
    ----------

    className : str
      The class the function belongs to.

    member : Record
      What the compiler wrote down about the function.
    """
    from . import CopyExpert
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    if tree.hasBody(member):
      return False
    partName = generator.getPartName()
    if tree.isDefined(member.get('mangledName', ''), partName):
      return False
    if member.get('inline'):
      return True
    copyExpert = generator.getExpert(CopyExpert)
    definition = copyExpert.findSourceCode(member, className)
    if definition is None:
      return False
    head = definition['text'].split('(')[0]
    return True if re.search(r'\binline\b', head) else False
