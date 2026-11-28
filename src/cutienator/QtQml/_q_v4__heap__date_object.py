"""
QV4::Heap::DateObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Heap::DateObject to be private: it declares the class in a
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

  from ..QtCore import QDateTime, QVariant

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DateObject(QV4.Heap.ReferenceObject, QV4.Heap.DateObjectData):
  """
  The cute side of Qt's QV4::Heap::DateObject: a plain Python object standing
  in front of one C++ QV4::Heap::DateObject.

  It is built on the cute 'QV4::Heap::ReferenceObject', as Qt's
  QV4::Heap::DateObject is built on Qt's QV4::Heap::ReferenceObject, and has
  everything that class has. It is built on the cute
  'QV4::Heap::DateObjectData' as well, as Qt's QV4::Heap::DateObject is built
  on Qt's QV4::Heap::DateObjectData too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::DateObject that has a ritual and that
  Python can call so far, 7 names in all: 'markObjects', 'doSetLocation',
  'init', 'date', 'toVariant', 'toQDateTime', 'writeBack'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has no ritual
  ------------------

  9 of the 17 functions Qt declares: 9 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::Heap::DateObject is created at the first use, not by
    'QV4::Heap::DateObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::DateObject.
  - Each name of Qt's QV4::Heap::DateObject that has no cute function yet,
    'detached', 'readReference', 'setDate', 'setVariant', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.Heap.Base, WAIT['QV4.MarkStack'])
  @overload(QV4.Heap.Base, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markObjects(
      b: Optional[QV4.Heap.Base],
      stack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::DateObject::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-dateobject.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::DateObject::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap10DateObject11markObjectsEPNS0_4BaseEPNS_9MarkSt'
        'ackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::DateObject'

  #  Qt's QV4::Heap::DateObject is built on more than one class. The part of
  #  a C++ QV4::Heap::DateObject that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::DateObjectData':
          'ritual_cast_QV4_Heap_DateObject_QV4_Heap_DateObjectData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def date(self) -> float:
    """
    Calls Qt's 'double QV4::Heap::DateObject::date() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-dateobject.html#date
    """
    #  double QV4::Heap::DateObject::date() const
    return self.uglySide.call('ritual_ZNK3QV44Heap10DateObject4dateEv')

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::Heap::DateObject::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-dateobject.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::Heap::DateObject::toVariant() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap10DateObject9toVariantEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def toQDateTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QV4::Heap::DateObject::toQDateTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-dateobject.html#toQDateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QV4::Heap::DateObject::toQDateTime() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap10DateObject11toQDateTimeEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

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

  def doSetLocation(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::DateObject::doSetLocation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-dateobject.html#doSetLocation
    """
    #  void QV4::Heap::DateObject::doSetLocation()
    self.uglySide.call('ritual_ZN3QV44Heap10DateObject13doSetLocationEv')

  @overload()
  def init(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::DateObject::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-dateobject.html#init
    """
    #  void QV4::Heap::DateObject::init()
    self.uglySide.call('ritual_ZN3QV44Heap10DateObject4initEv')

  @overload(WAIT['QV4.Date'])
  def init(self, date: QV4.Date) -> None:
    """
    Calls Qt's 'void QV4::Heap::DateObject::init(Date date)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-dateobject.html#init

    Parameters
    ----------

    date : QV4.Date
      Passed on as a value: Qt reads the C++ QV4::Date, which stays Python's
      own.
    """
    #  void QV4::Heap::DateObject::init(Date date)
    self.uglySide.call(
        'ritual_ZN3QV44Heap10DateObject4initENS_4DateE', self._valueOf(date),
    )

  @overload()
  @overload(int)
  def writeBack(self, internalIndex: int = -1) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::DateObject::writeBack(int internalIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-dateobject.html#writeBack

    Parameters
    ----------

    internalIndex : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QV4::Heap::DateObject::writeBack(int internalIndex)
    return self.uglySide.call(
        'ritual_ZN3QV44Heap10DateObject9writeBackEi', internalIndex,
    )

  @staticmethod
  def detached(*__, **_) -> Never:
    """
    Qt's 'DateObject *QV4::Heap::DateObject::detached() const': leans on
    'QV4::DateObject::static_vtbl', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.DateObject.detached' has no cute function yet. Qt's "
        "'DateObject *QV4::Heap::DateObject::detached() const': leans on "
        "'QV4::DateObject::static_vtbl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def readReference(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Heap::DateObject::readReference()': leans on
    'QV4::Date::init(QDate)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.DateObject.readReference' has no cute function yet. Qt's "
        "'bool QV4::Heap::DateObject::readReference()': leans on "
        "'QV4::Date::init(QDate)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setDate(*__, **_) -> Never:
    """
    Qt's 'void QV4::Heap::DateObject::setDate(double newDate)': leans on
    'QV4::Date::encode(double)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.DateObject.setDate' has no cute function yet. Qt's 'void "
        "QV4::Heap::DateObject::setDate(double newDate)': leans on "
        "'QV4::Date::encode(double)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setVariant(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Heap::DateObject::setVariant(const QVariant &variant)':
    leans on 'QV4::Date::init(QDate)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.DateObject.setVariant' has no cute function yet. Qt's "
        "'bool QV4::Heap::DateObject::setVariant(const QVariant &variant)': "
        "leans on 'QV4::Date::init(QDate)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
