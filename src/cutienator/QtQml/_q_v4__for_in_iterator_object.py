"""
QV4::ForInIteratorObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ForInIteratorObject to be private: it declares the class in
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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ForInIteratorObject(QV4.Object):
  """
  The cute side of Qt's QV4::ForInIteratorObject: a plain Python object
  standing in front of one C++ QV4::ForInIteratorObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::ForInIteratorObject is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ForInIteratorObject that has a ritual and that
  Python can call so far, 6 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultPrototype', 'virtualDestroy', 'nextProperty'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::ForInIteratorObject is created at the first use, not by
    'QV4::ForInIteratorObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ForInIteratorObject.
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
    *QV4::ForInIteratorObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-foriniteratorobject.html#defaultPrototype

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
    #  QV4::Object
    #      *QV4::ForInIteratorObject::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV419ForInIteratorObject16defaultPrototypeEPNS_15Executi'
        'onEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::ForInIteratorObject::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-foriniteratorobject.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ForInIteratorObject::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV419ForInIteratorObject14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ForInIteratorObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ForInIteratorObject]:
    """
    Calls Qt's 'QV4::Heap::ForInIteratorObject
    *QV4::ForInIteratorObject::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-foriniteratorobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ForInIteratorObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ForInIteratorObject
    #      *QV4::ForInIteratorObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419ForInIteratorObject11d_uncheckedEv',
    )
    return QV4.Heap.ForInIteratorObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ForInIteratorObject]:
    """
    Calls Qt's 'QV4::Heap::ForInIteratorObject *QV4::ForInIteratorObject::d()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-foriniteratorobject.html#d

    Returns
    -------

    Optional[QV4.Heap.ForInIteratorObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ForInIteratorObject *QV4::ForInIteratorObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV419ForInIteratorObject1dEv')
    return QV4.Heap.ForInIteratorObject._cuteAt(address)

  def nextProperty(self) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::ForInIteratorObject::nextProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-foriniteratorobject.html#nextProperty

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::ForInIteratorObject::nextProperty() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419ForInIteratorObject12nextPropertyEv',
    )
    return QV4.PropertyKey._cuteOwning(address)

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
    Calls Qt's 'void QV4::ForInIteratorObject::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-foriniteratorobject.html#__dataTest
    """
    #  void QV4::ForInIteratorObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV419ForInIteratorObject10__dataTestEv')
