"""DefaultValue is what Qt fills in for an argument that is left out,
read from what the compiler wrote down of it, and said in Python."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import threading
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable

from . import DependencyTree
from .class_tables import PYTHON_WORDS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional

  Record = Dict[str, Any]


class DefaultValue:
  """
  What Qt fills in for an argument of a function that is left out, as
  the compiler wrote it down in the header: a number, a member of an
  enum or several joined with '|', a value made of such, or the object
  a function of a class gives. It is read from that record and said in
  Python by 'findPython':

    default = DefaultValue()
    default.setArgument(argument)    # as the plan of the ritual has it
    default.setParameter(parameter)  # as the 'ClassGenerator' has it
    default.setViewer(classGenerator)
    default.findPython()             # {'text': '-1'}, or None

  What depends on other classes, as whether the cute class of a value
  can be made of what Qt hands its constructor, is asked of the
  'ClassGenerator' writing the class, the viewer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _unwrap(node: Optional[Record]) -> Optional[Record]:
    """
    Gives what the compiler wrote down for a value, without the layers
    it puts around it that change nothing of the value.
    """
    layers = (
        'ImplicitCastExpr', 'ExprWithCleanups', 'ConstantExpr',
        'MaterializeTemporaryExpr', 'CXXBindTemporaryExpr', 'ParenExpr',
    )
    while node is not None and node.get('kind') in layers:
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      node = inner[0] if inner else None
    return node

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _findGiven(node: Record) -> List[Record]:
    """Gives what a default of Qt hands to the constructor it calls,
    leaving out what that constructor fills in itself."""
    return [
        child for child in node.get('inner', ())
        if isinstance(child, dict)
        and child.get('kind') != 'CXXDefaultArgExpr'
    ]



  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The constants of the classes of Qt that are numbers are gathered
  #  once for each tree and kept in a dict the tree gives for it; see
  #  '_findConstantNumber'. The lock keeps two threads from both
  #  gathering them.
  __constant_lock__ = threading.RLock()

  #  Private Variables
  __argument__ = None  # type: Optional[Record]
  __parameter__ = None  # type: Optional[Record]
  __viewer__ = None  # type: Any

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getArgument(self) -> Record:
    """
    Gives the argument as the plan of the ritual has it, with what the
    compiler wrote down of its default under 'default'.

    Provided by you, through 'setArgument'.

    Raises
    ------

    MissingVariable
      'setArgument' has not been called.
    """
    if self.__argument__ is None:
      raise MissingVariable(self, '__argument__', dict)
    return self.__argument__

  def getParameter(self) -> Record:
    """
    Gives the same argument as the 'ClassGenerator' has it in Python:
    its 'kind', 'annotation', 'entry', 'className' and 'holder'.

    Provided by you, through 'setParameter'.

    Raises
    ------

    MissingVariable
      'setParameter' has not been called.
    """
    if self.__parameter__ is None:
      raise MissingVariable(self, '__parameter__', dict)
    return self.__parameter__

  def getViewer(self) -> Any:
    """
    Gives the 'ClassGenerator' of the cute class the argument is of.

    Provided by you, through 'setViewer'.

    Raises
    ------

    MissingVariable
      'setViewer' has not been called.
    """
    if self.__viewer__ is None:
      raise MissingVariable(self, '__viewer__', object)
    return self.__viewer__

  def getParts(self) -> Record:
    """
    Gives what the default is made of, as the compiler wrote it down:
    'kind', the kind of the outermost thing that is not a mere layer, as
    'IntegerLiteral' or 'CXXConstructExpr'; 'number', the number it
    stands for, or None; 'names', the members of an enum it names, or
    None; 'given', how many things it hands the constructor it calls.
    """
    node = self._unwrap(self.getArgument().get('default'))
    if node is None:
      return dict(kind=None, number=None, names=None, given=0)
    return dict(
        kind=node.get('kind'), number=self._findNumber(node),
        names=self._findJoinedNames(node), given=len(self._findGiven(node)))

  def findPython(self) -> Any:
    """
    Says in Python what Qt fills in for the argument when it is left
    out.

    Returns
    -------

    Optional[Record]
      None when it cannot be said in Python. Else 'text': the default
      of the Python argument, as 'None' or '-1'; and for a value that
      has to be made anew for each call, 'made': what makes it, as
      'QPoint()'.
    """
    argument, parameter = self.getArgument(), self.getParameter()
    node = self._unwrap(argument['default'])
    if node is None:
      return None
    kind, nodeKind = parameter['kind'], node.get('kind')
    making = ('CXXTemporaryObjectExpr', 'CXXConstructExpr')
    if nodeKind == 'CXXFunctionalCastExpr':
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      node = self._unwrap(inner[0]) if inner else None
      if node is None:
        return None
      nodeKind = node.get('kind')
    if kind in ('address', 'chars'):
      if nodeKind == 'CXXNullPtrLiteralExpr':
        return dict(text='None')
      if nodeKind == 'IntegerLiteral' and node.get('value') == '0':
        return dict(text='None')
      if kind == 'address' and nodeKind == 'CallExpr':
        return self._findCalledDefault(node, parameter)
      return None
    if kind == 'number':
      number = self._findNumber(node)
      if number is None:
        return None
      wanted = parameter['annotation']
      if wanted == 'bool':
        return dict(text=repr(True if number else False))
      if wanted == 'float':
        return dict(text=repr(float(number)))
      if isinstance(number, float):
        return None
      return dict(text=repr(int(number)))
    if kind in ('enum', 'flags'):
      if nodeKind in making and not self._findGiven(node):
        if kind == 'flags':
          return dict(text='%s()' % parameter['entry'])
        return None
      #  One member, or for flags several joined with '|', as Qt's
      #  'RenderFlags(DrawWindowBackground | DrawChildren)'.
      names = self._findJoinedNames(node)
      if names is None or (len(names) > 1 and kind != 'flags'):
        return None
      record = parameter['enumGenerator'].getEnumRecord()
      members = [name for name, _ in record['members']]
      if any(name not in members for name in names):
        return None
      words = PYTHON_WORDS
      return dict(text=' | '.join(
          '%s.%s' % (parameter['entry'], words.get(name, name))
          for name in names))
    if kind == 'text':
      if nodeKind in making and not self._findGiven(node):
        return dict(text="''")
      return None
    if kind == 'value':
      if nodeKind not in making:
        return None
      given = self._findGiven(node)
      if not given:
        if self.getViewer()._canBeMadeEmpty(parameter['className']):
          made = '%s()' % parameter['holder']
          return dict(text='None', made=made)
        return None
      #  A value Qt makes of numbers written out, of a member of an
      #  enum of the namespace Qt, or of such values in turn:
      #  'QMarginsF(0, 0, 0, 0)', 'QColor(Qt::white)',
      #  'QRect(QPoint(0, 0), QSize(-1, -1))'.
      parts = [self._findMadeOf(one) for one in given]
      if any(part is None for part in parts):
        return None
      if not self.getViewer()._canBeMadeOf(parameter['className'], parts):
        return None
      made = '%s(%s)' % (
          parameter['holder'], ', '.join(part['text'] for part in parts))
      brings = []  # type: List[str]
      for part in parts:
        brings.extend(n for n in part['brings'] if n not in brings)
      return dict(text='None', made=made, brings=(*brings,))
    return None

  def _findCalledDefault(self, node: Record, parameter: Record) -> Any:
    """
    Says in Python what Qt fills in for an object it gets by calling a
    function of the class of that object with nothing handed over, as
    'QPointingDevice::primaryPointingDevice()' for the device of a
    'QMouseEvent'.

    None stands for no object there, so it cannot also stand for an
    argument that was left out. '...' does: no signature takes it, so
    it reaches the function only where the argument is left out.

    Parameters
    ----------

    node : Record
      The call, as the compiler wrote it down.

    parameter : Record
      The argument as this generator has it in Python.

    Returns
    -------

    Optional[Record]
      None when it cannot be said in Python: the call hands something
      over, or the cute class of the object has no such function that
      is called on no object and with nothing. Else 'text': '...';
      'left': the same, what the function finds there; 'made': the
      call in Python; 'brings': the class it is called on.
    """
    inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
    if not inner:
      return None
    if any(c.get('kind') != 'CXXDefaultArgExpr' for c in inner[1:]):
      return None
    called = self._unwrap(inner[0])
    if called is None or called.get('kind') != 'DeclRefExpr':
      return None
    referenced = called.get('referencedDecl', dict())
    if referenced.get('kind') != 'CXXMethodDecl':
      return None
    name, className = referenced.get('name'), parameter['className']
    generator = self.getViewer().getRitualGenerator(className)
    found = [
        plan for plan in generator.getWritten()
        if plan['kind'] == 'static method' and plan['name'] == name
    ]
    if len(found) != 1:
      return None
    for argument in found[0]['arguments']:
      if argument.get('default') is None:
        return None
    made = '%s.%s()' % (parameter['holder'], name)
    return dict(text='...', left='...', made=made, brings=(className,))

  def _findNumber(self, node: Optional[Record]) -> Any:
    """
    Gives the number a default of Qt stands for, as an 'int', a 'float'
    or a 'bool', or None when it is no plain number.
    """
    node = self._unwrap(node)
    if node is None:
      return None
    kind = node.get('kind')
    if kind == 'CXXBoolLiteralExpr':
      return True if node.get('value') else False
    if kind == 'IntegerLiteral':
      return int(node['value'])
    if kind == 'FloatingLiteral':
      return float(node['value'])
    if kind == 'UnaryOperator' and node.get('opcode') in ('-', '+'):
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      number = self._findNumber(inner[0]) if inner else None
      if number is None or isinstance(number, bool):
        return None
      return -number if node['opcode'] == '-' else number
    if kind == 'BinaryOperator' and node.get('opcode') in ('+', '-', '*'):
      #  Qt writes some numbers as a sum, as 'Qt::UserRole + 1'.
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      if len(inner) != 2:
        return None
      left, right = self._findNumber(inner[0]), self._findNumber(inner[1])
      for number in (left, right):
        if number is None or isinstance(number, bool):
          return None
      if node['opcode'] == '+':
        return left + right
      return left - right if node['opcode'] == '-' else left * right
    if kind == 'DeclRefExpr':
      referenced = node.get('referencedDecl', dict())
      if referenced.get('kind') == 'EnumConstantDecl':
        return self._findEnumNumber(referenced)
      if referenced.get('kind') == 'VarDecl':
        return self._findConstantNumber(referenced)
    return None

  def _findEnumNumber(self, referenced: Record) -> Optional[int]:
    """
    Gives the number of one name of an enum that a default of Qt
    refers to, or None when it is not found.

    Parameters
    ----------

    referenced : Record
      What the compiler wrote down of the name referred to: its 'name'
      and the 'type' of its enum.
    """
    viewer = self.getViewer()
    tree, name = viewer.getDependencyTree(), referenced.get('name')
    enumName = referenced.get('type', dict()).get('qualType', '')
    className, partName = viewer.getClassName(), viewer.getPartName()
    ancestors = [n for _, n in tree.getAncestors(className, partName)]
    for scope in ('', className, *ancestors):
      fullName = '%s::%s' % (scope, enumName) if scope else enumName
      try:
        members = tree.getEnumRecord(fullName, partName)['members']
      except ValueError:
        continue
      for memberName, number in members:
        if memberName == name:
          return number
    #  An enum without a name of its own is in no list of enums. Its
    #  names are found in the record of the class that writes it.
    for scope in (className, *ancestors):
      for child in tree.getClassRecord(scope, partName).get('inner', ()):
        if child.get('kind') != 'EnumDecl' or child.get('name'):
          continue
        collected = DependencyTree._collectEnumMembers(child)
        if collected['unsure'] is not None:
          continue
        for memberName, number in collected['members']:
          if memberName == name:
            return number
    return None

  def _findConstantNumber(self, referenced: Record) -> Any:
    """
    Gives the number of a constant of a class of Qt that a default
    refers to, as 'QLocale::DefaultTwoDigitBaseYear', which is 1900.

    What the compiler wrote down of the reference holds the name of
    the constant and not its class. So the constants of every cute
    class are gathered once for each tree, and a name is taken when
    the classes that have it agree on one number.

    Returns
    -------

    Any
      The number, or None when no class has such a constant, or the
      classes that have one disagree.
    """
    tree = self.getViewer().getDependencyTree()
    with self.__constant_lock__:
      kept = tree.getKept('constant numbers')
      numbers = kept.get('found', None)
      if numbers is None:
        #  Kept before it is filled: a constant written in terms of
        #  another one asks here again, and finds what is there so far.
        numbers = dict()
        kept['found'] = numbers
        for partName, className in self.getViewer().getCuteNames():
          record = tree.getClassRecord(className, partName)
          for child in record.get('inner', ()):
            if child.get('kind') != 'VarDecl':
              continue
            if not child.get('constexpr', False):
              continue
            written = child.get('inner', ())
            written = [c for c in written if isinstance(c, dict)]
            number = self._findNumber(written[0]) if written else None
            if number is None or isinstance(number, bool):
              continue
            numbers.setdefault(child.get('name'), set()).add(number)
    found = numbers.get(referenced.get('name'), ())
    return [*found][0] if len(found) == 1 else None

  def _findJoinedNames(self, node: Optional[Record]) -> Optional[List[str]]:
    """
    Gives the names of the members of an enum that a default of Qt
    stands for: the one name it refers to, or the names it joins with
    '|', as 'DrawWindowBackground | DrawChildren'. Gives None when the
    default is anything else.
    """
    node = self._unwrap(node)
    if node is None:
      return None
    kind = node.get('kind')
    inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
    if kind in ('CXXFunctionalCastExpr', 'CXXStaticCastExpr'):
      return self._findJoinedNames(inner[0]) if inner else None
    if kind in ('CXXConstructExpr', 'CXXTemporaryObjectExpr'):
      given = self._findGiven(node)
      return self._findJoinedNames(given[0]) if len(given) == 1 else None
    if kind == 'DeclRefExpr':
      referenced = node.get('referencedDecl', dict())
      if referenced.get('kind') != 'EnumConstantDecl':
        return None
      return [referenced.get('name')]
    if kind == 'BinaryOperator' and node.get('opcode') == '|':
      joined = inner
    elif kind == 'CXXOperatorCallExpr' and inner:
      called = self._unwrap(inner[0]) or dict()
      if called.get('referencedDecl', dict()).get('name') != 'operator|':
        return None
      joined = inner[1:]
    else:
      return None
    names = []  # type: List[str]
    for part in joined:
      found = self._findJoinedNames(part)
      if found is None:
        return None
      names.extend(found)
    return names or None

  def _findMadeOf(self, node: Optional[Record]) -> Optional[Record]:
    """
    Says in Python one thing a default of Qt makes a value of, as the
    'Qt::white' of 'QColor(Qt::white)': a number written out, or a
    member of an enum of the namespace Qt, which every class file has
    at hand.

    Returns
    -------

    Optional[Record]
      None when it is anything else. Else 'kind': 'number', 'enum' or
      'value'; 'cppName': the enum or the class as C++ names it, or ''
      for a number; 'text': how it is written in Python, as '0',
      'Qt.GlobalColor.white' or 'QPoint(0, 0)'; and 'brings': the late
      classes the text names, which have to be brought in before it is
      run.
    """
    node = self._unwrap(node)
    if node is None:
      return None
    kind = node.get('kind')
    if kind in ('CXXTemporaryObjectExpr', 'CXXConstructExpr'):
      #  A value made of what this very method can say, as the
      #  'QPoint(0, 0)' of 'QRect(QPoint(0, 0), QSize(-1, -1))'.
      cppName = node.get('type', dict()).get('qualType', '')
      cppName = cppName.replace('const ', '').strip()
      found = self.getViewer().getCuteName(cppName).findClassEntry()
      if not isinstance(found, dict):
        return None
      parts = [self._findMadeOf(one) for one in self._findGiven(node)]
      if any(part is None for part in parts):
        return None
      if parts and not self.getViewer()._canBeMadeOf(cppName, parts):
        return None
      if not parts and not self.getViewer()._canBeMadeEmpty(cppName):
        return None
      brings = [name for part in parts for name in part['brings']]
      if found['late'] and found['bring']:
        brings.append(found['bring'])
      made = '%s(%s)' % (
          found['holder'], ', '.join(part['text'] for part in parts))
      return dict(
          kind='value', cppName=cppName, text=made, brings=(*brings,))
    if kind == 'DeclRefExpr':
      referenced = node.get('referencedDecl', dict())
      if referenced.get('kind') != 'EnumConstantDecl':
        return None
      enumName = referenced.get('type', dict()).get('qualType', '')
      if not enumName.startswith('Qt::'):
        return None
      found = self.getViewer().getCuteName(enumName).findEnumEntry(False)
      if not isinstance(found, dict):
        return None
      name = referenced.get('name')
      record = found['generator'].getEnumRecord()
      if all(name != member for member, _ in record['members']):
        return None
      name = PYTHON_WORDS.get(name, name)
      return dict(
          kind='enum', cppName=enumName, brings=(),
          text='%s.%s' % (found['entry'], name))
    literals = ('IntegerLiteral', 'FloatingLiteral')
    if kind == 'UnaryOperator':
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      below = self._unwrap(inner[0]) if inner else None
      if below is None or below.get('kind') not in literals:
        return None
    elif kind not in literals:
      return None
    number = self._findNumber(node)
    if number is None or isinstance(number, bool):
      return None
    return dict(kind='number', cppName='', text=repr(number), brings=())



  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setArgument(self, argument: Record) -> None:
    """Sets the argument as the plan of the ritual has it."""
    self.__argument__ = argument

  def setParameter(self, parameter: Record) -> None:
    """Sets the same argument as the 'ClassGenerator' has it in Python."""
    self.__parameter__ = parameter

  def setViewer(self, viewer: Any) -> None:
    """Sets the 'ClassGenerator' of the cute class the argument is of."""
    self.__viewer__ = viewer
