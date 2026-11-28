"""
QV4::ConsoleObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::ConsoleObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ConsoleObject(QV4.Object):
  """
  The cute side of Qt's QV4::ConsoleObject: a plain Python object standing in
  front of one C++ QV4::ConsoleObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::ConsoleObject is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ConsoleObject that has a ritual and that Python
  can call so far, 8 names in all: '__dataTest', 'd_unchecked', 'd',
  'method_profile', 'method_profileEnd', 'method_time', 'method_timeEnd',
  'method_count'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has no ritual
  ------------------

  12 of the 20 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 forbidden;
  1 not a gap; 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::ConsoleObject is created at the first use, not by
    'QV4::ConsoleObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ConsoleObject.
  - Each name of Qt's QV4::ConsoleObject that has no cute function yet,
    'method_assert', 'method_error', 'method_exception', 'method_info',
    'method_log', 'method_trace', 'method_warn', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_profile(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ConsoleObject::method_profile(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-consoleobject.html#method_profile

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::ConsoleObject::method_profile(const FunctionObject
    #      *b, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV413ConsoleObject14method_profileEPKNS_14FunctionObject'
        'EPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_profileEnd(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ConsoleObject::method_profileEnd(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-consoleobject.html#method_profileEnd

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::ConsoleObject::method_profileEnd(const
    #      FunctionObject *b, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV413ConsoleObject17method_profileEndEPKNS_14FunctionObj'
        'ectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_time(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ConsoleObject::method_time(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-consoleobject.html#method_time

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::ConsoleObject::method_time(const FunctionObject *b,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV413ConsoleObject11method_timeEPKNS_14FunctionObjectEPK'
        'NS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_timeEnd(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ConsoleObject::method_timeEnd(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-consoleobject.html#method_timeEnd

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::ConsoleObject::method_timeEnd(const FunctionObject
    #      *b, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV413ConsoleObject14method_timeEndEPKNS_14FunctionObject'
        'EPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_count(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ConsoleObject::method_count(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-consoleobject.html#method_count

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::ConsoleObject::method_count(const FunctionObject
    #      *b, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV413ConsoleObject12method_countEPKNS_14FunctionObjectEP'
        'KNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ConsoleObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ConsoleObject]:
    """
    Calls Qt's 'QV4::Heap::ConsoleObject *QV4::ConsoleObject::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-consoleobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ConsoleObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ConsoleObject *QV4::ConsoleObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV413ConsoleObject11d_uncheckedEv',
    )
    return QV4.Heap.ConsoleObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ConsoleObject]:
    """
    Calls Qt's 'QV4::Heap::ConsoleObject *QV4::ConsoleObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-consoleobject.html#d

    Returns
    -------

    Optional[QV4.Heap.ConsoleObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ConsoleObject *QV4::ConsoleObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV413ConsoleObject1dEv')
    return QV4.Heap.ConsoleObject._cuteAt(address)

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::ConsoleObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-consoleobject.html#__dataTest
    """
    #  void QV4::ConsoleObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV413ConsoleObject10__dataTestEv')

  @staticmethod
  def method_assert(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ConsoleObject::method_assert(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'jsStack'.
    """
    raise NotImplementedError(
        "'QV4.ConsoleObject.method_assert' has no cute function yet. Qt's "
        "'ReturnedValue QV4::ConsoleObject::method_assert(const "
        "FunctionObject *b, const Value *thisObject, const Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'jsStack'.")

  @staticmethod
  def method_error(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ConsoleObject::method_error(const FunctionObject
    *b, const Value *thisObject, const Value *argv, int argc)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'writeToConsole'.
    """
    raise NotImplementedError(
        "'QV4.ConsoleObject.method_error' has no cute function yet. Qt's "
        "'ReturnedValue QV4::ConsoleObject::method_error(const "
        "FunctionObject *b, const Value *thisObject, const Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'writeToConsole'.")

  @staticmethod
  def method_exception(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ConsoleObject::method_exception(const
    FunctionObject *b, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'Error'.
    """
    raise NotImplementedError(
        "'QV4.ConsoleObject.method_exception' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::ConsoleObject::method_exception(const "
        "FunctionObject *b, const Value *thisObject, const Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'Error'.")

  @staticmethod
  def method_info(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ConsoleObject::method_info(const FunctionObject
    *b, const Value *thisObject, const Value *argv, int argc)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'writeToConsole'.
    """
    raise NotImplementedError(
        "'QV4.ConsoleObject.method_info' has no cute function yet. Qt's "
        "'ReturnedValue QV4::ConsoleObject::method_info(const "
        "FunctionObject *b, const Value *thisObject, const Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'writeToConsole'.")

  @staticmethod
  def method_log(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ConsoleObject::method_log(const FunctionObject
    *b, const Value *thisObject, const Value *argv, int argc)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'writeToConsole'.
    """
    raise NotImplementedError(
        "'QV4.ConsoleObject.method_log' has no cute function yet. Qt's "
        "'ReturnedValue QV4::ConsoleObject::method_log(const FunctionObject "
        "*b, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'writeToConsole'.")

  @staticmethod
  def method_trace(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ConsoleObject::method_trace(const FunctionObject
    *b, const Value *thisObject, const Value *argv, int argc)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'jsStack'.
    """
    raise NotImplementedError(
        "'QV4.ConsoleObject.method_trace' has no cute function yet. Qt's "
        "'ReturnedValue QV4::ConsoleObject::method_trace(const "
        "FunctionObject *b, const Value *thisObject, const Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'jsStack'.")

  @staticmethod
  def method_warn(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ConsoleObject::method_warn(const FunctionObject
    *b, const Value *thisObject, const Value *argv, int argc)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'writeToConsole'.
    """
    raise NotImplementedError(
        "'QV4.ConsoleObject.method_warn' has no cute function yet. Qt's "
        "'ReturnedValue QV4::ConsoleObject::method_warn(const "
        "FunctionObject *b, const Value *thisObject, const Value *argv, int "
        "argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'writeToConsole'.")
