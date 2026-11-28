"""
QQuickMaterialStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Material/6.12.0/QtQuickControls2Material/private/qquickmaterialstyle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMaterialStyle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject, QVariant
  from ..QtGui import QColor
  from ..QtQuickControls2 import QQuickAttachedPropertyPropagator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QObject = WAIT['QObject']
  QQuickAttachedPropertyPropagator = WAIT['QQuickAttachedPropertyPropagator']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMaterialStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickMaterialStyle: a plain Python object standing
  in front of one C++ QQuickMaterialStyle.

  What exists
  -----------

  Every function of Qt's QQuickMaterialStyle that has a ritual and that
  Python can call so far, 125 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'theme', 'setTheme', 'inheritTheme',
  'propagateTheme', 'resetTheme', 'themeChange', 'primary', 'setPrimary',
  'inheritPrimary', 'propagatePrimary', 'resetPrimary', 'primaryChange',
  'accent', 'setAccent', 'inheritAccent', 'propagateAccent', 'resetAccent',
  'accentChange', 'foreground', 'setForeground', 'inheritForeground',
  'propagateForeground', 'resetForeground', 'foregroundChange', 'background',
  'setBackground', 'inheritBackground', 'propagateBackground',
  'resetBackground', 'backgroundChange', 'elevation', 'setElevation',
  'resetElevation', 'elevationChange', 'roundedScale', 'setRoundedScale',
  'resetRoundedScale', 'containerStyle', 'setContainerStyle',
  'resetContainerStyle', 'primaryColor', 'accentColor', 'backgroundColor',
  'primaryTextColor', 'primaryHighlightedTextColor', 'secondaryTextColor',
  'hintTextColor', 'textSelectionColor', 'dropShadowColor', 'dividerColor',
  'iconColor', 'iconDisabledColor', 'buttonColor', 'frameColor',
  'rippleColor', 'highlightedRippleColor', 'switchUncheckedTrackColor',
  'switchCheckedTrackColor', 'switchDisabledUncheckedTrackColor',
  'switchDisabledCheckedTrackColor',
  'switchDisabledUncheckedTrackBorderColor', 'switchUncheckedHandleColor',
  'switchUncheckedHoveredHandleColor', 'switchCheckedHandleColor',
  'switchDisabledUncheckedHandleColor', 'switchDisabledCheckedHandleColor',
  'switchDisabledCheckedIconColor', 'switchDisabledUncheckedIconColor',
  'scrollBarColor', 'scrollBarHoveredColor', 'scrollBarPressedColor',
  'dialogColor', 'backgroundDimColor', 'listHighlightColor', 'tooltipColor',
  'toolBarColor', 'toolTextColor', 'spinBoxDisabledIconColor',
  'sliderDisabledColor', 'textFieldFilledContainerColor', 'color', 'shade',
  'touchTarget', 'buttonVerticalPadding', 'buttonLeftPadding',
  'buttonRightPadding', 'buttonHeight', 'delegateHeight',
  'dialogButtonBoxHeight', 'dialogTitleFontPixelSize', 'dialogRoundedScale',
  'frameVerticalPadding', 'menuItemHeight', 'menuItemVerticalPadding',
  'switchIndicatorWidth', 'switchIndicatorHeight',
  'switchNormalHandleHeight', 'switchCheckedHandleHeight',
  'switchLargestHandleHeight', 'switchDelegateVerticalPadding',
  'textFieldHeight', 'textFieldHorizontalPadding',
  'textFieldVerticalPadding', 'tooltipHeight', 'initGlobals', 'variant',
  'themeChanged', 'primaryChanged', 'accentChanged', 'foregroundChanged',
  'backgroundChanged', 'elevationChanged', 'themeOrAccentChanged',
  'primaryHighlightedTextColorChanged', 'dialogColorChanged',
  'tooltipColorChanged', 'toolBarColorChanged', 'toolTextColorChanged',
  'roundedScaleChanged', 'containerStyleChanged', 'attachedParentChange',
  'themeShade'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMaterialStyle::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickMaterialStyle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickMaterialStyle::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickMaterialStyle::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'bool QQuickMaterialStyle::variantToRgba(const QVariant &var, const
    char *name, QRgb *rgba, bool *custom) const': takes a number to change
    where it is.

  What has no ritual
  ------------------

  3 of the 136 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickMaterialStyle is created at the first use, not by
    'QQuickMaterialStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMaterialStyle.
  - Qt tells when it has removed the C++ QQuickMaterialStyle. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMaterialStyle that has no cute function yet,
    'variantToRgba', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQuickMaterialStyle, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Color(CuteNum):
    """
    The enum 'QQuickMaterialStyle::Color' of Qt, with the 19 names Qt gives
    in it.
    """

    Red = Kee[int](0)
    Pink = Kee[int](1)
    Purple = Kee[int](2)
    DeepPurple = Kee[int](3)
    Indigo = Kee[int](4)
    Blue = Kee[int](5)
    LightBlue = Kee[int](6)
    Cyan = Kee[int](7)
    Teal = Kee[int](8)
    Green = Kee[int](9)
    LightGreen = Kee[int](10)
    Lime = Kee[int](11)
    Yellow = Kee[int](12)
    Amber = Kee[int](13)
    Orange = Kee[int](14)
    DeepOrange = Kee[int](15)
    Brown = Kee[int](16)
    Grey = Kee[int](17)
    BlueGrey = Kee[int](18)

  class ContainerStyle(CuteNum, scoped=True):
    """
    The enum 'QQuickMaterialStyle::ContainerStyle' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Filled = Kee[int](0)
    Outlined = Kee[int](1)

  class RoundedScale(CuteNum, scoped=True):
    """
    The enum 'QQuickMaterialStyle::RoundedScale' of Qt, with the 7 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NotRounded = Kee[int](0)
    ExtraSmallScale = Kee[int](4)
    SmallScale = Kee[int](8)
    MediumScale = Kee[int](12)
    LargeScale = Kee[int](16)
    ExtraLargeScale = Kee[int](28)
    FullScale = Kee[int](255)

  class Shade(CuteNum):
    """
    The enum 'QQuickMaterialStyle::Shade' of Qt, with the 14 names Qt gives
    in it.
    """

    Shade50 = Kee[int](0)
    Shade100 = Kee[int](1)
    Shade200 = Kee[int](2)
    Shade300 = Kee[int](3)
    Shade400 = Kee[int](4)
    Shade500 = Kee[int](5)
    Shade600 = Kee[int](6)
    Shade700 = Kee[int](7)
    Shade800 = Kee[int](8)
    Shade900 = Kee[int](9)
    ShadeA100 = Kee[int](10)
    ShadeA200 = Kee[int](11)
    ShadeA400 = Kee[int](12)
    ShadeA700 = Kee[int](13)

  class Theme(CuteNum):
    """
    The enum 'QQuickMaterialStyle::Theme' of Qt, with the 3 names Qt gives in
    it.
    """

    Light = Kee[int](0)
    Dark = Kee[int](1)
    System = Kee[int](2)

  class Variant(CuteNum):
    """
    The enum 'QQuickMaterialStyle::Variant' of Qt, with the 2 names Qt gives
    in it.
    """

    Normal = Kee[int](0)
    Dense = Kee[int](1)

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
    Calls Qt's 'QString QQuickMaterialStyle::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#tr

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
    #  QString QQuickMaterialStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickMaterialStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickMaterialStyle]:
    """
    Calls Qt's 'QQuickMaterialStyle
    *QQuickMaterialStyle::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickMaterialStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMaterialStyle
    #      *QQuickMaterialStyle::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN19QQuickMaterialStyle21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QQuickMaterialStyle._cuteAt(address)

  @staticmethod
  def initGlobals() -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::initGlobals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#initGlobals
    """
    #  void QQuickMaterialStyle::initGlobals()
    Rituals.call('ritual_ZN19QQuickMaterialStyle11initGlobalsEv')

  @staticmethod
  def variant() -> Variant:
    """
    Calls Qt's 'Variant QQuickMaterialStyle::variant()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#variant

    Returns
    -------

    Variant
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Variant(number)' gives.
    """
    #  Variant QQuickMaterialStyle::variant()
    return QQuickMaterialStyle.Variant(Rituals.call(
        'ritual_ZN19QQuickMaterialStyle7variantEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMaterialStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMaterialStyle::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMaterialStyle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def theme(self) -> Theme:
    """
    Calls Qt's 'Theme QQuickMaterialStyle::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#theme

    Returns
    -------

    Theme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Theme(number)' gives.
    """
    #  Theme QQuickMaterialStyle::theme() const
    return QQuickMaterialStyle.Theme(self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle5themeEv',
    ))

  def primary(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickMaterialStyle::primary() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#primary

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickMaterialStyle::primary() const
    address = self.uglySide.call('ritual_ZNK19QQuickMaterialStyle7primaryEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def accent(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickMaterialStyle::accent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#accent

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickMaterialStyle::accent() const
    address = self.uglySide.call('ritual_ZNK19QQuickMaterialStyle6accentEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def foreground(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickMaterialStyle::foreground() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#foreground

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickMaterialStyle::foreground() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle10foregroundEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def background(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickMaterialStyle::background() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#background

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickMaterialStyle::background() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle10backgroundEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def elevation(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::elevation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#elevation
    """
    #  int QQuickMaterialStyle::elevation() const
    return self.uglySide.call('ritual_ZNK19QQuickMaterialStyle9elevationEv')

  def roundedScale(self) -> RoundedScale:
    """
    Calls Qt's 'RoundedScale QQuickMaterialStyle::roundedScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#roundedScale

    Returns
    -------

    RoundedScale
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RoundedScale(number)'
      gives.
    """
    #  RoundedScale QQuickMaterialStyle::roundedScale() const
    return QQuickMaterialStyle.RoundedScale(self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle12roundedScaleEv',
    ))

  def containerStyle(self) -> ContainerStyle:
    """
    Calls Qt's 'ContainerStyle QQuickMaterialStyle::containerStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#containerStyle

    Returns
    -------

    ContainerStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ContainerStyle(number)'
      gives.
    """
    #  ContainerStyle QQuickMaterialStyle::containerStyle() const
    return QQuickMaterialStyle.ContainerStyle(self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle14containerStyleEv',
    ))

  def primaryColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::primaryColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#primaryColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::primaryColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle12primaryColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload()
  def accentColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::accentColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#accentColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::accentColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle11accentColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(Shade)
  def accentColor(self, shade: Shade) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::accentColor(Shade shade) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#accentColor

    Parameters
    ----------

    shade : Shade
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::accentColor(Shade shade) const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle11accentColorENS_5ShadeE',
        shade.value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload()
  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::backgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::backgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle15backgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(Shade)
  def backgroundColor(self, shade: Shade) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::backgroundColor(Shade shade)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#backgroundColor

    Parameters
    ----------

    shade : Shade
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::backgroundColor(Shade shade) const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle15backgroundColorENS_5ShadeE',
        shade.value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def primaryTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::primaryTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#primaryTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::primaryTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle16primaryTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def primaryHighlightedTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::primaryHighlightedTextColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::primaryHighlightedTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle27primaryHighlightedTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def secondaryTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::secondaryTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#secondaryTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::secondaryTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle18secondaryTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def hintTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::hintTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#hintTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::hintTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle13hintTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def textSelectionColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::textSelectionColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#textSelectionColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::textSelectionColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle18textSelectionColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def dropShadowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::dropShadowColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#dropShadowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::dropShadowColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle15dropShadowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def dividerColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::dividerColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#dividerColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::dividerColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle12dividerColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def iconColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::iconColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#iconColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::iconColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle9iconColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def iconDisabledColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::iconDisabledColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#iconDisabledColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::iconDisabledColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle17iconDisabledColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(Theme, QVariant, QVariant, bool, bool, bool, bool)
  def buttonColor(
      self,
      theme: Theme,
      background: QVariant,
      accent: QVariant,
      enabled: bool,
      flat: bool,
      highlighted: bool,
      checked: bool,
  ) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::buttonColor(Theme theme, const
    QVariant &background, const QVariant &accent, bool enabled, bool flat,
    bool highlighted, bool checked) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#buttonColor

    Parameters
    ----------

    theme : Theme
      Passed on as its number.

    background : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    accent : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    enabled : bool
      Passed on as it is.

    flat : bool
      Passed on as it is.

    highlighted : bool
      Passed on as it is.

    checked : bool
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::buttonColor(Theme theme, const QVariant
    #      &background, const QVariant &accent, bool enabled, bool flat, bool
    #      highlighted, bool checked) const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle11buttonColorENS_5ThemeERK8QVariant'
        'S3_bbbb',
        theme.value, self._valueOf(background), self._valueOf(accent),
        enabled, flat, highlighted, checked,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def frameColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::frameColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#frameColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::frameColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle10frameColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def rippleColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::rippleColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#rippleColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::rippleColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle11rippleColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def highlightedRippleColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::highlightedRippleColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#highlightedRippleColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::highlightedRippleColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle22highlightedRippleColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchUncheckedTrackColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::switchUncheckedTrackColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#switchUncheckedTrackColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchUncheckedTrackColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle25switchUncheckedTrackColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchCheckedTrackColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::switchCheckedTrackColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#switchCheckedTrackColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchCheckedTrackColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle23switchCheckedTrackColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchDisabledUncheckedTrackColor(self) -> QColor:
    """
    Calls Qt's 'QColor
    QQuickMaterialStyle::switchDisabledUncheckedTrackColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchDisabledUncheckedTrackColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle33switchDisabledUncheckedTrackColor'
        'Ev',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchDisabledCheckedTrackColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::switchDisabledCheckedTrackColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchDisabledCheckedTrackColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle31switchDisabledCheckedTrackColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchDisabledUncheckedTrackBorderColor(self) -> QColor:
    """
    Calls Qt's 'QColor
    QQuickMaterialStyle::switchDisabledUncheckedTrackBorderColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchDisabledUncheckedTrackBorderColor()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle39switchDisabledUncheckedTrackBorde'
        'rColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchUncheckedHandleColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::switchUncheckedHandleColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchUncheckedHandleColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle26switchUncheckedHandleColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchUncheckedHoveredHandleColor(self) -> QColor:
    """
    Calls Qt's 'QColor
    QQuickMaterialStyle::switchUncheckedHoveredHandleColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchUncheckedHoveredHandleColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle33switchUncheckedHoveredHandleColor'
        'Ev',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchCheckedHandleColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::switchCheckedHandleColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#switchCheckedHandleColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchCheckedHandleColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle24switchCheckedHandleColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchDisabledUncheckedHandleColor(self) -> QColor:
    """
    Calls Qt's 'QColor
    QQuickMaterialStyle::switchDisabledUncheckedHandleColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchDisabledUncheckedHandleColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle34switchDisabledUncheckedHandleColo'
        'rEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchDisabledCheckedHandleColor(self) -> QColor:
    """
    Calls Qt's 'QColor
    QQuickMaterialStyle::switchDisabledCheckedHandleColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchDisabledCheckedHandleColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle32switchDisabledCheckedHandleColorE'
        'v',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchDisabledCheckedIconColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::switchDisabledCheckedIconColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchDisabledCheckedIconColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle30switchDisabledCheckedIconColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def switchDisabledUncheckedIconColor(self) -> QColor:
    """
    Calls Qt's 'QColor
    QQuickMaterialStyle::switchDisabledUncheckedIconColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::switchDisabledUncheckedIconColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle32switchDisabledUncheckedIconColorE'
        'v',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def scrollBarColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::scrollBarColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#scrollBarColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::scrollBarColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle14scrollBarColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def scrollBarHoveredColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::scrollBarHoveredColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#scrollBarHoveredColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::scrollBarHoveredColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle21scrollBarHoveredColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def scrollBarPressedColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::scrollBarPressedColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#scrollBarPressedColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::scrollBarPressedColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle21scrollBarPressedColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def dialogColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::dialogColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#dialogColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::dialogColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle11dialogColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def backgroundDimColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::backgroundDimColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#backgroundDimColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::backgroundDimColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle18backgroundDimColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def listHighlightColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::listHighlightColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#listHighlightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::listHighlightColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle18listHighlightColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def tooltipColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::tooltipColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#tooltipColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::tooltipColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle12tooltipColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def toolBarColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::toolBarColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#toolBarColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::toolBarColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle12toolBarColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def toolTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::toolTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#toolTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::toolTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle13toolTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def spinBoxDisabledIconColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::spinBoxDisabledIconColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#spinBoxDisabledIconColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::spinBoxDisabledIconColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle24spinBoxDisabledIconColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def sliderDisabledColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::sliderDisabledColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#sliderDisabledColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::sliderDisabledColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle19sliderDisabledColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def textFieldFilledContainerColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::textFieldFilledContainerColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::textFieldFilledContainerColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle29textFieldFilledContainerColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(Color)
  @overload(Color, Shade)
  def color(self, color: Color, shade: Shade = Shade.Shade500) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::color(Color color, Shade shade)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#color

    Parameters
    ----------

    color : Color
      Passed on as its number.

    shade : Shade
      Passed on as its number. May be left out, as in Qt: it is then
      Shade.Shade500.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::color(Color color, Shade shade) const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle5colorENS_5ColorENS_5ShadeE',
        color.value, shade.value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QColor, Shade)
  def shade(self, color: QColor, shade: Shade) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialStyle::shade(const QColor &color, Shade
    shade) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#shade

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    shade : Shade
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialStyle::shade(const QColor &color, Shade shade)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle5shadeERK6QColorNS_5ShadeE',
        self._valueOf(color), shade.value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def touchTarget(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::touchTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#touchTarget
    """
    #  int QQuickMaterialStyle::touchTarget() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle11touchTargetEv',
    )

  def buttonVerticalPadding(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::buttonVerticalPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#buttonVerticalPadding
    """
    #  int QQuickMaterialStyle::buttonVerticalPadding() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle21buttonVerticalPaddingEv',
    )

  @overload(bool, bool)
  def buttonLeftPadding(self, flat: bool, hasIcon: bool) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::buttonLeftPadding(bool flat, bool
    hasIcon) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#buttonLeftPadding

    Parameters
    ----------

    flat : bool
      Passed on as it is.

    hasIcon : bool
      Passed on as it is.
    """
    #  int QQuickMaterialStyle::buttonLeftPadding(bool flat, bool hasIcon)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle17buttonLeftPaddingEbb',
        flat, hasIcon,
    )

  @overload(bool, bool, bool)
  def buttonRightPadding(
      self,
      flat: bool,
      hasIcon: bool,
      hasText: bool,
  ) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::buttonRightPadding(bool flat, bool
    hasIcon, bool hasText) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#buttonRightPadding

    Parameters
    ----------

    flat : bool
      Passed on as it is.

    hasIcon : bool
      Passed on as it is.

    hasText : bool
      Passed on as it is.
    """
    #  int QQuickMaterialStyle::buttonRightPadding(bool flat, bool hasIcon,
    #      bool hasText) const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle18buttonRightPaddingEbbb',
        flat, hasIcon, hasText,
    )

  def buttonHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::buttonHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#buttonHeight
    """
    #  int QQuickMaterialStyle::buttonHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle12buttonHeightEv',
    )

  def delegateHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::delegateHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#delegateHeight
    """
    #  int QQuickMaterialStyle::delegateHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle14delegateHeightEv',
    )

  def dialogButtonBoxHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::dialogButtonBoxHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#dialogButtonBoxHeight
    """
    #  int QQuickMaterialStyle::dialogButtonBoxHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle21dialogButtonBoxHeightEv',
    )

  def dialogTitleFontPixelSize(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::dialogTitleFontPixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#dialogTitleFontPixelSize
    """
    #  int QQuickMaterialStyle::dialogTitleFontPixelSize() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle24dialogTitleFontPixelSizeEv',
    )

  def dialogRoundedScale(self) -> RoundedScale:
    """
    Calls Qt's 'RoundedScale QQuickMaterialStyle::dialogRoundedScale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#dialogRoundedScale

    Returns
    -------

    RoundedScale
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RoundedScale(number)'
      gives.
    """
    #  RoundedScale QQuickMaterialStyle::dialogRoundedScale() const
    return QQuickMaterialStyle.RoundedScale(self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle18dialogRoundedScaleEv',
    ))

  def frameVerticalPadding(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::frameVerticalPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#frameVerticalPadding
    """
    #  int QQuickMaterialStyle::frameVerticalPadding() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle20frameVerticalPaddingEv',
    )

  def menuItemHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::menuItemHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#menuItemHeight
    """
    #  int QQuickMaterialStyle::menuItemHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle14menuItemHeightEv',
    )

  def menuItemVerticalPadding(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::menuItemVerticalPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#menuItemVerticalPadding
    """
    #  int QQuickMaterialStyle::menuItemVerticalPadding() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle23menuItemVerticalPaddingEv',
    )

  def switchIndicatorWidth(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::switchIndicatorWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#switchIndicatorWidth
    """
    #  int QQuickMaterialStyle::switchIndicatorWidth() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle20switchIndicatorWidthEv',
    )

  def switchIndicatorHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::switchIndicatorHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#switchIndicatorHeight
    """
    #  int QQuickMaterialStyle::switchIndicatorHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle21switchIndicatorHeightEv',
    )

  def switchNormalHandleHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::switchNormalHandleHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#switchNormalHandleHeight
    """
    #  int QQuickMaterialStyle::switchNormalHandleHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle24switchNormalHandleHeightEv',
    )

  def switchCheckedHandleHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::switchCheckedHandleHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#switchCheckedHandleHeight
    """
    #  int QQuickMaterialStyle::switchCheckedHandleHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle25switchCheckedHandleHeightEv',
    )

  def switchLargestHandleHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::switchLargestHandleHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#switchLargestHandleHeight
    """
    #  int QQuickMaterialStyle::switchLargestHandleHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle25switchLargestHandleHeightEv',
    )

  def switchDelegateVerticalPadding(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::switchDelegateVerticalPadding()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html
    """
    #  int QQuickMaterialStyle::switchDelegateVerticalPadding() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle29switchDelegateVerticalPaddingEv',
    )

  def textFieldHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::textFieldHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#textFieldHeight
    """
    #  int QQuickMaterialStyle::textFieldHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle15textFieldHeightEv',
    )

  def textFieldHorizontalPadding(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::textFieldHorizontalPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html
    """
    #  int QQuickMaterialStyle::textFieldHorizontalPadding() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle26textFieldHorizontalPaddingEv',
    )

  def textFieldVerticalPadding(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::textFieldVerticalPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#textFieldVerticalPadding
    """
    #  int QQuickMaterialStyle::textFieldVerticalPadding() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle24textFieldVerticalPaddingEv',
    )

  def tooltipHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialStyle::tooltipHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#tooltipHeight
    """
    #  int QQuickMaterialStyle::tooltipHeight() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle13tooltipHeightEv',
    )

  def themeShade(self) -> Shade:
    """
    Calls Qt's 'Shade QQuickMaterialStyle::themeShade() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#themeShade

    Returns
    -------

    Shade
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Shade(number)' gives.
    """
    #  Shade QQuickMaterialStyle::themeShade() const
    return QQuickMaterialStyle.Shade(self.uglySide.call(
        'ritual_ZNK19QQuickMaterialStyle10themeShadeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Theme)
  def setTheme(self, theme: Theme) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::setTheme(Theme theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#setTheme

    Parameters
    ----------

    theme : Theme
      Passed on as its number.
    """
    #  void QQuickMaterialStyle::setTheme(Theme theme)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle8setThemeENS_5ThemeE', theme.value,
    )

  @overload(QVariant)
  def setPrimary(self, accent: QVariant) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::setPrimary(const QVariant
    &accent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#setPrimary

    Parameters
    ----------

    accent : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickMaterialStyle::setPrimary(const QVariant &accent)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle10setPrimaryERK8QVariant',
        self._valueOf(accent),
    )

  @overload(QVariant)
  def setAccent(self, accent: QVariant) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::setAccent(const QVariant &accent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaterialstyle.html#setAccent

    Parameters
    ----------

    accent : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickMaterialStyle::setAccent(const QVariant &accent)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle9setAccentERK8QVariant',
        self._valueOf(accent),
    )

  @overload(QVariant)
  def setForeground(self, foreground: QVariant) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::setForeground(const QVariant
    &foreground)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#setForeground

    Parameters
    ----------

    foreground : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickMaterialStyle::setForeground(const QVariant &foreground)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle13setForegroundERK8QVariant',
        self._valueOf(foreground),
    )

  @overload(QVariant)
  def setBackground(self, background: QVariant) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::setBackground(const QVariant
    &background)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#setBackground

    Parameters
    ----------

    background : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickMaterialStyle::setBackground(const QVariant &background)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle13setBackgroundERK8QVariant',
        self._valueOf(background),
    )

  @overload(int)
  def setElevation(self, elevation: int) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::setElevation(int elevation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#setElevation

    Parameters
    ----------

    elevation : int
      Passed on as it is.
    """
    #  void QQuickMaterialStyle::setElevation(int elevation)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle12setElevationEi', elevation,
    )

  @overload(RoundedScale)
  def setRoundedScale(self, roundedScale: RoundedScale) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::setRoundedScale(RoundedScale
    roundedScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#setRoundedScale

    Parameters
    ----------

    roundedScale : RoundedScale
      Passed on as its number.
    """
    #  void QQuickMaterialStyle::setRoundedScale(RoundedScale roundedScale)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle15setRoundedScaleENS_12RoundedScaleE',
        roundedScale.value,
    )

  @overload(ContainerStyle)
  def setContainerStyle(self, containerStyle: ContainerStyle) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::setContainerStyle(ContainerStyle
    containerStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#setContainerStyle

    Parameters
    ----------

    containerStyle : ContainerStyle
      Passed on as its number.
    """
    #  void QQuickMaterialStyle::setContainerStyle(ContainerStyle
    #      containerStyle)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle17setContainerStyleENS_14ContainerSt'
        'yleE',
        containerStyle.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMaterialStyle::QQuickMaterialStyle(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#QQuickMaterialStyle

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMaterialStyle::QQuickMaterialStyle(QObject *parent)
    self._noteCreation(QQuickMaterialStyle, lambda: Rituals.call(
        'ritual_ZN19QQuickMaterialStyleC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(Theme)
  def inheritTheme(self, theme: Theme) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::inheritTheme(Theme theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#inheritTheme

    Parameters
    ----------

    theme : Theme
      Passed on as its number.
    """
    #  void QQuickMaterialStyle::inheritTheme(Theme theme)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle12inheritThemeENS_5ThemeE',
        theme.value,
    )

  def propagateTheme(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::propagateTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#propagateTheme
    """
    #  void QQuickMaterialStyle::propagateTheme()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle14propagateThemeEv')

  def resetTheme(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::resetTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#resetTheme
    """
    #  void QQuickMaterialStyle::resetTheme()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle10resetThemeEv')

  def themeChange(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::themeChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#themeChange
    """
    #  void QQuickMaterialStyle::themeChange()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle11themeChangeEv')

  @overload(int, bool)
  def inheritPrimary(self, primary: int, custom: bool) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::inheritPrimary(uint primary, bool
    custom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#inheritPrimary

    Parameters
    ----------

    primary : int
      Passed on as it is.

    custom : bool
      Passed on as it is.
    """
    #  void QQuickMaterialStyle::inheritPrimary(uint primary, bool custom)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle14inheritPrimaryEjb', primary, custom,
    )

  def propagatePrimary(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::propagatePrimary()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#propagatePrimary
    """
    #  void QQuickMaterialStyle::propagatePrimary()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle16propagatePrimaryEv')

  def resetPrimary(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::resetPrimary()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#resetPrimary
    """
    #  void QQuickMaterialStyle::resetPrimary()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle12resetPrimaryEv')

  def primaryChange(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::primaryChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#primaryChange
    """
    #  void QQuickMaterialStyle::primaryChange()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle13primaryChangeEv')

  @overload(int, bool)
  def inheritAccent(self, accent: int, custom: bool) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::inheritAccent(uint accent, bool
    custom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#inheritAccent

    Parameters
    ----------

    accent : int
      Passed on as it is.

    custom : bool
      Passed on as it is.
    """
    #  void QQuickMaterialStyle::inheritAccent(uint accent, bool custom)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle13inheritAccentEjb', accent, custom,
    )

  def propagateAccent(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::propagateAccent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#propagateAccent
    """
    #  void QQuickMaterialStyle::propagateAccent()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle15propagateAccentEv')

  def resetAccent(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::resetAccent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#resetAccent
    """
    #  void QQuickMaterialStyle::resetAccent()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle11resetAccentEv')

  def accentChange(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::accentChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#accentChange
    """
    #  void QQuickMaterialStyle::accentChange()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle12accentChangeEv')

  @overload(int, bool, bool)
  def inheritForeground(
      self,
      foreground: int,
      custom: bool,
      has: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::inheritForeground(uint foreground,
    bool custom, bool has)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#inheritForeground

    Parameters
    ----------

    foreground : int
      Passed on as it is.

    custom : bool
      Passed on as it is.

    has : bool
      Passed on as it is.
    """
    #  void QQuickMaterialStyle::inheritForeground(uint foreground, bool
    #      custom, bool has)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle17inheritForegroundEjbb',
        foreground, custom, has,
    )

  def propagateForeground(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::propagateForeground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#propagateForeground
    """
    #  void QQuickMaterialStyle::propagateForeground()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle19propagateForegroundEv',
    )

  def resetForeground(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::resetForeground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#resetForeground
    """
    #  void QQuickMaterialStyle::resetForeground()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle15resetForegroundEv')

  def foregroundChange(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::foregroundChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#foregroundChange
    """
    #  void QQuickMaterialStyle::foregroundChange()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle16foregroundChangeEv')

  @overload(int, bool, bool)
  def inheritBackground(
      self,
      background: int,
      custom: bool,
      has: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::inheritBackground(uint background,
    bool custom, bool has)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#inheritBackground

    Parameters
    ----------

    background : int
      Passed on as it is.

    custom : bool
      Passed on as it is.

    has : bool
      Passed on as it is.
    """
    #  void QQuickMaterialStyle::inheritBackground(uint background, bool
    #      custom, bool has)
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle17inheritBackgroundEjbb',
        background, custom, has,
    )

  def propagateBackground(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::propagateBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#propagateBackground
    """
    #  void QQuickMaterialStyle::propagateBackground()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle19propagateBackgroundEv',
    )

  def resetBackground(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::resetBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#resetBackground
    """
    #  void QQuickMaterialStyle::resetBackground()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle15resetBackgroundEv')

  def backgroundChange(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::backgroundChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#backgroundChange
    """
    #  void QQuickMaterialStyle::backgroundChange()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle16backgroundChangeEv')

  def resetElevation(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::resetElevation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#resetElevation
    """
    #  void QQuickMaterialStyle::resetElevation()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle14resetElevationEv')

  def elevationChange(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::elevationChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#elevationChange
    """
    #  void QQuickMaterialStyle::elevationChange()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle15elevationChangeEv')

  def resetRoundedScale(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::resetRoundedScale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#resetRoundedScale
    """
    #  void QQuickMaterialStyle::resetRoundedScale()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle17resetRoundedScaleEv')

  def resetContainerStyle(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::resetContainerStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#resetContainerStyle
    """
    #  void QQuickMaterialStyle::resetContainerStyle()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle19resetContainerStyleEv',
    )

  def themeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::themeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#themeChanged
    """
    #  void QQuickMaterialStyle::themeChanged()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle12themeChangedEv')

  def primaryChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::primaryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#primaryChanged
    """
    #  void QQuickMaterialStyle::primaryChanged()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle14primaryChangedEv')

  def accentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::accentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#accentChanged
    """
    #  void QQuickMaterialStyle::accentChanged()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle13accentChangedEv')

  def foregroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::foregroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#foregroundChanged
    """
    #  void QQuickMaterialStyle::foregroundChanged()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle17foregroundChangedEv')

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::backgroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#backgroundChanged
    """
    #  void QQuickMaterialStyle::backgroundChanged()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle17backgroundChangedEv')

  def elevationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::elevationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#elevationChanged
    """
    #  void QQuickMaterialStyle::elevationChanged()
    self.uglySide.call('ritual_ZN19QQuickMaterialStyle16elevationChangedEv')

  def themeOrAccentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::themeOrAccentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#themeOrAccentChanged
    """
    #  void QQuickMaterialStyle::themeOrAccentChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle20themeOrAccentChangedEv',
    )

  def primaryHighlightedTextColorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialStyle::primaryHighlightedTextColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html
    """
    #  void QQuickMaterialStyle::primaryHighlightedTextColorChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle34primaryHighlightedTextColorChanged'
        'Ev',
    )

  def dialogColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::dialogColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#dialogColorChanged
    """
    #  void QQuickMaterialStyle::dialogColorChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle18dialogColorChangedEv',
    )

  def tooltipColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::tooltipColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#tooltipColorChanged
    """
    #  void QQuickMaterialStyle::tooltipColorChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle19tooltipColorChangedEv',
    )

  def toolBarColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::toolBarColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#toolBarColorChanged
    """
    #  void QQuickMaterialStyle::toolBarColorChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle19toolBarColorChangedEv',
    )

  def toolTextColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::toolTextColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#toolTextColorChanged
    """
    #  void QQuickMaterialStyle::toolTextColorChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle20toolTextColorChangedEv',
    )

  def roundedScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::roundedScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#roundedScaleChanged
    """
    #  void QQuickMaterialStyle::roundedScaleChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle19roundedScaleChangedEv',
    )

  def containerStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::containerStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#containerStyleChanged
    """
    #  void QQuickMaterialStyle::containerStyleChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMaterialStyle21containerStyleChangedEv',
    )

  @overload(
      QQuickAttachedPropertyPropagator, QQuickAttachedPropertyPropagator,
  )
  @overload(QQuickAttachedPropertyPropagator, NoneType)
  @overload(NoneType, QQuickAttachedPropertyPropagator)
  @overload(NoneType, NoneType)
  def attachedParentChange(
      self,
      newParent: Optional[QQuickAttachedPropertyPropagator],
      oldParent: Optional[QQuickAttachedPropertyPropagator],
  ) -> None:
    """
    Calls Qt's 'void QQuickMaterialStyle::attachedParentChange(
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialstyle.html#attachedParentChange

    Parameters
    ----------

    newParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMaterialStyle::attachedParentChange(
    #      QQuickAttachedPropertyPropagator *newParent,
    #      QQuickAttachedPropertyPropagator *oldParent)
    ritual = (
        'ritual_ZN19QQuickMaterialStyle20attachedParentChangeEP32QQuickAtta'
        'chedPropertyPropagatorS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickMaterialStyle20attachedParentChangeEP32QQui'
          'ckAttachedPropertyPropagatorS1_')
    self.uglySide.call(
        ritual, self._addressOf(newParent), self._addressOf(oldParent),
    )

  @staticmethod
  def variantToRgba(*__, **_) -> Never:
    """
    Qt's 'bool QQuickMaterialStyle::variantToRgba(const QVariant &var, const
    char *name, QRgb *rgba, bool *custom) const': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QQuickMaterialStyle.variantToRgba' has no cute function yet. Qt's "
        "'bool QQuickMaterialStyle::variantToRgba(const QVariant &var, "
        "const char *name, QRgb *rgba, bool *custom) const': takes a number "
        "to change where it is.")
