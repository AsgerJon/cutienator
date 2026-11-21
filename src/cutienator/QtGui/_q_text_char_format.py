"""
QTextCharFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QFont, QTextFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from . import QColor, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPen = WAIT['QPen']


class QTextCharFormat(QTextFormat):
  """
  The cute side of Qt's QTextCharFormat: a plain Python object standing in
  front of one C++ QTextCharFormat.

  It is built on the cute 'QTextFormat', as Qt's QTextCharFormat is built on
  Qt's QTextFormat, and has everything that class has.

  C++ hands a QTextCharFormat around as a copy, so every C++ QTextCharFormat
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextCharFormat that has a ritual and that Python
  can call so far, 64 names in all: 'isValid', 'setFont', 'font',
  'setFontFamily', 'fontFamily', 'fontFamilies', 'setFontStyleName',
  'fontStyleName', 'setFontPointSize', 'fontPointSize', 'setFontWeight',
  'fontWeight', 'setFontItalic', 'fontItalic', 'setFontCapitalization',
  'fontCapitalization', 'setFontLetterSpacingType', 'fontLetterSpacingType',
  'setFontLetterSpacing', 'fontLetterSpacing', 'setFontWordSpacing',
  'fontWordSpacing', 'setFontUnderline', 'fontUnderline', 'setFontOverline',
  'fontOverline', 'setFontStrikeOut', 'fontStrikeOut', 'setUnderlineColor',
  'underlineColor', 'setFontFixedPitch', 'fontFixedPitch', 'setFontStretch',
  'fontStretch', 'setFontStyleHint', 'setFontStyleStrategy', 'fontStyleHint',
  'fontStyleStrategy', 'setFontHintingPreference', 'fontHintingPreference',
  'setFontKerning', 'fontKerning', 'setUnderlineStyle', 'underlineStyle',
  'setVerticalAlignment', 'verticalAlignment', 'setTextOutline',
  'textOutline', 'setToolTip', 'toolTip', 'setSuperScriptBaseline',
  'superScriptBaseline', 'setSubScriptBaseline', 'subScriptBaseline',
  'setBaselineOffset', 'baselineOffset', 'setAnchor', 'isAnchor',
  'setAnchorHref', 'anchorHref', 'setTableCellRowSpan', 'tableCellRowSpan',
  'setTableCellColumnSpan', 'tableCellColumnSpan'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextCharFormat::~QTextCharFormat()': the destructor: Python
    removes its C++ QTextCharFormat by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 74 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QTextCharFormat is created at the first use, not by
    'QTextCharFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextCharFormat back gives a copy the ritual made for
    Python, in a new cute QTextCharFormat.
  """

  #  The enums Qt writes inside QTextCharFormat, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FontPropertiesInheritanceBehavior(CuteNum):
    """
    The enum 'QTextCharFormat::FontPropertiesInheritanceBehavior' of Qt, with
    the 2 names Qt gives in it.
    """

    FontPropertiesSpecifiedOnly = Kee[int](0)
    FontPropertiesAll = Kee[int](1)

  class UnderlineStyle(CuteNum):
    """
    The enum 'QTextCharFormat::UnderlineStyle' of Qt, with the 8 names Qt
    gives in it.
    """

    NoUnderline = Kee[int](0)
    SingleUnderline = Kee[int](1)
    DashUnderline = Kee[int](2)
    DotLine = Kee[int](3)
    DashDotLine = Kee[int](4)
    DashDotDotLine = Kee[int](5)
    WaveUnderline = Kee[int](6)
    SpellCheckUnderline = Kee[int](7)

  class VerticalAlignment(CuteNum):
    """
    The enum 'QTextCharFormat::VerticalAlignment' of Qt, with the 7 names Qt
    gives in it.
    """

    AlignNormal = Kee[int](0)
    AlignSuperScript = Kee[int](1)
    AlignSubScript = Kee[int](2)
    AlignMiddle = Kee[int](3)
    AlignTop = Kee[int](4)
    AlignBottom = Kee[int](5)
    AlignBaseline = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextCharFormat'

  #  Qt's '~QTextCharFormat()'. Naming it makes this a value class: Python
  #  owns every C++ QTextCharFormat behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QTextCharFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextCharFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#isValid
    """
    #  bool QTextCharFormat::isValid() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat7isValidEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QTextCharFormat::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTextCharFormat::font() const
    address = self.uglySide.call('ritual_ZNK15QTextCharFormat4fontEv')
    return QFont._cuteOwning(address)

  def fontFamily(self) -> str:
    """
    Calls Qt's 'QString QTextCharFormat::fontFamily() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontFamily

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextCharFormat::fontFamily() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat10fontFamilyEv')

  def fontFamilies(self) -> QVariant:
    """
    Calls Qt's 'QVariant QTextCharFormat::fontFamilies() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontFamilies

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextCharFormat::fontFamilies() const
    address = self.uglySide.call(
        'ritual_ZNK15QTextCharFormat12fontFamiliesEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def fontStyleName(self) -> QVariant:
    """
    Calls Qt's 'QVariant QTextCharFormat::fontStyleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontStyleName

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextCharFormat::fontStyleName() const
    address = self.uglySide.call(
        'ritual_ZNK15QTextCharFormat13fontStyleNameEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def fontPointSize(self) -> float:
    """
    Calls Qt's 'qreal QTextCharFormat::fontPointSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontPointSize
    """
    #  qreal QTextCharFormat::fontPointSize() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat13fontPointSizeEv')

  def fontWeight(self) -> int:
    """
    Calls Qt's 'int QTextCharFormat::fontWeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontWeight
    """
    #  int QTextCharFormat::fontWeight() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat10fontWeightEv')

  def fontItalic(self) -> bool:
    """
    Calls Qt's 'bool QTextCharFormat::fontItalic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontItalic
    """
    #  bool QTextCharFormat::fontItalic() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat10fontItalicEv')

  def fontCapitalization(self) -> QFont.Capitalization:
    """
    Calls Qt's 'QFont::Capitalization QTextCharFormat::fontCapitalization()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#fontCapitalization

    Returns
    -------

    QFont.Capitalization
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QFont.Capitalization(number)' gives.
    """
    #  QFont::Capitalization QTextCharFormat::fontCapitalization() const
    return QFont.Capitalization(self.uglySide.call(
        'ritual_ZNK15QTextCharFormat18fontCapitalizationEv',
    ))

  def fontLetterSpacingType(self) -> QFont.SpacingType:
    """
    Calls Qt's 'QFont::SpacingType QTextCharFormat::fontLetterSpacingType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#fontLetterSpacingType

    Returns
    -------

    QFont.SpacingType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QFont.SpacingType(number)' gives.
    """
    #  QFont::SpacingType QTextCharFormat::fontLetterSpacingType() const
    return QFont.SpacingType(self.uglySide.call(
        'ritual_ZNK15QTextCharFormat21fontLetterSpacingTypeEv',
    ))

  def fontLetterSpacing(self) -> float:
    """
    Calls Qt's 'qreal QTextCharFormat::fontLetterSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#fontLetterSpacing
    """
    #  qreal QTextCharFormat::fontLetterSpacing() const
    return self.uglySide.call(
        'ritual_ZNK15QTextCharFormat17fontLetterSpacingEv',
    )

  def fontWordSpacing(self) -> float:
    """
    Calls Qt's 'qreal QTextCharFormat::fontWordSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#fontWordSpacing
    """
    #  qreal QTextCharFormat::fontWordSpacing() const
    return self.uglySide.call(
        'ritual_ZNK15QTextCharFormat15fontWordSpacingEv',
    )

  def fontUnderline(self) -> bool:
    """
    Calls Qt's 'bool QTextCharFormat::fontUnderline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontUnderline
    """
    #  bool QTextCharFormat::fontUnderline() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat13fontUnderlineEv')

  def fontOverline(self) -> bool:
    """
    Calls Qt's 'bool QTextCharFormat::fontOverline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontOverline
    """
    #  bool QTextCharFormat::fontOverline() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat12fontOverlineEv')

  def fontStrikeOut(self) -> bool:
    """
    Calls Qt's 'bool QTextCharFormat::fontStrikeOut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontStrikeOut
    """
    #  bool QTextCharFormat::fontStrikeOut() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat13fontStrikeOutEv')

  def underlineColor(self) -> QColor:
    """
    Calls Qt's 'QColor QTextCharFormat::underlineColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#underlineColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QTextCharFormat::underlineColor() const
    address = self.uglySide.call(
        'ritual_ZNK15QTextCharFormat14underlineColorEv',
    )
    from . import QColor
    return QColor._cuteOwning(address)

  def fontFixedPitch(self) -> bool:
    """
    Calls Qt's 'bool QTextCharFormat::fontFixedPitch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#fontFixedPitch
    """
    #  bool QTextCharFormat::fontFixedPitch() const
    return self.uglySide.call(
        'ritual_ZNK15QTextCharFormat14fontFixedPitchEv',
    )

  def fontStretch(self) -> int:
    """
    Calls Qt's 'int QTextCharFormat::fontStretch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontStretch
    """
    #  int QTextCharFormat::fontStretch() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat11fontStretchEv')

  def fontStyleHint(self) -> QFont.StyleHint:
    """
    Calls Qt's 'QFont::StyleHint QTextCharFormat::fontStyleHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontStyleHint

    Returns
    -------

    QFont.StyleHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QFont.StyleHint(number)'
      gives.
    """
    #  QFont::StyleHint QTextCharFormat::fontStyleHint() const
    return QFont.StyleHint(self.uglySide.call(
        'ritual_ZNK15QTextCharFormat13fontStyleHintEv',
    ))

  def fontStyleStrategy(self) -> QFont.StyleStrategy:
    """
    Calls Qt's 'QFont::StyleStrategy QTextCharFormat::fontStyleStrategy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#fontStyleStrategy

    Returns
    -------

    QFont.StyleStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QFont.StyleStrategy(number)' gives.
    """
    #  QFont::StyleStrategy QTextCharFormat::fontStyleStrategy() const
    return QFont.StyleStrategy(self.uglySide.call(
        'ritual_ZNK15QTextCharFormat17fontStyleStrategyEv',
    ))

  def fontHintingPreference(self) -> QFont.HintingPreference:
    """
    Calls Qt's 'QFont::HintingPreference
    QTextCharFormat::fontHintingPreference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#fontHintingPreference

    Returns
    -------

    QFont.HintingPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QFont.HintingPreference(number)' gives.
    """
    #  QFont::HintingPreference QTextCharFormat::fontHintingPreference()
    #      const
    return QFont.HintingPreference(self.uglySide.call(
        'ritual_ZNK15QTextCharFormat21fontHintingPreferenceEv',
    ))

  def fontKerning(self) -> bool:
    """
    Calls Qt's 'bool QTextCharFormat::fontKerning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#fontKerning
    """
    #  bool QTextCharFormat::fontKerning() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat11fontKerningEv')

  def underlineStyle(self) -> UnderlineStyle:
    """
    Calls Qt's 'UnderlineStyle QTextCharFormat::underlineStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#underlineStyle

    Returns
    -------

    UnderlineStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UnderlineStyle(number)'
      gives.
    """
    #  UnderlineStyle QTextCharFormat::underlineStyle() const
    return QTextCharFormat.UnderlineStyle(self.uglySide.call(
        'ritual_ZNK15QTextCharFormat14underlineStyleEv',
    ))

  def verticalAlignment(self) -> VerticalAlignment:
    """
    Calls Qt's 'VerticalAlignment QTextCharFormat::verticalAlignment()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#verticalAlignment

    Returns
    -------

    VerticalAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'VerticalAlignment(number)' gives.
    """
    #  VerticalAlignment QTextCharFormat::verticalAlignment() const
    return QTextCharFormat.VerticalAlignment(self.uglySide.call(
        'ritual_ZNK15QTextCharFormat17verticalAlignmentEv',
    ))

  def textOutline(self) -> QPen:
    """
    Calls Qt's 'QPen QTextCharFormat::textOutline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#textOutline

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QTextCharFormat::textOutline() const
    address = self.uglySide.call(
        'ritual_ZNK15QTextCharFormat11textOutlineEv',
    )
    from . import QPen
    return QPen._cuteOwning(address)

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QTextCharFormat::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextCharFormat::toolTip() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat7toolTipEv')

  def superScriptBaseline(self) -> float:
    """
    Calls Qt's 'qreal QTextCharFormat::superScriptBaseline() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#superScriptBaseline
    """
    #  qreal QTextCharFormat::superScriptBaseline() const
    return self.uglySide.call(
        'ritual_ZNK15QTextCharFormat19superScriptBaselineEv',
    )

  def subScriptBaseline(self) -> float:
    """
    Calls Qt's 'qreal QTextCharFormat::subScriptBaseline() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#subScriptBaseline
    """
    #  qreal QTextCharFormat::subScriptBaseline() const
    return self.uglySide.call(
        'ritual_ZNK15QTextCharFormat17subScriptBaselineEv',
    )

  def baselineOffset(self) -> float:
    """
    Calls Qt's 'qreal QTextCharFormat::baselineOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#baselineOffset
    """
    #  qreal QTextCharFormat::baselineOffset() const
    return self.uglySide.call(
        'ritual_ZNK15QTextCharFormat14baselineOffsetEv',
    )

  def isAnchor(self) -> bool:
    """
    Calls Qt's 'bool QTextCharFormat::isAnchor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#isAnchor
    """
    #  bool QTextCharFormat::isAnchor() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat8isAnchorEv')

  def anchorHref(self) -> str:
    """
    Calls Qt's 'QString QTextCharFormat::anchorHref() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#anchorHref

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextCharFormat::anchorHref() const
    return self.uglySide.call('ritual_ZNK15QTextCharFormat10anchorHrefEv')

  def tableCellRowSpan(self) -> int:
    """
    Calls Qt's 'int QTextCharFormat::tableCellRowSpan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#tableCellRowSpan
    """
    #  int QTextCharFormat::tableCellRowSpan() const
    return self.uglySide.call(
        'ritual_ZNK15QTextCharFormat16tableCellRowSpanEv',
    )

  def tableCellColumnSpan(self) -> int:
    """
    Calls Qt's 'int QTextCharFormat::tableCellColumnSpan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#tableCellColumnSpan
    """
    #  int QTextCharFormat::tableCellColumnSpan() const
    return self.uglySide.call(
        'ritual_ZNK15QTextCharFormat19tableCellColumnSpanEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  @overload(QFont, FontPropertiesInheritanceBehavior)
  def setFont(
      self,
      font: QFont,
      behavior: FontPropertiesInheritanceBehavior = (
          FontPropertiesInheritanceBehavior.FontPropertiesAll),
  ) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFont(const QFont &font,
    FontPropertiesInheritanceBehavior behavior)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    behavior : FontPropertiesInheritanceBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      FontPropertiesInheritanceBehavior.FontPropertiesAll.
    """
    #  void QTextCharFormat::setFont(const QFont &font,
    #      FontPropertiesInheritanceBehavior behavior)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat7setFontERK5QFontNS_33FontPropertiesInhe'
        'ritanceBehaviorE',
        self._valueOf(font), behavior.value,
    )

  @overload(str)
  def setFontFamily(self, family: str) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontFamily(const QString &family)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#setFontFamily

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextCharFormat::setFontFamily(const QString &family)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat13setFontFamilyERK7QString', family,
    )

  @overload(str)
  def setFontStyleName(self, styleName: str) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontStyleName(const QString
    &styleName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontStyleName

    Parameters
    ----------

    styleName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextCharFormat::setFontStyleName(const QString &styleName)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat16setFontStyleNameERK7QString', styleName,
    )

  @overload(float)
  def setFontPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontPointSize(qreal size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontPointSize(qreal size)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat16setFontPointSizeEd', size,
    )

  @overload(int)
  def setFontWeight(self, weight: int) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontWeight(int weight)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#setFontWeight

    Parameters
    ----------

    weight : int
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontWeight(int weight)
    self.uglySide.call('ritual_ZN15QTextCharFormat13setFontWeightEi', weight)

  @overload(bool)
  def setFontItalic(self, italic: bool) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontItalic(bool italic)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#setFontItalic

    Parameters
    ----------

    italic : bool
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontItalic(bool italic)
    self.uglySide.call('ritual_ZN15QTextCharFormat13setFontItalicEb', italic)

  @overload(QFont.Capitalization)
  def setFontCapitalization(
      self,
      capitalization: QFont.Capitalization,
  ) -> None:
    """
    Calls Qt's 'void
    QTextCharFormat::setFontCapitalization(QFont::Capitalization
    capitalization)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontCapitalization

    Parameters
    ----------

    capitalization : QFont.Capitalization
      Passed on as its number.
    """
    #  void QTextCharFormat::setFontCapitalization(QFont::Capitalization
    #      capitalization)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat21setFontCapitalizationEN5QFont14Capital'
        'izationE',
        capitalization.value,
    )

  @overload(QFont.SpacingType)
  def setFontLetterSpacingType(
      self,
      letterSpacingType: QFont.SpacingType,
  ) -> None:
    """
    Calls Qt's 'void
    QTextCharFormat::setFontLetterSpacingType(QFont::SpacingType
    letterSpacingType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontLetterSpacingType

    Parameters
    ----------

    letterSpacingType : QFont.SpacingType
      Passed on as its number.
    """
    #  void QTextCharFormat::setFontLetterSpacingType(QFont::SpacingType
    #      letterSpacingType)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat24setFontLetterSpacingTypeEN5QFont11Spac'
        'ingTypeE',
        letterSpacingType.value,
    )

  @overload(float)
  def setFontLetterSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontLetterSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontLetterSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontLetterSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat20setFontLetterSpacingEd', spacing,
    )

  @overload(float)
  def setFontWordSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontWordSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontWordSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontWordSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat18setFontWordSpacingEd', spacing,
    )

  @overload(bool)
  def setFontUnderline(self, underline: bool) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontUnderline(bool underline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontUnderline

    Parameters
    ----------

    underline : bool
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontUnderline(bool underline)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat16setFontUnderlineEb', underline,
    )

  @overload(bool)
  def setFontOverline(self, overline: bool) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontOverline(bool overline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontOverline

    Parameters
    ----------

    overline : bool
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontOverline(bool overline)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat15setFontOverlineEb', overline,
    )

  @overload(bool)
  def setFontStrikeOut(self, strikeOut: bool) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontStrikeOut(bool strikeOut)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontStrikeOut

    Parameters
    ----------

    strikeOut : bool
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontStrikeOut(bool strikeOut)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat16setFontStrikeOutEb', strikeOut,
    )

  @overload(QColor)
  def setUnderlineColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setUnderlineColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setUnderlineColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QTextCharFormat::setUnderlineColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat17setUnderlineColorERK6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setFontFixedPitch(self, fixedPitch: bool) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontFixedPitch(bool fixedPitch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontFixedPitch

    Parameters
    ----------

    fixedPitch : bool
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontFixedPitch(bool fixedPitch)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat17setFontFixedPitchEb', fixedPitch,
    )

  @overload(int)
  def setFontStretch(self, factor: int) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontStretch(int factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontStretch

    Parameters
    ----------

    factor : int
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontStretch(int factor)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat14setFontStretchEi', factor,
    )

  @overload(QFont.StyleHint)
  @overload(QFont.StyleHint, QFont.StyleStrategy)
  def setFontStyleHint(
      self,
      hint: QFont.StyleHint,
      strategy: QFont.StyleStrategy = QFont.StyleStrategy.PreferDefault,
  ) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontStyleHint(QFont::StyleHint hint,
    QFont::StyleStrategy strategy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontStyleHint

    Parameters
    ----------

    hint : QFont.StyleHint
      Passed on as its number.

    strategy : QFont.StyleStrategy
      Passed on as its number. May be left out, as in Qt: it is then
      QFont.StyleStrategy.PreferDefault.
    """
    #  void QTextCharFormat::setFontStyleHint(QFont::StyleHint hint,
    #      QFont::StyleStrategy strategy)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat16setFontStyleHintEN5QFont9StyleHintENS0'
        '_13StyleStrategyE',
        hint.value, strategy.value,
    )

  @overload(QFont.StyleStrategy)
  def setFontStyleStrategy(self, strategy: QFont.StyleStrategy) -> None:
    """
    Calls Qt's 'void
    QTextCharFormat::setFontStyleStrategy(QFont::StyleStrategy strategy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontStyleStrategy

    Parameters
    ----------

    strategy : QFont.StyleStrategy
      Passed on as its number.
    """
    #  void QTextCharFormat::setFontStyleStrategy(QFont::StyleStrategy
    #      strategy)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat20setFontStyleStrategyEN5QFont13StyleStr'
        'ategyE',
        strategy.value,
    )

  @overload(QFont.HintingPreference)
  def setFontHintingPreference(
      self,
      hintingPreference: QFont.HintingPreference,
  ) -> None:
    """
    Calls Qt's 'void
    QTextCharFormat::setFontHintingPreference(QFont::HintingPreference
    hintingPreference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontHintingPreference

    Parameters
    ----------

    hintingPreference : QFont.HintingPreference
      Passed on as its number.
    """
    #  void
    #      QTextCharFormat::setFontHintingPreference(QFont::HintingPreference
    #      hintingPreference)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat24setFontHintingPreferenceEN5QFont17Hint'
        'ingPreferenceE',
        hintingPreference.value,
    )

  @overload(bool)
  def setFontKerning(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setFontKerning(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setFontKerning

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTextCharFormat::setFontKerning(bool enable)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat14setFontKerningEb', enable,
    )

  @overload(UnderlineStyle)
  def setUnderlineStyle(self, style: UnderlineStyle) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setUnderlineStyle(UnderlineStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setUnderlineStyle

    Parameters
    ----------

    style : UnderlineStyle
      Passed on as its number.
    """
    #  void QTextCharFormat::setUnderlineStyle(UnderlineStyle style)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat17setUnderlineStyleENS_14UnderlineStyleE',
        style.value,
    )

  @overload(VerticalAlignment)
  def setVerticalAlignment(self, alignment: VerticalAlignment) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setVerticalAlignment(VerticalAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setVerticalAlignment

    Parameters
    ----------

    alignment : VerticalAlignment
      Passed on as its number.
    """
    #  void QTextCharFormat::setVerticalAlignment(VerticalAlignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat20setVerticalAlignmentENS_17VerticalAlig'
        'nmentE',
        alignment.value,
    )

  @overload(QPen)
  def setTextOutline(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setTextOutline(const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setTextOutline

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QTextCharFormat::setTextOutline(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat14setTextOutlineERK4QPen',
        self._valueOf(pen),
    )

  @overload(str)
  def setToolTip(self, tip: str) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setToolTip(const QString &tip)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#setToolTip

    Parameters
    ----------

    tip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextCharFormat::setToolTip(const QString &tip)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat10setToolTipERK7QString', tip,
    )

  @overload(float)
  def setSuperScriptBaseline(self, baseline: float) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setSuperScriptBaseline(qreal
    baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setSuperScriptBaseline

    Parameters
    ----------

    baseline : float
      Passed on as it is.
    """
    #  void QTextCharFormat::setSuperScriptBaseline(qreal baseline)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat22setSuperScriptBaselineEd', baseline,
    )

  @overload(float)
  def setSubScriptBaseline(self, baseline: float) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setSubScriptBaseline(qreal baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setSubScriptBaseline

    Parameters
    ----------

    baseline : float
      Passed on as it is.
    """
    #  void QTextCharFormat::setSubScriptBaseline(qreal baseline)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat20setSubScriptBaselineEd', baseline,
    )

  @overload(float)
  def setBaselineOffset(self, baseline: float) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setBaselineOffset(qreal baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setBaselineOffset

    Parameters
    ----------

    baseline : float
      Passed on as it is.
    """
    #  void QTextCharFormat::setBaselineOffset(qreal baseline)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat17setBaselineOffsetEd', baseline,
    )

  @overload(bool)
  def setAnchor(self, anchor: bool) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setAnchor(bool anchor)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#setAnchor

    Parameters
    ----------

    anchor : bool
      Passed on as it is.
    """
    #  void QTextCharFormat::setAnchor(bool anchor)
    self.uglySide.call('ritual_ZN15QTextCharFormat9setAnchorEb', anchor)

  @overload(str)
  def setAnchorHref(self, value: str) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setAnchorHref(const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcharformat.html#setAnchorHref

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextCharFormat::setAnchorHref(const QString &value)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat13setAnchorHrefERK7QString', value,
    )

  @overload(int)
  def setTableCellRowSpan(self, tableCellRowSpan: int) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setTableCellRowSpan(int
    tableCellRowSpan)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setTableCellRowSpan

    Parameters
    ----------

    tableCellRowSpan : int
      Passed on as it is.
    """
    #  void QTextCharFormat::setTableCellRowSpan(int tableCellRowSpan)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat19setTableCellRowSpanEi',
        tableCellRowSpan,
    )

  @overload(int)
  def setTableCellColumnSpan(self, tableCellColumnSpan: int) -> None:
    """
    Calls Qt's 'void QTextCharFormat::setTableCellColumnSpan(int
    tableCellColumnSpan)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#setTableCellColumnSpan

    Parameters
    ----------

    tableCellColumnSpan : int
      Passed on as it is.
    """
    #  void QTextCharFormat::setTableCellColumnSpan(int tableCellColumnSpan)
    self.uglySide.call(
        'ritual_ZN15QTextCharFormat22setTableCellColumnSpanEi',
        tableCellColumnSpan,
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
    Notes what was given, for Qt's 'QTextCharFormat::QTextCharFormat()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcharformat.html#QTextCharFormat
    """
    #  QTextCharFormat::QTextCharFormat()
    self._noteCreation(QTextCharFormat, lambda: Rituals.call(
        'ritual_ZN15QTextCharFormatC1Ev',
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
