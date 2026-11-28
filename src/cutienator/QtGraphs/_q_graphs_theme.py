"""
QGraphsTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qgraphstheme.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QFont, QLinearGradient
  from ..QtQuick import QQuickGradient
  from . import QGraphsLine, QGraphsThemeDirtyBitField, QGraphsThemePrivate
  from . import QQuickGraphsColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QGraphsLine = WAIT['QGraphsLine']
  QLinearGradient = WAIT['QLinearGradient']
  QQuickGradient = WAIT['QQuickGradient']
  QQuickGraphsColor = WAIT['QQuickGraphsColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphsTheme(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QGraphsTheme: a plain Python object standing in front
  of one C++ QGraphsTheme.

  It is built on the cute 'QObject', as Qt's QGraphsTheme is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QGraphsTheme is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphsTheme that has a ritual and that Python can
  call so far, 118 names in all: 'metaObject', 'tr', 'themeDirty',
  'resetThemeDirty', 'resetColorTheme', 'dirtyBits', 'resetDirtyBits',
  'colorScheme', 'setColorScheme', 'theme', 'setTheme', 'colorStyle',
  'setColorStyle', 'backgroundColor', 'setBackgroundColor',
  'isBackgroundVisible', 'setBackgroundVisible', 'plotAreaBackgroundColor',
  'setPlotAreaBackgroundColor', 'isPlotAreaBackgroundVisible',
  'setPlotAreaBackgroundVisible', 'isGridVisible', 'setGridVisible',
  'labelsVisible', 'setLabelsVisible', 'labelBackgroundColor',
  'setLabelBackgroundColor', 'labelTextColor', 'setLabelTextColor',
  'singleHighlightColor', 'setSingleHighlightColor', 'multiHighlightColor',
  'setMultiHighlightColor', 'setSingleHighlightGradient',
  'singleHighlightGradient', 'setMultiHighlightGradient',
  'multiHighlightGradient', 'labelFont', 'setLabelFont', 'seriesColors',
  'setSeriesColors', 'borderColors', 'setBorderColors', 'seriesGradients',
  'setSeriesGradients', 'isLabelBackgroundVisible',
  'setLabelBackgroundVisible', 'isLabelBorderVisible',
  'setLabelBorderVisible', 'borderWidth', 'setBorderWidth', 'axisXLabelFont',
  'setAxisXLabelFont', 'axisYLabelFont', 'setAxisYLabelFont',
  'axisZLabelFont', 'setAxisZLabelFont', 'grid', 'setGrid', 'axisX',
  'setAxisX', 'axisY', 'setAxisY', 'axisZ', 'setAxisZ', 'update',
  'colorSchemeChanged', 'themeChanged', 'colorStyleChanged',
  'backgroundColorChanged', 'backgroundVisibleChanged',
  'plotAreaBackgroundColorChanged', 'plotAreaBackgroundVisibleChanged',
  'gridVisibleChanged', 'labelsVisibleChanged',
  'labelBackgroundColorChanged', 'labelTextColorChanged',
  'singleHighlightColorChanged', 'multiHighlightColorChanged',
  'singleHighlightGradientChanged', 'multiHighlightGradientChanged',
  'labelFontChanged', 'labelBackgroundVisibleChanged',
  'labelBorderVisibleChanged', 'seriesColorsChanged',
  'seriesGradientsChanged', 'borderColorsChanged', 'borderWidthChanged',
  'singleHighlightGradientQMLChanged', 'multiHighlightGradientQMLChanged',
  'axisXLabelFontChanged', 'axisYLabelFontChanged', 'axisZLabelFontChanged',
  'gridChanged', 'axisXChanged', 'axisYChanged', 'axisZChanged',
  'handleBaseColorUpdate', 'handleBaseGradientUpdate', 'classBegin',
  'componentComplete', 'updateAutomaticColorScheme', 'setColorSchemePalette',
  'setThemePalette', 'createGradient', 'convertGradient', 'addColor',
  'colorList', 'clearColors', 'clearDummyColors', 'clearGradients',
  'gradientList', 'addGradient', 'setSingleHighlightGradientQML',
  'singleHighlightGradientQML', 'setMultiHighlightGradientQML',
  'multiHighlightGradientQML', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphsTheme::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QGraphsTheme::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphsTheme::~QGraphsTheme()': the destructor: Python never
    removes a C++ QGraphsTheme.
  - Qt's 'QGraphsTheme::QGraphsTheme(QGraphsThemePrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'void QGraphsTheme::setThemeGradient(QQuickGradient *gradient,
    GradientQMLStyle type)': names the enum 'QGraphsTheme::GradientQMLStyle',
    whose class cannot be named here.
  - Qt's 'QQmlListProperty<QQuickGraphsColor> QGraphsTheme::baseColorsQML()':
    gives a type Python has no way to take yet.
  - Qt's 'void
    QGraphsTheme::appendBaseColorsFunc(QQmlListProperty<QQuickGraphsColor>
    *list, QQuickGraphsColor *color)': names
    'QQmlListProperty<QQuickGraphsColor>', which has no cute class yet.
  - Qt's 'qsizetype
    QGraphsTheme::countBaseColorsFunc(QQmlListProperty<QQuickGraphsColor>
    *list)': names 'QQmlListProperty<QQuickGraphsColor>', which has no cute
    class yet.
  - Qt's 'QQuickGraphsColor
    *QGraphsTheme::atBaseColorsFunc(QQmlListProperty<QQuickGraphsColor>
    *list, qsizetype index)': names 'QQmlListProperty<QQuickGraphsColor>',
    which has no cute class yet.
  - Qt's 'void
    QGraphsTheme::clearBaseColorsFunc(QQmlListProperty<QQuickGraphsColor>
    *list)': names 'QQmlListProperty<QQuickGraphsColor>', which has no cute
    class yet.
  - Qt's 'QQmlListProperty<QQuickGradient> QGraphsTheme::baseGradientsQML()':
    gives a type Python has no way to take yet.
  - Qt's 'void
    QGraphsTheme::appendBaseGradientsFunc(QQmlListProperty<QQuickGradient>
    *list, QQuickGradient *gradient)': names
    'QQmlListProperty<QQuickGradient>', which has no cute class yet.
  - Qt's 'qsizetype
    QGraphsTheme::countBaseGradientsFunc(QQmlListProperty<QQuickGradient>
    *list)': names 'QQmlListProperty<QQuickGradient>', which has no cute
    class yet.
  - Qt's 'QQuickGradient
    *QGraphsTheme::atBaseGradientsFunc(QQmlListProperty<QQuickGradient>
    *list, qsizetype index)': names 'QQmlListProperty<QQuickGradient>', which
    has no cute class yet.
  - Qt's 'void
    QGraphsTheme::clearBaseGradientsFunc(QQmlListProperty<QQuickGradient>
    *list)': names 'QQmlListProperty<QQuickGradient>', which has no cute
    class yet.
  - Qt's 'QQmlListProperty<QObject> QGraphsTheme::themeChildren()': gives a
    type Python has no way to take yet.
  - Qt's 'void QGraphsTheme::appendThemeChildren(QQmlListProperty<QObject>
    *list, QObject *element)': names 'QQmlListProperty<QObject>', which has
    no cute class yet.
  - Qt's 'const QGraphsThemePrivate *QGraphsTheme::d_func() const': takes in
    Python what 'QGraphsThemePrivate *QGraphsTheme::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 143 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QGraphsTheme is created at the first use, not by
    'QGraphsTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphsTheme.
  - Qt tells when it has removed the C++ QGraphsTheme. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QGraphsTheme that has no cute function yet,
    'appendBaseColorsFunc', 'appendBaseGradientsFunc', 'appendThemeChildren',
    'atBaseColorsFunc', 'atBaseGradientsFunc', 'baseColorsQML',
    'baseGradientsQML', 'clearBaseColorsFunc', 'clearBaseGradientsFunc',
    'countBaseColorsFunc', 'countBaseGradientsFunc', 'setThemeGradient',
    'themeChildren', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QGraphsTheme, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ColorScheme(CuteNum, scoped=True):
    """
    The enum 'QGraphsTheme::ColorScheme' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Automatic = Kee[int](0)
    Light = Kee[int](1)
    Dark = Kee[int](2)

  class ColorStyle(CuteNum, scoped=True):
    """
    The enum 'QGraphsTheme::ColorStyle' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Uniform = Kee[int](0)
    ObjectGradient = Kee[int](1)
    RangeGradient = Kee[int](2)

  class ForceTheme(CuteNum, scoped=True):
    """
    The enum 'QGraphsTheme::ForceTheme' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  class Theme(CuteNum, scoped=True):
    """
    The enum 'QGraphsTheme::Theme' of Qt, with the 9 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    QtGreen = Kee[int](0)
    QtGreenNeon = Kee[int](1)
    MixSeries = Kee[int](2)
    OrangeSeries = Kee[int](3)
    YellowSeries = Kee[int](4)
    BlueSeries = Kee[int](5)
    PurpleSeries = Kee[int](6)
    GreySeries = Kee[int](7)
    UserDefined = Kee[int](8)

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
    Calls Qt's 'QString QGraphsTheme::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#tr

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
    #  QString QGraphsTheme::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QGraphsTheme2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphsTheme'

  #  Qt's QGraphsTheme is built on more than one class. The part of a C++
  #  QGraphsTheme that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QGraphsTheme_QQmlParserStatus',
  }

  #  A C++ QGraphsTheme Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphsTheme'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphsTheme::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphsTheme::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QGraphsTheme10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def themeDirty(self) -> bool:
    """
    Calls Qt's 'bool QGraphsTheme::themeDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#themeDirty
    """
    #  bool QGraphsTheme::themeDirty() const
    return self.uglySide.call('ritual_ZNK12QGraphsTheme10themeDirtyEv')

  def colorScheme(self) -> ColorScheme:
    """
    Calls Qt's 'ColorScheme QGraphsTheme::colorScheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#colorScheme

    Returns
    -------

    ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorScheme(number)'
      gives.
    """
    #  ColorScheme QGraphsTheme::colorScheme() const
    return QGraphsTheme.ColorScheme(self.uglySide.call(
        'ritual_ZNK12QGraphsTheme11colorSchemeEv',
    ))

  def theme(self) -> Theme:
    """
    Calls Qt's 'Theme QGraphsTheme::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#theme

    Returns
    -------

    Theme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Theme(number)' gives.
    """
    #  Theme QGraphsTheme::theme() const
    return QGraphsTheme.Theme(self.uglySide.call(
        'ritual_ZNK12QGraphsTheme5themeEv',
    ))

  def colorStyle(self) -> ColorStyle:
    """
    Calls Qt's 'ColorStyle QGraphsTheme::colorStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#colorStyle

    Returns
    -------

    ColorStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorStyle(number)'
      gives.
    """
    #  ColorStyle QGraphsTheme::colorStyle() const
    return QGraphsTheme.ColorStyle(self.uglySide.call(
        'ritual_ZNK12QGraphsTheme10colorStyleEv',
    ))

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsTheme::backgroundColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsTheme::backgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme15backgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def isBackgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool QGraphsTheme::isBackgroundVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#isBackgroundVisible
    """
    #  bool QGraphsTheme::isBackgroundVisible() const
    return self.uglySide.call(
        'ritual_ZNK12QGraphsTheme19isBackgroundVisibleEv',
    )

  def plotAreaBackgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsTheme::plotAreaBackgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#plotAreaBackgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsTheme::plotAreaBackgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme23plotAreaBackgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def isPlotAreaBackgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool QGraphsTheme::isPlotAreaBackgroundVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#isPlotAreaBackgroundVisible
    """
    #  bool QGraphsTheme::isPlotAreaBackgroundVisible() const
    return self.uglySide.call(
        'ritual_ZNK12QGraphsTheme27isPlotAreaBackgroundVisibleEv',
    )

  def isGridVisible(self) -> bool:
    """
    Calls Qt's 'bool QGraphsTheme::isGridVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#isGridVisible
    """
    #  bool QGraphsTheme::isGridVisible() const
    return self.uglySide.call('ritual_ZNK12QGraphsTheme13isGridVisibleEv')

  def labelsVisible(self) -> bool:
    """
    Calls Qt's 'bool QGraphsTheme::labelsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#labelsVisible
    """
    #  bool QGraphsTheme::labelsVisible() const
    return self.uglySide.call('ritual_ZNK12QGraphsTheme13labelsVisibleEv')

  def labelBackgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsTheme::labelBackgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#labelBackgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsTheme::labelBackgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme20labelBackgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def labelTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsTheme::labelTextColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#labelTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsTheme::labelTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme14labelTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def singleHighlightColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsTheme::singleHighlightColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#singleHighlightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsTheme::singleHighlightColor() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme20singleHighlightColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def multiHighlightColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsTheme::multiHighlightColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#multiHighlightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsTheme::multiHighlightColor() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme19multiHighlightColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def singleHighlightGradient(self) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient QGraphsTheme::singleHighlightGradient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#singleHighlightGradient

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient QGraphsTheme::singleHighlightGradient() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme23singleHighlightGradientEv',
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  def multiHighlightGradient(self) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient QGraphsTheme::multiHighlightGradient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#multiHighlightGradient

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient QGraphsTheme::multiHighlightGradient() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme22multiHighlightGradientEv',
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  def labelFont(self) -> QFont:
    """
    Calls Qt's 'QFont QGraphsTheme::labelFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#labelFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGraphsTheme::labelFont() const
    address = self.uglySide.call('ritual_ZNK12QGraphsTheme9labelFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def seriesColors(self) -> QList[QColor]:
    """
    Calls Qt's 'QList<QColor> QGraphsTheme::seriesColors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#seriesColors

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QColor> QGraphsTheme::seriesColors() const
    address = self.uglySide.call('ritual_ZNK12QGraphsTheme12seriesColorsEv')
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

  def borderColors(self) -> QList[QColor]:
    """
    Calls Qt's 'QList<QColor> QGraphsTheme::borderColors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#borderColors

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QColor> QGraphsTheme::borderColors() const
    address = self.uglySide.call('ritual_ZNK12QGraphsTheme12borderColorsEv')
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

  def seriesGradients(self) -> QList[QLinearGradient]:
    """
    Calls Qt's 'QList<QLinearGradient> QGraphsTheme::seriesGradients()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#seriesGradients

    Returns
    -------

    QList[QLinearGradient]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLinearGradient> QGraphsTheme::seriesGradients() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme15seriesGradientsEv',
    )
    from ..QtGui import QLinearGradient
    return QList[QLinearGradient]._cuteOwning(address)

  def isLabelBackgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool QGraphsTheme::isLabelBackgroundVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#isLabelBackgroundVisible
    """
    #  bool QGraphsTheme::isLabelBackgroundVisible() const
    return self.uglySide.call(
        'ritual_ZNK12QGraphsTheme24isLabelBackgroundVisibleEv',
    )

  def isLabelBorderVisible(self) -> bool:
    """
    Calls Qt's 'bool QGraphsTheme::isLabelBorderVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#isLabelBorderVisible
    """
    #  bool QGraphsTheme::isLabelBorderVisible() const
    return self.uglySide.call(
        'ritual_ZNK12QGraphsTheme20isLabelBorderVisibleEv',
    )

  def borderWidth(self) -> float:
    """
    Calls Qt's 'qreal QGraphsTheme::borderWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#borderWidth
    """
    #  qreal QGraphsTheme::borderWidth() const
    return self.uglySide.call('ritual_ZNK12QGraphsTheme11borderWidthEv')

  def axisXLabelFont(self) -> QFont:
    """
    Calls Qt's 'QFont QGraphsTheme::axisXLabelFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#axisXLabelFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGraphsTheme::axisXLabelFont() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme14axisXLabelFontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def axisYLabelFont(self) -> QFont:
    """
    Calls Qt's 'QFont QGraphsTheme::axisYLabelFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#axisYLabelFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGraphsTheme::axisYLabelFont() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme14axisYLabelFontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def axisZLabelFont(self) -> QFont:
    """
    Calls Qt's 'QFont QGraphsTheme::axisZLabelFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#axisZLabelFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGraphsTheme::axisZLabelFont() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme14axisZLabelFontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def grid(self) -> QGraphsLine:
    """
    Calls Qt's 'QGraphsLine QGraphsTheme::grid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#grid

    Returns
    -------

    QGraphsLine
      A new cute QGraphsLine around the copy Qt gave back. Python owns it.
    """
    #  QGraphsLine QGraphsTheme::grid() const
    address = self.uglySide.call('ritual_ZNK12QGraphsTheme4gridEv')
    from . import QGraphsLine
    return QGraphsLine._cuteOwning(address)

  def axisX(self) -> QGraphsLine:
    """
    Calls Qt's 'QGraphsLine QGraphsTheme::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#axisX

    Returns
    -------

    QGraphsLine
      A new cute QGraphsLine around the copy Qt gave back. Python owns it.
    """
    #  QGraphsLine QGraphsTheme::axisX() const
    address = self.uglySide.call('ritual_ZNK12QGraphsTheme5axisXEv')
    from . import QGraphsLine
    return QGraphsLine._cuteOwning(address)

  def axisY(self) -> QGraphsLine:
    """
    Calls Qt's 'QGraphsLine QGraphsTheme::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#axisY

    Returns
    -------

    QGraphsLine
      A new cute QGraphsLine around the copy Qt gave back. Python owns it.
    """
    #  QGraphsLine QGraphsTheme::axisY() const
    address = self.uglySide.call('ritual_ZNK12QGraphsTheme5axisYEv')
    from . import QGraphsLine
    return QGraphsLine._cuteOwning(address)

  def axisZ(self) -> QGraphsLine:
    """
    Calls Qt's 'QGraphsLine QGraphsTheme::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#axisZ

    Returns
    -------

    QGraphsLine
      A new cute QGraphsLine around the copy Qt gave back. Python owns it.
    """
    #  QGraphsLine QGraphsTheme::axisZ() const
    address = self.uglySide.call('ritual_ZNK12QGraphsTheme5axisZEv')
    from . import QGraphsLine
    return QGraphsLine._cuteOwning(address)

  def singleHighlightGradientQML(self) -> Optional[QQuickGradient]:
    """
    Calls Qt's 'QQuickGradient *QGraphsTheme::singleHighlightGradientQML()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#singleHighlightGradientQML

    Returns
    -------

    Optional[QQuickGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGradient *QGraphsTheme::singleHighlightGradientQML() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme26singleHighlightGradientQMLEv',
    )
    from ..QtQuick import QQuickGradient
    return QQuickGradient._cuteAt(address)

  def multiHighlightGradientQML(self) -> Optional[QQuickGradient]:
    """
    Calls Qt's 'QQuickGradient *QGraphsTheme::multiHighlightGradientQML()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#multiHighlightGradientQML

    Returns
    -------

    Optional[QQuickGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGradient *QGraphsTheme::multiHighlightGradientQML() const
    address = self.uglySide.call(
        'ritual_ZNK12QGraphsTheme25multiHighlightGradientQMLEv',
    )
    from ..QtQuick import QQuickGradient
    return QQuickGradient._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ColorScheme)
  def setColorScheme(self, newColorScheme: ColorScheme) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setColorScheme(ColorScheme
    newColorScheme)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setColorScheme

    Parameters
    ----------

    newColorScheme : ColorScheme
      Passed on as its number.
    """
    #  void QGraphsTheme::setColorScheme(ColorScheme newColorScheme)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme14setColorSchemeENS_11ColorSchemeE',
        newColorScheme.value,
    )

  @overload(Theme)
  @overload(Theme, ForceTheme)
  def setTheme(
      self,
      newTheme: Theme,
      force: ForceTheme = ForceTheme.No,
  ) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setTheme(Theme newTheme, ForceTheme
    force)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setTheme

    Parameters
    ----------

    newTheme : Theme
      Passed on as its number.

    force : ForceTheme
      Passed on as its number. May be left out, as in Qt: it is then
      ForceTheme.No.
    """
    #  void QGraphsTheme::setTheme(Theme newTheme, ForceTheme force)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme8setThemeENS_5ThemeENS_10ForceThemeE',
        newTheme.value, force.value,
    )

  @overload(ColorStyle)
  def setColorStyle(self, newColorStyle: ColorStyle) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setColorStyle(ColorStyle newColorStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setColorStyle

    Parameters
    ----------

    newColorStyle : ColorStyle
      Passed on as its number.
    """
    #  void QGraphsTheme::setColorStyle(ColorStyle newColorStyle)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme13setColorStyleENS_10ColorStyleE',
        newColorStyle.value,
    )

  @overload(QColor)
  def setBackgroundColor(self, newBackgroundColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setBackgroundColor(QColor
    newBackgroundColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setBackgroundColor

    Parameters
    ----------

    newBackgroundColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsTheme::setBackgroundColor(QColor newBackgroundColor)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme18setBackgroundColorE6QColor',
        self._valueOf(newBackgroundColor),
    )

  @overload(bool)
  def setBackgroundVisible(self, newBackgroundVisible: bool) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setBackgroundVisible(bool
    newBackgroundVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setBackgroundVisible

    Parameters
    ----------

    newBackgroundVisible : bool
      Passed on as it is.
    """
    #  void QGraphsTheme::setBackgroundVisible(bool newBackgroundVisible)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme20setBackgroundVisibleEb',
        newBackgroundVisible,
    )

  @overload(QColor)
  def setPlotAreaBackgroundColor(self, newBackgroundColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setPlotAreaBackgroundColor(QColor
    newBackgroundColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setPlotAreaBackgroundColor

    Parameters
    ----------

    newBackgroundColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsTheme::setPlotAreaBackgroundColor(QColor
    #      newBackgroundColor)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme26setPlotAreaBackgroundColorE6QColor',
        self._valueOf(newBackgroundColor),
    )

  @overload(bool)
  def setPlotAreaBackgroundVisible(
      self,
      newBackgroundVisibility: bool,
  ) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setPlotAreaBackgroundVisible(bool
    newBackgroundVisibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setPlotAreaBackgroundVisible

    Parameters
    ----------

    newBackgroundVisibility : bool
      Passed on as it is.
    """
    #  void QGraphsTheme::setPlotAreaBackgroundVisible(bool
    #      newBackgroundVisibility)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme28setPlotAreaBackgroundVisibleEb',
        newBackgroundVisibility,
    )

  @overload(bool)
  def setGridVisible(self, newGridVisibility: bool) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setGridVisible(bool newGridVisibility)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setGridVisible

    Parameters
    ----------

    newGridVisibility : bool
      Passed on as it is.
    """
    #  void QGraphsTheme::setGridVisible(bool newGridVisibility)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme14setGridVisibleEb', newGridVisibility,
    )

  @overload(bool)
  def setLabelsVisible(self, newLabelsVisibility: bool) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setLabelsVisible(bool
    newLabelsVisibility)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setLabelsVisible

    Parameters
    ----------

    newLabelsVisibility : bool
      Passed on as it is.
    """
    #  void QGraphsTheme::setLabelsVisible(bool newLabelsVisibility)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme16setLabelsVisibleEb', newLabelsVisibility,
    )

  @overload(QColor)
  def setLabelBackgroundColor(self, newLabelBackgroundColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setLabelBackgroundColor(QColor
    newLabelBackgroundColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setLabelBackgroundColor

    Parameters
    ----------

    newLabelBackgroundColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsTheme::setLabelBackgroundColor(QColor
    #      newLabelBackgroundColor)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme23setLabelBackgroundColorE6QColor',
        self._valueOf(newLabelBackgroundColor),
    )

  @overload(QColor)
  def setLabelTextColor(self, newLabelTextColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setLabelTextColor(QColor
    newLabelTextColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setLabelTextColor

    Parameters
    ----------

    newLabelTextColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsTheme::setLabelTextColor(QColor newLabelTextColor)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme17setLabelTextColorE6QColor',
        self._valueOf(newLabelTextColor),
    )

  @overload(QColor)
  def setSingleHighlightColor(self, newSingleHighlightColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setSingleHighlightColor(QColor
    newSingleHighlightColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setSingleHighlightColor

    Parameters
    ----------

    newSingleHighlightColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsTheme::setSingleHighlightColor(QColor
    #      newSingleHighlightColor)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme23setSingleHighlightColorE6QColor',
        self._valueOf(newSingleHighlightColor),
    )

  @overload(QColor)
  def setMultiHighlightColor(self, newMultiHighlightColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setMultiHighlightColor(QColor
    newMultiHighlightColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setMultiHighlightColor

    Parameters
    ----------

    newMultiHighlightColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsTheme::setMultiHighlightColor(QColor
    #      newMultiHighlightColor)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme22setMultiHighlightColorE6QColor',
        self._valueOf(newMultiHighlightColor),
    )

  @overload(QLinearGradient)
  def setSingleHighlightGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setSingleHighlightGradient(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setSingleHighlightGradient

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QGraphsTheme::setSingleHighlightGradient(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme26setSingleHighlightGradientERK15QLinearGra'
        'dient',
        self._valueOf(gradient),
    )

  @overload(QLinearGradient)
  def setMultiHighlightGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setMultiHighlightGradient(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setMultiHighlightGradient

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QGraphsTheme::setMultiHighlightGradient(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme25setMultiHighlightGradientERK15QLinearGrad'
        'ient',
        self._valueOf(gradient),
    )

  @overload(QFont)
  def setLabelFont(self, newFont: QFont) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setLabelFont(const QFont &newFont)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setLabelFont

    Parameters
    ----------

    newFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphsTheme::setLabelFont(const QFont &newFont)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme12setLabelFontERK5QFont',
        self._valueOf(newFont),
    )

  @overload(QList[QColor])
  def setSeriesColors(self, newSeriesColors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setSeriesColors(const QList<QColor>
    &newSeriesColors)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setSeriesColors

    Parameters
    ----------

    newSeriesColors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGraphsTheme::setSeriesColors(const QList<QColor>
    #      &newSeriesColors)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme15setSeriesColorsERK5QListI6QColorE',
        self._valueOf(newSeriesColors),
    )

  @overload(QList[QColor])
  def setBorderColors(self, newBorderColors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setBorderColors(const QList<QColor>
    &newBorderColors)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setBorderColors

    Parameters
    ----------

    newBorderColors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGraphsTheme::setBorderColors(const QList<QColor>
    #      &newBorderColors)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme15setBorderColorsERK5QListI6QColorE',
        self._valueOf(newBorderColors),
    )

  @overload(QList[QLinearGradient])
  def setSeriesGradients(
      self,
      newSeriesGradients: QList[QLinearGradient],
  ) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setSeriesGradients(const
    QList<QLinearGradient> &newSeriesGradients)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setSeriesGradients

    Parameters
    ----------

    newSeriesGradients : QList[QLinearGradient]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGraphsTheme::setSeriesGradients(const QList<QLinearGradient>
    #      &newSeriesGradients)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme18setSeriesGradientsERK5QListI15QLinearGrad'
        'ientE',
        self._valueOf(newSeriesGradients),
    )

  @overload(bool)
  def setLabelBackgroundVisible(
      self,
      newLabelBackgroundVisibility: bool,
  ) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setLabelBackgroundVisible(bool
    newLabelBackgroundVisibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setLabelBackgroundVisible

    Parameters
    ----------

    newLabelBackgroundVisibility : bool
      Passed on as it is.
    """
    #  void QGraphsTheme::setLabelBackgroundVisible(bool
    #      newLabelBackgroundVisibility)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme25setLabelBackgroundVisibleEb',
        newLabelBackgroundVisibility,
    )

  @overload(bool)
  def setLabelBorderVisible(self, newLabelBorderVisibility: bool) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setLabelBorderVisible(bool
    newLabelBorderVisibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setLabelBorderVisible

    Parameters
    ----------

    newLabelBorderVisibility : bool
      Passed on as it is.
    """
    #  void QGraphsTheme::setLabelBorderVisible(bool
    #      newLabelBorderVisibility)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme21setLabelBorderVisibleEb',
        newLabelBorderVisibility,
    )

  @overload(float)
  def setBorderWidth(self, newBorderWidth: float) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setBorderWidth(qreal newBorderWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setBorderWidth

    Parameters
    ----------

    newBorderWidth : float
      Passed on as it is.
    """
    #  void QGraphsTheme::setBorderWidth(qreal newBorderWidth)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme14setBorderWidthEd', newBorderWidth,
    )

  @overload(QFont)
  def setAxisXLabelFont(self, newAxisXLabelFont: QFont) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setAxisXLabelFont(const QFont
    &newAxisXLabelFont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setAxisXLabelFont

    Parameters
    ----------

    newAxisXLabelFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphsTheme::setAxisXLabelFont(const QFont &newAxisXLabelFont)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme17setAxisXLabelFontERK5QFont',
        self._valueOf(newAxisXLabelFont),
    )

  @overload(QFont)
  def setAxisYLabelFont(self, newAxisYLabelFont: QFont) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setAxisYLabelFont(const QFont
    &newAxisYLabelFont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setAxisYLabelFont

    Parameters
    ----------

    newAxisYLabelFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphsTheme::setAxisYLabelFont(const QFont &newAxisYLabelFont)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme17setAxisYLabelFontERK5QFont',
        self._valueOf(newAxisYLabelFont),
    )

  @overload(QFont)
  def setAxisZLabelFont(self, newAxisZLabelFont: QFont) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setAxisZLabelFont(const QFont
    &newAxisZLabelFont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setAxisZLabelFont

    Parameters
    ----------

    newAxisZLabelFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphsTheme::setAxisZLabelFont(const QFont &newAxisZLabelFont)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme17setAxisZLabelFontERK5QFont',
        self._valueOf(newAxisZLabelFont),
    )

  @overload(QGraphsLine)
  def setGrid(self, newGrid: QGraphsLine) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setGrid(const QGraphsLine &newGrid)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setGrid

    Parameters
    ----------

    newGrid : QGraphsLine
      Passed on as a value: Qt reads the C++ QGraphsLine, which stays
      Python's own.
    """
    #  void QGraphsTheme::setGrid(const QGraphsLine &newGrid)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme7setGridERK11QGraphsLine',
        self._valueOf(newGrid),
    )

  @overload(QGraphsLine)
  def setAxisX(self, newAxisX: QGraphsLine) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setAxisX(const QGraphsLine &newAxisX)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setAxisX

    Parameters
    ----------

    newAxisX : QGraphsLine
      Passed on as a value: Qt reads the C++ QGraphsLine, which stays
      Python's own.
    """
    #  void QGraphsTheme::setAxisX(const QGraphsLine &newAxisX)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme8setAxisXERK11QGraphsLine',
        self._valueOf(newAxisX),
    )

  @overload(QGraphsLine)
  def setAxisY(self, newAxisY: QGraphsLine) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setAxisY(const QGraphsLine &newAxisY)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setAxisY

    Parameters
    ----------

    newAxisY : QGraphsLine
      Passed on as a value: Qt reads the C++ QGraphsLine, which stays
      Python's own.
    """
    #  void QGraphsTheme::setAxisY(const QGraphsLine &newAxisY)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme8setAxisYERK11QGraphsLine',
        self._valueOf(newAxisY),
    )

  @overload(QGraphsLine)
  def setAxisZ(self, newAxisZ: QGraphsLine) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setAxisZ(const QGraphsLine &newAxisZ)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setAxisZ

    Parameters
    ----------

    newAxisZ : QGraphsLine
      Passed on as a value: Qt reads the C++ QGraphsLine, which stays
      Python's own.
    """
    #  void QGraphsTheme::setAxisZ(const QGraphsLine &newAxisZ)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme8setAxisZERK11QGraphsLine',
        self._valueOf(newAxisZ),
    )

  def setColorSchemePalette(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setColorSchemePalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setColorSchemePalette
    """
    #  void QGraphsTheme::setColorSchemePalette()
    self.uglySide.call('ritual_ZN12QGraphsTheme21setColorSchemePaletteEv')

  def setThemePalette(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::setThemePalette()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#setThemePalette
    """
    #  void QGraphsTheme::setThemePalette()
    self.uglySide.call('ritual_ZN12QGraphsTheme15setThemePaletteEv')

  @overload(QQuickGradient)
  @overload(NoneType)
  def setSingleHighlightGradientQML(
      self,
      gradient: Optional[QQuickGradient],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphsTheme::setSingleHighlightGradientQML(QQuickGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setSingleHighlightGradientQML

    Parameters
    ----------

    gradient : Optional[QQuickGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsTheme::setSingleHighlightGradientQML(QQuickGradient
    #      *gradient)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme29setSingleHighlightGradientQMLEP14QQuickGr'
        'adient',
        self._addressOf(gradient),
    )

  @overload(QQuickGradient)
  @overload(NoneType)
  def setMultiHighlightGradientQML(
      self,
      gradient: Optional[QQuickGradient],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphsTheme::setMultiHighlightGradientQML(QQuickGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#setMultiHighlightGradientQML

    Parameters
    ----------

    gradient : Optional[QQuickGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsTheme::setMultiHighlightGradientQML(QQuickGradient
    #      *gradient)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme28setMultiHighlightGradientQMLEP14QQuickGra'
        'dient',
        self._addressOf(gradient),
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
    Notes what was given, for Qt's 'QGraphsTheme::QGraphsTheme(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#QGraphsTheme

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphsTheme::QGraphsTheme(QObject *parent)
    self._noteCreation(QGraphsTheme, lambda: Rituals.call(
        'ritual_ZN12QGraphsThemeC1EP7QObject',
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

  def resetThemeDirty(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::resetThemeDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#resetThemeDirty
    """
    #  void QGraphsTheme::resetThemeDirty()
    self.uglySide.call('ritual_ZN12QGraphsTheme15resetThemeDirtyEv')

  def resetColorTheme(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::resetColorTheme()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#resetColorTheme
    """
    #  void QGraphsTheme::resetColorTheme()
    self.uglySide.call('ritual_ZN12QGraphsTheme15resetColorThemeEv')

  def dirtyBits(self) -> Optional[QGraphsThemeDirtyBitField]:
    """
    Calls Qt's 'QGraphsThemeDirtyBitField *QGraphsTheme::dirtyBits()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#dirtyBits

    Returns
    -------

    Optional[QGraphsThemeDirtyBitField]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphsThemeDirtyBitField *QGraphsTheme::dirtyBits()
    address = self.uglySide.call('ritual_ZN12QGraphsTheme9dirtyBitsEv')
    from . import QGraphsThemeDirtyBitField
    return QGraphsThemeDirtyBitField._cuteAt(address)

  def resetDirtyBits(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::resetDirtyBits()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#resetDirtyBits
    """
    #  void QGraphsTheme::resetDirtyBits()
    self.uglySide.call('ritual_ZN12QGraphsTheme14resetDirtyBitsEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#update
    """
    #  void QGraphsTheme::update()
    self.uglySide.call('ritual_ZN12QGraphsTheme6updateEv')

  def colorSchemeChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::colorSchemeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#colorSchemeChanged
    """
    #  void QGraphsTheme::colorSchemeChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme18colorSchemeChangedEv')

  @overload(Theme)
  def themeChanged(self, theme: Theme) -> None:
    """
    Calls Qt's 'void QGraphsTheme::themeChanged(QGraphsTheme::Theme theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#themeChanged

    Parameters
    ----------

    theme : Theme
      Passed on as its number.
    """
    #  void QGraphsTheme::themeChanged(QGraphsTheme::Theme theme)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme12themeChangedENS_5ThemeE', theme.value,
    )

  @overload(ColorStyle)
  def colorStyleChanged(self, type: ColorStyle) -> None:
    """
    Calls Qt's 'void QGraphsTheme::colorStyleChanged(QGraphsTheme::ColorStyle
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#colorStyleChanged

    Parameters
    ----------

    type : ColorStyle
      Passed on as its number.
    """
    #  void QGraphsTheme::colorStyleChanged(QGraphsTheme::ColorStyle type)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme17colorStyleChangedENS_10ColorStyleE',
        type.value,
    )

  def backgroundColorChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::backgroundColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#backgroundColorChanged
    """
    #  void QGraphsTheme::backgroundColorChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme22backgroundColorChangedEv')

  def backgroundVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::backgroundVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#backgroundVisibleChanged
    """
    #  void QGraphsTheme::backgroundVisibleChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme24backgroundVisibleChangedEv')

  def plotAreaBackgroundColorChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::plotAreaBackgroundColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#plotAreaBackgroundColorChanged
    """
    #  void QGraphsTheme::plotAreaBackgroundColorChanged()
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme30plotAreaBackgroundColorChangedEv',
    )

  def plotAreaBackgroundVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::plotAreaBackgroundVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#plotAreaBackgroundVisibleChanged
    """
    #  void QGraphsTheme::plotAreaBackgroundVisibleChanged()
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme32plotAreaBackgroundVisibleChangedEv',
    )

  def gridVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::gridVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#gridVisibleChanged
    """
    #  void QGraphsTheme::gridVisibleChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme18gridVisibleChangedEv')

  def labelsVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::labelsVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#labelsVisibleChanged
    """
    #  void QGraphsTheme::labelsVisibleChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme20labelsVisibleChangedEv')

  def labelBackgroundColorChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::labelBackgroundColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#labelBackgroundColorChanged
    """
    #  void QGraphsTheme::labelBackgroundColorChanged()
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme27labelBackgroundColorChangedEv',
    )

  def labelTextColorChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::labelTextColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#labelTextColorChanged
    """
    #  void QGraphsTheme::labelTextColorChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme21labelTextColorChangedEv')

  @overload(QColor)
  def singleHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QGraphsTheme::singleHighlightColorChanged(QColor
    color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#singleHighlightColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsTheme::singleHighlightColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme27singleHighlightColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def multiHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QGraphsTheme::multiHighlightColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#multiHighlightColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsTheme::multiHighlightColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme26multiHighlightColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def singleHighlightGradientChanged(
      self,
      gradient: QLinearGradient,
  ) -> None:
    """
    Calls Qt's 'void QGraphsTheme::singleHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#singleHighlightGradientChanged

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QGraphsTheme::singleHighlightGradientChanged(const
    #      QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme30singleHighlightGradientChangedERK15QLinea'
        'rGradient',
        self._valueOf(gradient),
    )

  @overload(QLinearGradient)
  def multiHighlightGradientChanged(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QGraphsTheme::multiHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#multiHighlightGradientChanged

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QGraphsTheme::multiHighlightGradientChanged(const QLinearGradient
    #      &gradient)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme29multiHighlightGradientChangedERK15QLinear'
        'Gradient',
        self._valueOf(gradient),
    )

  def labelFontChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::labelFontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#labelFontChanged
    """
    #  void QGraphsTheme::labelFontChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme16labelFontChangedEv')

  def labelBackgroundVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::labelBackgroundVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#labelBackgroundVisibleChanged
    """
    #  void QGraphsTheme::labelBackgroundVisibleChanged()
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme29labelBackgroundVisibleChangedEv',
    )

  def labelBorderVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::labelBorderVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#labelBorderVisibleChanged
    """
    #  void QGraphsTheme::labelBorderVisibleChanged()
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme25labelBorderVisibleChangedEv',
    )

  @overload(QList[QColor])
  def seriesColorsChanged(self, list: QList[QColor]) -> None:
    """
    Calls Qt's 'void QGraphsTheme::seriesColorsChanged(const QList<QColor>
    &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#seriesColorsChanged

    Parameters
    ----------

    list : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGraphsTheme::seriesColorsChanged(const QList<QColor> &list)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme19seriesColorsChangedERK5QListI6QColorE',
        self._valueOf(list),
    )

  @overload(QList[QLinearGradient])
  def seriesGradientsChanged(self, list: QList[QLinearGradient]) -> None:
    """
    Calls Qt's 'void QGraphsTheme::seriesGradientsChanged(const
    QList<QLinearGradient> &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#seriesGradientsChanged

    Parameters
    ----------

    list : QList[QLinearGradient]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGraphsTheme::seriesGradientsChanged(const QList<QLinearGradient>
    #      &list)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme22seriesGradientsChangedERK5QListI15QLinear'
        'GradientE',
        self._valueOf(list),
    )

  def borderColorsChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::borderColorsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#borderColorsChanged
    """
    #  void QGraphsTheme::borderColorsChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme19borderColorsChangedEv')

  def borderWidthChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::borderWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#borderWidthChanged
    """
    #  void QGraphsTheme::borderWidthChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme18borderWidthChangedEv')

  def singleHighlightGradientQMLChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::singleHighlightGradientQMLChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html
    """
    #  void QGraphsTheme::singleHighlightGradientQMLChanged()
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme33singleHighlightGradientQMLChangedEv',
    )

  def multiHighlightGradientQMLChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::multiHighlightGradientQMLChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#multiHighlightGradientQMLChanged
    """
    #  void QGraphsTheme::multiHighlightGradientQMLChanged()
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme32multiHighlightGradientQMLChangedEv',
    )

  def axisXLabelFontChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::axisXLabelFontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#axisXLabelFontChanged
    """
    #  void QGraphsTheme::axisXLabelFontChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme21axisXLabelFontChangedEv')

  def axisYLabelFontChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::axisYLabelFontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#axisYLabelFontChanged
    """
    #  void QGraphsTheme::axisYLabelFontChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme21axisYLabelFontChangedEv')

  def axisZLabelFontChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::axisZLabelFontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#axisZLabelFontChanged
    """
    #  void QGraphsTheme::axisZLabelFontChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme21axisZLabelFontChangedEv')

  def gridChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::gridChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#gridChanged
    """
    #  void QGraphsTheme::gridChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme11gridChangedEv')

  def axisXChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::axisXChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#axisXChanged
    """
    #  void QGraphsTheme::axisXChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme12axisXChangedEv')

  def axisYChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::axisYChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#axisYChanged
    """
    #  void QGraphsTheme::axisYChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme12axisYChangedEv')

  def axisZChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::axisZChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#axisZChanged
    """
    #  void QGraphsTheme::axisZChanged()
    self.uglySide.call('ritual_ZN12QGraphsTheme12axisZChangedEv')

  def handleBaseColorUpdate(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::handleBaseColorUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#handleBaseColorUpdate
    """
    #  void QGraphsTheme::handleBaseColorUpdate()
    self.uglySide.call('ritual_ZN12QGraphsTheme21handleBaseColorUpdateEv')

  def handleBaseGradientUpdate(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::handleBaseGradientUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#handleBaseGradientUpdate
    """
    #  void QGraphsTheme::handleBaseGradientUpdate()
    self.uglySide.call('ritual_ZN12QGraphsTheme24handleBaseGradientUpdateEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#classBegin
    """
    #  void QGraphsTheme::classBegin()
    ritual = 'ritual_ZN12QGraphsTheme10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QGraphsTheme10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#componentComplete
    """
    #  void QGraphsTheme::componentComplete()
    ritual = 'ritual_ZN12QGraphsTheme17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QGraphsTheme17componentCompleteEv'
    self.uglySide.call(ritual)

  def updateAutomaticColorScheme(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::updateAutomaticColorScheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphstheme.html#updateAutomaticColorScheme
    """
    #  void QGraphsTheme::updateAutomaticColorScheme()
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme26updateAutomaticColorSchemeEv',
    )

  @overload(QColor, float)
  def createGradient(
      self,
      color: QColor,
      colorLevel: float,
  ) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient QGraphsTheme::createGradient(QColor color,
    float colorLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#createGradient

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    colorLevel : float
      Passed on as it is.

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient QGraphsTheme::createGradient(QColor color, float
    #      colorLevel)
    address = self.uglySide.call(
        'ritual_ZN12QGraphsTheme14createGradientE6QColorf',
        self._valueOf(color), colorLevel,
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  @overload(QQuickGradient)
  @overload(NoneType)
  def convertGradient(
      self,
      gradient: Optional[QQuickGradient],
  ) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient QGraphsTheme::convertGradient(QQuickGradient
    *gradient)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#convertGradient

    Parameters
    ----------

    gradient : Optional[QQuickGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient QGraphsTheme::convertGradient(QQuickGradient
    #      *gradient)
    address = self.uglySide.call(
        'ritual_ZN12QGraphsTheme15convertGradientEP14QQuickGradient',
        self._addressOf(gradient),
    )
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  @overload(QQuickGraphsColor)
  @overload(NoneType)
  def addColor(self, color: Optional[QQuickGraphsColor]) -> None:
    """
    Calls Qt's 'void QGraphsTheme::addColor(QQuickGraphsColor *color)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#addColor

    Parameters
    ----------

    color : Optional[QQuickGraphsColor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsTheme::addColor(QQuickGraphsColor *color)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme8addColorEP17QQuickGraphsColor',
        self._addressOf(color),
    )

  def colorList(self) -> QList[QQuickGraphsColor]:
    """
    Calls Qt's 'QList<QQuickGraphsColor *> QGraphsTheme::colorList()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#colorList

    Returns
    -------

    QList[QQuickGraphsColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickGraphsColor *> QGraphsTheme::colorList()
    address = self.uglySide.call('ritual_ZN12QGraphsTheme9colorListEv')
    from . import QQuickGraphsColor
    return QList[QQuickGraphsColor]._cuteOwning(address)

  def clearColors(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::clearColors()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#clearColors
    """
    #  void QGraphsTheme::clearColors()
    self.uglySide.call('ritual_ZN12QGraphsTheme11clearColorsEv')

  def clearDummyColors(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::clearDummyColors()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#clearDummyColors
    """
    #  void QGraphsTheme::clearDummyColors()
    self.uglySide.call('ritual_ZN12QGraphsTheme16clearDummyColorsEv')

  def clearGradients(self) -> None:
    """
    Calls Qt's 'void QGraphsTheme::clearGradients()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#clearGradients
    """
    #  void QGraphsTheme::clearGradients()
    self.uglySide.call('ritual_ZN12QGraphsTheme14clearGradientsEv')

  def gradientList(self) -> QList[QQuickGradient]:
    """
    Calls Qt's 'QList<QQuickGradient *> QGraphsTheme::gradientList()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#gradientList

    Returns
    -------

    QList[QQuickGradient]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickGradient *> QGraphsTheme::gradientList()
    address = self.uglySide.call('ritual_ZN12QGraphsTheme12gradientListEv')
    from ..QtQuick import QQuickGradient
    return QList[QQuickGradient]._cuteOwning(address)

  @overload(QQuickGradient)
  @overload(NoneType)
  def addGradient(self, gradient: Optional[QQuickGradient]) -> None:
    """
    Calls Qt's 'void QGraphsTheme::addGradient(QQuickGradient *gradient)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#addGradient

    Parameters
    ----------

    gradient : Optional[QQuickGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsTheme::addGradient(QQuickGradient *gradient)
    self.uglySide.call(
        'ritual_ZN12QGraphsTheme11addGradientEP14QQuickGradient',
        self._addressOf(gradient),
    )

  def d_func(self) -> Optional[QGraphsThemePrivate]:
    """
    Calls Qt's 'QGraphsThemePrivate *QGraphsTheme::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphstheme.html#d_func

    Returns
    -------

    Optional[QGraphsThemePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphsThemePrivate *QGraphsTheme::d_func()
    address = self.uglySide.call('ritual_ZN12QGraphsTheme6d_funcEv')
    from . import QGraphsThemePrivate
    return QGraphsThemePrivate._cuteAt(address)

  @staticmethod
  def appendBaseColorsFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphsTheme::appendBaseColorsFunc(QQmlListProperty<QQuickGraphsColor>
    *list, QQuickGraphsColor *color)': names
    'QQmlListProperty<QQuickGraphsColor>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.appendBaseColorsFunc' has no cute function yet. Qt's "
        "'void "
        "QGraphsTheme::appendBaseColorsFunc(QQmlListProperty<QQuickGraphsCol"
        "or> *list, QQuickGraphsColor *color)': names "
        "'QQmlListProperty<QQuickGraphsColor>', which has no cute class yet."
    )

  @staticmethod
  def appendBaseGradientsFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphsTheme::appendBaseGradientsFunc(QQmlListProperty<QQuickGradient>
    *list, QQuickGradient *gradient)': names
    'QQmlListProperty<QQuickGradient>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.appendBaseGradientsFunc' has no cute function yet. "
        "Qt's 'void "
        "QGraphsTheme::appendBaseGradientsFunc(QQmlListProperty<QQuickGradie"
        "nt> *list, QQuickGradient *gradient)': names "
        "'QQmlListProperty<QQuickGradient>', which has no cute class yet.")

  @staticmethod
  def appendThemeChildren(*__, **_) -> Never:
    """
    Qt's 'void QGraphsTheme::appendThemeChildren(QQmlListProperty<QObject>
    *list, QObject *element)': names 'QQmlListProperty<QObject>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.appendThemeChildren' has no cute function yet. Qt's "
        "'void QGraphsTheme::appendThemeChildren(QQmlListProperty<QObject> "
        "*list, QObject *element)': names 'QQmlListProperty<QObject>', "
        "which has no cute class yet.")

  @staticmethod
  def atBaseColorsFunc(*__, **_) -> Never:
    """
    Qt's 'QQuickGraphsColor
    *QGraphsTheme::atBaseColorsFunc(QQmlListProperty<QQuickGraphsColor>
    *list, qsizetype index)': names 'QQmlListProperty<QQuickGraphsColor>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.atBaseColorsFunc' has no cute function yet. Qt's "
        "'QQuickGraphsColor "
        "*QGraphsTheme::atBaseColorsFunc(QQmlListProperty<QQuickGraphsColor>"
        " *list, qsizetype index)': names "
        "'QQmlListProperty<QQuickGraphsColor>', which has no cute class yet."
    )

  @staticmethod
  def atBaseGradientsFunc(*__, **_) -> Never:
    """
    Qt's 'QQuickGradient
    *QGraphsTheme::atBaseGradientsFunc(QQmlListProperty<QQuickGradient>
    *list, qsizetype index)': names 'QQmlListProperty<QQuickGradient>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.atBaseGradientsFunc' has no cute function yet. Qt's "
        "'QQuickGradient "
        "*QGraphsTheme::atBaseGradientsFunc(QQmlListProperty<QQuickGradient>"
        " *list, qsizetype index)': names "
        "'QQmlListProperty<QQuickGradient>', which has no cute class yet.")

  @staticmethod
  def baseColorsQML(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickGraphsColor> QGraphsTheme::baseColorsQML()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.baseColorsQML' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickGraphsColor> "
        "QGraphsTheme::baseColorsQML()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def baseGradientsQML(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickGradient> QGraphsTheme::baseGradientsQML()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.baseGradientsQML' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickGradient> "
        "QGraphsTheme::baseGradientsQML()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def clearBaseColorsFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphsTheme::clearBaseColorsFunc(QQmlListProperty<QQuickGraphsColor>
    *list)': names 'QQmlListProperty<QQuickGraphsColor>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.clearBaseColorsFunc' has no cute function yet. Qt's "
        "'void "
        "QGraphsTheme::clearBaseColorsFunc(QQmlListProperty<QQuickGraphsColo"
        "r> *list)': names 'QQmlListProperty<QQuickGraphsColor>', which has "
        "no cute class yet.")

  @staticmethod
  def clearBaseGradientsFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphsTheme::clearBaseGradientsFunc(QQmlListProperty<QQuickGradient>
    *list)': names 'QQmlListProperty<QQuickGradient>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.clearBaseGradientsFunc' has no cute function yet. "
        "Qt's 'void "
        "QGraphsTheme::clearBaseGradientsFunc(QQmlListProperty<QQuickGradien"
        "t> *list)': names 'QQmlListProperty<QQuickGradient>', which has no "
        "cute class yet.")

  @staticmethod
  def countBaseColorsFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QGraphsTheme::countBaseColorsFunc(QQmlListProperty<QQuickGraphsColor>
    *list)': names 'QQmlListProperty<QQuickGraphsColor>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.countBaseColorsFunc' has no cute function yet. Qt's "
        "'qsizetype "
        "QGraphsTheme::countBaseColorsFunc(QQmlListProperty<QQuickGraphsColo"
        "r> *list)': names 'QQmlListProperty<QQuickGraphsColor>', which has "
        "no cute class yet.")

  @staticmethod
  def countBaseGradientsFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QGraphsTheme::countBaseGradientsFunc(QQmlListProperty<QQuickGradient>
    *list)': names 'QQmlListProperty<QQuickGradient>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.countBaseGradientsFunc' has no cute function yet. "
        "Qt's 'qsizetype "
        "QGraphsTheme::countBaseGradientsFunc(QQmlListProperty<QQuickGradien"
        "t> *list)': names 'QQmlListProperty<QQuickGradient>', which has no "
        "cute class yet.")

  @staticmethod
  def setThemeGradient(*__, **_) -> Never:
    """
    Qt's 'void QGraphsTheme::setThemeGradient(QQuickGradient *gradient,
    GradientQMLStyle type)': names the enum 'QGraphsTheme::GradientQMLStyle',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QGraphsTheme.setThemeGradient' has no cute function yet. Qt's "
        "'void QGraphsTheme::setThemeGradient(QQuickGradient *gradient, "
        "GradientQMLStyle type)': names the enum "
        "'QGraphsTheme::GradientQMLStyle', whose class cannot be named here."
    )

  @staticmethod
  def themeChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QGraphsTheme::themeChildren()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGraphsTheme.themeChildren' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QGraphsTheme::themeChildren()': gives a "
        "type Python has no way to take yet.")


#  Qt's 'QList<QGraphsTheme *>': the list of QGraphsTheme, which
#  'QList[QGraphsTheme]' gives. It is made here, so that there is one as soon
#  as there can be a QGraphsTheme.
QList.createKind(
    QGraphsTheme, 'address',
    make='ritual_list_make_QGraphsTheme_ptr',
    add='ritual_list_add_QGraphsTheme_ptr',
    size='ritual_list_size_QGraphsTheme_ptr',
    at='ritual_list_at_QGraphsTheme_ptr',
    drop='ritual_list_drop_QGraphsTheme_ptr',
)
