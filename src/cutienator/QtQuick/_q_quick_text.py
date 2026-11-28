"""
QQuickText binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickText to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickImplicitSizeItem, QQuickItem, QQuickTextInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSizeF, QUrl, QVariant
  from ..QtGui import QColor, QFont, QHoverEvent, QMouseEvent
  from ..QtQml import QJSValue
  from . import QQuickTextLine, QQuickTextPrivate, QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QHoverEvent = WAIT['QHoverEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickTextLine = WAIT['QQuickTextLine']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickText(QQuickImplicitSizeItem, QQuickTextInterface):
  """
  The cute side of Qt's QQuickText: a plain Python object standing in front
  of one C++ QQuickText.

  It is built on the cute 'QQuickImplicitSizeItem', as Qt's QQuickText is
  built on Qt's QQuickImplicitSizeItem, and has everything that class has. It
  is built on the cute 'QQuickTextInterface' as well, as Qt's QQuickText is
  built on Qt's QQuickTextInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickText that has a ritual and that Python can
  call so far, 126 names in all: 'metaObject', 'tr', 'text', 'setText',
  'font', 'setFont', 'color', 'setColor', 'linkColor', 'setLinkColor',
  'style', 'setStyle', 'styleColor', 'setStyleColor', 'hAlign', 'setHAlign',
  'resetHAlign', 'effectiveHAlign', 'vAlign', 'setVAlign', 'wrapMode',
  'setWrapMode', 'lineCount', 'truncated', 'maximumLineCount',
  'setMaximumLineCount', 'resetMaximumLineCount', 'textFormat',
  'setTextFormat', 'elideMode', 'setElideMode', 'lineHeight',
  'setLineHeight', 'lineHeightMode', 'setLineHeightMode', 'baseUrl',
  'setBaseUrl', 'resetBaseUrl', 'minimumPixelSize', 'setMinimumPixelSize',
  'minimumPointSize', 'setMinimumPointSize', 'fontSizeMode',
  'setFontSizeMode', 'componentComplete', 'resourcesLoading', 'contentWidth',
  'contentHeight', 'boundingRect', 'clipRect', 'forceLayout', 'renderType',
  'setRenderType', 'renderTypeQuality', 'setRenderTypeQuality',
  'hoveredLink', 'linkAt', 'padding', 'setPadding', 'resetPadding',
  'topPadding', 'setTopPadding', 'resetTopPadding', 'leftPadding',
  'setLeftPadding', 'resetLeftPadding', 'rightPadding', 'setRightPadding',
  'resetRightPadding', 'bottomPadding', 'setBottomPadding',
  'resetBottomPadding', 'fontInfo', 'advance', 'invalidate', 'textChanged',
  'linkActivated', 'linkHovered', 'fontChanged', 'colorChanged',
  'linkColorChanged', 'styleChanged', 'styleColorChanged',
  'horizontalAlignmentChanged', 'verticalAlignmentChanged',
  'wrapModeChanged', 'lineCountChanged', 'truncatedChanged',
  'maximumLineCountChanged', 'textFormatChanged', 'elideModeChanged',
  'contentSizeChanged', 'contentWidthChanged', 'contentHeightChanged',
  'lineHeightChanged', 'lineHeightModeChanged', 'fontSizeModeChanged',
  'minimumPixelSizeChanged', 'minimumPointSizeChanged',
  'effectiveHorizontalAlignmentChanged', 'lineLaidOut', 'baseUrlChanged',
  'renderTypeChanged', 'paddingChanged', 'topPaddingChanged',
  'leftPaddingChanged', 'rightPaddingChanged', 'bottomPaddingChanged',
  'fontInfoChanged', 'renderTypeQualityChanged', 'mousePressEvent',
  'mouseReleaseEvent', 'itemChange', 'geometryChange', 'updatePaintNode',
  'updatePolish', 'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent',
  'invalidateFontCaches', 'q_updateLayout', 'triggerPreprocess',
  'loadResource', 'resourceRequestFinished', 'imageDownloadFinished',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickText::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickText::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickText::~QQuickText()': the destructor: Python never removes a
    C++ QQuickText.
  - Qt's 'QQuickText::QQuickText(QQuickTextPrivate &dd, QQuickItem *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickTextPrivate *QQuickText::d_func() const': takes in
    Python what 'QQuickTextPrivate *QQuickText::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 136 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickText is created at the first use, not by 'QQuickText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickText.
  - Qt tells when it has removed the C++ QQuickText. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickText, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class FontSizeMode(CuteNum):
    """
    The enum 'QQuickText::FontSizeMode' of Qt, with the 4 names Qt gives in
    it.
    """

    FixedSize = Kee[int](0)
    HorizontalFit = Kee[int](1)
    VerticalFit = Kee[int](2)
    Fit = Kee[int](3)

  class HAlignment(CuteNum):
    """
    The enum 'QQuickText::HAlignment' of Qt, with the 4 names Qt gives in it.
    """

    AlignLeft = Kee[int](1)
    AlignRight = Kee[int](2)
    AlignHCenter = Kee[int](4)
    AlignJustify = Kee[int](8)

  class LineHeightMode(CuteNum):
    """
    The enum 'QQuickText::LineHeightMode' of Qt, with the 2 names Qt gives in
    it.
    """

    ProportionalHeight = Kee[int](0)
    FixedHeight = Kee[int](1)

  class RenderType(CuteNum):
    """
    The enum 'QQuickText::RenderType' of Qt, with the 3 names Qt gives in it.
    """

    QtRendering = Kee[int](0)
    NativeRendering = Kee[int](1)
    CurveRendering = Kee[int](2)

  class RenderTypeQuality(CuteNum):
    """
    The enum 'QQuickText::RenderTypeQuality' of Qt, with the 5 names Qt gives
    in it.
    """

    DefaultRenderTypeQuality = Kee[int](-1)
    LowRenderTypeQuality = Kee[int](26)
    NormalRenderTypeQuality = Kee[int](52)
    HighRenderTypeQuality = Kee[int](104)
    VeryHighRenderTypeQuality = Kee[int](208)

  class TextElideMode(CuteNum):
    """
    The enum 'QQuickText::TextElideMode' of Qt, with the 4 names Qt gives in
    it.
    """

    ElideLeft = Kee[int](0)
    ElideRight = Kee[int](1)
    ElideMiddle = Kee[int](2)
    ElideNone = Kee[int](3)

  class TextFormat(CuteNum):
    """
    The enum 'QQuickText::TextFormat' of Qt, with the 5 names Qt gives in it.
    """

    PlainText = Kee[int](0)
    RichText = Kee[int](1)
    MarkdownText = Kee[int](3)
    AutoText = Kee[int](2)
    StyledText = Kee[int](4)

  class TextStyle(CuteNum):
    """
    The enum 'QQuickText::TextStyle' of Qt, with the 4 names Qt gives in it.
    """

    Normal = Kee[int](0)
    Outline = Kee[int](1)
    Raised = Kee[int](2)
    Sunken = Kee[int](3)

  class VAlignment(CuteNum):
    """
    The enum 'QQuickText::VAlignment' of Qt, with the 3 names Qt gives in it.
    """

    AlignTop = Kee[int](32)
    AlignBottom = Kee[int](64)
    AlignVCenter = Kee[int](128)

  class WrapMode(CuteNum):
    """
    The enum 'QQuickText::WrapMode' of Qt, with the 5 names Qt gives in it.
    """

    NoWrap = Kee[int](0)
    WordWrap = Kee[int](1)
    WrapAnywhere = Kee[int](3)
    WrapAtWordBoundaryOrAnywhere = Kee[int](4)
    Wrap = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickText::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickText::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickText2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickText'

  #  Qt's QQuickText is built on more than one class. The part of a C++
  #  QQuickText that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickTextInterface': 'ritual_cast_QQuickText_QQuickTextInterface',
  }

  #  A C++ QQuickText Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickText'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickText::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickText::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickText10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickText::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickText::text() const
    return self.uglySide.call('ritual_ZNK10QQuickText4textEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickText::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickText::font() const
    address = self.uglySide.call('ritual_ZNK10QQuickText4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickText::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickText::color() const
    address = self.uglySide.call('ritual_ZNK10QQuickText5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def linkColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickText::linkColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#linkColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickText::linkColor() const
    address = self.uglySide.call('ritual_ZNK10QQuickText9linkColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def style(self) -> TextStyle:
    """
    Calls Qt's 'TextStyle QQuickText::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#style

    Returns
    -------

    TextStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextStyle(number)' gives.
    """
    #  TextStyle QQuickText::style() const
    return QQuickText.TextStyle(self.uglySide.call(
        'ritual_ZNK10QQuickText5styleEv',
    ))

  def styleColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickText::styleColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#styleColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickText::styleColor() const
    address = self.uglySide.call('ritual_ZNK10QQuickText10styleColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def hAlign(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickText::hAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#hAlign

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickText::hAlign() const
    return QQuickText.HAlignment(self.uglySide.call(
        'ritual_ZNK10QQuickText6hAlignEv',
    ))

  def effectiveHAlign(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickText::effectiveHAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#effectiveHAlign

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickText::effectiveHAlign() const
    return QQuickText.HAlignment(self.uglySide.call(
        'ritual_ZNK10QQuickText15effectiveHAlignEv',
    ))

  def vAlign(self) -> VAlignment:
    """
    Calls Qt's 'VAlignment QQuickText::vAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#vAlign

    Returns
    -------

    VAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'VAlignment(number)'
      gives.
    """
    #  VAlignment QQuickText::vAlign() const
    return QQuickText.VAlignment(self.uglySide.call(
        'ritual_ZNK10QQuickText6vAlignEv',
    ))

  def wrapMode(self) -> WrapMode:
    """
    Calls Qt's 'WrapMode QQuickText::wrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#wrapMode

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  WrapMode QQuickText::wrapMode() const
    return QQuickText.WrapMode(self.uglySide.call(
        'ritual_ZNK10QQuickText8wrapModeEv',
    ))

  def lineCount(self) -> int:
    """
    Calls Qt's 'int QQuickText::lineCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#lineCount
    """
    #  int QQuickText::lineCount() const
    return self.uglySide.call('ritual_ZNK10QQuickText9lineCountEv')

  def truncated(self) -> bool:
    """
    Calls Qt's 'bool QQuickText::truncated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#truncated
    """
    #  bool QQuickText::truncated() const
    return self.uglySide.call('ritual_ZNK10QQuickText9truncatedEv')

  def maximumLineCount(self) -> int:
    """
    Calls Qt's 'int QQuickText::maximumLineCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#maximumLineCount
    """
    #  int QQuickText::maximumLineCount() const
    return self.uglySide.call('ritual_ZNK10QQuickText16maximumLineCountEv')

  def textFormat(self) -> TextFormat:
    """
    Calls Qt's 'TextFormat QQuickText::textFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#textFormat

    Returns
    -------

    TextFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextFormat(number)'
      gives.
    """
    #  TextFormat QQuickText::textFormat() const
    return QQuickText.TextFormat(self.uglySide.call(
        'ritual_ZNK10QQuickText10textFormatEv',
    ))

  def elideMode(self) -> TextElideMode:
    """
    Calls Qt's 'TextElideMode QQuickText::elideMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#elideMode

    Returns
    -------

    TextElideMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextElideMode(number)'
      gives.
    """
    #  TextElideMode QQuickText::elideMode() const
    return QQuickText.TextElideMode(self.uglySide.call(
        'ritual_ZNK10QQuickText9elideModeEv',
    ))

  def lineHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickText::lineHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#lineHeight
    """
    #  qreal QQuickText::lineHeight() const
    return self.uglySide.call('ritual_ZNK10QQuickText10lineHeightEv')

  def lineHeightMode(self) -> LineHeightMode:
    """
    Calls Qt's 'LineHeightMode QQuickText::lineHeightMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#lineHeightMode

    Returns
    -------

    LineHeightMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LineHeightMode(number)'
      gives.
    """
    #  LineHeightMode QQuickText::lineHeightMode() const
    return QQuickText.LineHeightMode(self.uglySide.call(
        'ritual_ZNK10QQuickText14lineHeightModeEv',
    ))

  def baseUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickText::baseUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#baseUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickText::baseUrl() const
    address = self.uglySide.call('ritual_ZNK10QQuickText7baseUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def minimumPixelSize(self) -> int:
    """
    Calls Qt's 'int QQuickText::minimumPixelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#minimumPixelSize
    """
    #  int QQuickText::minimumPixelSize() const
    return self.uglySide.call('ritual_ZNK10QQuickText16minimumPixelSizeEv')

  def minimumPointSize(self) -> int:
    """
    Calls Qt's 'int QQuickText::minimumPointSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#minimumPointSize
    """
    #  int QQuickText::minimumPointSize() const
    return self.uglySide.call('ritual_ZNK10QQuickText16minimumPointSizeEv')

  def fontSizeMode(self) -> FontSizeMode:
    """
    Calls Qt's 'FontSizeMode QQuickText::fontSizeMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#fontSizeMode

    Returns
    -------

    FontSizeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FontSizeMode(number)'
      gives.
    """
    #  FontSizeMode QQuickText::fontSizeMode() const
    return QQuickText.FontSizeMode(self.uglySide.call(
        'ritual_ZNK10QQuickText12fontSizeModeEv',
    ))

  def resourcesLoading(self) -> int:
    """
    Calls Qt's 'int QQuickText::resourcesLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#resourcesLoading
    """
    #  int QQuickText::resourcesLoading() const
    return self.uglySide.call('ritual_ZNK10QQuickText16resourcesLoadingEv')

  def contentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickText::contentWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#contentWidth
    """
    #  qreal QQuickText::contentWidth() const
    return self.uglySide.call('ritual_ZNK10QQuickText12contentWidthEv')

  def contentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickText::contentHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#contentHeight
    """
    #  qreal QQuickText::contentHeight() const
    return self.uglySide.call('ritual_ZNK10QQuickText13contentHeightEv')

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickText::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickText::boundingRect() const
    ritual = 'ritual_ZNK10QQuickText12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickText12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def clipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickText::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#clipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickText::clipRect() const
    ritual = 'ritual_ZNK10QQuickText8clipRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickText8clipRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def renderType(self) -> RenderType:
    """
    Calls Qt's 'RenderType QQuickText::renderType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#renderType

    Returns
    -------

    RenderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderType(number)'
      gives.
    """
    #  RenderType QQuickText::renderType() const
    return QQuickText.RenderType(self.uglySide.call(
        'ritual_ZNK10QQuickText10renderTypeEv',
    ))

  def renderTypeQuality(self) -> int:
    """
    Calls Qt's 'int QQuickText::renderTypeQuality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#renderTypeQuality
    """
    #  int QQuickText::renderTypeQuality() const
    return self.uglySide.call('ritual_ZNK10QQuickText17renderTypeQualityEv')

  def hoveredLink(self) -> str:
    """
    Calls Qt's 'QString QQuickText::hoveredLink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#hoveredLink

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickText::hoveredLink() const
    return self.uglySide.call('ritual_ZNK10QQuickText11hoveredLinkEv')

  @overload(float, float)
  def linkAt(self, x: float, y: float) -> str:
    """
    Calls Qt's 'QString QQuickText::linkAt(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#linkAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickText::linkAt(qreal x, qreal y) const
    return self.uglySide.call('ritual_ZNK10QQuickText6linkAtEdd', x, y)

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickText::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#padding
    """
    #  qreal QQuickText::padding() const
    return self.uglySide.call('ritual_ZNK10QQuickText7paddingEv')

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickText::topPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#topPadding
    """
    #  qreal QQuickText::topPadding() const
    return self.uglySide.call('ritual_ZNK10QQuickText10topPaddingEv')

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickText::leftPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#leftPadding
    """
    #  qreal QQuickText::leftPadding() const
    return self.uglySide.call('ritual_ZNK10QQuickText11leftPaddingEv')

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickText::rightPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#rightPadding
    """
    #  qreal QQuickText::rightPadding() const
    return self.uglySide.call('ritual_ZNK10QQuickText12rightPaddingEv')

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickText::bottomPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#bottomPadding
    """
    #  qreal QQuickText::bottomPadding() const
    return self.uglySide.call('ritual_ZNK10QQuickText13bottomPaddingEv')

  def fontInfo(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickText::fontInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#fontInfo

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickText::fontInfo() const
    address = self.uglySide.call('ritual_ZNK10QQuickText8fontInfoEv')
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def advance(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickText::advance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#advance

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickText::advance() const
    address = self.uglySide.call('ritual_ZNK10QQuickText7advanceEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickText::setText(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setText

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickText::setText(const QString &a0)
    self.uglySide.call('ritual_ZN10QQuickText7setTextERK7QString', a0)

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickText::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickText::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN10QQuickText7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QColor)
  def setColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickText::setColor(const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickText::setColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN10QQuickText8setColorERK6QColor', self._valueOf(c),
    )

  @overload(QColor)
  def setLinkColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickText::setLinkColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setLinkColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickText::setLinkColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN10QQuickText12setLinkColorERK6QColor',
        self._valueOf(color),
    )

  @overload(TextStyle)
  def setStyle(self, style: TextStyle) -> None:
    """
    Calls Qt's 'void QQuickText::setStyle(TextStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setStyle

    Parameters
    ----------

    style : TextStyle
      Passed on as its number.
    """
    #  void QQuickText::setStyle(TextStyle style)
    self.uglySide.call(
        'ritual_ZN10QQuickText8setStyleENS_9TextStyleE', style.value,
    )

  @overload(QColor)
  def setStyleColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickText::setStyleColor(const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setStyleColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickText::setStyleColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN10QQuickText13setStyleColorERK6QColor', self._valueOf(c),
    )

  @overload(HAlignment)
  def setHAlign(self, align: HAlignment) -> None:
    """
    Calls Qt's 'void QQuickText::setHAlign(HAlignment align)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setHAlign

    Parameters
    ----------

    align : HAlignment
      Passed on as its number.
    """
    #  void QQuickText::setHAlign(HAlignment align)
    self.uglySide.call(
        'ritual_ZN10QQuickText9setHAlignENS_10HAlignmentE', align.value,
    )

  @overload(VAlignment)
  def setVAlign(self, align: VAlignment) -> None:
    """
    Calls Qt's 'void QQuickText::setVAlign(VAlignment align)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setVAlign

    Parameters
    ----------

    align : VAlignment
      Passed on as its number.
    """
    #  void QQuickText::setVAlign(VAlignment align)
    self.uglySide.call(
        'ritual_ZN10QQuickText9setVAlignENS_10VAlignmentE', align.value,
    )

  @overload(WrapMode)
  def setWrapMode(self, w: WrapMode) -> None:
    """
    Calls Qt's 'void QQuickText::setWrapMode(WrapMode w)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setWrapMode

    Parameters
    ----------

    w : WrapMode
      Passed on as its number.
    """
    #  void QQuickText::setWrapMode(WrapMode w)
    self.uglySide.call(
        'ritual_ZN10QQuickText11setWrapModeENS_8WrapModeE', w.value,
    )

  @overload(int)
  def setMaximumLineCount(self, lines: int) -> None:
    """
    Calls Qt's 'void QQuickText::setMaximumLineCount(int lines)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#setMaximumLineCount

    Parameters
    ----------

    lines : int
      Passed on as it is.
    """
    #  void QQuickText::setMaximumLineCount(int lines)
    self.uglySide.call('ritual_ZN10QQuickText19setMaximumLineCountEi', lines)

  @overload(TextFormat)
  def setTextFormat(self, format: TextFormat) -> None:
    """
    Calls Qt's 'void QQuickText::setTextFormat(TextFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setTextFormat

    Parameters
    ----------

    format : TextFormat
      Passed on as its number.
    """
    #  void QQuickText::setTextFormat(TextFormat format)
    self.uglySide.call(
        'ritual_ZN10QQuickText13setTextFormatENS_10TextFormatE',
        format.value,
    )

  @overload(TextElideMode)
  def setElideMode(self, a0: TextElideMode) -> None:
    """
    Calls Qt's 'void QQuickText::setElideMode(TextElideMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setElideMode

    Parameters
    ----------

    a0 : TextElideMode
      Passed on as its number.
    """
    #  void QQuickText::setElideMode(TextElideMode a0)
    self.uglySide.call(
        'ritual_ZN10QQuickText12setElideModeENS_13TextElideModeE', a0.value,
    )

  @overload(float)
  def setLineHeight(self, lineHeight: float) -> None:
    """
    Calls Qt's 'void QQuickText::setLineHeight(qreal lineHeight)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setLineHeight

    Parameters
    ----------

    lineHeight : float
      Passed on as it is.
    """
    #  void QQuickText::setLineHeight(qreal lineHeight)
    self.uglySide.call('ritual_ZN10QQuickText13setLineHeightEd', lineHeight)

  @overload(LineHeightMode)
  def setLineHeightMode(self, a0: LineHeightMode) -> None:
    """
    Calls Qt's 'void QQuickText::setLineHeightMode(LineHeightMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setLineHeightMode

    Parameters
    ----------

    a0 : LineHeightMode
      Passed on as its number.
    """
    #  void QQuickText::setLineHeightMode(LineHeightMode a0)
    self.uglySide.call(
        'ritual_ZN10QQuickText17setLineHeightModeENS_14LineHeightModeE',
        a0.value,
    )

  @overload(QUrl)
  def setBaseUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickText::setBaseUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setBaseUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickText::setBaseUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN10QQuickText10setBaseUrlERK4QUrl', self._valueOf(url),
    )

  @overload(int)
  def setMinimumPixelSize(self, size: int) -> None:
    """
    Calls Qt's 'void QQuickText::setMinimumPixelSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#setMinimumPixelSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QQuickText::setMinimumPixelSize(int size)
    self.uglySide.call('ritual_ZN10QQuickText19setMinimumPixelSizeEi', size)

  @overload(int)
  def setMinimumPointSize(self, size: int) -> None:
    """
    Calls Qt's 'void QQuickText::setMinimumPointSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#setMinimumPointSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QQuickText::setMinimumPointSize(int size)
    self.uglySide.call('ritual_ZN10QQuickText19setMinimumPointSizeEi', size)

  @overload(FontSizeMode)
  def setFontSizeMode(self, mode: FontSizeMode) -> None:
    """
    Calls Qt's 'void QQuickText::setFontSizeMode(FontSizeMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setFontSizeMode

    Parameters
    ----------

    mode : FontSizeMode
      Passed on as its number.
    """
    #  void QQuickText::setFontSizeMode(FontSizeMode mode)
    self.uglySide.call(
        'ritual_ZN10QQuickText15setFontSizeModeENS_12FontSizeModeE',
        mode.value,
    )

  @overload(RenderType)
  def setRenderType(self, renderType: RenderType) -> None:
    """
    Calls Qt's 'void QQuickText::setRenderType(RenderType renderType)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setRenderType

    Parameters
    ----------

    renderType : RenderType
      Passed on as its number.
    """
    #  void QQuickText::setRenderType(RenderType renderType)
    self.uglySide.call(
        'ritual_ZN10QQuickText13setRenderTypeENS_10RenderTypeE',
        renderType.value,
    )

  @overload(int)
  def setRenderTypeQuality(self, renderTypeQuality: int) -> None:
    """
    Calls Qt's 'void QQuickText::setRenderTypeQuality(int
    renderTypeQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#setRenderTypeQuality

    Parameters
    ----------

    renderTypeQuality : int
      Passed on as it is.
    """
    #  void QQuickText::setRenderTypeQuality(int renderTypeQuality)
    self.uglySide.call(
        'ritual_ZN10QQuickText20setRenderTypeQualityEi', renderTypeQuality,
    )

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickText::setPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickText::setPadding(qreal padding)
    self.uglySide.call('ritual_ZN10QQuickText10setPaddingEd', padding)

  @overload(float)
  def setTopPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickText::setTopPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickText::setTopPadding(qreal padding)
    self.uglySide.call('ritual_ZN10QQuickText13setTopPaddingEd', padding)

  @overload(float)
  def setLeftPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickText::setLeftPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickText::setLeftPadding(qreal padding)
    self.uglySide.call('ritual_ZN10QQuickText14setLeftPaddingEd', padding)

  @overload(float)
  def setRightPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickText::setRightPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickText::setRightPadding(qreal padding)
    self.uglySide.call('ritual_ZN10QQuickText15setRightPaddingEd', padding)

  @overload(float)
  def setBottomPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickText::setBottomPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickText::setBottomPadding(qreal padding)
    self.uglySide.call('ritual_ZN10QQuickText16setBottomPaddingEd', padding)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickText::QQuickText(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#QQuickText

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickText::QQuickText(QQuickItem *parent)
    self._noteCreation(QQuickText, lambda: Rituals.call(
        'ritual_ZN10QQuickTextC1EP10QQuickItem', self._addressOf(parent),
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

  def resetHAlign(self) -> None:
    """
    Calls Qt's 'void QQuickText::resetHAlign()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#resetHAlign
    """
    #  void QQuickText::resetHAlign()
    self.uglySide.call('ritual_ZN10QQuickText11resetHAlignEv')

  def resetMaximumLineCount(self) -> None:
    """
    Calls Qt's 'void QQuickText::resetMaximumLineCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#resetMaximumLineCount
    """
    #  void QQuickText::resetMaximumLineCount()
    self.uglySide.call('ritual_ZN10QQuickText21resetMaximumLineCountEv')

  def resetBaseUrl(self) -> None:
    """
    Calls Qt's 'void QQuickText::resetBaseUrl()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#resetBaseUrl
    """
    #  void QQuickText::resetBaseUrl()
    self.uglySide.call('ritual_ZN10QQuickText12resetBaseUrlEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickText::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#componentComplete
    """
    #  void QQuickText::componentComplete()
    ritual = 'ritual_ZN10QQuickText17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickText17componentCompleteEv'
    self.uglySide.call(ritual)

  def forceLayout(self) -> None:
    """
    Calls Qt's 'void QQuickText::forceLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#forceLayout
    """
    #  void QQuickText::forceLayout()
    self.uglySide.call('ritual_ZN10QQuickText11forceLayoutEv')

  def resetPadding(self) -> None:
    """
    Calls Qt's 'void QQuickText::resetPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#resetPadding
    """
    #  void QQuickText::resetPadding()
    self.uglySide.call('ritual_ZN10QQuickText12resetPaddingEv')

  def resetTopPadding(self) -> None:
    """
    Calls Qt's 'void QQuickText::resetTopPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#resetTopPadding
    """
    #  void QQuickText::resetTopPadding()
    self.uglySide.call('ritual_ZN10QQuickText15resetTopPaddingEv')

  def resetLeftPadding(self) -> None:
    """
    Calls Qt's 'void QQuickText::resetLeftPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#resetLeftPadding
    """
    #  void QQuickText::resetLeftPadding()
    self.uglySide.call('ritual_ZN10QQuickText16resetLeftPaddingEv')

  def resetRightPadding(self) -> None:
    """
    Calls Qt's 'void QQuickText::resetRightPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#resetRightPadding
    """
    #  void QQuickText::resetRightPadding()
    self.uglySide.call('ritual_ZN10QQuickText17resetRightPaddingEv')

  def resetBottomPadding(self) -> None:
    """
    Calls Qt's 'void QQuickText::resetBottomPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#resetBottomPadding
    """
    #  void QQuickText::resetBottomPadding()
    self.uglySide.call('ritual_ZN10QQuickText18resetBottomPaddingEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickText::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#invalidate
    """
    #  void QQuickText::invalidate()
    ritual = 'ritual_ZN10QQuickText10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickText10invalidateEv'
    self.uglySide.call(ritual)

  @overload(str)
  def textChanged(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickText::textChanged(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#textChanged

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickText::textChanged(const QString &text)
    self.uglySide.call('ritual_ZN10QQuickText11textChangedERK7QString', text)

  @overload(str)
  def linkActivated(self, link: str) -> None:
    """
    Calls Qt's 'void QQuickText::linkActivated(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#linkActivated

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickText::linkActivated(const QString &link)
    self.uglySide.call(
        'ritual_ZN10QQuickText13linkActivatedERK7QString', link,
    )

  @overload(str)
  def linkHovered(self, link: str) -> None:
    """
    Calls Qt's 'void QQuickText::linkHovered(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#linkHovered

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickText::linkHovered(const QString &link)
    self.uglySide.call('ritual_ZN10QQuickText11linkHoveredERK7QString', link)

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickText::fontChanged(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickText::fontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN10QQuickText11fontChangedERK5QFont', self._valueOf(font),
    )

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#colorChanged
    """
    #  void QQuickText::colorChanged()
    self.uglySide.call('ritual_ZN10QQuickText12colorChangedEv')

  def linkColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::linkColorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#linkColorChanged
    """
    #  void QQuickText::linkColorChanged()
    self.uglySide.call('ritual_ZN10QQuickText16linkColorChangedEv')

  @overload(TextStyle)
  def styleChanged(self, style: TextStyle) -> None:
    """
    Calls Qt's 'void QQuickText::styleChanged(QQuickText::TextStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#styleChanged

    Parameters
    ----------

    style : TextStyle
      Passed on as its number.
    """
    #  void QQuickText::styleChanged(QQuickText::TextStyle style)
    self.uglySide.call(
        'ritual_ZN10QQuickText12styleChangedENS_9TextStyleE', style.value,
    )

  def styleColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::styleColorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#styleColorChanged
    """
    #  void QQuickText::styleColorChanged()
    self.uglySide.call('ritual_ZN10QQuickText17styleColorChangedEv')

  @overload(HAlignment)
  def horizontalAlignmentChanged(self, alignment: HAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickText::horizontalAlignmentChanged(QQuickText::HAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#horizontalAlignmentChanged

    Parameters
    ----------

    alignment : HAlignment
      Passed on as its number.
    """
    #  void QQuickText::horizontalAlignmentChanged(QQuickText::HAlignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN10QQuickText26horizontalAlignmentChangedENS_10HAlignmentE',
        alignment.value,
    )

  @overload(VAlignment)
  def verticalAlignmentChanged(self, alignment: VAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickText::verticalAlignmentChanged(QQuickText::VAlignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#verticalAlignmentChanged

    Parameters
    ----------

    alignment : VAlignment
      Passed on as its number.
    """
    #  void QQuickText::verticalAlignmentChanged(QQuickText::VAlignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN10QQuickText24verticalAlignmentChangedENS_10VAlignmentE',
        alignment.value,
    )

  def wrapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::wrapModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#wrapModeChanged
    """
    #  void QQuickText::wrapModeChanged()
    self.uglySide.call('ritual_ZN10QQuickText15wrapModeChangedEv')

  def lineCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::lineCountChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#lineCountChanged
    """
    #  void QQuickText::lineCountChanged()
    self.uglySide.call('ritual_ZN10QQuickText16lineCountChangedEv')

  def truncatedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::truncatedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#truncatedChanged
    """
    #  void QQuickText::truncatedChanged()
    self.uglySide.call('ritual_ZN10QQuickText16truncatedChangedEv')

  def maximumLineCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::maximumLineCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#maximumLineCountChanged
    """
    #  void QQuickText::maximumLineCountChanged()
    self.uglySide.call('ritual_ZN10QQuickText23maximumLineCountChangedEv')

  @overload(TextFormat)
  def textFormatChanged(self, textFormat: TextFormat) -> None:
    """
    Calls Qt's 'void QQuickText::textFormatChanged(QQuickText::TextFormat
    textFormat)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#textFormatChanged

    Parameters
    ----------

    textFormat : TextFormat
      Passed on as its number.
    """
    #  void QQuickText::textFormatChanged(QQuickText::TextFormat textFormat)
    self.uglySide.call(
        'ritual_ZN10QQuickText17textFormatChangedENS_10TextFormatE',
        textFormat.value,
    )

  @overload(TextElideMode)
  def elideModeChanged(self, mode: TextElideMode) -> None:
    """
    Calls Qt's 'void QQuickText::elideModeChanged(QQuickText::TextElideMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#elideModeChanged

    Parameters
    ----------

    mode : TextElideMode
      Passed on as its number.
    """
    #  void QQuickText::elideModeChanged(QQuickText::TextElideMode mode)
    self.uglySide.call(
        'ritual_ZN10QQuickText16elideModeChangedENS_13TextElideModeE',
        mode.value,
    )

  def contentSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::contentSizeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#contentSizeChanged
    """
    #  void QQuickText::contentSizeChanged()
    self.uglySide.call('ritual_ZN10QQuickText18contentSizeChangedEv')

  @overload(float)
  def contentWidthChanged(self, contentWidth: float) -> None:
    """
    Calls Qt's 'void QQuickText::contentWidthChanged(qreal contentWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#contentWidthChanged

    Parameters
    ----------

    contentWidth : float
      Passed on as it is.
    """
    #  void QQuickText::contentWidthChanged(qreal contentWidth)
    self.uglySide.call(
        'ritual_ZN10QQuickText19contentWidthChangedEd', contentWidth,
    )

  @overload(float)
  def contentHeightChanged(self, contentHeight: float) -> None:
    """
    Calls Qt's 'void QQuickText::contentHeightChanged(qreal contentHeight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#contentHeightChanged

    Parameters
    ----------

    contentHeight : float
      Passed on as it is.
    """
    #  void QQuickText::contentHeightChanged(qreal contentHeight)
    self.uglySide.call(
        'ritual_ZN10QQuickText20contentHeightChangedEd', contentHeight,
    )

  @overload(float)
  def lineHeightChanged(self, lineHeight: float) -> None:
    """
    Calls Qt's 'void QQuickText::lineHeightChanged(qreal lineHeight)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#lineHeightChanged

    Parameters
    ----------

    lineHeight : float
      Passed on as it is.
    """
    #  void QQuickText::lineHeightChanged(qreal lineHeight)
    self.uglySide.call(
        'ritual_ZN10QQuickText17lineHeightChangedEd', lineHeight,
    )

  @overload(LineHeightMode)
  def lineHeightModeChanged(self, mode: LineHeightMode) -> None:
    """
    Calls Qt's 'void
    QQuickText::lineHeightModeChanged(QQuickText::LineHeightMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#lineHeightModeChanged

    Parameters
    ----------

    mode : LineHeightMode
      Passed on as its number.
    """
    #  void QQuickText::lineHeightModeChanged(QQuickText::LineHeightMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN10QQuickText21lineHeightModeChangedENS_14LineHeightModeE',
        mode.value,
    )

  def fontSizeModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::fontSizeModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#fontSizeModeChanged
    """
    #  void QQuickText::fontSizeModeChanged()
    self.uglySide.call('ritual_ZN10QQuickText19fontSizeModeChangedEv')

  def minimumPixelSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::minimumPixelSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#minimumPixelSizeChanged
    """
    #  void QQuickText::minimumPixelSizeChanged()
    self.uglySide.call('ritual_ZN10QQuickText23minimumPixelSizeChangedEv')

  def minimumPointSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::minimumPointSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#minimumPointSizeChanged
    """
    #  void QQuickText::minimumPointSizeChanged()
    self.uglySide.call('ritual_ZN10QQuickText23minimumPointSizeChangedEv')

  def effectiveHorizontalAlignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::effectiveHorizontalAlignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html
    """
    #  void QQuickText::effectiveHorizontalAlignmentChanged()
    self.uglySide.call(
        'ritual_ZN10QQuickText35effectiveHorizontalAlignmentChangedEv',
    )

  @overload(QQuickTextLine)
  @overload(NoneType)
  def lineLaidOut(self, line: Optional[QQuickTextLine]) -> None:
    """
    Calls Qt's 'void QQuickText::lineLaidOut(QQuickTextLine *line)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#lineLaidOut

    Parameters
    ----------

    line : Optional[QQuickTextLine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickText::lineLaidOut(QQuickTextLine *line)
    self.uglySide.call(
        'ritual_ZN10QQuickText11lineLaidOutEP14QQuickTextLine',
        self._addressOf(line),
    )

  def baseUrlChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::baseUrlChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#baseUrlChanged
    """
    #  void QQuickText::baseUrlChanged()
    self.uglySide.call('ritual_ZN10QQuickText14baseUrlChangedEv')

  def renderTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::renderTypeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#renderTypeChanged
    """
    #  void QQuickText::renderTypeChanged()
    self.uglySide.call('ritual_ZN10QQuickText17renderTypeChangedEv')

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::paddingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#paddingChanged
    """
    #  void QQuickText::paddingChanged()
    self.uglySide.call('ritual_ZN10QQuickText14paddingChangedEv')

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::topPaddingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#topPaddingChanged
    """
    #  void QQuickText::topPaddingChanged()
    self.uglySide.call('ritual_ZN10QQuickText17topPaddingChangedEv')

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::leftPaddingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#leftPaddingChanged
    """
    #  void QQuickText::leftPaddingChanged()
    self.uglySide.call('ritual_ZN10QQuickText18leftPaddingChangedEv')

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#rightPaddingChanged
    """
    #  void QQuickText::rightPaddingChanged()
    self.uglySide.call('ritual_ZN10QQuickText19rightPaddingChangedEv')

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#bottomPaddingChanged
    """
    #  void QQuickText::bottomPaddingChanged()
    self.uglySide.call('ritual_ZN10QQuickText20bottomPaddingChangedEv')

  def fontInfoChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::fontInfoChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#fontInfoChanged
    """
    #  void QQuickText::fontInfoChanged()
    self.uglySide.call('ritual_ZN10QQuickText15fontInfoChangedEv')

  def renderTypeQualityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickText::renderTypeQualityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#renderTypeQualityChanged
    """
    #  void QQuickText::renderTypeQualityChanged()
    self.uglySide.call('ritual_ZN10QQuickText24renderTypeQualityChangedEv')

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickText::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickText::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QQuickText15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickText15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickText::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickText::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QQuickText17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickText17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickText::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickText::itemChange(ItemChange change, const ItemChangeData
    #      &value)
    ritual = (
        'ritual_ZN10QQuickText10itemChangeEN10QQuickItem10ItemChangeERKNS0_'
        '14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QQuickText10itemChangeEN10QQuickItem10ItemChangeE'
          'RKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickText::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickText::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN10QQuickText14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickText14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickText::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickText::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
    #      *a1)
    ritual = (
        'ritual_ZN10QQuickText15updatePaintNodeEP7QSGNodePN10QQuickItem19Up'
        'datePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QQuickText15updatePaintNodeEP7QSGNodePN10QQuickIt'
          'em19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickText::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#updatePolish
    """
    #  void QQuickText::updatePolish()
    ritual = 'ritual_ZN10QQuickText12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickText12updatePolishEv'
    self.uglySide.call(ritual)

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickText::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickText::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN10QQuickText15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickText15hoverEnterEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickText::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickText::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN10QQuickText14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickText14hoverMoveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickText::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickText::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN10QQuickText15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickText15hoverLeaveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def invalidateFontCaches(self) -> None:
    """
    Calls Qt's 'void QQuickText::invalidateFontCaches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#invalidateFontCaches
    """
    #  void QQuickText::invalidateFontCaches()
    self.uglySide.call('ritual_ZN10QQuickText20invalidateFontCachesEv')

  def q_updateLayout(self) -> None:
    """
    Calls Qt's 'void QQuickText::q_updateLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#q_updateLayout
    """
    #  void QQuickText::q_updateLayout()
    self.uglySide.call('ritual_ZN10QQuickText14q_updateLayoutEv')

  def triggerPreprocess(self) -> None:
    """
    Calls Qt's 'void QQuickText::triggerPreprocess()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#triggerPreprocess
    """
    #  void QQuickText::triggerPreprocess()
    self.uglySide.call('ritual_ZN10QQuickText17triggerPreprocessEv')

  @overload(int, QUrl)
  def loadResource(self, type: int, source: QUrl) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickText::loadResource(int type, const QUrl
    &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#loadResource

    Parameters
    ----------

    type : int
      Passed on as it is.

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickText::loadResource(int type, const QUrl &source)
    address = self.uglySide.call(
        'ritual_ZN10QQuickText12loadResourceEiRK4QUrl',
        type, self._valueOf(source),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def resourceRequestFinished(self) -> None:
    """
    Calls Qt's 'void QQuickText::resourceRequestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#resourceRequestFinished
    """
    #  void QQuickText::resourceRequestFinished()
    self.uglySide.call('ritual_ZN10QQuickText23resourceRequestFinishedEv')

  def imageDownloadFinished(self) -> None:
    """
    Calls Qt's 'void QQuickText::imageDownloadFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktext.html#imageDownloadFinished
    """
    #  void QQuickText::imageDownloadFinished()
    self.uglySide.call('ritual_ZN10QQuickText21imageDownloadFinishedEv')

  def d_func(self) -> Optional[QQuickTextPrivate]:
    """
    Calls Qt's 'QQuickTextPrivate *QQuickText::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktext.html#d_func

    Returns
    -------

    Optional[QQuickTextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextPrivate *QQuickText::d_func()
    address = self.uglySide.call('ritual_ZN10QQuickText6d_funcEv')
    from . import QQuickTextPrivate
    return QQuickTextPrivate._cuteAt(address)
