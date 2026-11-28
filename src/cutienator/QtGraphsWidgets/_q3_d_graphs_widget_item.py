"""
Q3DGraphsWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphsWidgets/q3dgraphswidgetitem.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtGraphs import QtGraphs3D

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QLocale, QMetaObject, QPoint
  from ..QtGui import QColor, QEventPoint, QVector2D, QVector3D, QWheelEvent
  from ..QtGraphs import Q3DScene, QAbstract3DAxis, QAbstract3DSeries
  from ..QtGraphs import QCustom3DItem, QGraphsTheme
  from ..QtQuickWidgets import QQuickWidget
  from . import Q3DGraphsWidgetItemPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DSeries = WAIT['QtGraphs:QAbstract3DSeries']
  QColor = WAIT['QColor']
  QCustom3DItem = WAIT['QtGraphs:QCustom3DItem']
  QEvent = WAIT['QEvent']
  QEventPoint = WAIT['QEventPoint']
  QGraphsTheme = WAIT['QGraphsTheme']
  QLocale = WAIT['QLocale']
  QPoint = WAIT['QPoint']
  QQuickWidget = WAIT['QQuickWidget']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DGraphsWidgetItem(QObject):
  """
  The cute side of Qt's Q3DGraphsWidgetItem: a plain Python object standing
  in front of one C++ Q3DGraphsWidgetItem.

  It is built on the cute 'QObject', as Qt's Q3DGraphsWidgetItem is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DGraphsWidgetItem that has a ritual and that
  Python can call so far, 164 names in all: 'metaObject', 'tr', 'addTheme',
  'releaseTheme', 'activeTheme', 'themes', 'transparencyTechnique',
  'shadowQuality', 'selectionMode', 'scene', 'measureFps', 'currentFps',
  'isOrthoProjection', 'selectedElement', 'aspectRatio', 'optimizationHint',
  'isPolar', 'labelMargin', 'radialLabelOffset', 'horizontalAspectRatio',
  'locale', 'queriedGraphPosition', 'margin', 'cutoffMargin',
  'clearSelection', 'hasSeries', 'addCustomItem', 'removeCustomItems',
  'removeCustomItem', 'removeCustomItemAt', 'releaseCustomItem',
  'customItems', 'selectedLabelIndex', 'selectedAxis',
  'selectedCustomItemIndex', 'selectedCustomItem', 'cameraPreset',
  'cameraXRotation', 'cameraYRotation', 'minCameraXRotation',
  'maxCameraXRotation', 'minCameraYRotation', 'maxCameraYRotation',
  'isZoomAtTargetEnabled', 'isZoomEnabled', 'isSelectionEnabled',
  'isRotationEnabled', 'isPanEnabled', 'dragMode', 'cameraZoomLevel',
  'minCameraZoomLevel', 'maxCameraZoomLevel', 'cameraTargetPosition',
  'wrapCameraXRotation', 'wrapCameraYRotation', 'msaaSamples', 'doPicking',
  'doRayPicking', 'ambientLightStrength', 'lightStrength', 'shadowStrength',
  'lightColor', 'gridLineType', 'widget', 'setActiveTheme',
  'setTransparencyTechnique', 'setMeasureFps', 'setOrthoProjection',
  'setAspectRatio', 'setOptimizationHint', 'setPolar', 'setLabelMargin',
  'setRadialLabelOffset', 'setHorizontalAspectRatio', 'setLocale',
  'setMargin', 'setCutoffMargin', 'setCameraPreset', 'setCameraXRotation',
  'setCameraYRotation', 'setMinCameraXRotation', 'setMaxCameraXRotation',
  'setMinCameraYRotation', 'setMaxCameraYRotation', 'setZoomAtTargetEnabled',
  'setZoomEnabled', 'setSelectionEnabled', 'setRotationEnabled',
  'setPanEnabled', 'setDragMode', 'setDefaultInputHandler',
  'unsetDefaultInputHandler', 'unsetDefaultTapHandler',
  'unsetDefaultDragHandler', 'unsetDefaultWheelHandler',
  'unsetDefaultPinchHandler', 'setDragButton', 'setPanButton',
  'setCameraZoomLevel', 'setMinCameraZoomLevel', 'setMaxCameraZoomLevel',
  'setCameraTargetPosition', 'setWrapCameraXRotation',
  'setWrapCameraYRotation', 'setCameraPosition', 'setMsaaSamples',
  'setAmbientLightStrength', 'setLightStrength', 'setShadowStrength',
  'setLightColor', 'setWidget', 'event', 'eventFilter', 'activeThemeChanged',
  'shadowQualityChanged', 'transparencyTechniqueChanged',
  'selectionModeChanged', 'selectedElementChanged', 'measureFpsChanged',
  'currentFpsChanged', 'orthoProjectionChanged', 'aspectRatioChanged',
  'optimizationHintChanged', 'polarChanged', 'labelMarginChanged',
  'radialLabelOffsetChanged', 'horizontalAspectRatioChanged',
  'localeChanged', 'queriedGraphPositionChanged', 'marginChanged',
  'cutoffMarginChanged', 'cameraPresetChanged', 'cameraXRotationChanged',
  'cameraYRotationChanged', 'cameraZoomLevelChanged',
  'cameraTargetPositionChanged', 'minCameraZoomLevelChanged',
  'maxCameraZoomLevelChanged', 'minCameraXRotationChanged',
  'minCameraYRotationChanged', 'maxCameraXRotationChanged',
  'maxCameraYRotationChanged', 'wrapCameraXRotationChanged',
  'wrapCameraYRotationChanged', 'msaaSamplesChanged', 'tapped',
  'doubleTapped', 'longPressed', 'dragged', 'wheel', 'pinch', 'mouseMove',
  'zoomEnabledChanged', 'zoomAtTargetEnabledChanged',
  'rotationEnabledChanged', 'panEnabledChanged', 'dragModeChanged',
  'selectionEnabledChanged', 'ambientLightStrengthChanged',
  'lightStrengthChanged', 'shadowStrengthChanged', 'lightColorChanged',
  'gridLineTypeChanged', 'd_func'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DGraphsWidgetItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Q3DGraphsWidgetItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSharedPointer<QQuickItemGrabResult>
    Q3DGraphsWidgetItem::renderToImage(QSize imageSize) const': gives a type
    Python has no way to take yet.
  - Qt's 'Q3DGraphsWidgetItem::~Q3DGraphsWidgetItem()': the destructor:
    Python never removes a C++ Q3DGraphsWidgetItem.
  - Qt's 'void Q3DGraphsWidgetItem::setShadowQuality(const
    QtGraphs3D::ShadowQuality &shadowQuality)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void Q3DGraphsWidgetItem::setSelectionMode(const
    QtGraphs3D::SelectionFlags &selectionMode)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void Q3DGraphsWidgetItem::setGridLineType(const
    QtGraphs3D::GridLineType &gridLineType)': takes a type Python has no way
    to hand over yet.
  - Qt's 'Q3DGraphsWidgetItem::Q3DGraphsWidgetItem(Q3DGraphsWidgetItemPrivate
    &dd, QObject *parent, const QString &graph)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const Q3DGraphsWidgetItemPrivate *Q3DGraphsWidgetItem::d_func()
    const': takes in Python what 'Q3DGraphsWidgetItemPrivate
    *Q3DGraphsWidgetItem::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 179 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ Q3DGraphsWidgetItem is created at the first use, not by
    'Q3DGraphsWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DGraphsWidgetItem.
  - Qt tells when it has removed the C++ Q3DGraphsWidgetItem. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Q3DGraphsWidgetItem that has no cute function yet,
    '__init__', 'renderToImage', 'setGridLineType', 'setSelectionMode',
    'setShadowQuality', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

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
    Calls Qt's 'QString Q3DGraphsWidgetItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#tr

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
    #  QString Q3DGraphsWidgetItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19Q3DGraphsWidgetItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DGraphsWidgetItem'

  #  A C++ Q3DGraphsWidgetItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DGraphsWidgetItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DGraphsWidgetItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DGraphsWidgetItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def activeTheme(self) -> Optional[QGraphsTheme]:
    """
    Calls Qt's 'QGraphsTheme *Q3DGraphsWidgetItem::activeTheme() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#activeTheme

    Returns
    -------

    Optional[QGraphsTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphsTheme *Q3DGraphsWidgetItem::activeTheme() const
    address = self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem11activeThemeEv',
    )
    from ..QtGraphs import QGraphsTheme
    return QGraphsTheme._cuteAt(address)

  def themes(self) -> QList[QGraphsTheme]:
    """
    Calls Qt's 'QList<QGraphsTheme *> Q3DGraphsWidgetItem::themes() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#themes

    Returns
    -------

    QList[QGraphsTheme]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphsTheme *> Q3DGraphsWidgetItem::themes() const
    address = self.uglySide.call('ritual_ZNK19Q3DGraphsWidgetItem6themesEv')
    from ..QtGraphs import QGraphsTheme
    return QList[QGraphsTheme]._cuteOwning(address)

  def transparencyTechnique(self) -> QtGraphs3D.TransparencyTechnique:
    """
    Calls Qt's 'QtGraphs3D::TransparencyTechnique
    Q3DGraphsWidgetItem::transparencyTechnique() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#transparencyTechnique

    Returns
    -------

    QtGraphs3D.TransparencyTechnique
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.TransparencyTechnique(number)' gives.
    """
    #  QtGraphs3D::TransparencyTechnique
    #      Q3DGraphsWidgetItem::transparencyTechnique() const
    return QtGraphs3D.TransparencyTechnique(self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem21transparencyTechniqueEv',
    ))

  def shadowQuality(self) -> QtGraphs3D.ShadowQuality:
    """
    Calls Qt's 'QtGraphs3D::ShadowQuality
    Q3DGraphsWidgetItem::shadowQuality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#shadowQuality

    Returns
    -------

    QtGraphs3D.ShadowQuality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.ShadowQuality(number)' gives.
    """
    #  QtGraphs3D::ShadowQuality Q3DGraphsWidgetItem::shadowQuality() const
    return QtGraphs3D.ShadowQuality(self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem13shadowQualityEv',
    ))

  def selectionMode(self) -> QtGraphs3D.SelectionFlags:
    """
    Calls Qt's 'QtGraphs3D::SelectionFlags
    Q3DGraphsWidgetItem::selectionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#selectionMode

    Returns
    -------

    QtGraphs3D.SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  QtGraphs3D::SelectionFlags Q3DGraphsWidgetItem::selectionMode() const
    return QtGraphs3D.SelectionFlags(self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem13selectionModeEv',
    ))

  def scene(self) -> Optional[Q3DScene]:
    """
    Calls Qt's 'Q3DScene *Q3DGraphsWidgetItem::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#scene

    Returns
    -------

    Optional[Q3DScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScene *Q3DGraphsWidgetItem::scene() const
    address = self.uglySide.call('ritual_ZNK19Q3DGraphsWidgetItem5sceneEv')
    from ..QtGraphs import Q3DScene
    return Q3DScene._cuteAt(address)

  def measureFps(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::measureFps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#measureFps
    """
    #  bool Q3DGraphsWidgetItem::measureFps() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem10measureFpsEv',
    )

  def currentFps(self) -> int:
    """
    Calls Qt's 'int Q3DGraphsWidgetItem::currentFps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#currentFps
    """
    #  int Q3DGraphsWidgetItem::currentFps() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem10currentFpsEv',
    )

  def isOrthoProjection(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::isOrthoProjection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#isOrthoProjection
    """
    #  bool Q3DGraphsWidgetItem::isOrthoProjection() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem17isOrthoProjectionEv',
    )

  def selectedElement(self) -> QtGraphs3D.ElementType:
    """
    Calls Qt's 'QtGraphs3D::ElementType
    Q3DGraphsWidgetItem::selectedElement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#selectedElement

    Returns
    -------

    QtGraphs3D.ElementType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.ElementType(number)' gives.
    """
    #  QtGraphs3D::ElementType Q3DGraphsWidgetItem::selectedElement() const
    return QtGraphs3D.ElementType(self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem15selectedElementEv',
    ))

  def aspectRatio(self) -> float:
    """
    Calls Qt's 'qreal Q3DGraphsWidgetItem::aspectRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#aspectRatio
    """
    #  qreal Q3DGraphsWidgetItem::aspectRatio() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem11aspectRatioEv',
    )

  def optimizationHint(self) -> QtGraphs3D.OptimizationHint:
    """
    Calls Qt's 'QtGraphs3D::OptimizationHint
    Q3DGraphsWidgetItem::optimizationHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#optimizationHint

    Returns
    -------

    QtGraphs3D.OptimizationHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.OptimizationHint(number)' gives.
    """
    #  QtGraphs3D::OptimizationHint Q3DGraphsWidgetItem::optimizationHint()
    #      const
    return QtGraphs3D.OptimizationHint(self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem16optimizationHintEv',
    ))

  def isPolar(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::isPolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#isPolar
    """
    #  bool Q3DGraphsWidgetItem::isPolar() const
    return self.uglySide.call('ritual_ZNK19Q3DGraphsWidgetItem7isPolarEv')

  def labelMargin(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::labelMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#labelMargin
    """
    #  float Q3DGraphsWidgetItem::labelMargin() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem11labelMarginEv',
    )

  def radialLabelOffset(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::radialLabelOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#radialLabelOffset
    """
    #  float Q3DGraphsWidgetItem::radialLabelOffset() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem17radialLabelOffsetEv',
    )

  def horizontalAspectRatio(self) -> float:
    """
    Calls Qt's 'qreal Q3DGraphsWidgetItem::horizontalAspectRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#horizontalAspectRatio
    """
    #  qreal Q3DGraphsWidgetItem::horizontalAspectRatio() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem21horizontalAspectRatioEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale Q3DGraphsWidgetItem::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale Q3DGraphsWidgetItem::locale() const
    address = self.uglySide.call('ritual_ZNK19Q3DGraphsWidgetItem6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def queriedGraphPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Q3DGraphsWidgetItem::queriedGraphPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#queriedGraphPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Q3DGraphsWidgetItem::queriedGraphPosition() const
    address = self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem20queriedGraphPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def margin(self) -> float:
    """
    Calls Qt's 'qreal Q3DGraphsWidgetItem::margin() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#margin
    """
    #  qreal Q3DGraphsWidgetItem::margin() const
    return self.uglySide.call('ritual_ZNK19Q3DGraphsWidgetItem6marginEv')

  def cutoffMargin(self) -> float:
    """
    Calls Qt's 'qreal Q3DGraphsWidgetItem::cutoffMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cutoffMargin
    """
    #  qreal Q3DGraphsWidgetItem::cutoffMargin() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem12cutoffMarginEv',
    )

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def hasSeries(self, series: Optional[QAbstract3DSeries]) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::hasSeries(QAbstract3DSeries
    *series) const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#hasSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Q3DGraphsWidgetItem::hasSeries(QAbstract3DSeries *series) const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem9hasSeriesEP17QAbstract3DSeries',
        self._addressOf(series),
    )

  def customItems(self) -> QList[QCustom3DItem]:
    """
    Calls Qt's 'QList<QCustom3DItem *> Q3DGraphsWidgetItem::customItems()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#customItems

    Returns
    -------

    QList[QCustom3DItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCustom3DItem *> Q3DGraphsWidgetItem::customItems() const
    address = self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem11customItemsEv',
    )
    from ..QtGraphs import QCustom3DItem
    return QList[QCustom3DItem]._cuteOwning(address)

  def selectedLabelIndex(self) -> int:
    """
    Calls Qt's 'int Q3DGraphsWidgetItem::selectedLabelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#selectedLabelIndex
    """
    #  int Q3DGraphsWidgetItem::selectedLabelIndex() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem18selectedLabelIndexEv',
    )

  def selectedAxis(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *Q3DGraphsWidgetItem::selectedAxis() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#selectedAxis

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *Q3DGraphsWidgetItem::selectedAxis() const
    address = self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem12selectedAxisEv',
    )
    from ..QtGraphs import QAbstract3DAxis
    return QAbstract3DAxis._cuteAt(address)

  def selectedCustomItemIndex(self) -> int:
    """
    Calls Qt's 'qsizetype Q3DGraphsWidgetItem::selectedCustomItemIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#selectedCustomItemIndex
    """
    #  qsizetype Q3DGraphsWidgetItem::selectedCustomItemIndex() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem23selectedCustomItemIndexEv',
    )

  def selectedCustomItem(self) -> Optional[QCustom3DItem]:
    """
    Calls Qt's 'QCustom3DItem *Q3DGraphsWidgetItem::selectedCustomItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#selectedCustomItem

    Returns
    -------

    Optional[QCustom3DItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DItem *Q3DGraphsWidgetItem::selectedCustomItem() const
    address = self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem18selectedCustomItemEv',
    )
    from ..QtGraphs import QCustom3DItem
    return QCustom3DItem._cuteAt(address)

  def cameraPreset(self) -> QtGraphs3D.CameraPreset:
    """
    Calls Qt's 'QtGraphs3D::CameraPreset Q3DGraphsWidgetItem::cameraPreset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cameraPreset

    Returns
    -------

    QtGraphs3D.CameraPreset
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.CameraPreset(number)' gives.
    """
    #  QtGraphs3D::CameraPreset Q3DGraphsWidgetItem::cameraPreset() const
    return QtGraphs3D.CameraPreset(self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem12cameraPresetEv',
    ))

  def cameraXRotation(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::cameraXRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cameraXRotation
    """
    #  float Q3DGraphsWidgetItem::cameraXRotation() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem15cameraXRotationEv',
    )

  def cameraYRotation(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::cameraYRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cameraYRotation
    """
    #  float Q3DGraphsWidgetItem::cameraYRotation() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem15cameraYRotationEv',
    )

  def minCameraXRotation(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::minCameraXRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#minCameraXRotation
    """
    #  float Q3DGraphsWidgetItem::minCameraXRotation() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem18minCameraXRotationEv',
    )

  def maxCameraXRotation(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::maxCameraXRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#maxCameraXRotation
    """
    #  float Q3DGraphsWidgetItem::maxCameraXRotation() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem18maxCameraXRotationEv',
    )

  def minCameraYRotation(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::minCameraYRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#minCameraYRotation
    """
    #  float Q3DGraphsWidgetItem::minCameraYRotation() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem18minCameraYRotationEv',
    )

  def maxCameraYRotation(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::maxCameraYRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#maxCameraYRotation
    """
    #  float Q3DGraphsWidgetItem::maxCameraYRotation() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem18maxCameraYRotationEv',
    )

  def isZoomAtTargetEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::isZoomAtTargetEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#isZoomAtTargetEnabled
    """
    #  bool Q3DGraphsWidgetItem::isZoomAtTargetEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem21isZoomAtTargetEnabledEv',
    )

  def isZoomEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::isZoomEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#isZoomEnabled
    """
    #  bool Q3DGraphsWidgetItem::isZoomEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem13isZoomEnabledEv',
    )

  def isSelectionEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::isSelectionEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#isSelectionEnabled
    """
    #  bool Q3DGraphsWidgetItem::isSelectionEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem18isSelectionEnabledEv',
    )

  def isRotationEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::isRotationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#isRotationEnabled
    """
    #  bool Q3DGraphsWidgetItem::isRotationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem17isRotationEnabledEv',
    )

  def isPanEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::isPanEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#isPanEnabled
    """
    #  bool Q3DGraphsWidgetItem::isPanEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem12isPanEnabledEv',
    )

  def dragMode(self) -> QtGraphs3D.DragMode:
    """
    Calls Qt's 'QtGraphs3D::DragMode Q3DGraphsWidgetItem::dragMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#dragMode

    Returns
    -------

    QtGraphs3D.DragMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.DragMode(number)' gives.
    """
    #  QtGraphs3D::DragMode Q3DGraphsWidgetItem::dragMode() const
    return QtGraphs3D.DragMode(self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem8dragModeEv',
    ))

  def cameraZoomLevel(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::cameraZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cameraZoomLevel
    """
    #  float Q3DGraphsWidgetItem::cameraZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem15cameraZoomLevelEv',
    )

  def minCameraZoomLevel(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::minCameraZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#minCameraZoomLevel
    """
    #  float Q3DGraphsWidgetItem::minCameraZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem18minCameraZoomLevelEv',
    )

  def maxCameraZoomLevel(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::maxCameraZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#maxCameraZoomLevel
    """
    #  float Q3DGraphsWidgetItem::maxCameraZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem18maxCameraZoomLevelEv',
    )

  def cameraTargetPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Q3DGraphsWidgetItem::cameraTargetPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cameraTargetPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Q3DGraphsWidgetItem::cameraTargetPosition() const
    address = self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem20cameraTargetPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def wrapCameraXRotation(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::wrapCameraXRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#wrapCameraXRotation
    """
    #  bool Q3DGraphsWidgetItem::wrapCameraXRotation() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem19wrapCameraXRotationEv',
    )

  def wrapCameraYRotation(self) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::wrapCameraYRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#wrapCameraYRotation
    """
    #  bool Q3DGraphsWidgetItem::wrapCameraYRotation() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem19wrapCameraYRotationEv',
    )

  def msaaSamples(self) -> int:
    """
    Calls Qt's 'int Q3DGraphsWidgetItem::msaaSamples() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#msaaSamples
    """
    #  int Q3DGraphsWidgetItem::msaaSamples() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem11msaaSamplesEv',
    )

  def ambientLightStrength(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::ambientLightStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#ambientLightStrength
    """
    #  float Q3DGraphsWidgetItem::ambientLightStrength() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem20ambientLightStrengthEv',
    )

  def lightStrength(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::lightStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#lightStrength
    """
    #  float Q3DGraphsWidgetItem::lightStrength() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem13lightStrengthEv',
    )

  def shadowStrength(self) -> float:
    """
    Calls Qt's 'float Q3DGraphsWidgetItem::shadowStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#shadowStrength
    """
    #  float Q3DGraphsWidgetItem::shadowStrength() const
    return self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem14shadowStrengthEv',
    )

  def lightColor(self) -> QColor:
    """
    Calls Qt's 'QColor Q3DGraphsWidgetItem::lightColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#lightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Q3DGraphsWidgetItem::lightColor() const
    address = self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem10lightColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def gridLineType(self) -> QtGraphs3D.GridLineType:
    """
    Calls Qt's 'QtGraphs3D::GridLineType Q3DGraphsWidgetItem::gridLineType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#gridLineType

    Returns
    -------

    QtGraphs3D.GridLineType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.GridLineType(number)' gives.
    """
    #  QtGraphs3D::GridLineType Q3DGraphsWidgetItem::gridLineType() const
    return QtGraphs3D.GridLineType(self.uglySide.call(
        'ritual_ZNK19Q3DGraphsWidgetItem12gridLineTypeEv',
    ))

  def widget(self) -> Optional[QQuickWidget]:
    """
    Calls Qt's 'QQuickWidget *Q3DGraphsWidgetItem::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#widget

    Returns
    -------

    Optional[QQuickWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWidget *Q3DGraphsWidgetItem::widget() const
    address = self.uglySide.call('ritual_ZNK19Q3DGraphsWidgetItem6widgetEv')
    from ..QtQuickWidgets import QQuickWidget
    return QQuickWidget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphsTheme)
  @overload(NoneType)
  def setActiveTheme(self, activeTheme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setActiveTheme(QGraphsTheme
    *activeTheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setActiveTheme

    Parameters
    ----------

    activeTheme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DGraphsWidgetItem::setActiveTheme(QGraphsTheme *activeTheme)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem14setActiveThemeEP12QGraphsTheme',
        self._addressOf(activeTheme),
    )

  @overload(QtGraphs3D.TransparencyTechnique)
  def setTransparencyTechnique(
      self,
      technique: QtGraphs3D.TransparencyTechnique,
  ) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::setTransparencyTechnique(QtGraphs3D::
    TransparencyTechnique technique)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setTransparencyTechnique

    Parameters
    ----------

    technique : QtGraphs3D.TransparencyTechnique
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::setTransparencyTechnique(QtGraphs3D::
    #      TransparencyTechnique technique)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem24setTransparencyTechniqueEN10QtGrap'
        'hs3D21TransparencyTechniqueE',
        technique.value,
    )

  @overload(bool)
  def setMeasureFps(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setMeasureFps(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setMeasureFps

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setMeasureFps(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem13setMeasureFpsEb', enable,
    )

  @overload(bool)
  def setOrthoProjection(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setOrthoProjection(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setOrthoProjection

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setOrthoProjection(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18setOrthoProjectionEb', enable,
    )

  @overload(float)
  def setAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setAspectRatio(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setAspectRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem14setAspectRatioEd', ratio,
    )

  @overload(QtGraphs3D.OptimizationHint)
  def setOptimizationHint(self, hint: QtGraphs3D.OptimizationHint) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::setOptimizationHint(QtGraphs3D::OptimizationHint
    hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setOptimizationHint

    Parameters
    ----------

    hint : QtGraphs3D.OptimizationHint
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::setOptimizationHint(QtGraphs3D::
    #      OptimizationHint hint)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem19setOptimizationHintEN10QtGraphs3D1'
        '6OptimizationHintE',
        hint.value,
    )

  @overload(bool)
  def setPolar(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setPolar(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setPolar

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setPolar(bool enable)
    self.uglySide.call('ritual_ZN19Q3DGraphsWidgetItem8setPolarEb', enable)

  @overload(float)
  def setLabelMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setLabelMargin(float margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setLabelMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setLabelMargin(float margin)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem14setLabelMarginEf', margin,
    )

  @overload(float)
  def setRadialLabelOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setRadialLabelOffset(float
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setRadialLabelOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setRadialLabelOffset(float offset)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem20setRadialLabelOffsetEf', offset,
    )

  @overload(float)
  def setHorizontalAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setHorizontalAspectRatio(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setHorizontalAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setHorizontalAspectRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem24setHorizontalAspectRatioEd', ratio,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(float)
  def setMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setMargin(qreal margin)
    self.uglySide.call('ritual_ZN19Q3DGraphsWidgetItem9setMarginEd', margin)

  @overload(float)
  def setCutoffMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setCutoffMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setCutoffMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setCutoffMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem15setCutoffMarginEd', margin,
    )

  @overload(QtGraphs3D.CameraPreset)
  def setCameraPreset(self, preset: QtGraphs3D.CameraPreset) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::setCameraPreset(QtGraphs3D::CameraPreset preset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setCameraPreset

    Parameters
    ----------

    preset : QtGraphs3D.CameraPreset
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::setCameraPreset(QtGraphs3D::CameraPreset
    #      preset)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem15setCameraPresetEN10QtGraphs3D12Cam'
        'eraPresetE',
        preset.value,
    )

  @overload(float)
  def setCameraXRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setCameraXRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setCameraXRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setCameraXRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18setCameraXRotationEf', rotation,
    )

  @overload(float)
  def setCameraYRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setCameraYRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setCameraYRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setCameraYRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18setCameraYRotationEf', rotation,
    )

  @overload(float)
  def setMinCameraXRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setMinCameraXRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setMinCameraXRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setMinCameraXRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem21setMinCameraXRotationEf', rotation,
    )

  @overload(float)
  def setMaxCameraXRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setMaxCameraXRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setMaxCameraXRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setMaxCameraXRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem21setMaxCameraXRotationEf', rotation,
    )

  @overload(float)
  def setMinCameraYRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setMinCameraYRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setMinCameraYRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setMinCameraYRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem21setMinCameraYRotationEf', rotation,
    )

  @overload(float)
  def setMaxCameraYRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setMaxCameraYRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setMaxCameraYRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setMaxCameraYRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem21setMaxCameraYRotationEf', rotation,
    )

  @overload(bool)
  def setZoomAtTargetEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setZoomAtTargetEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setZoomAtTargetEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setZoomAtTargetEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22setZoomAtTargetEnabledEb', enable,
    )

  @overload(bool)
  def setZoomEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setZoomEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setZoomEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setZoomEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem14setZoomEnabledEb', enable,
    )

  @overload(bool)
  def setSelectionEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setSelectionEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setSelectionEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setSelectionEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem19setSelectionEnabledEb', enable,
    )

  @overload(bool)
  def setRotationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setRotationEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setRotationEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setRotationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18setRotationEnabledEb', enable,
    )

  @overload(bool)
  def setPanEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setPanEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setPanEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setPanEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem13setPanEnabledEb', enable,
    )

  @overload(QtGraphs3D.DragMode)
  def setDragMode(self, newDragMode: QtGraphs3D.DragMode) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setDragMode(QtGraphs3D::DragMode
    newDragMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setDragMode

    Parameters
    ----------

    newDragMode : QtGraphs3D.DragMode
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::setDragMode(QtGraphs3D::DragMode
    #      newDragMode)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem11setDragModeEN10QtGraphs3D8DragMode'
        'E',
        newDragMode.value,
    )

  def setDefaultInputHandler(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setDefaultInputHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setDefaultInputHandler
    """
    #  void Q3DGraphsWidgetItem::setDefaultInputHandler()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22setDefaultInputHandlerEv',
    )

  @overload(Qt.MouseButtons)
  def setDragButton(self, button: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setDragButton(Qt::MouseButtons
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setDragButton

    Parameters
    ----------

    button : Qt.MouseButtons
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::setDragButton(Qt::MouseButtons button)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem13setDragButtonE6QFlagsIN2Qt11MouseB'
        'uttonEE',
        button.value,
    )

  @overload(Qt.MouseButtons)
  def setPanButton(self, button: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setPanButton(Qt::MouseButtons
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setPanButton

    Parameters
    ----------

    button : Qt.MouseButtons
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::setPanButton(Qt::MouseButtons button)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem12setPanButtonE6QFlagsIN2Qt11MouseBu'
        'ttonEE',
        button.value,
    )

  @overload(float)
  def setCameraZoomLevel(self, level: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setCameraZoomLevel(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setCameraZoomLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setCameraZoomLevel(float level)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18setCameraZoomLevelEf', level,
    )

  @overload(float)
  def setMinCameraZoomLevel(self, level: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setMinCameraZoomLevel(float
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setMinCameraZoomLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setMinCameraZoomLevel(float level)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem21setMinCameraZoomLevelEf', level,
    )

  @overload(float)
  def setMaxCameraZoomLevel(self, level: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setMaxCameraZoomLevel(float
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setMaxCameraZoomLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setMaxCameraZoomLevel(float level)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem21setMaxCameraZoomLevelEf', level,
    )

  @overload(QVector3D)
  def setCameraTargetPosition(self, target: QVector3D) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setCameraTargetPosition(QVector3D
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setCameraTargetPosition

    Parameters
    ----------

    target : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::setCameraTargetPosition(QVector3D target)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem23setCameraTargetPositionE9QVector3D',
        self._valueOf(target),
    )

  @overload(bool)
  def setWrapCameraXRotation(self, wrap: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setWrapCameraXRotation(bool wrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setWrapCameraXRotation

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setWrapCameraXRotation(bool wrap)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22setWrapCameraXRotationEb', wrap,
    )

  @overload(bool)
  def setWrapCameraYRotation(self, wrap: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setWrapCameraYRotation(bool wrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setWrapCameraYRotation

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setWrapCameraYRotation(bool wrap)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22setWrapCameraYRotationEb', wrap,
    )

  @overload(float, float)
  @overload(float, float, float)
  def setCameraPosition(
      self,
      horizontal: float,
      vertical: float,
      zoom: float = 100.0,
  ) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setCameraPosition(float horizontal,
    float vertical, float zoom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setCameraPosition

    Parameters
    ----------

    horizontal : float
      Passed on as it is.

    vertical : float
      Passed on as it is.

    zoom : float
      Passed on as it is. May be left out, as in Qt: it is then 100.0.
    """
    #  void Q3DGraphsWidgetItem::setCameraPosition(float horizontal, float
    #      vertical, float zoom)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem17setCameraPositionEfff',
        horizontal, vertical, zoom,
    )

  @overload(int)
  def setMsaaSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setMsaaSamples(int samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setMsaaSamples

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setMsaaSamples(int samples)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem14setMsaaSamplesEi', samples,
    )

  @overload(float)
  def setAmbientLightStrength(self, newAmbientLightStrength: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setAmbientLightStrength(float
    newAmbientLightStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setAmbientLightStrength

    Parameters
    ----------

    newAmbientLightStrength : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setAmbientLightStrength(float
    #      newAmbientLightStrength)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem23setAmbientLightStrengthEf',
        newAmbientLightStrength,
    )

  @overload(float)
  def setLightStrength(self, newLightStrength: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setLightStrength(float
    newLightStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setLightStrength

    Parameters
    ----------

    newLightStrength : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setLightStrength(float newLightStrength)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem16setLightStrengthEf',
        newLightStrength,
    )

  @overload(float)
  def setShadowStrength(self, newShadowStrength: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setShadowStrength(float
    newShadowStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setShadowStrength

    Parameters
    ----------

    newShadowStrength : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::setShadowStrength(float newShadowStrength)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem17setShadowStrengthEf',
        newShadowStrength,
    )

  @overload(QColor)
  def setLightColor(self, newLightColor: QColor) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setLightColor(QColor
    newLightColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setLightColor

    Parameters
    ----------

    newLightColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::setLightColor(QColor newLightColor)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem13setLightColorE6QColor',
        self._valueOf(newLightColor),
    )

  @overload(QQuickWidget)
  @overload(NoneType)
  def setWidget(self, widget: Optional[QQuickWidget]) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::setWidget(QQuickWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#setWidget

    Parameters
    ----------

    widget : Optional[QQuickWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DGraphsWidgetItem::setWidget(QQuickWidget *widget)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem9setWidgetEP12QQuickWidget',
        self._addressOf(widget),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Q3DGraphsWidgetItem::Q3DGraphsWidgetItem(Q3DGraphsWidgetItemPrivate
    &dd, QObject *parent, const QString &graph)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DGraphsWidgetItem.__init__' has no cute function yet. Qt's "
        "'Q3DGraphsWidgetItem::Q3DGraphsWidgetItem(Q3DGraphsWidgetItemPrivat"
        "e &dd, QObject *parent, const QString &graph)': takes a type "
        "Python has no way to hand over yet.")

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

  @overload(QGraphsTheme)
  @overload(NoneType)
  def addTheme(self, theme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::addTheme(QGraphsTheme *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#addTheme

    Parameters
    ----------

    theme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DGraphsWidgetItem::addTheme(QGraphsTheme *theme)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem8addThemeEP12QGraphsTheme',
        self._addressOf(theme),
    )

  @overload(QGraphsTheme)
  @overload(NoneType)
  def releaseTheme(self, theme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::releaseTheme(QGraphsTheme *theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#releaseTheme

    Parameters
    ----------

    theme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DGraphsWidgetItem::releaseTheme(QGraphsTheme *theme)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem12releaseThemeEP12QGraphsTheme',
        self._addressOf(theme),
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#clearSelection
    """
    #  void Q3DGraphsWidgetItem::clearSelection()
    self.uglySide.call('ritual_ZN19Q3DGraphsWidgetItem14clearSelectionEv')

  @overload(QCustom3DItem)
  @overload(NoneType)
  def addCustomItem(self, item: Optional[QCustom3DItem]) -> int:
    """
    Calls Qt's 'qsizetype Q3DGraphsWidgetItem::addCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#addCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qsizetype Q3DGraphsWidgetItem::addCustomItem(QCustom3DItem *item)
    return self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem13addCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  def removeCustomItems(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::removeCustomItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#removeCustomItems
    """
    #  void Q3DGraphsWidgetItem::removeCustomItems()
    self.uglySide.call('ritual_ZN19Q3DGraphsWidgetItem17removeCustomItemsEv')

  @overload(QCustom3DItem)
  @overload(NoneType)
  def removeCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::removeCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#removeCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DGraphsWidgetItem::removeCustomItem(QCustom3DItem *item)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem16removeCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  @overload(QVector3D)
  def removeCustomItemAt(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::removeCustomItemAt(QVector3D
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#removeCustomItemAt

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::removeCustomItemAt(QVector3D position)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18removeCustomItemAtE9QVector3D',
        self._valueOf(position),
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def releaseCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::releaseCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#releaseCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DGraphsWidgetItem::releaseCustomItem(QCustom3DItem *item)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem17releaseCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  @overload(QPoint)
  def doPicking(self, point: QPoint) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::doPicking(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#doPicking

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::doPicking(QPoint point)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem9doPickingE6QPoint',
        self._valueOf(point),
    )

  @overload(QVector3D, QVector3D)
  def doRayPicking(self, origin: QVector3D, direction: QVector3D) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::doRayPicking(QVector3D origin,
    QVector3D direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#doRayPicking

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::doRayPicking(QVector3D origin, QVector3D
    #      direction)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem12doRayPickingE9QVector3DS0_',
        self._valueOf(origin), self._valueOf(direction),
    )

  def unsetDefaultInputHandler(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::unsetDefaultInputHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#unsetDefaultInputHandler
    """
    #  void Q3DGraphsWidgetItem::unsetDefaultInputHandler()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem24unsetDefaultInputHandlerEv',
    )

  def unsetDefaultTapHandler(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::unsetDefaultTapHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#unsetDefaultTapHandler
    """
    #  void Q3DGraphsWidgetItem::unsetDefaultTapHandler()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22unsetDefaultTapHandlerEv',
    )

  def unsetDefaultDragHandler(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::unsetDefaultDragHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#unsetDefaultDragHandler
    """
    #  void Q3DGraphsWidgetItem::unsetDefaultDragHandler()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem23unsetDefaultDragHandlerEv',
    )

  def unsetDefaultWheelHandler(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::unsetDefaultWheelHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#unsetDefaultWheelHandler
    """
    #  void Q3DGraphsWidgetItem::unsetDefaultWheelHandler()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem24unsetDefaultWheelHandlerEv',
    )

  def unsetDefaultPinchHandler(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::unsetDefaultPinchHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#unsetDefaultPinchHandler
    """
    #  void Q3DGraphsWidgetItem::unsetDefaultPinchHandler()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem24unsetDefaultPinchHandlerEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Q3DGraphsWidgetItem::event(QEvent *event)
    ritual = 'ritual_ZN19Q3DGraphsWidgetItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19Q3DGraphsWidgetItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      obj: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool Q3DGraphsWidgetItem::eventFilter(QObject *obj, QEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#eventFilter

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Q3DGraphsWidgetItem::eventFilter(QObject *obj, QEvent *event)
    ritual = 'ritual_ZN19Q3DGraphsWidgetItem11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19Q3DGraphsWidgetItem11eventFilterEP7QObjectP6QEven'
          't')
    return self.uglySide.call(
        ritual, self._addressOf(obj, 'QObject'), self._addressOf(event),
    )

  @overload(QGraphsTheme)
  @overload(NoneType)
  def activeThemeChanged(self, activeTheme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::activeThemeChanged(QGraphsTheme
    *activeTheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#activeThemeChanged

    Parameters
    ----------

    activeTheme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DGraphsWidgetItem::activeThemeChanged(QGraphsTheme
    #      *activeTheme)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18activeThemeChangedEP12QGraphsTheme',
        self._addressOf(activeTheme),
    )

  @overload(QtGraphs3D.ShadowQuality)
  def shadowQualityChanged(self, quality: QtGraphs3D.ShadowQuality) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::shadowQualityChanged(QtGraphs3D::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#shadowQualityChanged

    Parameters
    ----------

    quality : QtGraphs3D.ShadowQuality
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::shadowQualityChanged(QtGraphs3D::
    #      ShadowQuality quality)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem20shadowQualityChangedEN10QtGraphs3D'
        '13ShadowQualityE',
        quality.value,
    )

  @overload(QtGraphs3D.TransparencyTechnique)
  def transparencyTechniqueChanged(
      self,
      technique: QtGraphs3D.TransparencyTechnique,
  ) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::transparencyTechniqueChanged(QtGraphs3D::
    TransparencyTechnique technique)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html

    Parameters
    ----------

    technique : QtGraphs3D.TransparencyTechnique
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::transparencyTechniqueChanged(QtGraphs3D::
    #      TransparencyTechnique technique)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem28transparencyTechniqueChangedEN10Qt'
        'Graphs3D21TransparencyTechniqueE',
        technique.value,
    )

  @overload(QtGraphs3D.SelectionFlags)
  def selectionModeChanged(
      self,
      selectionMode: QtGraphs3D.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::selectionModeChanged(const
    QtGraphs3D::SelectionFlags selectionMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#selectionModeChanged

    Parameters
    ----------

    selectionMode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::selectionModeChanged(const
    #      QtGraphs3D::SelectionFlags selectionMode)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem20selectionModeChangedE6QFlagsIN10Qt'
        'Graphs3D13SelectionFlagEE',
        selectionMode.value,
    )

  @overload(QtGraphs3D.ElementType)
  def selectedElementChanged(self, type: QtGraphs3D.ElementType) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::selectedElementChanged(QtGraphs3D::ElementType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#selectedElementChanged

    Parameters
    ----------

    type : QtGraphs3D.ElementType
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::selectedElementChanged(QtGraphs3D::
    #      ElementType type)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22selectedElementChangedEN10QtGraphs'
        '3D11ElementTypeE',
        type.value,
    )

  @overload(bool)
  def measureFpsChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::measureFpsChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#measureFpsChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::measureFpsChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem17measureFpsChangedEb', enabled,
    )

  @overload(int)
  def currentFpsChanged(self, fps: int) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::currentFpsChanged(int fps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#currentFpsChanged

    Parameters
    ----------

    fps : int
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::currentFpsChanged(int fps)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem17currentFpsChangedEi', fps,
    )

  @overload(bool)
  def orthoProjectionChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::orthoProjectionChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#orthoProjectionChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::orthoProjectionChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22orthoProjectionChangedEb', enabled,
    )

  @overload(float)
  def aspectRatioChanged(self, ratio: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::aspectRatioChanged(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#aspectRatioChanged

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::aspectRatioChanged(qreal ratio)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18aspectRatioChangedEd', ratio,
    )

  @overload(QtGraphs3D.OptimizationHint)
  def optimizationHintChanged(
      self,
      hint: QtGraphs3D.OptimizationHint,
  ) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::optimizationHintChanged(QtGraphs3D::OptimizationHint
    hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#optimizationHintChanged

    Parameters
    ----------

    hint : QtGraphs3D.OptimizationHint
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::optimizationHintChanged(QtGraphs3D::
    #      OptimizationHint hint)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem23optimizationHintChangedEN10QtGraph'
        's3D16OptimizationHintE',
        hint.value,
    )

  @overload(bool)
  def polarChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::polarChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#polarChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::polarChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem12polarChangedEb', enabled,
    )

  @overload(float)
  def labelMarginChanged(self, margin: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::labelMarginChanged(float margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#labelMarginChanged

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::labelMarginChanged(float margin)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18labelMarginChangedEf', margin,
    )

  @overload(float)
  def radialLabelOffsetChanged(self, offset: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::radialLabelOffsetChanged(float
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#radialLabelOffsetChanged

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::radialLabelOffsetChanged(float offset)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem24radialLabelOffsetChangedEf', offset,
    )

  @overload(float)
  def horizontalAspectRatioChanged(self, ratio: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::horizontalAspectRatioChanged(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::horizontalAspectRatioChanged(qreal ratio)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem28horizontalAspectRatioChangedEd',
        ratio,
    )

  @overload(QLocale)
  def localeChanged(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::localeChanged(const QLocale
    &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#localeChanged

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::localeChanged(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem13localeChangedERK7QLocale',
        self._valueOf(locale),
    )

  @overload(QVector3D)
  def queriedGraphPositionChanged(self, data: QVector3D) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::queriedGraphPositionChanged(QVector3D data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html

    Parameters
    ----------

    data : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::queriedGraphPositionChanged(QVector3D data)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem27queriedGraphPositionChangedE9QVect'
        'or3D',
        self._valueOf(data),
    )

  @overload(float)
  def marginChanged(self, margin: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::marginChanged(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#marginChanged

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::marginChanged(qreal margin)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem13marginChangedEd', margin,
    )

  @overload(float)
  def cutoffMarginChanged(self, newMargin: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::cutoffMarginChanged(qreal
    newMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cutoffMarginChanged

    Parameters
    ----------

    newMargin : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::cutoffMarginChanged(qreal newMargin)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem19cutoffMarginChangedEd', newMargin,
    )

  @overload(QtGraphs3D.CameraPreset)
  def cameraPresetChanged(self, preset: QtGraphs3D.CameraPreset) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::cameraPresetChanged(QtGraphs3D::CameraPreset
    preset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cameraPresetChanged

    Parameters
    ----------

    preset : QtGraphs3D.CameraPreset
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::cameraPresetChanged(QtGraphs3D::CameraPreset
    #      preset)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem19cameraPresetChangedEN10QtGraphs3D1'
        '2CameraPresetE',
        preset.value,
    )

  @overload(float)
  def cameraXRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::cameraXRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cameraXRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::cameraXRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22cameraXRotationChangedEf', rotation,
    )

  @overload(float)
  def cameraYRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::cameraYRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cameraYRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::cameraYRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22cameraYRotationChangedEf', rotation,
    )

  @overload(float)
  def cameraZoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::cameraZoomLevelChanged(float
    zoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#cameraZoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::cameraZoomLevelChanged(float zoomLevel)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22cameraZoomLevelChangedEf',
        zoomLevel,
    )

  @overload(QVector3D)
  def cameraTargetPositionChanged(self, target: QVector3D) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::cameraTargetPositionChanged(QVector3D target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html

    Parameters
    ----------

    target : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::cameraTargetPositionChanged(QVector3D
    #      target)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem27cameraTargetPositionChangedE9QVect'
        'or3D',
        self._valueOf(target),
    )

  @overload(float)
  def minCameraZoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::minCameraZoomLevelChanged(float
    zoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#minCameraZoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::minCameraZoomLevelChanged(float zoomLevel)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem25minCameraZoomLevelChangedEf',
        zoomLevel,
    )

  @overload(float)
  def maxCameraZoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::maxCameraZoomLevelChanged(float
    zoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#maxCameraZoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::maxCameraZoomLevelChanged(float zoomLevel)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem25maxCameraZoomLevelChangedEf',
        zoomLevel,
    )

  @overload(float)
  def minCameraXRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::minCameraXRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#minCameraXRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::minCameraXRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem25minCameraXRotationChangedEf',
        rotation,
    )

  @overload(float)
  def minCameraYRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::minCameraYRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#minCameraYRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::minCameraYRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem25minCameraYRotationChangedEf',
        rotation,
    )

  @overload(float)
  def maxCameraXRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::maxCameraXRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#maxCameraXRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::maxCameraXRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem25maxCameraXRotationChangedEf',
        rotation,
    )

  @overload(float)
  def maxCameraYRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::maxCameraYRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#maxCameraYRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::maxCameraYRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem25maxCameraYRotationChangedEf',
        rotation,
    )

  @overload(bool)
  def wrapCameraXRotationChanged(self, wrap: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::wrapCameraXRotationChanged(bool
    wrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::wrapCameraXRotationChanged(bool wrap)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem26wrapCameraXRotationChangedEb', wrap,
    )

  @overload(bool)
  def wrapCameraYRotationChanged(self, wrap: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::wrapCameraYRotationChanged(bool
    wrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::wrapCameraYRotationChanged(bool wrap)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem26wrapCameraYRotationChangedEb', wrap,
    )

  @overload(int)
  def msaaSamplesChanged(self, samples: int) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::msaaSamplesChanged(int samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#msaaSamplesChanged

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::msaaSamplesChanged(int samples)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18msaaSamplesChangedEi', samples,
    )

  @overload(QEventPoint, Qt.MouseButton)
  def tapped(self, eventPoint: QEventPoint, button: Qt.MouseButton) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::tapped(QEventPoint eventPoint,
    Qt::MouseButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#tapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::tapped(QEventPoint eventPoint,
    #      Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem6tappedE11QEventPointN2Qt11MouseButt'
        'onE',
        self._valueOf(eventPoint), button.value,
    )

  @overload(QEventPoint, Qt.MouseButton)
  def doubleTapped(
      self,
      eventPoint: QEventPoint,
      button: Qt.MouseButton,
  ) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::doubleTapped(QEventPoint
    eventPoint, Qt::MouseButton button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#doubleTapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::doubleTapped(QEventPoint eventPoint,
    #      Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem12doubleTappedE11QEventPointN2Qt11Mo'
        'useButtonE',
        self._valueOf(eventPoint), button.value,
    )

  def longPressed(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::longPressed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#longPressed
    """
    #  void Q3DGraphsWidgetItem::longPressed()
    self.uglySide.call('ritual_ZN19Q3DGraphsWidgetItem11longPressedEv')

  @overload(QVector2D)
  def dragged(self, delta: QVector2D) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::dragged(QVector2D delta)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#dragged

    Parameters
    ----------

    delta : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::dragged(QVector2D delta)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem7draggedE9QVector2D',
        self._valueOf(delta),
    )

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheel(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::wheel(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#wheel

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DGraphsWidgetItem::wheel(QWheelEvent *event)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem5wheelEP11QWheelEvent',
        self._addressOf(event),
    )

  @overload(float)
  def pinch(self, delta: float) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::pinch(qreal delta)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#pinch

    Parameters
    ----------

    delta : float
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::pinch(qreal delta)
    self.uglySide.call('ritual_ZN19Q3DGraphsWidgetItem5pinchEd', delta)

  @overload(QPoint)
  def mouseMove(self, mousePos: QPoint) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::mouseMove(QPoint mousePos)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#mouseMove

    Parameters
    ----------

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Q3DGraphsWidgetItem::mouseMove(QPoint mousePos)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem9mouseMoveE6QPoint',
        self._valueOf(mousePos),
    )

  @overload(bool)
  def zoomEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::zoomEnabledChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#zoomEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::zoomEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem18zoomEnabledChangedEb', enable,
    )

  @overload(bool)
  def zoomAtTargetEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::zoomAtTargetEnabledChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::zoomAtTargetEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem26zoomAtTargetEnabledChangedEb',
        enable,
    )

  @overload(bool)
  def rotationEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::rotationEnabledChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#rotationEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::rotationEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem22rotationEnabledChangedEb', enable,
    )

  @overload(bool)
  def panEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::panEnabledChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#panEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::panEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem17panEnabledChangedEb', enable,
    )

  @overload(QtGraphs3D.DragMode)
  def dragModeChanged(self, dragMode: QtGraphs3D.DragMode) -> None:
    """
    Calls Qt's 'void
    Q3DGraphsWidgetItem::dragModeChanged(QtGraphs3D::DragMode dragMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#dragModeChanged

    Parameters
    ----------

    dragMode : QtGraphs3D.DragMode
      Passed on as its number.
    """
    #  void Q3DGraphsWidgetItem::dragModeChanged(QtGraphs3D::DragMode
    #      dragMode)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem15dragModeChangedEN10QtGraphs3D8Drag'
        'ModeE',
        dragMode.value,
    )

  @overload(bool)
  def selectionEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::selectionEnabledChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#selectionEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DGraphsWidgetItem::selectionEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem23selectionEnabledChangedEb', enable,
    )

  def ambientLightStrengthChanged(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::ambientLightStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html
    """
    #  void Q3DGraphsWidgetItem::ambientLightStrengthChanged()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem27ambientLightStrengthChangedEv',
    )

  def lightStrengthChanged(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::lightStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#lightStrengthChanged
    """
    #  void Q3DGraphsWidgetItem::lightStrengthChanged()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem20lightStrengthChangedEv',
    )

  def shadowStrengthChanged(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::shadowStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#shadowStrengthChanged
    """
    #  void Q3DGraphsWidgetItem::shadowStrengthChanged()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem21shadowStrengthChangedEv',
    )

  def lightColorChanged(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::lightColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#lightColorChanged
    """
    #  void Q3DGraphsWidgetItem::lightColorChanged()
    self.uglySide.call('ritual_ZN19Q3DGraphsWidgetItem17lightColorChangedEv')

  def gridLineTypeChanged(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItem::gridLineTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#gridLineTypeChanged
    """
    #  void Q3DGraphsWidgetItem::gridLineTypeChanged()
    self.uglySide.call(
        'ritual_ZN19Q3DGraphsWidgetItem19gridLineTypeChangedEv',
    )

  def d_func(self) -> Optional[Q3DGraphsWidgetItemPrivate]:
    """
    Calls Qt's 'Q3DGraphsWidgetItemPrivate *Q3DGraphsWidgetItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dgraphswidgetitem.html#d_func

    Returns
    -------

    Optional[Q3DGraphsWidgetItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DGraphsWidgetItemPrivate *Q3DGraphsWidgetItem::d_func()
    address = self.uglySide.call('ritual_ZN19Q3DGraphsWidgetItem6d_funcEv')
    from . import Q3DGraphsWidgetItemPrivate
    return Q3DGraphsWidgetItemPrivate._cuteAt(address)

  @staticmethod
  def renderToImage(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QQuickItemGrabResult>
    Q3DGraphsWidgetItem::renderToImage(QSize imageSize) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Q3DGraphsWidgetItem.renderToImage' has no cute function yet. Qt's "
        "'QSharedPointer<QQuickItemGrabResult> "
        "Q3DGraphsWidgetItem::renderToImage(QSize imageSize) const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def setGridLineType(*__, **_) -> Never:
    """
    Qt's 'void Q3DGraphsWidgetItem::setGridLineType(const
    QtGraphs3D::GridLineType &gridLineType)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DGraphsWidgetItem.setGridLineType' has no cute function yet. "
        "Qt's 'void Q3DGraphsWidgetItem::setGridLineType(const "
        "QtGraphs3D::GridLineType &gridLineType)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def setSelectionMode(*__, **_) -> Never:
    """
    Qt's 'void Q3DGraphsWidgetItem::setSelectionMode(const
    QtGraphs3D::SelectionFlags &selectionMode)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DGraphsWidgetItem.setSelectionMode' has no cute function yet. "
        "Qt's 'void Q3DGraphsWidgetItem::setSelectionMode(const "
        "QtGraphs3D::SelectionFlags &selectionMode)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setShadowQuality(*__, **_) -> Never:
    """
    Qt's 'void Q3DGraphsWidgetItem::setShadowQuality(const
    QtGraphs3D::ShadowQuality &shadowQuality)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DGraphsWidgetItem.setShadowQuality' has no cute function yet. "
        "Qt's 'void Q3DGraphsWidgetItem::setShadowQuality(const "
        "QtGraphs3D::ShadowQuality &shadowQuality)': takes a type Python "
        "has no way to hand over yet.")
