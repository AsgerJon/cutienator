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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

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
  so far, 56 names in all: 'language', 'script', 'country', 'name',
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
  'c', 'system', 'setNumberOptions', 'numberOptions', 'quoteString',
  '__eq__', '__ne__'. It can be made from Python, in 5 ways; see '__init__'.

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

  27 of the 147 functions Qt declares: 22 takes or gives a type that cannot
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

  #  The enums Qt writes inside QLocale, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Country(CuteNum):
    """
    The enum 'QLocale::Country' of Qt, with the 288 names Qt gives in it.
    """

    AnyTerritory = Kee[int](0)
    Afghanistan = Kee[int](1)
    AlandIslands = Kee[int](2)
    Albania = Kee[int](3)
    Algeria = Kee[int](4)
    AmericanSamoa = Kee[int](5)
    Andorra = Kee[int](6)
    Angola = Kee[int](7)
    Anguilla = Kee[int](8)
    Antarctica = Kee[int](9)
    AntiguaAndBarbuda = Kee[int](10)
    Argentina = Kee[int](11)
    Armenia = Kee[int](12)
    Aruba = Kee[int](13)
    AscensionIsland = Kee[int](14)
    Australia = Kee[int](15)
    Austria = Kee[int](16)
    Azerbaijan = Kee[int](17)
    Bahamas = Kee[int](18)
    Bahrain = Kee[int](19)
    Bangladesh = Kee[int](20)
    Barbados = Kee[int](21)
    Belarus = Kee[int](22)
    Belgium = Kee[int](23)
    Belize = Kee[int](24)
    Benin = Kee[int](25)
    Bermuda = Kee[int](26)
    Bhutan = Kee[int](27)
    Bolivia = Kee[int](28)
    BosniaAndHerzegovina = Kee[int](29)
    Botswana = Kee[int](30)
    BouvetIsland = Kee[int](31)
    Brazil = Kee[int](32)
    BritishIndianOceanTerritory = Kee[int](33)
    BritishVirginIslands = Kee[int](34)
    Brunei = Kee[int](35)
    Bulgaria = Kee[int](36)
    BurkinaFaso = Kee[int](37)
    Burundi = Kee[int](38)
    Cambodia = Kee[int](39)
    Cameroon = Kee[int](40)
    Canada = Kee[int](41)
    CanaryIslands = Kee[int](42)
    CapeVerde = Kee[int](43)
    CaribbeanNetherlands = Kee[int](44)
    CaymanIslands = Kee[int](45)
    CentralAfricanRepublic = Kee[int](46)
    CeutaAndMelilla = Kee[int](47)
    Chad = Kee[int](48)
    Chile = Kee[int](49)
    China = Kee[int](50)
    ChristmasIsland = Kee[int](51)
    ClippertonIsland = Kee[int](52)
    CocosIslands = Kee[int](53)
    Colombia = Kee[int](54)
    Comoros = Kee[int](55)
    CongoBrazzaville = Kee[int](56)
    CongoKinshasa = Kee[int](57)
    CookIslands = Kee[int](58)
    CostaRica = Kee[int](59)
    Croatia = Kee[int](60)
    Cuba = Kee[int](61)
    Curacao = Kee[int](62)
    Cyprus = Kee[int](63)
    Czechia = Kee[int](64)
    Denmark = Kee[int](65)
    DiegoGarcia = Kee[int](66)
    Djibouti = Kee[int](67)
    Dominica = Kee[int](68)
    DominicanRepublic = Kee[int](69)
    Ecuador = Kee[int](70)
    Egypt = Kee[int](71)
    ElSalvador = Kee[int](72)
    EquatorialGuinea = Kee[int](73)
    Eritrea = Kee[int](74)
    Estonia = Kee[int](75)
    Eswatini = Kee[int](76)
    Ethiopia = Kee[int](77)
    Europe = Kee[int](78)
    EuropeanUnion = Kee[int](79)
    FalklandIslands = Kee[int](80)
    FaroeIslands = Kee[int](81)
    Fiji = Kee[int](82)
    Finland = Kee[int](83)
    France = Kee[int](84)
    FrenchGuiana = Kee[int](85)
    FrenchPolynesia = Kee[int](86)
    FrenchSouthernTerritories = Kee[int](87)
    Gabon = Kee[int](88)
    Gambia = Kee[int](89)
    Georgia = Kee[int](90)
    Germany = Kee[int](91)
    Ghana = Kee[int](92)
    Gibraltar = Kee[int](93)
    Greece = Kee[int](94)
    Greenland = Kee[int](95)
    Grenada = Kee[int](96)
    Guadeloupe = Kee[int](97)
    Guam = Kee[int](98)
    Guatemala = Kee[int](99)
    Guernsey = Kee[int](100)
    GuineaBissau = Kee[int](101)
    Guinea = Kee[int](102)
    Guyana = Kee[int](103)
    Haiti = Kee[int](104)
    HeardAndMcDonaldIslands = Kee[int](105)
    Honduras = Kee[int](106)
    HongKong = Kee[int](107)
    Hungary = Kee[int](108)
    Iceland = Kee[int](109)
    India = Kee[int](110)
    Indonesia = Kee[int](111)
    Iran = Kee[int](112)
    Iraq = Kee[int](113)
    Ireland = Kee[int](114)
    IsleOfMan = Kee[int](115)
    Israel = Kee[int](116)
    Italy = Kee[int](117)
    IvoryCoast = Kee[int](118)
    Jamaica = Kee[int](119)
    Japan = Kee[int](120)
    Jersey = Kee[int](121)
    Jordan = Kee[int](122)
    Kazakhstan = Kee[int](123)
    Kenya = Kee[int](124)
    Kiribati = Kee[int](125)
    Kosovo = Kee[int](126)
    Kuwait = Kee[int](127)
    Kyrgyzstan = Kee[int](128)
    Laos = Kee[int](129)
    LatinAmerica = Kee[int](130)
    Latvia = Kee[int](131)
    Lebanon = Kee[int](132)
    Lesotho = Kee[int](133)
    Liberia = Kee[int](134)
    Libya = Kee[int](135)
    Liechtenstein = Kee[int](136)
    Lithuania = Kee[int](137)
    Luxembourg = Kee[int](138)
    Macao = Kee[int](139)
    Macedonia = Kee[int](140)
    Madagascar = Kee[int](141)
    Malawi = Kee[int](142)
    Malaysia = Kee[int](143)
    Maldives = Kee[int](144)
    Mali = Kee[int](145)
    Malta = Kee[int](146)
    MarshallIslands = Kee[int](147)
    Martinique = Kee[int](148)
    Mauritania = Kee[int](149)
    Mauritius = Kee[int](150)
    Mayotte = Kee[int](151)
    Mexico = Kee[int](152)
    Micronesia = Kee[int](153)
    Moldova = Kee[int](154)
    Monaco = Kee[int](155)
    Mongolia = Kee[int](156)
    Montenegro = Kee[int](157)
    Montserrat = Kee[int](158)
    Morocco = Kee[int](159)
    Mozambique = Kee[int](160)
    Myanmar = Kee[int](161)
    Namibia = Kee[int](162)
    NauruTerritory = Kee[int](163)
    Nepal = Kee[int](164)
    Netherlands = Kee[int](165)
    NewCaledonia = Kee[int](166)
    NewZealand = Kee[int](167)
    Nicaragua = Kee[int](168)
    Nigeria = Kee[int](169)
    Niger = Kee[int](170)
    Niue = Kee[int](171)
    NorfolkIsland = Kee[int](172)
    NorthernMarianaIslands = Kee[int](173)
    NorthKorea = Kee[int](174)
    Norway = Kee[int](175)
    Oman = Kee[int](176)
    OutlyingOceania = Kee[int](177)
    Pakistan = Kee[int](178)
    Palau = Kee[int](179)
    PalestinianTerritories = Kee[int](180)
    Panama = Kee[int](181)
    PapuaNewGuinea = Kee[int](182)
    Paraguay = Kee[int](183)
    Peru = Kee[int](184)
    Philippines = Kee[int](185)
    Pitcairn = Kee[int](186)
    Poland = Kee[int](187)
    Portugal = Kee[int](188)
    PuertoRico = Kee[int](189)
    Qatar = Kee[int](190)
    Reunion = Kee[int](191)
    Romania = Kee[int](192)
    Russia = Kee[int](193)
    Rwanda = Kee[int](194)
    SaintBarthelemy = Kee[int](195)
    SaintHelena = Kee[int](196)
    SaintKittsAndNevis = Kee[int](197)
    SaintLucia = Kee[int](198)
    SaintMartin = Kee[int](199)
    SaintPierreAndMiquelon = Kee[int](200)
    SaintVincentAndGrenadines = Kee[int](201)
    Samoa = Kee[int](202)
    SanMarino = Kee[int](203)
    SaoTomeAndPrincipe = Kee[int](204)
    SaudiArabia = Kee[int](205)
    Senegal = Kee[int](206)
    Serbia = Kee[int](207)
    Seychelles = Kee[int](208)
    SierraLeone = Kee[int](209)
    Singapore = Kee[int](210)
    SintMaarten = Kee[int](211)
    Slovakia = Kee[int](212)
    Slovenia = Kee[int](213)
    SolomonIslands = Kee[int](214)
    Somalia = Kee[int](215)
    SouthAfrica = Kee[int](216)
    SouthGeorgiaAndSouthSandwichIslands = Kee[int](217)
    SouthKorea = Kee[int](218)
    SouthSudan = Kee[int](219)
    Spain = Kee[int](220)
    SriLanka = Kee[int](221)
    Sudan = Kee[int](222)
    Suriname = Kee[int](223)
    SvalbardAndJanMayen = Kee[int](224)
    Sweden = Kee[int](225)
    Switzerland = Kee[int](226)
    Syria = Kee[int](227)
    Taiwan = Kee[int](228)
    Tajikistan = Kee[int](229)
    Tanzania = Kee[int](230)
    Thailand = Kee[int](231)
    TimorLeste = Kee[int](232)
    Togo = Kee[int](233)
    TokelauTerritory = Kee[int](234)
    Tonga = Kee[int](235)
    TrinidadAndTobago = Kee[int](236)
    TristanDaCunha = Kee[int](237)
    Tunisia = Kee[int](238)
    Turkey = Kee[int](239)
    Turkmenistan = Kee[int](240)
    TurksAndCaicosIslands = Kee[int](241)
    TuvaluTerritory = Kee[int](242)
    Uganda = Kee[int](243)
    Ukraine = Kee[int](244)
    UnitedArabEmirates = Kee[int](245)
    UnitedKingdom = Kee[int](246)
    UnitedStatesOutlyingIslands = Kee[int](247)
    UnitedStates = Kee[int](248)
    UnitedStatesVirginIslands = Kee[int](249)
    Uruguay = Kee[int](250)
    Uzbekistan = Kee[int](251)
    Vanuatu = Kee[int](252)
    VaticanCity = Kee[int](253)
    Venezuela = Kee[int](254)
    Vietnam = Kee[int](255)
    WallisAndFutuna = Kee[int](256)
    WesternSahara = Kee[int](257)
    World = Kee[int](258)
    Yemen = Kee[int](259)
    Zambia = Kee[int](260)
    Zimbabwe = Kee[int](261)
    AnyCountry = Kee[int](0)
    Bonaire = Kee[int](44)
    BosniaAndHerzegowina = Kee[int](29)
    CuraSao = Kee[int](62)
    CzechRepublic = Kee[int](64)
    DemocraticRepublicOfCongo = Kee[int](57)
    DemocraticRepublicOfKorea = Kee[int](174)
    EastTimor = Kee[int](232)
    LatinAmericaAndTheCaribbean = Kee[int](130)
    Macau = Kee[int](139)
    NauruCountry = Kee[int](163)
    PeoplesRepublicOfCongo = Kee[int](56)
    RepublicOfKorea = Kee[int](218)
    RussianFederation = Kee[int](193)
    SaintVincentAndTheGrenadines = Kee[int](201)
    SouthGeorgiaAndTheSouthSandwichIslands = Kee[int](217)
    SvalbardAndJanMayenIslands = Kee[int](224)
    Swaziland = Kee[int](76)
    SyrianArabRepublic = Kee[int](227)
    TokelauCountry = Kee[int](234)
    TuvaluCountry = Kee[int](242)
    UnitedStatesMinorOutlyingIslands = Kee[int](247)
    VaticanCityState = Kee[int](253)
    WallisAndFutunaIslands = Kee[int](256)
    LastTerritory = Kee[int](261)
    LastCountry = Kee[int](261)

  class CurrencySymbolFormat(CuteNum):
    """
    The enum 'QLocale::CurrencySymbolFormat' of Qt, with the 3 names Qt gives
    in it.
    """

    CurrencyIsoCode = Kee[int](0)
    CurrencySymbol = Kee[int](1)
    CurrencyDisplayName = Kee[int](2)

  class DataSizeFormat(CuteFlags):
    """
    The flags enum 'QLocale::DataSizeFormat' of Qt, with the 5 names Qt gives
    in it. Qt names the type of its combinations 'QLocale::DataSizeFormats'.
    """

    DataSizeBase1000 = 0x1
    DataSizeSIQuantifiers = 0x2
    DataSizeIecFormat = 0x0
    DataSizeTraditionalFormat = 0x2
    DataSizeSIFormat = 0x3

  DataSizeFormats = DataSizeFormat

  class FloatingPointPrecisionOption(CuteNum):
    """
    The enum 'QLocale::FloatingPointPrecisionOption' of Qt, with the 1 names
    Qt gives in it.
    """

    FloatingPointShortest = Kee[int](-128)

  class FormatType(CuteNum):
    """
    The enum 'QLocale::FormatType' of Qt, with the 3 names Qt gives in it.
    """

    LongFormat = Kee[int](0)
    ShortFormat = Kee[int](1)
    NarrowFormat = Kee[int](2)

  class Language(CuteNum):
    """
    The enum 'QLocale::Language' of Qt, with the 369 names Qt gives in it.
    """

    AnyLanguage = Kee[int](0)
    C = Kee[int](1)
    Abkhazian = Kee[int](2)
    Afar = Kee[int](3)
    Afrikaans = Kee[int](4)
    Aghem = Kee[int](5)
    Akan = Kee[int](6)
    Akkadian = Kee[int](7)
    Akoose = Kee[int](8)
    Albanian = Kee[int](9)
    AmericanSignLanguage = Kee[int](10)
    Amharic = Kee[int](11)
    AncientEgyptian = Kee[int](12)
    AncientGreek = Kee[int](13)
    Arabic = Kee[int](14)
    Aragonese = Kee[int](15)
    Aramaic = Kee[int](16)
    Armenian = Kee[int](17)
    Assamese = Kee[int](18)
    Asturian = Kee[int](19)
    Asu = Kee[int](20)
    Atsam = Kee[int](21)
    Avaric = Kee[int](22)
    Avestan = Kee[int](23)
    Aymara = Kee[int](24)
    Azerbaijani = Kee[int](25)
    Bafia = Kee[int](26)
    Balinese = Kee[int](27)
    Bambara = Kee[int](28)
    Bamun = Kee[int](29)
    Bangla = Kee[int](30)
    Basaa = Kee[int](31)
    Bashkir = Kee[int](32)
    Basque = Kee[int](33)
    BatakToba = Kee[int](34)
    Belarusian = Kee[int](35)
    Bemba = Kee[int](36)
    Bena = Kee[int](37)
    Bhojpuri = Kee[int](38)
    Bislama = Kee[int](39)
    Blin = Kee[int](40)
    Bodo = Kee[int](41)
    Bosnian = Kee[int](42)
    Breton = Kee[int](43)
    Buginese = Kee[int](44)
    Bulgarian = Kee[int](45)
    Burmese = Kee[int](46)
    Cantonese = Kee[int](47)
    Catalan = Kee[int](48)
    Cebuano = Kee[int](49)
    CentralAtlasTamazight = Kee[int](50)
    CentralKurdish = Kee[int](51)
    Chakma = Kee[int](52)
    Chamorro = Kee[int](53)
    Chechen = Kee[int](54)
    Cherokee = Kee[int](55)
    Chickasaw = Kee[int](56)
    Chiga = Kee[int](57)
    Chinese = Kee[int](58)
    Church = Kee[int](59)
    Chuvash = Kee[int](60)
    Colognian = Kee[int](61)
    Coptic = Kee[int](62)
    Cornish = Kee[int](63)
    Corsican = Kee[int](64)
    Cree = Kee[int](65)
    Croatian = Kee[int](66)
    Czech = Kee[int](67)
    Danish = Kee[int](68)
    Divehi = Kee[int](69)
    Dogri = Kee[int](70)
    Duala = Kee[int](71)
    Dutch = Kee[int](72)
    Dzongkha = Kee[int](73)
    Embu = Kee[int](74)
    English = Kee[int](75)
    Erzya = Kee[int](76)
    Esperanto = Kee[int](77)
    Estonian = Kee[int](78)
    Ewe = Kee[int](79)
    Ewondo = Kee[int](80)
    Faroese = Kee[int](81)
    Fijian = Kee[int](82)
    Filipino = Kee[int](83)
    Finnish = Kee[int](84)
    French = Kee[int](85)
    Friulian = Kee[int](86)
    Fulah = Kee[int](87)
    Gaelic = Kee[int](88)
    Ga = Kee[int](89)
    Galician = Kee[int](90)
    Ganda = Kee[int](91)
    Geez = Kee[int](92)
    Georgian = Kee[int](93)
    German = Kee[int](94)
    Gothic = Kee[int](95)
    Greek = Kee[int](96)
    Guarani = Kee[int](97)
    Gujarati = Kee[int](98)
    Gusii = Kee[int](99)
    Haitian = Kee[int](100)
    Hausa = Kee[int](101)
    Hawaiian = Kee[int](102)
    Hebrew = Kee[int](103)
    Herero = Kee[int](104)
    Hindi = Kee[int](105)
    HiriMotu = Kee[int](106)
    Hungarian = Kee[int](107)
    Icelandic = Kee[int](108)
    Ido = Kee[int](109)
    Igbo = Kee[int](110)
    InariSami = Kee[int](111)
    Indonesian = Kee[int](112)
    Ingush = Kee[int](113)
    Interlingua = Kee[int](114)
    Interlingue = Kee[int](115)
    Inuktitut = Kee[int](116)
    Inupiaq = Kee[int](117)
    Irish = Kee[int](118)
    Italian = Kee[int](119)
    Japanese = Kee[int](120)
    Javanese = Kee[int](121)
    Jju = Kee[int](122)
    JolaFonyi = Kee[int](123)
    Kabuverdianu = Kee[int](124)
    Kabyle = Kee[int](125)
    Kako = Kee[int](126)
    Kalaallisut = Kee[int](127)
    Kalenjin = Kee[int](128)
    Kamba = Kee[int](129)
    Kannada = Kee[int](130)
    Kanuri = Kee[int](131)
    Kashmiri = Kee[int](132)
    Kazakh = Kee[int](133)
    Kenyang = Kee[int](134)
    Khmer = Kee[int](135)
    Kiche = Kee[int](136)
    Kikuyu = Kee[int](137)
    Kinyarwanda = Kee[int](138)
    Komi = Kee[int](139)
    Kongo = Kee[int](140)
    Konkani = Kee[int](141)
    Korean = Kee[int](142)
    Koro = Kee[int](143)
    KoyraboroSenni = Kee[int](144)
    KoyraChiini = Kee[int](145)
    Kpelle = Kee[int](146)
    Kuanyama = Kee[int](147)
    Kurdish = Kee[int](148)
    Kwasio = Kee[int](149)
    Kyrgyz = Kee[int](150)
    Lakota = Kee[int](151)
    Langi = Kee[int](152)
    Lao = Kee[int](153)
    Latin = Kee[int](154)
    Latvian = Kee[int](155)
    Lezghian = Kee[int](156)
    Limburgish = Kee[int](157)
    Lingala = Kee[int](158)
    LiteraryChinese = Kee[int](159)
    Lithuanian = Kee[int](160)
    Lojban = Kee[int](161)
    LowerSorbian = Kee[int](162)
    LowGerman = Kee[int](163)
    LubaKatanga = Kee[int](164)
    LuleSami = Kee[int](165)
    Luo = Kee[int](166)
    Luxembourgish = Kee[int](167)
    Luyia = Kee[int](168)
    Macedonian = Kee[int](169)
    Machame = Kee[int](170)
    Maithili = Kee[int](171)
    MakhuwaMeetto = Kee[int](172)
    Makonde = Kee[int](173)
    Malagasy = Kee[int](174)
    Malayalam = Kee[int](175)
    Malay = Kee[int](176)
    Maltese = Kee[int](177)
    Mandingo = Kee[int](178)
    Manipuri = Kee[int](179)
    Manx = Kee[int](180)
    Maori = Kee[int](181)
    Mapuche = Kee[int](182)
    Marathi = Kee[int](183)
    Marshallese = Kee[int](184)
    Masai = Kee[int](185)
    Mazanderani = Kee[int](186)
    Mende = Kee[int](187)
    Meru = Kee[int](188)
    Meta = Kee[int](189)
    Mohawk = Kee[int](190)
    Mongolian = Kee[int](191)
    Morisyen = Kee[int](192)
    Mundang = Kee[int](193)
    Muscogee = Kee[int](194)
    Nama = Kee[int](195)
    NauruLanguage = Kee[int](196)
    Navajo = Kee[int](197)
    Ndonga = Kee[int](198)
    Nepali = Kee[int](199)
    Newari = Kee[int](200)
    Ngiemboon = Kee[int](201)
    Ngomba = Kee[int](202)
    NigerianPidgin = Kee[int](203)
    Nko = Kee[int](204)
    NorthernLuri = Kee[int](205)
    NorthernSami = Kee[int](206)
    NorthernSotho = Kee[int](207)
    NorthNdebele = Kee[int](208)
    NorwegianBokmal = Kee[int](209)
    NorwegianNynorsk = Kee[int](210)
    Nuer = Kee[int](211)
    Nyanja = Kee[int](212)
    Nyankole = Kee[int](213)
    Occitan = Kee[int](214)
    Odia = Kee[int](215)
    Ojibwa = Kee[int](216)
    OldIrish = Kee[int](217)
    OldNorse = Kee[int](218)
    OldPersian = Kee[int](219)
    Oromo = Kee[int](220)
    Osage = Kee[int](221)
    Ossetic = Kee[int](222)
    Pahlavi = Kee[int](223)
    Palauan = Kee[int](224)
    Pali = Kee[int](225)
    Papiamento = Kee[int](226)
    Pashto = Kee[int](227)
    Persian = Kee[int](228)
    Phoenician = Kee[int](229)
    Polish = Kee[int](230)
    Portuguese = Kee[int](231)
    Prussian = Kee[int](232)
    Punjabi = Kee[int](233)
    Quechua = Kee[int](234)
    Romanian = Kee[int](235)
    Romansh = Kee[int](236)
    Rombo = Kee[int](237)
    Rundi = Kee[int](238)
    Russian = Kee[int](239)
    Rwa = Kee[int](240)
    Saho = Kee[int](241)
    Sakha = Kee[int](242)
    Samburu = Kee[int](243)
    Samoan = Kee[int](244)
    Sango = Kee[int](245)
    Sangu = Kee[int](246)
    Sanskrit = Kee[int](247)
    Santali = Kee[int](248)
    Sardinian = Kee[int](249)
    Saurashtra = Kee[int](250)
    Sena = Kee[int](251)
    Serbian = Kee[int](252)
    Shambala = Kee[int](253)
    Shona = Kee[int](254)
    SichuanYi = Kee[int](255)
    Sicilian = Kee[int](256)
    Sidamo = Kee[int](257)
    Silesian = Kee[int](258)
    Sindhi = Kee[int](259)
    Sinhala = Kee[int](260)
    SkoltSami = Kee[int](261)
    Slovak = Kee[int](262)
    Slovenian = Kee[int](263)
    Soga = Kee[int](264)
    Somali = Kee[int](265)
    SouthernKurdish = Kee[int](266)
    SouthernSami = Kee[int](267)
    SouthernSotho = Kee[int](268)
    SouthNdebele = Kee[int](269)
    Spanish = Kee[int](270)
    StandardMoroccanTamazight = Kee[int](271)
    Sundanese = Kee[int](272)
    Swahili = Kee[int](273)
    Swati = Kee[int](274)
    Swedish = Kee[int](275)
    SwissGerman = Kee[int](276)
    Syriac = Kee[int](277)
    Tachelhit = Kee[int](278)
    Tahitian = Kee[int](279)
    TaiDam = Kee[int](280)
    Taita = Kee[int](281)
    Tajik = Kee[int](282)
    Tamil = Kee[int](283)
    Taroko = Kee[int](284)
    Tasawaq = Kee[int](285)
    Tatar = Kee[int](286)
    Telugu = Kee[int](287)
    Teso = Kee[int](288)
    Thai = Kee[int](289)
    Tibetan = Kee[int](290)
    Tigre = Kee[int](291)
    Tigrinya = Kee[int](292)
    TokelauLanguage = Kee[int](293)
    TokPisin = Kee[int](294)
    Tongan = Kee[int](295)
    Tsonga = Kee[int](296)
    Tswana = Kee[int](297)
    Turkish = Kee[int](298)
    Turkmen = Kee[int](299)
    TuvaluLanguage = Kee[int](300)
    Tyap = Kee[int](301)
    Ugaritic = Kee[int](302)
    Ukrainian = Kee[int](303)
    UpperSorbian = Kee[int](304)
    Urdu = Kee[int](305)
    Uyghur = Kee[int](306)
    Uzbek = Kee[int](307)
    Vai = Kee[int](308)
    Venda = Kee[int](309)
    Vietnamese = Kee[int](310)
    Volapuk = Kee[int](311)
    Vunjo = Kee[int](312)
    Walloon = Kee[int](313)
    Walser = Kee[int](314)
    Warlpiri = Kee[int](315)
    Welsh = Kee[int](316)
    WesternBalochi = Kee[int](317)
    WesternFrisian = Kee[int](318)
    Wolaytta = Kee[int](319)
    Wolof = Kee[int](320)
    Xhosa = Kee[int](321)
    Yangben = Kee[int](322)
    Yiddish = Kee[int](323)
    Yoruba = Kee[int](324)
    Zarma = Kee[int](325)
    Zhuang = Kee[int](326)
    Zulu = Kee[int](327)
    Kaingang = Kee[int](328)
    Nheengatu = Kee[int](329)
    Haryanvi = Kee[int](330)
    NorthernFrisian = Kee[int](331)
    Rajasthani = Kee[int](332)
    Moksha = Kee[int](333)
    TokiPona = Kee[int](334)
    Pijin = Kee[int](335)
    Obolo = Kee[int](336)
    Baluchi = Kee[int](337)
    Ligurian = Kee[int](338)
    Rohingya = Kee[int](339)
    Torwali = Kee[int](340)
    Anii = Kee[int](341)
    Kangri = Kee[int](342)
    Venetian = Kee[int](343)
    Kuvi = Kee[int](344)
    KaraKalpak = Kee[int](345)
    SwampyCree = Kee[int](346)
    Ladin = Kee[int](347)
    Shan = Kee[int](348)
    Afan = Kee[int](220)
    Bengali = Kee[int](30)
    Bhutani = Kee[int](73)
    Byelorussian = Kee[int](35)
    Cambodian = Kee[int](135)
    CentralMoroccoTamazight = Kee[int](50)
    Chewa = Kee[int](212)
    Frisian = Kee[int](318)
    Greenlandic = Kee[int](127)
    Inupiak = Kee[int](117)
    Kirghiz = Kee[int](150)
    Kurundi = Kee[int](238)
    Kwanyama = Kee[int](147)
    Navaho = Kee[int](197)
    Oriya = Kee[int](215)
    RhaetoRomance = Kee[int](236)
    Uighur = Kee[int](306)
    Uigur = Kee[int](306)
    Walamo = Kee[int](319)
    LastLanguage = Kee[int](348)

  class LanguageCodeType(CuteFlags):
    """
    The flags enum 'QLocale::LanguageCodeType' of Qt, with the 10 names Qt
    gives in it. Qt names the type of its combinations
    'QLocale::LanguageCodeTypes'.
    """

    ISO639Part1 = 0x1
    ISO639Part2B = 0x2
    ISO639Part2T = 0x4
    ISO639Part3 = 0x8
    LegacyLanguageCode = 0x8000
    ISO639Part2 = 0x6
    ISO639Alpha2 = 0x1
    ISO639Alpha3 = 0xe
    ISO639 = 0xf
    AnyLanguageCode = -1

  LanguageCodeTypes = LanguageCodeType

  class MeasurementSystem(CuteNum):
    """
    The enum 'QLocale::MeasurementSystem' of Qt, with the 4 names Qt gives in
    it.
    """

    MetricSystem = Kee[int](0)
    ImperialUSSystem = Kee[int](1)
    ImperialUKSystem = Kee[int](2)
    ImperialSystem = Kee[int](1)

  class NumberOption(CuteFlags):
    """
    The flags enum 'QLocale::NumberOption' of Qt, with the 7 names Qt gives
    in it. Qt names the type of its combinations 'QLocale::NumberOptions'.
    """

    DefaultNumberOptions = 0x0
    OmitGroupSeparator = 0x1
    RejectGroupSeparator = 0x2
    OmitLeadingZeroInExponent = 0x4
    RejectLeadingZeroInExponent = 0x8
    IncludeTrailingZeroesAfterDot = 0x10
    RejectTrailingZeroesAfterDot = 0x20

  NumberOptions = NumberOption

  class QuotationStyle(CuteNum):
    """
    The enum 'QLocale::QuotationStyle' of Qt, with the 2 names Qt gives in
    it.
    """

    StandardQuotation = Kee[int](0)
    AlternateQuotation = Kee[int](1)

  class Script(CuteNum):
    """
    The enum 'QLocale::Script' of Qt, with the 149 names Qt gives in it.
    """

    AnyScript = Kee[int](0)
    AdlamScript = Kee[int](1)
    AhomScript = Kee[int](2)
    AnatolianHieroglyphsScript = Kee[int](3)
    ArabicScript = Kee[int](4)
    ArmenianScript = Kee[int](5)
    AvestanScript = Kee[int](6)
    BalineseScript = Kee[int](7)
    BamumScript = Kee[int](8)
    BanglaScript = Kee[int](9)
    BassaVahScript = Kee[int](10)
    BatakScript = Kee[int](11)
    BhaiksukiScript = Kee[int](12)
    BopomofoScript = Kee[int](13)
    BrahmiScript = Kee[int](14)
    BrailleScript = Kee[int](15)
    BugineseScript = Kee[int](16)
    BuhidScript = Kee[int](17)
    CanadianAboriginalScript = Kee[int](18)
    CarianScript = Kee[int](19)
    CaucasianAlbanianScript = Kee[int](20)
    ChakmaScript = Kee[int](21)
    ChamScript = Kee[int](22)
    CherokeeScript = Kee[int](23)
    CopticScript = Kee[int](24)
    CuneiformScript = Kee[int](25)
    CypriotScript = Kee[int](26)
    CyrillicScript = Kee[int](27)
    DeseretScript = Kee[int](28)
    DevanagariScript = Kee[int](29)
    DuployanScript = Kee[int](30)
    EgyptianHieroglyphsScript = Kee[int](31)
    ElbasanScript = Kee[int](32)
    EthiopicScript = Kee[int](33)
    FraserScript = Kee[int](34)
    GeorgianScript = Kee[int](35)
    GlagoliticScript = Kee[int](36)
    GothicScript = Kee[int](37)
    GranthaScript = Kee[int](38)
    GreekScript = Kee[int](39)
    GujaratiScript = Kee[int](40)
    GurmukhiScript = Kee[int](41)
    HangulScript = Kee[int](42)
    HanScript = Kee[int](43)
    HanunooScript = Kee[int](44)
    HanWithBopomofoScript = Kee[int](45)
    HatranScript = Kee[int](46)
    HebrewScript = Kee[int](47)
    HiraganaScript = Kee[int](48)
    ImperialAramaicScript = Kee[int](49)
    InscriptionalPahlaviScript = Kee[int](50)
    InscriptionalParthianScript = Kee[int](51)
    JamoScript = Kee[int](52)
    JapaneseScript = Kee[int](53)
    JavaneseScript = Kee[int](54)
    KaithiScript = Kee[int](55)
    KannadaScript = Kee[int](56)
    KatakanaScript = Kee[int](57)
    KayahLiScript = Kee[int](58)
    KharoshthiScript = Kee[int](59)
    KhmerScript = Kee[int](60)
    KhojkiScript = Kee[int](61)
    KhudawadiScript = Kee[int](62)
    KoreanScript = Kee[int](63)
    LannaScript = Kee[int](64)
    LaoScript = Kee[int](65)
    LatinScript = Kee[int](66)
    LepchaScript = Kee[int](67)
    LimbuScript = Kee[int](68)
    LinearAScript = Kee[int](69)
    LinearBScript = Kee[int](70)
    LycianScript = Kee[int](71)
    LydianScript = Kee[int](72)
    MahajaniScript = Kee[int](73)
    MalayalamScript = Kee[int](74)
    MandaeanScript = Kee[int](75)
    ManichaeanScript = Kee[int](76)
    MarchenScript = Kee[int](77)
    MeiteiMayekScript = Kee[int](78)
    MendeScript = Kee[int](79)
    MeroiticCursiveScript = Kee[int](80)
    MeroiticScript = Kee[int](81)
    ModiScript = Kee[int](82)
    MongolianScript = Kee[int](83)
    MroScript = Kee[int](84)
    MultaniScript = Kee[int](85)
    MyanmarScript = Kee[int](86)
    NabataeanScript = Kee[int](87)
    NewaScript = Kee[int](88)
    NewTaiLueScript = Kee[int](89)
    NkoScript = Kee[int](90)
    OdiaScript = Kee[int](91)
    OghamScript = Kee[int](92)
    OlChikiScript = Kee[int](93)
    OldHungarianScript = Kee[int](94)
    OldItalicScript = Kee[int](95)
    OldNorthArabianScript = Kee[int](96)
    OldPermicScript = Kee[int](97)
    OldPersianScript = Kee[int](98)
    OldSouthArabianScript = Kee[int](99)
    OrkhonScript = Kee[int](100)
    OsageScript = Kee[int](101)
    OsmanyaScript = Kee[int](102)
    PahawhHmongScript = Kee[int](103)
    PalmyreneScript = Kee[int](104)
    PauCinHauScript = Kee[int](105)
    PhagsPaScript = Kee[int](106)
    PhoenicianScript = Kee[int](107)
    PollardPhoneticScript = Kee[int](108)
    PsalterPahlaviScript = Kee[int](109)
    RejangScript = Kee[int](110)
    RunicScript = Kee[int](111)
    SamaritanScript = Kee[int](112)
    SaurashtraScript = Kee[int](113)
    SharadaScript = Kee[int](114)
    ShavianScript = Kee[int](115)
    SiddhamScript = Kee[int](116)
    SignWritingScript = Kee[int](117)
    SimplifiedHanScript = Kee[int](118)
    SinhalaScript = Kee[int](119)
    SoraSompengScript = Kee[int](120)
    SundaneseScript = Kee[int](121)
    SylotiNagriScript = Kee[int](122)
    SyriacScript = Kee[int](123)
    TagalogScript = Kee[int](124)
    TagbanwaScript = Kee[int](125)
    TaiLeScript = Kee[int](126)
    TaiVietScript = Kee[int](127)
    TakriScript = Kee[int](128)
    TamilScript = Kee[int](129)
    TangutScript = Kee[int](130)
    TeluguScript = Kee[int](131)
    ThaanaScript = Kee[int](132)
    ThaiScript = Kee[int](133)
    TibetanScript = Kee[int](134)
    TifinaghScript = Kee[int](135)
    TirhutaScript = Kee[int](136)
    TraditionalHanScript = Kee[int](137)
    UgariticScript = Kee[int](138)
    VaiScript = Kee[int](139)
    VarangKshitiScript = Kee[int](140)
    YiScript = Kee[int](141)
    HanifiScript = Kee[int](142)
    BengaliScript = Kee[int](9)
    MendeKikakuiScript = Kee[int](79)
    OriyaScript = Kee[int](91)
    SimplifiedChineseScript = Kee[int](118)
    TraditionalChineseScript = Kee[int](137)
    LastScript = Kee[int](142)

  class TagSeparator(CuteNum, scoped=True):
    """
    The enum 'QLocale::TagSeparator' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Dash = Kee[int](45)
    Underscore = Kee[int](95)

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

  @overload(str)
  @overload(str, FormatType)
  @overload(str, FormatType, int)
  def toDate(
      self,
      string: str,
      a1: FormatType = FormatType.LongFormat,
      baseYear: int = 1900,
  ) -> QDate:
    """
    Calls Qt's 'QDate QLocale::toDate(const QString &string, FormatType a1,
    int baseYear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#toDate

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    a1 : FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    baseYear : int
      Passed on as it is. May be left out, as in Qt: it is then 1900.

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

  @overload(str, str)
  @overload(str, str, int)
  def toDate(self, string: str, format: str, baseYear: int = 1900) -> QDate:
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
      Passed on as it is. May be left out, as in Qt: it is then 1900.

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

  @overload(str, FormatType, QCalendar)
  @overload(str, FormatType, QCalendar, int)
  def toDate(
      self,
      string: str,
      format: FormatType,
      cal: QCalendar,
      baseYear: int = 1900,
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
      Passed on as it is. May be left out, as in Qt: it is then 1900.

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

  @overload(str, str, QCalendar)
  @overload(str, str, QCalendar, int)
  def toDate(
      self,
      string: str,
      format: str,
      cal: QCalendar,
      baseYear: int = 1900,
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
      Passed on as it is. May be left out, as in Qt: it is then 1900.

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

  @overload(str)
  @overload(str, FormatType)
  @overload(str, FormatType, int)
  def toDateTime(
      self,
      string: str,
      format: FormatType = FormatType.LongFormat,
      baseYear: int = 1900,
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
      Passed on as its number. May be left out, as in Qt: it is then
      FormatType.LongFormat.

    baseYear : int
      Passed on as it is. May be left out, as in Qt: it is then 1900.

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

  @overload(str, str)
  @overload(str, str, int)
  def toDateTime(
      self,
      string: str,
      format: str,
      baseYear: int = 1900,
  ) -> QDateTime:
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
      Passed on as it is. May be left out, as in Qt: it is then 1900.

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

  @overload(str, FormatType, QCalendar)
  @overload(str, FormatType, QCalendar, int)
  def toDateTime(
      self,
      string: str,
      format: FormatType,
      cal: QCalendar,
      baseYear: int = 1900,
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
      Passed on as it is. May be left out, as in Qt: it is then 1900.

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

  @overload(str, str, QCalendar)
  @overload(str, str, QCalendar, int)
  def toDateTime(
      self,
      string: str,
      format: str,
      cal: QCalendar,
      baseYear: int = 1900,
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
      Passed on as it is. May be left out, as in Qt: it is then 1900.

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

  @overload(THIS)
  def __eq__(self, rhs: QLocale) -> bool:
    """
    Calls Qt's 'bool operator==(const QLocale &lhs, const QLocale &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#operator==

    Parameters
    ----------

    rhs : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  bool operator==(const QLocale &lhs, const QLocale &rhs)
    return Rituals.call(
        'ritual_ZeqRK7QLocaleS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QLocale) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLocale &lhs, const QLocale &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocale.html#operator!=

    Parameters
    ----------

    rhs : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  bool operator!=(const QLocale &lhs, const QLocale &rhs)
    return Rituals.call(
        'ritual_ZneRK7QLocaleS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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
