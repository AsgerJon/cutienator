"""
QDateTimePattern binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qttemporalpattern_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDateTimePattern to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtTemporalPattern, QLocale

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QCalendar, QDateTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCalendar = WAIT['QCalendar']
  QDateTime = WAIT['QDateTime']


class QDateTimePattern(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDateTimePattern: a plain Python object standing in
  front of one C++ QDateTimePattern.

  C++ hands a QDateTimePattern around as a copy, so every C++
  QDateTimePattern behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDateTimePattern that has a ritual and that Python
  can call so far, 11 names in all: 'dateTimeSupport', 'isValid',
  'setLocale', 'locale', 'setBaseYear', 'clearBaseYear', 'setCalendar',
  'calendar', 'serialize', 'fromQtFormat', 'forLocale'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDateTimePattern::QDateTimePattern(const QList<Field> &fs)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QDateTimePattern::QDateTimePattern(const QList<Field> &fs, int
    centuryStart)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<int> QDateTimePattern::baseYear() const': gives a
    type Python has no way to take yet.
  - Qt's 'QtTemporalPattern::ParseResult<QDateTime>
    QDateTimePattern::parse(QStringView text, const QDateTime &defaults)
    const': gives a type Python has no way to take yet.
  - Qt's 'QDateTimePattern::~QDateTimePattern()': the destructor: Python
    removes its C++ QDateTimePattern by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDateTimePattern is created at the first use, not by
    'QDateTimePattern(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDateTimePattern back gives a copy the ritual made
    for Python, in a new cute QDateTimePattern.
  - Each name of Qt's QDateTimePattern that has no cute function yet,
    '__init__', 'baseYear', 'parse', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def fromQtFormat(format: str) -> QDateTimePattern:
    """
    Calls Qt's 'QDateTimePattern QDateTimePattern::fromQtFormat(QStringView
    format)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimepattern.html#fromQtFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDateTimePattern
      A new cute QDateTimePattern around the copy Qt gave back. Python owns
      it.
    """
    #  QDateTimePattern QDateTimePattern::fromQtFormat(QStringView format)
    address = Rituals.call(
        'ritual_ZN16QDateTimePattern12fromQtFormatE11QStringView', format,
    )
    return QDateTimePattern._cuteOwning(address)

  @staticmethod
  @overload(QLocale)
  @overload(QLocale, QLocale.FormatType)
  def forLocale(
      locale: QLocale,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> QDateTimePattern:
    """
    Calls Qt's 'QDateTimePattern QDateTimePattern::forLocale(const QLocale
    &locale, QLocale::FormatType format)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimepattern.html#forLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    QDateTimePattern
      A new cute QDateTimePattern around the copy Qt gave back. Python owns
      it.
    """
    #  QDateTimePattern QDateTimePattern::forLocale(const QLocale &locale,
    #      QLocale::FormatType format)
    address = Rituals.call(
        'ritual_ZN16QDateTimePattern9forLocaleERK7QLocaleNS0_10FormatTypeE',
        CuteMixin._valueOf(locale), format.value,
    )
    return QDateTimePattern._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDateTimePattern'

  #  Qt's '~QDateTimePattern()'. Naming it makes this a value class: Python
  #  owns every C++ QDateTimePattern behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QDateTimePatternD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def dateTimeSupport(self) -> QtTemporalPattern.SupportType:
    """
    Calls Qt's 'QtTemporalPattern::SupportType
    QDateTimePattern::dateTimeSupport() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimepattern.html#dateTimeSupport

    Returns
    -------

    QtTemporalPattern.SupportType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtTemporalPattern.SupportType(number)' gives.
    """
    #  QtTemporalPattern::SupportType QDateTimePattern::dateTimeSupport()
    #      const
    return QtTemporalPattern.SupportType(self.uglySide.call(
        'ritual_ZNK16QDateTimePattern15dateTimeSupportEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDateTimePattern::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimepattern.html#isValid
    """
    #  bool QDateTimePattern::isValid() const
    return self.uglySide.call('ritual_ZNK16QDateTimePattern7isValidEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'const QLocale &QDateTimePattern::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimepattern.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  const QLocale &QDateTimePattern::locale() const
    address = self.uglySide.call('ritual_ZNK16QDateTimePattern6localeEv')
    return QLocale._cuteOwning(address)

  def calendar(self) -> QCalendar:
    """
    Calls Qt's 'QCalendar QDateTimePattern::calendar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimepattern.html#calendar

    Returns
    -------

    QCalendar
      A new cute QCalendar around the copy Qt gave back. Python owns it.
    """
    #  QCalendar QDateTimePattern::calendar() const
    address = self.uglySide.call('ritual_ZNK16QDateTimePattern8calendarEv')
    from . import QCalendar
    return QCalendar._cuteOwning(address)

  @overload(QDateTime)
  def serialize(self, datetime: QDateTime) -> str:
    """
    Calls Qt's 'QString QDateTimePattern::serialize(const QDateTime
    &datetime) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimepattern.html#serialize

    Parameters
    ----------

    datetime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimePattern::serialize(const QDateTime &datetime) const
    return self.uglySide.call(
        'ritual_ZNK16QDateTimePattern9serializeERK9QDateTime',
        self._valueOf(datetime),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, loc: QLocale) -> None:
    """
    Calls Qt's 'void QDateTimePattern::setLocale(const QLocale &loc)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimepattern.html#setLocale

    Parameters
    ----------

    loc : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QDateTimePattern::setLocale(const QLocale &loc)
    self.uglySide.call(
        'ritual_ZN16QDateTimePattern9setLocaleERK7QLocale',
        self._valueOf(loc),
    )

  @overload(int)
  def setBaseYear(self, centuryStart: int) -> None:
    """
    Calls Qt's 'void QDateTimePattern::setBaseYear(int centuryStart)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimepattern.html#setBaseYear

    Parameters
    ----------

    centuryStart : int
      Passed on as it is.
    """
    #  void QDateTimePattern::setBaseYear(int centuryStart)
    self.uglySide.call(
        'ritual_ZN16QDateTimePattern11setBaseYearEi', centuryStart,
    )

  @overload(QCalendar)
  def setCalendar(self, cal: QCalendar) -> None:
    """
    Calls Qt's 'void QDateTimePattern::setCalendar(QCalendar cal)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimepattern.html#setCalendar

    Parameters
    ----------

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  void QDateTimePattern::setCalendar(QCalendar cal)
    self.uglySide.call(
        'ritual_ZN16QDateTimePattern11setCalendarE9QCalendar',
        self._valueOf(cal),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QDateTimePattern::QDateTimePattern(const QList<Field> &fs)':
      takes a type Python has no way to hand over yet.
    - Qt's 'QDateTimePattern::QDateTimePattern(const QList<Field> &fs, int
      centuryStart)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDateTimePattern.__init__' has no cute function yet. Qt's "
        "'QDateTimePattern::QDateTimePattern(const QList<Field> &fs)': "
        "takes a type Python has no way to hand over yet. Qt's "
        "'QDateTimePattern::QDateTimePattern(const QList<Field> &fs, int "
        "centuryStart)': takes a type Python has no way to hand over yet.")

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

  def clearBaseYear(self) -> None:
    """
    Calls Qt's 'void QDateTimePattern::clearBaseYear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimepattern.html#clearBaseYear
    """
    #  void QDateTimePattern::clearBaseYear()
    self.uglySide.call('ritual_ZN16QDateTimePattern13clearBaseYearEv')

  @staticmethod
  def baseYear(*__, **_) -> Never:
    """
    Qt's 'std::optional<int> QDateTimePattern::baseYear() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDateTimePattern.baseYear' has no cute function yet. Qt's "
        "'std::optional<int> QDateTimePattern::baseYear() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    Qt's 'QtTemporalPattern::ParseResult<QDateTime>
    QDateTimePattern::parse(QStringView text, const QDateTime &defaults)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDateTimePattern.parse' has no cute function yet. Qt's "
        "'QtTemporalPattern::ParseResult<QDateTime> "
        "QDateTimePattern::parse(QStringView text, const QDateTime "
        "&defaults) const': gives a type Python has no way to take yet.")
