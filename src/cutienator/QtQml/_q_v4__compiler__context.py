"""
QV4::Compiler::Context binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Compiler::Context to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Context(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Compiler::Context: a plain Python object
  standing in front of one C++ QV4::Compiler::Context.

  What exists
  -----------

  Every function of Qt's QV4::Compiler::Context that has a ritual and that
  Python can call so far, 8 names in all: 'hasArgument', 'findMember',
  'requiresImplicitReturnValue', 'addUsedVariable', 'addLocalVar',
  'resolveName', 'canHaveTailCalls', 'isCaseBlock'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QV4::Compiler::Context::findArgument(const QString &name, bool
    *isInjected) const': takes a number to change where it is.
  - Qt's 'bool QV4::Compiler::Context::memberInfo(const QString &name, const
    Member **m) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 3 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::Compiler::Context is created at the first use, not by
    'QV4::Compiler::Context(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Compiler::Context.
  - Each name of Qt's QV4::Compiler::Context that has no cute function yet,
    'emitBlockFooter', 'emitBlockHeader', 'findArgument', 'memberInfo',
    'setupFunctionIndices', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Compiler::Context, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class MemberType(CuteNum):
    """
    The enum 'QV4::Compiler::Context::MemberType' of Qt, with the 5 names Qt
    gives in it.
    """

    UndefinedMember = Kee[int](0)
    ThisFunctionName = Kee[int](1)
    VariableDefinition = Kee[int](2)
    VariableDeclaration = Kee[int](3)
    FunctionDefinition = Kee[int](4)

  class UsesArgumentsObject(CuteNum, scoped=True):
    """
    The enum 'QV4::Compiler::Context::UsesArgumentsObject' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    NotUsed = Kee[int](1)
    Used = Kee[int](2)

  #  The classes Qt writes inside QV4::Compiler::Context, each a class in
  #  here as in C++.

  class KeyValuePair(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Compiler::Context::KeyValuePair: a plain
    Python object standing in front of one C++
    QV4::Compiler::Context::KeyValuePair.

    C++ hands a QV4::Compiler::Context::KeyValuePair around as a copy, so
    every C++ QV4::Compiler::Context::KeyValuePair behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Compiler::Context::KeyValuePair that has a
    ritual and that Python can call so far, 2 names in all: 'key', 'value'.
    It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Compiler::Context::KeyValuePair::~KeyValuePair()': the
      destructor: Python removes its C++ QV4::Compiler::Context::KeyValuePair
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Compiler::Context::KeyValuePair is created at the first
      use, not by 'QV4::Compiler::Context::KeyValuePair(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Compiler::Context::KeyValuePair back gives a
      copy the ritual made for Python, in a new cute
      QV4::Compiler::Context::KeyValuePair.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Compiler::Context::KeyValuePair'

    #  Qt's '~QV4::Compiler::Context::KeyValuePair()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QV4::Compiler::Context::KeyValuePair behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV48Compiler7Context12KeyValuePairD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def key(self) -> int:
      """
      Calls Qt's 'quint32 QV4::Compiler::Context::KeyValuePair::key() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compiler-context-keyvaluepair.html#key
      """
      #  quint32 QV4::Compiler::Context::KeyValuePair::key() const
      return self.uglySide.call(
          'ritual_ZNK3QV48Compiler7Context12KeyValuePair3keyEv',
      )

    def value(self) -> int:
      """
      Calls Qt's 'quint32 QV4::Compiler::Context::KeyValuePair::value()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compiler-context-keyvaluepair.html#value
      """
      #  quint32 QV4::Compiler::Context::KeyValuePair::value() const
      return self.uglySide.call(
          'ritual_ZNK3QV48Compiler7Context12KeyValuePair5valueEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QV4::Compiler::Context::KeyValuePair::KeyValuePair()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compiler-context-keyvaluepair.html
      """
      #  QV4::Compiler::Context::KeyValuePair::KeyValuePair()
      self._noteCreation(Context.KeyValuePair, lambda: Rituals.call(
          'ritual_ZN3QV48Compiler7Context12KeyValuePairC1Ev',
      ))

    @overload(int, int)
    def __init__(self, key: int, value: int) -> None:
      """
      Notes what was given, for Qt's
      'QV4::Compiler::Context::KeyValuePair::KeyValuePair(quint32 key,
      quint32 value)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compiler-context-keyvaluepair.html

      Parameters
      ----------

      key : int
        Passed on as it is.

      value : int
        Passed on as it is.
      """
      #  QV4::Compiler::Context::KeyValuePair::KeyValuePair(quint32 key,
      #      quint32 value)
      self._noteCreation(Context.KeyValuePair, lambda: Rituals.call(
          'ritual_ZN3QV48Compiler7Context12KeyValuePairC1Ejj', key, value,
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Member(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Compiler::Context::Member: a plain Python
    object standing in front of one C++ QV4::Compiler::Context::Member.

    C++ hands a QV4::Compiler::Context::Member around as a copy, so every C++
    QV4::Compiler::Context::Member behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Compiler::Context::Member that has a ritual
    and that Python can call so far, 2 names in all: 'isLexicallyScoped',
    'requiresTDZCheck'. None can be made from Python: one comes out of a
    function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Compiler::Context::Member::~Member()': the destructor:
      Python removes its C++ QV4::Compiler::Context::Member by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Compiler::Context::Member is created at the first use, not
      by 'QV4::Compiler::Context::Member(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Compiler::Context::Member back gives a copy
      the ritual made for Python, in a new cute
      QV4::Compiler::Context::Member.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Compiler::Context::Member'

    #  Qt's '~QV4::Compiler::Context::Member()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Compiler::Context::Member behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV48Compiler7Context6MemberD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isLexicallyScoped(self) -> bool:
      """
      Calls Qt's 'bool QV4::Compiler::Context::Member::isLexicallyScoped()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compiler-context-member.html
      """
      #  bool QV4::Compiler::Context::Member::isLexicallyScoped() const
      return self.uglySide.call(
          'ritual_ZNK3QV48Compiler7Context6Member17isLexicallyScopedEv',
      )

    @overload(WAIT['QQmlJS.SourceLocation'], bool)
    def requiresTDZCheck(
        self,
        accessLocation: QQmlJS.SourceLocation,
        accessAcrossContextBoundaries: bool,
    ) -> bool:
      """
      Calls Qt's 'bool QV4::Compiler::Context::Member::requiresTDZCheck(const
      QQmlJS::SourceLocation &accessLocation, bool
      accessAcrossContextBoundaries) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compiler-context-member.html

      Parameters
      ----------

      accessLocation : QQmlJS.SourceLocation
        Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
        stays Python's own.

      accessAcrossContextBoundaries : bool
        Passed on as it is.
      """
      #  bool QV4::Compiler::Context::Member::requiresTDZCheck(const
      #      QQmlJS::SourceLocation &accessLocation, bool
      #      accessAcrossContextBoundaries) const
      return self.uglySide.call(
          'ritual_ZNK3QV48Compiler7Context6Member16requiresTDZCheckERKN6QQm'
          'lJS14SourceLocationEb',
          self._valueOf(accessLocation), accessAcrossContextBoundaries,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class PropertyDependencyMap(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Compiler::Context::PropertyDependencyMap: a
    plain Python object standing in front of one C++
    QV4::Compiler::Context::PropertyDependencyMap.

    C++ hands a QV4::Compiler::Context::PropertyDependencyMap around as a
    copy, so every C++ QV4::Compiler::Context::PropertyDependencyMap behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Compiler::Context::PropertyDependencyMap that
    has a ritual and that Python can call so far, 1 name in all: 'insert'.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QV4::Compiler::Context::PropertyDependencyMap::~PropertyDependencyMap(
      )': the destructor: Python removes its C++
      QV4::Compiler::Context::PropertyDependencyMap by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QV4::Compiler::Context::PropertyDependencyMap is created at the
      first use, not by 'QV4::Compiler::Context::PropertyDependencyMap(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Compiler::Context::PropertyDependencyMap back
      gives a copy the ritual made for Python, in a new cute
      QV4::Compiler::Context::PropertyDependencyMap.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Compiler::Context::PropertyDependencyMap'

    #  Qt's '~QV4::Compiler::Context::PropertyDependencyMap()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QV4::Compiler::Context::PropertyDependencyMap behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV48Compiler7Context21PropertyDependencyMapD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int, int)
    def insert(self, key: int, value: int) -> None:
      """
      Calls Qt's 'void
      QV4::Compiler::Context::PropertyDependencyMap::insert(quint32 key,
      quint32 value)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compiler-context-propertydependencymap.html

      Parameters
      ----------

      key : int
        Passed on as it is.

      value : int
        Passed on as it is.
      """
      #  void QV4::Compiler::Context::PropertyDependencyMap::insert(quint32
      #      key, quint32 value)
      self.uglySide.call(
          'ritual_ZN3QV48Compiler7Context21PropertyDependencyMap6insertEjj',
          key, value,
      )

  class ResolvedName(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Compiler::Context::ResolvedName: a plain
    Python object standing in front of one C++
    QV4::Compiler::Context::ResolvedName.

    C++ hands a QV4::Compiler::Context::ResolvedName around as a copy, so
    every C++ QV4::Compiler::Context::ResolvedName behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Compiler::Context::ResolvedName that has a
    ritual and that Python can call so far, 1 name in all: 'isValid'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Compiler::Context::ResolvedName::~ResolvedName()': the
      destructor: Python removes its C++ QV4::Compiler::Context::ResolvedName
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Compiler::Context::ResolvedName is created at the first
      use, not by 'QV4::Compiler::Context::ResolvedName(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Compiler::Context::ResolvedName back gives a
      copy the ritual made for Python, in a new cute
      QV4::Compiler::Context::ResolvedName.
    """

    #  The enums Qt writes inside QV4::Compiler::Context::ResolvedName, each
    #  a class in here as in C++, and the names Qt has for the combinations
    #  of its flags enums.

    class Type(CuteNum):
      """
      The enum 'QV4::Compiler::Context::ResolvedName::Type' of Qt, with the 6
      names Qt gives in it.
      """

      Unresolved = Kee[int](0)
      QmlGlobal = Kee[int](1)
      Global = Kee[int](2)
      Local = Kee[int](3)
      Stack = Kee[int](4)
      Import = Kee[int](5)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Compiler::Context::ResolvedName'

    #  Qt's '~QV4::Compiler::Context::ResolvedName()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QV4::Compiler::Context::ResolvedName behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV48Compiler7Context12ResolvedNameD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QV4::Compiler::Context::ResolvedName::isValid()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compiler-context-resolvedname.html#isValid
      """
      #  bool QV4::Compiler::Context::ResolvedName::isValid() const
      return self.uglySide.call(
          'ritual_ZNK3QV48Compiler7Context12ResolvedName7isValidEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class SourceLocationTable(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Compiler::Context::SourceLocationTable: a
    plain Python object standing in front of one C++
    QV4::Compiler::Context::SourceLocationTable.

    C++ hands a QV4::Compiler::Context::SourceLocationTable around as a copy,
    so every C++ QV4::Compiler::Context::SourceLocationTable behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QV4::Compiler::Context::SourceLocationTable yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QV4::Compiler::Context::SourceLocationTable::~SourceLocationTable()':
      the destructor: Python removes its C++
      QV4::Compiler::Context::SourceLocationTable by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Compiler::Context::SourceLocationTable is created at the
      first use, not by 'QV4::Compiler::Context::SourceLocationTable(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Compiler::Context::SourceLocationTable back
      gives a copy the ritual made for Python, in a new cute
      QV4::Compiler::Context::SourceLocationTable.
    """

    #  The classes Qt writes inside
    #  QV4::Compiler::Context::SourceLocationTable, each a class in here as
    #  in C++.

    class Entry(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QV4::Compiler::Context::SourceLocationTable::Entry: a plain Python
      object standing in front of one C++
      QV4::Compiler::Context::SourceLocationTable::Entry.

      C++ hands a QV4::Compiler::Context::SourceLocationTable::Entry around
      as a copy, so every C++
      QV4::Compiler::Context::SourceLocationTable::Entry behind a cute one is
      Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QV4::Compiler::Context::SourceLocationTable::Entry
      yet. None can be made from Python: one comes out of a function of
      another class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QV4::Compiler::Context::SourceLocationTable::Entry::~Entry()':
        the destructor: Python removes its C++
        QV4::Compiler::Context::SourceLocationTable::Entry by it, and has no
        other use for it.

      What to expect
      --------------

      - The C++ QV4::Compiler::Context::SourceLocationTable::Entry is created
        at the first use, not by
        'QV4::Compiler::Context::SourceLocationTable::Entry(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a
        QV4::Compiler::Context::SourceLocationTable::Entry back gives a copy
        the ritual made for Python, in a new cute
        QV4::Compiler::Context::SourceLocationTable::Entry.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QV4::Compiler::Context::SourceLocationTable::Entry'

      #  Qt's '~QV4::Compiler::Context::SourceLocationTable::Entry()'. Naming
      #  it makes this a value class: Python owns every C++
      #  QV4::Compiler::Context::SourceLocationTable::Entry behind a cute
      #  one, and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN3QV48Compiler7Context19SourceLocationTable5EntryD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Compiler::Context::SourceLocationTable'

    #  Qt's '~QV4::Compiler::Context::SourceLocationTable()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::Compiler::Context::SourceLocationTable behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV48Compiler7Context19SourceLocationTableD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Compiler::Context'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def hasArgument(self, name: str) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::Context::hasArgument(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-context.html#hasArgument

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::Compiler::Context::hasArgument(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler7Context11hasArgumentERK7QString', name,
    )

  @overload(str)
  def findMember(self, name: str) -> Member:
    """
    Calls Qt's 'Member QV4::Compiler::Context::findMember(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-context.html#findMember

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Member
      A new cute QV4::Compiler::Context::Member around the copy Qt gave back.
      Python owns it.
    """
    #  Member QV4::Compiler::Context::findMember(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK3QV48Compiler7Context10findMemberERK7QString', name,
    )
    return QV4.Compiler.Context.Member._cuteOwning(address)

  def requiresImplicitReturnValue(self) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::Context::requiresImplicitReturnValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-context.html
    """
    #  bool QV4::Compiler::Context::requiresImplicitReturnValue() const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler7Context27requiresImplicitReturnValueEv',
    )

  def canHaveTailCalls(self) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::Context::canHaveTailCalls() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-context.html#canHaveTailCalls
    """
    #  bool QV4::Compiler::Context::canHaveTailCalls() const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler7Context16canHaveTailCallsEv',
    )

  def isCaseBlock(self) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::Context::isCaseBlock() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-context.html#isCaseBlock
    """
    #  bool QV4::Compiler::Context::isCaseBlock() const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler7Context11isCaseBlockEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS, QV4.Compiler.ContextType)
  @overload(NoneType, QV4.Compiler.ContextType)
  def __init__(
      self,
      parent: Optional[Context],
      type: QV4.Compiler.ContextType,
  ) -> None:
    """
    Notes what was given, for Qt's 'QV4::Compiler::Context::Context(Context
    *parent, ContextType type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compiler-context.html#Context

    Parameters
    ----------

    parent : Optional[Context]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QV4.Compiler.ContextType
      Passed on as its number.
    """
    #  QV4::Compiler::Context::Context(Context *parent, ContextType type)
    self._noteCreation(Context, lambda: Rituals.call(
        'ritual_ZN3QV48Compiler7ContextC1EPS1_NS0_11ContextTypeE',
        self._addressOf(parent), type.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def addUsedVariable(self, name: str) -> None:
    """
    Calls Qt's 'void QV4::Compiler::Context::addUsedVariable(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-context.html#addUsedVariable

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QV4::Compiler::Context::addUsedVariable(const QString &name)
    self.uglySide.call(
        'ritual_ZN3QV48Compiler7Context15addUsedVariableERK7QString', name,
    )

  @overload(
      str, MemberType, QQmlJS.AST.VariableScope,
      WAIT['QQmlJS.AST.FunctionExpression'], WAIT['QQmlJS.SourceLocation'],
  )
  @overload(
      str, MemberType, QQmlJS.AST.VariableScope, NoneType,
      WAIT['QQmlJS.SourceLocation'],
  )
  @overload(
      str, MemberType, QQmlJS.AST.VariableScope,
      WAIT['QQmlJS.AST.FunctionExpression'], WAIT['QQmlJS.SourceLocation'],
      bool,
  )
  @overload(
      str, MemberType, QQmlJS.AST.VariableScope, NoneType,
      WAIT['QQmlJS.SourceLocation'], bool,
  )
  def addLocalVar(
      self,
      name: str,
      contextType: MemberType,
      scope: QQmlJS.AST.VariableScope,
      function: Optional[QQmlJS.AST.FunctionExpression],
      declarationLocation: QQmlJS.SourceLocation,
      isInjected: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::Context::addLocalVar(const QString &name,
    MemberType contextType, QQmlJS::AST::VariableScope scope,
    QQmlJS::AST::FunctionExpression *function, const QQmlJS::SourceLocation
    &declarationLocation, bool isInjected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-context.html#addLocalVar

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    contextType : MemberType
      Passed on as its number.

    scope : QQmlJS.AST.VariableScope
      Passed on as its number.

    function : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    declarationLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    isInjected : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QV4::Compiler::Context::addLocalVar(const QString &name,
    #      MemberType contextType, QQmlJS::AST::VariableScope scope,
    #      QQmlJS::AST::FunctionExpression *function, const
    #      QQmlJS::SourceLocation &declarationLocation, bool isInjected)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler7Context11addLocalVarERK7QStringNS1_10Member'
        'TypeEN6QQmlJS3AST13VariableScopeEPNS7_18FunctionExpressionERKNS6_1'
        '4SourceLocationEb',
        name, contextType.value, scope.value, self._addressOf(function),
        self._valueOf(declarationLocation), isInjected,
    )

  @overload(str, WAIT['QQmlJS.SourceLocation'])
  def resolveName(
      self,
      name: str,
      accessLocation: QQmlJS.SourceLocation,
  ) -> ResolvedName:
    """
    Calls Qt's 'ResolvedName QV4::Compiler::Context::resolveName(const
    QString &name, const QQmlJS::SourceLocation &accessLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-context.html#resolveName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    accessLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    Returns
    -------

    ResolvedName
      A new cute QV4::Compiler::Context::ResolvedName around the copy Qt gave
      back. Python owns it.
    """
    #  ResolvedName QV4::Compiler::Context::resolveName(const QString &name,
    #      const QQmlJS::SourceLocation &accessLocation)
    address = self.uglySide.call(
        'ritual_ZN3QV48Compiler7Context11resolveNameERK7QStringRKN6QQmlJS14'
        'SourceLocationE',
        name, self._valueOf(accessLocation),
    )
    return QV4.Compiler.Context.ResolvedName._cuteOwning(address)

  @staticmethod
  def emitBlockFooter(*__, **_) -> Never:
    """
    Qt's 'void QV4::Compiler::Context::emitBlockFooter(Compiler::Codegen
    *codegen)': leans on
    'QV4::Moth::BytecodeGenerator::addInstructionHelper(QV4::Moth::Instr::
    Type, QV4::Moth::Instr const&, int)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Compiler.Context.emitBlockFooter' has no cute function yet. "
        "Qt's 'void "
        "QV4::Compiler::Context::emitBlockFooter(Compiler::Codegen "
        "*codegen)': leans on "
        "'QV4::Moth::BytecodeGenerator::addInstructionHelper(QV4::Moth::Inst"
        "r::Type, QV4::Moth::Instr const&, int)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def emitBlockHeader(*__, **_) -> Never:
    """
    Qt's 'void QV4::Compiler::Context::emitBlockHeader(Compiler::Codegen
    *codegen)': leans on 'QV4::Moth::BytecodeGenerator::newRegister()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Compiler.Context.emitBlockHeader' has no cute function yet. "
        "Qt's 'void "
        "QV4::Compiler::Context::emitBlockHeader(Compiler::Codegen "
        "*codegen)': leans on "
        "'QV4::Moth::BytecodeGenerator::newRegister()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def findArgument(*__, **_) -> Never:
    """
    Qt's 'int QV4::Compiler::Context::findArgument(const QString &name, bool
    *isInjected) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QV4.Compiler.Context.findArgument' has no cute function yet. Qt's "
        "'int QV4::Compiler::Context::findArgument(const QString &name, "
        "bool *isInjected) const': takes a number to change where it is.")

  @staticmethod
  def memberInfo(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Compiler::Context::memberInfo(const QString &name, const
    Member **m) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.Context.memberInfo' has no cute function yet. Qt's "
        "'bool QV4::Compiler::Context::memberInfo(const QString &name, "
        "const Member **m) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setupFunctionIndices(*__, **_) -> Never:
    """
    Qt's 'void
    QV4::Compiler::Context::setupFunctionIndices(Moth::BytecodeGenerator
    *bytecodeGenerator)': leans on
    'QV4::Moth::BytecodeGenerator::newRegister()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Compiler.Context.setupFunctionIndices' has no cute function "
        "yet. Qt's 'void "
        "QV4::Compiler::Context::setupFunctionIndices(Moth::BytecodeGenerato"
        "r *bytecodeGenerator)': leans on "
        "'QV4::Moth::BytecodeGenerator::newRegister()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
