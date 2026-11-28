"""
QV4::StringCtor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::StringCtor to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StringCtor(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::StringCtor: a plain Python object standing in
  front of one C++ QV4::StringCtor.

  It is built on the cute 'QV4::FunctionObject', as Qt's QV4::StringCtor is
  built on Qt's QV4::FunctionObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::StringCtor that has a ritual and that Python
  can call so far, 8 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualCallAsConstructor', 'virtualCall', 'method_fromCharCode',
  'method_fromCodePoint', 'method_raw'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::StringCtor is created at the first use, not by
    'QV4::StringCtor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::StringCtor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, int, QV4.Value)
  @overload(QV4.FunctionObject, QV4.Value, int, NoneType)
  @overload(QV4.FunctionObject, NoneType, int, QV4.Value)
  @overload(QV4.FunctionObject, NoneType, int, NoneType)
  @overload(NoneType, QV4.Value, int, QV4.Value)
  @overload(NoneType, QV4.Value, int, NoneType)
  @overload(NoneType, NoneType, int, QV4.Value)
  @overload(NoneType, NoneType, int, NoneType)
  def virtualCallAsConstructor(
      f: Optional[QV4.FunctionObject],
      argv: Optional[QV4.Value],
      argc: int,
      a3: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::StringCtor::virtualCallAsConstructor(const
    FunctionObject *f, const Value *argv, int argc, const Value *a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringctor.html#virtualCallAsConstructor

    Parameters
    ----------

    f : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.

    a3 : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::StringCtor::virtualCallAsConstructor(const
    #      FunctionObject *f, const Value *argv, int argc, const Value *a3)
    return Rituals.call(
        'ritual_ZN3QV410StringCtor24virtualCallAsConstructorEPKNS_14Functio'
        'nObjectEPKNS_5ValueEiS6_',
        CuteMixin._addressOf(f), CuteMixin._addressOf(argv), argc,
        CuteMixin._addressOf(a3),
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def virtualCall(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::StringCtor::virtualCall(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-stringctor.html#virtualCall

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
    #  ReturnedValue QV4::StringCtor::virtualCall(const FunctionObject *a0,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV410StringCtor11virtualCallEPKNS_14FunctionObjectEPKNS_'
        '5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_fromCharCode(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::StringCtor::method_fromCharCode(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringctor.html#method_fromCharCode

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
    #  ReturnedValue QV4::StringCtor::method_fromCharCode(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV410StringCtor19method_fromCharCodeEPKNS_14FunctionObje'
        'ctEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_fromCodePoint(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::StringCtor::method_fromCodePoint(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringctor.html#method_fromCodePoint

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
    #  ReturnedValue QV4::StringCtor::method_fromCodePoint(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV410StringCtor20method_fromCodePointEPKNS_14FunctionObj'
        'ectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_raw(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::StringCtor::method_raw(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-stringctor.html#method_raw

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
    #  ReturnedValue QV4::StringCtor::method_raw(const FunctionObject *a0,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV410StringCtor10method_rawEPKNS_14FunctionObjectEPKNS_5'
        'ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::StringCtor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.StringCtor]:
    """
    Calls Qt's 'QV4::Heap::StringCtor *QV4::StringCtor::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-stringctor.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.StringCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::StringCtor *QV4::StringCtor::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV410StringCtor11d_uncheckedEv')
    return QV4.Heap.StringCtor._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.StringCtor]:
    """
    Calls Qt's 'QV4::Heap::StringCtor *QV4::StringCtor::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-stringctor.html#d

    Returns
    -------

    Optional[QV4.Heap.StringCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::StringCtor *QV4::StringCtor::d() const
    address = self.uglySide.call('ritual_ZNK3QV410StringCtor1dEv')
    return QV4.Heap.StringCtor._cuteAt(address)

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
    Calls Qt's 'void QV4::StringCtor::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-stringctor.html#__dataTest
    """
    #  void QV4::StringCtor::__dataTest()
    self.uglySide.call('ritual_ZN3QV410StringCtor10__dataTestEv')
