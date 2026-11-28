"""
ChartPresenter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/chartpresenter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means ChartPresenter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEasingCurve, QLocale, QMetaObject, QPointF, QRectF
  from ..QtGui import QBrush, QFont, QPen
  from ..QtWidgets import QAbstractGraphicsShapeItem, QGraphicsItem
  from . import AbstractChartLayout, ChartAnimation, ChartAxisElement
  from . import ChartBackground, ChartItem, ChartTitle, QAbstractAxis
  from . import QAbstractSeries, QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartAnimation = WAIT['ChartAnimation']
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QBrush = WAIT['QBrush']
  QEasingCurve = WAIT['QEasingCurve']
  QFont = WAIT['QFont']
  QLocale = WAIT['QLocale']
  QPen = WAIT['QPen']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChartPresenter(QObject):
  """
  The cute side of Qt's ChartPresenter: a plain Python object standing in
  front of one C++ ChartPresenter.

  It is built on the cute 'QObject', as Qt's ChartPresenter is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ChartPresenter that has a ritual and that Python can
  call so far, 67 names in all: 'metaObject', 'tr', 'isFixedGeometry',
  'setFixedGeometry', 'setGeometry', 'geometry', 'updateGeometry',
  'rootItem', 'backgroundElement', 'plotAreaElement', 'titleElement',
  'axisItems', 'chartItems', 'legend', 'setBackgroundBrush',
  'backgroundBrush', 'setBackgroundPen', 'backgroundPen',
  'setBackgroundRoundness', 'backgroundRoundness',
  'setPlotAreaBackgroundBrush', 'plotAreaBackgroundBrush',
  'setPlotAreaBackgroundPen', 'plotAreaBackgroundPen', 'setTitle', 'title',
  'setTitleFont', 'titleFont', 'setTitleBrush', 'titleBrush',
  'setBackgroundVisible', 'isBackgroundVisible',
  'setPlotAreaBackgroundVisible', 'isPlotAreaBackgroundVisible',
  'setBackgroundDropShadowEnabled', 'isBackgroundDropShadowEnabled',
  'setLocalizeNumbers', 'localizeNumbers', 'setLocale', 'locale',
  'setVisible', 'setAnimationOptions', 'animationOptions',
  'setAnimationDuration', 'animationDuration', 'setAnimationEasingCurve',
  'animationEasingCurve', 'startAnimation', 'setState', 'state',
  'statePoint', 'layout', 'chartType', 'chart', 'textBoundingRect',
  'textMargin', 'numberToString', 'updateGLWidget', 'glSetUseWidget',
  'createBackgroundItem', 'createPlotAreaBackgroundItem', 'createTitleItem',
  'handleSeriesAdded', 'handleSeriesRemoved', 'handleAxisAdded',
  'handleAxisRemoved', 'plotAreaChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ChartPresenter::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int ChartPresenter::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'ChartPresenter::~ChartPresenter()': the destructor: Python never
    removes a C++ ChartPresenter.
  - Qt's 'QString ChartPresenter::truncatedText(const QFont &font, const
    QString &text, qreal angle, qreal maxWidth, qreal maxHeight, QRectF
    &boundingRect)': takes a type Python has no way to hand over yet.
  - Qt's 'QString ChartPresenter::numberToString(double value, char f, int
    prec)': takes a single letter as C has it.

  What has no ritual
  ------------------

  2 of the 75 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ChartPresenter is created at the first use, not by
    'ChartPresenter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ChartPresenter.
  - Qt tells when it has removed the C++ ChartPresenter. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ChartPresenter that has no cute function yet,
    'truncatedText', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside ChartPresenter, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """
    The enum 'ChartPresenter::State' of Qt, with the 7 names Qt gives in it.
    """

    ShowState = Kee[int](0)
    ScrollUpState = Kee[int](1)
    ScrollDownState = Kee[int](2)
    ScrollLeftState = Kee[int](3)
    ScrollRightState = Kee[int](4)
    ZoomInState = Kee[int](5)
    ZoomOutState = Kee[int](6)

  class ZValues(CuteNum):
    """
    The enum 'ChartPresenter::ZValues' of Qt, with the 15 names Qt gives in
    it.
    """

    BackgroundZValue = Kee[int](-1)
    PlotAreaZValue = Kee[int](0)
    ShadesZValue = Kee[int](1)
    GridZValue = Kee[int](2)
    AxisZValue = Kee[int](3)
    SeriesZValue = Kee[int](4)
    LineChartZValue = Kee[int](4)
    SplineChartZValue = Kee[int](4)
    BarSeriesZValue = Kee[int](4)
    ScatterSeriesZValue = Kee[int](4)
    PieSeriesZValue = Kee[int](4)
    BoxPlotSeriesZValue = Kee[int](4)
    CandlestickSeriesZValue = Kee[int](4)
    LegendZValue = Kee[int](5)
    TopMostZValue = Kee[int](6)

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
    Calls Qt's 'QString ChartPresenter::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#tr

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
    #  QString ChartPresenter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14ChartPresenter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QFont, str)
  @overload(QFont, str, float)
  def textBoundingRect(font: QFont, text: str, angle: float = 0.0) -> QRectF:
    """
    Calls Qt's 'QRectF ChartPresenter::textBoundingRect(const QFont &font,
    const QString &text, qreal angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#textBoundingRect

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    angle : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF ChartPresenter::textBoundingRect(const QFont &font, const
    #      QString &text, qreal angle)
    address = Rituals.call(
        'ritual_ZN14ChartPresenter16textBoundingRectERK5QFontRK7QStringd',
        CuteMixin._valueOf(font), text, angle,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @staticmethod
  def textMargin() -> float:
    """
    Calls Qt's 'qreal ChartPresenter::textMargin()'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#textMargin
    """
    #  qreal ChartPresenter::textMargin()
    return Rituals.call('ritual_ZN14ChartPresenter10textMarginEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartPresenter'

  #  A C++ ChartPresenter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ChartPresenter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ChartPresenter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ChartPresenter::metaObject() const
    address = self.uglySide.call('ritual_ZNK14ChartPresenter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isFixedGeometry(self) -> bool:
    """
    Calls Qt's 'bool ChartPresenter::isFixedGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#isFixedGeometry
    """
    #  bool ChartPresenter::isFixedGeometry() const
    return self.uglySide.call(
        'ritual_ZNK14ChartPresenter15isFixedGeometryEv',
    )

  def geometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF ChartPresenter::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#geometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF ChartPresenter::geometry() const
    address = self.uglySide.call('ritual_ZNK14ChartPresenter8geometryEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def axisItems(self) -> QList[ChartAxisElement]:
    """
    Calls Qt's 'QList<ChartAxisElement *> ChartPresenter::axisItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#axisItems

    Returns
    -------

    QList[ChartAxisElement]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<ChartAxisElement *> ChartPresenter::axisItems() const
    address = self.uglySide.call('ritual_ZNK14ChartPresenter9axisItemsEv')
    from . import ChartAxisElement
    return QList[ChartAxisElement]._cuteOwning(address)

  def chartItems(self) -> QList[ChartItem]:
    """
    Calls Qt's 'QList<ChartItem *> ChartPresenter::chartItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#chartItems

    Returns
    -------

    QList[ChartItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<ChartItem *> ChartPresenter::chartItems() const
    address = self.uglySide.call('ritual_ZNK14ChartPresenter10chartItemsEv')
    from . import ChartItem
    return QList[ChartItem]._cuteOwning(address)

  def backgroundBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush ChartPresenter::backgroundBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#backgroundBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush ChartPresenter::backgroundBrush() const
    address = self.uglySide.call(
        'ritual_ZNK14ChartPresenter15backgroundBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def backgroundPen(self) -> QPen:
    """
    Calls Qt's 'QPen ChartPresenter::backgroundPen() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#backgroundPen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen ChartPresenter::backgroundPen() const
    address = self.uglySide.call(
        'ritual_ZNK14ChartPresenter13backgroundPenEv',
    )
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def backgroundRoundness(self) -> float:
    """
    Calls Qt's 'qreal ChartPresenter::backgroundRoundness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#backgroundRoundness
    """
    #  qreal ChartPresenter::backgroundRoundness() const
    return self.uglySide.call(
        'ritual_ZNK14ChartPresenter19backgroundRoundnessEv',
    )

  def plotAreaBackgroundBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush ChartPresenter::plotAreaBackgroundBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#plotAreaBackgroundBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush ChartPresenter::plotAreaBackgroundBrush() const
    address = self.uglySide.call(
        'ritual_ZNK14ChartPresenter23plotAreaBackgroundBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def plotAreaBackgroundPen(self) -> QPen:
    """
    Calls Qt's 'QPen ChartPresenter::plotAreaBackgroundPen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#plotAreaBackgroundPen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen ChartPresenter::plotAreaBackgroundPen() const
    address = self.uglySide.call(
        'ritual_ZNK14ChartPresenter21plotAreaBackgroundPenEv',
    )
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString ChartPresenter::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString ChartPresenter::title() const
    return self.uglySide.call('ritual_ZNK14ChartPresenter5titleEv')

  def titleFont(self) -> QFont:
    """
    Calls Qt's 'QFont ChartPresenter::titleFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#titleFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont ChartPresenter::titleFont() const
    address = self.uglySide.call('ritual_ZNK14ChartPresenter9titleFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def titleBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush ChartPresenter::titleBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#titleBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush ChartPresenter::titleBrush() const
    address = self.uglySide.call('ritual_ZNK14ChartPresenter10titleBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def isBackgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool ChartPresenter::isBackgroundVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#isBackgroundVisible
    """
    #  bool ChartPresenter::isBackgroundVisible() const
    return self.uglySide.call(
        'ritual_ZNK14ChartPresenter19isBackgroundVisibleEv',
    )

  def isPlotAreaBackgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool ChartPresenter::isPlotAreaBackgroundVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#isPlotAreaBackgroundVisible
    """
    #  bool ChartPresenter::isPlotAreaBackgroundVisible() const
    return self.uglySide.call(
        'ritual_ZNK14ChartPresenter27isPlotAreaBackgroundVisibleEv',
    )

  def isBackgroundDropShadowEnabled(self) -> bool:
    """
    Calls Qt's 'bool ChartPresenter::isBackgroundDropShadowEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#isBackgroundDropShadowEnabled
    """
    #  bool ChartPresenter::isBackgroundDropShadowEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14ChartPresenter29isBackgroundDropShadowEnabledEv',
    )

  def localizeNumbers(self) -> bool:
    """
    Calls Qt's 'bool ChartPresenter::localizeNumbers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#localizeNumbers
    """
    #  bool ChartPresenter::localizeNumbers() const
    return self.uglySide.call(
        'ritual_ZNK14ChartPresenter15localizeNumbersEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'const QLocale &ChartPresenter::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  const QLocale &ChartPresenter::locale() const
    address = self.uglySide.call('ritual_ZNK14ChartPresenter6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def animationOptions(self) -> QChart.AnimationOptions:
    """
    Calls Qt's 'QChart::AnimationOptions ChartPresenter::animationOptions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#animationOptions

    Returns
    -------

    QChart.AnimationOptions
      The value standing for the combination Qt gave back.
    """
    #  QChart::AnimationOptions ChartPresenter::animationOptions() const
    return QChart.AnimationOptions(self.uglySide.call(
        'ritual_ZNK14ChartPresenter16animationOptionsEv',
    ))

  def animationDuration(self) -> int:
    """
    Calls Qt's 'int ChartPresenter::animationDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#animationDuration
    """
    #  int ChartPresenter::animationDuration() const
    return self.uglySide.call(
        'ritual_ZNK14ChartPresenter17animationDurationEv',
    )

  def animationEasingCurve(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve ChartPresenter::animationEasingCurve() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#animationEasingCurve

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve ChartPresenter::animationEasingCurve() const
    address = self.uglySide.call(
        'ritual_ZNK14ChartPresenter20animationEasingCurveEv',
    )
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def state(self) -> State:
    """
    Calls Qt's 'State ChartPresenter::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State ChartPresenter::state() const
    return ChartPresenter.State(self.uglySide.call(
        'ritual_ZNK14ChartPresenter5stateEv',
    ))

  def statePoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF ChartPresenter::statePoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#statePoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF ChartPresenter::statePoint() const
    address = self.uglySide.call('ritual_ZNK14ChartPresenter10statePointEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def chartType(self) -> QChart.ChartType:
    """
    Calls Qt's 'QChart::ChartType ChartPresenter::chartType() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#chartType

    Returns
    -------

    QChart.ChartType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QChart.ChartType(number)'
      gives.
    """
    #  QChart::ChartType ChartPresenter::chartType() const
    return QChart.ChartType(self.uglySide.call(
        'ritual_ZNK14ChartPresenter9chartTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setFixedGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void ChartPresenter::setFixedGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setFixedGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void ChartPresenter::setFixedGeometry(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter16setFixedGeometryERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void ChartPresenter::setGeometry(QRectF rect)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void ChartPresenter::setGeometry(QRectF rect)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter11setGeometryE6QRectF',
        self._valueOf(rect),
    )

  @overload(QBrush)
  def setBackgroundBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void ChartPresenter::setBackgroundBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setBackgroundBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void ChartPresenter::setBackgroundBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter18setBackgroundBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QPen)
  def setBackgroundPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void ChartPresenter::setBackgroundPen(const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setBackgroundPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void ChartPresenter::setBackgroundPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter16setBackgroundPenERK4QPen',
        self._valueOf(pen),
    )

  @overload(float)
  def setBackgroundRoundness(self, diameter: float) -> None:
    """
    Calls Qt's 'void ChartPresenter::setBackgroundRoundness(qreal diameter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setBackgroundRoundness

    Parameters
    ----------

    diameter : float
      Passed on as it is.
    """
    #  void ChartPresenter::setBackgroundRoundness(qreal diameter)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter22setBackgroundRoundnessEd', diameter,
    )

  @overload(QBrush)
  def setPlotAreaBackgroundBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void ChartPresenter::setPlotAreaBackgroundBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setPlotAreaBackgroundBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void ChartPresenter::setPlotAreaBackgroundBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter26setPlotAreaBackgroundBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QPen)
  def setPlotAreaBackgroundPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void ChartPresenter::setPlotAreaBackgroundPen(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setPlotAreaBackgroundPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void ChartPresenter::setPlotAreaBackgroundPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter24setPlotAreaBackgroundPenERK4QPen',
        self._valueOf(pen),
    )

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void ChartPresenter::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void ChartPresenter::setTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter8setTitleERK7QString', title,
    )

  @overload(QFont)
  def setTitleFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void ChartPresenter::setTitleFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#setTitleFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void ChartPresenter::setTitleFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter12setTitleFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QBrush)
  def setTitleBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void ChartPresenter::setTitleBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#setTitleBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void ChartPresenter::setTitleBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter13setTitleBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(bool)
  def setBackgroundVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartPresenter::setBackgroundVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setBackgroundVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartPresenter::setBackgroundVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter20setBackgroundVisibleEb', visible,
    )

  @overload(bool)
  def setPlotAreaBackgroundVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartPresenter::setPlotAreaBackgroundVisible(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setPlotAreaBackgroundVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartPresenter::setPlotAreaBackgroundVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter28setPlotAreaBackgroundVisibleEb', visible,
    )

  @overload(bool)
  def setBackgroundDropShadowEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void ChartPresenter::setBackgroundDropShadowEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setBackgroundDropShadowEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void ChartPresenter::setBackgroundDropShadowEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter30setBackgroundDropShadowEnabledEb',
        enabled,
    )

  @overload(bool)
  def setLocalizeNumbers(self, localize: bool) -> None:
    """
    Calls Qt's 'void ChartPresenter::setLocalizeNumbers(bool localize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setLocalizeNumbers

    Parameters
    ----------

    localize : bool
      Passed on as it is.
    """
    #  void ChartPresenter::setLocalizeNumbers(bool localize)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter18setLocalizeNumbersEb', localize,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void ChartPresenter::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void ChartPresenter::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartPresenter::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartPresenter::setVisible(bool visible)
    self.uglySide.call('ritual_ZN14ChartPresenter10setVisibleEb', visible)

  @overload(QChart.AnimationOptions)
  def setAnimationOptions(self, options: QChart.AnimationOptions) -> None:
    """
    Calls Qt's 'void
    ChartPresenter::setAnimationOptions(QChart::AnimationOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setAnimationOptions

    Parameters
    ----------

    options : QChart.AnimationOptions
      Passed on as its number.
    """
    #  void ChartPresenter::setAnimationOptions(QChart::AnimationOptions
    #      options)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter19setAnimationOptionsE6QFlagsIN6QChart15A'
        'nimationOptionEE',
        options.value,
    )

  @overload(int)
  def setAnimationDuration(self, msecs: int) -> None:
    """
    Calls Qt's 'void ChartPresenter::setAnimationDuration(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setAnimationDuration

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void ChartPresenter::setAnimationDuration(int msecs)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter20setAnimationDurationEi', msecs,
    )

  @overload(QEasingCurve)
  def setAnimationEasingCurve(self, curve: QEasingCurve) -> None:
    """
    Calls Qt's 'void ChartPresenter::setAnimationEasingCurve(const
    QEasingCurve &curve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#setAnimationEasingCurve

    Parameters
    ----------

    curve : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void ChartPresenter::setAnimationEasingCurve(const QEasingCurve
    #      &curve)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter23setAnimationEasingCurveERK12QEasingCurv'
        'e',
        self._valueOf(curve),
    )

  @overload(State, QPointF)
  def setState(self, state: State, point: QPointF) -> None:
    """
    Calls Qt's 'void ChartPresenter::setState(State state, QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#setState

    Parameters
    ----------

    state : State
      Passed on as its number.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void ChartPresenter::setState(State state, QPointF point)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter8setStateENS_5StateE7QPointF',
        state.value, self._valueOf(point, 'QPointF'),
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

  @overload(QChart, QChart.ChartType)
  @overload(NoneType, QChart.ChartType)
  def __init__(
      self,
      chart: Optional[QChart],
      type: QChart.ChartType,
  ) -> None:
    """
    Notes what was given, for Qt's 'ChartPresenter::ChartPresenter(QChart
    *chart, QChart::ChartType type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#ChartPresenter

    Parameters
    ----------

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QChart.ChartType
      Passed on as its number.
    """
    #  ChartPresenter::ChartPresenter(QChart *chart, QChart::ChartType type)
    self._noteCreation(ChartPresenter, lambda: Rituals.call(
        'ritual_ZN14ChartPresenterC1EP6QChartNS0_9ChartTypeE',
        self._addressOf(chart), type.value,
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

  @overload(QRectF)
  def updateGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void ChartPresenter::updateGeometry(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#updateGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void ChartPresenter::updateGeometry(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter14updateGeometryERK6QRectF',
        self._valueOf(rect),
    )

  def rootItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *ChartPresenter::rootItem()'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#rootItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *ChartPresenter::rootItem()
    address = self.uglySide.call('ritual_ZN14ChartPresenter8rootItemEv')
    from ..QtWidgets import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def backgroundElement(self) -> Optional[ChartBackground]:
    """
    Calls Qt's 'ChartBackground *ChartPresenter::backgroundElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#backgroundElement

    Returns
    -------

    Optional[ChartBackground]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartBackground *ChartPresenter::backgroundElement()
    address = self.uglySide.call(
        'ritual_ZN14ChartPresenter17backgroundElementEv',
    )
    from . import ChartBackground
    return ChartBackground._cuteAt(address)

  def plotAreaElement(self) -> Optional[QAbstractGraphicsShapeItem]:
    """
    Calls Qt's 'QAbstractGraphicsShapeItem
    *ChartPresenter::plotAreaElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#plotAreaElement

    Returns
    -------

    Optional[QAbstractGraphicsShapeItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractGraphicsShapeItem *ChartPresenter::plotAreaElement()
    address = self.uglySide.call(
        'ritual_ZN14ChartPresenter15plotAreaElementEv',
    )
    from ..QtWidgets import QAbstractGraphicsShapeItem
    return QAbstractGraphicsShapeItem._cuteAt(address)

  def titleElement(self) -> Optional[ChartTitle]:
    """
    Calls Qt's 'ChartTitle *ChartPresenter::titleElement()'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#titleElement

    Returns
    -------

    Optional[ChartTitle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartTitle *ChartPresenter::titleElement()
    address = self.uglySide.call('ritual_ZN14ChartPresenter12titleElementEv')
    from . import ChartTitle
    return ChartTitle._cuteAt(address)

  def legend(self) -> Optional[QLegend]:
    """
    Calls Qt's 'QLegend *ChartPresenter::legend()'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#legend

    Returns
    -------

    Optional[QLegend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLegend *ChartPresenter::legend()
    address = self.uglySide.call('ritual_ZN14ChartPresenter6legendEv')
    from . import QLegend
    return QLegend._cuteAt(address)

  @overload(ChartAnimation)
  @overload(NoneType)
  def startAnimation(self, animation: Optional[ChartAnimation]) -> None:
    """
    Calls Qt's 'void ChartPresenter::startAnimation(ChartAnimation
    *animation)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#startAnimation

    Parameters
    ----------

    animation : Optional[ChartAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartPresenter::startAnimation(ChartAnimation *animation)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter14startAnimationEP14ChartAnimation',
        self._addressOf(animation),
    )

  def layout(self) -> Optional[AbstractChartLayout]:
    """
    Calls Qt's 'AbstractChartLayout *ChartPresenter::layout()'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#layout

    Returns
    -------

    Optional[AbstractChartLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractChartLayout *ChartPresenter::layout()
    address = self.uglySide.call('ritual_ZN14ChartPresenter6layoutEv')
    from . import AbstractChartLayout
    return AbstractChartLayout._cuteAt(address)

  def chart(self) -> Optional[QChart]:
    """
    Calls Qt's 'QChart *ChartPresenter::chart()'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#chart

    Returns
    -------

    Optional[QChart]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChart *ChartPresenter::chart()
    address = self.uglySide.call('ritual_ZN14ChartPresenter5chartEv')
    return QChart._cuteAt(address)

  @overload(int)
  def numberToString(self, value: int) -> str:
    """
    Calls Qt's 'QString ChartPresenter::numberToString(int value)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#numberToString

    Parameters
    ----------

    value : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString ChartPresenter::numberToString(int value)
    return self.uglySide.call(
        'ritual_ZN14ChartPresenter14numberToStringEi', value,
    )

  def updateGLWidget(self) -> None:
    """
    Calls Qt's 'void ChartPresenter::updateGLWidget()'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#updateGLWidget
    """
    #  void ChartPresenter::updateGLWidget()
    self.uglySide.call('ritual_ZN14ChartPresenter14updateGLWidgetEv')

  @overload(bool)
  def glSetUseWidget(self, enable: bool) -> None:
    """
    Calls Qt's 'void ChartPresenter::glSetUseWidget(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/chartpresenter.html#glSetUseWidget

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void ChartPresenter::glSetUseWidget(bool enable)
    self.uglySide.call('ritual_ZN14ChartPresenter14glSetUseWidgetEb', enable)

  def createBackgroundItem(self) -> None:
    """
    Calls Qt's 'void ChartPresenter::createBackgroundItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#createBackgroundItem
    """
    #  void ChartPresenter::createBackgroundItem()
    self.uglySide.call('ritual_ZN14ChartPresenter20createBackgroundItemEv')

  def createPlotAreaBackgroundItem(self) -> None:
    """
    Calls Qt's 'void ChartPresenter::createPlotAreaBackgroundItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#createPlotAreaBackgroundItem
    """
    #  void ChartPresenter::createPlotAreaBackgroundItem()
    self.uglySide.call(
        'ritual_ZN14ChartPresenter28createPlotAreaBackgroundItemEv',
    )

  def createTitleItem(self) -> None:
    """
    Calls Qt's 'void ChartPresenter::createTitleItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#createTitleItem
    """
    #  void ChartPresenter::createTitleItem()
    self.uglySide.call('ritual_ZN14ChartPresenter15createTitleItemEv')

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesAdded(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void ChartPresenter::handleSeriesAdded(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#handleSeriesAdded

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartPresenter::handleSeriesAdded(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter17handleSeriesAddedEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesRemoved(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void ChartPresenter::handleSeriesRemoved(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#handleSeriesRemoved

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartPresenter::handleSeriesRemoved(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter19handleSeriesRemovedEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def handleAxisAdded(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void ChartPresenter::handleAxisAdded(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#handleAxisAdded

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartPresenter::handleAxisAdded(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter15handleAxisAddedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def handleAxisRemoved(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void ChartPresenter::handleAxisRemoved(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#handleAxisRemoved

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartPresenter::handleAxisRemoved(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter17handleAxisRemovedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QRectF)
  def plotAreaChanged(self, plotArea: QRectF) -> None:
    """
    Calls Qt's 'void ChartPresenter::plotAreaChanged(const QRectF
    &plotArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartpresenter.html#plotAreaChanged

    Parameters
    ----------

    plotArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void ChartPresenter::plotAreaChanged(const QRectF &plotArea)
    self.uglySide.call(
        'ritual_ZN14ChartPresenter15plotAreaChangedERK6QRectF',
        self._valueOf(plotArea),
    )

  @staticmethod
  def truncatedText(*__, **_) -> Never:
    """
    Qt's 'QString ChartPresenter::truncatedText(const QFont &font, const
    QString &text, qreal angle, qreal maxWidth, qreal maxHeight, QRectF
    &boundingRect)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ChartPresenter.truncatedText' has no cute function yet. Qt's "
        "'QString ChartPresenter::truncatedText(const QFont &font, const "
        "QString &text, qreal angle, qreal maxWidth, qreal maxHeight, "
        "QRectF &boundingRect)': takes a type Python has no way to hand "
        "over yet.")
