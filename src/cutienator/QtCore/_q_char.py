"""
QChar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QChar(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QChar: a plain Python object standing in front of one
  C++ QChar.

  C++ hands a QChar around as a copy, so every C++ QChar behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QChar that has a ritual and that Python can call so
  far, 45 names in all: 'category', 'direction', 'joiningType',
  'combiningClass', 'mirroredChar', 'hasMirrored', 'decomposition',
  'decompositionTag', 'digitValue', 'toLower', 'toUpper', 'toTitleCase',
  'toCaseFolded', 'script', 'unicodeVersion', 'isNull', 'isPrint', 'isSpace',
  'isMark', 'isPunct', 'isSymbol', 'isLetter', 'isNumber',
  'isLetterOrNumber', 'isDigit', 'isLower', 'isUpper', 'isTitleCase',
  'isNonCharacter', 'isHighSurrogate', 'isLowSurrogate', 'isSurrogate',
  'cell', 'row', 'setCell', 'setRow', 'currentUnicodeVersion', '__eq__',
  '__ne__', '__lt__', '__gt__', '__le__', '__ge__', 'equal_helper',
  'compare_helper'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char QChar::toLatin1() const': gives a single letter as C has it.
  - Qt's 'QChar QChar::fromLatin1(char c)': takes a single letter as C has
    it.
  - Qt's 'QChar::~QChar()': the destructor: Python removes its C++ QChar by
    it, and has no other use for it.

  What has no ritual
  ------------------

  60 of the 110 functions Qt declares: 56 takes or gives a type that cannot
  be passed yet; 4 a template.

  What to expect
  --------------

  - The C++ QChar is created at the first use, not by 'QChar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QChar back gives a copy the ritual made for Python,
    in a new cute QChar.
  """

  #  The enums Qt writes inside QChar, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Category(CuteNum):
    """The enum 'QChar::Category' of Qt, with the 30 names Qt gives in it."""

    Mark_NonSpacing = Kee[int](0)
    Mark_SpacingCombining = Kee[int](1)
    Mark_Enclosing = Kee[int](2)
    Number_DecimalDigit = Kee[int](3)
    Number_Letter = Kee[int](4)
    Number_Other = Kee[int](5)
    Separator_Space = Kee[int](6)
    Separator_Line = Kee[int](7)
    Separator_Paragraph = Kee[int](8)
    Other_Control = Kee[int](9)
    Other_Format = Kee[int](10)
    Other_Surrogate = Kee[int](11)
    Other_PrivateUse = Kee[int](12)
    Other_NotAssigned = Kee[int](13)
    Letter_Uppercase = Kee[int](14)
    Letter_Lowercase = Kee[int](15)
    Letter_Titlecase = Kee[int](16)
    Letter_Modifier = Kee[int](17)
    Letter_Other = Kee[int](18)
    Punctuation_Connector = Kee[int](19)
    Punctuation_Dash = Kee[int](20)
    Punctuation_Open = Kee[int](21)
    Punctuation_Close = Kee[int](22)
    Punctuation_InitialQuote = Kee[int](23)
    Punctuation_FinalQuote = Kee[int](24)
    Punctuation_Other = Kee[int](25)
    Symbol_Math = Kee[int](26)
    Symbol_Currency = Kee[int](27)
    Symbol_Modifier = Kee[int](28)
    Symbol_Other = Kee[int](29)

  class CombiningClass(CuteNum):
    """
    The enum 'QChar::CombiningClass' of Qt, with the 19 names Qt gives in it.
    """

    Combining_BelowLeftAttached = Kee[int](200)
    Combining_BelowAttached = Kee[int](202)
    Combining_BelowRightAttached = Kee[int](204)
    Combining_LeftAttached = Kee[int](208)
    Combining_RightAttached = Kee[int](210)
    Combining_AboveLeftAttached = Kee[int](212)
    Combining_AboveAttached = Kee[int](214)
    Combining_AboveRightAttached = Kee[int](216)
    Combining_BelowLeft = Kee[int](218)
    Combining_Below = Kee[int](220)
    Combining_BelowRight = Kee[int](222)
    Combining_Left = Kee[int](224)
    Combining_Right = Kee[int](226)
    Combining_AboveLeft = Kee[int](228)
    Combining_Above = Kee[int](230)
    Combining_AboveRight = Kee[int](232)
    Combining_DoubleBelow = Kee[int](233)
    Combining_DoubleAbove = Kee[int](234)
    Combining_IotaSubscript = Kee[int](240)

  class Decomposition(CuteNum):
    """
    The enum 'QChar::Decomposition' of Qt, with the 18 names Qt gives in it.
    """

    NoDecomposition = Kee[int](0)
    Canonical = Kee[int](1)
    Font = Kee[int](2)
    NoBreak = Kee[int](3)
    Initial = Kee[int](4)
    Medial = Kee[int](5)
    Final = Kee[int](6)
    Isolated = Kee[int](7)
    Circle = Kee[int](8)
    Super = Kee[int](9)
    Sub = Kee[int](10)
    Vertical = Kee[int](11)
    Wide = Kee[int](12)
    Narrow = Kee[int](13)
    Small = Kee[int](14)
    Square = Kee[int](15)
    Compat = Kee[int](16)
    Fraction = Kee[int](17)

  class Direction(CuteNum):
    """
    The enum 'QChar::Direction' of Qt, with the 23 names Qt gives in it.
    """

    DirL = Kee[int](0)
    DirR = Kee[int](1)
    DirEN = Kee[int](2)
    DirES = Kee[int](3)
    DirET = Kee[int](4)
    DirAN = Kee[int](5)
    DirCS = Kee[int](6)
    DirB = Kee[int](7)
    DirS = Kee[int](8)
    DirWS = Kee[int](9)
    DirON = Kee[int](10)
    DirLRE = Kee[int](11)
    DirLRO = Kee[int](12)
    DirAL = Kee[int](13)
    DirRLE = Kee[int](14)
    DirRLO = Kee[int](15)
    DirPDF = Kee[int](16)
    DirNSM = Kee[int](17)
    DirBN = Kee[int](18)
    DirLRI = Kee[int](19)
    DirRLI = Kee[int](20)
    DirFSI = Kee[int](21)
    DirPDI = Kee[int](22)

  class JoiningType(CuteNum):
    """
    The enum 'QChar::JoiningType' of Qt, with the 6 names Qt gives in it.
    """

    Joining_None = Kee[int](0)
    Joining_Causing = Kee[int](1)
    Joining_Dual = Kee[int](2)
    Joining_Right = Kee[int](3)
    Joining_Left = Kee[int](4)
    Joining_Transparent = Kee[int](5)

  class Script(CuteNum):
    """The enum 'QChar::Script' of Qt, with the 176 names Qt gives in it."""

    Script_Unknown = Kee[int](0)
    Script_Inherited = Kee[int](1)
    Script_Common = Kee[int](2)
    Script_Latin = Kee[int](3)
    Script_Greek = Kee[int](4)
    Script_Cyrillic = Kee[int](5)
    Script_Armenian = Kee[int](6)
    Script_Hebrew = Kee[int](7)
    Script_Arabic = Kee[int](8)
    Script_Syriac = Kee[int](9)
    Script_Thaana = Kee[int](10)
    Script_Devanagari = Kee[int](11)
    Script_Bengali = Kee[int](12)
    Script_Gurmukhi = Kee[int](13)
    Script_Gujarati = Kee[int](14)
    Script_Oriya = Kee[int](15)
    Script_Tamil = Kee[int](16)
    Script_Telugu = Kee[int](17)
    Script_Kannada = Kee[int](18)
    Script_Malayalam = Kee[int](19)
    Script_Sinhala = Kee[int](20)
    Script_Thai = Kee[int](21)
    Script_Lao = Kee[int](22)
    Script_Tibetan = Kee[int](23)
    Script_Myanmar = Kee[int](24)
    Script_Georgian = Kee[int](25)
    Script_Hangul = Kee[int](26)
    Script_Ethiopic = Kee[int](27)
    Script_Cherokee = Kee[int](28)
    Script_CanadianAboriginal = Kee[int](29)
    Script_Ogham = Kee[int](30)
    Script_Runic = Kee[int](31)
    Script_Khmer = Kee[int](32)
    Script_Mongolian = Kee[int](33)
    Script_Hiragana = Kee[int](34)
    Script_Katakana = Kee[int](35)
    Script_Bopomofo = Kee[int](36)
    Script_Han = Kee[int](37)
    Script_Yi = Kee[int](38)
    Script_OldItalic = Kee[int](39)
    Script_Gothic = Kee[int](40)
    Script_Deseret = Kee[int](41)
    Script_Tagalog = Kee[int](42)
    Script_Hanunoo = Kee[int](43)
    Script_Buhid = Kee[int](44)
    Script_Tagbanwa = Kee[int](45)
    Script_Coptic = Kee[int](46)
    Script_Limbu = Kee[int](47)
    Script_TaiLe = Kee[int](48)
    Script_LinearB = Kee[int](49)
    Script_Ugaritic = Kee[int](50)
    Script_Shavian = Kee[int](51)
    Script_Osmanya = Kee[int](52)
    Script_Cypriot = Kee[int](53)
    Script_Braille = Kee[int](54)
    Script_Buginese = Kee[int](55)
    Script_NewTaiLue = Kee[int](56)
    Script_Glagolitic = Kee[int](57)
    Script_Tifinagh = Kee[int](58)
    Script_SylotiNagri = Kee[int](59)
    Script_OldPersian = Kee[int](60)
    Script_Kharoshthi = Kee[int](61)
    Script_Balinese = Kee[int](62)
    Script_Cuneiform = Kee[int](63)
    Script_Phoenician = Kee[int](64)
    Script_PhagsPa = Kee[int](65)
    Script_Nko = Kee[int](66)
    Script_Sundanese = Kee[int](67)
    Script_Lepcha = Kee[int](68)
    Script_OlChiki = Kee[int](69)
    Script_Vai = Kee[int](70)
    Script_Saurashtra = Kee[int](71)
    Script_KayahLi = Kee[int](72)
    Script_Rejang = Kee[int](73)
    Script_Lycian = Kee[int](74)
    Script_Carian = Kee[int](75)
    Script_Lydian = Kee[int](76)
    Script_Cham = Kee[int](77)
    Script_TaiTham = Kee[int](78)
    Script_TaiViet = Kee[int](79)
    Script_Avestan = Kee[int](80)
    Script_EgyptianHieroglyphs = Kee[int](81)
    Script_Samaritan = Kee[int](82)
    Script_Lisu = Kee[int](83)
    Script_Bamum = Kee[int](84)
    Script_Javanese = Kee[int](85)
    Script_MeeteiMayek = Kee[int](86)
    Script_ImperialAramaic = Kee[int](87)
    Script_OldSouthArabian = Kee[int](88)
    Script_InscriptionalParthian = Kee[int](89)
    Script_InscriptionalPahlavi = Kee[int](90)
    Script_OldTurkic = Kee[int](91)
    Script_Kaithi = Kee[int](92)
    Script_Batak = Kee[int](93)
    Script_Brahmi = Kee[int](94)
    Script_Mandaic = Kee[int](95)
    Script_Chakma = Kee[int](96)
    Script_MeroiticCursive = Kee[int](97)
    Script_MeroiticHieroglyphs = Kee[int](98)
    Script_Miao = Kee[int](99)
    Script_Sharada = Kee[int](100)
    Script_SoraSompeng = Kee[int](101)
    Script_Takri = Kee[int](102)
    Script_CaucasianAlbanian = Kee[int](103)
    Script_BassaVah = Kee[int](104)
    Script_Duployan = Kee[int](105)
    Script_Elbasan = Kee[int](106)
    Script_Grantha = Kee[int](107)
    Script_PahawhHmong = Kee[int](108)
    Script_Khojki = Kee[int](109)
    Script_LinearA = Kee[int](110)
    Script_Mahajani = Kee[int](111)
    Script_Manichaean = Kee[int](112)
    Script_MendeKikakui = Kee[int](113)
    Script_Modi = Kee[int](114)
    Script_Mro = Kee[int](115)
    Script_OldNorthArabian = Kee[int](116)
    Script_Nabataean = Kee[int](117)
    Script_Palmyrene = Kee[int](118)
    Script_PauCinHau = Kee[int](119)
    Script_OldPermic = Kee[int](120)
    Script_PsalterPahlavi = Kee[int](121)
    Script_Siddham = Kee[int](122)
    Script_Khudawadi = Kee[int](123)
    Script_Tirhuta = Kee[int](124)
    Script_WarangCiti = Kee[int](125)
    Script_Ahom = Kee[int](126)
    Script_AnatolianHieroglyphs = Kee[int](127)
    Script_Hatran = Kee[int](128)
    Script_Multani = Kee[int](129)
    Script_OldHungarian = Kee[int](130)
    Script_SignWriting = Kee[int](131)
    Script_Adlam = Kee[int](132)
    Script_Bhaiksuki = Kee[int](133)
    Script_Marchen = Kee[int](134)
    Script_Newa = Kee[int](135)
    Script_Osage = Kee[int](136)
    Script_Tangut = Kee[int](137)
    Script_MasaramGondi = Kee[int](138)
    Script_Nushu = Kee[int](139)
    Script_Soyombo = Kee[int](140)
    Script_ZanabazarSquare = Kee[int](141)
    Script_Dogra = Kee[int](142)
    Script_GunjalaGondi = Kee[int](143)
    Script_HanifiRohingya = Kee[int](144)
    Script_Makasar = Kee[int](145)
    Script_Medefaidrin = Kee[int](146)
    Script_OldSogdian = Kee[int](147)
    Script_Sogdian = Kee[int](148)
    Script_Elymaic = Kee[int](149)
    Script_Nandinagari = Kee[int](150)
    Script_NyiakengPuachueHmong = Kee[int](151)
    Script_Wancho = Kee[int](152)
    Script_Chorasmian = Kee[int](153)
    Script_DivesAkuru = Kee[int](154)
    Script_KhitanSmallScript = Kee[int](155)
    Script_Yezidi = Kee[int](156)
    Script_CyproMinoan = Kee[int](157)
    Script_OldUyghur = Kee[int](158)
    Script_Tangsa = Kee[int](159)
    Script_Toto = Kee[int](160)
    Script_Vithkuqi = Kee[int](161)
    Script_Kawi = Kee[int](162)
    Script_NagMundari = Kee[int](163)
    Script_Garay = Kee[int](164)
    Script_GurungKhema = Kee[int](165)
    Script_KiratRai = Kee[int](166)
    Script_OlOnal = Kee[int](167)
    Script_Sunuwar = Kee[int](168)
    Script_Todhri = Kee[int](169)
    Script_TuluTigalari = Kee[int](170)
    Script_Sidetic = Kee[int](171)
    Script_TaiYo = Kee[int](172)
    Script_TolongSiki = Kee[int](173)
    Script_BeriaErfe = Kee[int](174)
    ScriptCount = Kee[int](175)

  class SpecialCharacter(CuteNum):
    """
    The enum 'QChar::SpecialCharacter' of Qt, with the 16 names Qt gives in
    it.
    """

    Null = Kee[int](0)
    Tabulation = Kee[int](9)
    LineFeed = Kee[int](10)
    FormFeed = Kee[int](12)
    CarriageReturn = Kee[int](13)
    Space = Kee[int](32)
    Nbsp = Kee[int](160)
    SoftHyphen = Kee[int](173)
    ReplacementCharacter = Kee[int](65533)
    ObjectReplacementCharacter = Kee[int](65532)
    ByteOrderMark = Kee[int](65279)
    ByteOrderSwapped = Kee[int](65534)
    ParagraphSeparator = Kee[int](8233)
    LineSeparator = Kee[int](8232)
    VisualTabCharacter = Kee[int](8594)
    LastValidCodePoint = Kee[int](1114111)

  class UnicodeVersion(CuteNum):
    """
    The enum 'QChar::UnicodeVersion' of Qt, with the 29 names Qt gives in it.
    """

    Unicode_Unassigned = Kee[int](0)
    Unicode_1_1 = Kee[int](1)
    Unicode_2_0 = Kee[int](2)
    Unicode_2_1_2 = Kee[int](3)
    Unicode_3_0 = Kee[int](4)
    Unicode_3_1 = Kee[int](5)
    Unicode_3_2 = Kee[int](6)
    Unicode_4_0 = Kee[int](7)
    Unicode_4_1 = Kee[int](8)
    Unicode_5_0 = Kee[int](9)
    Unicode_5_1 = Kee[int](10)
    Unicode_5_2 = Kee[int](11)
    Unicode_6_0 = Kee[int](12)
    Unicode_6_1 = Kee[int](13)
    Unicode_6_2 = Kee[int](14)
    Unicode_6_3 = Kee[int](15)
    Unicode_7_0 = Kee[int](16)
    Unicode_8_0 = Kee[int](17)
    Unicode_9_0 = Kee[int](18)
    Unicode_10_0 = Kee[int](19)
    Unicode_11_0 = Kee[int](20)
    Unicode_12_0 = Kee[int](21)
    Unicode_12_1 = Kee[int](22)
    Unicode_13_0 = Kee[int](23)
    Unicode_14_0 = Kee[int](24)
    Unicode_15_0 = Kee[int](25)
    Unicode_15_1 = Kee[int](26)
    Unicode_16_0 = Kee[int](27)
    Unicode_17_0 = Kee[int](28)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def currentUnicodeVersion() -> UnicodeVersion:
    """
    Calls Qt's 'UnicodeVersion QChar::currentUnicodeVersion()'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#currentUnicodeVersion

    Returns
    -------

    UnicodeVersion
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UnicodeVersion(number)'
      gives.
    """
    #  UnicodeVersion QChar::currentUnicodeVersion()
    return QChar.UnicodeVersion(Rituals.call(
        'ritual_ZN5QChar21currentUnicodeVersionEv',
    ))

  @staticmethod
  @overload(THIS, str)
  @overload(THIS, NoneType)
  def equal_helper(lhs: QChar, rhs: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QChar::equal_helper(QChar lhs, const char *rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#equal_helper

    Parameters
    ----------

    lhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    rhs : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QChar::equal_helper(QChar lhs, const char *rhs)
    return Rituals.call(
        'ritual_ZN5QChar12equal_helperES_PKc',
        CuteMixin._valueOf(lhs), CuteMixin._bytesOf(rhs),
    )

  @staticmethod
  @overload(THIS, str)
  @overload(THIS, NoneType)
  def compare_helper(lhs: QChar, rhs: Optional[str]) -> int:
    """
    Calls Qt's 'int QChar::compare_helper(QChar lhs, const char *rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#compare_helper

    Parameters
    ----------

    lhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    rhs : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QChar::compare_helper(QChar lhs, const char *rhs)
    return Rituals.call(
        'ritual_ZN5QChar14compare_helperES_PKc',
        CuteMixin._valueOf(lhs), CuteMixin._bytesOf(rhs),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QChar'

  #  Qt's '~QChar()'. Naming it makes this a value class: Python owns every
  #  C++ QChar behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QCharD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def category(self) -> Category:
    """
    Calls Qt's 'Category QChar::category() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#category

    Returns
    -------

    Category
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Category(number)' gives.
    """
    #  Category QChar::category() const
    return QChar.Category(self.uglySide.call('ritual_ZNK5QChar8categoryEv'))

  def direction(self) -> Direction:
    """
    Calls Qt's 'Direction QChar::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#direction

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  Direction QChar::direction() const
    return QChar.Direction(self.uglySide.call(
        'ritual_ZNK5QChar9directionEv',
    ))

  def joiningType(self) -> JoiningType:
    """
    Calls Qt's 'JoiningType QChar::joiningType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#joiningType

    Returns
    -------

    JoiningType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'JoiningType(number)'
      gives.
    """
    #  JoiningType QChar::joiningType() const
    return QChar.JoiningType(self.uglySide.call(
        'ritual_ZNK5QChar11joiningTypeEv',
    ))

  def combiningClass(self) -> int:
    """
    Calls Qt's 'unsigned char QChar::combiningClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#combiningClass
    """
    #  unsigned char QChar::combiningClass() const
    return self.uglySide.call('ritual_ZNK5QChar14combiningClassEv')

  def mirroredChar(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::mirroredChar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#mirroredChar

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::mirroredChar() const
    address = self.uglySide.call('ritual_ZNK5QChar12mirroredCharEv')
    return QChar._cuteOwning(address)

  def hasMirrored(self) -> bool:
    """
    Calls Qt's 'bool QChar::hasMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#hasMirrored
    """
    #  bool QChar::hasMirrored() const
    return self.uglySide.call('ritual_ZNK5QChar11hasMirroredEv')

  def decomposition(self) -> str:
    """
    Calls Qt's 'QString QChar::decomposition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#decomposition

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QChar::decomposition() const
    return self.uglySide.call('ritual_ZNK5QChar13decompositionEv')

  def decompositionTag(self) -> Decomposition:
    """
    Calls Qt's 'Decomposition QChar::decompositionTag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#decompositionTag

    Returns
    -------

    Decomposition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Decomposition(number)'
      gives.
    """
    #  Decomposition QChar::decompositionTag() const
    return QChar.Decomposition(self.uglySide.call(
        'ritual_ZNK5QChar16decompositionTagEv',
    ))

  def digitValue(self) -> int:
    """
    Calls Qt's 'int QChar::digitValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#digitValue
    """
    #  int QChar::digitValue() const
    return self.uglySide.call('ritual_ZNK5QChar10digitValueEv')

  def toLower(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::toLower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#toLower

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::toLower() const
    address = self.uglySide.call('ritual_ZNK5QChar7toLowerEv')
    return QChar._cuteOwning(address)

  def toUpper(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::toUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#toUpper

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::toUpper() const
    address = self.uglySide.call('ritual_ZNK5QChar7toUpperEv')
    return QChar._cuteOwning(address)

  def toTitleCase(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::toTitleCase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#toTitleCase

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::toTitleCase() const
    address = self.uglySide.call('ritual_ZNK5QChar11toTitleCaseEv')
    return QChar._cuteOwning(address)

  def toCaseFolded(self) -> QChar:
    """
    Calls Qt's 'QChar QChar::toCaseFolded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#toCaseFolded

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QChar::toCaseFolded() const
    address = self.uglySide.call('ritual_ZNK5QChar12toCaseFoldedEv')
    return QChar._cuteOwning(address)

  def script(self) -> Script:
    """
    Calls Qt's 'Script QChar::script() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#script

    Returns
    -------

    Script
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Script(number)' gives.
    """
    #  Script QChar::script() const
    return QChar.Script(self.uglySide.call('ritual_ZNK5QChar6scriptEv'))

  def unicodeVersion(self) -> UnicodeVersion:
    """
    Calls Qt's 'UnicodeVersion QChar::unicodeVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#unicodeVersion

    Returns
    -------

    UnicodeVersion
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UnicodeVersion(number)'
      gives.
    """
    #  UnicodeVersion QChar::unicodeVersion() const
    return QChar.UnicodeVersion(self.uglySide.call(
        'ritual_ZNK5QChar14unicodeVersionEv',
    ))

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QChar::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isNull
    """
    #  bool QChar::isNull() const
    return self.uglySide.call('ritual_ZNK5QChar6isNullEv')

  def isPrint(self) -> bool:
    """
    Calls Qt's 'bool QChar::isPrint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isPrint
    """
    #  bool QChar::isPrint() const
    return self.uglySide.call('ritual_ZNK5QChar7isPrintEv')

  def isSpace(self) -> bool:
    """
    Calls Qt's 'bool QChar::isSpace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isSpace
    """
    #  bool QChar::isSpace() const
    return self.uglySide.call('ritual_ZNK5QChar7isSpaceEv')

  def isMark(self) -> bool:
    """
    Calls Qt's 'bool QChar::isMark() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isMark
    """
    #  bool QChar::isMark() const
    return self.uglySide.call('ritual_ZNK5QChar6isMarkEv')

  def isPunct(self) -> bool:
    """
    Calls Qt's 'bool QChar::isPunct() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isPunct
    """
    #  bool QChar::isPunct() const
    return self.uglySide.call('ritual_ZNK5QChar7isPunctEv')

  def isSymbol(self) -> bool:
    """
    Calls Qt's 'bool QChar::isSymbol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isSymbol
    """
    #  bool QChar::isSymbol() const
    return self.uglySide.call('ritual_ZNK5QChar8isSymbolEv')

  def isLetter(self) -> bool:
    """
    Calls Qt's 'bool QChar::isLetter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isLetter
    """
    #  bool QChar::isLetter() const
    return self.uglySide.call('ritual_ZNK5QChar8isLetterEv')

  def isNumber(self) -> bool:
    """
    Calls Qt's 'bool QChar::isNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isNumber
    """
    #  bool QChar::isNumber() const
    return self.uglySide.call('ritual_ZNK5QChar8isNumberEv')

  def isLetterOrNumber(self) -> bool:
    """
    Calls Qt's 'bool QChar::isLetterOrNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isLetterOrNumber
    """
    #  bool QChar::isLetterOrNumber() const
    return self.uglySide.call('ritual_ZNK5QChar16isLetterOrNumberEv')

  def isDigit(self) -> bool:
    """
    Calls Qt's 'bool QChar::isDigit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isDigit
    """
    #  bool QChar::isDigit() const
    return self.uglySide.call('ritual_ZNK5QChar7isDigitEv')

  def isLower(self) -> bool:
    """
    Calls Qt's 'bool QChar::isLower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isLower
    """
    #  bool QChar::isLower() const
    return self.uglySide.call('ritual_ZNK5QChar7isLowerEv')

  def isUpper(self) -> bool:
    """
    Calls Qt's 'bool QChar::isUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isUpper
    """
    #  bool QChar::isUpper() const
    return self.uglySide.call('ritual_ZNK5QChar7isUpperEv')

  def isTitleCase(self) -> bool:
    """
    Calls Qt's 'bool QChar::isTitleCase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isTitleCase
    """
    #  bool QChar::isTitleCase() const
    return self.uglySide.call('ritual_ZNK5QChar11isTitleCaseEv')

  def isNonCharacter(self) -> bool:
    """
    Calls Qt's 'bool QChar::isNonCharacter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isNonCharacter
    """
    #  bool QChar::isNonCharacter() const
    return self.uglySide.call('ritual_ZNK5QChar14isNonCharacterEv')

  def isHighSurrogate(self) -> bool:
    """
    Calls Qt's 'bool QChar::isHighSurrogate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isHighSurrogate
    """
    #  bool QChar::isHighSurrogate() const
    return self.uglySide.call('ritual_ZNK5QChar15isHighSurrogateEv')

  def isLowSurrogate(self) -> bool:
    """
    Calls Qt's 'bool QChar::isLowSurrogate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isLowSurrogate
    """
    #  bool QChar::isLowSurrogate() const
    return self.uglySide.call('ritual_ZNK5QChar14isLowSurrogateEv')

  def isSurrogate(self) -> bool:
    """
    Calls Qt's 'bool QChar::isSurrogate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#isSurrogate
    """
    #  bool QChar::isSurrogate() const
    return self.uglySide.call('ritual_ZNK5QChar11isSurrogateEv')

  def cell(self) -> int:
    """
    Calls Qt's 'uchar QChar::cell() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#cell
    """
    #  uchar QChar::cell() const
    return self.uglySide.call('ritual_ZNK5QChar4cellEv')

  def row(self) -> int:
    """
    Calls Qt's 'uchar QChar::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#row
    """
    #  uchar QChar::row() const
    return self.uglySide.call('ritual_ZNK5QChar3rowEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCell(self, acell: int) -> None:
    """
    Calls Qt's 'void QChar::setCell(uchar acell)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#setCell

    Parameters
    ----------

    acell : int
      Passed on as it is.
    """
    #  void QChar::setCell(uchar acell)
    self.uglySide.call('ritual_ZN5QChar7setCellEh', acell)

  @overload(int)
  def setRow(self, arow: int) -> None:
    """
    Calls Qt's 'void QChar::setRow(uchar arow)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#setRow

    Parameters
    ----------

    arow : int
      Passed on as it is.
    """
    #  void QChar::setRow(uchar arow)
    self.uglySide.call('ritual_ZN5QChar6setRowEh', arow)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator==(const QChar &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#operator==

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator==(const QChar &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZeqRK5QCharS1_',
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
  def __ne__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator!=(const QChar &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#operator!=

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator!=(const QChar &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZneRK5QCharS1_',
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

  @overload(THIS)
  def __lt__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator<(const QChar &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#operator<

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator<(const QChar &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZltRK5QCharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator>(const QChar &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#operator>

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator>(const QChar &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZgtRK5QCharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator<=(const QChar &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#operator<=

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator<=(const QChar &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZleRK5QCharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator>=(const QChar &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#operator>=

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator>=(const QChar &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZgeRK5QCharS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QChar::QChar()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#QChar
    """
    #  QChar::QChar()
    self._noteCreation(QChar, lambda: Rituals.call('ritual_ZN5QCharC1Ev'))

  @overload(int, int)
  def __init__(self, c: int, r: int) -> None:
    """
    Notes what was given, for Qt's 'QChar::QChar(uchar c, uchar r)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qchar.html#QChar

    Parameters
    ----------

    c : int
      Passed on as it is.

    r : int
      Passed on as it is.
    """
    #  QChar::QChar(uchar c, uchar r)
    self._noteCreation(QChar, lambda: Rituals.call(
        'ritual_ZN5QCharC1Ehh', c, r,
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
