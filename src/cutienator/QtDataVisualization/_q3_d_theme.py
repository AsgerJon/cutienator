"""
Q3DTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/q3dtheme.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QFont, QLinearGradient
  from . import Q3DThemePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DThemePrivate = WAIT['Q3DThemePrivate']
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QLinearGradient = WAIT['QLinearGradient']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DTheme(QObject):
  """
  The cute side of Qt's Q3DTheme: a plain Python object standing in front of
  one C++ Q3DTheme.

  It is built on the cute 'QObject', as Qt's Q3DTheme is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DTheme that has a ritual and that Python can call
  so far, 68 names in all: 'metaObject', 'tr', 'setType', 'type',
  'setBaseColors', 'baseColors', 'setBackgroundColor', 'backgroundColor',
  'setWindowColor', 'windowColor', 'setLabelTextColor', 'labelTextColor',
  'setLabelBackgroundColor', 'labelBackgroundColor', 'setGridLineColor',
  'gridLineColor', 'setSingleHighlightColor', 'singleHighlightColor',
  'setMultiHighlightColor', 'multiHighlightColor', 'setLightColor',
  'lightColor', 'setBaseGradients', 'baseGradients',
  'setSingleHighlightGradient', 'singleHighlightGradient',
  'setMultiHighlightGradient', 'multiHighlightGradient', 'setLightStrength',
  'lightStrength', 'setAmbientLightStrength', 'ambientLightStrength',
  'setHighlightLightStrength', 'highlightLightStrength',
  'setLabelBorderEnabled', 'isLabelBorderEnabled', 'setFont', 'font',
  'setBackgroundEnabled', 'isBackgroundEnabled', 'setGridEnabled',
  'isGridEnabled', 'setLabelBackgroundEnabled', 'isLabelBackgroundEnabled',
  'setColorStyle', 'colorStyle', 'typeChanged', 'baseColorsChanged',
  'backgroundColorChanged', 'windowColorChanged', 'labelTextColorChanged',
  'labelBackgroundColorChanged', 'gridLineColorChanged',
  'singleHighlightColorChanged', 'multiHighlightColorChanged',
  'lightColorChanged', 'baseGradientsChanged',
  'singleHighlightGradientChanged', 'multiHighlightGradientChanged',
  'lightStrengthChanged', 'ambientLightStrengthChanged',
  'highlightLightStrengthChanged', 'labelBorderEnabledChanged',
  'fontChanged', 'backgroundEnabledChanged', 'gridEnabledChanged',
  'labelBackgroundEnabledChanged', 'colorStyleChanged'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DTheme::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int Q3DTheme::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DTheme::~Q3DTheme()': the destructor: Python never removes a C++
    Q3DTheme.

  What has no ritual
  ------------------

  4 of the 78 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DTheme is created at the first use, not by 'Q3DTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DTheme.
  - Qt tells when it has removed the C++ Q3DTheme. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside Q3DTheme, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class ColorStyle(CuteNum):
    """
    The enum 'Q3DTheme::ColorStyle' of Qt, with the 3 names Qt gives in it.
    """

    ColorStyleUniform = Kee[int](0)
    ColorStyleObjectGradient = Kee[int](1)
    ColorStyleRangeGradient = Kee[int](2)

  class Theme(CuteNum):
    """The enum 'Q3DTheme::Theme' of Qt, with the 9 names Qt gives in it."""

    ThemeQt = Kee[int](0)
    ThemePrimaryColors = Kee[int](1)
    ThemeDigia = Kee[int](2)
    ThemeStoneMoss = Kee[int](3)
    ThemeArmyBlue = Kee[int](4)
    ThemeRetro = Kee[int](5)
    ThemeEbony = Kee[int](6)
    ThemeIsabelle = Kee[int](7)
    ThemeUserDefined = Kee[int](8)

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
    Calls Qt's 'QString Q3DTheme::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#tr

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
    #  QString Q3DTheme::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Q3DTheme2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DTheme'

  #  A C++ Q3DTheme Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DTheme'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DTheme::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DTheme::metaObject() const
    address = self.uglySide.call('ritual_ZNK8Q3DTheme10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> Theme:
    """
    Calls Qt's 'Theme Q3DTheme::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#type

    Returns
    -------

    Theme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Theme(number)' gives.
    """
    #  Theme Q3DTheme::type() const
    return Q3DTheme.Theme(self.uglySide.call('ritual_ZNK8Q3DTheme4typeEv'))

  def baseColors(self) -> QList[QColor]:
    """
    Calls Qt's 'QList<QColor> Q3DTheme::baseColors() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#baseColors

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QColor> Q3DTheme::baseColors() const
    address = self.uglySide.call('ritual_ZNK8Q3DTheme10baseColorsEv')
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor Q3DTheme::backgroundColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Q3DTheme::backgroundColor() const
    address = self.uglySide.call('ritual_ZNK8Q3DTheme15backgroundColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def windowColor(self) -> QColor:
    """
    Calls Qt's 'QColor Q3DTheme::windowColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#windowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Q3DTheme::windowColor() const
    address = self.uglySide.call('ritual_ZNK8Q3DTheme11windowColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def labelTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor Q3DTheme::labelTextColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#labelTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Q3DTheme::labelTextColor() const
    address = self.uglySide.call('ritual_ZNK8Q3DTheme14labelTextColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def labelBackgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor Q3DTheme::labelBackgroundColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#labelBackgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Q3DTheme::labelBackgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK8Q3DTheme20labelBackgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def gridLineColor(self) -> QColor:
    """
    Calls Qt's 'QColor Q3DTheme::gridLineColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#gridLineColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Q3DTheme::gridLineColor() const
    address = self.uglySide.call('ritual_ZNK8Q3DTheme13gridLineColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def singleHighlightColor(self) -> QColor:
    """
    Calls Qt's 'QColor Q3DTheme::singleHighlightColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#singleHighlightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Q3DTheme::singleHighlightColor() const
    address = self.uglySide.call(
        'ritual_ZNK8Q3DTheme20singleHighlightColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def multiHighlightColor(self) -> QColor:
    """
    Calls Qt's 'QColor Q3DTheme::multiHighlightColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#multiHighlightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Q3DTheme::multiHighlightColor() const
    address = self.uglySide.call(
        'ritual_ZNK8Q3DTheme19multiHighlightColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def lightColor(self) -> QColor:
    """
    Calls Qt's 'QColor Q3DTheme::lightColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#lightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Q3DTheme::lightColor() const
    address = self.uglySide.call('ritual_ZNK8Q3DTheme10lightColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def baseGradients(self) -> QList[QLinearGradient]:
    """
    Calls Qt's 'QList<QLinearGradient> Q3DTheme::baseGradients() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#baseGradients

    Returns
    -------

    QList[QLinearGradient]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLinearGradient> Q3DTheme::baseGradients() const
    address = self.uglySide.call('ritual_ZNK8Q3DTheme13baseGradientsEv')
    from ..QtGui import QLinearGradient
    return QList[QLinearGradient]._cuteOwning(address)

  def singleHighlightGradient(self) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient Q3DTheme::singleHighlightGradient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#singleHighlightGradient

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient Q3DTheme::singleHighlightGradient() const
    address = self.uglySide.call(
        'ritual_ZNK8Q3DTheme23singleHighlightGradientEv',
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  def multiHighlightGradient(self) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient Q3DTheme::multiHighlightGradient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#multiHighlightGradient

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient Q3DTheme::multiHighlightGradient() const
    address = self.uglySide.call(
        'ritual_ZNK8Q3DTheme22multiHighlightGradientEv',
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  def lightStrength(self) -> float:
    """
    Calls Qt's 'float Q3DTheme::lightStrength() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#lightStrength
    """
    #  float Q3DTheme::lightStrength() const
    return self.uglySide.call('ritual_ZNK8Q3DTheme13lightStrengthEv')

  def ambientLightStrength(self) -> float:
    """
    Calls Qt's 'float Q3DTheme::ambientLightStrength() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#ambientLightStrength
    """
    #  float Q3DTheme::ambientLightStrength() const
    return self.uglySide.call('ritual_ZNK8Q3DTheme20ambientLightStrengthEv')

  def highlightLightStrength(self) -> float:
    """
    Calls Qt's 'float Q3DTheme::highlightLightStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#highlightLightStrength
    """
    #  float Q3DTheme::highlightLightStrength() const
    return self.uglySide.call(
        'ritual_ZNK8Q3DTheme22highlightLightStrengthEv',
    )

  def isLabelBorderEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DTheme::isLabelBorderEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#isLabelBorderEnabled
    """
    #  bool Q3DTheme::isLabelBorderEnabled() const
    return self.uglySide.call('ritual_ZNK8Q3DTheme20isLabelBorderEnabledEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont Q3DTheme::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont Q3DTheme::font() const
    address = self.uglySide.call('ritual_ZNK8Q3DTheme4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def isBackgroundEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DTheme::isBackgroundEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#isBackgroundEnabled
    """
    #  bool Q3DTheme::isBackgroundEnabled() const
    return self.uglySide.call('ritual_ZNK8Q3DTheme19isBackgroundEnabledEv')

  def isGridEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DTheme::isGridEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#isGridEnabled
    """
    #  bool Q3DTheme::isGridEnabled() const
    return self.uglySide.call('ritual_ZNK8Q3DTheme13isGridEnabledEv')

  def isLabelBackgroundEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DTheme::isLabelBackgroundEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#isLabelBackgroundEnabled
    """
    #  bool Q3DTheme::isLabelBackgroundEnabled() const
    return self.uglySide.call(
        'ritual_ZNK8Q3DTheme24isLabelBackgroundEnabledEv',
    )

  def colorStyle(self) -> ColorStyle:
    """
    Calls Qt's 'ColorStyle Q3DTheme::colorStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#colorStyle

    Returns
    -------

    ColorStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorStyle(number)'
      gives.
    """
    #  ColorStyle Q3DTheme::colorStyle() const
    return Q3DTheme.ColorStyle(self.uglySide.call(
        'ritual_ZNK8Q3DTheme10colorStyleEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Theme)
  def setType(self, themeType: Theme) -> None:
    """
    Calls Qt's 'void Q3DTheme::setType(Theme themeType)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setType

    Parameters
    ----------

    themeType : Theme
      Passed on as its number.
    """
    #  void Q3DTheme::setType(Theme themeType)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme7setTypeENS_5ThemeE', themeType.value,
    )

  @overload(QList[QColor])
  def setBaseColors(self, colors: QList[QColor]) -> None:
    """
    Calls Qt's 'void Q3DTheme::setBaseColors(const QList<QColor> &colors)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setBaseColors

    Parameters
    ----------

    colors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Q3DTheme::setBaseColors(const QList<QColor> &colors)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme13setBaseColorsERK5QListI6QColorE',
        self._valueOf(colors),
    )

  @overload(QColor)
  def setBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::setBackgroundColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setBackgroundColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::setBackgroundColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme18setBackgroundColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setWindowColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::setWindowColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setWindowColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::setWindowColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme14setWindowColorERK6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def setLabelTextColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::setLabelTextColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setLabelTextColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::setLabelTextColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme17setLabelTextColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setLabelBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::setLabelBackgroundColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#setLabelBackgroundColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::setLabelBackgroundColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme23setLabelBackgroundColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setGridLineColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::setGridLineColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setGridLineColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::setGridLineColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme16setGridLineColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setSingleHighlightColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::setSingleHighlightColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#setSingleHighlightColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::setSingleHighlightColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme23setSingleHighlightColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setMultiHighlightColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::setMultiHighlightColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#setMultiHighlightColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::setMultiHighlightColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme22setMultiHighlightColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setLightColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::setLightColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setLightColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::setLightColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme13setLightColorERK6QColor', self._valueOf(color),
    )

  @overload(QList[QLinearGradient])
  def setBaseGradients(self, gradients: QList[QLinearGradient]) -> None:
    """
    Calls Qt's 'void Q3DTheme::setBaseGradients(const QList<QLinearGradient>
    &gradients)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setBaseGradients

    Parameters
    ----------

    gradients : QList[QLinearGradient]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Q3DTheme::setBaseGradients(const QList<QLinearGradient>
    #      &gradients)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme16setBaseGradientsERK5QListI15QLinearGradientE',
        self._valueOf(gradients),
    )

  @overload(QLinearGradient)
  def setSingleHighlightGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void Q3DTheme::setSingleHighlightGradient(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#setSingleHighlightGradient

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void Q3DTheme::setSingleHighlightGradient(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme26setSingleHighlightGradientERK15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(QLinearGradient)
  def setMultiHighlightGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void Q3DTheme::setMultiHighlightGradient(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#setMultiHighlightGradient

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void Q3DTheme::setMultiHighlightGradient(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme25setMultiHighlightGradientERK15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(float)
  def setLightStrength(self, strength: float) -> None:
    """
    Calls Qt's 'void Q3DTheme::setLightStrength(float strength)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setLightStrength

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void Q3DTheme::setLightStrength(float strength)
    self.uglySide.call('ritual_ZN8Q3DTheme16setLightStrengthEf', strength)

  @overload(float)
  def setAmbientLightStrength(self, strength: float) -> None:
    """
    Calls Qt's 'void Q3DTheme::setAmbientLightStrength(float strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#setAmbientLightStrength

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void Q3DTheme::setAmbientLightStrength(float strength)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme23setAmbientLightStrengthEf', strength,
    )

  @overload(float)
  def setHighlightLightStrength(self, strength: float) -> None:
    """
    Calls Qt's 'void Q3DTheme::setHighlightLightStrength(float strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#setHighlightLightStrength

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void Q3DTheme::setHighlightLightStrength(float strength)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme25setHighlightLightStrengthEf', strength,
    )

  @overload(bool)
  def setLabelBorderEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DTheme::setLabelBorderEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#setLabelBorderEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DTheme::setLabelBorderEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme21setLabelBorderEnabledEb', enabled,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void Q3DTheme::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void Q3DTheme::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme7setFontERK5QFont', self._valueOf(font),
    )

  @overload(bool)
  def setBackgroundEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DTheme::setBackgroundEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setBackgroundEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DTheme::setBackgroundEnabled(bool enabled)
    self.uglySide.call('ritual_ZN8Q3DTheme20setBackgroundEnabledEb', enabled)

  @overload(bool)
  def setGridEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DTheme::setGridEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setGridEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DTheme::setGridEnabled(bool enabled)
    self.uglySide.call('ritual_ZN8Q3DTheme14setGridEnabledEb', enabled)

  @overload(bool)
  def setLabelBackgroundEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DTheme::setLabelBackgroundEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#setLabelBackgroundEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DTheme::setLabelBackgroundEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme25setLabelBackgroundEnabledEb', enabled,
    )

  @overload(ColorStyle)
  def setColorStyle(self, style: ColorStyle) -> None:
    """
    Calls Qt's 'void Q3DTheme::setColorStyle(ColorStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#setColorStyle

    Parameters
    ----------

    style : ColorStyle
      Passed on as its number.
    """
    #  void Q3DTheme::setColorStyle(ColorStyle style)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme13setColorStyleENS_10ColorStyleE', style.value,
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
    Notes what was given, for Qt's 'Q3DTheme::Q3DTheme(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#Q3DTheme

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DTheme::Q3DTheme(QObject *parent)
    self._noteCreation(Q3DTheme, lambda: Rituals.call(
        'ritual_ZN8Q3DThemeC1EP7QObject', self._addressOf(parent, 'QObject'),
    ))

  @overload(Theme)
  @overload(Theme, QObject)
  @overload(Theme, NoneType)
  def __init__(
      self,
      themeType: Theme,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'Q3DTheme::Q3DTheme(Theme themeType,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#Q3DTheme

    Parameters
    ----------

    themeType : Theme
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DTheme::Q3DTheme(Theme themeType, QObject *parent)
    self._noteCreation(Q3DTheme, lambda: Rituals.call(
        'ritual_ZN8Q3DThemeC1ENS_5ThemeEP7QObject',
        themeType.value, self._addressOf(parent, 'QObject'),
    ))

  @overload(Q3DThemePrivate, Theme)
  @overload(NoneType, Theme)
  @overload(Q3DThemePrivate, Theme, QObject)
  @overload(Q3DThemePrivate, Theme, NoneType)
  @overload(NoneType, Theme, QObject)
  @overload(NoneType, Theme, NoneType)
  def __init__(
      self,
      d: Optional[Q3DThemePrivate],
      themeType: Theme,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'Q3DTheme::Q3DTheme(Q3DThemePrivate *d,
    Theme themeType, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#Q3DTheme

    Parameters
    ----------

    d : Optional[Q3DThemePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    themeType : Theme
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DTheme::Q3DTheme(Q3DThemePrivate *d, Theme themeType, QObject
    #      *parent)
    self._noteCreation(Q3DTheme, lambda: Rituals.call(
        'ritual_ZN8Q3DThemeC1EP15Q3DThemePrivateNS_5ThemeEP7QObject',
        self._addressOf(d), themeType.value, self._addressOf(parent,
        'QObject'),
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
  def typeChanged(self, themeType: Theme) -> None:
    """
    Calls Qt's 'void Q3DTheme::typeChanged(Q3DTheme::Theme themeType)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#typeChanged

    Parameters
    ----------

    themeType : Theme
      Passed on as its number.
    """
    #  void Q3DTheme::typeChanged(Q3DTheme::Theme themeType)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme11typeChangedENS_5ThemeE', themeType.value,
    )

  @overload(QList[QColor])
  def baseColorsChanged(self, colors: QList[QColor]) -> None:
    """
    Calls Qt's 'void Q3DTheme::baseColorsChanged(const QList<QColor>
    &colors)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#baseColorsChanged

    Parameters
    ----------

    colors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Q3DTheme::baseColorsChanged(const QList<QColor> &colors)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme17baseColorsChangedERK5QListI6QColorE',
        self._valueOf(colors),
    )

  @overload(QColor)
  def backgroundColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::backgroundColorChanged(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#backgroundColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::backgroundColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme22backgroundColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def windowColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::windowColorChanged(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#windowColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::windowColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme18windowColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def labelTextColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::labelTextColorChanged(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#labelTextColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::labelTextColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme21labelTextColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def labelBackgroundColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::labelBackgroundColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#labelBackgroundColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::labelBackgroundColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme27labelBackgroundColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def gridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::gridLineColorChanged(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#gridLineColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::gridLineColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme20gridLineColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def singleHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::singleHighlightColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#singleHighlightColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::singleHighlightColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme27singleHighlightColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def multiHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::multiHighlightColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#multiHighlightColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::multiHighlightColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme26multiHighlightColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def lightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Q3DTheme::lightColorChanged(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#lightColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DTheme::lightColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme17lightColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QList[QLinearGradient])
  def baseGradientsChanged(self, gradients: QList[QLinearGradient]) -> None:
    """
    Calls Qt's 'void Q3DTheme::baseGradientsChanged(const
    QList<QLinearGradient> &gradients)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#baseGradientsChanged

    Parameters
    ----------

    gradients : QList[QLinearGradient]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Q3DTheme::baseGradientsChanged(const QList<QLinearGradient>
    #      &gradients)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme20baseGradientsChangedERK5QListI15QLinearGradien'
        'tE',
        self._valueOf(gradients),
    )

  @overload(QLinearGradient)
  def singleHighlightGradientChanged(
      self,
      gradient: QLinearGradient,
  ) -> None:
    """
    Calls Qt's 'void Q3DTheme::singleHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#singleHighlightGradientChanged

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void Q3DTheme::singleHighlightGradientChanged(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme30singleHighlightGradientChangedERK15QLinearGrad'
        'ient',
        self._valueOf(gradient),
    )

  @overload(QLinearGradient)
  def multiHighlightGradientChanged(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void Q3DTheme::multiHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#multiHighlightGradientChanged

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void Q3DTheme::multiHighlightGradientChanged(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme29multiHighlightGradientChangedERK15QLinearGradi'
        'ent',
        self._valueOf(gradient),
    )

  @overload(float)
  def lightStrengthChanged(self, strength: float) -> None:
    """
    Calls Qt's 'void Q3DTheme::lightStrengthChanged(float strength)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#lightStrengthChanged

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void Q3DTheme::lightStrengthChanged(float strength)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme20lightStrengthChangedEf', strength,
    )

  @overload(float)
  def ambientLightStrengthChanged(self, strength: float) -> None:
    """
    Calls Qt's 'void Q3DTheme::ambientLightStrengthChanged(float strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#ambientLightStrengthChanged

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void Q3DTheme::ambientLightStrengthChanged(float strength)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme27ambientLightStrengthChangedEf', strength,
    )

  @overload(float)
  def highlightLightStrengthChanged(self, strength: float) -> None:
    """
    Calls Qt's 'void Q3DTheme::highlightLightStrengthChanged(float
    strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#highlightLightStrengthChanged

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void Q3DTheme::highlightLightStrengthChanged(float strength)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme29highlightLightStrengthChangedEf', strength,
    )

  @overload(bool)
  def labelBorderEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DTheme::labelBorderEnabledChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#labelBorderEnabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DTheme::labelBorderEnabledChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme25labelBorderEnabledChangedEb', enabled,
    )

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void Q3DTheme::fontChanged(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void Q3DTheme::fontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme11fontChangedERK5QFont', self._valueOf(font),
    )

  @overload(bool)
  def backgroundEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DTheme::backgroundEnabledChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#backgroundEnabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DTheme::backgroundEnabledChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme24backgroundEnabledChangedEb', enabled,
    )

  @overload(bool)
  def gridEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DTheme::gridEnabledChanged(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#gridEnabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DTheme::gridEnabledChanged(bool enabled)
    self.uglySide.call('ritual_ZN8Q3DTheme18gridEnabledChangedEb', enabled)

  @overload(bool)
  def labelBackgroundEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DTheme::labelBackgroundEnabledChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dtheme.html#labelBackgroundEnabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DTheme::labelBackgroundEnabledChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme29labelBackgroundEnabledChangedEb', enabled,
    )

  @overload(ColorStyle)
  def colorStyleChanged(self, style: ColorStyle) -> None:
    """
    Calls Qt's 'void Q3DTheme::colorStyleChanged(Q3DTheme::ColorStyle
    style)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dtheme.html#colorStyleChanged

    Parameters
    ----------

    style : ColorStyle
      Passed on as its number.
    """
    #  void Q3DTheme::colorStyleChanged(Q3DTheme::ColorStyle style)
    self.uglySide.call(
        'ritual_ZN8Q3DTheme17colorStyleChangedENS_10ColorStyleE',
        style.value,
    )


#  Qt's 'QList<Q3DTheme *>': the list of Q3DTheme, which 'QList[Q3DTheme]'
#  gives. It is made here, so that there is one as soon as there can be a
#  Q3DTheme.
QList.createKind(
    Q3DTheme, 'address',
    make='ritual_list_make_Q3DTheme_ptr',
    add='ritual_list_add_Q3DTheme_ptr',
    size='ritual_list_size_Q3DTheme_ptr',
    at='ritual_list_at_Q3DTheme_ptr',
    drop='ritual_list_drop_Q3DTheme_ptr',
)
