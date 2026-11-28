"""
QV4::BoundFunction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::BoundFunction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class BoundFunction(QV4.JavaScriptFunctionObject):
  """
  The cute side of Qt's QV4::BoundFunction: a plain Python object standing in
  front of one C++ QV4::BoundFunction.

  It is built on the cute 'QV4::JavaScriptFunctionObject', as Qt's
  QV4::BoundFunction is built on Qt's QV4::JavaScriptFunctionObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::BoundFunction that has a ritual and that Python
  can call so far, 7 names in all: '__dataTest', 'd_unchecked', 'd',
  'target', 'boundThis', 'boundArgs', 'virtualCall'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::BoundFunction is created at the first use, not by
    'QV4::BoundFunction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::BoundFunction.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
      f: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::BoundFunction::virtualCall(const
    FunctionObject *f, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-boundfunction.html#virtualCall

    Parameters
    ----------

    f : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::BoundFunction::virtualCall(const FunctionObject *f,
    #      const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV413BoundFunction11virtualCallEPKNS_14FunctionObjectEPK'
        'NS_5ValueES6_i',
        CuteMixin._addressOf(f), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::BoundFunction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.BoundFunction]:
    """
    Calls Qt's 'QV4::Heap::BoundFunction *QV4::BoundFunction::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-boundfunction.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.BoundFunction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::BoundFunction *QV4::BoundFunction::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV413BoundFunction11d_uncheckedEv',
    )
    return QV4.Heap.BoundFunction._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.BoundFunction]:
    """
    Calls Qt's 'QV4::Heap::BoundFunction *QV4::BoundFunction::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-boundfunction.html#d

    Returns
    -------

    Optional[QV4.Heap.BoundFunction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::BoundFunction *QV4::BoundFunction::d() const
    address = self.uglySide.call('ritual_ZNK3QV413BoundFunction1dEv')
    return QV4.Heap.BoundFunction._cuteAt(address)

  def target(self) -> Optional[QV4.Heap.FunctionObject]:
    """
    Calls Qt's 'Heap::FunctionObject *QV4::BoundFunction::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-boundfunction.html#target

    Returns
    -------

    Optional[QV4.Heap.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::FunctionObject *QV4::BoundFunction::target() const
    address = self.uglySide.call('ritual_ZNK3QV413BoundFunction6targetEv')
    return QV4.Heap.FunctionObject._cuteAt(address)

  def boundThis(self) -> QV4.Value:
    """
    Calls Qt's 'Value QV4::BoundFunction::boundThis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-boundfunction.html#boundThis

    Returns
    -------

    QV4.Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::BoundFunction::boundThis() const
    address = self.uglySide.call('ritual_ZNK3QV413BoundFunction9boundThisEv')
    return QV4.Value._cuteOwning(address)

  def boundArgs(self) -> Optional[QV4.Heap.MemberData]:
    """
    Calls Qt's 'Heap::MemberData *QV4::BoundFunction::boundArgs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-boundfunction.html#boundArgs

    Returns
    -------

    Optional[QV4.Heap.MemberData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::MemberData *QV4::BoundFunction::boundArgs() const
    address = self.uglySide.call('ritual_ZNK3QV413BoundFunction9boundArgsEv')
    return QV4.Heap.MemberData._cuteAt(address)

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
    Calls Qt's 'void QV4::BoundFunction::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-boundfunction.html#__dataTest
    """
    #  void QV4::BoundFunction::__dataTest()
    self.uglySide.call('ritual_ZN3QV413BoundFunction10__dataTestEv')
