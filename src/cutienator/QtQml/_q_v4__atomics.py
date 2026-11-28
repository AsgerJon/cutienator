"""
QV4::Atomics binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4atomics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Atomics to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
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


class Atomics(QV4.Object):
  """
  The cute side of Qt's QV4::Atomics: a plain Python object standing in front
  of one C++ QV4::Atomics.

  It is built on the cute 'QV4::Object', as Qt's QV4::Atomics is built on
  Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Atomics that has a ritual and that Python can
  call so far, 6 names in all: '__dataTest', 'd_unchecked', 'd',
  'method_isLockFree', 'method_wait', 'method_wake'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  14 of the 20 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 forbidden;
  1 not a gap; 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::Atomics is created at the first use, not by
    'QV4::Atomics(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Atomics.
  - Each name of Qt's QV4::Atomics that has no cute function yet,
    'method_add', 'method_and', 'method_compareExchange', 'method_exchange',
    'method_load', 'method_or', 'method_store', 'method_sub', 'method_xor',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
  def method_isLockFree(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Atomics::method_isLockFree(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-atomics.html#method_isLockFree

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::Atomics::method_isLockFree(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV47Atomics17method_isLockFreeEPKNS_14FunctionObjectEPKN'
        'S_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
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
  def method_wait(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Atomics::method_wait(const FunctionObject
    *a0, const Value *thisObject, const Value *argv, int argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-atomics.html#method_wait

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::Atomics::method_wait(const FunctionObject *a0,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV47Atomics11method_waitEPKNS_14FunctionObjectEPKNS_5Val'
        'ueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
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
  def method_wake(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Atomics::method_wake(const FunctionObject
    *a0, const Value *thisObject, const Value *argv, int argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-atomics.html#method_wake

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::Atomics::method_wake(const FunctionObject *a0,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV47Atomics11method_wakeEPKNS_14FunctionObjectEPKNS_5Val'
        'ueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Atomics'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.Atomics]:
    """
    Calls Qt's 'QV4::Heap::Atomics *QV4::Atomics::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-atomics.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.Atomics]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Atomics *QV4::Atomics::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV47Atomics11d_uncheckedEv')
    return QV4.Heap.Atomics._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.Atomics]:
    """
    Calls Qt's 'QV4::Heap::Atomics *QV4::Atomics::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-atomics.html#d

    Returns
    -------

    Optional[QV4.Heap.Atomics]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Atomics *QV4::Atomics::d() const
    address = self.uglySide.call('ritual_ZNK3QV47Atomics1dEv')
    return QV4.Heap.Atomics._cuteAt(address)

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
    Calls Qt's 'void QV4::Atomics::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-atomics.html#__dataTest
    """
    #  void QV4::Atomics::__dataTest()
    self.uglySide.call('ritual_ZN3QV47Atomics10__dataTestEv')

  @staticmethod
  def method_add(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Atomics::method_add(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'atomicReadModifyWrite'.
    """
    raise NotImplementedError(
        "'QV4.Atomics.method_add' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Atomics::method_add(const FunctionObject *a0, "
        "const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'atomicReadModifyWrite'.")

  @staticmethod
  def method_and(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Atomics::method_and(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'atomicReadModifyWrite'.
    """
    raise NotImplementedError(
        "'QV4.Atomics.method_and' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Atomics::method_and(const FunctionObject *a0, "
        "const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'atomicReadModifyWrite'.")

  @staticmethod
  def method_compareExchange(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Atomics::method_compareExchange(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'validateSharedIntegerTypedArray'.
    """
    raise NotImplementedError(
        "'QV4.Atomics.method_compareExchange' has no cute function yet. "
        "Qt's 'ReturnedValue QV4::Atomics::method_compareExchange(const "
        "FunctionObject *a0, const Value *thisObject, const Value *argv, "
        "int argc)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'validateSharedIntegerTypedArray'.")

  @staticmethod
  def method_exchange(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Atomics::method_exchange(const FunctionObject
    *a0, const Value *thisObject, const Value *argv, int argc)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'atomicReadModifyWrite'.
    """
    raise NotImplementedError(
        "'QV4.Atomics.method_exchange' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Atomics::method_exchange(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'atomicReadModifyWrite'.")

  @staticmethod
  def method_load(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Atomics::method_load(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'validateSharedIntegerTypedArray'.
    """
    raise NotImplementedError(
        "'QV4.Atomics.method_load' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Atomics::method_load(const FunctionObject *a0, "
        "const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'validateSharedIntegerTypedArray'.")

  @staticmethod
  def method_or(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Atomics::method_or(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'atomicReadModifyWrite'.
    """
    raise NotImplementedError(
        "'QV4.Atomics.method_or' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Atomics::method_or(const FunctionObject *a0, "
        "const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'atomicReadModifyWrite'.")

  @staticmethod
  def method_store(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Atomics::method_store(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'validateSharedIntegerTypedArray'.
    """
    raise NotImplementedError(
        "'QV4.Atomics.method_store' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Atomics::method_store(const FunctionObject "
        "*a0, const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'validateSharedIntegerTypedArray'.")

  @staticmethod
  def method_sub(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Atomics::method_sub(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'atomicReadModifyWrite'.
    """
    raise NotImplementedError(
        "'QV4.Atomics.method_sub' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Atomics::method_sub(const FunctionObject *a0, "
        "const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'atomicReadModifyWrite'.")

  @staticmethod
  def method_xor(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Atomics::method_xor(const FunctionObject *a0,
    const Value *thisObject, const Value *argv, int argc)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'atomicReadModifyWrite'.
    """
    raise NotImplementedError(
        "'QV4.Atomics.method_xor' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Atomics::method_xor(const FunctionObject *a0, "
        "const Value *thisObject, const Value *argv, int argc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'atomicReadModifyWrite'.")
