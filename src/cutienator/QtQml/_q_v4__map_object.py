"""
QV4::MapObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4mapobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::MapObject to be private: it declares the class in a header
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


class MapObject(QV4.Object):
  """
  The cute side of Qt's QV4::MapObject: a plain Python object standing in
  front of one C++ QV4::MapObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::MapObject is built on
  Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::MapObject that has a ritual and that Python can
  call so far, 5 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultPrototype', 'virtualDestroy'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::MapObject is created at the first use, not by
    'QV4::MapObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::MapObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::MapObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-mapobject.html#defaultPrototype

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
    #  QV4::Object *QV4::MapObject::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV49MapObject16defaultPrototypeEPNS_15ExecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::MapObject::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-mapobject.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::MapObject::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV49MapObject14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::MapObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.MapObject]:
    """
    Calls Qt's 'QV4::Heap::MapObject *QV4::MapObject::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-mapobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.MapObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::MapObject *QV4::MapObject::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV49MapObject11d_uncheckedEv')
    return QV4.Heap.MapObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.MapObject]:
    """
    Calls Qt's 'QV4::Heap::MapObject *QV4::MapObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-mapobject.html#d

    Returns
    -------

    Optional[QV4.Heap.MapObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::MapObject *QV4::MapObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV49MapObject1dEv')
    return QV4.Heap.MapObject._cuteAt(address)

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
    Calls Qt's 'void QV4::MapObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-mapobject.html#__dataTest
    """
    #  void QV4::MapObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV49MapObject10__dataTestEv')
