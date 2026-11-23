"""
QTextFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from . import QBrush, QColor, QPen, QTextBlockFormat, QTextCharFormat
  from . import QTextFrameFormat, QTextImageFormat, QTextLength
  from . import QTextListFormat, QTextTableCellFormat, QTextTableFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QTextLength = WAIT['QTextLength']
  QVariant = WAIT['QVariant']


class QTextFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextFormat: a plain Python object standing in front
  of one C++ QTextFormat.

  C++ hands a QTextFormat around as a copy, so every C++ QTextFormat behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextFormat that has a ritual and that Python can
  call so far, 47 names in all: 'merge', 'isValid', 'isEmpty', 'type',
  'objectIndex', 'setObjectIndex', 'property', 'setProperty',
  'clearProperty', 'hasProperty', 'boolProperty', 'intProperty',
  'doubleProperty', 'stringProperty', 'colorProperty', 'penProperty',
  'brushProperty', 'lengthProperty', 'lengthVectorProperty', 'properties',
  'propertyCount', 'setObjectType', 'objectType', 'isCharFormat',
  'isBlockFormat', 'isListFormat', 'isFrameFormat', 'isImageFormat',
  'isTableFormat', 'isTableCellFormat', 'toBlockFormat', 'toCharFormat',
  'toListFormat', 'toTableFormat', 'toFrameFormat', 'toImageFormat',
  'toTableCellFormat', '__eq__', '__ne__', 'setLayoutDirection',
  'layoutDirection', 'setBackground', 'background', 'clearBackground',
  'setForeground', 'foreground', 'clearForeground'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextFormat::~QTextFormat()': the destructor: Python removes its
    C++ QTextFormat by it, and has no other use for it.
  - Qt's 'QVariant QTextFormat::operator QVariant() const': an operator
    Python has no name for.

  What has no ritual
  ------------------

  7 of the 60 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QTextFormat is created at the first use, not by
    'QTextFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextFormat back gives a copy the ritual made for
    Python, in a new cute QTextFormat.
  """

  #  The enums Qt writes inside QTextFormat, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class FormatType(CuteNum):
    """
    The enum 'QTextFormat::FormatType' of Qt, with the 6 names Qt gives in
    it.
    """

    InvalidFormat = Kee[int](-1)
    BlockFormat = Kee[int](1)
    CharFormat = Kee[int](2)
    ListFormat = Kee[int](3)
    FrameFormat = Kee[int](5)
    UserFormat = Kee[int](100)

  class ObjectTypes(CuteNum):
    """
    The enum 'QTextFormat::ObjectTypes' of Qt, with the 5 names Qt gives in
    it.
    """

    NoObject = Kee[int](0)
    ImageObject = Kee[int](1)
    TableObject = Kee[int](2)
    TableCellObject = Kee[int](3)
    UserObject = Kee[int](4096)

  class PageBreakFlag(CuteFlags):
    """
    The flags enum 'QTextFormat::PageBreakFlag' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QTextFormat::PageBreakFlags'.
    """

    PageBreak_Auto = 0x0
    PageBreak_AlwaysBefore = 0x1
    PageBreak_AlwaysAfter = 0x10

  PageBreakFlags = PageBreakFlag

  class Property(CuteNum):
    """
    The enum 'QTextFormat::Property' of Qt, with the 116 names Qt gives in
    it.
    """

    ObjectIndex = Kee[int](0)
    CssFloat = Kee[int](2048)
    LayoutDirection = Kee[int](2049)
    OutlinePen = Kee[int](2064)
    BackgroundBrush = Kee[int](2080)
    ForegroundBrush = Kee[int](2081)
    BackgroundImageUrl = Kee[int](2083)
    BlockAlignment = Kee[int](4112)
    BlockTopMargin = Kee[int](4144)
    BlockBottomMargin = Kee[int](4145)
    BlockLeftMargin = Kee[int](4146)
    BlockRightMargin = Kee[int](4147)
    TextIndent = Kee[int](4148)
    TabPositions = Kee[int](4149)
    BlockIndent = Kee[int](4160)
    LineHeight = Kee[int](4168)
    LineHeightType = Kee[int](4169)
    BlockNonBreakableLines = Kee[int](4176)
    BlockTrailingHorizontalRulerWidth = Kee[int](4192)
    HeadingLevel = Kee[int](4208)
    BlockQuoteLevel = Kee[int](4224)
    BlockCodeLanguage = Kee[int](4240)
    BlockCodeFence = Kee[int](4241)
    BlockMarker = Kee[int](4256)
    FirstFontProperty = Kee[int](8160)
    FontCapitalization = Kee[int](8160)
    FontLetterSpacing = Kee[int](8161)
    FontWordSpacing = Kee[int](8162)
    FontStyleHint = Kee[int](8163)
    FontStyleStrategy = Kee[int](8164)
    FontKerning = Kee[int](8165)
    FontHintingPreference = Kee[int](8166)
    FontFamilies = Kee[int](8167)
    FontStyleName = Kee[int](8168)
    FontLetterSpacingType = Kee[int](8169)
    FontStretch = Kee[int](8170)
    FontFamily = Kee[int](8192)
    FontPointSize = Kee[int](8193)
    FontSizeAdjustment = Kee[int](8194)
    FontSizeIncrement = Kee[int](8194)
    FontWeight = Kee[int](8195)
    FontItalic = Kee[int](8196)
    FontUnderline = Kee[int](8197)
    FontOverline = Kee[int](8198)
    FontStrikeOut = Kee[int](8199)
    FontFixedPitch = Kee[int](8200)
    FontPixelSize = Kee[int](8201)
    FontFeatures = Kee[int](8208)
    FontVariableAxes = Kee[int](8209)
    LastFontProperty = Kee[int](8209)
    TextUnderlineColor = Kee[int](8224)
    TextVerticalAlignment = Kee[int](8225)
    TextOutline = Kee[int](8226)
    TextUnderlineStyle = Kee[int](8227)
    TextToolTip = Kee[int](8228)
    TextSuperScriptBaseline = Kee[int](8229)
    TextSubScriptBaseline = Kee[int](8230)
    TextBaselineOffset = Kee[int](8231)
    IsAnchor = Kee[int](8240)
    AnchorHref = Kee[int](8241)
    AnchorName = Kee[int](8242)
    OldFontLetterSpacingType = Kee[int](8243)
    OldFontStretch = Kee[int](8244)
    OldTextUnderlineColor = Kee[int](8208)
    OldFontFamily = Kee[int](8192)
    ObjectType = Kee[int](12032)
    ListStyle = Kee[int](12288)
    ListIndent = Kee[int](12289)
    ListNumberPrefix = Kee[int](12290)
    ListNumberSuffix = Kee[int](12291)
    ListStart = Kee[int](12292)
    FrameBorder = Kee[int](16384)
    FrameMargin = Kee[int](16385)
    FramePadding = Kee[int](16386)
    FrameWidth = Kee[int](16387)
    FrameHeight = Kee[int](16388)
    FrameTopMargin = Kee[int](16389)
    FrameBottomMargin = Kee[int](16390)
    FrameLeftMargin = Kee[int](16391)
    FrameRightMargin = Kee[int](16392)
    FrameBorderBrush = Kee[int](16393)
    FrameBorderStyle = Kee[int](16400)
    TableColumns = Kee[int](16640)
    TableColumnWidthConstraints = Kee[int](16641)
    TableCellSpacing = Kee[int](16642)
    TableCellPadding = Kee[int](16643)
    TableHeaderRowCount = Kee[int](16644)
    TableBorderCollapse = Kee[int](16645)
    TableCellRowSpan = Kee[int](18448)
    TableCellColumnSpan = Kee[int](18449)
    TableCellTopPadding = Kee[int](18450)
    TableCellBottomPadding = Kee[int](18451)
    TableCellLeftPadding = Kee[int](18452)
    TableCellRightPadding = Kee[int](18453)
    TableCellTopBorder = Kee[int](18454)
    TableCellBottomBorder = Kee[int](18455)
    TableCellLeftBorder = Kee[int](18456)
    TableCellRightBorder = Kee[int](18457)
    TableCellTopBorderStyle = Kee[int](18458)
    TableCellBottomBorderStyle = Kee[int](18459)
    TableCellLeftBorderStyle = Kee[int](18460)
    TableCellRightBorderStyle = Kee[int](18461)
    TableCellTopBorderBrush = Kee[int](18462)
    TableCellBottomBorderBrush = Kee[int](18463)
    TableCellLeftBorderBrush = Kee[int](18464)
    TableCellRightBorderBrush = Kee[int](18465)
    ImageName = Kee[int](20480)
    ImageTitle = Kee[int](20481)
    ImageAltText = Kee[int](20482)
    ImageWidth = Kee[int](20496)
    ImageHeight = Kee[int](20497)
    ImageQuality = Kee[int](20500)
    ImageMaxWidth = Kee[int](20501)
    FullWidthSelection = Kee[int](24576)
    PageBreakPolicy = Kee[int](28672)
    UserProperty = Kee[int](1048576)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextFormat'

  #  Qt's '~QTextFormat()'. Naming it makes this a value class: Python owns
  #  every C++ QTextFormat behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QTextFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isValid
    """
    #  bool QTextFormat::isValid() const
    return self.uglySide.call('ritual_ZNK11QTextFormat7isValidEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isEmpty
    """
    #  bool QTextFormat::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QTextFormat7isEmptyEv')

  def type(self) -> int:
    """
    Calls Qt's 'int QTextFormat::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#type
    """
    #  int QTextFormat::type() const
    return self.uglySide.call('ritual_ZNK11QTextFormat4typeEv')

  def objectIndex(self) -> int:
    """
    Calls Qt's 'int QTextFormat::objectIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#objectIndex
    """
    #  int QTextFormat::objectIndex() const
    return self.uglySide.call('ritual_ZNK11QTextFormat11objectIndexEv')

  @overload(int)
  def property(self, propertyId: int) -> QVariant:
    """
    Calls Qt's 'QVariant QTextFormat::property(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#property

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextFormat::property(int propertyId) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat8propertyEi', propertyId,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def hasProperty(self, propertyId: int) -> bool:
    """
    Calls Qt's 'bool QTextFormat::hasProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#hasProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  bool QTextFormat::hasProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat11hasPropertyEi', propertyId,
    )

  @overload(int)
  def boolProperty(self, propertyId: int) -> bool:
    """
    Calls Qt's 'bool QTextFormat::boolProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#boolProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  bool QTextFormat::boolProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat12boolPropertyEi', propertyId,
    )

  @overload(int)
  def intProperty(self, propertyId: int) -> int:
    """
    Calls Qt's 'int QTextFormat::intProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#intProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  int QTextFormat::intProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat11intPropertyEi', propertyId,
    )

  @overload(int)
  def doubleProperty(self, propertyId: int) -> float:
    """
    Calls Qt's 'qreal QTextFormat::doubleProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#doubleProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  qreal QTextFormat::doubleProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat14doublePropertyEi', propertyId,
    )

  @overload(int)
  def stringProperty(self, propertyId: int) -> str:
    """
    Calls Qt's 'QString QTextFormat::stringProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#stringProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextFormat::stringProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat14stringPropertyEi', propertyId,
    )

  @overload(int)
  def colorProperty(self, propertyId: int) -> QColor:
    """
    Calls Qt's 'QColor QTextFormat::colorProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#colorProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QTextFormat::colorProperty(int propertyId) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat13colorPropertyEi', propertyId,
    )
    from . import QColor
    return QColor._cuteOwning(address)

  @overload(int)
  def penProperty(self, propertyId: int) -> QPen:
    """
    Calls Qt's 'QPen QTextFormat::penProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#penProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QTextFormat::penProperty(int propertyId) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat11penPropertyEi', propertyId,
    )
    from . import QPen
    return QPen._cuteOwning(address)

  @overload(int)
  def brushProperty(self, propertyId: int) -> QBrush:
    """
    Calls Qt's 'QBrush QTextFormat::brushProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#brushProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextFormat::brushProperty(int propertyId) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat13brushPropertyEi', propertyId,
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  @overload(int)
  def lengthProperty(self, propertyId: int) -> QTextLength:
    """
    Calls Qt's 'QTextLength QTextFormat::lengthProperty(int propertyId)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#lengthProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QTextLength
      A new cute QTextLength around the copy Qt gave back. Python owns it.
    """
    #  QTextLength QTextFormat::lengthProperty(int propertyId) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat14lengthPropertyEi', propertyId,
    )
    from . import QTextLength
    return QTextLength._cuteOwning(address)

  @overload(int)
  def lengthVectorProperty(self, propertyId: int) -> QList[QTextLength]:
    """
    Calls Qt's 'QList<QTextLength> QTextFormat::lengthVectorProperty(int
    propertyId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformat.html#lengthVectorProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QList[QTextLength]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTextLength> QTextFormat::lengthVectorProperty(int propertyId)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat20lengthVectorPropertyEi', propertyId,
    )
    from . import QTextLength
    return QList[QTextLength]._cuteOwning(address)

  def properties(self) -> QMap[int, QVariant]:
    """
    Calls Qt's 'QMap<int, QVariant> QTextFormat::properties() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#properties

    Returns
    -------

    QMap[int, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<int, QVariant> QTextFormat::properties() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat10propertiesEv')
    from ..QtCore import QVariant
    return QMap[int, QVariant]._cuteOwning(address)

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QTextFormat::propertyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#propertyCount
    """
    #  int QTextFormat::propertyCount() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13propertyCountEv')

  def objectType(self) -> int:
    """
    Calls Qt's 'int QTextFormat::objectType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#objectType
    """
    #  int QTextFormat::objectType() const
    return self.uglySide.call('ritual_ZNK11QTextFormat10objectTypeEv')

  def isCharFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isCharFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isCharFormat
    """
    #  bool QTextFormat::isCharFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat12isCharFormatEv')

  def isBlockFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isBlockFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isBlockFormat
    """
    #  bool QTextFormat::isBlockFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13isBlockFormatEv')

  def isListFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isListFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isListFormat
    """
    #  bool QTextFormat::isListFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat12isListFormatEv')

  def isFrameFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isFrameFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isFrameFormat
    """
    #  bool QTextFormat::isFrameFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13isFrameFormatEv')

  def isImageFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isImageFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isImageFormat
    """
    #  bool QTextFormat::isImageFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13isImageFormatEv')

  def isTableFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isTableFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isTableFormat
    """
    #  bool QTextFormat::isTableFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13isTableFormatEv')

  def isTableCellFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isTableCellFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isTableCellFormat
    """
    #  bool QTextFormat::isTableCellFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat17isTableCellFormatEv')

  def toBlockFormat(self) -> QTextBlockFormat:
    """
    Calls Qt's 'QTextBlockFormat QTextFormat::toBlockFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#toBlockFormat

    Returns
    -------

    QTextBlockFormat
      A new cute QTextBlockFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextBlockFormat QTextFormat::toBlockFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat13toBlockFormatEv')
    from . import QTextBlockFormat
    return QTextBlockFormat._cuteOwning(address)

  def toCharFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextFormat::toCharFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#toCharFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextFormat::toCharFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat12toCharFormatEv')
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def toListFormat(self) -> QTextListFormat:
    """
    Calls Qt's 'QTextListFormat QTextFormat::toListFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#toListFormat

    Returns
    -------

    QTextListFormat
      A new cute QTextListFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextListFormat QTextFormat::toListFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat12toListFormatEv')
    from . import QTextListFormat
    return QTextListFormat._cuteOwning(address)

  def toTableFormat(self) -> QTextTableFormat:
    """
    Calls Qt's 'QTextTableFormat QTextFormat::toTableFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#toTableFormat

    Returns
    -------

    QTextTableFormat
      A new cute QTextTableFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextTableFormat QTextFormat::toTableFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat13toTableFormatEv')
    from . import QTextTableFormat
    return QTextTableFormat._cuteOwning(address)

  def toFrameFormat(self) -> QTextFrameFormat:
    """
    Calls Qt's 'QTextFrameFormat QTextFormat::toFrameFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#toFrameFormat

    Returns
    -------

    QTextFrameFormat
      A new cute QTextFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextFrameFormat QTextFormat::toFrameFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat13toFrameFormatEv')
    from . import QTextFrameFormat
    return QTextFrameFormat._cuteOwning(address)

  def toImageFormat(self) -> QTextImageFormat:
    """
    Calls Qt's 'QTextImageFormat QTextFormat::toImageFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#toImageFormat

    Returns
    -------

    QTextImageFormat
      A new cute QTextImageFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextImageFormat QTextFormat::toImageFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat13toImageFormatEv')
    from . import QTextImageFormat
    return QTextImageFormat._cuteOwning(address)

  def toTableCellFormat(self) -> QTextTableCellFormat:
    """
    Calls Qt's 'QTextTableCellFormat QTextFormat::toTableCellFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#toTableCellFormat

    Returns
    -------

    QTextTableCellFormat
      A new cute QTextTableCellFormat around the copy Qt gave back. Python
      owns it.
    """
    #  QTextTableCellFormat QTextFormat::toTableCellFormat() const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat17toTableCellFormatEv',
    )
    from . import QTextTableCellFormat
    return QTextTableCellFormat._cuteOwning(address)

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QTextFormat::layoutDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QTextFormat::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK11QTextFormat15layoutDirectionEv',
    ))

  def background(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTextFormat::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#background

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextFormat::background() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat10backgroundEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def foreground(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTextFormat::foreground() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#foreground

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextFormat::foreground() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat10foregroundEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setObjectIndex(self, object: int) -> None:
    """
    Calls Qt's 'void QTextFormat::setObjectIndex(int object)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setObjectIndex

    Parameters
    ----------

    object : int
      Passed on as it is.
    """
    #  void QTextFormat::setObjectIndex(int object)
    self.uglySide.call('ritual_ZN11QTextFormat14setObjectIndexEi', object)

  @overload(int, QVariant)
  def setProperty(self, propertyId: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QTextFormat::setProperty(int propertyId, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QTextFormat::setProperty(int propertyId, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN11QTextFormat11setPropertyEiRK8QVariant',
        propertyId, self._valueOf(value),
    )

  @overload(int, QList[QTextLength])
  def setProperty(
      self,
      propertyId: int,
      lengths: QList[QTextLength],
  ) -> None:
    """
    Calls Qt's 'void QTextFormat::setProperty(int propertyId, const
    QList<QTextLength> &lengths)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    lengths : QList[QTextLength]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTextFormat::setProperty(int propertyId, const QList<QTextLength>
    #      &lengths)
    self.uglySide.call(
        'ritual_ZN11QTextFormat11setPropertyEiRK5QListI11QTextLengthE',
        propertyId, self._valueOf(lengths),
    )

  @overload(int)
  def setObjectType(self, type: int) -> None:
    """
    Calls Qt's 'void QTextFormat::setObjectType(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setObjectType

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  void QTextFormat::setObjectType(int type)
    self.uglySide.call('ritual_ZN11QTextFormat13setObjectTypeEi', type)

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QTextFormat::setLayoutDirection(Qt::LayoutDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformat.html#setLayoutDirection

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QTextFormat::setLayoutDirection(Qt::LayoutDirection direction)
    self.uglySide.call(
        'ritual_ZN11QTextFormat18setLayoutDirectionEN2Qt15LayoutDirectionE',
        direction.value,
    )

  @overload(QBrush)
  def setBackground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextFormat::setBackground(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setBackground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextFormat::setBackground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN11QTextFormat13setBackgroundERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setForeground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextFormat::setForeground(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setForeground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextFormat::setForeground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN11QTextFormat13setForegroundERK6QBrush',
        self._valueOf(brush),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QTextFormat) -> bool:
    """
    Calls Qt's 'bool QTextFormat::operator==(const QTextFormat &rhs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#operator==

    Parameters
    ----------

    rhs : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  bool QTextFormat::operator==(const QTextFormat &rhs) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormateqERKS_', self._valueOf(rhs),
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
  def __ne__(self, rhs: QTextFormat) -> bool:
    """
    Calls Qt's 'bool QTextFormat::operator!=(const QTextFormat &rhs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#operator!=

    Parameters
    ----------

    rhs : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  bool QTextFormat::operator!=(const QTextFormat &rhs) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormatneERKS_', self._valueOf(rhs),
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
    Notes what was given, for Qt's 'QTextFormat::QTextFormat()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#QTextFormat
    """
    #  QTextFormat::QTextFormat()
    self._noteCreation(QTextFormat, lambda: Rituals.call(
        'ritual_ZN11QTextFormatC1Ev',
    ))

  @overload(int)
  def __init__(self, type: int) -> None:
    """
    Notes what was given, for Qt's 'QTextFormat::QTextFormat(int type)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#QTextFormat

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  QTextFormat::QTextFormat(int type)
    self._noteCreation(QTextFormat, lambda: Rituals.call(
        'ritual_ZN11QTextFormatC1Ei', type,
    ))

  @overload(THIS)
  def __init__(self, rhs: QTextFormat) -> None:
    """
    Notes what was given, for Qt's 'QTextFormat::QTextFormat(const
    QTextFormat &rhs)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#QTextFormat

    Parameters
    ----------

    rhs : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  QTextFormat::QTextFormat(const QTextFormat &rhs)
    self._noteCreation(QTextFormat, lambda: Rituals.call(
        'ritual_ZN11QTextFormatC1ERKS_', self._valueOf(rhs),
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

  @overload(THIS)
  def merge(self, other: QTextFormat) -> None:
    """
    Calls Qt's 'void QTextFormat::merge(const QTextFormat &other)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#merge

    Parameters
    ----------

    other : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QTextFormat::merge(const QTextFormat &other)
    self.uglySide.call(
        'ritual_ZN11QTextFormat5mergeERKS_', self._valueOf(other),
    )

  @overload(int)
  def clearProperty(self, propertyId: int) -> None:
    """
    Calls Qt's 'void QTextFormat::clearProperty(int propertyId)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#clearProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  void QTextFormat::clearProperty(int propertyId)
    self.uglySide.call('ritual_ZN11QTextFormat13clearPropertyEi', propertyId)

  def clearBackground(self) -> None:
    """
    Calls Qt's 'void QTextFormat::clearBackground()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#clearBackground
    """
    #  void QTextFormat::clearBackground()
    self.uglySide.call('ritual_ZN11QTextFormat15clearBackgroundEv')

  def clearForeground(self) -> None:
    """
    Calls Qt's 'void QTextFormat::clearForeground()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#clearForeground
    """
    #  void QTextFormat::clearForeground()
    self.uglySide.call('ritual_ZN11QTextFormat15clearForegroundEv')


#  Qt's 'QList<QTextFormat>': the list of QTextFormat, which
#  'QList[QTextFormat]' gives. It is made here, so that there is one as soon
#  as there can be a QTextFormat.
QList.createKind(
    QTextFormat, 'value',
    make='ritual_list_make_QTextFormat',
    add='ritual_list_add_QTextFormat',
    size='ritual_list_size_QTextFormat',
    at='ritual_list_at_QTextFormat',
    drop='ritual_list_drop_QTextFormat',
)
