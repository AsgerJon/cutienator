"""
QQmlLocaleValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmllocale_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlLocaleValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QLocale, QStringList
from . import QQmlLocale

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime
  from . import QQmlV4Function
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QQmlV4Function = WAIT['QQmlV4Function']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlLocaleValueType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlLocaleValueType: a plain Python object standing
  in front of one C++ QQmlLocaleValueType.

  C++ hands a QQmlLocaleValueType around as a copy, so every C++
  QQmlLocaleValueType behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlLocaleValueType that has a ritual and that
  Python can call so far, 29 names in all: 'currencySymbol',
  'dateTimeFormat', 'timeFormat', 'dateFormat', 'monthName',
  'standaloneMonthName', 'dayName', 'standaloneDayName', 'formattedDataSize',
  'toString', 'createSeparatedList', 'firstDayOfWeek', 'measurementSystem',
  'textDirection', 'uiLanguages', 'name', 'nativeLanguageName',
  'nativeCountryName', 'nativeTerritoryName', 'decimalPoint',
  'groupSeparator', 'percent', 'zeroDigit', 'negativeSign', 'positiveSign',
  'exponential', 'amText', 'pmText', 'numberOptions'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlLocaleValueType::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'void QQmlLocaleValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlLocaleValueType::qt_qmlMarker_extended()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlLocaleValueType::setNumberOptions(const
    QLocale::NumberOptions &numberOptions)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QQmlLocaleValueType::~QQmlLocaleValueType()': the destructor:
    Python removes its C++ QQmlLocaleValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  5 of the 46 functions Qt declares: 3 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQmlLocaleValueType is created at the first use, not by
    'QQmlLocaleValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlLocaleValueType back gives a copy the ritual made
    for Python, in a new cute QQmlLocaleValueType.
  - Each name of Qt's QQmlLocaleValueType that has no cute function yet,
    'setNumberOptions', 'weekDays', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlLocaleValueType'

  #  Qt's '~QQmlLocaleValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlLocaleValueType behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlLocaleValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QLocale.CurrencySymbolFormat)
  def currencySymbol(
      self,
      format: QLocale.CurrencySymbolFormat = (
          QLocale.CurrencySymbolFormat.CurrencySymbol),
  ) -> str:
    """
    Calls Qt's 'QString
    QQmlLocaleValueType::currencySymbol(QLocale::CurrencySymbolFormat format)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#currencySymbol

    Parameters
    ----------

    format : QLocale.CurrencySymbolFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.CurrencySymbolFormat.CurrencySymbol.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QQmlLocaleValueType::currencySymbol(QLocale::CurrencySymbolFormat
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType14currencySymbolEN7QLocale20Currenc'
        'ySymbolFormatE',
        format.value,
    )

  @overload()
  @overload(QLocale.FormatType)
  def dateTimeFormat(
      self,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString
    QQmlLocaleValueType::dateTimeFormat(QLocale::FormatType format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#dateTimeFormat

    Parameters
    ----------

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::dateTimeFormat(QLocale::FormatType
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType14dateTimeFormatEN7QLocale10FormatT'
        'ypeE',
        format.value,
    )

  @overload()
  @overload(QLocale.FormatType)
  def timeFormat(
      self,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::timeFormat(QLocale::FormatType
    format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#timeFormat

    Parameters
    ----------

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::timeFormat(QLocale::FormatType format)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType10timeFormatEN7QLocale10FormatTypeE',
        format.value,
    )

  @overload()
  @overload(QLocale.FormatType)
  def dateFormat(
      self,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::dateFormat(QLocale::FormatType
    format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#dateFormat

    Parameters
    ----------

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::dateFormat(QLocale::FormatType format)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType10dateFormatEN7QLocale10FormatTypeE',
        format.value,
    )

  @overload(int)
  @overload(int, QLocale.FormatType)
  def monthName(
      self,
      index: int,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::monthName(int index,
    QLocale::FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#monthName

    Parameters
    ----------

    index : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::monthName(int index, QLocale::FormatType
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType9monthNameEiN7QLocale10FormatTypeE',
        index, format.value,
    )

  @overload(int)
  @overload(int, QLocale.FormatType)
  def standaloneMonthName(
      self,
      index: int,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::standaloneMonthName(int index,
    QLocale::FormatType format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#standaloneMonthName

    Parameters
    ----------

    index : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::standaloneMonthName(int index,
    #      QLocale::FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType19standaloneMonthNameEiN7QLocale10F'
        'ormatTypeE',
        index, format.value,
    )

  @overload(int)
  @overload(int, QLocale.FormatType)
  def dayName(
      self,
      index: int,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::dayName(int index,
    QLocale::FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#dayName

    Parameters
    ----------

    index : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::dayName(int index, QLocale::FormatType
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType7dayNameEiN7QLocale10FormatTypeE',
        index, format.value,
    )

  @overload(int)
  @overload(int, QLocale.FormatType)
  def standaloneDayName(
      self,
      index: int,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::standaloneDayName(int index,
    QLocale::FormatType format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#standaloneDayName

    Parameters
    ----------

    index : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::standaloneDayName(int index,
    #      QLocale::FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType17standaloneDayNameEiN7QLocale10For'
        'matTypeE',
        index, format.value,
    )

  @overload()
  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::toString() const
    return self.uglySide.call('ritual_ZNK19QQmlLocaleValueType8toStringEv')

  @overload(int)
  def toString(self, i: int) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::toString(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#toString

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::toString(int i) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType8toStringEi', i,
    )

  @overload(float)
  def toString(self, f: float) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::toString(double f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#toString

    Parameters
    ----------

    f : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::toString(double f) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType8toStringEd', f,
    )

  @overload(float, str)
  @overload(float, str, int)
  def toString(self, f: float, format: str, precision: int = 6) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::toString(double f, const QString
    &format, int precision) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#toString

    Parameters
    ----------

    f : float
      Passed on as it is.

    format : str
      Passed on as it is: a QString is made of it for the call.

    precision : int
      Passed on as it is. May be left out, as in Qt: it is then 6.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::toString(double f, const QString &format,
    #      int precision) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType8toStringEdRK7QStringi',
        f, format, precision,
    )

  @overload(QDateTime, str)
  def toString(self, dateTime: QDateTime, format: str) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::toString(const QDateTime
    &dateTime, const QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#toString

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::toString(const QDateTime &dateTime, const
    #      QString &format) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType8toStringERK9QDateTimeRK7QString',
        self._valueOf(dateTime), format,
    )

  @overload(QDateTime)
  @overload(QDateTime, QLocale.FormatType)
  def toString(
      self,
      dateTime: QDateTime,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::toString(const QDateTime
    &dateTime, QLocale::FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#toString

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::toString(const QDateTime &dateTime,
    #      QLocale::FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType8toStringERK9QDateTimeN7QLocale10Fo'
        'rmatTypeE',
        self._valueOf(dateTime), format.value,
    )

  @overload(QStringList)
  def createSeparatedList(self, list: QStringList) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::createSeparatedList(const
    QStringList &list) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#createSeparatedList

    Parameters
    ----------

    list : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::createSeparatedList(const QStringList
    #      &list) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType19createSeparatedListERK5QListI7QSt'
        'ringE',
        self._valueOf(list),
    )

  def firstDayOfWeek(self) -> QQmlLocale.DayOfWeek:
    """
    Calls Qt's 'QQmlLocale::DayOfWeek QQmlLocaleValueType::firstDayOfWeek()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#firstDayOfWeek

    Returns
    -------

    QQmlLocale.DayOfWeek
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlLocale.DayOfWeek(number)' gives.
    """
    #  QQmlLocale::DayOfWeek QQmlLocaleValueType::firstDayOfWeek() const
    return QQmlLocale.DayOfWeek(self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType14firstDayOfWeekEv',
    ))

  def measurementSystem(self) -> QLocale.MeasurementSystem:
    """
    Calls Qt's 'QLocale::MeasurementSystem
    QQmlLocaleValueType::measurementSystem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#measurementSystem

    Returns
    -------

    QLocale.MeasurementSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocale.MeasurementSystem(number)' gives.
    """
    #  QLocale::MeasurementSystem QQmlLocaleValueType::measurementSystem()
    #      const
    return QLocale.MeasurementSystem(self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType17measurementSystemEv',
    ))

  def textDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQmlLocaleValueType::textDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#textDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQmlLocaleValueType::textDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType13textDirectionEv',
    ))

  def uiLanguages(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlLocaleValueType::uiLanguages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#uiLanguages

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlLocaleValueType::uiLanguages() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType11uiLanguagesEv',
    )
    return QStringList._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::name() const
    return self.uglySide.call('ritual_ZNK19QQmlLocaleValueType4nameEv')

  def nativeLanguageName(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::nativeLanguageName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#nativeLanguageName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::nativeLanguageName() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType18nativeLanguageNameEv',
    )

  def nativeCountryName(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::nativeCountryName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#nativeCountryName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::nativeCountryName() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType17nativeCountryNameEv',
    )

  def nativeTerritoryName(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::nativeTerritoryName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#nativeTerritoryName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::nativeTerritoryName() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType19nativeTerritoryNameEv',
    )

  def decimalPoint(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::decimalPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#decimalPoint

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::decimalPoint() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType12decimalPointEv',
    )

  def groupSeparator(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::groupSeparator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#groupSeparator

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::groupSeparator() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType14groupSeparatorEv',
    )

  def percent(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::percent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#percent

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::percent() const
    return self.uglySide.call('ritual_ZNK19QQmlLocaleValueType7percentEv')

  def zeroDigit(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::zeroDigit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#zeroDigit

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::zeroDigit() const
    return self.uglySide.call('ritual_ZNK19QQmlLocaleValueType9zeroDigitEv')

  def negativeSign(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::negativeSign() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#negativeSign

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::negativeSign() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType12negativeSignEv',
    )

  def positiveSign(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::positiveSign() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#positiveSign

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::positiveSign() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType12positiveSignEv',
    )

  def exponential(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::exponential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#exponential

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::exponential() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType11exponentialEv',
    )

  def amText(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::amText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#amText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::amText() const
    return self.uglySide.call('ritual_ZNK19QQmlLocaleValueType6amTextEv')

  def pmText(self) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::pmText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocalevaluetype.html#pmText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::pmText() const
    return self.uglySide.call('ritual_ZNK19QQmlLocaleValueType6pmTextEv')

  def numberOptions(self) -> QLocale.NumberOptions:
    """
    Calls Qt's 'QLocale::NumberOptions QQmlLocaleValueType::numberOptions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#numberOptions

    Returns
    -------

    QLocale.NumberOptions
      The value standing for the combination Qt gave back.
    """
    #  QLocale::NumberOptions QQmlLocaleValueType::numberOptions() const
    return QLocale.NumberOptions(self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType13numberOptionsEv',
    ))

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

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's
    'QQmlLocaleValueType::QQmlLocaleValueType(const QString &name)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#QQmlLocaleValueType

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlLocaleValueType::QQmlLocaleValueType(const QString &name)
    self._noteCreation(QQmlLocaleValueType, lambda: Rituals.call(
        'ritual_ZN19QQmlLocaleValueTypeC1ERK7QString', name,
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

  @overload(QQmlV4Function)
  @overload(NoneType)
  def formattedDataSize(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlLocaleValueType::formattedDataSize(QQmlV4FunctionPtr
    args) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#formattedDataSize

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlLocaleValueType::formattedDataSize(QQmlV4FunctionPtr args)
    #      const
    self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType17formattedDataSizeEP14QQmlV4Functi'
        'on',
        self._addressOf(args),
    )

  @overload(float)
  @overload(float, int)
  @overload(float, int, QLocale.DataSizeFormats)
  def formattedDataSize(
      self,
      bytes: float,
      precision: int = 2,
      format: QLocale.DataSizeFormats = (
          QLocale.DataSizeFormats.DataSizeIecFormat),
  ) -> str:
    """
    Calls Qt's 'QString QQmlLocaleValueType::formattedDataSize(double bytes,
    int precision, QLocale::DataSizeFormats format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocalevaluetype.html#formattedDataSize

    Parameters
    ----------

    bytes : float
      Passed on as it is.

    precision : int
      Passed on as it is. May be left out, as in Qt: it is then 2.

    format : QLocale.DataSizeFormats
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.DataSizeFormats.DataSizeIecFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLocaleValueType::formattedDataSize(double bytes, int
    #      precision, QLocale::DataSizeFormats format) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlLocaleValueType17formattedDataSizeEdi6QFlagsIN7QLo'
        'cale14DataSizeFormatEE',
        bytes, precision, format.value,
    )

  @staticmethod
  def setNumberOptions(*__, **_) -> Never:
    """
    Qt's 'void QQmlLocaleValueType::setNumberOptions(const
    QLocale::NumberOptions &numberOptions)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlLocaleValueType.setNumberOptions' has no cute function yet. "
        "Qt's 'void QQmlLocaleValueType::setNumberOptions(const "
        "QLocale::NumberOptions &numberOptions)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def weekDays(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlLocale::DayOfWeek> QQmlLocaleValueType::weekDays()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'qtDayToQmlDay'.
    """
    raise NotImplementedError(
        "'QQmlLocaleValueType.weekDays' has no cute function yet. Qt's "
        "'QList<QQmlLocale::DayOfWeek> QQmlLocaleValueType::weekDays() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'qtDayToQmlDay'.")
