"""
QLocale binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QLocaleCountry, QLocaleCurrencySymbolFormat
from . import QLocaleDataSizeFormat, QLocaleFloatingPointPrecisionOption
from . import QLocaleFormatType, QLocaleLanguage, QLocaleLanguageCodeType
from . import QLocaleMeasurementSystem, QLocaleNumberOption
from . import QLocaleQuotationStyle, QLocaleScript, QLocaleTagSeparator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QCalendar, QDate, QDateTime, QTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCalendar = WAIT['QCalendar']
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
  QTime = WAIT['QTime']


class QLocale(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLocale: a plain Python object standing in front of
  one C++ QLocale.

  C++ hands a QLocale around as a copy, so every C++ QLocale behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLocale that has a ritual and that Python can call
  so far, 54 names in all: 'language', 'script', 'country', 'name',
  'bcp47Name', 'nativeLanguageName', 'nativeTerritoryName',
  'nativeCountryName', 'toString', 'dateFormat', 'timeFormat',
  'dateTimeFormat', 'toTime', 'toDate', 'toDateTime', 'decimalPoint',
  'groupSeparator', 'percent', 'zeroDigit', 'negativeSign', 'positiveSign',
  'exponential', 'monthName', 'standaloneMonthName', 'dayName',
  'standaloneDayName', 'firstDayOfWeek', 'amText', 'pmText',
  'measurementSystem', 'collation', 'textDirection', 'toUpper', 'toLower',
  'currencySymbol', 'toCurrencyString', 'formattedDataSize',
  'languageToCode', 'codeToLanguage', 'territoryToCode', 'countryToCode',
  'codeToCountry', 'scriptToCode', 'codeToScript', 'languageToString',
  'territoryToString', 'countryToString', 'scriptToString', 'setDefault',
  'c', 'system', 'setNumberOptions', 'numberOptions', 'quoteString'. It can
  be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLocale::QLocale(QStringView name)': takes in Python what
    'QLocale::QLocale(const QString &name)' takes.
  - Qt's 'QLocale::~QLocale()': the destructor: Python removes its C++
    QLocale by it, and has no other use for it.
  - Qt's 'short QLocale::toShort(const QString &s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'ushort QLocale::toUShort(const QString &s, bool *ok) const': takes
    a number to change where it is.
  - Qt's 'int QLocale::toInt(const QString &s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'uint QLocale::toUInt(const QString &s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'long QLocale::toLong(const QString &s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'ulong QLocale::toULong(const QString &s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'qlonglong QLocale::toLongLong(const QString &s, bool *ok) const':
    takes a number to change where it is.
  - Qt's 'qulonglong QLocale::toULongLong(const QString &s, bool *ok) const':
    takes a number to change where it is.
  - Qt's 'float QLocale::toFloat(const QString &s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'double QLocale::toDouble(const QString &s, bool *ok) const': takes
    a number to change where it is.
  - Qt's 'short QLocale::toShort(QStringView s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'ushort QLocale::toUShort(QStringView s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'int QLocale::toInt(QStringView s, bool *ok) const': takes a number
    to change where it is.
  - Qt's 'uint QLocale::toUInt(QStringView s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'long QLocale::toLong(QStringView s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'ulong QLocale::toULong(QStringView s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'qlonglong QLocale::toLongLong(QStringView s, bool *ok) const':
    takes a number to change where it is.
  - Qt's 'qulonglong QLocale::toULongLong(QStringView s, bool *ok) const':
    takes a number to change where it is.
  - Qt's 'float QLocale::toFloat(QStringView s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'double QLocale::toDouble(QStringView s, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'QString QLocale::toString(qulonglong i) const': takes in Python
    what 'QString QLocale::toString(qlonglong i) const' takes.
  - Qt's 'QString QLocale::toString(long i) const': takes in Python what
    'QString QLocale::toString(qlonglong i) const' takes.
  - Qt's 'QString QLocale::toString(ulong i) const': takes in Python what
    'QString QLocale::toString(qlonglong i) const' takes.
  - Qt's 'QString QLocale::toString(short i) const': takes in Python what
    'QString QLocale::toString(qlonglong i) const' takes.
  - Qt's 'QString QLocale::toString(ushort i) const': takes in Python what
    'QString QLocale::toString(qlonglong i) const' takes.
  - Qt's 'QString QLocale::toString(int i) const': takes in Python what
    'QString QLocale::toString(qlonglong i) const' takes.
  - Qt's 'QString QLocale::toString(uint i) const': takes in Python what
    'QString QLocale::toString(qlonglong i) const' takes.
  - Qt's 'QString QLocale::toString(double f, char format, int precision)
    const': takes a single letter as C has it.
  - Qt's 'QString QLocale::toString(float f, char format, int precision)
    const': takes a single letter as C has it.
  - Qt's 'QString QLocale::toString(QDate date, QStringView format) const':
    takes in Python what 'QString QLocale::toString(QDate date, const QString
    &format) const' takes.
  - Qt's 'QString QLocale::toString(QTime time, QStringView format) const':
    takes in Python what 'QString QLocale::toString(QTime time, const QString
    &format) const' takes.
  - Qt's 'QString QLocale::toString(const QDateTime &dateTime, QStringView
    format) const': takes in Python what 'QString QLocale::toString(const
    QDateTime &dateTime, const QString &format) const' takes.
  - Qt's 'QString QLocale::toCurrencyString(qulonglong a0, const QString
    &symbol) const': takes in Python what 'QString
    QLocale::toCurrencyString(qlonglong a0, const QString &symbol) const'
    takes.
  - Qt's 'QString QLocale::toCurrencyString(short i, const QString &symbol)
    const': takes in Python what 'QString QLocale::toCurrencyString(qlonglong
    a0, const QString &symbol) const' takes.
  - Qt's 'QString QLocale::toCurrencyString(ushort i, const QString &symbol)
    const': takes in Python what 'QString QLocale::toCurrencyString(qlonglong
    a0, const QString &symbol) const' takes.
  - Qt's 'QString QLocale::toCurrencyString(int i, const QString &symbol)
    const': takes in Python what 'QString QLocale::toCurrencyString(qlonglong
    a0, const QString &symbol) const' takes.
  - Qt's 'QString QLocale::toCurrencyString(uint i, const QString &symbol)
    const': takes in Python what 'QString QLocale::toCurrencyString(qlonglong
    a0, const QString &symbol) const' takes.
  - Qt's 'QString QLocale::toCurrencyString(float i, const QString &symbol,
    int precision) const': takes in Python what 'QString
    QLocale::toCurrencyString(double a0, const QString &symbol, int
    precision) const' takes.
  - Qt's 'QString QLocale::quoteString(QStringView str, QuotationStyle style)
    const': takes in Python what 'QString QLocale::quoteString(const QString
    &str, QuotationStyle style) const' takes.

  What has no ritual
  ------------------

  23 of the 141 functions Qt declares: 18 takes or gives a type that cannot
  be passed yet; 3 private; 1 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QLocale is created at the first use, not by 'QLocale(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLocale back gives a copy the ritual made for Python,
    in a new cute QLocale.
  """

  #  The enums Qt writes inside QLocale, and the names Qt has for the
  #  combinations of its flags enums.
  Country = QLocaleCountry
  CurrencySymbolFormat = QLocaleCurrencySymbolFormat
  DataSizeFormat = QLocaleDataSizeFormat
  DataSizeFormats = QLocaleDataSizeFormat
  FloatingPointPrecisionOption = QLocaleFloatingPointPrecisionOption
  FormatType = QLocaleFormatType
  Language = QLocaleLanguage
  LanguageCodeType = QLocaleLanguageCodeType
  LanguageCodeTypes = QLocaleLanguageCodeType
  MeasurementSystem = QLocaleMeasurementSystem
  NumberOption = QLocaleNumberOption
  NumberOptions = QLocaleNumberOption
  QuotationStyle = QLocaleQuotationStyle
  Script = QLocaleScript
  TagSeparator = QLocaleTagSeparator

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Language)
  @overload(Language, LanguageCodeTypes)
  def languageToCode(
      language: Language,
      codeTypes: LanguageCodeTypes = LanguageCodeTypes.AnyLanguageCode,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::languageToCode(Language language,
    LanguageCodeTypes codeTypes)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#languageToCode

    Parameters
    ----------

    language : Language
      Passed on as its number.

    codeTypes : LanguageCodeTypes
      Passed on as its number. May be left out, as in Qt: it is then
      LanguageCodeTypes.AnyLanguageCode.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::languageToCode(Language language, LanguageCodeTypes
    #      codeTypes)
    return Rituals.call(
        'ritual_ZN7QLocale14languageToCodeENS_8LanguageE6QFlagsINS_16Langua'
        'geCodeTypeEE',
        language.value, codeTypes.value,
    )

  @staticmethod
  @overload(str)
  @overload(str, LanguageCodeTypes)
  def codeToLanguage(
      languageCode: str,
      codeTypes: LanguageCodeTypes = LanguageCodeTypes.AnyLanguageCode,
  ) -> Language:
    """
    Calls Qt's 'Language QLocale::codeToLanguage(QStringView languageCode,
    LanguageCodeTypes codeTypes)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#codeToLanguage

    Parameters
    ----------

    languageCode : str
      Passed on as it is: a QString is made of it for the call.

    codeTypes : LanguageCodeTypes
      Passed on as its number. May be left out, as in Qt: it is then
      LanguageCodeTypes.AnyLanguageCode.

    Returns
    -------

    Language
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Language(number)' gives.
    """
    #  Language QLocale::codeToLanguage(QStringView languageCode,
    #      LanguageCodeTypes codeTypes)
    return QLocale.Language(Rituals.call(
        'ritual_ZN7QLocale14codeToLanguageE11QStringView6QFlagsINS_16Langua'
        'geCodeTypeEE',
        languageCode, codeTypes.value,
    ))

  @staticmethod
  @overload(Country)
  def territoryToCode(territory: Country) -> str:
    """
    Calls Qt's 'QString QLocale::territoryToCode(Territory territory)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#territoryToCode

    Parameters
    ----------

    territory : Country
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::territoryToCode(Territory territory)
    return Rituals.call(
        'ritual_ZN7QLocale15territoryToCodeENS_7CountryE', territory.value,
    )

  @staticmethod
  @overload(Country)
  def countryToCode(country: Country) -> str:
    """
    Calls Qt's 'QString QLocale::countryToCode(Country country)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#countryToCode

    Parameters
    ----------

    country : Country
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::countryToCode(Country country)
    return Rituals.call(
        'ritual_ZN7QLocale13countryToCodeENS_7CountryE', country.value,
    )

  @staticmethod
  @overload(str)
  def codeToCountry(countryCode: str) -> Country:
    """
    Calls Qt's 'Country QLocale::codeToCountry(QStringView countryCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#codeToCountry

    Parameters
    ----------

    countryCode : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Country
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Country(number)' gives.
    """
    #  Country QLocale::codeToCountry(QStringView countryCode)
    return QLocale.Country(Rituals.call(
        'ritual_ZN7QLocale13codeToCountryE11QStringView', countryCode,
    ))

  @staticmethod
  @overload(Script)
  def scriptToCode(script: Script) -> str:
    """
    Calls Qt's 'QString QLocale::scriptToCode(Script script)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#scriptToCode

    Parameters
    ----------

    script : Script
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::scriptToCode(Script script)
    return Rituals.call(
        'ritual_ZN7QLocale12scriptToCodeENS_6ScriptE', script.value,
    )

  @staticmethod
  @overload(str)
  def codeToScript(scriptCode: str) -> Script:
    """
    Calls Qt's 'Script QLocale::codeToScript(QStringView scriptCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#codeToScript

    Parameters
    ----------

    scriptCode : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Script
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Script(number)' gives.
    """
    #  Script QLocale::codeToScript(QStringView scriptCode)
    return QLocale.Script(Rituals.call(
        'ritual_ZN7QLocale12codeToScriptE11QStringView', scriptCode,
    ))

  @staticmethod
  @overload(Language)
  def languageToString(language: Language) -> str:
    """
    Calls Qt's 'QString QLocale::languageToString(Language language)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#languageToString

    Parameters
    ----------

    language : Language
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::languageToString(Language language)
    return Rituals.call(
        'ritual_ZN7QLocale16languageToStringENS_8LanguageE', language.value,
    )

  @staticmethod
  @overload(Country)
  def territoryToString(territory: Country) -> str:
    """
    Calls Qt's 'QString QLocale::territoryToString(Territory territory)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#territoryToString

    Parameters
    ----------

    territory : Country
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::territoryToString(Territory territory)
    return Rituals.call(
        'ritual_ZN7QLocale17territoryToStringENS_7CountryE', territory.value,
    )

  @staticmethod
  @overload(Country)
  def countryToString(country: Country) -> str:
    """
    Calls Qt's 'QString QLocale::countryToString(Country country)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#countryToString

    Parameters
    ----------

    country : Country
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::countryToString(Country country)
    return Rituals.call(
        'ritual_ZN7QLocale15countryToStringENS_7CountryE', country.value,
    )

  @staticmethod
  @overload(Script)
  def scriptToString(script: Script) -> str:
    """
    Calls Qt's 'QString QLocale::scriptToString(Script script)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#scriptToString

    Parameters
    ----------

    script : Script
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::scriptToString(Script script)
    return Rituals.call(
        'ritual_ZN7QLocale14scriptToStringENS_6ScriptE', script.value,
    )

  @staticmethod
  @overload(THIS)
  def setDefault(locale: QLocale) -> None:
    """
    Calls Qt's 'void QLocale::setDefault(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#setDefault

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QLocale::setDefault(const QLocale &locale)
    Rituals.call(
        'ritual_ZN7QLocale10setDefaultERKS_', CuteMixin._valueOf(locale),
    )

  @staticmethod
  def c() -> QLocale:
    """
    Calls Qt's 'QLocale QLocale::c()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#c

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QLocale::c()
    address = Rituals.call('ritual_ZN7QLocale1cEv')
    return QLocale._cuteOwning(address)

  @staticmethod
  def system() -> QLocale:
    """
    Calls Qt's 'QLocale QLocale::system()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#system

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QLocale::system()
    address = Rituals.call('ritual_ZN7QLocale6systemEv')
    return QLocale._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocale'

  #  Qt's '~QLocale()'. Naming it makes this a value class: Python owns every
  #  C++ QLocale behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QLocaleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def language(self) -> Language:
    """
    Calls Qt's 'Language QLocale::language() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#language

    Returns
    -------

    Language
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Language(number)' gives.
    """
    #  Language QLocale::language() const
    return QLocale.Language(self.uglySide.call(
        'ritual_ZNK7QLocale8languageEv',
    ))

  def script(self) -> Script:
    """
    Calls Qt's 'Script QLocale::script() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#script

    Returns
    -------

    Script
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Script(number)' gives.
    """
    #  Script QLocale::script() const
    return QLocale.Script(self.uglySide.call('ritual_ZNK7QLocale6scriptEv'))

  def country(self) -> Country:
    """
    Calls Qt's 'Country QLocale::country() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#country

    Returns
    -------

    Country
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Country(number)' gives.
    """
    #  Country QLocale::country() const
    return QLocale.Country(self.uglySide.call(
        'ritual_ZNK7QLocale7countryEv',
    ))

  @overload()
  @overload(TagSeparator)
  def name(self, separator: TagSeparator = TagSeparator.Underscore) -> str:
    """
    Calls Qt's 'QString QLocale::name(TagSeparator separator) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#name

    Parameters
    ----------

    separator : TagSeparator
      Passed on as its number. May be left out, as in Qt: it is then
      TagSeparator.Underscore.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::name(TagSeparator separator) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale4nameENS_12TagSeparatorE', separator.value,
    )

  @overload()
  @overload(TagSeparator)
  def bcp47Name(self, separator: TagSeparator = TagSeparator.Dash) -> str:
    """
    Calls Qt's 'QString QLocale::bcp47Name(TagSeparator separator) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#bcp47Name

    Parameters
    ----------

    separator : TagSeparator
      Passed on as its number. May be left out, as in Qt: it is then
      TagSeparator.Dash.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::bcp47Name(TagSeparator separator) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale9bcp47NameENS_12TagSeparatorE', separator.value,
    )

  def nativeLanguageName(self) -> str:
    """
    Calls Qt's 'QString QLocale::nativeLanguageName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#nativeLanguageName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::nativeLanguageName() const
    return self.uglySide.call('ritual_ZNK7QLocale18nativeLanguageNameEv')

  def nativeTerritoryName(self) -> str:
    """
    Calls Qt's 'QString QLocale::nativeTerritoryName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#nativeTerritoryName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::nativeTerritoryName() const
    return self.uglySide.call('ritual_ZNK7QLocale19nativeTerritoryNameEv')

  def nativeCountryName(self) -> str:
    """
    Calls Qt's 'QString QLocale::nativeCountryName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#nativeCountryName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::nativeCountryName() const
    return self.uglySide.call('ritual_ZNK7QLocale17nativeCountryNameEv')

  @overload(int)
  def toString(self, i: int) -> str:
    """
    Calls Qt's 'QString QLocale::toString(qlonglong i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(qlonglong i) const
    return self.uglySide.call('ritual_ZNK7QLocale8toStringEx', i)

  @overload(QDate, str)
  def toString(self, date: QDate, format: str) -> str:
    """
    Calls Qt's 'QString QLocale::toString(QDate date, const QString &format)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(QDate date, const QString &format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringE5QDateRK7QString',
        self._valueOf(date), format,
    )

  @overload(QTime, str)
  def toString(self, time: QTime, format: str) -> str:
    """
    Calls Qt's 'QString QLocale::toString(QTime time, const QString &format)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(QTime time, const QString &format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringE5QTimeRK7QString',
        self._valueOf(time), format,
    )

  @overload(QDateTime, str)
  def toString(self, dateTime: QDateTime, format: str) -> str:
    """
    Calls Qt's 'QString QLocale::toString(const QDateTime &dateTime, const
    QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

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
    #  QString QLocale::toString(const QDateTime &dateTime, const QString
    #      &format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringERK9QDateTimeRK7QString',
        self._valueOf(dateTime), format,
    )

  @overload(QDate)
  @overload(QDate, FormatType)
  def toString(
      self,
      date: QDate,
      format: FormatType = FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::toString(QDate date, FormatType format)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(QDate date, FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringE5QDateNS_10FormatTypeE',
        self._valueOf(date), format.value,
    )

  @overload(QTime)
  @overload(QTime, FormatType)
  def toString(
      self,
      time: QTime,
      format: FormatType = FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::toString(QTime time, FormatType format)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(QTime time, FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringE5QTimeNS_10FormatTypeE',
        self._valueOf(time), format.value,
    )

  @overload(QDateTime)
  @overload(QDateTime, FormatType)
  def toString(
      self,
      dateTime: QDateTime,
      format: FormatType = FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::toString(const QDateTime &dateTime,
    FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(const QDateTime &dateTime, FormatType
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringERK9QDateTimeNS_10FormatTypeE',
        self._valueOf(dateTime), format.value,
    )

  @overload(QDate, str, QCalendar)
  def toString(self, date: QDate, format: str, cal: QCalendar) -> str:
    """
    Calls Qt's 'QString QLocale::toString(QDate date, QStringView format,
    QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(QDate date, QStringView format, QCalendar
    #      cal) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringE5QDate11QStringView9QCalendar',
        self._valueOf(date), format, self._valueOf(cal),
    )

  @overload(QDate, FormatType, QCalendar)
  def toString(self, date: QDate, format: FormatType, cal: QCalendar) -> str:
    """
    Calls Qt's 'QString QLocale::toString(QDate date, FormatType format,
    QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    format : FormatType
      Passed on as its number.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(QDate date, FormatType format, QCalendar
    #      cal) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringE5QDateNS_10FormatTypeE9QCalendar',
        self._valueOf(date), format.value, self._valueOf(cal),
    )

  @overload(QDateTime, FormatType, QCalendar)
  def toString(
      self,
      dateTime: QDateTime,
      format: FormatType,
      cal: QCalendar,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::toString(const QDateTime &dateTime,
    FormatType format, QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : FormatType
      Passed on as its number.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(const QDateTime &dateTime, FormatType
    #      format, QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringERK9QDateTimeNS_10FormatTypeE9QCalendar',
        self._valueOf(dateTime), format.value, self._valueOf(cal),
    )

  @overload(QDateTime, str, QCalendar)
  def toString(
      self,
      dateTime: QDateTime,
      format: str,
      cal: QCalendar,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::toString(const QDateTime &dateTime,
    QStringView format, QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toString

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toString(const QDateTime &dateTime, QStringView
    #      format, QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale8toStringERK9QDateTime11QStringView9QCalendar',
        self._valueOf(dateTime), format, self._valueOf(cal),
    )

  @overload()
  @overload(FormatType)
  def dateFormat(self, format: FormatType = FormatType.LongFormat) -> str:
    """
    Calls Qt's 'QString QLocale::dateFormat(FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#dateFormat

    Parameters
    ----------

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::dateFormat(FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale10dateFormatENS_10FormatTypeE', format.value,
    )

  @overload()
  @overload(FormatType)
  def timeFormat(self, format: FormatType = FormatType.LongFormat) -> str:
    """
    Calls Qt's 'QString QLocale::timeFormat(FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#timeFormat

    Parameters
    ----------

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::timeFormat(FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale10timeFormatENS_10FormatTypeE', format.value,
    )

  @overload()
  @overload(FormatType)
  def dateTimeFormat(
      self,
      format: FormatType = FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::dateTimeFormat(FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#dateTimeFormat

    Parameters
    ----------

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::dateTimeFormat(FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale14dateTimeFormatENS_10FormatTypeE', format.value,
    )

  @overload(str)
  @overload(str, FormatType)
  def toTime(
      self,
      string: str,
      a1: FormatType = FormatType.LongFormat,
  ) -> QTime:
    """
    Calls Qt's 'QTime QLocale::toTime(const QString &string, FormatType a1)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toTime

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    a1 : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QLocale::toTime(const QString &string, FormatType a1) const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale6toTimeERK7QStringNS_10FormatTypeE',
        string, a1.value,
    )
    from . import QTime
    return QTime._cuteOwning(address)

  @overload(str, str)
  def toTime(self, string: str, format: str) -> QTime:
    """
    Calls Qt's 'QTime QLocale::toTime(const QString &string, const QString
    &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toTime

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
    #  QTime QLocale::toTime(const QString &string, const QString &format)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale6toTimeERK7QStringS2_', string, format,
    )
    from . import QTime
    return QTime._cuteOwning(address)

  @overload(str, FormatType, int)
  def toDate(self, string: str, a1: FormatType, baseYear: int) -> QDate:
    """
    Calls Qt's 'QDate QLocale::toDate(const QString &string, FormatType a1,
    int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toDate

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    a1 : FormatType
      Passed on as its number.

    baseYear : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QLocale::toDate(const QString &string, FormatType a1, int
    #      baseYear) const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale6toDateERK7QStringNS_10FormatTypeEi',
        string, a1.value, baseYear,
    )
    from . import QDate
    return QDate._cuteOwning(address)

  @overload(str, str, int)
  def toDate(self, string: str, format: str, baseYear: int) -> QDate:
    """
    Calls Qt's 'QDate QLocale::toDate(const QString &string, const QString
    &format, int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toDate

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    baseYear : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QLocale::toDate(const QString &string, const QString &format,
    #      int baseYear) const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale6toDateERK7QStringS2_i', string, format, baseYear,
    )
    from . import QDate
    return QDate._cuteOwning(address)

  @overload(str, FormatType, QCalendar, int)
  def toDate(
      self,
      string: str,
      format: FormatType,
      cal: QCalendar,
      baseYear: int,
  ) -> QDate:
    """
    Calls Qt's 'QDate QLocale::toDate(const QString &string, FormatType
    format, QCalendar cal, int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toDate

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : FormatType
      Passed on as its number.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    baseYear : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QLocale::toDate(const QString &string, FormatType format,
    #      QCalendar cal, int baseYear) const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale6toDateERK7QStringNS_10FormatTypeE9QCalendari',
        string, format.value, self._valueOf(cal), baseYear,
    )
    from . import QDate
    return QDate._cuteOwning(address)

  @overload(str, str, QCalendar, int)
  def toDate(
      self,
      string: str,
      format: str,
      cal: QCalendar,
      baseYear: int,
  ) -> QDate:
    """
    Calls Qt's 'QDate QLocale::toDate(const QString &string, const QString
    &format, QCalendar cal, int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toDate

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    baseYear : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QLocale::toDate(const QString &string, const QString &format,
    #      QCalendar cal, int baseYear) const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale6toDateERK7QStringS2_9QCalendari',
        string, format, self._valueOf(cal), baseYear,
    )
    from . import QDate
    return QDate._cuteOwning(address)

  @overload(str, FormatType, int)
  def toDateTime(
      self,
      string: str,
      format: FormatType,
      baseYear: int,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QLocale::toDateTime(const QString &string,
    FormatType format, int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toDateTime

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : FormatType
      Passed on as its number.

    baseYear : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QLocale::toDateTime(const QString &string, FormatType
    #      format, int baseYear) const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale10toDateTimeERK7QStringNS_10FormatTypeEi',
        string, format.value, baseYear,
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(str, str, int)
  def toDateTime(self, string: str, format: str, baseYear: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QLocale::toDateTime(const QString &string, const
    QString &format, int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toDateTime

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    baseYear : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QLocale::toDateTime(const QString &string, const QString
    #      &format, int baseYear) const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale10toDateTimeERK7QStringS2_i',
        string, format, baseYear,
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(str, FormatType, QCalendar, int)
  def toDateTime(
      self,
      string: str,
      format: FormatType,
      cal: QCalendar,
      baseYear: int,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QLocale::toDateTime(const QString &string,
    FormatType format, QCalendar cal, int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toDateTime

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : FormatType
      Passed on as its number.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    baseYear : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QLocale::toDateTime(const QString &string, FormatType
    #      format, QCalendar cal, int baseYear) const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale10toDateTimeERK7QStringNS_10FormatTypeE9QCalenda'
        'ri',
        string, format.value, self._valueOf(cal), baseYear,
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(str, str, QCalendar, int)
  def toDateTime(
      self,
      string: str,
      format: str,
      cal: QCalendar,
      baseYear: int,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QLocale::toDateTime(const QString &string, const
    QString &format, QCalendar cal, int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toDateTime

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    baseYear : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QLocale::toDateTime(const QString &string, const QString
    #      &format, QCalendar cal, int baseYear) const
    address = self.uglySide.call(
        'ritual_ZNK7QLocale10toDateTimeERK7QStringS2_9QCalendari',
        string, format, self._valueOf(cal), baseYear,
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  def decimalPoint(self) -> str:
    """
    Calls Qt's 'QString QLocale::decimalPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#decimalPoint

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::decimalPoint() const
    return self.uglySide.call('ritual_ZNK7QLocale12decimalPointEv')

  def groupSeparator(self) -> str:
    """
    Calls Qt's 'QString QLocale::groupSeparator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#groupSeparator

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::groupSeparator() const
    return self.uglySide.call('ritual_ZNK7QLocale14groupSeparatorEv')

  def percent(self) -> str:
    """
    Calls Qt's 'QString QLocale::percent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#percent

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::percent() const
    return self.uglySide.call('ritual_ZNK7QLocale7percentEv')

  def zeroDigit(self) -> str:
    """
    Calls Qt's 'QString QLocale::zeroDigit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#zeroDigit

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::zeroDigit() const
    return self.uglySide.call('ritual_ZNK7QLocale9zeroDigitEv')

  def negativeSign(self) -> str:
    """
    Calls Qt's 'QString QLocale::negativeSign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#negativeSign

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::negativeSign() const
    return self.uglySide.call('ritual_ZNK7QLocale12negativeSignEv')

  def positiveSign(self) -> str:
    """
    Calls Qt's 'QString QLocale::positiveSign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#positiveSign

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::positiveSign() const
    return self.uglySide.call('ritual_ZNK7QLocale12positiveSignEv')

  def exponential(self) -> str:
    """
    Calls Qt's 'QString QLocale::exponential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#exponential

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::exponential() const
    return self.uglySide.call('ritual_ZNK7QLocale11exponentialEv')

  @overload(int)
  @overload(int, FormatType)
  def monthName(
      self,
      a0: int,
      format: FormatType = FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::monthName(int a0, FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#monthName

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::monthName(int a0, FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale9monthNameEiNS_10FormatTypeE', a0, format.value,
    )

  @overload(int)
  @overload(int, FormatType)
  def standaloneMonthName(
      self,
      a0: int,
      format: FormatType = FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::standaloneMonthName(int a0, FormatType
    format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#standaloneMonthName

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::standaloneMonthName(int a0, FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale19standaloneMonthNameEiNS_10FormatTypeE',
        a0, format.value,
    )

  @overload(int)
  @overload(int, FormatType)
  def dayName(
      self,
      a0: int,
      format: FormatType = FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::dayName(int a0, FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#dayName

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::dayName(int a0, FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale7dayNameEiNS_10FormatTypeE', a0, format.value,
    )

  @overload(int)
  @overload(int, FormatType)
  def standaloneDayName(
      self,
      a0: int,
      format: FormatType = FormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::standaloneDayName(int a0, FormatType format)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#standaloneDayName

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    format : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::standaloneDayName(int a0, FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale17standaloneDayNameEiNS_10FormatTypeE',
        a0, format.value,
    )

  def firstDayOfWeek(self) -> Qt.DayOfWeek:
    """
    Calls Qt's 'Qt::DayOfWeek QLocale::firstDayOfWeek() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#firstDayOfWeek

    Returns
    -------

    Qt.DayOfWeek
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DayOfWeek(number)'
      gives.
    """
    #  Qt::DayOfWeek QLocale::firstDayOfWeek() const
    return Qt.DayOfWeek(self.uglySide.call(
        'ritual_ZNK7QLocale14firstDayOfWeekEv',
    ))

  def amText(self) -> str:
    """
    Calls Qt's 'QString QLocale::amText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#amText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::amText() const
    return self.uglySide.call('ritual_ZNK7QLocale6amTextEv')

  def pmText(self) -> str:
    """
    Calls Qt's 'QString QLocale::pmText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#pmText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::pmText() const
    return self.uglySide.call('ritual_ZNK7QLocale6pmTextEv')

  def measurementSystem(self) -> MeasurementSystem:
    """
    Calls Qt's 'MeasurementSystem QLocale::measurementSystem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#measurementSystem

    Returns
    -------

    MeasurementSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'MeasurementSystem(number)' gives.
    """
    #  MeasurementSystem QLocale::measurementSystem() const
    return QLocale.MeasurementSystem(self.uglySide.call(
        'ritual_ZNK7QLocale17measurementSystemEv',
    ))

  def collation(self) -> QLocale:
    """
    Calls Qt's 'QLocale QLocale::collation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#collation

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QLocale::collation() const
    address = self.uglySide.call('ritual_ZNK7QLocale9collationEv')
    return QLocale._cuteOwning(address)

  def textDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QLocale::textDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#textDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QLocale::textDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK7QLocale13textDirectionEv',
    ))

  @overload(str)
  def toUpper(self, str: str) -> str:
    """
    Calls Qt's 'QString QLocale::toUpper(const QString &str) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toUpper

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toUpper(const QString &str) const
    return self.uglySide.call('ritual_ZNK7QLocale7toUpperERK7QString', str)

  @overload(str)
  def toLower(self, str: str) -> str:
    """
    Calls Qt's 'QString QLocale::toLower(const QString &str) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toLower

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toLower(const QString &str) const
    return self.uglySide.call('ritual_ZNK7QLocale7toLowerERK7QString', str)

  @overload()
  @overload(CurrencySymbolFormat)
  def currencySymbol(
      self,
      a0: CurrencySymbolFormat = CurrencySymbolFormat.CurrencySymbol,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::currencySymbol(CurrencySymbolFormat a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#currencySymbol

    Parameters
    ----------

    a0 : CurrencySymbolFormat
      Passed on as its number. May be left out, as in Qt: it is then
      CurrencySymbolFormat.CurrencySymbol.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::currencySymbol(CurrencySymbolFormat a0) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale14currencySymbolENS_20CurrencySymbolFormatE',
        a0.value,
    )

  @overload(int)
  @overload(int, str)
  def toCurrencyString(self, a0: int, symbol: str = '') -> str:
    """
    Calls Qt's 'QString QLocale::toCurrencyString(qlonglong a0, const QString
    &symbol) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toCurrencyString

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    symbol : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toCurrencyString(qlonglong a0, const QString &symbol)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QLocale16toCurrencyStringExRK7QString', a0, symbol,
    )

  @overload(float)
  @overload(float, str)
  @overload(float, str, int)
  def toCurrencyString(
      self,
      a0: float,
      symbol: str = '',
      precision: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::toCurrencyString(double a0, const QString
    &symbol, int precision) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toCurrencyString

    Parameters
    ----------

    a0 : float
      Passed on as it is.

    symbol : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    precision : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::toCurrencyString(double a0, const QString &symbol,
    #      int precision) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale16toCurrencyStringEdRK7QStringi',
        a0, symbol, precision,
    )

  @overload(int)
  @overload(int, int)
  @overload(int, int, DataSizeFormats)
  def formattedDataSize(
      self,
      bytes: int,
      precision: int = 2,
      format: DataSizeFormats = DataSizeFormats.DataSizeIecFormat,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::formattedDataSize(qint64 bytes, int
    precision, DataSizeFormats format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#formattedDataSize

    Parameters
    ----------

    bytes : int
      Passed on as it is.

    precision : int
      Passed on as it is. May be left out, as in Qt: it is then 2.

    format : DataSizeFormats
      Passed on as its number. May be left out, as in Qt: it is then
      DataSizeFormats.DataSizeIecFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::formattedDataSize(qint64 bytes, int precision,
    #      DataSizeFormats format) const
    return self.uglySide.call(
        'ritual_ZNK7QLocale17formattedDataSizeExi6QFlagsINS_14DataSizeForma'
        'tEE',
        bytes, precision, format.value,
    )

  def numberOptions(self) -> NumberOptions:
    """
    Calls Qt's 'NumberOptions QLocale::numberOptions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#numberOptions

    Returns
    -------

    NumberOptions
      The value standing for the combination Qt gave back.
    """
    #  NumberOptions QLocale::numberOptions() const
    return QLocale.NumberOptions(self.uglySide.call(
        'ritual_ZNK7QLocale13numberOptionsEv',
    ))

  @overload(str)
  @overload(str, QuotationStyle)
  def quoteString(
      self,
      str: str,
      style: QuotationStyle = QuotationStyle.StandardQuotation,
  ) -> str:
    """
    Calls Qt's 'QString QLocale::quoteString(const QString &str,
    QuotationStyle style) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#quoteString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    style : QuotationStyle
      Passed on as its number. May be left out, as in Qt: it is then
      QuotationStyle.StandardQuotation.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocale::quoteString(const QString &str, QuotationStyle style)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QLocale11quoteStringERK7QStringNS_14QuotationStyleE',
        str, style.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(NumberOptions)
  def setNumberOptions(self, options: NumberOptions) -> None:
    """
    Calls Qt's 'void QLocale::setNumberOptions(NumberOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#setNumberOptions

    Parameters
    ----------

    options : NumberOptions
      Passed on as its number.
    """
    #  void QLocale::setNumberOptions(NumberOptions options)
    self.uglySide.call(
        'ritual_ZN7QLocale16setNumberOptionsE6QFlagsINS_12NumberOptionEE',
        options.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLocale::QLocale()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#QLocale
    """
    #  QLocale::QLocale()
    self._noteCreation(QLocale, lambda: Rituals.call(
        'ritual_ZN7QLocaleC1Ev',
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QLocale::QLocale(const QString &name)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#QLocale

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QLocale::QLocale(const QString &name)
    self._noteCreation(QLocale, lambda: Rituals.call(
        'ritual_ZN7QLocaleC1ERK7QString', name,
    ))

  @overload(Language, Country)
  def __init__(self, language: Language, territory: Country) -> None:
    """
    Notes what was given, for Qt's 'QLocale::QLocale(Language language,
    Territory territory)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#QLocale

    Parameters
    ----------

    language : Language
      Passed on as its number.

    territory : Country
      Passed on as its number.
    """
    #  QLocale::QLocale(Language language, Territory territory)
    self._noteCreation(QLocale, lambda: Rituals.call(
        'ritual_ZN7QLocaleC1ENS_8LanguageENS_7CountryE',
        language.value, territory.value,
    ))

  @overload(Language)
  @overload(Language, Script)
  @overload(Language, Script, Country)
  def __init__(
      self,
      language: Language,
      script: Script = Script.AnyScript,
      territory: Country = Country.AnyTerritory,
  ) -> None:
    """
    Notes what was given, for Qt's 'QLocale::QLocale(Language language,
    Script script, Territory territory)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#QLocale

    Parameters
    ----------

    language : Language
      Passed on as its number.

    script : Script
      Passed on as its number. May be left out, as in Qt: it is then
      Script.AnyScript.

    territory : Country
      Passed on as its number. May be left out, as in Qt: it is then
      Country.AnyTerritory.
    """
    #  QLocale::QLocale(Language language, Script script, Territory
    #      territory)
    self._noteCreation(QLocale, lambda: Rituals.call(
        'ritual_ZN7QLocaleC1ENS_8LanguageENS_6ScriptENS_7CountryE',
        language.value, script.value, territory.value,
    ))

  @overload(THIS)
  def __init__(self, other: QLocale) -> None:
    """
    Notes what was given, for Qt's 'QLocale::QLocale(const QLocale &other)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#QLocale

    Parameters
    ----------

    other : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  QLocale::QLocale(const QLocale &other)
    self._noteCreation(QLocale, lambda: Rituals.call(
        'ritual_ZN7QLocaleC1ERKS_', self._valueOf(other),
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
