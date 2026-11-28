"""
DeclarativeChart binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativechart_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means DeclarativeChart to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from ..QtCharts import QChart
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEasingCurve, QLocale, QMetaObject, QPointF, QRectF
  from ..QtGui import QColor, QFont, QHoverEvent, QMouseEvent
  from ..QtCharts import QAbstractAxis, QAbstractSeries, QLegend
  from ..QtQuick import QSGNode
  from . import DeclarativeAxes, DeclarativeMargins
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DeclarativeAxes = WAIT['DeclarativeAxes']
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QColor = WAIT['QColor']
  QEasingCurve = WAIT['QEasingCurve']
  QFont = WAIT['QFont']
  QHoverEvent = WAIT['QHoverEvent']
  QLocale = WAIT['QLocale']
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeChart(QQuickItem):
  """
  The cute side of Qt's DeclarativeChart: a plain Python object standing in
  front of one C++ DeclarativeChart.

  It is built on the cute 'QQuickItem', as Qt's DeclarativeChart is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeChart that has a ritual and that Python
  can call so far, 91 names in all: 'metaObject', 'tr', 'componentComplete',
  'geometryChange', 'updatePaintNode', 'mousePressEvent',
  'mouseReleaseEvent', 'hoverMoveEvent', 'mouseDoubleClickEvent',
  'handleAntialiasingChanged', 'sceneChanged', 'renderScene', 'setTheme',
  'theme', 'setAnimationOptions', 'animationOptions', 'setAnimationDuration',
  'animationDuration', 'setAnimationEasingCurve', 'animationEasingCurve',
  'setTitle', 'title', 'legend', 'titleFont', 'setTitleFont',
  'setTitleColor', 'titleColor', 'setBackgroundColor', 'backgroundColor',
  'setPlotAreaColor', 'plotAreaColor', 'setLocalizeNumbers',
  'localizeNumbers', 'setLocale', 'locale', 'count', 'setDropShadowEnabled',
  'dropShadowEnabled', 'backgroundRoundness', 'setBackgroundRoundness',
  'margins', 'plotArea', 'setPlotArea', 'defaultAxis', 'initializeAxes',
  'doInitializeAxes', 'series', 'createSeries', 'removeSeries',
  'removeAllSeries', 'setAxisX', 'setAxisY', 'axisX', 'axisY', 'zoom',
  'zoomIn', 'zoomOut', 'zoomReset', 'isZoomed', 'scrollLeft', 'scrollRight',
  'scrollUp', 'scrollDown', 'mapToValue', 'mapToPosition',
  'axisLabelsChanged', 'titleColorChanged', 'backgroundColorChanged',
  'dropShadowEnabledChanged', 'marginsChanged', 'plotAreaChanged',
  'seriesAdded', 'seriesRemoved', 'plotAreaColorChanged',
  'backgroundRoundnessChanged', 'localizeNumbersChanged', 'localeChanged',
  'animationDurationChanged', 'animationEasingCurveChanged', 'needRender',
  'pendingRenderNodeMouseEventResponses', 'changeMargins', 'handleAxisXSet',
  'handleAxisYSet', 'handleAxisXTopSet', 'handleAxisYRightSet',
  'handleSeriesAdded', 'handlePendingRenderNodeMouseEventResponses',
  'initChart', 'seriesAxisAttachHelper', 'queueRendererMouseEvent'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeChart::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int DeclarativeChart::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'DeclarativeChart::~DeclarativeChart()': the destructor: Python
    never removes a C++ DeclarativeChart.
  - Qt's 'QQmlListProperty<QAbstractAxis> DeclarativeChart::axes()': gives a
    type Python has no way to take yet.
  - Qt's 'void
    DeclarativeChart::axesAppendFunc(QQmlListProperty<QAbstractAxis> *list,
    QAbstractAxis *element)': names 'QQmlListProperty<QAbstractAxis>', which
    has no cute class yet.
  - Qt's 'qsizetype
    DeclarativeChart::axesCountFunc(QQmlListProperty<QAbstractAxis> *list)':
    names 'QQmlListProperty<QAbstractAxis>', which has no cute class yet.
  - Qt's 'QAbstractAxis
    *DeclarativeChart::axesAtFunc(QQmlListProperty<QAbstractAxis> *list,
    qsizetype index)': names 'QQmlListProperty<QAbstractAxis>', which has no
    cute class yet.
  - Qt's 'void
    DeclarativeChart::axesClearFunc(QQmlListProperty<QAbstractAxis> *list)':
    names 'QQmlListProperty<QAbstractAxis>', which has no cute class yet.
  - Qt's 'void DeclarativeChart::findMinMaxForSeries(QAbstractSeries *series,
    Qt::Orientations orientation, qreal &min, qreal &max)': takes a number to
    change where it is.

  What has no ritual
  ------------------

  2 of the 106 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeChart is created at the first use, not by
    'DeclarativeChart(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeChart.
  - Qt tells when it has removed the C++ DeclarativeChart. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DeclarativeChart that has no cute function yet, 'axes',
    'axesAppendFunc', 'axesAtFunc', 'axesClearFunc', 'axesCountFunc',
    'findMinMaxForSeries', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside DeclarativeChart, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Animation(CuteNum):
    """
    The enum 'DeclarativeChart::Animation' of Qt, with the 4 names Qt gives
    in it.
    """

    NoAnimation = Kee[int](0)
    GridAxisAnimations = Kee[int](1)
    SeriesAnimations = Kee[int](2)
    AllAnimations = Kee[int](3)

  class SeriesType(CuteNum):
    """
    The enum 'DeclarativeChart::SeriesType' of Qt, with the 13 names Qt gives
    in it.
    """

    SeriesTypeLine = Kee[int](0)
    SeriesTypeArea = Kee[int](1)
    SeriesTypeBar = Kee[int](2)
    SeriesTypeStackedBar = Kee[int](3)
    SeriesTypePercentBar = Kee[int](4)
    SeriesTypePie = Kee[int](5)
    SeriesTypeScatter = Kee[int](6)
    SeriesTypeSpline = Kee[int](7)
    SeriesTypeHorizontalBar = Kee[int](8)
    SeriesTypeHorizontalStackedBar = Kee[int](9)
    SeriesTypeHorizontalPercentBar = Kee[int](10)
    SeriesTypeBoxPlot = Kee[int](11)
    SeriesTypeCandlestick = Kee[int](12)

  class Theme(CuteNum):
    """
    The enum 'DeclarativeChart::Theme' of Qt, with the 8 names Qt gives in
    it.
    """

    ChartThemeLight = Kee[int](0)
    ChartThemeBlueCerulean = Kee[int](1)
    ChartThemeDark = Kee[int](2)
    ChartThemeBrownSand = Kee[int](3)
    ChartThemeBlueNcs = Kee[int](4)
    ChartThemeHighContrast = Kee[int](5)
    ChartThemeBlueIcy = Kee[int](6)
    ChartThemeQt = Kee[int](7)

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
    Calls Qt's 'QString DeclarativeChart::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#tr

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
    #  QString DeclarativeChart::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16DeclarativeChart2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeChart'

  #  A C++ DeclarativeChart Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DeclarativeChart'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeChart::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeChart::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16DeclarativeChart10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def animationDuration(self) -> int:
    """
    Calls Qt's 'int DeclarativeChart::animationDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#animationDuration
    """
    #  int DeclarativeChart::animationDuration() const
    return self.uglySide.call(
        'ritual_ZNK16DeclarativeChart17animationDurationEv',
    )

  def animationEasingCurve(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve DeclarativeChart::animationEasingCurve() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#animationEasingCurve

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve DeclarativeChart::animationEasingCurve() const
    address = self.uglySide.call(
        'ritual_ZNK16DeclarativeChart20animationEasingCurveEv',
    )
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def titleFont(self) -> QFont:
    """
    Calls Qt's 'QFont DeclarativeChart::titleFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#titleFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont DeclarativeChart::titleFont() const
    address = self.uglySide.call('ritual_ZNK16DeclarativeChart9titleFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def localizeNumbers(self) -> bool:
    """
    Calls Qt's 'bool DeclarativeChart::localizeNumbers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#localizeNumbers
    """
    #  bool DeclarativeChart::localizeNumbers() const
    return self.uglySide.call(
        'ritual_ZNK16DeclarativeChart15localizeNumbersEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale DeclarativeChart::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale DeclarativeChart::locale() const
    address = self.uglySide.call('ritual_ZNK16DeclarativeChart6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def backgroundRoundness(self) -> float:
    """
    Calls Qt's 'qreal DeclarativeChart::backgroundRoundness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#backgroundRoundness
    """
    #  qreal DeclarativeChart::backgroundRoundness() const
    return self.uglySide.call(
        'ritual_ZNK16DeclarativeChart19backgroundRoundnessEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Theme)
  def setTheme(self, theme: Theme) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setTheme(DeclarativeChart::Theme
    theme)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#setTheme

    Parameters
    ----------

    theme : Theme
      Passed on as its number.
    """
    #  void DeclarativeChart::setTheme(DeclarativeChart::Theme theme)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart8setThemeENS_5ThemeE', theme.value,
    )

  @overload(Animation)
  def setAnimationOptions(self, animations: Animation) -> None:
    """
    Calls Qt's 'void
    DeclarativeChart::setAnimationOptions(DeclarativeChart::Animation
    animations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#setAnimationOptions

    Parameters
    ----------

    animations : Animation
      Passed on as its number.
    """
    #  void DeclarativeChart::setAnimationOptions(DeclarativeChart::Animation
    #      animations)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart19setAnimationOptionsENS_9AnimationE',
        animations.value,
    )

  @overload(int)
  def setAnimationDuration(self, msecs: int) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setAnimationDuration(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#setAnimationDuration

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void DeclarativeChart::setAnimationDuration(int msecs)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart20setAnimationDurationEi', msecs,
    )

  @overload(QEasingCurve)
  def setAnimationEasingCurve(self, curve: QEasingCurve) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setAnimationEasingCurve(const
    QEasingCurve &curve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#setAnimationEasingCurve

    Parameters
    ----------

    curve : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void DeclarativeChart::setAnimationEasingCurve(const QEasingCurve
    #      &curve)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart23setAnimationEasingCurveERK12QEasingCu'
        'rve',
        self._valueOf(curve),
    )

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setTitle(QString title)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeChart::setTitle(QString title)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart8setTitleE7QString', title,
    )

  @overload(QFont)
  def setTitleFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setTitleFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#setTitleFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void DeclarativeChart::setTitleFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart12setTitleFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QColor)
  def setTitleColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setTitleColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#setTitleColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void DeclarativeChart::setTitleColor(QColor color)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart13setTitleColorE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setBackgroundColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#setBackgroundColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void DeclarativeChart::setBackgroundColor(QColor color)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart18setBackgroundColorE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setPlotAreaColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setPlotAreaColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#setPlotAreaColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void DeclarativeChart::setPlotAreaColor(QColor color)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart16setPlotAreaColorE6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setLocalizeNumbers(self, localize: bool) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setLocalizeNumbers(bool localize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#setLocalizeNumbers

    Parameters
    ----------

    localize : bool
      Passed on as it is.
    """
    #  void DeclarativeChart::setLocalizeNumbers(bool localize)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart18setLocalizeNumbersEb', localize,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void DeclarativeChart::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(bool)
  def setDropShadowEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setDropShadowEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#setDropShadowEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void DeclarativeChart::setDropShadowEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart20setDropShadowEnabledEb', enabled,
    )

  @overload(float)
  def setBackgroundRoundness(self, diameter: float) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setBackgroundRoundness(qreal
    diameter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#setBackgroundRoundness

    Parameters
    ----------

    diameter : float
      Passed on as it is.
    """
    #  void DeclarativeChart::setBackgroundRoundness(qreal diameter)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart22setBackgroundRoundnessEd', diameter,
    )

  @overload(QRectF)
  def setPlotArea(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setPlotArea(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#setPlotArea

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void DeclarativeChart::setPlotArea(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart11setPlotAreaERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  @overload(QAbstractAxis, QAbstractSeries)
  @overload(QAbstractAxis, NoneType)
  @overload(NoneType, QAbstractSeries)
  @overload(NoneType, NoneType)
  def setAxisX(
      self,
      axis: Optional[QAbstractAxis],
      series: Optional[QAbstractSeries] = None,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setAxisX(QAbstractAxis *axis,
    QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void DeclarativeChart::setAxisX(QAbstractAxis *axis, QAbstractSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart8setAxisXEP13QAbstractAxisP15QAbstractS'
        'eries',
        self._addressOf(axis), self._addressOf(series),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  @overload(QAbstractAxis, QAbstractSeries)
  @overload(QAbstractAxis, NoneType)
  @overload(NoneType, QAbstractSeries)
  @overload(NoneType, NoneType)
  def setAxisY(
      self,
      axis: Optional[QAbstractAxis],
      series: Optional[QAbstractSeries] = None,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeChart::setAxisY(QAbstractAxis *axis,
    QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void DeclarativeChart::setAxisY(QAbstractAxis *axis, QAbstractSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart8setAxisYEP13QAbstractAxisP15QAbstractS'
        'eries',
        self._addressOf(axis), self._addressOf(series),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'DeclarativeChart::DeclarativeChart(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#DeclarativeChart

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeChart::DeclarativeChart(QQuickItem *parent)
    self._noteCreation(DeclarativeChart, lambda: Rituals.call(
        'ritual_ZN16DeclarativeChartC1EP10QQuickItem',
        self._addressOf(parent),
    ))

  @overload(QChart.ChartType, QQuickItem)
  @overload(QChart.ChartType, NoneType)
  def __init__(
      self,
      type: QChart.ChartType,
      parent: Optional[QQuickItem],
  ) -> None:
    """
    Notes what was given, for Qt's
    'DeclarativeChart::DeclarativeChart(QChart::ChartType type, QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#DeclarativeChart

    Parameters
    ----------

    type : QChart.ChartType
      Passed on as its number.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  DeclarativeChart::DeclarativeChart(QChart::ChartType type, QQuickItem
    #      *parent)
    self._noteCreation(DeclarativeChart, lambda: Rituals.call(
        'ritual_ZN16DeclarativeChartC1EN6QChart9ChartTypeEP10QQuickItem',
        type.value, self._addressOf(parent),
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#componentComplete
    """
    #  void DeclarativeChart::componentComplete()
    ritual = 'ritual_ZN16DeclarativeChart17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16DeclarativeChart17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void DeclarativeChart::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void DeclarativeChart::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN16DeclarativeChart14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16DeclarativeChart14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *DeclarativeChart::updatePaintNode(QSGNode *oldNode,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
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
    #  QSGNode *DeclarativeChart::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN16DeclarativeChart15updatePaintNodeEP7QSGNodePN10QQuickIt'
        'em19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16DeclarativeChart15updatePaintNodeEP7QSGNodePN10QQ'
          'uickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(oldNode, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN16DeclarativeChart15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16DeclarativeChart15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::mouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN16DeclarativeChart17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16DeclarativeChart17mouseReleaseEventEP11QMouseEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN16DeclarativeChart14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16DeclarativeChart14hoverMoveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN16DeclarativeChart21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16DeclarativeChart21mouseDoubleClickEventEP11QMouse'
          'Event')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(bool)
  def handleAntialiasingChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void DeclarativeChart::handleAntialiasingChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#handleAntialiasingChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void DeclarativeChart::handleAntialiasingChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart25handleAntialiasingChangedEb', enable,
    )

  @overload(QList[QRectF])
  def sceneChanged(self, region: QList[QRectF]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::sceneChanged(const QList<QRectF>
    &region)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#sceneChanged

    Parameters
    ----------

    region : QList[QRectF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DeclarativeChart::sceneChanged(const QList<QRectF> &region)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart12sceneChangedERK5QListI6QRectFE',
        self._valueOf(region),
    )

  def renderScene(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::renderScene()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#renderScene
    """
    #  void DeclarativeChart::renderScene()
    self.uglySide.call('ritual_ZN16DeclarativeChart11renderSceneEv')

  def theme(self) -> Theme:
    """
    Calls Qt's 'DeclarativeChart::Theme DeclarativeChart::theme()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#theme

    Returns
    -------

    Theme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Theme(number)' gives.
    """
    #  DeclarativeChart::Theme DeclarativeChart::theme()
    return DeclarativeChart.Theme(self.uglySide.call(
        'ritual_ZN16DeclarativeChart5themeEv',
    ))

  def animationOptions(self) -> Animation:
    """
    Calls Qt's 'DeclarativeChart::Animation
    DeclarativeChart::animationOptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#animationOptions

    Returns
    -------

    Animation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Animation(number)' gives.
    """
    #  DeclarativeChart::Animation DeclarativeChart::animationOptions()
    return DeclarativeChart.Animation(self.uglySide.call(
        'ritual_ZN16DeclarativeChart16animationOptionsEv',
    ))

  def title(self) -> str:
    """
    Calls Qt's 'QString DeclarativeChart::title()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeChart::title()
    return self.uglySide.call('ritual_ZN16DeclarativeChart5titleEv')

  def legend(self) -> Optional[QLegend]:
    """
    Calls Qt's 'QLegend *DeclarativeChart::legend()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#legend

    Returns
    -------

    Optional[QLegend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLegend *DeclarativeChart::legend()
    address = self.uglySide.call('ritual_ZN16DeclarativeChart6legendEv')
    from ..QtCharts import QLegend
    return QLegend._cuteAt(address)

  def titleColor(self) -> QColor:
    """
    Calls Qt's 'QColor DeclarativeChart::titleColor()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#titleColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor DeclarativeChart::titleColor()
    address = self.uglySide.call('ritual_ZN16DeclarativeChart10titleColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor DeclarativeChart::backgroundColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor DeclarativeChart::backgroundColor()
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart15backgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def plotAreaColor(self) -> QColor:
    """
    Calls Qt's 'QColor DeclarativeChart::plotAreaColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#plotAreaColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor DeclarativeChart::plotAreaColor()
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart13plotAreaColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int DeclarativeChart::count()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#count
    """
    #  int DeclarativeChart::count()
    return self.uglySide.call('ritual_ZN16DeclarativeChart5countEv')

  def dropShadowEnabled(self) -> bool:
    """
    Calls Qt's 'bool DeclarativeChart::dropShadowEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#dropShadowEnabled
    """
    #  bool DeclarativeChart::dropShadowEnabled()
    return self.uglySide.call(
        'ritual_ZN16DeclarativeChart17dropShadowEnabledEv',
    )

  def margins(self) -> Optional[DeclarativeMargins]:
    """
    Calls Qt's 'DeclarativeMargins *DeclarativeChart::margins()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#margins

    Returns
    -------

    Optional[DeclarativeMargins]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativeMargins *DeclarativeChart::margins()
    address = self.uglySide.call('ritual_ZN16DeclarativeChart7marginsEv')
    from . import DeclarativeMargins
    return DeclarativeMargins._cuteAt(address)

  def plotArea(self) -> QRectF:
    """
    Calls Qt's 'QRectF DeclarativeChart::plotArea()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#plotArea

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF DeclarativeChart::plotArea()
    address = self.uglySide.call('ritual_ZN16DeclarativeChart8plotAreaEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Qt.Orientation, QAbstractSeries)
  @overload(Qt.Orientation, NoneType)
  def defaultAxis(
      self,
      orientation: Qt.Orientation,
      series: Optional[QAbstractSeries],
  ) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeChart::defaultAxis(Qt::Orientation
    orientation, QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#defaultAxis

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeChart::defaultAxis(Qt::Orientation
    #      orientation, QAbstractSeries *series)
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart11defaultAxisEN2Qt11OrientationEP15QAbs'
        'tractSeries',
        orientation.value, self._addressOf(series),
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload(QAbstractSeries)
  @overload(NoneType)
  def initializeAxes(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::initializeAxes(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#initializeAxes

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::initializeAxes(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart14initializeAxesEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries, DeclarativeAxes)
  @overload(QAbstractSeries, NoneType)
  @overload(NoneType, DeclarativeAxes)
  @overload(NoneType, NoneType)
  def doInitializeAxes(
      self,
      series: Optional[QAbstractSeries],
      axes: Optional[DeclarativeAxes],
  ) -> None:
    """
    Calls Qt's 'void DeclarativeChart::doInitializeAxes(QAbstractSeries
    *series, DeclarativeAxes *axes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#doInitializeAxes

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    axes : Optional[DeclarativeAxes]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::doInitializeAxes(QAbstractSeries *series,
    #      DeclarativeAxes *axes)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart16doInitializeAxesEP15QAbstractSeriesP1'
        '5DeclarativeAxes',
        self._addressOf(series), self._addressOf(axes),
    )

  @overload(int)
  def series(self, index: int) -> Optional[QAbstractSeries]:
    """
    Calls Qt's 'QAbstractSeries *DeclarativeChart::series(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#series

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QAbstractSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSeries *DeclarativeChart::series(int index)
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart6seriesEi', index,
    )
    from ..QtCharts import QAbstractSeries
    return QAbstractSeries._cuteAt(address)

  @overload(str)
  def series(self, seriesName: str) -> Optional[QAbstractSeries]:
    """
    Calls Qt's 'QAbstractSeries *DeclarativeChart::series(QString
    seriesName)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#series

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAbstractSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSeries *DeclarativeChart::series(QString seriesName)
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart6seriesE7QString', seriesName,
    )
    from ..QtCharts import QAbstractSeries
    return QAbstractSeries._cuteAt(address)

  @overload(int)
  @overload(int, str)
  @overload(int, str, QAbstractAxis)
  @overload(int, str, NoneType)
  @overload(int, str, QAbstractAxis, QAbstractAxis)
  @overload(int, str, QAbstractAxis, NoneType)
  @overload(int, str, NoneType, QAbstractAxis)
  @overload(int, str, NoneType, NoneType)
  def createSeries(
      self,
      type: int,
      name: str = '',
      axisX: Optional[QAbstractAxis] = None,
      axisY: Optional[QAbstractAxis] = None,
  ) -> Optional[QAbstractSeries]:
    """
    Calls Qt's 'QAbstractSeries *DeclarativeChart::createSeries(int type,
    QString name, QAbstractAxis *axisX, QAbstractAxis *axisY)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#createSeries

    Parameters
    ----------

    type : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    axisX : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    axisY : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QAbstractSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSeries *DeclarativeChart::createSeries(int type, QString
    #      name, QAbstractAxis *axisX, QAbstractAxis *axisY)
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart12createSeriesEi7QStringP13QAbstractAxi'
        'sS2_',
        type, name, self._addressOf(axisX), self._addressOf(axisY),
    )
    from ..QtCharts import QAbstractSeries
    return QAbstractSeries._cuteAt(address)

  @overload(QAbstractSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::removeSeries(QAbstractSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#removeSeries

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::removeSeries(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart12removeSeriesEP15QAbstractSeries',
        self._addressOf(series),
    )

  def removeAllSeries(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::removeAllSeries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#removeAllSeries
    """
    #  void DeclarativeChart::removeAllSeries()
    self.uglySide.call('ritual_ZN16DeclarativeChart15removeAllSeriesEv')

  @overload()
  @overload(QAbstractSeries)
  @overload(NoneType)
  def axisX(
      self,
      series: Optional[QAbstractSeries] = None,
  ) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeChart::axisX(QAbstractSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#axisX

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeChart::axisX(QAbstractSeries *series)
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart5axisXEP15QAbstractSeries',
        self._addressOf(series),
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload()
  @overload(QAbstractSeries)
  @overload(NoneType)
  def axisY(
      self,
      series: Optional[QAbstractSeries] = None,
  ) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeChart::axisY(QAbstractSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#axisY

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeChart::axisY(QAbstractSeries *series)
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart5axisYEP15QAbstractSeries',
        self._addressOf(series),
    )
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload(float)
  def zoom(self, factor: float) -> None:
    """
    Calls Qt's 'void DeclarativeChart::zoom(qreal factor)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#zoom

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void DeclarativeChart::zoom(qreal factor)
    self.uglySide.call('ritual_ZN16DeclarativeChart4zoomEd', factor)

  @overload()
  def zoomIn(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::zoomIn()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#zoomIn
    """
    #  void DeclarativeChart::zoomIn()
    self.uglySide.call('ritual_ZN16DeclarativeChart6zoomInEv')

  @overload(QRectF)
  def zoomIn(self, rectangle: QRectF) -> None:
    """
    Calls Qt's 'void DeclarativeChart::zoomIn(const QRectF &rectangle)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#zoomIn

    Parameters
    ----------

    rectangle : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void DeclarativeChart::zoomIn(const QRectF &rectangle)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart6zoomInERK6QRectF',
        self._valueOf(rectangle),
    )

  def zoomOut(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::zoomOut()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#zoomOut
    """
    #  void DeclarativeChart::zoomOut()
    self.uglySide.call('ritual_ZN16DeclarativeChart7zoomOutEv')

  def zoomReset(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::zoomReset()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#zoomReset
    """
    #  void DeclarativeChart::zoomReset()
    self.uglySide.call('ritual_ZN16DeclarativeChart9zoomResetEv')

  def isZoomed(self) -> bool:
    """
    Calls Qt's 'bool DeclarativeChart::isZoomed()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#isZoomed
    """
    #  bool DeclarativeChart::isZoomed()
    return self.uglySide.call('ritual_ZN16DeclarativeChart8isZoomedEv')

  @overload(float)
  def scrollLeft(self, pixels: float) -> None:
    """
    Calls Qt's 'void DeclarativeChart::scrollLeft(qreal pixels)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#scrollLeft

    Parameters
    ----------

    pixels : float
      Passed on as it is.
    """
    #  void DeclarativeChart::scrollLeft(qreal pixels)
    self.uglySide.call('ritual_ZN16DeclarativeChart10scrollLeftEd', pixels)

  @overload(float)
  def scrollRight(self, pixels: float) -> None:
    """
    Calls Qt's 'void DeclarativeChart::scrollRight(qreal pixels)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#scrollRight

    Parameters
    ----------

    pixels : float
      Passed on as it is.
    """
    #  void DeclarativeChart::scrollRight(qreal pixels)
    self.uglySide.call('ritual_ZN16DeclarativeChart11scrollRightEd', pixels)

  @overload(float)
  def scrollUp(self, pixels: float) -> None:
    """
    Calls Qt's 'void DeclarativeChart::scrollUp(qreal pixels)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#scrollUp

    Parameters
    ----------

    pixels : float
      Passed on as it is.
    """
    #  void DeclarativeChart::scrollUp(qreal pixels)
    self.uglySide.call('ritual_ZN16DeclarativeChart8scrollUpEd', pixels)

  @overload(float)
  def scrollDown(self, pixels: float) -> None:
    """
    Calls Qt's 'void DeclarativeChart::scrollDown(qreal pixels)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#scrollDown

    Parameters
    ----------

    pixels : float
      Passed on as it is.
    """
    #  void DeclarativeChart::scrollDown(qreal pixels)
    self.uglySide.call('ritual_ZN16DeclarativeChart10scrollDownEd', pixels)

  @overload(QPointF)
  @overload(QPointF, QAbstractSeries)
  @overload(QPointF, NoneType)
  def mapToValue(
      self,
      position: QPointF,
      series: Optional[QAbstractSeries] = None,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF DeclarativeChart::mapToValue(const QPointF &position,
    QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#mapToValue

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF DeclarativeChart::mapToValue(const QPointF &position,
    #      QAbstractSeries *series)
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart10mapToValueERK7QPointFP15QAbstractSeri'
        'es',
        self._valueOf(position, 'QPointF'), self._addressOf(series),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPointF)
  @overload(QPointF, QAbstractSeries)
  @overload(QPointF, NoneType)
  def mapToPosition(
      self,
      value: QPointF,
      series: Optional[QAbstractSeries] = None,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF DeclarativeChart::mapToPosition(const QPointF &value,
    QAbstractSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#mapToPosition

    Parameters
    ----------

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF DeclarativeChart::mapToPosition(const QPointF &value,
    #      QAbstractSeries *series)
    address = self.uglySide.call(
        'ritual_ZN16DeclarativeChart13mapToPositionERK7QPointFP15QAbstractS'
        'eries',
        self._valueOf(value, 'QPointF'), self._addressOf(series),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def axisLabelsChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::axisLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#axisLabelsChanged
    """
    #  void DeclarativeChart::axisLabelsChanged()
    self.uglySide.call('ritual_ZN16DeclarativeChart17axisLabelsChangedEv')

  @overload(QColor)
  def titleColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void DeclarativeChart::titleColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#titleColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void DeclarativeChart::titleColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart17titleColorChangedE6QColor',
        self._valueOf(color),
    )

  def backgroundColorChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::backgroundColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#backgroundColorChanged
    """
    #  void DeclarativeChart::backgroundColorChanged()
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart22backgroundColorChangedEv',
    )

  @overload(bool)
  def dropShadowEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void DeclarativeChart::dropShadowEnabledChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#dropShadowEnabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void DeclarativeChart::dropShadowEnabledChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart24dropShadowEnabledChangedEb', enabled,
    )

  def marginsChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::marginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#marginsChanged
    """
    #  void DeclarativeChart::marginsChanged()
    self.uglySide.call('ritual_ZN16DeclarativeChart14marginsChangedEv')

  @overload(QRectF)
  def plotAreaChanged(self, plotArea: QRectF) -> None:
    """
    Calls Qt's 'void DeclarativeChart::plotAreaChanged(QRectF plotArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#plotAreaChanged

    Parameters
    ----------

    plotArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void DeclarativeChart::plotAreaChanged(QRectF plotArea)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart15plotAreaChangedE6QRectF',
        self._valueOf(plotArea),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def seriesAdded(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::seriesAdded(QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#seriesAdded

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::seriesAdded(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart11seriesAddedEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def seriesRemoved(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::seriesRemoved(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#seriesRemoved

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::seriesRemoved(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart13seriesRemovedEP15QAbstractSeries',
        self._addressOf(series),
    )

  def plotAreaColorChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::plotAreaColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#plotAreaColorChanged
    """
    #  void DeclarativeChart::plotAreaColorChanged()
    self.uglySide.call('ritual_ZN16DeclarativeChart20plotAreaColorChangedEv')

  @overload(float)
  def backgroundRoundnessChanged(self, diameter: float) -> None:
    """
    Calls Qt's 'void DeclarativeChart::backgroundRoundnessChanged(qreal
    diameter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#backgroundRoundnessChanged

    Parameters
    ----------

    diameter : float
      Passed on as it is.
    """
    #  void DeclarativeChart::backgroundRoundnessChanged(qreal diameter)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart26backgroundRoundnessChangedEd',
        diameter,
    )

  def localizeNumbersChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::localizeNumbersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#localizeNumbersChanged
    """
    #  void DeclarativeChart::localizeNumbersChanged()
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart22localizeNumbersChangedEv',
    )

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#localeChanged
    """
    #  void DeclarativeChart::localeChanged()
    self.uglySide.call('ritual_ZN16DeclarativeChart13localeChangedEv')

  @overload(int)
  def animationDurationChanged(self, msecs: int) -> None:
    """
    Calls Qt's 'void DeclarativeChart::animationDurationChanged(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#animationDurationChanged

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void DeclarativeChart::animationDurationChanged(int msecs)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart24animationDurationChangedEi', msecs,
    )

  @overload(QEasingCurve)
  def animationEasingCurveChanged(self, curve: QEasingCurve) -> None:
    """
    Calls Qt's 'void
    DeclarativeChart::animationEasingCurveChanged(QEasingCurve curve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#animationEasingCurveChanged

    Parameters
    ----------

    curve : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void DeclarativeChart::animationEasingCurveChanged(QEasingCurve curve)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart27animationEasingCurveChangedE12QEasing'
        'Curve',
        self._valueOf(curve),
    )

  def needRender(self) -> None:
    """
    Calls Qt's 'void DeclarativeChart::needRender()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#needRender
    """
    #  void DeclarativeChart::needRender()
    self.uglySide.call('ritual_ZN16DeclarativeChart10needRenderEv')

  def pendingRenderNodeMouseEventResponses(self) -> None:
    """
    Calls Qt's 'void
    DeclarativeChart::pendingRenderNodeMouseEventResponses()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html
    """
    #  void DeclarativeChart::pendingRenderNodeMouseEventResponses()
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart36pendingRenderNodeMouseEventResponsesE'
        'v',
    )

  @overload(int, int, int, int)
  def changeMargins(
      self,
      top: int,
      bottom: int,
      left: int,
      right: int,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeChart::changeMargins(int top, int bottom, int
    left, int right)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#changeMargins

    Parameters
    ----------

    top : int
      Passed on as it is.

    bottom : int
      Passed on as it is.

    left : int
      Passed on as it is.

    right : int
      Passed on as it is.
    """
    #  void DeclarativeChart::changeMargins(int top, int bottom, int left,
    #      int right)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart13changeMarginsEiiii',
        top, bottom, left, right,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def handleAxisXSet(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::handleAxisXSet(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#handleAxisXSet

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::handleAxisXSet(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart14handleAxisXSetEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def handleAxisYSet(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::handleAxisYSet(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#handleAxisYSet

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::handleAxisYSet(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart14handleAxisYSetEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def handleAxisXTopSet(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::handleAxisXTopSet(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#handleAxisXTopSet

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::handleAxisXTopSet(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart17handleAxisXTopSetEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def handleAxisYRightSet(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::handleAxisYRightSet(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#handleAxisYRightSet

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::handleAxisYRightSet(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart19handleAxisYRightSetEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesAdded(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::handleSeriesAdded(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#handleSeriesAdded

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::handleSeriesAdded(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart17handleSeriesAddedEP15QAbstractSeries',
        self._addressOf(series),
    )

  def handlePendingRenderNodeMouseEventResponses(self) -> None:
    """
    Calls Qt's 'void
    DeclarativeChart::handlePendingRenderNodeMouseEventResponses()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html
    """
    #  void DeclarativeChart::handlePendingRenderNodeMouseEventResponses()
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart42handlePendingRenderNodeMouseEventResp'
        'onsesEv',
    )

  @overload(QChart.ChartType)
  def initChart(self, type: QChart.ChartType) -> None:
    """
    Calls Qt's 'void DeclarativeChart::initChart(QChart::ChartType type)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativechart.html#initChart

    Parameters
    ----------

    type : QChart.ChartType
      Passed on as its number.
    """
    #  void DeclarativeChart::initChart(QChart::ChartType type)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart9initChartEN6QChart9ChartTypeE',
        type.value,
    )

  @overload(QAbstractSeries, QAbstractAxis, Qt.Orientations, Qt.Alignment)
  @overload(QAbstractSeries, NoneType, Qt.Orientations, Qt.Alignment)
  @overload(NoneType, QAbstractAxis, Qt.Orientations, Qt.Alignment)
  @overload(NoneType, NoneType, Qt.Orientations, Qt.Alignment)
  def seriesAxisAttachHelper(
      self,
      series: Optional[QAbstractSeries],
      axis: Optional[QAbstractAxis],
      orientation: Qt.Orientations,
      alignment: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeChart::seriesAxisAttachHelper(QAbstractSeries
    *series, QAbstractAxis *axis, Qt::Orientations orientation, Qt::Alignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#seriesAxisAttachHelper

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : Qt.Orientations
      Passed on as its number.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void DeclarativeChart::seriesAxisAttachHelper(QAbstractSeries *series,
    #      QAbstractAxis *axis, Qt::Orientations orientation, Qt::Alignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart22seriesAxisAttachHelperEP15QAbstractSe'
        'riesP13QAbstractAxis6QFlagsIN2Qt11OrientationEES4_INS5_13Alignment'
        'FlagEE',
        self._addressOf(series), self._addressOf(axis), orientation.value,
        alignment.value,
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def queueRendererMouseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void DeclarativeChart::queueRendererMouseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativechart.html#queueRendererMouseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeChart::queueRendererMouseEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN16DeclarativeChart23queueRendererMouseEventEP11QMouseEven'
        't',
        self._addressOf(event),
    )

  @staticmethod
  def axes(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QAbstractAxis> DeclarativeChart::axes()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativeChart.axes' has no cute function yet. Qt's "
        "'QQmlListProperty<QAbstractAxis> DeclarativeChart::axes()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def axesAppendFunc(*__, **_) -> Never:
    """
    Qt's 'void
    DeclarativeChart::axesAppendFunc(QQmlListProperty<QAbstractAxis> *list,
    QAbstractAxis *element)': names 'QQmlListProperty<QAbstractAxis>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeChart.axesAppendFunc' has no cute function yet. Qt's "
        "'void "
        "DeclarativeChart::axesAppendFunc(QQmlListProperty<QAbstractAxis> "
        "*list, QAbstractAxis *element)': names "
        "'QQmlListProperty<QAbstractAxis>', which has no cute class yet.")

  @staticmethod
  def axesAtFunc(*__, **_) -> Never:
    """
    Qt's 'QAbstractAxis
    *DeclarativeChart::axesAtFunc(QQmlListProperty<QAbstractAxis> *list,
    qsizetype index)': names 'QQmlListProperty<QAbstractAxis>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeChart.axesAtFunc' has no cute function yet. Qt's "
        "'QAbstractAxis "
        "*DeclarativeChart::axesAtFunc(QQmlListProperty<QAbstractAxis> "
        "*list, qsizetype index)': names 'QQmlListProperty<QAbstractAxis>', "
        "which has no cute class yet.")

  @staticmethod
  def axesClearFunc(*__, **_) -> Never:
    """
    Qt's 'void
    DeclarativeChart::axesClearFunc(QQmlListProperty<QAbstractAxis> *list)':
    names 'QQmlListProperty<QAbstractAxis>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeChart.axesClearFunc' has no cute function yet. Qt's "
        "'void "
        "DeclarativeChart::axesClearFunc(QQmlListProperty<QAbstractAxis> "
        "*list)': names 'QQmlListProperty<QAbstractAxis>', which has no "
        "cute class yet.")

  @staticmethod
  def axesCountFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    DeclarativeChart::axesCountFunc(QQmlListProperty<QAbstractAxis> *list)':
    names 'QQmlListProperty<QAbstractAxis>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativeChart.axesCountFunc' has no cute function yet. Qt's "
        "'qsizetype "
        "DeclarativeChart::axesCountFunc(QQmlListProperty<QAbstractAxis> "
        "*list)': names 'QQmlListProperty<QAbstractAxis>', which has no "
        "cute class yet.")

  @staticmethod
  def findMinMaxForSeries(*__, **_) -> Never:
    """
    Qt's 'void DeclarativeChart::findMinMaxForSeries(QAbstractSeries *series,
    Qt::Orientations orientation, qreal &min, qreal &max)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'DeclarativeChart.findMinMaxForSeries' has no cute function yet. "
        "Qt's 'void DeclarativeChart::findMinMaxForSeries(QAbstractSeries "
        "*series, Qt::Orientations orientation, qreal &min, qreal &max)': "
        "takes a number to change where it is.")
