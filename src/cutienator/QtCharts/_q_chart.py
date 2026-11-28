"""
QChart binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qchart.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from ..QtWidgets import QGraphicsItem, QGraphicsWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEasingCurve, QLocale, QMargins, QMetaObject, QPointF
  from ..QtCore import QRectF
  from ..QtGui import QBrush, QFont, QPen
  from . import QAbstractAxis, QAbstractSeries, QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QBrush = WAIT['QBrush']
  QEasingCurve = WAIT['QEasingCurve']
  QFont = WAIT['QFont']
  QLocale = WAIT['QLocale']
  QMargins = WAIT['QMargins']
  QPen = WAIT['QPen']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QChart(QGraphicsWidget):
  """
  The cute side of Qt's QChart: a plain Python object standing in front of
  one C++ QChart.

  It is built on the cute 'QGraphicsWidget', as Qt's QChart is built on Qt's
  QGraphicsWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QChart that has a ritual and that Python can call so
  far, 63 names in all: 'metaObject', 'tr', 'addSeries', 'removeSeries',
  'removeAllSeries', 'series', 'setAxisX', 'setAxisY', 'axisX', 'axisY',
  'addAxis', 'removeAxis', 'axes', 'createDefaultAxes', 'setTheme', 'theme',
  'setTitle', 'title', 'setTitleFont', 'titleFont', 'setTitleBrush',
  'titleBrush', 'setBackgroundBrush', 'backgroundBrush', 'setBackgroundPen',
  'backgroundPen', 'setBackgroundVisible', 'isBackgroundVisible',
  'setDropShadowEnabled', 'isDropShadowEnabled', 'setBackgroundRoundness',
  'backgroundRoundness', 'setAnimationOptions', 'animationOptions',
  'setAnimationDuration', 'animationDuration', 'setAnimationEasingCurve',
  'animationEasingCurve', 'zoomIn', 'zoomOut', 'zoom', 'zoomReset',
  'isZoomed', 'scroll', 'legend', 'setMargins', 'margins', 'plotArea',
  'setPlotArea', 'setPlotAreaBackgroundBrush', 'plotAreaBackgroundBrush',
  'setPlotAreaBackgroundPen', 'plotAreaBackgroundPen',
  'setPlotAreaBackgroundVisible', 'isPlotAreaBackgroundVisible',
  'setLocalizeNumbers', 'localizeNumbers', 'setLocale', 'locale',
  'mapToValue', 'mapToPosition', 'chartType', 'plotAreaChanged'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QChart::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QChart::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QChart::~QChart()': the destructor: Python never removes a C++
    QChart.

  What has no ritual
  ------------------

  4 of the 73 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QChart is created at the first use, not by 'QChart(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QChart.
  - Qt tells when it has removed the C++ QChart. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QChart, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class AnimationOption(CuteFlags):
    """
    The flags enum 'QChart::AnimationOption' of Qt, with the 4 names Qt gives
    in it. Qt names the type of its combinations 'QChart::AnimationOptions'.
    """

    NoAnimation = 0x0
    GridAxisAnimations = 0x1
    SeriesAnimations = 0x2
    AllAnimations = 0x3

  AnimationOptions = AnimationOption

  class ChartTheme(CuteNum):
    """
    The enum 'QChart::ChartTheme' of Qt, with the 8 names Qt gives in it.
    """

    ChartThemeLight = Kee[int](0)
    ChartThemeBlueCerulean = Kee[int](1)
    ChartThemeDark = Kee[int](2)
    ChartThemeBrownSand = Kee[int](3)
    ChartThemeBlueNcs = Kee[int](4)
    ChartThemeHighContrast = Kee[int](5)
    ChartThemeBlueIcy = Kee[int](6)
    ChartThemeQt = Kee[int](7)

  class ChartType(CuteNum):
    """
    The enum 'QChart::ChartType' of Qt, with the 3 names Qt gives in it.
    """

    ChartTypeUndefined = Kee[int](0)
    ChartTypeCartesian = Kee[int](1)
    ChartTypePolar = Kee[int](2)

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
    Calls Qt's 'QString QChart::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#tr

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
    #  QString QChart::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6QChart2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QChart'

  #  A C++ QChart Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QChart'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QChart::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QChart::metaObject() const
    address = self.uglySide.call('ritual_ZNK6QChart10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def series(self) -> QList[QAbstractSeries]:
    """
    Calls Qt's 'QList<QAbstractSeries *> QChart::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#series

    Returns
    -------

    QList[QAbstractSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractSeries *> QChart::series() const
    address = self.uglySide.call('ritual_ZNK6QChart6seriesEv')
    from . import QAbstractSeries
    return QList[QAbstractSeries]._cuteOwning(address)

  @overload()
  @overload(QAbstractSeries)
  @overload(NoneType)
  def axisX(
      self,
      series: Optional[QAbstractSeries] = None,
  ) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *QChart::axisX(QAbstractSeries *series) const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#axisX

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
    #  QAbstractAxis *QChart::axisX(QAbstractSeries *series) const
    address = self.uglySide.call(
        'ritual_ZNK6QChart5axisXEP15QAbstractSeries',
        self._addressOf(series),
    )
    from . import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload()
  @overload(QAbstractSeries)
  @overload(NoneType)
  def axisY(
      self,
      series: Optional[QAbstractSeries] = None,
  ) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *QChart::axisY(QAbstractSeries *series) const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#axisY

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
    #  QAbstractAxis *QChart::axisY(QAbstractSeries *series) const
    address = self.uglySide.call(
        'ritual_ZNK6QChart5axisYEP15QAbstractSeries',
        self._addressOf(series),
    )
    from . import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  @overload()
  @overload(Qt.Orientations)
  @overload(Qt.Orientations, QAbstractSeries)
  @overload(Qt.Orientations, NoneType)
  def axes(
      self,
      orientation: Qt.Orientations = (
          Qt.Orientations.Horizontal | Qt.Orientations.Vertical),
      series: Optional[QAbstractSeries] = None,
  ) -> QList[QAbstractAxis]:
    """
    Calls Qt's 'QList<QAbstractAxis *> QChart::axes(Qt::Orientations
    orientation, QAbstractSeries *series) const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#axes

    Parameters
    ----------

    orientation : Qt.Orientations
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientations.Horizontal | Qt.Orientations.Vertical.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QList[QAbstractAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractAxis *> QChart::axes(Qt::Orientations orientation,
    #      QAbstractSeries *series) const
    address = self.uglySide.call(
        'ritual_ZNK6QChart4axesE6QFlagsIN2Qt11OrientationEEP15QAbstractSeri'
        'es',
        orientation.value, self._addressOf(series),
    )
    from . import QAbstractAxis
    return QList[QAbstractAxis]._cuteOwning(address)

  def theme(self) -> ChartTheme:
    """
    Calls Qt's 'QChart::ChartTheme QChart::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#theme

    Returns
    -------

    ChartTheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ChartTheme(number)'
      gives.
    """
    #  QChart::ChartTheme QChart::theme() const
    return QChart.ChartTheme(self.uglySide.call('ritual_ZNK6QChart5themeEv'))

  def title(self) -> str:
    """
    Calls Qt's 'QString QChart::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QChart::title() const
    return self.uglySide.call('ritual_ZNK6QChart5titleEv')

  def titleFont(self) -> QFont:
    """
    Calls Qt's 'QFont QChart::titleFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#titleFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QChart::titleFont() const
    address = self.uglySide.call('ritual_ZNK6QChart9titleFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def titleBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QChart::titleBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#titleBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QChart::titleBrush() const
    address = self.uglySide.call('ritual_ZNK6QChart10titleBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def backgroundBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QChart::backgroundBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#backgroundBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QChart::backgroundBrush() const
    address = self.uglySide.call('ritual_ZNK6QChart15backgroundBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def backgroundPen(self) -> QPen:
    """
    Calls Qt's 'QPen QChart::backgroundPen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#backgroundPen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QChart::backgroundPen() const
    address = self.uglySide.call('ritual_ZNK6QChart13backgroundPenEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def isBackgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool QChart::isBackgroundVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#isBackgroundVisible
    """
    #  bool QChart::isBackgroundVisible() const
    return self.uglySide.call('ritual_ZNK6QChart19isBackgroundVisibleEv')

  def isDropShadowEnabled(self) -> bool:
    """
    Calls Qt's 'bool QChart::isDropShadowEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#isDropShadowEnabled
    """
    #  bool QChart::isDropShadowEnabled() const
    return self.uglySide.call('ritual_ZNK6QChart19isDropShadowEnabledEv')

  def backgroundRoundness(self) -> float:
    """
    Calls Qt's 'qreal QChart::backgroundRoundness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#backgroundRoundness
    """
    #  qreal QChart::backgroundRoundness() const
    return self.uglySide.call('ritual_ZNK6QChart19backgroundRoundnessEv')

  def animationOptions(self) -> AnimationOptions:
    """
    Calls Qt's 'AnimationOptions QChart::animationOptions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#animationOptions

    Returns
    -------

    AnimationOptions
      The value standing for the combination Qt gave back.
    """
    #  AnimationOptions QChart::animationOptions() const
    return QChart.AnimationOptions(self.uglySide.call(
        'ritual_ZNK6QChart16animationOptionsEv',
    ))

  def animationDuration(self) -> int:
    """
    Calls Qt's 'int QChart::animationDuration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#animationDuration
    """
    #  int QChart::animationDuration() const
    return self.uglySide.call('ritual_ZNK6QChart17animationDurationEv')

  def animationEasingCurve(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QChart::animationEasingCurve() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#animationEasingCurve

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QChart::animationEasingCurve() const
    address = self.uglySide.call('ritual_ZNK6QChart20animationEasingCurveEv')
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def legend(self) -> Optional[QLegend]:
    """
    Calls Qt's 'QLegend *QChart::legend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#legend

    Returns
    -------

    Optional[QLegend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLegend *QChart::legend() const
    address = self.uglySide.call('ritual_ZNK6QChart6legendEv')
    from . import QLegend
    return QLegend._cuteAt(address)

  def margins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QChart::margins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#margins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QChart::margins() const
    address = self.uglySide.call('ritual_ZNK6QChart7marginsEv')
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  def plotArea(self) -> QRectF:
    """
    Calls Qt's 'QRectF QChart::plotArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#plotArea

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QChart::plotArea() const
    address = self.uglySide.call('ritual_ZNK6QChart8plotAreaEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def plotAreaBackgroundBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QChart::plotAreaBackgroundBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qchart.html#plotAreaBackgroundBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QChart::plotAreaBackgroundBrush() const
    address = self.uglySide.call(
        'ritual_ZNK6QChart23plotAreaBackgroundBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def plotAreaBackgroundPen(self) -> QPen:
    """
    Calls Qt's 'QPen QChart::plotAreaBackgroundPen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#plotAreaBackgroundPen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QChart::plotAreaBackgroundPen() const
    address = self.uglySide.call(
        'ritual_ZNK6QChart21plotAreaBackgroundPenEv',
    )
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def isPlotAreaBackgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool QChart::isPlotAreaBackgroundVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qchart.html#isPlotAreaBackgroundVisible
    """
    #  bool QChart::isPlotAreaBackgroundVisible() const
    return self.uglySide.call(
        'ritual_ZNK6QChart27isPlotAreaBackgroundVisibleEv',
    )

  def localizeNumbers(self) -> bool:
    """
    Calls Qt's 'bool QChart::localizeNumbers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#localizeNumbers
    """
    #  bool QChart::localizeNumbers() const
    return self.uglySide.call('ritual_ZNK6QChart15localizeNumbersEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QChart::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QChart::locale() const
    address = self.uglySide.call('ritual_ZNK6QChart6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def chartType(self) -> ChartType:
    """
    Calls Qt's 'ChartType QChart::chartType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#chartType

    Returns
    -------

    ChartType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ChartType(number)' gives.
    """
    #  ChartType QChart::chartType() const
    return QChart.ChartType(self.uglySide.call(
        'ritual_ZNK6QChart9chartTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'void QChart::setAxisX(QAbstractAxis *axis, QAbstractSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QChart::setAxisX(QAbstractAxis *axis, QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN6QChart8setAxisXEP13QAbstractAxisP15QAbstractSeries',
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
    Calls Qt's 'void QChart::setAxisY(QAbstractAxis *axis, QAbstractSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QChart::setAxisY(QAbstractAxis *axis, QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN6QChart8setAxisYEP13QAbstractAxisP15QAbstractSeries',
        self._addressOf(axis), self._addressOf(series),
    )

  @overload(ChartTheme)
  def setTheme(self, theme: ChartTheme) -> None:
    """
    Calls Qt's 'void QChart::setTheme(QChart::ChartTheme theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setTheme

    Parameters
    ----------

    theme : ChartTheme
      Passed on as its number.
    """
    #  void QChart::setTheme(QChart::ChartTheme theme)
    self.uglySide.call(
        'ritual_ZN6QChart8setThemeENS_10ChartThemeE', theme.value,
    )

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QChart::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QChart::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN6QChart8setTitleERK7QString', title)

  @overload(QFont)
  def setTitleFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QChart::setTitleFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setTitleFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QChart::setTitleFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN6QChart12setTitleFontERK5QFont', self._valueOf(font),
    )

  @overload(QBrush)
  def setTitleBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QChart::setTitleBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setTitleBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QChart::setTitleBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN6QChart13setTitleBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QBrush)
  def setBackgroundBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QChart::setBackgroundBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setBackgroundBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QChart::setBackgroundBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN6QChart18setBackgroundBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QPen)
  def setBackgroundPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QChart::setBackgroundPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setBackgroundPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QChart::setBackgroundPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN6QChart16setBackgroundPenERK4QPen', self._valueOf(pen),
    )

  @overload()
  @overload(bool)
  def setBackgroundVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QChart::setBackgroundVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setBackgroundVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QChart::setBackgroundVisible(bool visible)
    self.uglySide.call('ritual_ZN6QChart20setBackgroundVisibleEb', visible)

  @overload()
  @overload(bool)
  def setDropShadowEnabled(self, enabled: bool = True) -> None:
    """
    Calls Qt's 'void QChart::setDropShadowEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setDropShadowEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QChart::setDropShadowEnabled(bool enabled)
    self.uglySide.call('ritual_ZN6QChart20setDropShadowEnabledEb', enabled)

  @overload(float)
  def setBackgroundRoundness(self, diameter: float) -> None:
    """
    Calls Qt's 'void QChart::setBackgroundRoundness(qreal diameter)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setBackgroundRoundness

    Parameters
    ----------

    diameter : float
      Passed on as it is.
    """
    #  void QChart::setBackgroundRoundness(qreal diameter)
    self.uglySide.call(
        'ritual_ZN6QChart22setBackgroundRoundnessEd', diameter,
    )

  @overload(AnimationOptions)
  def setAnimationOptions(self, options: AnimationOptions) -> None:
    """
    Calls Qt's 'void QChart::setAnimationOptions(AnimationOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setAnimationOptions

    Parameters
    ----------

    options : AnimationOptions
      Passed on as its number.
    """
    #  void QChart::setAnimationOptions(AnimationOptions options)
    self.uglySide.call(
        'ritual_ZN6QChart19setAnimationOptionsE6QFlagsINS_15AnimationOption'
        'EE',
        options.value,
    )

  @overload(int)
  def setAnimationDuration(self, msecs: int) -> None:
    """
    Calls Qt's 'void QChart::setAnimationDuration(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setAnimationDuration

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QChart::setAnimationDuration(int msecs)
    self.uglySide.call('ritual_ZN6QChart20setAnimationDurationEi', msecs)

  @overload(QEasingCurve)
  def setAnimationEasingCurve(self, curve: QEasingCurve) -> None:
    """
    Calls Qt's 'void QChart::setAnimationEasingCurve(const QEasingCurve
    &curve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qchart.html#setAnimationEasingCurve

    Parameters
    ----------

    curve : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QChart::setAnimationEasingCurve(const QEasingCurve &curve)
    self.uglySide.call(
        'ritual_ZN6QChart23setAnimationEasingCurveERK12QEasingCurve',
        self._valueOf(curve),
    )

  @overload(QMargins)
  def setMargins(self, margins: QMargins) -> None:
    """
    Calls Qt's 'void QChart::setMargins(const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setMargins

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  void QChart::setMargins(const QMargins &margins)
    self.uglySide.call(
        'ritual_ZN6QChart10setMarginsERK8QMargins',
        self._valueOf(margins, 'QMargins'),
    )

  @overload(QRectF)
  def setPlotArea(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QChart::setPlotArea(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setPlotArea

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QChart::setPlotArea(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN6QChart11setPlotAreaERK6QRectF', self._valueOf(rect),
    )

  @overload(QBrush)
  def setPlotAreaBackgroundBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QChart::setPlotAreaBackgroundBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qchart.html#setPlotAreaBackgroundBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QChart::setPlotAreaBackgroundBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN6QChart26setPlotAreaBackgroundBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QPen)
  def setPlotAreaBackgroundPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QChart::setPlotAreaBackgroundPen(const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qchart.html#setPlotAreaBackgroundPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QChart::setPlotAreaBackgroundPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN6QChart24setPlotAreaBackgroundPenERK4QPen',
        self._valueOf(pen),
    )

  @overload()
  @overload(bool)
  def setPlotAreaBackgroundVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QChart::setPlotAreaBackgroundVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qchart.html#setPlotAreaBackgroundVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QChart::setPlotAreaBackgroundVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN6QChart28setPlotAreaBackgroundVisibleEb', visible,
    )

  @overload(bool)
  def setLocalizeNumbers(self, localize: bool) -> None:
    """
    Calls Qt's 'void QChart::setLocalizeNumbers(bool localize)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setLocalizeNumbers

    Parameters
    ----------

    localize : bool
      Passed on as it is.
    """
    #  void QChart::setLocalizeNumbers(bool localize)
    self.uglySide.call('ritual_ZN6QChart18setLocalizeNumbersEb', localize)

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QChart::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QChart::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN6QChart9setLocaleERK7QLocale', self._valueOf(locale),
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
  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QGraphicsItem] = None,
      wFlags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QChart::QChart(QGraphicsItem *parent,
    Qt::WindowFlags wFlags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#QChart

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    wFlags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QChart::QChart(QGraphicsItem *parent, Qt::WindowFlags wFlags)
    self._noteCreation(QChart, lambda: Rituals.call(
        'ritual_ZN6QChartC1EP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent, 'QGraphicsItem'), wFlags.value,
    ))

  @overload(ChartType, QGraphicsItem, Qt.WindowFlags)
  @overload(ChartType, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      type: ChartType,
      parent: Optional[QGraphicsItem],
      wFlags: Qt.WindowFlags,
  ) -> None:
    """
    Notes what was given, for Qt's 'QChart::QChart(QChart::ChartType type,
    QGraphicsItem *parent, Qt::WindowFlags wFlags)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#QChart

    Parameters
    ----------

    type : ChartType
      Passed on as its number.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    wFlags : Qt.WindowFlags
      Passed on as its number.
    """
    #  QChart::QChart(QChart::ChartType type, QGraphicsItem *parent,
    #      Qt::WindowFlags wFlags)
    self._noteCreation(QChart, lambda: Rituals.call(
        'ritual_ZN6QChartC1ENS_9ChartTypeEP13QGraphicsItem6QFlagsIN2Qt10Win'
        'dowTypeEE',
        type.value, self._addressOf(parent, 'QGraphicsItem'), wFlags.value,
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

  @overload(QAbstractSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void QChart::addSeries(QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#addSeries

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChart::addSeries(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN6QChart9addSeriesEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void QChart::removeSeries(QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#removeSeries

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChart::removeSeries(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN6QChart12removeSeriesEP15QAbstractSeries',
        self._addressOf(series),
    )

  def removeAllSeries(self) -> None:
    """
    Calls Qt's 'void QChart::removeAllSeries()'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#removeAllSeries
    """
    #  void QChart::removeAllSeries()
    self.uglySide.call('ritual_ZN6QChart15removeAllSeriesEv')

  @overload(QAbstractAxis, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def addAxis(
      self,
      axis: Optional[QAbstractAxis],
      alignment: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void QChart::addAxis(QAbstractAxis *axis, Qt::Alignment
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#addAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QChart::addAxis(QAbstractAxis *axis, Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN6QChart7addAxisEP13QAbstractAxis6QFlagsIN2Qt13AlignmentFl'
        'agEE',
        self._addressOf(axis), alignment.value,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def removeAxis(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void QChart::removeAxis(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#removeAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChart::removeAxis(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN6QChart10removeAxisEP13QAbstractAxis',
        self._addressOf(axis),
    )

  def createDefaultAxes(self) -> None:
    """
    Calls Qt's 'void QChart::createDefaultAxes()'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#createDefaultAxes
    """
    #  void QChart::createDefaultAxes()
    self.uglySide.call('ritual_ZN6QChart17createDefaultAxesEv')

  @overload()
  def zoomIn(self) -> None:
    """
    Calls Qt's 'void QChart::zoomIn()'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#zoomIn
    """
    #  void QChart::zoomIn()
    self.uglySide.call('ritual_ZN6QChart6zoomInEv')

  @overload(QRectF)
  def zoomIn(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QChart::zoomIn(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#zoomIn

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QChart::zoomIn(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN6QChart6zoomInERK6QRectF', self._valueOf(rect),
    )

  def zoomOut(self) -> None:
    """
    Calls Qt's 'void QChart::zoomOut()'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#zoomOut
    """
    #  void QChart::zoomOut()
    self.uglySide.call('ritual_ZN6QChart7zoomOutEv')

  @overload(float)
  def zoom(self, factor: float) -> None:
    """
    Calls Qt's 'void QChart::zoom(qreal factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#zoom

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QChart::zoom(qreal factor)
    self.uglySide.call('ritual_ZN6QChart4zoomEd', factor)

  def zoomReset(self) -> None:
    """
    Calls Qt's 'void QChart::zoomReset()'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#zoomReset
    """
    #  void QChart::zoomReset()
    self.uglySide.call('ritual_ZN6QChart9zoomResetEv')

  def isZoomed(self) -> bool:
    """
    Calls Qt's 'bool QChart::isZoomed()'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#isZoomed
    """
    #  bool QChart::isZoomed()
    return self.uglySide.call('ritual_ZN6QChart8isZoomedEv')

  @overload(float, float)
  def scroll(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QChart::scroll(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#scroll

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QChart::scroll(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN6QChart6scrollEdd', dx, dy)

  @overload(QPointF)
  @overload(QPointF, QAbstractSeries)
  @overload(QPointF, NoneType)
  def mapToValue(
      self,
      position: QPointF,
      series: Optional[QAbstractSeries] = None,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QChart::mapToValue(const QPointF &position,
    QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#mapToValue

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
    #  QPointF QChart::mapToValue(const QPointF &position, QAbstractSeries
    #      *series)
    address = self.uglySide.call(
        'ritual_ZN6QChart10mapToValueERK7QPointFP15QAbstractSeries',
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
    Calls Qt's 'QPointF QChart::mapToPosition(const QPointF &value,
    QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#mapToPosition

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
    #  QPointF QChart::mapToPosition(const QPointF &value, QAbstractSeries
    #      *series)
    address = self.uglySide.call(
        'ritual_ZN6QChart13mapToPositionERK7QPointFP15QAbstractSeries',
        self._valueOf(value, 'QPointF'), self._addressOf(series),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRectF)
  def plotAreaChanged(self, plotArea: QRectF) -> None:
    """
    Calls Qt's 'void QChart::plotAreaChanged(const QRectF &plotArea)'.

    Qt's own words: https://doc.qt.io/qt-6/qchart.html#plotAreaChanged

    Parameters
    ----------

    plotArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QChart::plotAreaChanged(const QRectF &plotArea)
    self.uglySide.call(
        'ritual_ZN6QChart15plotAreaChangedERK6QRectF',
        self._valueOf(plotArea),
    )
