"""
QCss stands for the namespace 'QCss' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QCss:
  """
  The namespace 'QCss' of Qt, which holds no objects. It holds the 12 enums
  Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class Attachment(CuteNum):
    """The enum 'QCss::Attachment' of Qt, with the 3 names Qt gives in it."""

    Attachment_Unknown = Kee[int](0)
    Attachment_Fixed = Kee[int](1)
    Attachment_Scroll = Kee[int](2)

  class BorderStyle(CuteNum):
    """
    The enum 'QCss::BorderStyle' of Qt, with the 13 names Qt gives in it.
    """

    BorderStyle_Unknown = Kee[int](0)
    BorderStyle_None = Kee[int](1)
    BorderStyle_Dotted = Kee[int](2)
    BorderStyle_Dashed = Kee[int](3)
    BorderStyle_Solid = Kee[int](4)
    BorderStyle_Double = Kee[int](5)
    BorderStyle_DotDash = Kee[int](6)
    BorderStyle_DotDotDash = Kee[int](7)
    BorderStyle_Groove = Kee[int](8)
    BorderStyle_Ridge = Kee[int](9)
    BorderStyle_Inset = Kee[int](10)
    BorderStyle_Outset = Kee[int](11)
    BorderStyle_Native = Kee[int](12)

  class Edge(CuteNum):
    """The enum 'QCss::Edge' of Qt, with the 5 names Qt gives in it."""

    TopEdge = Kee[int](0)
    RightEdge = Kee[int](1)
    BottomEdge = Kee[int](2)
    LeftEdge = Kee[int](3)
    NumEdges = Kee[int](4)

  class KnownValue(CuteNum):
    """
    The enum 'QCss::KnownValue' of Qt, with the 88 names Qt gives in it.
    """

    UnknownValue = Kee[int](0)
    Value_Normal = Kee[int](1)
    Value_Pre = Kee[int](2)
    Value_NoWrap = Kee[int](3)
    Value_PreLine = Kee[int](4)
    Value_PreWrap = Kee[int](5)
    Value_Small = Kee[int](6)
    Value_Medium = Kee[int](7)
    Value_Large = Kee[int](8)
    Value_XLarge = Kee[int](9)
    Value_XXLarge = Kee[int](10)
    Value_Italic = Kee[int](11)
    Value_Oblique = Kee[int](12)
    Value_Bold = Kee[int](13)
    Value_Underline = Kee[int](14)
    Value_Overline = Kee[int](15)
    Value_LineThrough = Kee[int](16)
    Value_Sub = Kee[int](17)
    Value_Super = Kee[int](18)
    Value_Left = Kee[int](19)
    Value_Right = Kee[int](20)
    Value_Top = Kee[int](21)
    Value_Bottom = Kee[int](22)
    Value_Center = Kee[int](23)
    Value_Native = Kee[int](24)
    Value_Solid = Kee[int](25)
    Value_Dotted = Kee[int](26)
    Value_Dashed = Kee[int](27)
    Value_DotDash = Kee[int](28)
    Value_DotDotDash = Kee[int](29)
    Value_Double = Kee[int](30)
    Value_Groove = Kee[int](31)
    Value_Ridge = Kee[int](32)
    Value_Inset = Kee[int](33)
    Value_Outset = Kee[int](34)
    Value_Wave = Kee[int](35)
    Value_Middle = Kee[int](36)
    Value_Auto = Kee[int](37)
    Value_Always = Kee[int](38)
    Value_None = Kee[int](39)
    Value_Transparent = Kee[int](40)
    Value_Disc = Kee[int](41)
    Value_Circle = Kee[int](42)
    Value_Square = Kee[int](43)
    Value_Decimal = Kee[int](44)
    Value_LowerAlpha = Kee[int](45)
    Value_UpperAlpha = Kee[int](46)
    Value_LowerRoman = Kee[int](47)
    Value_UpperRoman = Kee[int](48)
    Value_SmallCaps = Kee[int](49)
    Value_Uppercase = Kee[int](50)
    Value_Lowercase = Kee[int](51)
    Value_SquareCap = Kee[int](52)
    Value_FlatCap = Kee[int](53)
    Value_RoundCap = Kee[int](54)
    Value_MiterJoin = Kee[int](55)
    Value_BevelJoin = Kee[int](56)
    Value_RoundJoin = Kee[int](57)
    Value_SvgMiterJoin = Kee[int](58)
    Value_FirstColorRole = Kee[int](59)
    Value_WindowText = Kee[int](59)
    Value_Button = Kee[int](60)
    Value_Light = Kee[int](61)
    Value_Midlight = Kee[int](62)
    Value_Dark = Kee[int](63)
    Value_Mid = Kee[int](64)
    Value_Text = Kee[int](65)
    Value_BrightText = Kee[int](66)
    Value_ButtonText = Kee[int](67)
    Value_Base = Kee[int](68)
    Value_Window = Kee[int](69)
    Value_Shadow = Kee[int](70)
    Value_Highlight = Kee[int](71)
    Value_HighlightedText = Kee[int](72)
    Value_Link = Kee[int](73)
    Value_LinkVisited = Kee[int](74)
    Value_AlternateBase = Kee[int](75)
    Value_NoRole = Kee[int](76)
    Value_ToolTipBase = Kee[int](77)
    Value_ToolTipText = Kee[int](78)
    Value_PlaceholderText = Kee[int](79)
    Value_Accent = Kee[int](80)
    Value_LastColorRole = Kee[int](80)
    Value_Disabled = Kee[int](81)
    Value_Active = Kee[int](82)
    Value_Selected = Kee[int](83)
    Value_On = Kee[int](84)
    Value_Off = Kee[int](85)

  class Origin(CuteNum):
    """The enum 'QCss::Origin' of Qt, with the 5 names Qt gives in it."""

    Origin_Unknown = Kee[int](0)
    Origin_Padding = Kee[int](1)
    Origin_Border = Kee[int](2)
    Origin_Content = Kee[int](3)
    Origin_Margin = Kee[int](4)

  class PositionMode(CuteNum):
    """
    The enum 'QCss::PositionMode' of Qt, with the 5 names Qt gives in it.
    """

    PositionMode_Unknown = Kee[int](0)
    PositionMode_Static = Kee[int](1)
    PositionMode_Relative = Kee[int](2)
    PositionMode_Absolute = Kee[int](3)
    PositionMode_Fixed = Kee[int](4)

  class Property(CuteNum):
    """The enum 'QCss::Property' of Qt, with the 121 names Qt gives in it."""

    UnknownProperty = Kee[int](0)
    BackgroundColor = Kee[int](1)
    Color = Kee[int](2)
    Float = Kee[int](3)
    Font = Kee[int](4)
    FontFamily = Kee[int](5)
    FontSize = Kee[int](6)
    FontStyle = Kee[int](7)
    FontWeight = Kee[int](8)
    Margin = Kee[int](9)
    MarginBottom = Kee[int](10)
    MarginLeft = Kee[int](11)
    MarginRight = Kee[int](12)
    MarginTop = Kee[int](13)
    QtBlockIndent = Kee[int](14)
    QtListIndent = Kee[int](15)
    QtParagraphType = Kee[int](16)
    QtTableType = Kee[int](17)
    QtUserState = Kee[int](18)
    TextDecoration = Kee[int](19)
    TextIndent = Kee[int](20)
    TextUnderlineStyle = Kee[int](21)
    VerticalAlignment = Kee[int](22)
    Whitespace = Kee[int](23)
    QtSelectionForeground = Kee[int](24)
    QtSelectionBackground = Kee[int](25)
    Border = Kee[int](26)
    BorderLeft = Kee[int](27)
    BorderRight = Kee[int](28)
    BorderTop = Kee[int](29)
    BorderBottom = Kee[int](30)
    BorderCollapse = Kee[int](31)
    Padding = Kee[int](32)
    PaddingLeft = Kee[int](33)
    PaddingRight = Kee[int](34)
    PaddingTop = Kee[int](35)
    PaddingBottom = Kee[int](36)
    PageBreakBefore = Kee[int](37)
    PageBreakAfter = Kee[int](38)
    QtAlternateBackground = Kee[int](39)
    BorderLeftStyle = Kee[int](40)
    BorderRightStyle = Kee[int](41)
    BorderTopStyle = Kee[int](42)
    BorderBottomStyle = Kee[int](43)
    BorderStyles = Kee[int](44)
    BorderLeftColor = Kee[int](45)
    BorderRightColor = Kee[int](46)
    BorderTopColor = Kee[int](47)
    BorderBottomColor = Kee[int](48)
    BorderColor = Kee[int](49)
    BorderLeftWidth = Kee[int](50)
    BorderRightWidth = Kee[int](51)
    BorderTopWidth = Kee[int](52)
    BorderBottomWidth = Kee[int](53)
    BorderWidth = Kee[int](54)
    BorderTopLeftRadius = Kee[int](55)
    BorderTopRightRadius = Kee[int](56)
    BorderBottomLeftRadius = Kee[int](57)
    BorderBottomRightRadius = Kee[int](58)
    BorderRadius = Kee[int](59)
    Background = Kee[int](60)
    BackgroundOrigin = Kee[int](61)
    BackgroundClip = Kee[int](62)
    BackgroundRepeat = Kee[int](63)
    BackgroundPosition = Kee[int](64)
    BackgroundAttachment = Kee[int](65)
    BackgroundImage = Kee[int](66)
    BorderImage = Kee[int](67)
    QtSpacing = Kee[int](68)
    Width = Kee[int](69)
    Height = Kee[int](70)
    MinimumWidth = Kee[int](71)
    MinimumHeight = Kee[int](72)
    MaximumWidth = Kee[int](73)
    MaximumHeight = Kee[int](74)
    QtImage = Kee[int](75)
    Left = Kee[int](76)
    Right = Kee[int](77)
    Top = Kee[int](78)
    Bottom = Kee[int](79)
    QtOrigin = Kee[int](80)
    QtPosition = Kee[int](81)
    Position = Kee[int](82)
    QtStyleFeatures = Kee[int](83)
    QtBackgroundRole = Kee[int](84)
    ListStyleType = Kee[int](85)
    ListStyle = Kee[int](86)
    QtImageAlignment = Kee[int](87)
    TextAlignment = Kee[int](88)
    Outline = Kee[int](89)
    OutlineOffset = Kee[int](90)
    OutlineWidth = Kee[int](91)
    OutlineColor = Kee[int](92)
    OutlineStyle = Kee[int](93)
    OutlineRadius = Kee[int](94)
    OutlineTopLeftRadius = Kee[int](95)
    OutlineTopRightRadius = Kee[int](96)
    OutlineBottomLeftRadius = Kee[int](97)
    OutlineBottomRightRadius = Kee[int](98)
    FontVariant = Kee[int](99)
    TextTransform = Kee[int](100)
    QtListNumberPrefix = Kee[int](101)
    QtListNumberSuffix = Kee[int](102)
    LineHeight = Kee[int](103)
    QtLineHeightType = Kee[int](104)
    FontKerning = Kee[int](105)
    QtForegroundTextureCacheKey = Kee[int](106)
    QtIcon = Kee[int](107)
    LetterSpacing = Kee[int](108)
    WordSpacing = Kee[int](109)
    TextDecorationColor = Kee[int](110)
    QtPlaceHolderTextColor = Kee[int](111)
    QtAccent = Kee[int](112)
    QtStrokeWidth = Kee[int](113)
    QtStrokeColor = Kee[int](114)
    QtStrokeLineCap = Kee[int](115)
    QtStrokeLineJoin = Kee[int](116)
    QtStrokeMiterLimit = Kee[int](117)
    QtStrokeDashArray = Kee[int](118)
    QtStrokeDashOffset = Kee[int](119)
    QtForeground = Kee[int](120)

  class Repeat(CuteNum):
    """The enum 'QCss::Repeat' of Qt, with the 5 names Qt gives in it."""

    Repeat_Unknown = Kee[int](0)
    Repeat_None = Kee[int](1)
    Repeat_X = Kee[int](2)
    Repeat_Y = Kee[int](3)
    Repeat_XY = Kee[int](4)

  class StyleFeature(CuteNum):
    """
    The enum 'QCss::StyleFeature' of Qt, with the 3 names Qt gives in it.
    """

    StyleFeature_None = Kee[int](0)
    StyleFeature_BackgroundColor = Kee[int](1)
    StyleFeature_BackgroundGradient = Kee[int](2)

  class StyleSheetOrigin(CuteNum):
    """
    The enum 'QCss::StyleSheetOrigin' of Qt, with the 5 names Qt gives in it.
    """

    StyleSheetOrigin_Unspecified = Kee[int](0)
    StyleSheetOrigin_UserAgent = Kee[int](1)
    StyleSheetOrigin_User = Kee[int](2)
    StyleSheetOrigin_Author = Kee[int](3)
    StyleSheetOrigin_Inline = Kee[int](4)

  class TileMode(CuteNum):
    """The enum 'QCss::TileMode' of Qt, with the 4 names Qt gives in it."""

    TileMode_Unknown = Kee[int](0)
    TileMode_Round = Kee[int](1)
    TileMode_Stretch = Kee[int](2)
    TileMode_Repeat = Kee[int](3)

  class TokenType(CuteNum):
    """The enum 'QCss::TokenType' of Qt, with the 37 names Qt gives in it."""

    NONE = Kee[int](0)
    S = Kee[int](1)
    CDO = Kee[int](2)
    CDC = Kee[int](3)
    INCLUDES = Kee[int](4)
    DASHMATCH = Kee[int](5)
    BEGINSWITH = Kee[int](6)
    ENDSWITH = Kee[int](7)
    CONTAINS = Kee[int](8)
    LBRACE = Kee[int](9)
    PLUS = Kee[int](10)
    GREATER = Kee[int](11)
    COMMA = Kee[int](12)
    TILDE = Kee[int](13)
    STRING = Kee[int](14)
    INVALID = Kee[int](15)
    IDENT = Kee[int](16)
    HASH = Kee[int](17)
    ATKEYWORD_SYM = Kee[int](18)
    EXCLAMATION_SYM = Kee[int](19)
    LENGTH = Kee[int](20)
    PERCENTAGE = Kee[int](21)
    NUMBER = Kee[int](22)
    FUNCTION = Kee[int](23)
    COLON = Kee[int](24)
    SEMICOLON = Kee[int](25)
    RBRACE = Kee[int](26)
    SLASH = Kee[int](27)
    MINUS = Kee[int](28)
    DOT = Kee[int](29)
    STAR = Kee[int](30)
    LBRACKET = Kee[int](31)
    RBRACKET = Kee[int](32)
    EQUAL = Kee[int](33)
    LPAREN = Kee[int](34)
    RPAREN = Kee[int](35)
    OR = Kee[int](36)
