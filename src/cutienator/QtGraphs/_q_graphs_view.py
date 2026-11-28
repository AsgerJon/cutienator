"""
QGraphsView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qgraphsview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGraphsView to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtGui import QPointingDevice
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QColor, QEventPoint, QHoverEvent, QWheelEvent
  from ..QtQml import QQmlComponent
  from ..QtQuick import QSGNode
  from . import QAbstractAxis, QAbstractSeries, QCustomSeries, QGraphsTheme
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtGraphs:QAbstractAxis']
  QAbstractSeries = WAIT['QtGraphs:QAbstractSeries']
  QColor = WAIT['QColor']
  QCustomSeries = WAIT['QCustomSeries']
  QEventPoint = WAIT['QEventPoint']
  QGraphsTheme = WAIT['QGraphsTheme']
  QHoverEvent = WAIT['QHoverEvent']
  QPointF = WAIT['QPointF']
  QQmlComponent = WAIT['QQmlComponent']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphsView(QQuickItem):
  """
  The cute side of Qt's QGraphsView: a plain Python object standing in front
  of one C++ QGraphsView.

  It is built on the cute 'QQuickItem', as Qt's QGraphsView is built on Qt's
  QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphsView that has a ritual and that Python can
  call so far, 118 names in all: 'metaObject', 'tr', 'addSeries',
  'insertSeries', 'removeSeries', 'hasSeries', 'getSeriesList',
  'getDataPointCoordinates', 'theme', 'setTheme', 'marginTop',
  'setMarginTop', 'marginBottom', 'setMarginBottom', 'marginLeft',
  'setMarginLeft', 'marginRight', 'setMarginRight', 'clipPlotArea',
  'setClipPlotArea', 'plotArea', 'updatePlotArea', 'updateAxisAreas',
  'addAxis', 'removeAxis', 'graphSeriesCount', 'setGraphSeriesCount',
  'createBarsRenderer', 'createAxisRenderer', 'createPointRenderer',
  'createPieRenderer', 'createAreaRenderer', 'createCustomRenderer',
  'createCanvasPainter', 'removeCanvasPainter', 'axisXSmoothing',
  'setAxisXSmoothing', 'axisYSmoothing', 'setAxisYSmoothing',
  'gridSmoothing', 'setGridSmoothing', 'isShadowVisible', 'setShadowVisible',
  'shadowColor', 'setShadowColor', 'shadowBarWidth', 'setShadowBarWidth',
  'shadowXOffset', 'setShadowXOffset', 'shadowYOffset', 'setShadowYOffset',
  'shadowSmoothing', 'setShadowSmoothing', 'axisX', 'setAxisX', 'axisY',
  'setAxisY', 'orientation', 'setOrientation', 'zoomStyle', 'setZoomStyle',
  'panStyle', 'setPanStyle', 'zoomAreaEnabled', 'setZoomAreaEnabled',
  'zoomAreaDelegate', 'setZoomAreaDelegate', 'zoomSensitivity',
  'setZoomSensitivity', 'mapX', 'mapY', 'useCanvasPainter',
  'setUseCanvasPainter', 'dynamicLabelMargins', 'setDynamicLabelMargins',
  'handleHoverEnter', 'handleHoverExit', 'handleHover',
  'updateComponentSizes', 'componentComplete', 'geometryChange',
  'hoverMoveEvent', 'wheelEvent', 'updatePaintNode', 'updatePolish',
  'themeChanged', 'marginTopChanged', 'marginBottomChanged',
  'marginLeftChanged', 'marginRightChanged', 'clipPlotAreaChanged',
  'plotAreaChanged', 'hoverEnter', 'hoverExit', 'hover',
  'axisXSmoothingChanged', 'axisYSmoothingChanged', 'gridSmoothingChanged',
  'shadowVisibleChanged', 'shadowColorChanged', 'shadowBarWidthChanged',
  'shadowXOffsetChanged', 'shadowYOffsetChanged', 'shadowSmoothingChanged',
  'axisXChanged', 'axisYChanged', 'orientationChanged', 'zoomStyleChanged',
  'panStyleChanged', 'zoomAreaEnabledChanged', 'zoomAreaDelegateChanged',
  'zoomSensitivityChanged', 'useCanvasPainterChanged',
  'dynamicLabelMarginsChanged', 'polishAndUpdate', 'getSeriesRendererIndex',
  'onPinchScaleChanged', 'onPinchGrabChanged'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphsView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QGraphsView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphsView::~QGraphsView()': the destructor: Python never removes
    a C++ QGraphsView.
  - Qt's 'QQmlListProperty<QObject> QGraphsView::seriesList()': gives a type
    Python has no way to take yet.
  - Qt's 'void QGraphsView::appendSeriesFunc(QQmlListProperty<QObject> *list,
    QObject *series)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'qsizetype QGraphsView::countSeriesFunc(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QGraphsView::atSeriesFunc(QQmlListProperty<QObject> *list,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void QGraphsView::clearSeriesFunc(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'CustomRenderer *QGraphsView::customRenderer() const': gives
    'CustomRenderer', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 131 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QGraphsView is created at the first use, not by
    'QGraphsView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphsView.
  - Qt tells when it has removed the C++ QGraphsView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QGraphsView that has no cute function yet,
    'appendSeriesFunc', 'atSeriesFunc', 'clearSeriesFunc', 'countSeriesFunc',
    'customRenderer', 'seriesList', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGraphsView, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PanStyle(CuteNum, scoped=True):
    """
    The enum 'QGraphsView::PanStyle' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NULL = Kee[int](0)
    Drag = Kee[int](1)

  class ZoomStyle(CuteNum, scoped=True):
    """
    The enum 'QGraphsView::ZoomStyle' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NULL = Kee[int](0)
    Center = Kee[int](1)

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
    Calls Qt's 'QString QGraphsView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#tr

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
    #  QString QGraphsView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QGraphsView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphsView'

  #  A C++ QGraphsView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphsView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphsView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphsView::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QGraphsView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def getSeriesList(self) -> QList[QObject]:
    """
    Calls Qt's 'QList<QObject *> QGraphsView::getSeriesList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#getSeriesList

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QObject *> QGraphsView::getSeriesList() const
    address = self.uglySide.call('ritual_ZNK11QGraphsView13getSeriesListEv')
    return QList[QObject]._cuteOwning(address)

  def theme(self) -> Optional[QGraphsTheme]:
    """
    Calls Qt's 'QGraphsTheme *QGraphsView::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#theme

    Returns
    -------

    Optional[QGraphsTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphsTheme *QGraphsView::theme() const
    address = self.uglySide.call('ritual_ZNK11QGraphsView5themeEv')
    from . import QGraphsTheme
    return QGraphsTheme._cuteAt(address)

  def marginTop(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::marginTop() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#marginTop
    """
    #  qreal QGraphsView::marginTop() const
    return self.uglySide.call('ritual_ZNK11QGraphsView9marginTopEv')

  def marginBottom(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::marginBottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#marginBottom
    """
    #  qreal QGraphsView::marginBottom() const
    return self.uglySide.call('ritual_ZNK11QGraphsView12marginBottomEv')

  def marginLeft(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::marginLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#marginLeft
    """
    #  qreal QGraphsView::marginLeft() const
    return self.uglySide.call('ritual_ZNK11QGraphsView10marginLeftEv')

  def marginRight(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::marginRight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#marginRight
    """
    #  qreal QGraphsView::marginRight() const
    return self.uglySide.call('ritual_ZNK11QGraphsView11marginRightEv')

  def clipPlotArea(self) -> bool:
    """
    Calls Qt's 'bool QGraphsView::clipPlotArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#clipPlotArea
    """
    #  bool QGraphsView::clipPlotArea() const
    return self.uglySide.call('ritual_ZNK11QGraphsView12clipPlotAreaEv')

  def plotArea(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphsView::plotArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#plotArea

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphsView::plotArea() const
    address = self.uglySide.call('ritual_ZNK11QGraphsView8plotAreaEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def graphSeriesCount(self) -> int:
    """
    Calls Qt's 'qsizetype QGraphsView::graphSeriesCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#graphSeriesCount
    """
    #  qsizetype QGraphsView::graphSeriesCount() const
    return self.uglySide.call('ritual_ZNK11QGraphsView16graphSeriesCountEv')

  def axisXSmoothing(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::axisXSmoothing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#axisXSmoothing
    """
    #  qreal QGraphsView::axisXSmoothing() const
    return self.uglySide.call('ritual_ZNK11QGraphsView14axisXSmoothingEv')

  def axisYSmoothing(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::axisYSmoothing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#axisYSmoothing
    """
    #  qreal QGraphsView::axisYSmoothing() const
    return self.uglySide.call('ritual_ZNK11QGraphsView14axisYSmoothingEv')

  def gridSmoothing(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::gridSmoothing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#gridSmoothing
    """
    #  qreal QGraphsView::gridSmoothing() const
    return self.uglySide.call('ritual_ZNK11QGraphsView13gridSmoothingEv')

  def isShadowVisible(self) -> bool:
    """
    Calls Qt's 'bool QGraphsView::isShadowVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#isShadowVisible
    """
    #  bool QGraphsView::isShadowVisible() const
    return self.uglySide.call('ritual_ZNK11QGraphsView15isShadowVisibleEv')

  def shadowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphsView::shadowColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#shadowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphsView::shadowColor() const
    address = self.uglySide.call('ritual_ZNK11QGraphsView11shadowColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def shadowBarWidth(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::shadowBarWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#shadowBarWidth
    """
    #  qreal QGraphsView::shadowBarWidth() const
    return self.uglySide.call('ritual_ZNK11QGraphsView14shadowBarWidthEv')

  def shadowXOffset(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::shadowXOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#shadowXOffset
    """
    #  qreal QGraphsView::shadowXOffset() const
    return self.uglySide.call('ritual_ZNK11QGraphsView13shadowXOffsetEv')

  def shadowYOffset(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::shadowYOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#shadowYOffset
    """
    #  qreal QGraphsView::shadowYOffset() const
    return self.uglySide.call('ritual_ZNK11QGraphsView13shadowYOffsetEv')

  def shadowSmoothing(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::shadowSmoothing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#shadowSmoothing
    """
    #  qreal QGraphsView::shadowSmoothing() const
    return self.uglySide.call('ritual_ZNK11QGraphsView15shadowSmoothingEv')

  def axisX(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *QGraphsView::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *QGraphsView::axisX() const
    address = self.uglySide.call('ritual_ZNK11QGraphsView5axisXEv')
    from . import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *QGraphsView::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *QGraphsView::axisY() const
    address = self.uglySide.call('ritual_ZNK11QGraphsView5axisYEv')
    from . import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QGraphsView::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QGraphsView::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK11QGraphsView11orientationEv',
    ))

  def zoomStyle(self) -> ZoomStyle:
    """
    Calls Qt's 'ZoomStyle QGraphsView::zoomStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#zoomStyle

    Returns
    -------

    ZoomStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ZoomStyle(number)' gives.
    """
    #  ZoomStyle QGraphsView::zoomStyle() const
    return QGraphsView.ZoomStyle(self.uglySide.call(
        'ritual_ZNK11QGraphsView9zoomStyleEv',
    ))

  def panStyle(self) -> PanStyle:
    """
    Calls Qt's 'PanStyle QGraphsView::panStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#panStyle

    Returns
    -------

    PanStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PanStyle(number)' gives.
    """
    #  PanStyle QGraphsView::panStyle() const
    return QGraphsView.PanStyle(self.uglySide.call(
        'ritual_ZNK11QGraphsView8panStyleEv',
    ))

  def zoomAreaEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGraphsView::zoomAreaEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#zoomAreaEnabled
    """
    #  bool QGraphsView::zoomAreaEnabled() const
    return self.uglySide.call('ritual_ZNK11QGraphsView15zoomAreaEnabledEv')

  def zoomAreaDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QGraphsView::zoomAreaDelegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#zoomAreaDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QGraphsView::zoomAreaDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK11QGraphsView16zoomAreaDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def zoomSensitivity(self) -> float:
    """
    Calls Qt's 'qreal QGraphsView::zoomSensitivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#zoomSensitivity
    """
    #  qreal QGraphsView::zoomSensitivity() const
    return self.uglySide.call('ritual_ZNK11QGraphsView15zoomSensitivityEv')

  def useCanvasPainter(self) -> bool:
    """
    Calls Qt's 'bool QGraphsView::useCanvasPainter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#useCanvasPainter
    """
    #  bool QGraphsView::useCanvasPainter() const
    return self.uglySide.call('ritual_ZNK11QGraphsView16useCanvasPainterEv')

  def dynamicLabelMargins(self) -> bool:
    """
    Calls Qt's 'bool QGraphsView::dynamicLabelMargins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#dynamicLabelMargins
    """
    #  bool QGraphsView::dynamicLabelMargins() const
    return self.uglySide.call(
        'ritual_ZNK11QGraphsView19dynamicLabelMarginsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphsTheme)
  @overload(NoneType)
  def setTheme(self, newTheme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void QGraphsView::setTheme(QGraphsTheme *newTheme)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setTheme

    Parameters
    ----------

    newTheme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::setTheme(QGraphsTheme *newTheme)
    self.uglySide.call(
        'ritual_ZN11QGraphsView8setThemeEP12QGraphsTheme',
        self._addressOf(newTheme),
    )

  @overload(float)
  def setMarginTop(self, newMarginTop: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setMarginTop(qreal newMarginTop)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setMarginTop

    Parameters
    ----------

    newMarginTop : float
      Passed on as it is.
    """
    #  void QGraphsView::setMarginTop(qreal newMarginTop)
    self.uglySide.call(
        'ritual_ZN11QGraphsView12setMarginTopEd', newMarginTop,
    )

  @overload(float)
  def setMarginBottom(self, newMarginBottom: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setMarginBottom(qreal newMarginBottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setMarginBottom

    Parameters
    ----------

    newMarginBottom : float
      Passed on as it is.
    """
    #  void QGraphsView::setMarginBottom(qreal newMarginBottom)
    self.uglySide.call(
        'ritual_ZN11QGraphsView15setMarginBottomEd', newMarginBottom,
    )

  @overload(float)
  def setMarginLeft(self, newMarginLeft: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setMarginLeft(qreal newMarginLeft)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setMarginLeft

    Parameters
    ----------

    newMarginLeft : float
      Passed on as it is.
    """
    #  void QGraphsView::setMarginLeft(qreal newMarginLeft)
    self.uglySide.call(
        'ritual_ZN11QGraphsView13setMarginLeftEd', newMarginLeft,
    )

  @overload(float)
  def setMarginRight(self, newMarginRight: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setMarginRight(qreal newMarginRight)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setMarginRight

    Parameters
    ----------

    newMarginRight : float
      Passed on as it is.
    """
    #  void QGraphsView::setMarginRight(qreal newMarginRight)
    self.uglySide.call(
        'ritual_ZN11QGraphsView14setMarginRightEd', newMarginRight,
    )

  @overload(bool)
  def setClipPlotArea(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphsView::setClipPlotArea(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setClipPlotArea

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphsView::setClipPlotArea(bool enabled)
    self.uglySide.call('ritual_ZN11QGraphsView15setClipPlotAreaEb', enabled)

  @overload(int)
  def setGraphSeriesCount(self, count: int) -> None:
    """
    Calls Qt's 'void QGraphsView::setGraphSeriesCount(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#setGraphSeriesCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QGraphsView::setGraphSeriesCount(qsizetype count)
    self.uglySide.call(
        'ritual_ZN11QGraphsView19setGraphSeriesCountEx', count,
    )

  @overload(float)
  def setAxisXSmoothing(self, smoothing: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setAxisXSmoothing(qreal smoothing)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setAxisXSmoothing

    Parameters
    ----------

    smoothing : float
      Passed on as it is.
    """
    #  void QGraphsView::setAxisXSmoothing(qreal smoothing)
    self.uglySide.call(
        'ritual_ZN11QGraphsView17setAxisXSmoothingEd', smoothing,
    )

  @overload(float)
  def setAxisYSmoothing(self, smoothing: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setAxisYSmoothing(qreal smoothing)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setAxisYSmoothing

    Parameters
    ----------

    smoothing : float
      Passed on as it is.
    """
    #  void QGraphsView::setAxisYSmoothing(qreal smoothing)
    self.uglySide.call(
        'ritual_ZN11QGraphsView17setAxisYSmoothingEd', smoothing,
    )

  @overload(float)
  def setGridSmoothing(self, smoothing: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setGridSmoothing(qreal smoothing)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setGridSmoothing

    Parameters
    ----------

    smoothing : float
      Passed on as it is.
    """
    #  void QGraphsView::setGridSmoothing(qreal smoothing)
    self.uglySide.call(
        'ritual_ZN11QGraphsView16setGridSmoothingEd', smoothing,
    )

  @overload(bool)
  def setShadowVisible(self, newShadowVisibility: bool) -> None:
    """
    Calls Qt's 'void QGraphsView::setShadowVisible(bool
    newShadowVisibility)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setShadowVisible

    Parameters
    ----------

    newShadowVisibility : bool
      Passed on as it is.
    """
    #  void QGraphsView::setShadowVisible(bool newShadowVisibility)
    self.uglySide.call(
        'ritual_ZN11QGraphsView16setShadowVisibleEb', newShadowVisibility,
    )

  @overload(QColor)
  def setShadowColor(self, newShadowColor: QColor) -> None:
    """
    Calls Qt's 'void QGraphsView::setShadowColor(QColor newShadowColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setShadowColor

    Parameters
    ----------

    newShadowColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphsView::setShadowColor(QColor newShadowColor)
    self.uglySide.call(
        'ritual_ZN11QGraphsView14setShadowColorE6QColor',
        self._valueOf(newShadowColor),
    )

  @overload(float)
  def setShadowBarWidth(self, newShadowBarWidth: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setShadowBarWidth(qreal
    newShadowBarWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setShadowBarWidth

    Parameters
    ----------

    newShadowBarWidth : float
      Passed on as it is.
    """
    #  void QGraphsView::setShadowBarWidth(qreal newShadowBarWidth)
    self.uglySide.call(
        'ritual_ZN11QGraphsView17setShadowBarWidthEd', newShadowBarWidth,
    )

  @overload(float)
  def setShadowXOffset(self, newShadowXOffset: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setShadowXOffset(qreal newShadowXOffset)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setShadowXOffset

    Parameters
    ----------

    newShadowXOffset : float
      Passed on as it is.
    """
    #  void QGraphsView::setShadowXOffset(qreal newShadowXOffset)
    self.uglySide.call(
        'ritual_ZN11QGraphsView16setShadowXOffsetEd', newShadowXOffset,
    )

  @overload(float)
  def setShadowYOffset(self, newShadowYOffset: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setShadowYOffset(qreal newShadowYOffset)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setShadowYOffset

    Parameters
    ----------

    newShadowYOffset : float
      Passed on as it is.
    """
    #  void QGraphsView::setShadowYOffset(qreal newShadowYOffset)
    self.uglySide.call(
        'ritual_ZN11QGraphsView16setShadowYOffsetEd', newShadowYOffset,
    )

  @overload(float)
  def setShadowSmoothing(self, smoothing: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setShadowSmoothing(qreal smoothing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#setShadowSmoothing

    Parameters
    ----------

    smoothing : float
      Passed on as it is.
    """
    #  void QGraphsView::setShadowSmoothing(qreal smoothing)
    self.uglySide.call(
        'ritual_ZN11QGraphsView18setShadowSmoothingEd', smoothing,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void QGraphsView::setAxisX(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::setAxisX(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN11QGraphsView8setAxisXEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void QGraphsView::setAxisY(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::setAxisY(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN11QGraphsView8setAxisYEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(Qt.Orientation)
  def setOrientation(self, newOrientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QGraphsView::setOrientation(Qt::Orientation
    newOrientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setOrientation

    Parameters
    ----------

    newOrientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphsView::setOrientation(Qt::Orientation newOrientation)
    self.uglySide.call(
        'ritual_ZN11QGraphsView14setOrientationEN2Qt11OrientationE',
        newOrientation.value,
    )

  @overload(ZoomStyle)
  def setZoomStyle(self, newZoomStyle: ZoomStyle) -> None:
    """
    Calls Qt's 'void QGraphsView::setZoomStyle(ZoomStyle newZoomStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setZoomStyle

    Parameters
    ----------

    newZoomStyle : ZoomStyle
      Passed on as its number.
    """
    #  void QGraphsView::setZoomStyle(ZoomStyle newZoomStyle)
    self.uglySide.call(
        'ritual_ZN11QGraphsView12setZoomStyleENS_9ZoomStyleE',
        newZoomStyle.value,
    )

  @overload(PanStyle)
  def setPanStyle(self, newPanStyle: PanStyle) -> None:
    """
    Calls Qt's 'void QGraphsView::setPanStyle(PanStyle newPanStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#setPanStyle

    Parameters
    ----------

    newPanStyle : PanStyle
      Passed on as its number.
    """
    #  void QGraphsView::setPanStyle(PanStyle newPanStyle)
    self.uglySide.call(
        'ritual_ZN11QGraphsView11setPanStyleENS_8PanStyleE',
        newPanStyle.value,
    )

  @overload(bool)
  def setZoomAreaEnabled(self, newZoomAreaEnabled: bool) -> None:
    """
    Calls Qt's 'void QGraphsView::setZoomAreaEnabled(bool
    newZoomAreaEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#setZoomAreaEnabled

    Parameters
    ----------

    newZoomAreaEnabled : bool
      Passed on as it is.
    """
    #  void QGraphsView::setZoomAreaEnabled(bool newZoomAreaEnabled)
    self.uglySide.call(
        'ritual_ZN11QGraphsView18setZoomAreaEnabledEb', newZoomAreaEnabled,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setZoomAreaDelegate(
      self,
      newZoomAreaDelegate: Optional[QQmlComponent],
  ) -> None:
    """
    Calls Qt's 'void QGraphsView::setZoomAreaDelegate(QQmlComponent
    *newZoomAreaDelegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#setZoomAreaDelegate

    Parameters
    ----------

    newZoomAreaDelegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::setZoomAreaDelegate(QQmlComponent
    #      *newZoomAreaDelegate)
    self.uglySide.call(
        'ritual_ZN11QGraphsView19setZoomAreaDelegateEP13QQmlComponent',
        self._addressOf(newZoomAreaDelegate),
    )

  @overload(float)
  def setZoomSensitivity(self, newZoomSensitivity: float) -> None:
    """
    Calls Qt's 'void QGraphsView::setZoomSensitivity(qreal
    newZoomSensitivity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#setZoomSensitivity

    Parameters
    ----------

    newZoomSensitivity : float
      Passed on as it is.
    """
    #  void QGraphsView::setZoomSensitivity(qreal newZoomSensitivity)
    self.uglySide.call(
        'ritual_ZN11QGraphsView18setZoomSensitivityEd', newZoomSensitivity,
    )

  @overload(bool)
  def setUseCanvasPainter(self, newUseCanvasPainter: bool) -> None:
    """
    Calls Qt's 'void QGraphsView::setUseCanvasPainter(bool
    newUseCanvasPainter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#setUseCanvasPainter

    Parameters
    ----------

    newUseCanvasPainter : bool
      Passed on as it is.
    """
    #  void QGraphsView::setUseCanvasPainter(bool newUseCanvasPainter)
    self.uglySide.call(
        'ritual_ZN11QGraphsView19setUseCanvasPainterEb', newUseCanvasPainter,
    )

  @overload(bool)
  def setDynamicLabelMargins(self, newDynamicLabelMargins: bool) -> None:
    """
    Calls Qt's 'void QGraphsView::setDynamicLabelMargins(bool
    newDynamicLabelMargins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#setDynamicLabelMargins

    Parameters
    ----------

    newDynamicLabelMargins : bool
      Passed on as it is.
    """
    #  void QGraphsView::setDynamicLabelMargins(bool newDynamicLabelMargins)
    self.uglySide.call(
        'ritual_ZN11QGraphsView22setDynamicLabelMarginsEb',
        newDynamicLabelMargins,
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
    Notes what was given, for Qt's 'QGraphsView::QGraphsView(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#QGraphsView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphsView::QGraphsView(QQuickItem *parent)
    self._noteCreation(QGraphsView, lambda: Rituals.call(
        'ritual_ZN11QGraphsViewC1EP10QQuickItem', self._addressOf(parent),
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

  @overload(QObject)
  @overload(NoneType)
  def addSeries(self, series: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QGraphsView::addSeries(QObject *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#addSeries

    Parameters
    ----------

    series : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::addSeries(QObject *series)
    self.uglySide.call(
        'ritual_ZN11QGraphsView9addSeriesEP7QObject',
        self._addressOf(series, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def insertSeries(self, index: int, series: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QGraphsView::insertSeries(qsizetype index, QObject
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#insertSeries

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::insertSeries(qsizetype index, QObject *series)
    self.uglySide.call(
        'ritual_ZN11QGraphsView12insertSeriesExP7QObject',
        index, self._addressOf(series, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QGraphsView::removeSeries(QObject *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#removeSeries

    Parameters
    ----------

    series : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::removeSeries(QObject *series)
    self.uglySide.call(
        'ritual_ZN11QGraphsView12removeSeriesEP7QObject',
        self._addressOf(series, 'QObject'),
    )

  @overload(int)
  def removeSeries(self, index: int) -> None:
    """
    Calls Qt's 'void QGraphsView::removeSeries(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#removeSeries

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGraphsView::removeSeries(qsizetype index)
    self.uglySide.call('ritual_ZN11QGraphsView12removeSeriesEx', index)

  @overload(QObject)
  @overload(NoneType)
  def hasSeries(self, series: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QGraphsView::hasSeries(QObject *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#hasSeries

    Parameters
    ----------

    series : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphsView::hasSeries(QObject *series)
    return self.uglySide.call(
        'ritual_ZN11QGraphsView9hasSeriesEP7QObject',
        self._addressOf(series, 'QObject'),
    )

  @overload(QAbstractSeries, float, float)
  @overload(NoneType, float, float)
  def getDataPointCoordinates(
      self,
      series: Optional[QAbstractSeries],
      x: float,
      y: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphsView::getDataPointCoordinates(QAbstractSeries
    *series, qreal x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#getDataPointCoordinates

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphsView::getDataPointCoordinates(QAbstractSeries *series,
    #      qreal x, qreal y)
    address = self.uglySide.call(
        'ritual_ZN11QGraphsView23getDataPointCoordinatesEP15QAbstractSeries'
        'dd',
        self._addressOf(series), x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def updatePlotArea(self) -> None:
    """
    Calls Qt's 'void QGraphsView::updatePlotArea()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#updatePlotArea
    """
    #  void QGraphsView::updatePlotArea()
    self.uglySide.call('ritual_ZN11QGraphsView14updatePlotAreaEv')

  def updateAxisAreas(self) -> None:
    """
    Calls Qt's 'void QGraphsView::updateAxisAreas()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#updateAxisAreas
    """
    #  void QGraphsView::updateAxisAreas()
    self.uglySide.call('ritual_ZN11QGraphsView15updateAxisAreasEv')

  @overload(QAbstractAxis)
  @overload(NoneType)
  def addAxis(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void QGraphsView::addAxis(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#addAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::addAxis(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN11QGraphsView7addAxisEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  @overload(QAbstractAxis, bool)
  @overload(NoneType, bool)
  def removeAxis(
      self,
      axis: Optional[QAbstractAxis],
      removeAllReferences: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QGraphsView::removeAxis(QAbstractAxis *axis, bool
    removeAllReferences)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#removeAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    removeAllReferences : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QGraphsView::removeAxis(QAbstractAxis *axis, bool
    #      removeAllReferences)
    self.uglySide.call(
        'ritual_ZN11QGraphsView10removeAxisEP13QAbstractAxisb',
        self._addressOf(axis), removeAllReferences,
    )

  def createBarsRenderer(self) -> None:
    """
    Calls Qt's 'void QGraphsView::createBarsRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#createBarsRenderer
    """
    #  void QGraphsView::createBarsRenderer()
    self.uglySide.call('ritual_ZN11QGraphsView18createBarsRendererEv')

  def createAxisRenderer(self) -> None:
    """
    Calls Qt's 'void QGraphsView::createAxisRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#createAxisRenderer
    """
    #  void QGraphsView::createAxisRenderer()
    self.uglySide.call('ritual_ZN11QGraphsView18createAxisRendererEv')

  def createPointRenderer(self) -> None:
    """
    Calls Qt's 'void QGraphsView::createPointRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#createPointRenderer
    """
    #  void QGraphsView::createPointRenderer()
    self.uglySide.call('ritual_ZN11QGraphsView19createPointRendererEv')

  def createPieRenderer(self) -> None:
    """
    Calls Qt's 'void QGraphsView::createPieRenderer()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#createPieRenderer
    """
    #  void QGraphsView::createPieRenderer()
    self.uglySide.call('ritual_ZN11QGraphsView17createPieRendererEv')

  def createAreaRenderer(self) -> None:
    """
    Calls Qt's 'void QGraphsView::createAreaRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#createAreaRenderer
    """
    #  void QGraphsView::createAreaRenderer()
    self.uglySide.call('ritual_ZN11QGraphsView18createAreaRendererEv')

  def createCustomRenderer(self) -> None:
    """
    Calls Qt's 'void QGraphsView::createCustomRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#createCustomRenderer
    """
    #  void QGraphsView::createCustomRenderer()
    self.uglySide.call('ritual_ZN11QGraphsView20createCustomRendererEv')

  def createCanvasPainter(self) -> None:
    """
    Calls Qt's 'void QGraphsView::createCanvasPainter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#createCanvasPainter
    """
    #  void QGraphsView::createCanvasPainter()
    self.uglySide.call('ritual_ZN11QGraphsView19createCanvasPainterEv')

  def removeCanvasPainter(self) -> None:
    """
    Calls Qt's 'void QGraphsView::removeCanvasPainter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#removeCanvasPainter
    """
    #  void QGraphsView::removeCanvasPainter()
    self.uglySide.call('ritual_ZN11QGraphsView19removeCanvasPainterEv')

  @overload(QCustomSeries, float)
  @overload(NoneType, float)
  def mapX(self, series: Optional[QCustomSeries], x: float) -> float:
    """
    Calls Qt's 'qreal QGraphsView::mapX(QCustomSeries *series, qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#mapX

    Parameters
    ----------

    series : Optional[QCustomSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.
    """
    #  qreal QGraphsView::mapX(QCustomSeries *series, qreal x)
    return self.uglySide.call(
        'ritual_ZN11QGraphsView4mapXEP13QCustomSeriesd',
        self._addressOf(series), x,
    )

  @overload(QCustomSeries, float)
  @overload(NoneType, float)
  def mapY(self, series: Optional[QCustomSeries], y: float) -> float:
    """
    Calls Qt's 'qreal QGraphsView::mapY(QCustomSeries *series, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#mapY

    Parameters
    ----------

    series : Optional[QCustomSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    y : float
      Passed on as it is.
    """
    #  qreal QGraphsView::mapY(QCustomSeries *series, qreal y)
    return self.uglySide.call(
        'ritual_ZN11QGraphsView4mapYEP13QCustomSeriesd',
        self._addressOf(series), y,
    )

  @overload(str, QPointF, QPointF)
  def handleHoverEnter(
      self,
      seriesName: str,
      position: QPointF,
      value: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QGraphsView::handleHoverEnter(const QString &seriesName,
    QPointF position, QPointF value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#handleHoverEnter

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphsView::handleHoverEnter(const QString &seriesName, QPointF
    #      position, QPointF value)
    self.uglySide.call(
        'ritual_ZN11QGraphsView16handleHoverEnterERK7QString7QPointFS3_',
        seriesName, self._valueOf(position, 'QPointF'), self._valueOf(value,
        'QPointF'),
    )

  @overload(str, QPointF)
  def handleHoverExit(self, seriesName: str, position: QPointF) -> None:
    """
    Calls Qt's 'void QGraphsView::handleHoverExit(const QString &seriesName,
    QPointF position)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#handleHoverExit

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphsView::handleHoverExit(const QString &seriesName, QPointF
    #      position)
    self.uglySide.call(
        'ritual_ZN11QGraphsView15handleHoverExitERK7QString7QPointF',
        seriesName, self._valueOf(position, 'QPointF'),
    )

  @overload(str, QPointF, QPointF)
  def handleHover(
      self,
      seriesName: str,
      position: QPointF,
      value: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QGraphsView::handleHover(const QString &seriesName,
    QPointF position, QPointF value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#handleHover

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphsView::handleHover(const QString &seriesName, QPointF
    #      position, QPointF value)
    self.uglySide.call(
        'ritual_ZN11QGraphsView11handleHoverERK7QString7QPointFS3_',
        seriesName, self._valueOf(position, 'QPointF'), self._valueOf(value,
        'QPointF'),
    )

  def updateComponentSizes(self) -> None:
    """
    Calls Qt's 'void QGraphsView::updateComponentSizes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#updateComponentSizes
    """
    #  void QGraphsView::updateComponentSizes()
    self.uglySide.call('ritual_ZN11QGraphsView20updateComponentSizesEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QGraphsView::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#componentComplete
    """
    #  void QGraphsView::componentComplete()
    ritual = 'ritual_ZN11QGraphsView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QGraphsView17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QGraphsView::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphsView::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN11QGraphsView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QGraphsView14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QGraphsView::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN11QGraphsView14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QGraphsView14hoverMoveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QGraphsView::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphsView::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN11QGraphsView10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QGraphsView10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      updatePaintNodeData: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QGraphsView::updatePaintNode(QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *updatePaintNodeData)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    updatePaintNodeData : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QGraphsView::updatePaintNode(QSGNode *oldNode,
    #      QQuickItem::UpdatePaintNodeData *updatePaintNodeData)
    ritual = (
        'ritual_ZN11QGraphsView15updatePaintNodeEP7QSGNodePN10QQuickItem19U'
        'pdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QGraphsView15updatePaintNodeEP7QSGNodePN10QQuickI'
          'tem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual,
        self._addressOf(oldNode, 'QSGNode'),
        self._addressOf(updatePaintNodeData),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QGraphsView::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#updatePolish
    """
    #  void QGraphsView::updatePolish()
    ritual = 'ritual_ZN11QGraphsView12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QGraphsView12updatePolishEv'
    self.uglySide.call(ritual)

  def themeChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::themeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#themeChanged
    """
    #  void QGraphsView::themeChanged()
    self.uglySide.call('ritual_ZN11QGraphsView12themeChangedEv')

  def marginTopChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::marginTopChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#marginTopChanged
    """
    #  void QGraphsView::marginTopChanged()
    self.uglySide.call('ritual_ZN11QGraphsView16marginTopChangedEv')

  def marginBottomChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::marginBottomChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#marginBottomChanged
    """
    #  void QGraphsView::marginBottomChanged()
    self.uglySide.call('ritual_ZN11QGraphsView19marginBottomChangedEv')

  def marginLeftChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::marginLeftChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#marginLeftChanged
    """
    #  void QGraphsView::marginLeftChanged()
    self.uglySide.call('ritual_ZN11QGraphsView17marginLeftChangedEv')

  def marginRightChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::marginRightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#marginRightChanged
    """
    #  void QGraphsView::marginRightChanged()
    self.uglySide.call('ritual_ZN11QGraphsView18marginRightChangedEv')

  def clipPlotAreaChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::clipPlotAreaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#clipPlotAreaChanged
    """
    #  void QGraphsView::clipPlotAreaChanged()
    self.uglySide.call('ritual_ZN11QGraphsView19clipPlotAreaChangedEv')

  def plotAreaChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::plotAreaChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#plotAreaChanged
    """
    #  void QGraphsView::plotAreaChanged()
    self.uglySide.call('ritual_ZN11QGraphsView15plotAreaChangedEv')

  @overload(str, QPointF, QPointF)
  def hoverEnter(
      self,
      seriesName: str,
      position: QPointF,
      value: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QGraphsView::hoverEnter(const QString &seriesName,
    QPointF position, QPointF value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#hoverEnter

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphsView::hoverEnter(const QString &seriesName, QPointF
    #      position, QPointF value)
    self.uglySide.call(
        'ritual_ZN11QGraphsView10hoverEnterERK7QString7QPointFS3_',
        seriesName, self._valueOf(position, 'QPointF'), self._valueOf(value,
        'QPointF'),
    )

  @overload(str, QPointF)
  def hoverExit(self, seriesName: str, position: QPointF) -> None:
    """
    Calls Qt's 'void QGraphsView::hoverExit(const QString &seriesName,
    QPointF position)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#hoverExit

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphsView::hoverExit(const QString &seriesName, QPointF
    #      position)
    self.uglySide.call(
        'ritual_ZN11QGraphsView9hoverExitERK7QString7QPointF',
        seriesName, self._valueOf(position, 'QPointF'),
    )

  @overload(str, QPointF, QPointF)
  def hover(
      self,
      seriesName: str,
      position: QPointF,
      value: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QGraphsView::hover(const QString &seriesName, QPointF
    position, QPointF value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#hover

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphsView::hover(const QString &seriesName, QPointF position,
    #      QPointF value)
    self.uglySide.call(
        'ritual_ZN11QGraphsView5hoverERK7QString7QPointFS3_',
        seriesName, self._valueOf(position, 'QPointF'), self._valueOf(value,
        'QPointF'),
    )

  def axisXSmoothingChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::axisXSmoothingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#axisXSmoothingChanged
    """
    #  void QGraphsView::axisXSmoothingChanged()
    self.uglySide.call('ritual_ZN11QGraphsView21axisXSmoothingChangedEv')

  def axisYSmoothingChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::axisYSmoothingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#axisYSmoothingChanged
    """
    #  void QGraphsView::axisYSmoothingChanged()
    self.uglySide.call('ritual_ZN11QGraphsView21axisYSmoothingChangedEv')

  def gridSmoothingChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::gridSmoothingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#gridSmoothingChanged
    """
    #  void QGraphsView::gridSmoothingChanged()
    self.uglySide.call('ritual_ZN11QGraphsView20gridSmoothingChangedEv')

  def shadowVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::shadowVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#shadowVisibleChanged
    """
    #  void QGraphsView::shadowVisibleChanged()
    self.uglySide.call('ritual_ZN11QGraphsView20shadowVisibleChangedEv')

  def shadowColorChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::shadowColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#shadowColorChanged
    """
    #  void QGraphsView::shadowColorChanged()
    self.uglySide.call('ritual_ZN11QGraphsView18shadowColorChangedEv')

  def shadowBarWidthChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::shadowBarWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#shadowBarWidthChanged
    """
    #  void QGraphsView::shadowBarWidthChanged()
    self.uglySide.call('ritual_ZN11QGraphsView21shadowBarWidthChangedEv')

  def shadowXOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::shadowXOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#shadowXOffsetChanged
    """
    #  void QGraphsView::shadowXOffsetChanged()
    self.uglySide.call('ritual_ZN11QGraphsView20shadowXOffsetChangedEv')

  def shadowYOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::shadowYOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#shadowYOffsetChanged
    """
    #  void QGraphsView::shadowYOffsetChanged()
    self.uglySide.call('ritual_ZN11QGraphsView20shadowYOffsetChangedEv')

  def shadowSmoothingChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::shadowSmoothingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#shadowSmoothingChanged
    """
    #  void QGraphsView::shadowSmoothingChanged()
    self.uglySide.call('ritual_ZN11QGraphsView22shadowSmoothingChangedEv')

  def axisXChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::axisXChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#axisXChanged
    """
    #  void QGraphsView::axisXChanged()
    self.uglySide.call('ritual_ZN11QGraphsView12axisXChangedEv')

  def axisYChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::axisYChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#axisYChanged
    """
    #  void QGraphsView::axisYChanged()
    self.uglySide.call('ritual_ZN11QGraphsView12axisYChangedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#orientationChanged
    """
    #  void QGraphsView::orientationChanged()
    self.uglySide.call('ritual_ZN11QGraphsView18orientationChangedEv')

  def zoomStyleChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::zoomStyleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#zoomStyleChanged
    """
    #  void QGraphsView::zoomStyleChanged()
    self.uglySide.call('ritual_ZN11QGraphsView16zoomStyleChangedEv')

  def panStyleChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::panStyleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#panStyleChanged
    """
    #  void QGraphsView::panStyleChanged()
    self.uglySide.call('ritual_ZN11QGraphsView15panStyleChangedEv')

  def zoomAreaEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::zoomAreaEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#zoomAreaEnabledChanged
    """
    #  void QGraphsView::zoomAreaEnabledChanged()
    self.uglySide.call('ritual_ZN11QGraphsView22zoomAreaEnabledChangedEv')

  def zoomAreaDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::zoomAreaDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#zoomAreaDelegateChanged
    """
    #  void QGraphsView::zoomAreaDelegateChanged()
    self.uglySide.call('ritual_ZN11QGraphsView23zoomAreaDelegateChangedEv')

  def zoomSensitivityChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::zoomSensitivityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#zoomSensitivityChanged
    """
    #  void QGraphsView::zoomSensitivityChanged()
    self.uglySide.call('ritual_ZN11QGraphsView22zoomSensitivityChangedEv')

  def useCanvasPainterChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::useCanvasPainterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#useCanvasPainterChanged
    """
    #  void QGraphsView::useCanvasPainterChanged()
    self.uglySide.call('ritual_ZN11QGraphsView23useCanvasPainterChangedEv')

  def dynamicLabelMarginsChanged(self) -> None:
    """
    Calls Qt's 'void QGraphsView::dynamicLabelMarginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#dynamicLabelMarginsChanged
    """
    #  void QGraphsView::dynamicLabelMarginsChanged()
    self.uglySide.call(
        'ritual_ZN11QGraphsView26dynamicLabelMarginsChangedEv',
    )

  def polishAndUpdate(self) -> None:
    """
    Calls Qt's 'void QGraphsView::polishAndUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphsview.html#polishAndUpdate
    """
    #  void QGraphsView::polishAndUpdate()
    self.uglySide.call('ritual_ZN11QGraphsView15polishAndUpdateEv')

  @overload(QAbstractSeries)
  @overload(NoneType)
  def getSeriesRendererIndex(self, series: Optional[QAbstractSeries]) -> int:
    """
    Calls Qt's 'int QGraphsView::getSeriesRendererIndex(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#getSeriesRendererIndex

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QGraphsView::getSeriesRendererIndex(QAbstractSeries *series)
    return self.uglySide.call(
        'ritual_ZN11QGraphsView22getSeriesRendererIndexEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(float)
  def onPinchScaleChanged(self, delta: float) -> None:
    """
    Calls Qt's 'void QGraphsView::onPinchScaleChanged(qreal delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#onPinchScaleChanged

    Parameters
    ----------

    delta : float
      Passed on as it is.
    """
    #  void QGraphsView::onPinchScaleChanged(qreal delta)
    self.uglySide.call(
        'ritual_ZN11QGraphsView19onPinchScaleChangedEd', delta,
    )

  @overload(QPointingDevice.GrabTransition, QEventPoint)
  def onPinchGrabChanged(
      self,
      transition: QPointingDevice.GrabTransition,
      point: QEventPoint,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphsView::onPinchGrabChanged(QPointingDevice::GrabTransition
    transition, QEventPoint point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphsview.html#onPinchGrabChanged

    Parameters
    ----------

    transition : QPointingDevice.GrabTransition
      Passed on as its number.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QGraphsView::onPinchGrabChanged(QPointingDevice::GrabTransition
    #      transition, QEventPoint point)
    self.uglySide.call(
        'ritual_ZN11QGraphsView18onPinchGrabChangedEN15QPointingDevice14Gra'
        'bTransitionE11QEventPoint',
        transition.value, self._valueOf(point),
    )

  @staticmethod
  def appendSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void QGraphsView::appendSeriesFunc(QQmlListProperty<QObject> *list,
    QObject *series)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QGraphsView.appendSeriesFunc' has no cute function yet. Qt's "
        "'void QGraphsView::appendSeriesFunc(QQmlListProperty<QObject> "
        "*list, QObject *series)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def atSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'QObject *QGraphsView::atSeriesFunc(QQmlListProperty<QObject> *list,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QGraphsView.atSeriesFunc' has no cute function yet. Qt's 'QObject "
        "*QGraphsView::atSeriesFunc(QQmlListProperty<QObject> *list, "
        "qsizetype index)': names 'QQmlListProperty<QObject>', which has no "
        "cute class yet.")

  @staticmethod
  def clearSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void QGraphsView::clearSeriesFunc(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphsView.clearSeriesFunc' has no cute function yet. Qt's 'void "
        "QGraphsView::clearSeriesFunc(QQmlListProperty<QObject> *list)': "
        "names 'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def countSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype QGraphsView::countSeriesFunc(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphsView.countSeriesFunc' has no cute function yet. Qt's "
        "'qsizetype QGraphsView::countSeriesFunc(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def customRenderer(*__, **_) -> Never:
    """
    Qt's 'CustomRenderer *QGraphsView::customRenderer() const': gives
    'CustomRenderer', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphsView.customRenderer' has no cute function yet. Qt's "
        "'CustomRenderer *QGraphsView::customRenderer() const': gives "
        "'CustomRenderer', which has no cute class yet.")

  @staticmethod
  def seriesList(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QGraphsView::seriesList()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGraphsView.seriesList' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QGraphsView::seriesList()': gives a "
        "type Python has no way to take yet.")
