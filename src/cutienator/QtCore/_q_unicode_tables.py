"""
QUnicodeTables stands for the namespace 'QUnicodeTables' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QUnicodeTables:
  """
  The namespace 'QUnicodeTables' of Qt, which holds no objects. It holds the
  8 enums Qt writes in it, each under its name, and the 0 names Qt has for
  the combinations of a flags enum, each holding the class of that enum. It
  is never made into an object.
  """

  class Case(CuteNum):
    """
    The enum 'QUnicodeTables::Case' of Qt, with the 5 names Qt gives in it.
    """

    LowerCase = Kee[int](0)
    UpperCase = Kee[int](1)
    TitleCase = Kee[int](2)
    CaseFold = Kee[int](3)
    NumCases = Kee[int](4)

  class EastAsianWidth(CuteNum, scoped=True):
    """
    The enum 'QUnicodeTables::EastAsianWidth' of Qt, with the 6 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    A = Kee[int](0)
    F = Kee[int](1)
    H = Kee[int](2)
    N = Kee[int](3)
    Na = Kee[int](4)
    W = Kee[int](5)

  class EmojiFlags(CuteNum, scoped=True):
    """
    The enum 'QUnicodeTables::EmojiFlags' of Qt, with the 6 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoEmoji = Kee[int](0)
    Emoji = Kee[int](1)
    Emoji_Presentation = Kee[int](2)
    Emoji_Modifier = Kee[int](4)
    Emoji_Modifier_Base = Kee[int](8)
    Emoji_Component = Kee[int](16)

  class GraphemeBreakClass(CuteNum):
    """
    The enum 'QUnicodeTables::GraphemeBreakClass' of Qt, with the 16 names Qt
    gives in it.
    """

    GraphemeBreak_Any = Kee[int](0)
    GraphemeBreak_CR = Kee[int](1)
    GraphemeBreak_LF = Kee[int](2)
    GraphemeBreak_Control = Kee[int](3)
    GraphemeBreak_Extend = Kee[int](4)
    GraphemeBreak_ZWJ = Kee[int](5)
    GraphemeBreak_RegionalIndicator = Kee[int](6)
    GraphemeBreak_Prepend = Kee[int](7)
    GraphemeBreak_SpacingMark = Kee[int](8)
    GraphemeBreak_L = Kee[int](9)
    GraphemeBreak_V = Kee[int](10)
    GraphemeBreak_T = Kee[int](11)
    GraphemeBreak_LV = Kee[int](12)
    GraphemeBreak_LVT = Kee[int](13)
    GraphemeBreak_Extended_Pictographic = Kee[int](14)
    NumGraphemeBreakClasses = Kee[int](15)

  class IdnaStatus(CuteNum, scoped=True):
    """
    The enum 'QUnicodeTables::IdnaStatus' of Qt, with the 5 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Disallowed = Kee[int](0)
    Valid = Kee[int](1)
    Ignored = Kee[int](2)
    Mapped = Kee[int](3)
    Deviation = Kee[int](4)

  class LineBreakClass(CuteNum):
    """
    The enum 'QUnicodeTables::LineBreakClass' of Qt, with the 52 names Qt
    gives in it.
    """

    LineBreak_OP = Kee[int](0)
    LineBreak_CL = Kee[int](1)
    LineBreak_CP = Kee[int](2)
    LineBreak_QU = Kee[int](3)
    LineBreak_QU_Pi = Kee[int](4)
    LineBreak_QU_Pf = Kee[int](5)
    LineBreak_QU_19 = Kee[int](6)
    LineBreak_GL = Kee[int](7)
    LineBreak_NS = Kee[int](8)
    LineBreak_EX = Kee[int](9)
    LineBreak_SY = Kee[int](10)
    LineBreak_IS = Kee[int](11)
    LineBreak_PR = Kee[int](12)
    LineBreak_PO = Kee[int](13)
    LineBreak_NU = Kee[int](14)
    LineBreak_AL = Kee[int](15)
    LineBreak_HL = Kee[int](16)
    LineBreak_ID = Kee[int](17)
    LineBreak_IN = Kee[int](18)
    LineBreak_HY = Kee[int](19)
    LineBreak_WS_HY = Kee[int](20)
    LineBreak_HH = Kee[int](21)
    LineBreak_BA = Kee[int](22)
    LineBreak_WS_BA = Kee[int](23)
    LineBreak_HYBA = Kee[int](24)
    LineBreak_BB = Kee[int](25)
    LineBreak_B2 = Kee[int](26)
    LineBreak_ZW = Kee[int](27)
    LineBreak_CM = Kee[int](28)
    LineBreak_WJ = Kee[int](29)
    LineBreak_H2 = Kee[int](30)
    LineBreak_H3 = Kee[int](31)
    LineBreak_JL = Kee[int](32)
    LineBreak_JV = Kee[int](33)
    LineBreak_JT = Kee[int](34)
    LineBreak_RI = Kee[int](35)
    LineBreak_CB = Kee[int](36)
    LineBreak_EB = Kee[int](37)
    LineBreak_EM = Kee[int](38)
    LineBreak_AK = Kee[int](39)
    LineBreak_AP = Kee[int](40)
    LineBreak_AS = Kee[int](41)
    LineBreak_VI = Kee[int](42)
    LineBreak_VF = Kee[int](43)
    LineBreak_ZWJ = Kee[int](44)
    LineBreak_SA = Kee[int](45)
    LineBreak_SG = Kee[int](46)
    LineBreak_SP = Kee[int](47)
    LineBreak_CR = Kee[int](48)
    LineBreak_LF = Kee[int](49)
    LineBreak_BK = Kee[int](50)
    NumLineBreakClasses = Kee[int](51)

  class SentenceBreakClass(CuteNum):
    """
    The enum 'QUnicodeTables::SentenceBreakClass' of Qt, with the 15 names Qt
    gives in it.
    """

    SentenceBreak_Any = Kee[int](0)
    SentenceBreak_CR = Kee[int](1)
    SentenceBreak_LF = Kee[int](2)
    SentenceBreak_Sep = Kee[int](3)
    SentenceBreak_Extend = Kee[int](4)
    SentenceBreak_Sp = Kee[int](5)
    SentenceBreak_Lower = Kee[int](6)
    SentenceBreak_Upper = Kee[int](7)
    SentenceBreak_OLetter = Kee[int](8)
    SentenceBreak_Numeric = Kee[int](9)
    SentenceBreak_ATerm = Kee[int](10)
    SentenceBreak_SContinue = Kee[int](11)
    SentenceBreak_STerm = Kee[int](12)
    SentenceBreak_Close = Kee[int](13)
    NumSentenceBreakClasses = Kee[int](14)

  class WordBreakClass(CuteNum):
    """
    The enum 'QUnicodeTables::WordBreakClass' of Qt, with the 20 names Qt
    gives in it.
    """

    WordBreak_Any = Kee[int](0)
    WordBreak_CR = Kee[int](1)
    WordBreak_LF = Kee[int](2)
    WordBreak_Newline = Kee[int](3)
    WordBreak_Extend = Kee[int](4)
    WordBreak_ZWJ = Kee[int](5)
    WordBreak_Format = Kee[int](6)
    WordBreak_RegionalIndicator = Kee[int](7)
    WordBreak_Katakana = Kee[int](8)
    WordBreak_HebrewLetter = Kee[int](9)
    WordBreak_ALetter = Kee[int](10)
    WordBreak_SingleQuote = Kee[int](11)
    WordBreak_DoubleQuote = Kee[int](12)
    WordBreak_MidNumLet = Kee[int](13)
    WordBreak_MidLetter = Kee[int](14)
    WordBreak_MidNum = Kee[int](15)
    WordBreak_Numeric = Kee[int](16)
    WordBreak_ExtendNumLet = Kee[int](17)
    WordBreak_WSegSpace = Kee[int](18)
    NumWordBreakClasses = Kee[int](19)
