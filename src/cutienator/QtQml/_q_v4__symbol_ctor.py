"""
QV4::SymbolCtor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4symbol_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::SymbolCtor to be private: it declares the class in a header
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


class SymbolCtor(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::SymbolCtor: a plain Python object standing in
  front of one C++ QV4::SymbolCtor.

  It is built on the cute 'QV4::FunctionObject', as Qt's QV4::SymbolCtor is
  built on Qt's QV4::FunctionObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::SymbolCtor that has a ritual and that Python
  can call so far, 6 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualCallAsConstructor', 'method_for', 'method_keyFor'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 3 forbidden; 1 not a gap; 1 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file; 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::SymbolCtor is created at the first use, not by
    'QV4::SymbolCtor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::SymbolCtor.
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
      a0: Optional[QV4.FunctionObject],
      argv: Optional[QV4.Value],
      argc: int,
      newTarget: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SymbolCtor::virtualCallAsConstructor(const
    FunctionObject *a0, const Value *argv, int argc, const Value
    *newTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-symbolctor.html#virtualCallAsConstructor

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.

    newTarget : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::SymbolCtor::virtualCallAsConstructor(const
    #      FunctionObject *a0, const Value *argv, int argc, const Value
    #      *newTarget)
    return Rituals.call(
        'ritual_ZN3QV410SymbolCtor24virtualCallAsConstructorEPKNS_14Functio'
        'nObjectEPKNS_5ValueEiS6_',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(argv), argc,
        CuteMixin._addressOf(newTarget),
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
  def method_for(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SymbolCtor::method_for(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbolctor.html#method_for

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
    #  ReturnedValue QV4::SymbolCtor::method_for(const FunctionObject *a0,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV410SymbolCtor10method_forEPKNS_14FunctionObjectEPKNS_5'
        'ValueES6_i',
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
  def method_keyFor(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SymbolCtor::method_keyFor(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbolctor.html#method_keyFor

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
    #  ReturnedValue QV4::SymbolCtor::method_keyFor(const FunctionObject *a0,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV410SymbolCtor13method_keyForEPKNS_14FunctionObjectEPKN'
        'S_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::SymbolCtor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.SymbolCtor]:
    """
    Calls Qt's 'QV4::Heap::SymbolCtor *QV4::SymbolCtor::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbolctor.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.SymbolCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::SymbolCtor *QV4::SymbolCtor::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV410SymbolCtor11d_uncheckedEv')
    return QV4.Heap.SymbolCtor._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.SymbolCtor]:
    """
    Calls Qt's 'QV4::Heap::SymbolCtor *QV4::SymbolCtor::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbolctor.html#d

    Returns
    -------

    Optional[QV4.Heap.SymbolCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::SymbolCtor *QV4::SymbolCtor::d() const
    address = self.uglySide.call('ritual_ZNK3QV410SymbolCtor1dEv')
    return QV4.Heap.SymbolCtor._cuteAt(address)

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
    Calls Qt's 'void QV4::SymbolCtor::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbolctor.html#__dataTest
    """
    #  void QV4::SymbolCtor::__dataTest()
    self.uglySide.call('ritual_ZN3QV410SymbolCtor10__dataTestEv')
