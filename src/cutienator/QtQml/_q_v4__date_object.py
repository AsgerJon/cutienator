"""
QV4::DateObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::DateObject to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDate, QDateTime, QTimeZone
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QTimeZone = WAIT['QTimeZone']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DateObject(QV4.ReferenceObject):
  """
  The cute side of Qt's QV4::DateObject: a plain Python object standing in
  front of one C++ QV4::DateObject.

  It is built on the cute 'QV4::ReferenceObject', as Qt's QV4::DateObject is
  built on Qt's QV4::ReferenceObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::DateObject that has a ritual and that Python
  can call so far, 8 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultPrototype', 'date', 'toQDateTime', 'dateTimeToDate',
  'timestampToDateTime'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  11 of the 19 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 forbidden;
  2 leans on 'QV4; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::DateObject is created at the first use, not by
    'QV4::DateObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::DateObject.
  - Each name of Qt's QV4::DateObject that has no cute function yet,
    'componentsToTimestamp', 'dateTimeToNumber', 'dateTimeToString',
    'setDate', 'stringToDateTime', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    *QV4::DateObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-dateobject.html#defaultPrototype

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
    #  QV4::Object *QV4::DateObject::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV410DateObject16defaultPrototypeEPNS_15ExecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(QDateTime)
  def dateTimeToDate(dateTime: QDateTime) -> QDate:
    """
    Calls Qt's 'QDate QV4::DateObject::dateTimeToDate(const QDateTime
    &dateTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-dateobject.html#dateTimeToDate

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QV4::DateObject::dateTimeToDate(const QDateTime &dateTime)
    address = Rituals.call(
        'ritual_ZN3QV410DateObject14dateTimeToDateERK9QDateTime',
        CuteMixin._valueOf(dateTime),
    )
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  @staticmethod
  @overload(float, QTimeZone)
  def timestampToDateTime(timestamp: float, zone: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QV4::DateObject::timestampToDateTime(double
    timestamp, QTimeZone zone)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-dateobject.html#timestampToDateTime

    Parameters
    ----------

    timestamp : float
      Passed on as it is.

    zone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QV4::DateObject::timestampToDateTime(double timestamp,
    #      QTimeZone zone)
    address = Rituals.call(
        'ritual_ZN3QV410DateObject19timestampToDateTimeEd9QTimeZone',
        timestamp, CuteMixin._valueOf(zone),
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::DateObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.DateObject]:
    """
    Calls Qt's 'QV4::Heap::DateObject *QV4::DateObject::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-dateobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.DateObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::DateObject *QV4::DateObject::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV410DateObject11d_uncheckedEv')
    return QV4.Heap.DateObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.DateObject]:
    """
    Calls Qt's 'QV4::Heap::DateObject *QV4::DateObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-dateobject.html#d

    Returns
    -------

    Optional[QV4.Heap.DateObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::DateObject *QV4::DateObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV410DateObject1dEv')
    return QV4.Heap.DateObject._cuteAt(address)

  def date(self) -> float:
    """
    Calls Qt's 'double QV4::DateObject::date() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-dateobject.html#date
    """
    #  double QV4::DateObject::date() const
    return self.uglySide.call('ritual_ZNK3QV410DateObject4dateEv')

  def toQDateTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QV4::DateObject::toQDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-dateobject.html#toQDateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QV4::DateObject::toQDateTime() const
    address = self.uglySide.call('ritual_ZNK3QV410DateObject11toQDateTimeEv')
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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::DateObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-dateobject.html#__dataTest
    """
    #  void QV4::DateObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV410DateObject10__dataTestEv')

  @staticmethod
  def componentsToTimestamp(*__, **_) -> Never:
    """
    Qt's 'double QV4::DateObject::componentsToTimestamp(double year, double
    month, double day, double hours, double mins, double secs, double ms,
    ExecutionEngine *v4)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'MakeTime'.
    """
    raise NotImplementedError(
        "'QV4.DateObject.componentsToTimestamp' has no cute function yet. "
        "Qt's 'double QV4::DateObject::componentsToTimestamp(double year, "
        "double month, double day, double hours, double mins, double secs, "
        "double ms, ExecutionEngine *v4)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'MakeTime'.")

  @staticmethod
  def dateTimeToNumber(*__, **_) -> Never:
    """
    Qt's 'double QV4::DateObject::dateTimeToNumber(const QDateTime
    &dateTime)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'TimeClip'.
    """
    raise NotImplementedError(
        "'QV4.DateObject.dateTimeToNumber' has no cute function yet. Qt's "
        "'double QV4::DateObject::dateTimeToNumber(const QDateTime "
        "&dateTime)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'TimeClip'.")

  @staticmethod
  def dateTimeToString(*__, **_) -> Never:
    """
    Qt's 'QString QV4::DateObject::dateTimeToString(const QDateTime
    &dateTime, ExecutionEngine *engine)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'TimeClip'.
    """
    raise NotImplementedError(
        "'QV4.DateObject.dateTimeToString' has no cute function yet. Qt's "
        "'QString QV4::DateObject::dateTimeToString(const QDateTime "
        "&dateTime, ExecutionEngine *engine)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'TimeClip'.")

  @staticmethod
  def setDate(*__, **_) -> Never:
    """
    Qt's 'void QV4::DateObject::setDate(double date)': leans on
    'QV4::Date::encode(double)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.DateObject.setDate' has no cute function yet. Qt's 'void "
        "QV4::DateObject::setDate(double date)': leans on "
        "'QV4::Date::encode(double)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def stringToDateTime(*__, **_) -> Never:
    """
    Qt's 'QDateTime QV4::DateObject::stringToDateTime(const QString &string,
    ExecutionEngine *engine)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'ParseString'.
    """
    raise NotImplementedError(
        "'QV4.DateObject.stringToDateTime' has no cute function yet. Qt's "
        "'QDateTime QV4::DateObject::stringToDateTime(const QString "
        "&string, ExecutionEngine *engine)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'ParseString'.")
