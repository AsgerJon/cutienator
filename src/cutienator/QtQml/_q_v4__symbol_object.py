"""
QV4::SymbolObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4symbol_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::SymbolObject to be private: it declares the class in a
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


class SymbolObject(QV4.Object):
  """
  The cute side of Qt's QV4::SymbolObject: a plain Python object standing in
  front of one C++ QV4::SymbolObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::SymbolObject is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::SymbolObject that has a ritual and that Python
  can call so far, 5 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'defaultPrototype'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::SymbolObject is created at the first use, not by
    'QV4::SymbolObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::SymbolObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::SymbolObject::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-symbolobject.html#defaultInternalClass

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass
    #      *QV4::SymbolObject::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV412SymbolObject20defaultInternalClassEPNS_10EngineBase'
        'E',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::SymbolObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-symbolobject.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object *QV4::SymbolObject::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV412SymbolObject16defaultPrototypeEPNS_15ExecutionEngin'
        'eE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::SymbolObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.SymbolObject]:
    """
    Calls Qt's 'QV4::Heap::SymbolObject *QV4::SymbolObject::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbolobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.SymbolObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::SymbolObject *QV4::SymbolObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412SymbolObject11d_uncheckedEv',
    )
    return QV4.Heap.SymbolObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.SymbolObject]:
    """
    Calls Qt's 'QV4::Heap::SymbolObject *QV4::SymbolObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbolobject.html#d

    Returns
    -------

    Optional[QV4.Heap.SymbolObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::SymbolObject *QV4::SymbolObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV412SymbolObject1dEv')
    return QV4.Heap.SymbolObject._cuteAt(address)

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
    Calls Qt's 'void QV4::SymbolObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbolobject.html#__dataTest
    """
    #  void QV4::SymbolObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV412SymbolObject10__dataTestEv')
