"""
QTime binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qdatetime.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Qt


class QTime(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTime: a plain Python object standing in front of one
  C++ QTime.

  C++ hands a QTime around as a copy, so every C++ QTime behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTime that has a ritual and that Python can call so
  far, 16 names in all: 'isNull', 'isValid', 'hour', 'minute', 'second',
  'msec', 'toString', 'setHMS', 'addSecs', 'secsTo', 'addMSecs', 'msecsTo',
  'fromMSecsSinceStartOfDay', 'msecsSinceStartOfDay', 'currentTime',
  'fromString'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QTime::toString(QStringView format) const': takes in Python
    what 'QString QTime::toString(const QString &format) const' takes.
  - Qt's 'QTime QTime::fromString(const QString &string, QStringView
    format)': takes in Python what 'QTime QTime::fromString(QStringView
    string, QStringView format)' takes.
  - Qt's 'QTime QTime::fromString(const QString &string, Qt::DateFormat
    format)': takes in Python what 'QTime QTime::fromString(QStringView
    string, Qt::DateFormat format)' takes.
  - Qt's 'QTime QTime::fromString(const QString &string, const QString
    &format)': takes in Python what 'QTime QTime::fromString(QStringView
    string, QStringView format)' takes.
  - Qt's 'QTime::~QTime()': the destructor: Python removes its C++ QTime by
    it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 private.

  What to expect
  --------------

  - The C++ QTime is created at the first use, not by 'QTime(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTime back gives a copy the ritual made for Python,
    in a new cute QTime.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def fromMSecsSinceStartOfDay(msecs: int) -> QTime:
    """
    Calls Qt's 'QTime QTime::fromMSecsSinceStartOfDay(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtime.html#fromMSecsSinceStartOfDay

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QTime::fromMSecsSinceStartOfDay(int msecs)
    address = Rituals.call(
        'ritual_ZN5QTime24fromMSecsSinceStartOfDayEi', msecs,
    )
    return QTime._cuteOwning(address)

  @staticmethod
  def currentTime() -> QTime:
    """
    Calls Qt's 'QTime QTime::currentTime()'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#currentTime

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QTime::currentTime()
    address = Rituals.call('ritual_ZN5QTime11currentTimeEv')
    return QTime._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, Qt.DateFormat)
  def fromString(
      string: str,
      format: Qt.DateFormat = Qt.DateFormat.TextDate,
  ) -> QTime:
    """
    Calls Qt's 'QTime QTime::fromString(QStringView string, Qt::DateFormat
    format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : Qt.DateFormat
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.DateFormat.TextDate.

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QTime::fromString(QStringView string, Qt::DateFormat format)
    address = Rituals.call(
        'ritual_ZN5QTime10fromStringE11QStringViewN2Qt10DateFormatE',
        string, format.value,
    )
    return QTime._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def fromString(string: str, format: str) -> QTime:
    """
    Calls Qt's 'QTime QTime::fromString(QStringView string, QStringView
    format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QTime::fromString(QStringView string, QStringView format)
    address = Rituals.call(
        'ritual_ZN5QTime10fromStringE11QStringViewS0_', string, format,
    )
    return QTime._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTime'

  #  Qt's '~QTime()'. Naming it makes this a value class: Python owns every
  #  C++ QTime behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QTimeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QTime::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#isNull
    """
    #  bool QTime::isNull() const
    return self.uglySide.call('ritual_ZNK5QTime6isNullEv')

  @overload()
  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTime::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#isValid
    """
    #  bool QTime::isValid() const
    return self.uglySide.call('ritual_ZNK5QTime7isValidEv')

  @staticmethod
  @overload(int, int, int)
  @overload(int, int, int, int)
  def isValid(h: int, m: int, s: int, ms: int = 0) -> bool:
    """
    Calls Qt's 'bool QTime::isValid(int h, int m, int s, int ms)'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#isValid

    Parameters
    ----------

    h : int
      Passed on as it is.

    m : int
      Passed on as it is.

    s : int
      Passed on as it is.

    ms : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QTime::isValid(int h, int m, int s, int ms)
    return Rituals.call('ritual_ZN5QTime7isValidEiiii', h, m, s, ms)

  def hour(self) -> int:
    """
    Calls Qt's 'int QTime::hour() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#hour
    """
    #  int QTime::hour() const
    return self.uglySide.call('ritual_ZNK5QTime4hourEv')

  def minute(self) -> int:
    """
    Calls Qt's 'int QTime::minute() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#minute
    """
    #  int QTime::minute() const
    return self.uglySide.call('ritual_ZNK5QTime6minuteEv')

  def second(self) -> int:
    """
    Calls Qt's 'int QTime::second() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#second
    """
    #  int QTime::second() const
    return self.uglySide.call('ritual_ZNK5QTime6secondEv')

  def msec(self) -> int:
    """
    Calls Qt's 'int QTime::msec() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#msec
    """
    #  int QTime::msec() const
    return self.uglySide.call('ritual_ZNK5QTime4msecEv')

  @overload()
  @overload(Qt.DateFormat)
  def toString(self, f: Qt.DateFormat = Qt.DateFormat.TextDate) -> str:
    """
    Calls Qt's 'QString QTime::toString(Qt::DateFormat f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#toString

    Parameters
    ----------

    f : Qt.DateFormat
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.DateFormat.TextDate.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTime::toString(Qt::DateFormat f) const
    return self.uglySide.call(
        'ritual_ZNK5QTime8toStringEN2Qt10DateFormatE', f.value,
    )

  @overload(str)
  def toString(self, format: str) -> str:
    """
    Calls Qt's 'QString QTime::toString(const QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#toString

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTime::toString(const QString &format) const
    return self.uglySide.call('ritual_ZNK5QTime8toStringERK7QString', format)

  @overload(int)
  def addSecs(self, secs: int) -> QTime:
    """
    Calls Qt's 'QTime QTime::addSecs(int secs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#addSecs

    Parameters
    ----------

    secs : int
      Passed on as it is.

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QTime::addSecs(int secs) const
    address = self.uglySide.call('ritual_ZNK5QTime7addSecsEi', secs)
    return QTime._cuteOwning(address)

  @overload(THIS)
  def secsTo(self, t: QTime) -> int:
    """
    Calls Qt's 'int QTime::secsTo(QTime t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#secsTo

    Parameters
    ----------

    t : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.
    """
    #  int QTime::secsTo(QTime t) const
    return self.uglySide.call('ritual_ZNK5QTime6secsToES_', self._valueOf(t))

  @overload(int)
  def addMSecs(self, ms: int) -> QTime:
    """
    Calls Qt's 'QTime QTime::addMSecs(int ms) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#addMSecs

    Parameters
    ----------

    ms : int
      Passed on as it is.

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QTime::addMSecs(int ms) const
    address = self.uglySide.call('ritual_ZNK5QTime8addMSecsEi', ms)
    return QTime._cuteOwning(address)

  @overload(THIS)
  def msecsTo(self, t: QTime) -> int:
    """
    Calls Qt's 'int QTime::msecsTo(QTime t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#msecsTo

    Parameters
    ----------

    t : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.
    """
    #  int QTime::msecsTo(QTime t) const
    return self.uglySide.call(
        'ritual_ZNK5QTime7msecsToES_', self._valueOf(t),
    )

  def msecsSinceStartOfDay(self) -> int:
    """
    Calls Qt's 'int QTime::msecsSinceStartOfDay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#msecsSinceStartOfDay
    """
    #  int QTime::msecsSinceStartOfDay() const
    return self.uglySide.call('ritual_ZNK5QTime20msecsSinceStartOfDayEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int)
  @overload(int, int, int, int)
  def setHMS(self, h: int, m: int, s: int, ms: int = 0) -> bool:
    """
    Calls Qt's 'bool QTime::setHMS(int h, int m, int s, int ms)'.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#setHMS

    Parameters
    ----------

    h : int
      Passed on as it is.

    m : int
      Passed on as it is.

    s : int
      Passed on as it is.

    ms : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QTime::setHMS(int h, int m, int s, int ms)
    return self.uglySide.call('ritual_ZN5QTime6setHMSEiiii', h, m, s, ms)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTime::QTime()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#QTime
    """
    #  QTime::QTime()
    self._noteCreation(QTime, lambda: Rituals.call('ritual_ZN5QTimeC1Ev'))

  @overload(int, int)
  @overload(int, int, int)
  @overload(int, int, int, int)
  def __init__(self, h: int, m: int, s: int = 0, ms: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QTime::QTime(int h, int m, int s, int
    ms)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtime.html#QTime

    Parameters
    ----------

    h : int
      Passed on as it is.

    m : int
      Passed on as it is.

    s : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    ms : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTime::QTime(int h, int m, int s, int ms)
    self._noteCreation(QTime, lambda: Rituals.call(
        'ritual_ZN5QTimeC1Eiiii', h, m, s, ms,
    ))

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
