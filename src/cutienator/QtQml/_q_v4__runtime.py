"""
QV4::Runtime binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Runtime to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Runtime(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Runtime: a plain Python object standing in front
  of one C++ QV4::Runtime.

  C++ hands a QV4::Runtime around as a copy, so every C++ QV4::Runtime behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QV4::Runtime yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHash<const void *, const char *> QV4::Runtime::symbolTable()':
    gives a type Python has no way to take yet.
  - Qt's 'QV4::Runtime::~Runtime()': the destructor: Python removes its C++
    QV4::Runtime by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::Runtime is created at the first use, not by
    'QV4::Runtime(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Runtime back gives a copy the ritual made for
    Python, in a new cute QV4::Runtime.
  - Each name of Qt's QV4::Runtime that has no cute function yet,
    'symbolTable', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QV4::Runtime, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ChangesContext(CuteNum, scoped=True):
    """
    The enum 'QV4::Runtime::ChangesContext' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  class LastArgumentIsOutputValue(CuteNum, scoped=True):
    """
    The enum 'QV4::Runtime::LastArgumentIsOutputValue' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  class Pure(CuteNum, scoped=True):
    """
    The enum 'QV4::Runtime::Pure' of Qt, with the 2 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  class Throws(CuteNum, scoped=True):
    """
    The enum 'QV4::Runtime::Throws' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  #  The classes Qt writes inside QV4::Runtime, each a class in here as in
  #  C++.

  class Add(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Add: a plain Python object standing
    in front of one C++ QV4::Runtime::Add.

    C++ hands a QV4::Runtime::Add around as a copy, so every C++
    QV4::Runtime::Add behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Add that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Add::~Add()': the destructor: Python removes its
      C++ QV4::Runtime::Add by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Add is created at the first use, not by
      'QV4::Runtime::Add(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Add back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::Add.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Add::call(ExecutionEngine *a0,
      const Value &a1, const Value &a2)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-add.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Add::call(ExecutionEngine *a0, const
      #      Value &a1, const Value &a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime3Add4callEPNS_15ExecutionEngineERKNS_5Value'
          'ES6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Add'

    #  Qt's '~QV4::Runtime::Add()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Add behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime3AddD1Ev'

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

  class ArrayLiteral(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ArrayLiteral: a plain Python object
    standing in front of one C++ QV4::Runtime::ArrayLiteral.

    C++ hands a QV4::Runtime::ArrayLiteral around as a copy, so every C++
    QV4::Runtime::ArrayLiteral behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ArrayLiteral that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ArrayLiteral::~ArrayLiteral()': the destructor:
      Python removes its C++ QV4::Runtime::ArrayLiteral by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ArrayLiteral is created at the first use, not by
      'QV4::Runtime::ArrayLiteral(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ArrayLiteral back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::ArrayLiteral.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], int)
    @overload(WAIT['QV4.ExecutionEngine'], NoneType, int)
    @overload(NoneType, WAIT['QV4.Value'], int)
    @overload(NoneType, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: Optional[QV4.Value],
        a2: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::ArrayLiteral::call(ExecutionEngine *a0, Value *a1, uint
      a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-arrayliteral.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a2 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::ArrayLiteral::call(ExecutionEngine *a0,
      #      Value *a1, uint a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime12ArrayLiteral4callEPNS_15ExecutionEngineEP'
          'NS_5ValueEj',
          CuteMixin._addressOf(a0), CuteMixin._addressOf(a1), a2,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ArrayLiteral'

    #  Qt's '~QV4::Runtime::ArrayLiteral()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::ArrayLiteral behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime12ArrayLiteralD1Ev'

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

  class As(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::As: a plain Python object standing in
    front of one C++ QV4::Runtime::As.

    C++ hands a QV4::Runtime::As around as a copy, so every C++
    QV4::Runtime::As behind a cute one is Python's own: it is removed, by the
    ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::As that has a ritual and that Python
    can call so far, 1 name in all: 'call'. None can be made from Python: one
    comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::As::~As()': the destructor: Python removes its C++
      QV4::Runtime::As by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::As is created at the first use, not by
      'QV4::Runtime::As(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::As back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::As.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::As::call(ExecutionEngine *a0,
      const Value &a1, const Value &a2)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-as.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::As::call(ExecutionEngine *a0, const
      #      Value &a1, const Value &a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime2As4callEPNS_15ExecutionEngineERKNS_5ValueE'
          'S6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::As'

    #  Qt's '~QV4::Runtime::As()'. Naming it makes this a value class: Python
    #  owns every C++ QV4::Runtime::As behind a cute one, and removes it by
    #  this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime2AsD1Ev'

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

  class BitAnd(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::BitAnd: a plain Python object
    standing in front of one C++ QV4::Runtime::BitAnd.

    C++ hands a QV4::Runtime::BitAnd around as a copy, so every C++
    QV4::Runtime::BitAnd behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::BitAnd that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::BitAnd::~BitAnd()': the destructor: Python removes
      its C++ QV4::Runtime::BitAnd by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::BitAnd is created at the first use, not by
      'QV4::Runtime::BitAnd(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::BitAnd back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::BitAnd.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::BitAnd::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-bitand.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::BitAnd::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime6BitAnd4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::BitAnd'

    #  Qt's '~QV4::Runtime::BitAnd()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::BitAnd behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime6BitAndD1Ev'

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

  class BitOr(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::BitOr: a plain Python object standing
    in front of one C++ QV4::Runtime::BitOr.

    C++ hands a QV4::Runtime::BitOr around as a copy, so every C++
    QV4::Runtime::BitOr behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::BitOr that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::BitOr::~BitOr()': the destructor: Python removes
      its C++ QV4::Runtime::BitOr by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::BitOr is created at the first use, not by
      'QV4::Runtime::BitOr(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::BitOr back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::BitOr.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::BitOr::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-bitor.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::BitOr::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime5BitOr4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::BitOr'

    #  Qt's '~QV4::Runtime::BitOr()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::BitOr behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime5BitOrD1Ev'

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

  class BitXor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::BitXor: a plain Python object
    standing in front of one C++ QV4::Runtime::BitXor.

    C++ hands a QV4::Runtime::BitXor around as a copy, so every C++
    QV4::Runtime::BitXor behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::BitXor that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::BitXor::~BitXor()': the destructor: Python removes
      its C++ QV4::Runtime::BitXor by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::BitXor is created at the first use, not by
      'QV4::Runtime::BitXor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::BitXor back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::BitXor.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::BitXor::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-bitxor.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::BitXor::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime6BitXor4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::BitXor'

    #  Qt's '~QV4::Runtime::BitXor()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::BitXor behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime6BitXorD1Ev'

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

  class CallGlobalLookup(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CallGlobalLookup: a plain Python
    object standing in front of one C++ QV4::Runtime::CallGlobalLookup.

    C++ hands a QV4::Runtime::CallGlobalLookup around as a copy, so every C++
    QV4::Runtime::CallGlobalLookup behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CallGlobalLookup that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CallGlobalLookup::~CallGlobalLookup()': the
      destructor: Python removes its C++ QV4::Runtime::CallGlobalLookup by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CallGlobalLookup is created at the first use, not
      by 'QV4::Runtime::CallGlobalLookup(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CallGlobalLookup back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CallGlobalLookup.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'], int)
    @overload(WAIT['QV4.ExecutionEngine'], int, NoneType, int)
    @overload(NoneType, int, WAIT['QV4.Value'], int)
    @overload(NoneType, int, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: int,
        a2: Optional[QV4.Value],
        a3: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CallGlobalLookup::call(ExecutionEngine *a0, uint a1,
      Value *a2, int a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-callgloballookup.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.

      a2 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a3 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::CallGlobalLookup::call(ExecutionEngine
      #      *a0, uint a1, Value *a2, int a3)
      return Rituals.call(
          'ritual_ZN3QV47Runtime16CallGlobalLookup4callEPNS_15ExecutionEngi'
          'neEjPNS_5ValueEi',
          CuteMixin._addressOf(a0), a1, CuteMixin._addressOf(a2), a3,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CallGlobalLookup'

    #  Qt's '~QV4::Runtime::CallGlobalLookup()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::CallGlobalLookup behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime16CallGlobalLookupD1Ev'

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

  class CallName(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CallName: a plain Python object
    standing in front of one C++ QV4::Runtime::CallName.

    C++ hands a QV4::Runtime::CallName around as a copy, so every C++
    QV4::Runtime::CallName behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CallName that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CallName::~CallName()': the destructor: Python
      removes its C++ QV4::Runtime::CallName by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CallName is created at the first use, not by
      'QV4::Runtime::CallName(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CallName back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::CallName.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'], int)
    @overload(WAIT['QV4.ExecutionEngine'], int, NoneType, int)
    @overload(NoneType, int, WAIT['QV4.Value'], int)
    @overload(NoneType, int, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: int,
        a2: Optional[QV4.Value],
        a3: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::CallName::call(ExecutionEngine
      *a0, int a1, Value *a2, int a3)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-callname.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.

      a2 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a3 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::CallName::call(ExecutionEngine *a0, int
      #      a1, Value *a2, int a3)
      return Rituals.call(
          'ritual_ZN3QV47Runtime8CallName4callEPNS_15ExecutionEngineEiPNS_5'
          'ValueEi',
          CuteMixin._addressOf(a0), a1, CuteMixin._addressOf(a2), a3,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CallName'

    #  Qt's '~QV4::Runtime::CallName()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::CallName behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime8CallNameD1Ev'

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

  class CallPossiblyDirectEval(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CallPossiblyDirectEval: a plain
    Python object standing in front of one C++
    QV4::Runtime::CallPossiblyDirectEval.

    C++ hands a QV4::Runtime::CallPossiblyDirectEval around as a copy, so
    every C++ QV4::Runtime::CallPossiblyDirectEval behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CallPossiblyDirectEval that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CallPossiblyDirectEval::~CallPossiblyDirectEval()':
      the destructor: Python removes its C++
      QV4::Runtime::CallPossiblyDirectEval by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CallPossiblyDirectEval is created at the first
      use, not by 'QV4::Runtime::CallPossiblyDirectEval(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CallPossiblyDirectEval back gives a
      copy the ritual made for Python, in a new cute
      QV4::Runtime::CallPossiblyDirectEval.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], int)
    @overload(WAIT['QV4.ExecutionEngine'], NoneType, int)
    @overload(NoneType, WAIT['QV4.Value'], int)
    @overload(NoneType, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: Optional[QV4.Value],
        a2: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CallPossiblyDirectEval::call(ExecutionEngine *a0, Value
      *a1, int a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-callpossiblydirecteval.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a2 : int
        Passed on as it is.
      """
      #  ReturnedValue
      #      QV4::Runtime::CallPossiblyDirectEval::call(ExecutionEngine *a0,
      #      Value *a1, int a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime22CallPossiblyDirectEval4callEPNS_15Executi'
          'onEngineEPNS_5ValueEi',
          CuteMixin._addressOf(a0), CuteMixin._addressOf(a1), a2,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CallPossiblyDirectEval'

    #  Qt's '~QV4::Runtime::CallPossiblyDirectEval()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QV4::Runtime::CallPossiblyDirectEval behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime22CallPossiblyDirectEvalD1Ev'

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

  class CallProperty(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CallProperty: a plain Python object
    standing in front of one C++ QV4::Runtime::CallProperty.

    C++ hands a QV4::Runtime::CallProperty around as a copy, so every C++
    QV4::Runtime::CallProperty behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CallProperty that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CallProperty::~CallProperty()': the destructor:
      Python removes its C++ QV4::Runtime::CallProperty by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CallProperty is created at the first use, not by
      'QV4::Runtime::CallProperty(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CallProperty back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::CallProperty.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], int,
        WAIT['QV4.Value'], int,
    )
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], int, NoneType, int,
    )
    @overload(NoneType, WAIT['QV4.Value'], int, WAIT['QV4.Value'], int)
    @overload(NoneType, WAIT['QV4.Value'], int, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: int,
        a3: Optional[QV4.Value],
        a4: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CallProperty::call(ExecutionEngine *a0, const Value &a1,
      int a2, Value *a3, int a4)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-callproperty.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : int
        Passed on as it is.

      a3 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a4 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::CallProperty::call(ExecutionEngine *a0,
      #      const Value &a1, int a2, Value *a3, int a4)
      return Rituals.call(
          'ritual_ZN3QV47Runtime12CallProperty4callEPNS_15ExecutionEngineER'
          'KNS_5ValueEiPS4_i',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
          CuteMixin._addressOf(a3), a4,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CallProperty'

    #  Qt's '~QV4::Runtime::CallProperty()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::CallProperty behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime12CallPropertyD1Ev'

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

  class CallPropertyLookup(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CallPropertyLookup: a plain Python
    object standing in front of one C++ QV4::Runtime::CallPropertyLookup.

    C++ hands a QV4::Runtime::CallPropertyLookup around as a copy, so every
    C++ QV4::Runtime::CallPropertyLookup behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CallPropertyLookup that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CallPropertyLookup::~CallPropertyLookup()': the
      destructor: Python removes its C++ QV4::Runtime::CallPropertyLookup by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CallPropertyLookup is created at the first use,
      not by 'QV4::Runtime::CallPropertyLookup(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CallPropertyLookup back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CallPropertyLookup.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], int,
        WAIT['QV4.Value'], int,
    )
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], int, NoneType, int,
    )
    @overload(NoneType, WAIT['QV4.Value'], int, WAIT['QV4.Value'], int)
    @overload(NoneType, WAIT['QV4.Value'], int, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: int,
        a3: Optional[QV4.Value],
        a4: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CallPropertyLookup::call(ExecutionEngine *a0, const Value
      &a1, uint a2, Value *a3, int a4)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-callpropertylookup.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : int
        Passed on as it is.

      a3 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a4 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::CallPropertyLookup::call(ExecutionEngine
      #      *a0, const Value &a1, uint a2, Value *a3, int a4)
      return Rituals.call(
          'ritual_ZN3QV47Runtime18CallPropertyLookup4callEPNS_15ExecutionEn'
          'gineERKNS_5ValueEjPS4_i',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
          CuteMixin._addressOf(a3), a4,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CallPropertyLookup'

    #  Qt's '~QV4::Runtime::CallPropertyLookup()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::CallPropertyLookup
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime18CallPropertyLookupD1Ev'

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

  class CallQmlContextPropertyLookup(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CallQmlContextPropertyLookup: a plain
    Python object standing in front of one C++
    QV4::Runtime::CallQmlContextPropertyLookup.

    C++ hands a QV4::Runtime::CallQmlContextPropertyLookup around as a copy,
    so every C++ QV4::Runtime::CallQmlContextPropertyLookup behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CallQmlContextPropertyLookup that
    has a ritual and that Python can call so far, 1 name in all: 'call'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CallQmlContextPropertyLookup::
      ~CallQmlContextPropertyLookup()': the destructor: Python removes its
      C++ QV4::Runtime::CallQmlContextPropertyLookup by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CallQmlContextPropertyLookup is created at the
      first use, not by 'QV4::Runtime::CallQmlContextPropertyLookup(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CallQmlContextPropertyLookup back
      gives a copy the ritual made for Python, in a new cute
      QV4::Runtime::CallQmlContextPropertyLookup.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'], int)
    @overload(WAIT['QV4.ExecutionEngine'], int, NoneType, int)
    @overload(NoneType, int, WAIT['QV4.Value'], int)
    @overload(NoneType, int, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: int,
        a2: Optional[QV4.Value],
        a3: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CallQmlContextPropertyLookup::call(ExecutionEngine *a0,
      uint a1, Value *a2, int a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-callqmlcontextpropertylookup.html

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.

      a2 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a3 : int
        Passed on as it is.
      """
      #  ReturnedValue
      #      QV4::Runtime::CallQmlContextPropertyLookup::call(ExecutionEngine
      #      *a0, uint a1, Value *a2, int a3)
      return Rituals.call(
          'ritual_ZN3QV47Runtime28CallQmlContextPropertyLookup4callEPNS_15E'
          'xecutionEngineEjPNS_5ValueEi',
          CuteMixin._addressOf(a0), a1, CuteMixin._addressOf(a2), a3,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CallQmlContextPropertyLookup'

    #  Qt's '~QV4::Runtime::CallQmlContextPropertyLookup()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::Runtime::CallQmlContextPropertyLookup behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV47Runtime28CallQmlContextPropertyLookupD1Ev')

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

  class CallValue(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CallValue: a plain Python object
    standing in front of one C++ QV4::Runtime::CallValue.

    C++ hands a QV4::Runtime::CallValue around as a copy, so every C++
    QV4::Runtime::CallValue behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CallValue that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CallValue::~CallValue()': the destructor: Python
      removes its C++ QV4::Runtime::CallValue by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CallValue is created at the first use, not by
      'QV4::Runtime::CallValue(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CallValue back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::CallValue.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        int,
    )
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], NoneType, int)
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
    @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: Optional[QV4.Value],
        a3: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::CallValue::call(ExecutionEngine
      *a0, const Value &a1, Value *a2, int a3)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-callvalue.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a3 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::CallValue::call(ExecutionEngine *a0,
      #      const Value &a1, Value *a2, int a3)
      return Rituals.call(
          'ritual_ZN3QV47Runtime9CallValue4callEPNS_15ExecutionEngineERKNS_'
          '5ValueEPS4_i',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._addressOf(a2), a3,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CallValue'

    #  Qt's '~QV4::Runtime::CallValue()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::CallValue behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime9CallValueD1Ev'

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

  class CallWithReceiver(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CallWithReceiver: a plain Python
    object standing in front of one C++ QV4::Runtime::CallWithReceiver.

    C++ hands a QV4::Runtime::CallWithReceiver around as a copy, so every C++
    QV4::Runtime::CallWithReceiver behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CallWithReceiver that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CallWithReceiver::~CallWithReceiver()': the
      destructor: Python removes its C++ QV4::Runtime::CallWithReceiver by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CallWithReceiver is created at the first use, not
      by 'QV4::Runtime::CallWithReceiver(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CallWithReceiver back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CallWithReceiver.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        WAIT['QV4.Value'], int,
    )
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        NoneType, int,
    )
    @overload(
        NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        int,
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
        a3: Optional[QV4.Value],
        a4: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CallWithReceiver::call(ExecutionEngine *a0, const Value
      &a1, const Value &a2, Value *a3, int a4)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-callwithreceiver.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a3 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a4 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::CallWithReceiver::call(ExecutionEngine
      #      *a0, const Value &a1, const Value &a2, Value *a3, int a4)
      return Rituals.call(
          'ritual_ZN3QV47Runtime16CallWithReceiver4callEPNS_15ExecutionEngi'
          'neERKNS_5ValueES6_PS4_i',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2), CuteMixin._addressOf(a3), a4,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CallWithReceiver'

    #  Qt's '~QV4::Runtime::CallWithReceiver()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::CallWithReceiver behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime16CallWithReceiverD1Ev'

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

  class CallWithSpread(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CallWithSpread: a plain Python object
    standing in front of one C++ QV4::Runtime::CallWithSpread.

    C++ hands a QV4::Runtime::CallWithSpread around as a copy, so every C++
    QV4::Runtime::CallWithSpread behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CallWithSpread that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CallWithSpread::~CallWithSpread()': the destructor:
      Python removes its C++ QV4::Runtime::CallWithSpread by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CallWithSpread is created at the first use, not
      by 'QV4::Runtime::CallWithSpread(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CallWithSpread back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::CallWithSpread.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        WAIT['QV4.Value'], int,
    )
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        NoneType, int,
    )
    @overload(
        NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        int,
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
        a3: Optional[QV4.Value],
        a4: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CallWithSpread::call(ExecutionEngine *a0, const Value
      &a1, const Value &a2, Value *a3, int a4)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-callwithspread.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a3 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a4 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::CallWithSpread::call(ExecutionEngine
      #      *a0, const Value &a1, const Value &a2, Value *a3, int a4)
      return Rituals.call(
          'ritual_ZN3QV47Runtime14CallWithSpread4callEPNS_15ExecutionEngine'
          'ERKNS_5ValueES6_PS4_i',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2), CuteMixin._addressOf(a3), a4,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CallWithSpread'

    #  Qt's '~QV4::Runtime::CallWithSpread()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::CallWithSpread behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime14CallWithSpreadD1Ev'

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

  class CloneBlockContext(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CloneBlockContext: a plain Python
    object standing in front of one C++ QV4::Runtime::CloneBlockContext.

    C++ hands a QV4::Runtime::CloneBlockContext around as a copy, so every
    C++ QV4::Runtime::CloneBlockContext behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CloneBlockContext that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CloneBlockContext::~CloneBlockContext()': the
      destructor: Python removes its C++ QV4::Runtime::CloneBlockContext by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CloneBlockContext is created at the first use,
      not by 'QV4::Runtime::CloneBlockContext(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CloneBlockContext back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CloneBlockContext.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'])
    @overload(NoneType)
    def call(a0: Optional[QV4.ExecutionEngine]) -> None:
      """
      Calls Qt's 'void QV4::Runtime::CloneBlockContext::call(ExecutionEngine
      *a0)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-cloneblockcontext.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QV4::Runtime::CloneBlockContext::call(ExecutionEngine *a0)
      Rituals.call(
          'ritual_ZN3QV47Runtime17CloneBlockContext4callEPNS_15ExecutionEng'
          'ineE',
          CuteMixin._addressOf(a0),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CloneBlockContext'

    #  Qt's '~QV4::Runtime::CloneBlockContext()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::CloneBlockContext
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime17CloneBlockContextD1Ev'

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

  class Closure(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Closure: a plain Python object
    standing in front of one C++ QV4::Runtime::Closure.

    C++ hands a QV4::Runtime::Closure around as a copy, so every C++
    QV4::Runtime::Closure behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Closure that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Closure::~Closure()': the destructor: Python
      removes its C++ QV4::Runtime::Closure by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Closure is created at the first use, not by
      'QV4::Runtime::Closure(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Closure back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::Closure.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Closure::call(ExecutionEngine
      *a0, int a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-closure.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::Closure::call(ExecutionEngine *a0, int
      #      a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime7Closure4callEPNS_15ExecutionEngineEi',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Closure'

    #  Qt's '~QV4::Runtime::Closure()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Closure behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime7ClosureD1Ev'

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

  class CompareEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareEqual: a plain Python object
    standing in front of one C++ QV4::Runtime::CompareEqual.

    C++ hands a QV4::Runtime::CompareEqual around as a copy, so every C++
    QV4::Runtime::CompareEqual behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareEqual that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareEqual::~CompareEqual()': the destructor:
      Python removes its C++ QV4::Runtime::CompareEqual by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareEqual is created at the first use, not by
      'QV4::Runtime::CompareEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareEqual back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::CompareEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareEqual::call(const Value &a0,
      const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-compareequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareEqual::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime12CompareEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareEqual'

    #  Qt's '~QV4::Runtime::CompareEqual()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::CompareEqual behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime12CompareEqualD1Ev'

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

  class CompareGreaterEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareGreaterEqual: a plain Python
    object standing in front of one C++ QV4::Runtime::CompareGreaterEqual.

    C++ hands a QV4::Runtime::CompareGreaterEqual around as a copy, so every
    C++ QV4::Runtime::CompareGreaterEqual behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareGreaterEqual that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareGreaterEqual::~CompareGreaterEqual()': the
      destructor: Python removes its C++ QV4::Runtime::CompareGreaterEqual by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareGreaterEqual is created at the first use,
      not by 'QV4::Runtime::CompareGreaterEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareGreaterEqual back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CompareGreaterEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareGreaterEqual::call(const Value
      &a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-comparegreaterequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareGreaterEqual::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime19CompareGreaterEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareGreaterEqual'

    #  Qt's '~QV4::Runtime::CompareGreaterEqual()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::CompareGreaterEqual
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime19CompareGreaterEqualD1Ev'

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

  class CompareGreaterThan(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareGreaterThan: a plain Python
    object standing in front of one C++ QV4::Runtime::CompareGreaterThan.

    C++ hands a QV4::Runtime::CompareGreaterThan around as a copy, so every
    C++ QV4::Runtime::CompareGreaterThan behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareGreaterThan that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareGreaterThan::~CompareGreaterThan()': the
      destructor: Python removes its C++ QV4::Runtime::CompareGreaterThan by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareGreaterThan is created at the first use,
      not by 'QV4::Runtime::CompareGreaterThan(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareGreaterThan back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CompareGreaterThan.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareGreaterThan::call(const Value
      &a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-comparegreaterthan.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareGreaterThan::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime18CompareGreaterThan4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareGreaterThan'

    #  Qt's '~QV4::Runtime::CompareGreaterThan()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::CompareGreaterThan
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime18CompareGreaterThanD1Ev'

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

  class CompareIn(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareIn: a plain Python object
    standing in front of one C++ QV4::Runtime::CompareIn.

    C++ hands a QV4::Runtime::CompareIn around as a copy, so every C++
    QV4::Runtime::CompareIn behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareIn that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareIn::~CompareIn()': the destructor: Python
      removes its C++ QV4::Runtime::CompareIn by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareIn is created at the first use, not by
      'QV4::Runtime::CompareIn(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareIn back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::CompareIn.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
    ) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareIn::call(ExecutionEngine *a0,
      const Value &a1, const Value &a2)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-comparein.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareIn::call(ExecutionEngine *a0, const Value
      #      &a1, const Value &a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime9CompareIn4callEPNS_15ExecutionEngineERKNS_'
          '5ValueES6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareIn'

    #  Qt's '~QV4::Runtime::CompareIn()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::CompareIn behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime9CompareInD1Ev'

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

  class CompareInstanceof(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareInstanceof: a plain Python
    object standing in front of one C++ QV4::Runtime::CompareInstanceof.

    C++ hands a QV4::Runtime::CompareInstanceof around as a copy, so every
    C++ QV4::Runtime::CompareInstanceof behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareInstanceof that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareInstanceof::~CompareInstanceof()': the
      destructor: Python removes its C++ QV4::Runtime::CompareInstanceof by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareInstanceof is created at the first use,
      not by 'QV4::Runtime::CompareInstanceof(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareInstanceof back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CompareInstanceof.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
    ) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareInstanceof::call(ExecutionEngine
      *a0, const Value &a1, const Value &a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-compareinstanceof.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareInstanceof::call(ExecutionEngine *a0,
      #      const Value &a1, const Value &a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime17CompareInstanceof4callEPNS_15ExecutionEng'
          'ineERKNS_5ValueES6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareInstanceof'

    #  Qt's '~QV4::Runtime::CompareInstanceof()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::CompareInstanceof
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime17CompareInstanceofD1Ev'

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

  class CompareLessEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareLessEqual: a plain Python
    object standing in front of one C++ QV4::Runtime::CompareLessEqual.

    C++ hands a QV4::Runtime::CompareLessEqual around as a copy, so every C++
    QV4::Runtime::CompareLessEqual behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareLessEqual that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareLessEqual::~CompareLessEqual()': the
      destructor: Python removes its C++ QV4::Runtime::CompareLessEqual by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareLessEqual is created at the first use, not
      by 'QV4::Runtime::CompareLessEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareLessEqual back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CompareLessEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareLessEqual::call(const Value &a0,
      const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-comparelessequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareLessEqual::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime16CompareLessEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareLessEqual'

    #  Qt's '~QV4::Runtime::CompareLessEqual()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::CompareLessEqual behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime16CompareLessEqualD1Ev'

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

  class CompareLessThan(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareLessThan: a plain Python
    object standing in front of one C++ QV4::Runtime::CompareLessThan.

    C++ hands a QV4::Runtime::CompareLessThan around as a copy, so every C++
    QV4::Runtime::CompareLessThan behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareLessThan that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareLessThan::~CompareLessThan()': the
      destructor: Python removes its C++ QV4::Runtime::CompareLessThan by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareLessThan is created at the first use, not
      by 'QV4::Runtime::CompareLessThan(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareLessThan back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::CompareLessThan.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareLessThan::call(const Value &a0,
      const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-comparelessthan.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareLessThan::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime15CompareLessThan4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareLessThan'

    #  Qt's '~QV4::Runtime::CompareLessThan()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::CompareLessThan behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime15CompareLessThanD1Ev'

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

  class CompareNotEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareNotEqual: a plain Python
    object standing in front of one C++ QV4::Runtime::CompareNotEqual.

    C++ hands a QV4::Runtime::CompareNotEqual around as a copy, so every C++
    QV4::Runtime::CompareNotEqual behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareNotEqual that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareNotEqual::~CompareNotEqual()': the
      destructor: Python removes its C++ QV4::Runtime::CompareNotEqual by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareNotEqual is created at the first use, not
      by 'QV4::Runtime::CompareNotEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareNotEqual back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::CompareNotEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareNotEqual::call(const Value &a0,
      const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-comparenotequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareNotEqual::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime15CompareNotEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareNotEqual'

    #  Qt's '~QV4::Runtime::CompareNotEqual()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::CompareNotEqual behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime15CompareNotEqualD1Ev'

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

  class CompareStrictEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareStrictEqual: a plain Python
    object standing in front of one C++ QV4::Runtime::CompareStrictEqual.

    C++ hands a QV4::Runtime::CompareStrictEqual around as a copy, so every
    C++ QV4::Runtime::CompareStrictEqual behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareStrictEqual that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareStrictEqual::~CompareStrictEqual()': the
      destructor: Python removes its C++ QV4::Runtime::CompareStrictEqual by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareStrictEqual is created at the first use,
      not by 'QV4::Runtime::CompareStrictEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareStrictEqual back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CompareStrictEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareStrictEqual::call(const Value
      &a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-comparestrictequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareStrictEqual::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime18CompareStrictEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareStrictEqual'

    #  Qt's '~QV4::Runtime::CompareStrictEqual()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::CompareStrictEqual
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime18CompareStrictEqualD1Ev'

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

  class CompareStrictNotEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CompareStrictNotEqual: a plain Python
    object standing in front of one C++ QV4::Runtime::CompareStrictNotEqual.

    C++ hands a QV4::Runtime::CompareStrictNotEqual around as a copy, so
    every C++ QV4::Runtime::CompareStrictNotEqual behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CompareStrictNotEqual that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CompareStrictNotEqual::~CompareStrictNotEqual()':
      the destructor: Python removes its C++
      QV4::Runtime::CompareStrictNotEqual by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CompareStrictNotEqual is created at the first
      use, not by 'QV4::Runtime::CompareStrictNotEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CompareStrictNotEqual back gives a
      copy the ritual made for Python, in a new cute
      QV4::Runtime::CompareStrictNotEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::CompareStrictNotEqual::call(const Value
      &a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-comparestrictnotequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::CompareStrictNotEqual::call(const Value &a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime21CompareStrictNotEqual4callERKNS_5ValueES4'
          '_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CompareStrictNotEqual'

    #  Qt's '~QV4::Runtime::CompareStrictNotEqual()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::CompareStrictNotEqual
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime21CompareStrictNotEqualD1Ev'

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

  class Construct(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Construct: a plain Python object
    standing in front of one C++ QV4::Runtime::Construct.

    C++ hands a QV4::Runtime::Construct around as a copy, so every C++
    QV4::Runtime::Construct behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Construct that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Construct::~Construct()': the destructor: Python
      removes its C++ QV4::Runtime::Construct by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Construct is created at the first use, not by
      'QV4::Runtime::Construct(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Construct back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::Construct.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        WAIT['QV4.Value'], int,
    )
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        NoneType, int,
    )
    @overload(
        NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        int,
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
        a3: Optional[QV4.Value],
        a4: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Construct::call(ExecutionEngine
      *a0, const Value &a1, const Value &a2, Value *a3, int a4)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-construct.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a3 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a4 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::Construct::call(ExecutionEngine *a0,
      #      const Value &a1, const Value &a2, Value *a3, int a4)
      return Rituals.call(
          'ritual_ZN3QV47Runtime9Construct4callEPNS_15ExecutionEngineERKNS_'
          '5ValueES6_PS4_i',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2), CuteMixin._addressOf(a3), a4,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Construct'

    #  Qt's '~QV4::Runtime::Construct()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Construct behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime9ConstructD1Ev'

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

  class ConstructWithSpread(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ConstructWithSpread: a plain Python
    object standing in front of one C++ QV4::Runtime::ConstructWithSpread.

    C++ hands a QV4::Runtime::ConstructWithSpread around as a copy, so every
    C++ QV4::Runtime::ConstructWithSpread behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ConstructWithSpread that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ConstructWithSpread::~ConstructWithSpread()': the
      destructor: Python removes its C++ QV4::Runtime::ConstructWithSpread by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ConstructWithSpread is created at the first use,
      not by 'QV4::Runtime::ConstructWithSpread(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ConstructWithSpread back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::ConstructWithSpread.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        WAIT['QV4.Value'], int,
    )
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        NoneType, int,
    )
    @overload(
        NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        int,
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
        a3: Optional[QV4.Value],
        a4: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::ConstructWithSpread::call(ExecutionEngine *a0, const
      Value &a1, const Value &a2, Value *a3, int a4)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-constructwithspread.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a3 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a4 : int
        Passed on as it is.
      """
      #  ReturnedValue
      #      QV4::Runtime::ConstructWithSpread::call(ExecutionEngine *a0,
      #      const Value &a1, const Value &a2, Value *a3, int a4)
      return Rituals.call(
          'ritual_ZN3QV47Runtime19ConstructWithSpread4callEPNS_15ExecutionE'
          'ngineERKNS_5ValueES6_PS4_i',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2), CuteMixin._addressOf(a3), a4,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ConstructWithSpread'

    #  Qt's '~QV4::Runtime::ConstructWithSpread()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::ConstructWithSpread
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime19ConstructWithSpreadD1Ev'

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

  class ConvertThisToObject(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ConvertThisToObject: a plain Python
    object standing in front of one C++ QV4::Runtime::ConvertThisToObject.

    C++ hands a QV4::Runtime::ConvertThisToObject around as a copy, so every
    C++ QV4::Runtime::ConvertThisToObject behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ConvertThisToObject that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ConvertThisToObject::~ConvertThisToObject()': the
      destructor: Python removes its C++ QV4::Runtime::ConvertThisToObject by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ConvertThisToObject is created at the first use,
      not by 'QV4::Runtime::ConvertThisToObject(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ConvertThisToObject back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::ConvertThisToObject.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::ConvertThisToObject::call(ExecutionEngine *a0, const
      Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-convertthistoobject.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue
      #      QV4::Runtime::ConvertThisToObject::call(ExecutionEngine *a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime19ConvertThisToObject4callEPNS_15ExecutionE'
          'ngineERKNS_5ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ConvertThisToObject'

    #  Qt's '~QV4::Runtime::ConvertThisToObject()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::ConvertThisToObject
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime19ConvertThisToObjectD1Ev'

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

  class CreateClass(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CreateClass: a plain Python object
    standing in front of one C++ QV4::Runtime::CreateClass.

    C++ hands a QV4::Runtime::CreateClass around as a copy, so every C++
    QV4::Runtime::CreateClass behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CreateClass that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CreateClass::~CreateClass()': the destructor:
      Python removes its C++ QV4::Runtime::CreateClass by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CreateClass is created at the first use, not by
      'QV4::Runtime::CreateClass(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CreateClass back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::CreateClass.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'],
        WAIT['QV4.Value'],
    )
    @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'], NoneType)
    @overload(NoneType, int, WAIT['QV4.Value'], WAIT['QV4.Value'])
    @overload(NoneType, int, WAIT['QV4.Value'], NoneType)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: int,
        a2: QV4.Value,
        a3: Optional[QV4.Value],
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CreateClass::call(ExecutionEngine *a0, int a1, const
      Value &a2, Value *a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-createclass.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a3 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  ReturnedValue QV4::Runtime::CreateClass::call(ExecutionEngine *a0,
      #      int a1, const Value &a2, Value *a3)
      return Rituals.call(
          'ritual_ZN3QV47Runtime11CreateClass4callEPNS_15ExecutionEngineEiR'
          'KNS_5ValueEPS4_',
          CuteMixin._addressOf(a0), a1, CuteMixin._valueOf(a2),
          CuteMixin._addressOf(a3),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CreateClass'

    #  Qt's '~QV4::Runtime::CreateClass()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::CreateClass behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime11CreateClassD1Ev'

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

  class CreateMappedArgumentsObject(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CreateMappedArgumentsObject: a plain
    Python object standing in front of one C++
    QV4::Runtime::CreateMappedArgumentsObject.

    C++ hands a QV4::Runtime::CreateMappedArgumentsObject around as a copy,
    so every C++ QV4::Runtime::CreateMappedArgumentsObject behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CreateMappedArgumentsObject that has
    a ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CreateMappedArgumentsObject::
      ~CreateMappedArgumentsObject()': the destructor: Python removes its C++
      QV4::Runtime::CreateMappedArgumentsObject by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CreateMappedArgumentsObject is created at the
      first use, not by 'QV4::Runtime::CreateMappedArgumentsObject(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CreateMappedArgumentsObject back
      gives a copy the ritual made for Python, in a new cute
      QV4::Runtime::CreateMappedArgumentsObject.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'])
    @overload(NoneType)
    def call(a0: Optional[QV4.ExecutionEngine]) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CreateMappedArgumentsObject::call(ExecutionEngine *a0)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-createmappedargumentsobject.html

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  ReturnedValue
      #      QV4::Runtime::CreateMappedArgumentsObject::call(ExecutionEngine
      #      *a0)
      return Rituals.call(
          'ritual_ZN3QV47Runtime27CreateMappedArgumentsObject4callEPNS_15Ex'
          'ecutionEngineE',
          CuteMixin._addressOf(a0),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CreateMappedArgumentsObject'

    #  Qt's '~QV4::Runtime::CreateMappedArgumentsObject()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::Runtime::CreateMappedArgumentsObject behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV47Runtime27CreateMappedArgumentsObjectD1Ev')

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

  class CreateRestParameter(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CreateRestParameter: a plain Python
    object standing in front of one C++ QV4::Runtime::CreateRestParameter.

    C++ hands a QV4::Runtime::CreateRestParameter around as a copy, so every
    C++ QV4::Runtime::CreateRestParameter behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CreateRestParameter that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CreateRestParameter::~CreateRestParameter()': the
      destructor: Python removes its C++ QV4::Runtime::CreateRestParameter by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CreateRestParameter is created at the first use,
      not by 'QV4::Runtime::CreateRestParameter(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CreateRestParameter back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::CreateRestParameter.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CreateRestParameter::call(ExecutionEngine *a0, int a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-createrestparameter.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  ReturnedValue
      #      QV4::Runtime::CreateRestParameter::call(ExecutionEngine *a0, int
      #      a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime19CreateRestParameter4callEPNS_15ExecutionE'
          'ngineEi',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CreateRestParameter'

    #  Qt's '~QV4::Runtime::CreateRestParameter()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::CreateRestParameter
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime19CreateRestParameterD1Ev'

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

  class CreateUnmappedArgumentsObject(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::CreateUnmappedArgumentsObject: a
    plain Python object standing in front of one C++
    QV4::Runtime::CreateUnmappedArgumentsObject.

    C++ hands a QV4::Runtime::CreateUnmappedArgumentsObject around as a copy,
    so every C++ QV4::Runtime::CreateUnmappedArgumentsObject behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::CreateUnmappedArgumentsObject that
    has a ritual and that Python can call so far, 1 name in all: 'call'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::CreateUnmappedArgumentsObject::
      ~CreateUnmappedArgumentsObject()': the destructor: Python removes its
      C++ QV4::Runtime::CreateUnmappedArgumentsObject by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::CreateUnmappedArgumentsObject is created at the
      first use, not by 'QV4::Runtime::CreateUnmappedArgumentsObject(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::CreateUnmappedArgumentsObject back
      gives a copy the ritual made for Python, in a new cute
      QV4::Runtime::CreateUnmappedArgumentsObject.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'])
    @overload(NoneType)
    def call(a0: Optional[QV4.ExecutionEngine]) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::CreateUnmappedArgumentsObject::call(ExecutionEngine
      *a0)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-createunmappedargumentsobject.html

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  ReturnedValue QV4::Runtime::CreateUnmappedArgumentsObject::call(
      #      ExecutionEngine *a0)
      return Rituals.call(
          'ritual_ZN3QV47Runtime29CreateUnmappedArgumentsObject4callEPNS_15'
          'ExecutionEngineE',
          CuteMixin._addressOf(a0),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::CreateUnmappedArgumentsObject'

    #  Qt's '~QV4::Runtime::CreateUnmappedArgumentsObject()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::Runtime::CreateUnmappedArgumentsObject behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV47Runtime29CreateUnmappedArgumentsObjectD1Ev')

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

  class DeclareVar(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::DeclareVar: a plain Python object
    standing in front of one C++ QV4::Runtime::DeclareVar.

    C++ hands a QV4::Runtime::DeclareVar around as a copy, so every C++
    QV4::Runtime::DeclareVar behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::DeclareVar that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::DeclareVar::~DeclareVar()': the destructor: Python
      removes its C++ QV4::Runtime::DeclareVar by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::DeclareVar is created at the first use, not by
      'QV4::Runtime::DeclareVar(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::DeclareVar back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::DeclareVar.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int, int)
    @overload(NoneType, int, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int, a2: int) -> None:
      """
      Calls Qt's 'void QV4::Runtime::DeclareVar::call(ExecutionEngine *a0,
      Bool a1, int a2)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-declarevar.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.

      a2 : int
        Passed on as it is.
      """
      #  void QV4::Runtime::DeclareVar::call(ExecutionEngine *a0, Bool a1,
      #      int a2)
      Rituals.call(
          'ritual_ZN3QV47Runtime10DeclareVar4callEPNS_15ExecutionEngineEji',
          CuteMixin._addressOf(a0), a1, a2,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::DeclareVar'

    #  Qt's '~QV4::Runtime::DeclareVar()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::DeclareVar behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime10DeclareVarD1Ev'

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

  class DeleteName(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::DeleteName: a plain Python object
    standing in front of one C++ QV4::Runtime::DeleteName.

    C++ hands a QV4::Runtime::DeleteName around as a copy, so every C++
    QV4::Runtime::DeleteName behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::DeleteName that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::DeleteName::~DeleteName()': the destructor: Python
      removes its C++ QV4::Runtime::DeleteName by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::DeleteName is created at the first use, not by
      'QV4::Runtime::DeleteName(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::DeleteName back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::DeleteName.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Function'], int)
    @overload(WAIT['QV4.ExecutionEngine'], NoneType, int)
    @overload(NoneType, WAIT['QV4.Function'], int)
    @overload(NoneType, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: Optional[QV4.Function],
        a2: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::DeleteName::call(ExecutionEngine *a0, Function *a1, int
      a2)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-deletename.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : Optional[QV4.Function]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a2 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::DeleteName::call(ExecutionEngine *a0,
      #      Function *a1, int a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime10DeleteName4callEPNS_15ExecutionEngineEPNS'
          '_8FunctionEi',
          CuteMixin._addressOf(a0), CuteMixin._addressOf(a1), a2,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::DeleteName'

    #  Qt's '~QV4::Runtime::DeleteName()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::DeleteName behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime10DeleteNameD1Ev'

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

  class DeleteName_NoThrow(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::DeleteName_NoThrow: a plain Python
    object standing in front of one C++ QV4::Runtime::DeleteName_NoThrow.

    C++ hands a QV4::Runtime::DeleteName_NoThrow around as a copy, so every
    C++ QV4::Runtime::DeleteName_NoThrow behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::DeleteName_NoThrow that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::DeleteName_NoThrow::~DeleteName_NoThrow()': the
      destructor: Python removes its C++ QV4::Runtime::DeleteName_NoThrow by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::DeleteName_NoThrow is created at the first use,
      not by 'QV4::Runtime::DeleteName_NoThrow(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::DeleteName_NoThrow back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::DeleteName_NoThrow.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::DeleteName_NoThrow::call(ExecutionEngine
      *a0, int a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-deletename_nothrow.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  Bool QV4::Runtime::DeleteName_NoThrow::call(ExecutionEngine *a0, int
      #      a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime18DeleteName_NoThrow4callEPNS_15ExecutionEn'
          'gineEi',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::DeleteName_NoThrow'

    #  Qt's '~QV4::Runtime::DeleteName_NoThrow()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::DeleteName_NoThrow
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime18DeleteName_NoThrowD1Ev'

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

  class DeleteProperty(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::DeleteProperty: a plain Python object
    standing in front of one C++ QV4::Runtime::DeleteProperty.

    C++ hands a QV4::Runtime::DeleteProperty around as a copy, so every C++
    QV4::Runtime::DeleteProperty behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::DeleteProperty that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::DeleteProperty::~DeleteProperty()': the destructor:
      Python removes its C++ QV4::Runtime::DeleteProperty by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::DeleteProperty is created at the first use, not
      by 'QV4::Runtime::DeleteProperty(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::DeleteProperty back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::DeleteProperty.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Function'], WAIT['QV4.Value'],
        WAIT['QV4.Value'],
    )
    @overload(
        WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'],
        WAIT['QV4.Value'],
    )
    @overload(
        NoneType, WAIT['QV4.Function'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: Optional[QV4.Function],
        a2: QV4.Value,
        a3: QV4.Value,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::DeleteProperty::call(ExecutionEngine *a0, Function *a1,
      const Value &a2, const Value &a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-deleteproperty.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : Optional[QV4.Function]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a3 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::DeleteProperty::call(ExecutionEngine
      #      *a0, Function *a1, const Value &a2, const Value &a3)
      return Rituals.call(
          'ritual_ZN3QV47Runtime14DeleteProperty4callEPNS_15ExecutionEngine'
          'EPNS_8FunctionERKNS_5ValueES8_',
          CuteMixin._addressOf(a0), CuteMixin._addressOf(a1),
          CuteMixin._valueOf(a2), CuteMixin._valueOf(a3),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::DeleteProperty'

    #  Qt's '~QV4::Runtime::DeleteProperty()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::DeleteProperty behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime14DeletePropertyD1Ev'

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

  class DeleteProperty_NoThrow(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::DeleteProperty_NoThrow: a plain
    Python object standing in front of one C++
    QV4::Runtime::DeleteProperty_NoThrow.

    C++ hands a QV4::Runtime::DeleteProperty_NoThrow around as a copy, so
    every C++ QV4::Runtime::DeleteProperty_NoThrow behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::DeleteProperty_NoThrow that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::DeleteProperty_NoThrow::~DeleteProperty_NoThrow()':
      the destructor: Python removes its C++
      QV4::Runtime::DeleteProperty_NoThrow by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::DeleteProperty_NoThrow is created at the first
      use, not by 'QV4::Runtime::DeleteProperty_NoThrow(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::DeleteProperty_NoThrow back gives a
      copy the ritual made for Python, in a new cute
      QV4::Runtime::DeleteProperty_NoThrow.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
    ) -> int:
      """
      Calls Qt's 'Bool
      QV4::Runtime::DeleteProperty_NoThrow::call(ExecutionEngine *a0, const
      Value &a1, const Value &a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-deleteproperty_nothrow.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::DeleteProperty_NoThrow::call(ExecutionEngine *a0,
      #      const Value &a1, const Value &a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime22DeleteProperty_NoThrow4callEPNS_15Executi'
          'onEngineERKNS_5ValueES6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::DeleteProperty_NoThrow'

    #  Qt's '~QV4::Runtime::DeleteProperty_NoThrow()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QV4::Runtime::DeleteProperty_NoThrow behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime22DeleteProperty_NoThrowD1Ev'

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

  class DestructureRestElement(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::DestructureRestElement: a plain
    Python object standing in front of one C++
    QV4::Runtime::DestructureRestElement.

    C++ hands a QV4::Runtime::DestructureRestElement around as a copy, so
    every C++ QV4::Runtime::DestructureRestElement behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::DestructureRestElement that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::DestructureRestElement::~DestructureRestElement()':
      the destructor: Python removes its C++
      QV4::Runtime::DestructureRestElement by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::DestructureRestElement is created at the first
      use, not by 'QV4::Runtime::DestructureRestElement(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::DestructureRestElement back gives a
      copy the ritual made for Python, in a new cute
      QV4::Runtime::DestructureRestElement.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::DestructureRestElement::call(ExecutionEngine *a0, const
      Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-destructurerestelement.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue
      #      QV4::Runtime::DestructureRestElement::call(ExecutionEngine *a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime22DestructureRestElement4callEPNS_15Executi'
          'onEngineERKNS_5ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::DestructureRestElement'

    #  Qt's '~QV4::Runtime::DestructureRestElement()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QV4::Runtime::DestructureRestElement behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime22DestructureRestElementD1Ev'

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

  class Div(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Div: a plain Python object standing
    in front of one C++ QV4::Runtime::Div.

    C++ hands a QV4::Runtime::Div around as a copy, so every C++
    QV4::Runtime::Div behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Div that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Div::~Div()': the destructor: Python removes its
      C++ QV4::Runtime::Div by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Div is created at the first use, not by
      'QV4::Runtime::Div(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Div back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::Div.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Div::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-div.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Div::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime3Div4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Div'

    #  Qt's '~QV4::Runtime::Div()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Div behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime3DivD1Ev'

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

  class Equal(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Equal: a plain Python object standing
    in front of one C++ QV4::Runtime::Equal.

    C++ hands a QV4::Runtime::Equal around as a copy, so every C++
    QV4::Runtime::Equal behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Equal that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Equal::~Equal()': the destructor: Python removes
      its C++ QV4::Runtime::Equal by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Equal is created at the first use, not by
      'QV4::Runtime::Equal(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Equal back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::Equal.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Equal::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-equal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Equal::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime5Equal4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Equal'

    #  Qt's '~QV4::Runtime::Equal()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Equal behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime5EqualD1Ev'

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

  class Exp(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Exp: a plain Python object standing
    in front of one C++ QV4::Runtime::Exp.

    C++ hands a QV4::Runtime::Exp around as a copy, so every C++
    QV4::Runtime::Exp behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Exp that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Exp::~Exp()': the destructor: Python removes its
      C++ QV4::Runtime::Exp by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Exp is created at the first use, not by
      'QV4::Runtime::Exp(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Exp back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::Exp.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Exp::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-exp.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Exp::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime3Exp4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Exp'

    #  Qt's '~QV4::Runtime::Exp()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Exp behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime3ExpD1Ev'

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

  class GetIterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::GetIterator: a plain Python object
    standing in front of one C++ QV4::Runtime::GetIterator.

    C++ hands a QV4::Runtime::GetIterator around as a copy, so every C++
    QV4::Runtime::GetIterator behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::GetIterator that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::GetIterator::~GetIterator()': the destructor:
      Python removes its C++ QV4::Runtime::GetIterator by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::GetIterator is created at the first use, not by
      'QV4::Runtime::GetIterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::GetIterator back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::GetIterator.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], int)
    @overload(NoneType, WAIT['QV4.Value'], int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::GetIterator::call(ExecutionEngine *a0, const Value &a1,
      int a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-getiterator.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::GetIterator::call(ExecutionEngine *a0,
      #      const Value &a1, int a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime11GetIterator4callEPNS_15ExecutionEngineERK'
          'NS_5ValueEi',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::GetIterator'

    #  Qt's '~QV4::Runtime::GetIterator()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::GetIterator behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime11GetIteratorD1Ev'

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

  class GetLookup(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::GetLookup: a plain Python object
    standing in front of one C++ QV4::Runtime::GetLookup.

    C++ hands a QV4::Runtime::GetLookup around as a copy, so every C++
    QV4::Runtime::GetLookup behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::GetLookup that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::GetLookup::~GetLookup()': the destructor: Python
      removes its C++ QV4::Runtime::GetLookup by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::GetLookup is created at the first use, not by
      'QV4::Runtime::GetLookup(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::GetLookup back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::GetLookup.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Function'], WAIT['QV4.Value'],
        int,
    )
    @overload(WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'], int)
    @overload(NoneType, WAIT['QV4.Function'], WAIT['QV4.Value'], int)
    @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: Optional[QV4.Function],
        a2: QV4.Value,
        a3: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::GetLookup::call(ExecutionEngine
      *a0, Function *a1, const Value &a2, int a3)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-getlookup.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : Optional[QV4.Function]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a3 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::GetLookup::call(ExecutionEngine *a0,
      #      Function *a1, const Value &a2, int a3)
      return Rituals.call(
          'ritual_ZN3QV47Runtime9GetLookup4callEPNS_15ExecutionEngineEPNS_8'
          'FunctionERKNS_5ValueEi',
          CuteMixin._addressOf(a0), CuteMixin._addressOf(a1),
          CuteMixin._valueOf(a2), a3,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::GetLookup'

    #  Qt's '~QV4::Runtime::GetLookup()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::GetLookup behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime9GetLookupD1Ev'

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

  class GetTemplateObject(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::GetTemplateObject: a plain Python
    object standing in front of one C++ QV4::Runtime::GetTemplateObject.

    C++ hands a QV4::Runtime::GetTemplateObject around as a copy, so every
    C++ QV4::Runtime::GetTemplateObject behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::GetTemplateObject that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::GetTemplateObject::~GetTemplateObject()': the
      destructor: Python removes its C++ QV4::Runtime::GetTemplateObject by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::GetTemplateObject is created at the first use,
      not by 'QV4::Runtime::GetTemplateObject(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::GetTemplateObject back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::GetTemplateObject.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Function'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.Function], a1: int) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::GetTemplateObject::call(Function *a0, int a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-gettemplateobject.html#call

      Parameters
      ----------

      a0 : Optional[QV4.Function]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::GetTemplateObject::call(Function *a0,
      #      int a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime17GetTemplateObject4callEPNS_8FunctionEi',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::GetTemplateObject'

    #  Qt's '~QV4::Runtime::GetTemplateObject()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::GetTemplateObject
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime17GetTemplateObjectD1Ev'

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

  class GreaterEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::GreaterEqual: a plain Python object
    standing in front of one C++ QV4::Runtime::GreaterEqual.

    C++ hands a QV4::Runtime::GreaterEqual around as a copy, so every C++
    QV4::Runtime::GreaterEqual behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::GreaterEqual that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::GreaterEqual::~GreaterEqual()': the destructor:
      Python removes its C++ QV4::Runtime::GreaterEqual by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::GreaterEqual is created at the first use, not by
      'QV4::Runtime::GreaterEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::GreaterEqual back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::GreaterEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::GreaterEqual::call(const Value
      &a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-greaterequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::GreaterEqual::call(const Value &a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime12GreaterEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::GreaterEqual'

    #  Qt's '~QV4::Runtime::GreaterEqual()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::GreaterEqual behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime12GreaterEqualD1Ev'

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

  class GreaterThan(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::GreaterThan: a plain Python object
    standing in front of one C++ QV4::Runtime::GreaterThan.

    C++ hands a QV4::Runtime::GreaterThan around as a copy, so every C++
    QV4::Runtime::GreaterThan behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::GreaterThan that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::GreaterThan::~GreaterThan()': the destructor:
      Python removes its C++ QV4::Runtime::GreaterThan by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::GreaterThan is created at the first use, not by
      'QV4::Runtime::GreaterThan(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::GreaterThan back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::GreaterThan.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::GreaterThan::call(const Value
      &a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-greaterthan.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::GreaterThan::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime11GreaterThan4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::GreaterThan'

    #  Qt's '~QV4::Runtime::GreaterThan()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::GreaterThan behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime11GreaterThanD1Ev'

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

  class In(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::In: a plain Python object standing in
    front of one C++ QV4::Runtime::In.

    C++ hands a QV4::Runtime::In around as a copy, so every C++
    QV4::Runtime::In behind a cute one is Python's own: it is removed, by the
    ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::In that has a ritual and that Python
    can call so far, 1 name in all: 'call'. None can be made from Python: one
    comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::In::~In()': the destructor: Python removes its C++
      QV4::Runtime::In by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::In is created at the first use, not by
      'QV4::Runtime::In(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::In back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::In.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::In::call(ExecutionEngine *a0,
      const Value &a1, const Value &a2)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-in.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::In::call(ExecutionEngine *a0, const
      #      Value &a1, const Value &a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime2In4callEPNS_15ExecutionEngineERKNS_5ValueE'
          'S6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::In'

    #  Qt's '~QV4::Runtime::In()'. Naming it makes this a value class: Python
    #  owns every C++ QV4::Runtime::In behind a cute one, and removes it by
    #  this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime2InD1Ev'

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

  class Instanceof(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Instanceof: a plain Python object
    standing in front of one C++ QV4::Runtime::Instanceof.

    C++ hands a QV4::Runtime::Instanceof around as a copy, so every C++
    QV4::Runtime::Instanceof behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Instanceof that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Instanceof::~Instanceof()': the destructor: Python
      removes its C++ QV4::Runtime::Instanceof by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Instanceof is created at the first use, not by
      'QV4::Runtime::Instanceof(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Instanceof back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::Instanceof.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::Instanceof::call(ExecutionEngine *a0, const Value &a1,
      const Value &a2)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-instanceof.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Instanceof::call(ExecutionEngine *a0,
      #      const Value &a1, const Value &a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime10Instanceof4callEPNS_15ExecutionEngineERKN'
          'S_5ValueES6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Instanceof'

    #  Qt's '~QV4::Runtime::Instanceof()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::Instanceof behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime10InstanceofD1Ev'

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

  class IteratorClose(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::IteratorClose: a plain Python object
    standing in front of one C++ QV4::Runtime::IteratorClose.

    C++ hands a QV4::Runtime::IteratorClose around as a copy, so every C++
    QV4::Runtime::IteratorClose behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::IteratorClose that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::IteratorClose::~IteratorClose()': the destructor:
      Python removes its C++ QV4::Runtime::IteratorClose by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::IteratorClose is created at the first use, not by
      'QV4::Runtime::IteratorClose(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::IteratorClose back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::IteratorClose.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::IteratorClose::call(ExecutionEngine *a0, const Value
      &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-iteratorclose.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::IteratorClose::call(ExecutionEngine *a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime13IteratorClose4callEPNS_15ExecutionEngineE'
          'RKNS_5ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::IteratorClose'

    #  Qt's '~QV4::Runtime::IteratorClose()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::IteratorClose behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime13IteratorCloseD1Ev'

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

  class IteratorNext(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::IteratorNext: a plain Python object
    standing in front of one C++ QV4::Runtime::IteratorNext.

    C++ hands a QV4::Runtime::IteratorNext around as a copy, so every C++
    QV4::Runtime::IteratorNext behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::IteratorNext that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::IteratorNext::~IteratorNext()': the destructor:
      Python removes its C++ QV4::Runtime::IteratorNext by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::IteratorNext is created at the first use, not by
      'QV4::Runtime::IteratorNext(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::IteratorNext back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::IteratorNext.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], NoneType)
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'], NoneType)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: Optional[QV4.Value],
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::IteratorNext::call(ExecutionEngine *a0, const Value &a1,
      Value *a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-iteratornext.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  ReturnedValue QV4::Runtime::IteratorNext::call(ExecutionEngine *a0,
      #      const Value &a1, Value *a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime12IteratorNext4callEPNS_15ExecutionEngineER'
          'KNS_5ValueEPS4_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._addressOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::IteratorNext'

    #  Qt's '~QV4::Runtime::IteratorNext()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::IteratorNext behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime12IteratorNextD1Ev'

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

  class IteratorNextForYieldStar(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::IteratorNextForYieldStar: a plain
    Python object standing in front of one C++
    QV4::Runtime::IteratorNextForYieldStar.

    C++ hands a QV4::Runtime::IteratorNextForYieldStar around as a copy, so
    every C++ QV4::Runtime::IteratorNextForYieldStar behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::IteratorNextForYieldStar that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QV4::Runtime::IteratorNextForYieldStar::~IteratorNextForYieldStar()':
      the destructor: Python removes its C++
      QV4::Runtime::IteratorNextForYieldStar by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::IteratorNextForYieldStar is created at the first
      use, not by 'QV4::Runtime::IteratorNextForYieldStar(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::IteratorNextForYieldStar back gives a
      copy the ritual made for Python, in a new cute
      QV4::Runtime::IteratorNextForYieldStar.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        WAIT['QV4.Value'],
    )
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        NoneType,
    )
    @overload(
        NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
        a3: Optional[QV4.Value],
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::IteratorNextForYieldStar::call(ExecutionEngine *a0, const
      Value &a1, const Value &a2, Value *a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-iteratornextforyieldstar.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a3 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  ReturnedValue
      #      QV4::Runtime::IteratorNextForYieldStar::call(ExecutionEngine
      #      *a0, const Value &a1, const Value &a2, Value *a3)
      return Rituals.call(
          'ritual_ZN3QV47Runtime24IteratorNextForYieldStar4callEPNS_15Execu'
          'tionEngineERKNS_5ValueES6_PS4_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2), CuteMixin._addressOf(a3),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::IteratorNextForYieldStar'

    #  Qt's '~QV4::Runtime::IteratorNextForYieldStar()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QV4::Runtime::IteratorNextForYieldStar behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime24IteratorNextForYieldStarD1Ev'

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

  class LessEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::LessEqual: a plain Python object
    standing in front of one C++ QV4::Runtime::LessEqual.

    C++ hands a QV4::Runtime::LessEqual around as a copy, so every C++
    QV4::Runtime::LessEqual behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::LessEqual that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::LessEqual::~LessEqual()': the destructor: Python
      removes its C++ QV4::Runtime::LessEqual by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::LessEqual is created at the first use, not by
      'QV4::Runtime::LessEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::LessEqual back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::LessEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::LessEqual::call(const Value
      &a0, const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-lessequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::LessEqual::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime9LessEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::LessEqual'

    #  Qt's '~QV4::Runtime::LessEqual()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::LessEqual behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime9LessEqualD1Ev'

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

  class LessThan(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::LessThan: a plain Python object
    standing in front of one C++ QV4::Runtime::LessThan.

    C++ hands a QV4::Runtime::LessThan around as a copy, so every C++
    QV4::Runtime::LessThan behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::LessThan that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::LessThan::~LessThan()': the destructor: Python
      removes its C++ QV4::Runtime::LessThan by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::LessThan is created at the first use, not by
      'QV4::Runtime::LessThan(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::LessThan back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::LessThan.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::LessThan::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-lessthan.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::LessThan::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime8LessThan4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::LessThan'

    #  Qt's '~QV4::Runtime::LessThan()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::LessThan behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime8LessThanD1Ev'

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

  class LoadElement(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::LoadElement: a plain Python object
    standing in front of one C++ QV4::Runtime::LoadElement.

    C++ hands a QV4::Runtime::LoadElement around as a copy, so every C++
    QV4::Runtime::LoadElement behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::LoadElement that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::LoadElement::~LoadElement()': the destructor:
      Python removes its C++ QV4::Runtime::LoadElement by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::LoadElement is created at the first use, not by
      'QV4::Runtime::LoadElement(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::LoadElement back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::LoadElement.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::LoadElement::call(ExecutionEngine *a0, const Value &a1,
      const Value &a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-loadelement.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::LoadElement::call(ExecutionEngine *a0,
      #      const Value &a1, const Value &a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime11LoadElement4callEPNS_15ExecutionEngineERK'
          'NS_5ValueES6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::LoadElement'

    #  Qt's '~QV4::Runtime::LoadElement()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::LoadElement behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime11LoadElementD1Ev'

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

  class LoadGlobalLookup(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::LoadGlobalLookup: a plain Python
    object standing in front of one C++ QV4::Runtime::LoadGlobalLookup.

    C++ hands a QV4::Runtime::LoadGlobalLookup around as a copy, so every C++
    QV4::Runtime::LoadGlobalLookup behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::LoadGlobalLookup that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::LoadGlobalLookup::~LoadGlobalLookup()': the
      destructor: Python removes its C++ QV4::Runtime::LoadGlobalLookup by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::LoadGlobalLookup is created at the first use, not
      by 'QV4::Runtime::LoadGlobalLookup(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::LoadGlobalLookup back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::LoadGlobalLookup.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Function'], int)
    @overload(WAIT['QV4.ExecutionEngine'], NoneType, int)
    @overload(NoneType, WAIT['QV4.Function'], int)
    @overload(NoneType, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: Optional[QV4.Function],
        a2: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::LoadGlobalLookup::call(ExecutionEngine *a0, Function *a1,
      int a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-loadgloballookup.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : Optional[QV4.Function]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a2 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::LoadGlobalLookup::call(ExecutionEngine
      #      *a0, Function *a1, int a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime16LoadGlobalLookup4callEPNS_15ExecutionEngi'
          'neEPNS_8FunctionEi',
          CuteMixin._addressOf(a0), CuteMixin._addressOf(a1), a2,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::LoadGlobalLookup'

    #  Qt's '~QV4::Runtime::LoadGlobalLookup()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::LoadGlobalLookup behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime16LoadGlobalLookupD1Ev'

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

  class LoadName(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::LoadName: a plain Python object
    standing in front of one C++ QV4::Runtime::LoadName.

    C++ hands a QV4::Runtime::LoadName around as a copy, so every C++
    QV4::Runtime::LoadName behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::LoadName that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::LoadName::~LoadName()': the destructor: Python
      removes its C++ QV4::Runtime::LoadName by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::LoadName is created at the first use, not by
      'QV4::Runtime::LoadName(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::LoadName back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::LoadName.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::LoadName::call(ExecutionEngine
      *a0, int a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-loadname.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::LoadName::call(ExecutionEngine *a0, int
      #      a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime8LoadName4callEPNS_15ExecutionEngineEi',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::LoadName'

    #  Qt's '~QV4::Runtime::LoadName()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::LoadName behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime8LoadNameD1Ev'

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

  class LoadProperty(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::LoadProperty: a plain Python object
    standing in front of one C++ QV4::Runtime::LoadProperty.

    C++ hands a QV4::Runtime::LoadProperty around as a copy, so every C++
    QV4::Runtime::LoadProperty behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::LoadProperty that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::LoadProperty::~LoadProperty()': the destructor:
      Python removes its C++ QV4::Runtime::LoadProperty by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::LoadProperty is created at the first use, not by
      'QV4::Runtime::LoadProperty(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::LoadProperty back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::LoadProperty.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], int)
    @overload(NoneType, WAIT['QV4.Value'], int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::LoadProperty::call(ExecutionEngine *a0, const Value &a1,
      int a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-loadproperty.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::LoadProperty::call(ExecutionEngine *a0,
      #      const Value &a1, int a2)
      return Rituals.call(
          'ritual_ZN3QV47Runtime12LoadProperty4callEPNS_15ExecutionEngineER'
          'KNS_5ValueEi',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::LoadProperty'

    #  Qt's '~QV4::Runtime::LoadProperty()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::LoadProperty behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime12LoadPropertyD1Ev'

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

  class LoadQmlContextPropertyLookup(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::LoadQmlContextPropertyLookup: a plain
    Python object standing in front of one C++
    QV4::Runtime::LoadQmlContextPropertyLookup.

    C++ hands a QV4::Runtime::LoadQmlContextPropertyLookup around as a copy,
    so every C++ QV4::Runtime::LoadQmlContextPropertyLookup behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::LoadQmlContextPropertyLookup that
    has a ritual and that Python can call so far, 1 name in all: 'call'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::LoadQmlContextPropertyLookup::
      ~LoadQmlContextPropertyLookup()': the destructor: Python removes its
      C++ QV4::Runtime::LoadQmlContextPropertyLookup by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::LoadQmlContextPropertyLookup is created at the
      first use, not by 'QV4::Runtime::LoadQmlContextPropertyLookup(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::LoadQmlContextPropertyLookup back
      gives a copy the ritual made for Python, in a new cute
      QV4::Runtime::LoadQmlContextPropertyLookup.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::LoadQmlContextPropertyLookup::call(ExecutionEngine *a0,
      uint a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-loadqmlcontextpropertylookup.html

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  ReturnedValue
      #      QV4::Runtime::LoadQmlContextPropertyLookup::call(ExecutionEngine
      #      *a0, uint a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime28LoadQmlContextPropertyLookup4callEPNS_15E'
          'xecutionEngineEj',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::LoadQmlContextPropertyLookup'

    #  Qt's '~QV4::Runtime::LoadQmlContextPropertyLookup()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::Runtime::LoadQmlContextPropertyLookup behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV47Runtime28LoadQmlContextPropertyLookupD1Ev')

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

  class LoadSuperConstructor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::LoadSuperConstructor: a plain Python
    object standing in front of one C++ QV4::Runtime::LoadSuperConstructor.

    C++ hands a QV4::Runtime::LoadSuperConstructor around as a copy, so every
    C++ QV4::Runtime::LoadSuperConstructor behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::LoadSuperConstructor that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::LoadSuperConstructor::~LoadSuperConstructor()': the
      destructor: Python removes its C++ QV4::Runtime::LoadSuperConstructor
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::LoadSuperConstructor is created at the first use,
      not by 'QV4::Runtime::LoadSuperConstructor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::LoadSuperConstructor back gives a
      copy the ritual made for Python, in a new cute
      QV4::Runtime::LoadSuperConstructor.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::LoadSuperConstructor::call(ExecutionEngine *a0, const
      Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-loadsuperconstructor.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue
      #      QV4::Runtime::LoadSuperConstructor::call(ExecutionEngine *a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime20LoadSuperConstructor4callEPNS_15Execution'
          'EngineERKNS_5ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::LoadSuperConstructor'

    #  Qt's '~QV4::Runtime::LoadSuperConstructor()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::LoadSuperConstructor
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime20LoadSuperConstructorD1Ev'

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

  class LoadSuperProperty(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::LoadSuperProperty: a plain Python
    object standing in front of one C++ QV4::Runtime::LoadSuperProperty.

    C++ hands a QV4::Runtime::LoadSuperProperty around as a copy, so every
    C++ QV4::Runtime::LoadSuperProperty behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::LoadSuperProperty that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::LoadSuperProperty::~LoadSuperProperty()': the
      destructor: Python removes its C++ QV4::Runtime::LoadSuperProperty by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::LoadSuperProperty is created at the first use,
      not by 'QV4::Runtime::LoadSuperProperty(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::LoadSuperProperty back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::LoadSuperProperty.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::LoadSuperProperty::call(ExecutionEngine *a0, const Value
      &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-loadsuperproperty.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::LoadSuperProperty::call(ExecutionEngine
      #      *a0, const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime17LoadSuperProperty4callEPNS_15ExecutionEng'
          'ineERKNS_5ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::LoadSuperProperty'

    #  Qt's '~QV4::Runtime::LoadSuperProperty()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::LoadSuperProperty
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime17LoadSuperPropertyD1Ev'

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

  class MarkCustom(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::MarkCustom: a plain Python object
    standing in front of one C++ QV4::Runtime::MarkCustom.

    C++ hands a QV4::Runtime::MarkCustom around as a copy, so every C++
    QV4::Runtime::MarkCustom behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::MarkCustom that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::MarkCustom::~MarkCustom()': the destructor: Python
      removes its C++ QV4::Runtime::MarkCustom by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::MarkCustom is created at the first use, not by
      'QV4::Runtime::MarkCustom(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::MarkCustom back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::MarkCustom.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'])
    def call(toBeMarked: QV4.Value) -> None:
      """
      Calls Qt's 'void QV4::Runtime::MarkCustom::call(const Value
      &toBeMarked)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-markcustom.html#call

      Parameters
      ----------

      toBeMarked : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::MarkCustom::call(const Value &toBeMarked)
      Rituals.call(
          'ritual_ZN3QV47Runtime10MarkCustom4callERKNS_5ValueE',
          CuteMixin._valueOf(toBeMarked),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::MarkCustom'

    #  Qt's '~QV4::Runtime::MarkCustom()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::MarkCustom behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime10MarkCustomD1Ev'

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

  class Mod(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Mod: a plain Python object standing
    in front of one C++ QV4::Runtime::Mod.

    C++ hands a QV4::Runtime::Mod around as a copy, so every C++
    QV4::Runtime::Mod behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Mod that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Mod::~Mod()': the destructor: Python removes its
      C++ QV4::Runtime::Mod by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Mod is created at the first use, not by
      'QV4::Runtime::Mod(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Mod back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::Mod.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Mod::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-mod.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Mod::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime3Mod4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Mod'

    #  Qt's '~QV4::Runtime::Mod()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Mod behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime3ModD1Ev'

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

  class Mul(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Mul: a plain Python object standing
    in front of one C++ QV4::Runtime::Mul.

    C++ hands a QV4::Runtime::Mul around as a copy, so every C++
    QV4::Runtime::Mul behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Mul that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Mul::~Mul()': the destructor: Python removes its
      C++ QV4::Runtime::Mul by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Mul is created at the first use, not by
      'QV4::Runtime::Mul(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Mul back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::Mul.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Mul::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-mul.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Mul::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime3Mul4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Mul'

    #  Qt's '~QV4::Runtime::Mul()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Mul behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime3MulD1Ev'

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

  class NotEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::NotEqual: a plain Python object
    standing in front of one C++ QV4::Runtime::NotEqual.

    C++ hands a QV4::Runtime::NotEqual around as a copy, so every C++
    QV4::Runtime::NotEqual behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::NotEqual that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::NotEqual::~NotEqual()': the destructor: Python
      removes its C++ QV4::Runtime::NotEqual by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::NotEqual is created at the first use, not by
      'QV4::Runtime::NotEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::NotEqual back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::NotEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::NotEqual::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-notequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::NotEqual::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime8NotEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::NotEqual'

    #  Qt's '~QV4::Runtime::NotEqual()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::NotEqual behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime8NotEqualD1Ev'

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

  class ObjectLiteral(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ObjectLiteral: a plain Python object
    standing in front of one C++ QV4::Runtime::ObjectLiteral.

    C++ hands a QV4::Runtime::ObjectLiteral around as a copy, so every C++
    QV4::Runtime::ObjectLiteral behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ObjectLiteral that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ObjectLiteral::~ObjectLiteral()': the destructor:
      Python removes its C++ QV4::Runtime::ObjectLiteral by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ObjectLiteral is created at the first use, not by
      'QV4::Runtime::ObjectLiteral(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ObjectLiteral back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::ObjectLiteral.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'], int)
    @overload(WAIT['QV4.ExecutionEngine'], int, NoneType, int)
    @overload(NoneType, int, WAIT['QV4.Value'], int)
    @overload(NoneType, int, NoneType, int)
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: int,
        a2: Optional[QV4.Value],
        a3: int,
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::ObjectLiteral::call(ExecutionEngine *a0, int a1, Value
      *a2, int a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-objectliteral.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.

      a2 : Optional[QV4.Value]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a3 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::ObjectLiteral::call(ExecutionEngine *a0,
      #      int a1, Value *a2, int a3)
      return Rituals.call(
          'ritual_ZN3QV47Runtime13ObjectLiteral4callEPNS_15ExecutionEngineE'
          'iPNS_5ValueEi',
          CuteMixin._addressOf(a0), a1, CuteMixin._addressOf(a2), a3,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ObjectLiteral'

    #  Qt's '~QV4::Runtime::ObjectLiteral()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::ObjectLiteral behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime13ObjectLiteralD1Ev'

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

  class PopScriptContext(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::PopScriptContext: a plain Python
    object standing in front of one C++ QV4::Runtime::PopScriptContext.

    C++ hands a QV4::Runtime::PopScriptContext around as a copy, so every C++
    QV4::Runtime::PopScriptContext behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::PopScriptContext that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::PopScriptContext::~PopScriptContext()': the
      destructor: Python removes its C++ QV4::Runtime::PopScriptContext by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::PopScriptContext is created at the first use, not
      by 'QV4::Runtime::PopScriptContext(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::PopScriptContext back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::PopScriptContext.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'])
    @overload(NoneType)
    def call(a0: Optional[QV4.ExecutionEngine]) -> None:
      """
      Calls Qt's 'void QV4::Runtime::PopScriptContext::call(ExecutionEngine
      *a0)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-popscriptcontext.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QV4::Runtime::PopScriptContext::call(ExecutionEngine *a0)
      Rituals.call(
          'ritual_ZN3QV47Runtime16PopScriptContext4callEPNS_15ExecutionEngi'
          'neE',
          CuteMixin._addressOf(a0),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::PopScriptContext'

    #  Qt's '~QV4::Runtime::PopScriptContext()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::PopScriptContext behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime16PopScriptContextD1Ev'

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

  class PushBlockContext(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::PushBlockContext: a plain Python
    object standing in front of one C++ QV4::Runtime::PushBlockContext.

    C++ hands a QV4::Runtime::PushBlockContext around as a copy, so every C++
    QV4::Runtime::PushBlockContext behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::PushBlockContext that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::PushBlockContext::~PushBlockContext()': the
      destructor: Python removes its C++ QV4::Runtime::PushBlockContext by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::PushBlockContext is created at the first use, not
      by 'QV4::Runtime::PushBlockContext(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::PushBlockContext back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::PushBlockContext.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> None:
      """
      Calls Qt's 'void QV4::Runtime::PushBlockContext::call(ExecutionEngine
      *a0, int a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-pushblockcontext.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  void QV4::Runtime::PushBlockContext::call(ExecutionEngine *a0, int
      #      a1)
      Rituals.call(
          'ritual_ZN3QV47Runtime16PushBlockContext4callEPNS_15ExecutionEngi'
          'neEi',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::PushBlockContext'

    #  Qt's '~QV4::Runtime::PushBlockContext()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::PushBlockContext behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime16PushBlockContextD1Ev'

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

  class PushCallContext(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::PushCallContext: a plain Python
    object standing in front of one C++ QV4::Runtime::PushCallContext.

    C++ hands a QV4::Runtime::PushCallContext around as a copy, so every C++
    QV4::Runtime::PushCallContext behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::PushCallContext that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::PushCallContext::~PushCallContext()': the
      destructor: Python removes its C++ QV4::Runtime::PushCallContext by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::PushCallContext is created at the first use, not
      by 'QV4::Runtime::PushCallContext(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::PushCallContext back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::PushCallContext.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.JSTypesStackFrame'])
    @overload(NoneType)
    def call(a0: Optional[QV4.JSTypesStackFrame]) -> None:
      """
      Calls Qt's 'void QV4::Runtime::PushCallContext::call(JSTypesStackFrame
      *a0)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-pushcallcontext.html#call

      Parameters
      ----------

      a0 : Optional[QV4.JSTypesStackFrame]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QV4::Runtime::PushCallContext::call(JSTypesStackFrame *a0)
      Rituals.call(
          'ritual_ZN3QV47Runtime15PushCallContext4callEPNS_17JSTypesStackFr'
          'ameE',
          CuteMixin._addressOf(a0),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::PushCallContext'

    #  Qt's '~QV4::Runtime::PushCallContext()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::PushCallContext behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime15PushCallContextD1Ev'

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

  class PushCatchContext(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::PushCatchContext: a plain Python
    object standing in front of one C++ QV4::Runtime::PushCatchContext.

    C++ hands a QV4::Runtime::PushCatchContext around as a copy, so every C++
    QV4::Runtime::PushCatchContext behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::PushCatchContext that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::PushCatchContext::~PushCatchContext()': the
      destructor: Python removes its C++ QV4::Runtime::PushCatchContext by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::PushCatchContext is created at the first use, not
      by 'QV4::Runtime::PushCatchContext(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::PushCatchContext back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::PushCatchContext.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int, int)
    @overload(NoneType, int, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int, a2: int) -> None:
      """
      Calls Qt's 'void QV4::Runtime::PushCatchContext::call(ExecutionEngine
      *a0, int a1, int a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-pushcatchcontext.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.

      a2 : int
        Passed on as it is.
      """
      #  void QV4::Runtime::PushCatchContext::call(ExecutionEngine *a0, int
      #      a1, int a2)
      Rituals.call(
          'ritual_ZN3QV47Runtime16PushCatchContext4callEPNS_15ExecutionEngi'
          'neEii',
          CuteMixin._addressOf(a0), a1, a2,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::PushCatchContext'

    #  Qt's '~QV4::Runtime::PushCatchContext()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::PushCatchContext behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime16PushCatchContextD1Ev'

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

  class PushScriptContext(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::PushScriptContext: a plain Python
    object standing in front of one C++ QV4::Runtime::PushScriptContext.

    C++ hands a QV4::Runtime::PushScriptContext around as a copy, so every
    C++ QV4::Runtime::PushScriptContext behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::PushScriptContext that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::PushScriptContext::~PushScriptContext()': the
      destructor: Python removes its C++ QV4::Runtime::PushScriptContext by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::PushScriptContext is created at the first use,
      not by 'QV4::Runtime::PushScriptContext(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::PushScriptContext back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::PushScriptContext.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> None:
      """
      Calls Qt's 'void QV4::Runtime::PushScriptContext::call(ExecutionEngine
      *a0, int a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-pushscriptcontext.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  void QV4::Runtime::PushScriptContext::call(ExecutionEngine *a0, int
      #      a1)
      Rituals.call(
          'ritual_ZN3QV47Runtime17PushScriptContext4callEPNS_15ExecutionEng'
          'ineEi',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::PushScriptContext'

    #  Qt's '~QV4::Runtime::PushScriptContext()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::PushScriptContext
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime17PushScriptContextD1Ev'

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

  class PushWithContext(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::PushWithContext: a plain Python
    object standing in front of one C++ QV4::Runtime::PushWithContext.

    C++ hands a QV4::Runtime::PushWithContext around as a copy, so every C++
    QV4::Runtime::PushWithContext behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::PushWithContext that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::PushWithContext::~PushWithContext()': the
      destructor: Python removes its C++ QV4::Runtime::PushWithContext by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::PushWithContext is created at the first use, not
      by 'QV4::Runtime::PushWithContext(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::PushWithContext back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::PushWithContext.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::PushWithContext::call(ExecutionEngine *a0, const Value
      &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-pushwithcontext.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::PushWithContext::call(ExecutionEngine
      #      *a0, const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime15PushWithContext4callEPNS_15ExecutionEngin'
          'eERKNS_5ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::PushWithContext'

    #  Qt's '~QV4::Runtime::PushWithContext()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::PushWithContext behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime15PushWithContextD1Ev'

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

  class RegexpLiteral(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::RegexpLiteral: a plain Python object
    standing in front of one C++ QV4::Runtime::RegexpLiteral.

    C++ hands a QV4::Runtime::RegexpLiteral around as a copy, so every C++
    QV4::Runtime::RegexpLiteral behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::RegexpLiteral that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::RegexpLiteral::~RegexpLiteral()': the destructor:
      Python removes its C++ QV4::Runtime::RegexpLiteral by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::RegexpLiteral is created at the first use, not by
      'QV4::Runtime::RegexpLiteral(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::RegexpLiteral back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::RegexpLiteral.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::RegexpLiteral::call(ExecutionEngine *a0, int a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-regexpliteral.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::RegexpLiteral::call(ExecutionEngine *a0,
      #      int a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime13RegexpLiteral4callEPNS_15ExecutionEngineE'
          'i',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::RegexpLiteral'

    #  Qt's '~QV4::Runtime::RegexpLiteral()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::RegexpLiteral behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime13RegexpLiteralD1Ev'

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

  class SetLookupSloppy(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::SetLookupSloppy: a plain Python
    object standing in front of one C++ QV4::Runtime::SetLookupSloppy.

    C++ hands a QV4::Runtime::SetLookupSloppy around as a copy, so every C++
    QV4::Runtime::SetLookupSloppy behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::SetLookupSloppy that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::SetLookupSloppy::~SetLookupSloppy()': the
      destructor: Python removes its C++ QV4::Runtime::SetLookupSloppy by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::SetLookupSloppy is created at the first use, not
      by 'QV4::Runtime::SetLookupSloppy(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::SetLookupSloppy back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::SetLookupSloppy.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.Function'], WAIT['QV4.Value'], int, WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], int, WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.Function],
        a1: QV4.Value,
        a2: int,
        a3: QV4.Value,
    ) -> None:
      """
      Calls Qt's 'void QV4::Runtime::SetLookupSloppy::call(Function *a0,
      const Value &a1, int a2, const Value &a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-setlookupsloppy.html#call

      Parameters
      ----------

      a0 : Optional[QV4.Function]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : int
        Passed on as it is.

      a3 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::SetLookupSloppy::call(Function *a0, const Value
      #      &a1, int a2, const Value &a3)
      Rituals.call(
          'ritual_ZN3QV47Runtime15SetLookupSloppy4callEPNS_8FunctionERKNS_5'
          'ValueEiS6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
          CuteMixin._valueOf(a3),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::SetLookupSloppy'

    #  Qt's '~QV4::Runtime::SetLookupSloppy()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::SetLookupSloppy behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime15SetLookupSloppyD1Ev'

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

  class SetLookupStrict(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::SetLookupStrict: a plain Python
    object standing in front of one C++ QV4::Runtime::SetLookupStrict.

    C++ hands a QV4::Runtime::SetLookupStrict around as a copy, so every C++
    QV4::Runtime::SetLookupStrict behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::SetLookupStrict that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::SetLookupStrict::~SetLookupStrict()': the
      destructor: Python removes its C++ QV4::Runtime::SetLookupStrict by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::SetLookupStrict is created at the first use, not
      by 'QV4::Runtime::SetLookupStrict(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::SetLookupStrict back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::SetLookupStrict.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.Function'], WAIT['QV4.Value'], int, WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], int, WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.Function],
        a1: QV4.Value,
        a2: int,
        a3: QV4.Value,
    ) -> None:
      """
      Calls Qt's 'void QV4::Runtime::SetLookupStrict::call(Function *a0,
      const Value &a1, int a2, const Value &a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-setlookupstrict.html#call

      Parameters
      ----------

      a0 : Optional[QV4.Function]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : int
        Passed on as it is.

      a3 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::SetLookupStrict::call(Function *a0, const Value
      #      &a1, int a2, const Value &a3)
      Rituals.call(
          'ritual_ZN3QV47Runtime15SetLookupStrict4callEPNS_8FunctionERKNS_5'
          'ValueEiS6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
          CuteMixin._valueOf(a3),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::SetLookupStrict'

    #  Qt's '~QV4::Runtime::SetLookupStrict()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::SetLookupStrict behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime15SetLookupStrictD1Ev'

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

  class Shl(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Shl: a plain Python object standing
    in front of one C++ QV4::Runtime::Shl.

    C++ hands a QV4::Runtime::Shl around as a copy, so every C++
    QV4::Runtime::Shl behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Shl that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Shl::~Shl()': the destructor: Python removes its
      C++ QV4::Runtime::Shl by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Shl is created at the first use, not by
      'QV4::Runtime::Shl(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Shl back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::Shl.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Shl::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-shl.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Shl::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime3Shl4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Shl'

    #  Qt's '~QV4::Runtime::Shl()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Shl behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime3ShlD1Ev'

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

  class Shr(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Shr: a plain Python object standing
    in front of one C++ QV4::Runtime::Shr.

    C++ hands a QV4::Runtime::Shr around as a copy, so every C++
    QV4::Runtime::Shr behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Shr that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Shr::~Shr()': the destructor: Python removes its
      C++ QV4::Runtime::Shr by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Shr is created at the first use, not by
      'QV4::Runtime::Shr(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Shr back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::Shr.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Shr::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-shr.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Shr::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime3Shr4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Shr'

    #  Qt's '~QV4::Runtime::Shr()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Shr behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime3ShrD1Ev'

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

  class StackOffsets(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::StackOffsets: a plain Python object
    standing in front of one C++ QV4::Runtime::StackOffsets.

    C++ hands a QV4::Runtime::StackOffsets around as a copy, so every C++
    QV4::Runtime::StackOffsets behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QV4::Runtime::StackOffsets yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::StackOffsets::~StackOffsets()': the destructor:
      Python removes its C++ QV4::Runtime::StackOffsets by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::StackOffsets is created at the first use, not by
      'QV4::Runtime::StackOffsets(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::StackOffsets back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::StackOffsets.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::StackOffsets'

    #  Qt's '~QV4::Runtime::StackOffsets()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::StackOffsets behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime12StackOffsetsD1Ev'

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

  class StoreElement(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::StoreElement: a plain Python object
    standing in front of one C++ QV4::Runtime::StoreElement.

    C++ hands a QV4::Runtime::StoreElement around as a copy, so every C++
    QV4::Runtime::StoreElement behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::StoreElement that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::StoreElement::~StoreElement()': the destructor:
      Python removes its C++ QV4::Runtime::StoreElement by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::StoreElement is created at the first use, not by
      'QV4::Runtime::StoreElement(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::StoreElement back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::StoreElement.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
        WAIT['QV4.Value'],
    )
    @overload(
        NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
        a3: QV4.Value,
    ) -> None:
      """
      Calls Qt's 'void QV4::Runtime::StoreElement::call(ExecutionEngine *a0,
      const Value &a1, const Value &a2, const Value &a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-storeelement.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a3 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::StoreElement::call(ExecutionEngine *a0, const
      #      Value &a1, const Value &a2, const Value &a3)
      Rituals.call(
          'ritual_ZN3QV47Runtime12StoreElement4callEPNS_15ExecutionEngineER'
          'KNS_5ValueES6_S6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2), CuteMixin._valueOf(a3),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::StoreElement'

    #  Qt's '~QV4::Runtime::StoreElement()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::StoreElement behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime12StoreElementD1Ev'

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

  class StoreNameSloppy(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::StoreNameSloppy: a plain Python
    object standing in front of one C++ QV4::Runtime::StoreNameSloppy.

    C++ hands a QV4::Runtime::StoreNameSloppy around as a copy, so every C++
    QV4::Runtime::StoreNameSloppy behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::StoreNameSloppy that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::StoreNameSloppy::~StoreNameSloppy()': the
      destructor: Python removes its C++ QV4::Runtime::StoreNameSloppy by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::StoreNameSloppy is created at the first use, not
      by 'QV4::Runtime::StoreNameSloppy(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::StoreNameSloppy back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::StoreNameSloppy.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'])
    @overload(NoneType, int, WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: int,
        a2: QV4.Value,
    ) -> None:
      """
      Calls Qt's 'void QV4::Runtime::StoreNameSloppy::call(ExecutionEngine
      *a0, int a1, const Value &a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-storenamesloppy.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::StoreNameSloppy::call(ExecutionEngine *a0, int
      #      a1, const Value &a2)
      Rituals.call(
          'ritual_ZN3QV47Runtime15StoreNameSloppy4callEPNS_15ExecutionEngin'
          'eEiRKNS_5ValueE',
          CuteMixin._addressOf(a0), a1, CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::StoreNameSloppy'

    #  Qt's '~QV4::Runtime::StoreNameSloppy()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::StoreNameSloppy behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime15StoreNameSloppyD1Ev'

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

  class StoreNameStrict(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::StoreNameStrict: a plain Python
    object standing in front of one C++ QV4::Runtime::StoreNameStrict.

    C++ hands a QV4::Runtime::StoreNameStrict around as a copy, so every C++
    QV4::Runtime::StoreNameStrict behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::StoreNameStrict that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::StoreNameStrict::~StoreNameStrict()': the
      destructor: Python removes its C++ QV4::Runtime::StoreNameStrict by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::StoreNameStrict is created at the first use, not
      by 'QV4::Runtime::StoreNameStrict(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::StoreNameStrict back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::StoreNameStrict.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'])
    @overload(NoneType, int, WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: int,
        a2: QV4.Value,
    ) -> None:
      """
      Calls Qt's 'void QV4::Runtime::StoreNameStrict::call(ExecutionEngine
      *a0, int a1, const Value &a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-storenamestrict.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::StoreNameStrict::call(ExecutionEngine *a0, int
      #      a1, const Value &a2)
      Rituals.call(
          'ritual_ZN3QV47Runtime15StoreNameStrict4callEPNS_15ExecutionEngin'
          'eEiRKNS_5ValueE',
          CuteMixin._addressOf(a0), a1, CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::StoreNameStrict'

    #  Qt's '~QV4::Runtime::StoreNameStrict()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::StoreNameStrict behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime15StoreNameStrictD1Ev'

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

  class StoreProperty(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::StoreProperty: a plain Python object
    standing in front of one C++ QV4::Runtime::StoreProperty.

    C++ hands a QV4::Runtime::StoreProperty around as a copy, so every C++
    QV4::Runtime::StoreProperty behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::StoreProperty that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::StoreProperty::~StoreProperty()': the destructor:
      Python removes its C++ QV4::Runtime::StoreProperty by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::StoreProperty is created at the first use, not by
      'QV4::Runtime::StoreProperty(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::StoreProperty back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::StoreProperty.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], int,
        WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], int, WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: int,
        a3: QV4.Value,
    ) -> None:
      """
      Calls Qt's 'void QV4::Runtime::StoreProperty::call(ExecutionEngine *a0,
      const Value &a1, int a2, const Value &a3)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-storeproperty.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : int
        Passed on as it is.

      a3 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::StoreProperty::call(ExecutionEngine *a0, const
      #      Value &a1, int a2, const Value &a3)
      Rituals.call(
          'ritual_ZN3QV47Runtime13StoreProperty4callEPNS_15ExecutionEngineE'
          'RKNS_5ValueEiS6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
          CuteMixin._valueOf(a3),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::StoreProperty'

    #  Qt's '~QV4::Runtime::StoreProperty()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::StoreProperty behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime13StorePropertyD1Ev'

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

  class StoreSuperProperty(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::StoreSuperProperty: a plain Python
    object standing in front of one C++ QV4::Runtime::StoreSuperProperty.

    C++ hands a QV4::Runtime::StoreSuperProperty around as a copy, so every
    C++ QV4::Runtime::StoreSuperProperty behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::StoreSuperProperty that has a ritual
    and that Python can call so far, 1 name in all: 'call'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::StoreSuperProperty::~StoreSuperProperty()': the
      destructor: Python removes its C++ QV4::Runtime::StoreSuperProperty by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::StoreSuperProperty is created at the first use,
      not by 'QV4::Runtime::StoreSuperProperty(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::StoreSuperProperty back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::StoreSuperProperty.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(
        WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'], WAIT['QV4.Value'],
    )
    @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(
        a0: Optional[QV4.ExecutionEngine],
        a1: QV4.Value,
        a2: QV4.Value,
    ) -> None:
      """
      Calls Qt's 'void QV4::Runtime::StoreSuperProperty::call(ExecutionEngine
      *a0, const Value &a1, const Value &a2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-storesuperproperty.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a2 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::StoreSuperProperty::call(ExecutionEngine *a0,
      #      const Value &a1, const Value &a2)
      Rituals.call(
          'ritual_ZN3QV47Runtime18StoreSuperProperty4callEPNS_15ExecutionEn'
          'gineERKNS_5ValueES6_',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
          CuteMixin._valueOf(a2),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::StoreSuperProperty'

    #  Qt's '~QV4::Runtime::StoreSuperProperty()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::StoreSuperProperty
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime18StoreSuperPropertyD1Ev'

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

  class StrictEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::StrictEqual: a plain Python object
    standing in front of one C++ QV4::Runtime::StrictEqual.

    C++ hands a QV4::Runtime::StrictEqual around as a copy, so every C++
    QV4::Runtime::StrictEqual behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::StrictEqual that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::StrictEqual::~StrictEqual()': the destructor:
      Python removes its C++ QV4::Runtime::StrictEqual by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::StrictEqual is created at the first use, not by
      'QV4::Runtime::StrictEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::StrictEqual back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::StrictEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::StrictEqual::call(const Value
      &a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-strictequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::StrictEqual::call(const Value &a0, const
      #      Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime11StrictEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::StrictEqual'

    #  Qt's '~QV4::Runtime::StrictEqual()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::StrictEqual behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime11StrictEqualD1Ev'

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

  class StrictNotEqual(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::StrictNotEqual: a plain Python object
    standing in front of one C++ QV4::Runtime::StrictNotEqual.

    C++ hands a QV4::Runtime::StrictNotEqual around as a copy, so every C++
    QV4::Runtime::StrictNotEqual behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::StrictNotEqual that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::StrictNotEqual::~StrictNotEqual()': the destructor:
      Python removes its C++ QV4::Runtime::StrictNotEqual by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::StrictNotEqual is created at the first use, not
      by 'QV4::Runtime::StrictNotEqual(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::StrictNotEqual back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::StrictNotEqual.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::StrictNotEqual::call(const
      Value &a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-strictnotequal.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::StrictNotEqual::call(const Value &a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime14StrictNotEqual4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::StrictNotEqual'

    #  Qt's '~QV4::Runtime::StrictNotEqual()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::StrictNotEqual behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime14StrictNotEqualD1Ev'

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

  class Sub(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::Sub: a plain Python object standing
    in front of one C++ QV4::Runtime::Sub.

    C++ hands a QV4::Runtime::Sub around as a copy, so every C++
    QV4::Runtime::Sub behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::Sub that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::Sub::~Sub()': the destructor: Python removes its
      C++ QV4::Runtime::Sub by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::Sub is created at the first use, not by
      'QV4::Runtime::Sub(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::Sub back gives a copy the ritual made
      for Python, in a new cute QV4::Runtime::Sub.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::Sub::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-sub.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::Sub::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime3Sub4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::Sub'

    #  Qt's '~QV4::Runtime::Sub()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::Sub behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime3SubD1Ev'

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

  class TailCall(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::TailCall: a plain Python object
    standing in front of one C++ QV4::Runtime::TailCall.

    C++ hands a QV4::Runtime::TailCall around as a copy, so every C++
    QV4::Runtime::TailCall behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::TailCall that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::TailCall::~TailCall()': the destructor: Python
      removes its C++ QV4::Runtime::TailCall by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::TailCall is created at the first use, not by
      'QV4::Runtime::TailCall(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::TailCall back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::TailCall.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.JSTypesStackFrame'], WAIT['QV4.ExecutionEngine'])
    @overload(WAIT['QV4.JSTypesStackFrame'], NoneType)
    @overload(NoneType, WAIT['QV4.ExecutionEngine'])
    @overload(NoneType, NoneType)
    def call(
        a0: Optional[QV4.JSTypesStackFrame],
        engine: Optional[QV4.ExecutionEngine],
    ) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::TailCall::call(JSTypesStackFrame *a0, ExecutionEngine
      *engine)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-tailcall.html#call

      Parameters
      ----------

      a0 : Optional[QV4.JSTypesStackFrame]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      engine : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  ReturnedValue QV4::Runtime::TailCall::call(JSTypesStackFrame *a0,
      #      ExecutionEngine *engine)
      return Rituals.call(
          'ritual_ZN3QV47Runtime8TailCall4callEPNS_17JSTypesStackFrameEPNS_'
          '15ExecutionEngineE',
          CuteMixin._addressOf(a0), CuteMixin._addressOf(engine),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::TailCall'

    #  Qt's '~QV4::Runtime::TailCall()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::TailCall behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime8TailCallD1Ev'

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

  class ThrowException(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ThrowException: a plain Python object
    standing in front of one C++ QV4::Runtime::ThrowException.

    C++ hands a QV4::Runtime::ThrowException around as a copy, so every C++
    QV4::Runtime::ThrowException behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ThrowException that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ThrowException::~ThrowException()': the destructor:
      Python removes its C++ QV4::Runtime::ThrowException by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ThrowException is created at the first use, not
      by 'QV4::Runtime::ThrowException(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ThrowException back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::ThrowException.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> None:
      """
      Calls Qt's 'void QV4::Runtime::ThrowException::call(ExecutionEngine
      *a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-throwexception.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::ThrowException::call(ExecutionEngine *a0, const
      #      Value &a1)
      Rituals.call(
          'ritual_ZN3QV47Runtime14ThrowException4callEPNS_15ExecutionEngine'
          'ERKNS_5ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ThrowException'

    #  Qt's '~QV4::Runtime::ThrowException()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::ThrowException behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime14ThrowExceptionD1Ev'

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

  class ThrowOnNullOrUndefined(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ThrowOnNullOrUndefined: a plain
    Python object standing in front of one C++
    QV4::Runtime::ThrowOnNullOrUndefined.

    C++ hands a QV4::Runtime::ThrowOnNullOrUndefined around as a copy, so
    every C++ QV4::Runtime::ThrowOnNullOrUndefined behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ThrowOnNullOrUndefined that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ThrowOnNullOrUndefined::~ThrowOnNullOrUndefined()':
      the destructor: Python removes its C++
      QV4::Runtime::ThrowOnNullOrUndefined by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ThrowOnNullOrUndefined is created at the first
      use, not by 'QV4::Runtime::ThrowOnNullOrUndefined(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ThrowOnNullOrUndefined back gives a
      copy the ritual made for Python, in a new cute
      QV4::Runtime::ThrowOnNullOrUndefined.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> None:
      """
      Calls Qt's 'void
      QV4::Runtime::ThrowOnNullOrUndefined::call(ExecutionEngine *a0, const
      Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-throwonnullorundefined.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  void QV4::Runtime::ThrowOnNullOrUndefined::call(ExecutionEngine *a0,
      #      const Value &a1)
      Rituals.call(
          'ritual_ZN3QV47Runtime22ThrowOnNullOrUndefined4callEPNS_15Executi'
          'onEngineERKNS_5ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ThrowOnNullOrUndefined'

    #  Qt's '~QV4::Runtime::ThrowOnNullOrUndefined()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QV4::Runtime::ThrowOnNullOrUndefined behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime22ThrowOnNullOrUndefinedD1Ev'

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

  class ThrowReferenceError(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ThrowReferenceError: a plain Python
    object standing in front of one C++ QV4::Runtime::ThrowReferenceError.

    C++ hands a QV4::Runtime::ThrowReferenceError around as a copy, so every
    C++ QV4::Runtime::ThrowReferenceError behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ThrowReferenceError that has a
    ritual and that Python can call so far, 1 name in all: 'call'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ThrowReferenceError::~ThrowReferenceError()': the
      destructor: Python removes its C++ QV4::Runtime::ThrowReferenceError by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ThrowReferenceError is created at the first use,
      not by 'QV4::Runtime::ThrowReferenceError(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ThrowReferenceError back gives a copy
      the ritual made for Python, in a new cute
      QV4::Runtime::ThrowReferenceError.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> None:
      """
      Calls Qt's 'void
      QV4::Runtime::ThrowReferenceError::call(ExecutionEngine *a0, int a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-throwreferenceerror.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  void QV4::Runtime::ThrowReferenceError::call(ExecutionEngine *a0,
      #      int a1)
      Rituals.call(
          'ritual_ZN3QV47Runtime19ThrowReferenceError4callEPNS_15ExecutionE'
          'ngineEi',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ThrowReferenceError'

    #  Qt's '~QV4::Runtime::ThrowReferenceError()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Runtime::ThrowReferenceError
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime19ThrowReferenceErrorD1Ev'

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

  class ToBoolean(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ToBoolean: a plain Python object
    standing in front of one C++ QV4::Runtime::ToBoolean.

    C++ hands a QV4::Runtime::ToBoolean around as a copy, so every C++
    QV4::Runtime::ToBoolean behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ToBoolean that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ToBoolean::~ToBoolean()': the destructor: Python
      removes its C++ QV4::Runtime::ToBoolean by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ToBoolean is created at the first use, not by
      'QV4::Runtime::ToBoolean(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ToBoolean back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::ToBoolean.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'])
    def call(a0: QV4.Value) -> int:
      """
      Calls Qt's 'Bool QV4::Runtime::ToBoolean::call(const Value &a0)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-toboolean.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  Bool QV4::Runtime::ToBoolean::call(const Value &a0)
      return Rituals.call(
          'ritual_ZN3QV47Runtime9ToBoolean4callERKNS_5ValueE',
          CuteMixin._valueOf(a0),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ToBoolean'

    #  Qt's '~QV4::Runtime::ToBoolean()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::ToBoolean behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime9ToBooleanD1Ev'

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

  class ToNumber(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ToNumber: a plain Python object
    standing in front of one C++ QV4::Runtime::ToNumber.

    C++ hands a QV4::Runtime::ToNumber around as a copy, so every C++
    QV4::Runtime::ToNumber behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ToNumber that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ToNumber::~ToNumber()': the destructor: Python
      removes its C++ QV4::Runtime::ToNumber by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ToNumber is created at the first use, not by
      'QV4::Runtime::ToNumber(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ToNumber back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::ToNumber.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::ToNumber::call(ExecutionEngine
      *a0, const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-tonumber.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::ToNumber::call(ExecutionEngine *a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime8ToNumber4callEPNS_15ExecutionEngineERKNS_5'
          'ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ToNumber'

    #  Qt's '~QV4::Runtime::ToNumber()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::ToNumber behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime8ToNumberD1Ev'

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

  class ToObject(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::ToObject: a plain Python object
    standing in front of one C++ QV4::Runtime::ToObject.

    C++ hands a QV4::Runtime::ToObject around as a copy, so every C++
    QV4::Runtime::ToObject behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::ToObject that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::ToObject::~ToObject()': the destructor: Python
      removes its C++ QV4::Runtime::ToObject by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QV4::Runtime::ToObject is created at the first use, not by
      'QV4::Runtime::ToObject(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::ToObject back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::ToObject.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::ToObject::call(ExecutionEngine
      *a0, const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-toobject.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::ToObject::call(ExecutionEngine *a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime8ToObject4callEPNS_15ExecutionEngineERKNS_5'
          'ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::ToObject'

    #  Qt's '~QV4::Runtime::ToObject()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::ToObject behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime8ToObjectD1Ev'

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

  class TypeofName(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::TypeofName: a plain Python object
    standing in front of one C++ QV4::Runtime::TypeofName.

    C++ hands a QV4::Runtime::TypeofName around as a copy, so every C++
    QV4::Runtime::TypeofName behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::TypeofName that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::TypeofName::~TypeofName()': the destructor: Python
      removes its C++ QV4::Runtime::TypeofName by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::TypeofName is created at the first use, not by
      'QV4::Runtime::TypeofName(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::TypeofName back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::TypeofName.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], int)
    @overload(NoneType, int)
    def call(a0: Optional[QV4.ExecutionEngine], a1: int) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::TypeofName::call(ExecutionEngine *a0, int a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-typeofname.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : int
        Passed on as it is.
      """
      #  ReturnedValue QV4::Runtime::TypeofName::call(ExecutionEngine *a0,
      #      int a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime10TypeofName4callEPNS_15ExecutionEngineEi',
          CuteMixin._addressOf(a0), a1,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::TypeofName'

    #  Qt's '~QV4::Runtime::TypeofName()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::TypeofName behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime10TypeofNameD1Ev'

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

  class TypeofValue(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::TypeofValue: a plain Python object
    standing in front of one C++ QV4::Runtime::TypeofValue.

    C++ hands a QV4::Runtime::TypeofValue around as a copy, so every C++
    QV4::Runtime::TypeofValue behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::TypeofValue that has a ritual and
    that Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::TypeofValue::~TypeofValue()': the destructor:
      Python removes its C++ QV4::Runtime::TypeofValue by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::TypeofValue is created at the first use, not by
      'QV4::Runtime::TypeofValue(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::TypeofValue back gives a copy the
      ritual made for Python, in a new cute QV4::Runtime::TypeofValue.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
    @overload(NoneType, WAIT['QV4.Value'])
    def call(a0: Optional[QV4.ExecutionEngine], a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue
      QV4::Runtime::TypeofValue::call(ExecutionEngine *a0, const Value &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-runtime-typeofvalue.html#call

      Parameters
      ----------

      a0 : Optional[QV4.ExecutionEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::TypeofValue::call(ExecutionEngine *a0,
      #      const Value &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime11TypeofValue4callEPNS_15ExecutionEngineERK'
          'NS_5ValueE',
          CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::TypeofValue'

    #  Qt's '~QV4::Runtime::TypeofValue()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Runtime::TypeofValue behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime11TypeofValueD1Ev'

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

  class UMinus(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::UMinus: a plain Python object
    standing in front of one C++ QV4::Runtime::UMinus.

    C++ hands a QV4::Runtime::UMinus around as a copy, so every C++
    QV4::Runtime::UMinus behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::UMinus that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::UMinus::~UMinus()': the destructor: Python removes
      its C++ QV4::Runtime::UMinus by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::UMinus is created at the first use, not by
      'QV4::Runtime::UMinus(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::UMinus back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::UMinus.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'])
    def call(a0: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::UMinus::call(const Value &a0)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-uminus.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::UMinus::call(const Value &a0)
      return Rituals.call(
          'ritual_ZN3QV47Runtime6UMinus4callERKNS_5ValueE',
          CuteMixin._valueOf(a0),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::UMinus'

    #  Qt's '~QV4::Runtime::UMinus()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::UMinus behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime6UMinusD1Ev'

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

  class UShr(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Runtime::UShr: a plain Python object standing
    in front of one C++ QV4::Runtime::UShr.

    C++ hands a QV4::Runtime::UShr around as a copy, so every C++
    QV4::Runtime::UShr behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Runtime::UShr that has a ritual and that
    Python can call so far, 1 name in all: 'call'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Runtime::UShr::~UShr()': the destructor: Python removes its
      C++ QV4::Runtime::UShr by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Runtime::UShr is created at the first use, not by
      'QV4::Runtime::UShr(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Runtime::UShr back gives a copy the ritual
      made for Python, in a new cute QV4::Runtime::UShr.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
    def call(a0: QV4.Value, a1: QV4.Value) -> int:
      """
      Calls Qt's 'ReturnedValue QV4::Runtime::UShr::call(const Value &a0,
      const Value &a1)'.

      Qt's own words: https://doc.qt.io/qt-6/qv4-runtime-ushr.html#call

      Parameters
      ----------

      a0 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.

      a1 : QV4.Value
        Passed on as a value: Qt reads the C++ QV4::Value, which stays
        Python's own.
      """
      #  ReturnedValue QV4::Runtime::UShr::call(const Value &a0, const Value
      #      &a1)
      return Rituals.call(
          'ritual_ZN3QV47Runtime4UShr4callERKNS_5ValueES4_',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Runtime::UShr'

    #  Qt's '~QV4::Runtime::UShr()'. Naming it makes this a value class:
    #  Python owns every C++ QV4::Runtime::UShr behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47Runtime4UShrD1Ev'

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
  __qt_class__ = 'QV4::Runtime'

  #  Qt's '~QV4::Runtime()'. Naming it makes this a value class: Python owns
  #  every C++ QV4::Runtime behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV47RuntimeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def symbolTable(*__, **_) -> Never:
    """
    Qt's 'QHash<const void *, const char *> QV4::Runtime::symbolTable()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.Runtime.symbolTable' has no cute function yet. Qt's "
        "'QHash<const void *, const char *> QV4::Runtime::symbolTable()': "
        "gives a type Python has no way to take yet.")
