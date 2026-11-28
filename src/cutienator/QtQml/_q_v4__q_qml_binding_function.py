"""
QV4::QQmlBindingFunction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::QQmlBindingFunction to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlSourceLocation

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlBindingFunction(QV4.JavaScriptFunctionObject):
  """
  The cute side of Qt's QV4::QQmlBindingFunction: a plain Python object
  standing in front of one C++ QV4::QQmlBindingFunction.

  It is built on the cute 'QV4::JavaScriptFunctionObject', as Qt's
  QV4::QQmlBindingFunction is built on Qt's QV4::JavaScriptFunctionObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QQmlBindingFunction that has a ritual and that
  Python can call so far, 6 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualCall', 'bindingFunction', 'currentLocation'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::QQmlBindingFunction is created at the first use, not by
    'QV4::QQmlBindingFunction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QQmlBindingFunction.
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
    Calls Qt's 'ReturnedValue QV4::QQmlBindingFunction::virtualCall(const
    FunctionObject *f, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlbindingfunction.html#virtualCall

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
    #  ReturnedValue QV4::QQmlBindingFunction::virtualCall(const
    #      FunctionObject *f, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV419QQmlBindingFunction11virtualCallEPKNS_14FunctionObj'
        'ectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(f), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QQmlBindingFunction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QQmlBindingFunction]:
    """
    Calls Qt's 'QV4::Heap::QQmlBindingFunction
    *QV4::QQmlBindingFunction::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlbindingfunction.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QQmlBindingFunction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlBindingFunction
    #      *QV4::QQmlBindingFunction::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419QQmlBindingFunction11d_uncheckedEv',
    )
    return QV4.Heap.QQmlBindingFunction._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QQmlBindingFunction]:
    """
    Calls Qt's 'QV4::Heap::QQmlBindingFunction *QV4::QQmlBindingFunction::d()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qqmlbindingfunction.html#d

    Returns
    -------

    Optional[QV4.Heap.QQmlBindingFunction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlBindingFunction *QV4::QQmlBindingFunction::d() const
    address = self.uglySide.call('ritual_ZNK3QV419QQmlBindingFunction1dEv')
    return QV4.Heap.QQmlBindingFunction._cuteAt(address)

  def bindingFunction(self) -> Optional[QV4.Heap.JavaScriptFunctionObject]:
    """
    Calls Qt's 'Heap::JavaScriptFunctionObject
    *QV4::QQmlBindingFunction::bindingFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlbindingfunction.html#bindingFunction

    Returns
    -------

    Optional[QV4.Heap.JavaScriptFunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::JavaScriptFunctionObject
    #      *QV4::QQmlBindingFunction::bindingFunction() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419QQmlBindingFunction15bindingFunctionEv',
    )
    return QV4.Heap.JavaScriptFunctionObject._cuteAt(address)

  def currentLocation(self) -> QQmlSourceLocation:
    """
    Calls Qt's 'QQmlSourceLocation
    QV4::QQmlBindingFunction::currentLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlbindingfunction.html#currentLocation

    Returns
    -------

    QQmlSourceLocation
      A new cute QQmlSourceLocation around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlSourceLocation QV4::QQmlBindingFunction::currentLocation() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419QQmlBindingFunction15currentLocationEv',
    )
    from . import QQmlSourceLocation
    return QQmlSourceLocation._cuteOwning(address)

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
    Calls Qt's 'void QV4::QQmlBindingFunction::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlbindingfunction.html#__dataTest
    """
    #  void QV4::QQmlBindingFunction::__dataTest()
    self.uglySide.call('ritual_ZN3QV419QQmlBindingFunction10__dataTestEv')
