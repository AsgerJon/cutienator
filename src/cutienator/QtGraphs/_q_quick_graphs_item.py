"""
QQuickGraphsItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickGraphsItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QStringList
from ..QtQuick import QQuickItem
from . import QtGraphs3D, QAbstract3DAxis, QGraphsTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QLocale, QMetaObject, QObject, QPoint, QPointF
  from ..QtCore import QRect, QRectF, QSizeF
  from ..QtGui import QColor, QEventPoint, QFont, QImage, QKeyEvent
  from ..QtGui import QLinearGradient, QQuaternion, QVector2D, QVector3D
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickWheelEvent, QQuickWindow
  from . import Q3DScene, QAbstract3DSeries, QCategory3DAxis, QCustom3DItem
  from . import QGraphsInputHandler, QValue3DAxis
  from ..QtQuick3D import QQuick3DCustomMaterial, QQuick3DDirectionalLight
  from ..QtQuick3D import QQuick3DModel, QQuick3DNode
  from ..QtQuick3D import QQuick3DPrincipledMaterial, QQuick3DRepeater
  from ..QtQuick3D import QQuick3DViewport
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DSeries = WAIT['QtGraphs:QAbstract3DSeries']
  QColor = WAIT['QColor']
  QCustom3DItem = WAIT['QtGraphs:QCustom3DItem']
  QEvent = WAIT['QEvent']
  QEventPoint = WAIT['QEventPoint']
  QFont = WAIT['QFont']
  QKeyEvent = WAIT['QKeyEvent']
  QLinearGradient = WAIT['QLinearGradient']
  QLocale = WAIT['QLocale']
  QObject = WAIT['QObject']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QQuaternion = WAIT['QQuaternion']
  QQuick3DModel = WAIT['QQuick3DModel']
  QQuick3DNode = WAIT['QQuick3DNode']
  QQuick3DRepeater = WAIT['QQuick3DRepeater']
  QQuick3DViewport = WAIT['QQuick3DViewport']
  QQuickWheelEvent = WAIT['QQuickWheelEvent']
  QQuickWindow = WAIT['QQuickWindow']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphsItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGraphsItem: a plain Python object standing in
  front of one C++ QQuickGraphsItem.

  What exists
  -----------

  Every function of Qt's QQuickGraphsItem that has a ritual and that Python
  can call so far, 404 names in all: 'metaObject', 'tr', 'markDataDirty',
  'markSeriesVisualsDirty', 'markSeriesItemLabelsDirty', 'emitNeedRender',
  'setQueriedGraphPosition', 'handleAxisTitleChangedBySender',
  'handleAxisLabelsChangedBySender', 'handleAxisRangeChangedBySender',
  'handleAxisSegmentCountChangedBySender',
  'handleAxisSubSegmentCountChangedBySender',
  'handleAxisAutoAdjustRangeChangedInOrientation',
  'handleAxisLabelFormatChangedBySender',
  'handleAxisReversedChangedBySender', 'handleAxisFormatterDirtyBySender',
  'handleAxisLabelAutoRotationChangedBySender',
  'handleAxisScaleLabelsByCountChangedBySender',
  'handleAxisLabelSizeChangedBySender',
  'handleAxisTitleVisibilityChangedBySender',
  'handleAxisLabelVisibilityChangedBySender',
  'handleAxisTitleFixedChangedBySender',
  'handleAxisTitleOffsetChangedBySender',
  'handleSeriesVisibilityChangedBySender', 'handleLightingModeChanged',
  'adjustAxisRanges', 'handleMultiAxisChanged', 'handleMultiAxisDirty',
  'graphPositionQueryPending', 'setGraphPositionQueryPending',
  'addSeriesInternal', 'insertSeries', 'removeSeriesInternal', 'seriesList',
  'setAxisX', 'axisX', 'setAxisY', 'axisY', 'setAxisZ', 'axisZ', 'addAxis',
  'releaseAxis', 'axes', 'setRenderingMode', 'renderingMode',
  'setTransparencyTechnique', 'transparencyTechnique', 'setSelectionMode',
  'selectionMode', 'doSetShadowQuality', 'setShadowQuality', 'shadowQuality',
  'selectedElement', 'setMsaaSamples', 'msaaSamples', 'addTheme',
  'releaseTheme', 'setTheme', 'theme', 'themes', 'isSlicingActive',
  'setSlicingActive', 'isCustomDataDirty', 'setCustomDataDirty',
  'isCustomItemDirty', 'setCustomItemDirty', 'isCustomLabelItem',
  'isCustomVolumeItem', 'customTextureImage', 'scene', 'hasSeries',
  'clearSelection', 'deleteCustomItems', 'deleteCustomItem', 'customItems',
  'addCustomItem', 'removeCustomItems', 'removeCustomItem',
  'removeCustomItemAt', 'releaseCustomItem', 'selectedLabelIndex',
  'selectedAxis', 'selectedCustomItemIndex', 'selectedCustomItem',
  'geometryChange', 'resizeViewports', 'checkWindowList', 'setMeasureFps',
  'measureFps', 'currentFps', 'setOrthoProjection', 'isOrthoProjection',
  'setAspectRatio', 'aspectRatio', 'setOptimizationHint', 'optimizationHint',
  'setPolar', 'isPolar', 'setLabelMargin', 'labelMargin',
  'setRadialLabelOffset', 'radialLabelOffset', 'setHorizontalAspectRatio',
  'horizontalAspectRatio', 'setLocale', 'locale', 'queriedGraphPosition',
  'setMargin', 'margin', 'setCutoffMargin', 'cutoffMargin', 'isReady',
  'rootNode', 'cameraTarget', 'setCameraTarget', 'background',
  'setBackground', 'backgroundBB', 'light', 'createQmlCustomMaterial',
  'createPrincipledMaterial', 'itemLabel', 'sliceItemLabel', 'repeaterX',
  'repeaterY', 'repeaterZ', 'titleLabelX', 'titleLabelY', 'titleLabelZ',
  'isXFlipped', 'setXFlipped', 'isYFlipped', 'setYFlipped', 'isZFlipped',
  'setZFlipped', 'scaleWithBackground', 'backgroundScaleMargin',
  'setScaleWithBackground', 'setBackgroundScaleMargin', 'rotation',
  'setRotation', 'scale', 'setScale', 'translate', 'setTranslate',
  'lineLengthScaleFactor', 'setLineLengthScaleFactor',
  'lineWidthScaleFactor', 'setLineWidthScaleFactor', 'gridOffset',
  'cameraPreset', 'setCameraPreset', 'cameraXRotation', 'setCameraXRotation',
  'cameraYRotation', 'setCameraYRotation', 'minCameraXRotation',
  'setMinCameraXRotation', 'maxCameraXRotation', 'setMaxCameraXRotation',
  'minCameraYRotation', 'setMinCameraYRotation', 'maxCameraYRotation',
  'setMaxCameraYRotation', 'setZoomAtTargetEnabled', 'zoomAtTargetEnabled',
  'setZoomEnabled', 'zoomEnabled', 'setSelectionEnabled', 'selectionEnabled',
  'setRotationEnabled', 'rotationEnabled', 'setPanEnabled', 'panEnabled',
  'setDragMode', 'dragMode', 'setDefaultInputHandler',
  'unsetDefaultInputHandler', 'unsetDefaultTapHandler',
  'unsetDefaultDragHandler', 'unsetDefaultWheelHandler',
  'unsetDefaultPinchHandler', 'setDragButton', 'setPanButton',
  'cameraZoomLevel', 'setCameraZoomLevel', 'minCameraZoomLevel',
  'setMinCameraZoomLevel', 'maxCameraZoomLevel', 'setMaxCameraZoomLevel',
  'setCameraTargetPosition', 'cameraTargetPosition', 'wrapCameraXRotation',
  'setWrapCameraXRotation', 'wrapCameraYRotation', 'setWrapCameraYRotation',
  'graphPositionAt', 'setCameraPosition', 'changeLabelBackgroundColor',
  'changeLabelBackgroundVisible', 'changeLabelBorderVisible',
  'changeLabelTextColor', 'changeLabelFont', 'changeLabelsVisible',
  'changeGridLineColor', 'updateTitleLabels', 'updateSelectionMode',
  'setSliceActivatedChanged', 'doPicking', 'doRayPicking',
  'minimizeMainGraph', 'horizontalFlipFactor', 'setHorizontalFlipFactor',
  'ambientLightStrength', 'setAmbientLightStrength', 'lightStrength',
  'setLightStrength', 'shadowStrength', 'setShadowStrength', 'lightColor',
  'setLightColor', 'gridLineType', 'handleAxisXChanged',
  'handleAxisYChanged', 'handleAxisZChanged', 'handleFpsChanged',
  'windowDestroyed', 'handleAxisTitleChanged', 'handleAxisLabelsChanged',
  'handleAxisRangeChanged', 'handleAxisSegmentCountChanged',
  'handleAxisSubSegmentCountChanged', 'handleAxisAutoAdjustRangeChanged',
  'handleAxisScaleLabelsByCountChanged', 'handleAxisLabelSizeChanged',
  'handleAxisLabelFormatChanged', 'handleAxisReversedChanged',
  'handleAxisFormatterDirty', 'handleAxisLabelAutoRotationChanged',
  'handleAxisTitleVisibilityChanged', 'handleAxisLabelVisibilityChanged',
  'handleAxisTitleFixedChanged', 'handleAxisTitleOffsetChanged',
  'handleInputPositionChanged', 'handleSeriesVisibilityChanged',
  'handleItemLabelVisibleChanged', 'handleItemLabelVisibleChangedBySender',
  'handleThemeColorStyleChanged', 'handleThemeBaseColorsChanged',
  'handleThemeBaseGradientsChanged',
  'handleThemeSingleHighlightColorChanged',
  'handleThemeSingleHighlightGradientChanged',
  'handleThemeMultiHighlightColorChanged',
  'handleThemeMultiHighlightGradientChanged', 'handleThemeTypeChanged',
  'handleRequestShadowQuality', 'updateCustomItem', 'selectionModeChanged',
  'shadowQualityChanged', 'shadowsSupportedChanged', 'msaaSamplesChanged',
  'themeChanged', 'renderingModeChanged', 'transparencyTechniqueChanged',
  'measureFpsChanged', 'currentFpsChanged', 'selectedElementChanged',
  'orthoProjectionChanged', 'aspectRatioChanged', 'optimizationHintChanged',
  'polarChanged', 'labelMarginChanged', 'radialLabelOffsetChanged',
  'horizontalAspectRatioChanged', 'localeChanged',
  'queriedGraphPositionChanged', 'marginChanged', 'cutoffMarginChanged',
  'cameraPresetChanged', 'cameraXRotationChanged', 'cameraYRotationChanged',
  'cameraZoomLevelChanged', 'cameraTargetPositionChanged',
  'minCameraZoomLevelChanged', 'maxCameraZoomLevelChanged',
  'minCameraXRotationChanged', 'minCameraYRotationChanged',
  'maxCameraXRotationChanged', 'maxCameraYRotationChanged',
  'wrapCameraXRotationChanged', 'wrapCameraYRotationChanged', 'needRender',
  'themeTypeChanged', 'axisXChanged', 'axisYChanged', 'axisZChanged',
  'activeThemeChanged', 'tapped', 'doubleTapped', 'longPressed', 'dragged',
  'wheel', 'pinch', 'mouseMove', 'zoomEnabledChanged',
  'zoomAtTargetEnabledChanged', 'rotationEnabledChanged',
  'panEnabledChanged', 'dragModeChanged', 'selectionEnabledChanged',
  'ambientLightStrengthChanged', 'lightStrengthChanged',
  'shadowStrengthChanged', 'lightColorChanged', 'gridLineTypeChanged',
  'event', 'setParentNode', 'handleWindowChanged', 'itemChange',
  'updateWindowParameters', 'handleSelectionModeChange',
  'handleShadowQualityChange', 'handleSelectedElementChange',
  'handleOptimizationHintChange', 'keyPressEvent', 'handleThemeTypeChange',
  'handleParentWidthChange', 'handleParentHeightChange', 'componentComplete',
  'checkSliceEnabled', 'isUserCameraRotationRange',
  'setUserCameraRotationRange', 'createSliceView',
  'createOffscreenSliceView', 'handleGraphQueryPositionChanged',
  'handleSelectionQueryPositionChanged', 'handlePrimarySubViewportChanged',
  'handleSecondarySubViewportChanged', 'graphNode', 'sliceView',
  'createRepeaterDelegateComponent', 'createRepeater', 'createTitleLabel',
  'createItemLabel', 'updateXTitle', 'updateYTitle', 'updateZTitle',
  'calculateSceneScalingFactors', 'positionAndScaleLine',
  'findLabelsMaxWidth', 'calculateCategoryLabelPosition',
  'calculateCategoryGridLinePosition', 'calculatePolarBackgroundMargin',
  'setFloorGridInRange', 'setVerticalSegmentLine', 'updateGrid',
  'updateGridLineType', 'updateLabels', 'calculateLabelRotation',
  'updateSliceGrid', 'updateSliceLabels', 'updateBackgroundColor',
  'setItemSelected', 'updateShadowQuality', 'updateItemLabel',
  'updateSliceItemLabel', 'synchData', 'updateGraph', 'isSliceEnabled',
  'setSliceEnabled', 'isSliceActivatedChanged', 'toggleSliceGraph',
  'createSliceCamera', 'isSliceOrthoProjection', 'setSliceOrthoProjection',
  'updateAxisRange', 'updateAxisReversed', 'updateSingleHighlightColor',
  'updateLightStrength', 'handleLabelCountChanged', 'updateMultiAxis',
  'updateMultiAxisLabels', 'updateMultiAxisGrid', 'releaseMultiAxis',
  'connectMultiAxis', 'getSeriesMultiAxis', 'isGridUpdated',
  'setGridUpdated', 'graphsInputHandler', 'createDefaultAxis',
  'createDefaultValueAxis', 'createDefaultCategoryAxis',
  'startRecordingRemovesAndInserts', 'setUpCamera', 'setUpLight',
  'updateCamera', 'updateRadialLabelOffset', 'updateCustomData',
  'updateCustomLabelsRotation', 'fontScaleFactor', 'labelAdjustment',
  'graphPosToAbsolute', 'updateSubViews', 'updateCustomVolumes'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickGraphsItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickGraphsItem::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuickGraphsItem::~QQuickGraphsItem()': the destructor: Python
    never removes a C++ QQuickGraphsItem.
  - Qt's 'QQmlListProperty<QCustom3DItem>
    QQuickGraphsItem::customItemList()': gives a type Python has no way to
    take yet.
  - Qt's 'void
    QQuickGraphsItem::appendCustomItemFunc(QQmlListProperty<QCustom3DItem>
    *list, QCustom3DItem *item)': names 'QQmlListProperty<QCustom3DItem>',
    which has no cute class yet.
  - Qt's 'qsizetype
    QQuickGraphsItem::countCustomItemFunc(QQmlListProperty<QCustom3DItem>
    *list)': names 'QQmlListProperty<QCustom3DItem>', which has no cute class
    yet.
  - Qt's 'QCustom3DItem
    *QQuickGraphsItem::atCustomItemFunc(QQmlListProperty<QCustom3DItem>
    *list, qsizetype index)': names 'QQmlListProperty<QCustom3DItem>', which
    has no cute class yet.
  - Qt's 'void
    QQuickGraphsItem::clearCustomItemFunc(QQmlListProperty<QCustom3DItem>
    *list)': names 'QQmlListProperty<QCustom3DItem>', which has no cute class
    yet.
  - Qt's 'void QQuickGraphsItem::setGridLineType(const
    QtGraphs3D::GridLineType &gridLineType)': takes a type Python has no way
    to hand over yet.
  - Qt's 'MultiAxis QQuickGraphsItem::getMultiAxis(qsizetype axisIndex,
    QAbstract3DAxis *axis)': gives a type Python has no way to take yet.
  - Qt's 'MultiAxis QQuickGraphsItem::createMultiAxis(qsizetype axisIndex)':
    gives a type Python has no way to take yet.
  - Qt's 'void
    QQuickGraphsItem::setAxisHelper(QAbstract3DAxis::AxisOrientation
    orientation, QAbstract3DAxis *axis, QAbstract3DAxis **axisPtr)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQuickGraphsItem::gridLineCountHelper(QAbstract3DAxis *axis,
    qsizetype &lineCount, qsizetype &sublineCount)': takes a number to change
    where it is.
  - Qt's 'void QQuickGraphsItem::createVolumeMaterial(QCustom3DVolume
    *volume, Volume &volumeItem)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQuick3DModel *QQuickGraphsItem::createSliceFrame(Volume
    &volumeItem)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickGraphsItem::updateSliceFrameMaterials(QCustom3DVolume
    *volume, Volume &volumeItem)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 426 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGraphsItem is created at the first use, not by
    'QQuickGraphsItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsItem.
  - Qt tells when it has removed the C++ QQuickGraphsItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsItem that has no cute function yet,
    'appendCustomItemFunc', 'atCustomItemFunc', 'clearCustomItemFunc',
    'countCustomItemFunc', 'createMultiAxis', 'createSliceFrame',
    'createVolumeMaterial', 'customItemList', 'getMultiAxis',
    'gridLineCountHelper', 'setAxisHelper', 'setGridLineType',
    'updateSliceFrameMaterials', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickGraphsItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#tr

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
    #  QString QQuickGraphsItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickGraphsItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphsItem'

  #  A C++ QQuickGraphsItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsItem'

  #  The functions Qt calls itself that QQuickGraphsItem is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'axes': (
          'QList<QAbstract3DAxis *> QQuickGraphsItem::axes() const',
      ),
  }

  #  The functions Qt calls itself that QQuickGraphsItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'handleAxisTitleChangedBySender': (
          ('_ZN16QQuickGraphsItem30handleAxisTitleChangedBySenderEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisLabelsChangedBySender': (
          ('_ZN16QQuickGraphsItem31handleAxisLabelsChangedBySenderEP7QObjec'
           't',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisRangeChangedBySender': (
          ('_ZN16QQuickGraphsItem30handleAxisRangeChangedBySenderEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisSegmentCountChangedBySender': (
          ('_ZN16QQuickGraphsItem37handleAxisSegmentCountChangedBySenderEP7'
           'QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisSubSegmentCountChangedBySender': (
          ('_ZN16QQuickGraphsItem40handleAxisSubSegmentCountChangedBySender'
           'EP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisAutoAdjustRangeChangedInOrientation': (
          ('_ZN16QQuickGraphsItem45handleAxisAutoAdjustRangeChangedInOrient'
           'ationEN15QAbstract3DAxis15AxisOrientationEb',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGraphs:QAbstract3DAxis.AxisOrientation'),
               ('bool', 'number', ''),
           )),
      ),
      'handleAxisLabelFormatChangedBySender': (
          ('_ZN16QQuickGraphsItem36handleAxisLabelFormatChangedBySenderEP7Q'
           'Object',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisReversedChangedBySender': (
          ('_ZN16QQuickGraphsItem33handleAxisReversedChangedBySenderEP7QObj'
           'ect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisFormatterDirtyBySender': (
          ('_ZN16QQuickGraphsItem32handleAxisFormatterDirtyBySenderEP7QObje'
           'ct',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisLabelAutoRotationChangedBySender': (
          ('_ZN16QQuickGraphsItem42handleAxisLabelAutoRotationChangedBySend'
           'erEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisScaleLabelsByCountChangedBySender': (
          ('_ZN16QQuickGraphsItem43handleAxisScaleLabelsByCountChangedBySen'
           'derEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisLabelSizeChangedBySender': (
          ('_ZN16QQuickGraphsItem34handleAxisLabelSizeChangedBySenderEP7QOb'
           'ject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisTitleVisibilityChangedBySender': (
          ('_ZN16QQuickGraphsItem40handleAxisTitleVisibilityChangedBySender'
           'EP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisLabelVisibilityChangedBySender': (
          ('_ZN16QQuickGraphsItem40handleAxisLabelVisibilityChangedBySender'
           'EP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisTitleFixedChangedBySender': (
          ('_ZN16QQuickGraphsItem35handleAxisTitleFixedChangedBySenderEP7QO'
           'bject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisTitleOffsetChangedBySender': (
          ('_ZN16QQuickGraphsItem36handleAxisTitleOffsetChangedBySenderEP7Q'
           'Object',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleSeriesVisibilityChangedBySender': (
          ('_ZN16QQuickGraphsItem37handleSeriesVisibilityChangedBySenderEP7'
           'QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleLightingModeChanged': (
          ('_ZN16QQuickGraphsItem25handleLightingModeChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'adjustAxisRanges': (
          ('_ZN16QQuickGraphsItem16adjustAxisRangesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleMultiAxisChanged': (
          ('_ZN16QQuickGraphsItem22handleMultiAxisChangedEP15QAbstract3DAxi'
           's',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           )),
      ),
      'addSeriesInternal': (
          ('_ZN16QQuickGraphsItem17addSeriesInternalEP17QAbstract3DSeries',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DSeries'),
           )),
      ),
      'removeSeriesInternal': (
          ('_ZN16QQuickGraphsItem20removeSeriesInternalEP17QAbstract3DSerie'
           's',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DSeries'),
           )),
      ),
      'addAxis': (
          ('_ZN16QQuickGraphsItem7addAxisEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           )),
      ),
      'releaseAxis': (
          ('_ZN16QQuickGraphsItem11releaseAxisEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           )),
      ),
      'setRenderingMode': (
          ('_ZN16QQuickGraphsItem16setRenderingModeEN10QtGraphs3D13Renderin'
           'gModeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGraphs:QtGraphs3D.RenderingMode'),
           )),
      ),
      'renderingMode': (
          ('_ZNK16QQuickGraphsItem13renderingModeEv',
           ('int', 'enum', 'QtGraphs:QtGraphs3D.RenderingMode'),
           ()),
      ),
      'setTransparencyTechnique': (
          ('_ZN16QQuickGraphsItem24setTransparencyTechniqueEN10QtGraphs3D21'
           'TransparencyTechniqueE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGraphs:QtGraphs3D.TransparencyTechnique'),
           )),
      ),
      'transparencyTechnique': (
          ('_ZNK16QQuickGraphsItem21transparencyTechniqueEv',
           ('int', 'enum', 'QtGraphs:QtGraphs3D.TransparencyTechnique'),
           ()),
      ),
      'setSelectionMode': (
          ('_ZN16QQuickGraphsItem16setSelectionModeE6QFlagsIN10QtGraphs3D13'
           'SelectionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtGraphs:QtGraphs3D.SelectionFlag'),
           )),
      ),
      'selectionMode': (
          ('_ZNK16QQuickGraphsItem13selectionModeEv',
           ('int', 'flags', 'QtGraphs:QtGraphs3D.SelectionFlag'),
           ()),
      ),
      'setShadowQuality': (
          ('_ZN16QQuickGraphsItem16setShadowQualityEN10QtGraphs3D13ShadowQu'
           'alityE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGraphs:QtGraphs3D.ShadowQuality'),
           )),
      ),
      'shadowQuality': (
          ('_ZNK16QQuickGraphsItem13shadowQualityEv',
           ('int', 'enum', 'QtGraphs:QtGraphs3D.ShadowQuality'),
           ()),
      ),
      'selectedElement': (
          ('_ZNK16QQuickGraphsItem15selectedElementEv',
           ('int', 'enum', 'QtGraphs:QtGraphs3D.ElementType'),
           ()),
      ),
      'setMsaaSamples': (
          ('_ZN16QQuickGraphsItem14setMsaaSamplesEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'msaaSamples': (
          ('_ZNK16QQuickGraphsItem11msaaSamplesEv',
           ('int', 'number', ''),
           ()),
      ),
      'hasSeries': (
          ('_ZN16QQuickGraphsItem9hasSeriesEP17QAbstract3DSeries',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DSeries'),
           )),
      ),
      'clearSelection': (
          ('_ZN16QQuickGraphsItem14clearSelectionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addCustomItem': (
          ('_ZN16QQuickGraphsItem13addCustomItemEP13QCustom3DItem',
           ('long long', 'number', ''),
           (
               ('address', 'address', 'QtGraphs:QCustom3DItem'),
           )),
      ),
      'removeCustomItems': (
          ('_ZN16QQuickGraphsItem17removeCustomItemsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'removeCustomItem': (
          ('_ZN16QQuickGraphsItem16removeCustomItemEP13QCustom3DItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QCustom3DItem'),
           )),
      ),
      'removeCustomItemAt': (
          ('_ZN16QQuickGraphsItem18removeCustomItemAtE9QVector3D',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QVector3D'),
           )),
      ),
      'releaseCustomItem': (
          ('_ZN16QQuickGraphsItem17releaseCustomItemEP13QCustom3DItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QCustom3DItem'),
           )),
      ),
      'selectedLabelIndex': (
          ('_ZNK16QQuickGraphsItem18selectedLabelIndexEv',
           ('int', 'number', ''),
           ()),
      ),
      'selectedAxis': (
          ('_ZNK16QQuickGraphsItem12selectedAxisEv',
           ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           ()),
      ),
      'selectedCustomItemIndex': (
          ('_ZNK16QQuickGraphsItem23selectedCustomItemIndexEv',
           ('long long', 'number', ''),
           ()),
      ),
      'selectedCustomItem': (
          ('_ZNK16QQuickGraphsItem18selectedCustomItemEv',
           ('address', 'address', 'QtGraphs:QCustom3DItem'),
           ()),
      ),
      'updateSelectionMode': (
          ('_ZN16QQuickGraphsItem19updateSelectionModeE6QFlagsIN10QtGraphs3'
           'D13SelectionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtGraphs:QtGraphs3D.SelectionFlag'),
           )),
      ),
      'doPicking': (
          ('_ZN16QQuickGraphsItem9doPickingE7QPointF',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'doRayPicking': (
          ('_ZN16QQuickGraphsItem12doRayPickingE9QVector3DS0_',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QVector3D'),
               ('address', 'value', 'QtGui:QVector3D'),
           )),
      ),
      'handleAxisXChanged': (
          ('_ZN16QQuickGraphsItem18handleAxisXChangedEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           )),
      ),
      'handleAxisYChanged': (
          ('_ZN16QQuickGraphsItem18handleAxisYChangedEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           )),
      ),
      'handleAxisZChanged': (
          ('_ZN16QQuickGraphsItem18handleAxisZChangedEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           )),
      ),
      'handleItemLabelVisibleChangedBySender': (
          ('_ZN16QQuickGraphsItem37handleItemLabelVisibleChangedBySenderEbP'
           '7QObject',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleWindowChanged': (
          ('_ZN16QQuickGraphsItem19handleWindowChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateWindowParameters': (
          ('_ZN16QQuickGraphsItem22updateWindowParametersEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleSelectionModeChange': (
          ('_ZN16QQuickGraphsItem25handleSelectionModeChangeE6QFlagsIN10QtG'
           'raphs3D13SelectionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtGraphs:QtGraphs3D.SelectionFlag'),
           )),
      ),
      'handleShadowQualityChange': (
          ('_ZN16QQuickGraphsItem25handleShadowQualityChangeEN10QtGraphs3D1'
           '3ShadowQualityE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGraphs:QtGraphs3D.ShadowQuality'),
           )),
      ),
      'handleSelectedElementChange': (
          ('_ZN16QQuickGraphsItem27handleSelectedElementChangeEN10QtGraphs3'
           'D11ElementTypeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGraphs:QtGraphs3D.ElementType'),
           )),
      ),
      'handleOptimizationHintChange': (
          ('_ZN16QQuickGraphsItem28handleOptimizationHintChangeEN10QtGraphs'
           '3D16OptimizationHintE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGraphs:QtGraphs3D.OptimizationHint'),
           )),
      ),
      'handleThemeTypeChange': (
          ('_ZN16QQuickGraphsItem21handleThemeTypeChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleParentWidthChange': (
          ('_ZN16QQuickGraphsItem23handleParentWidthChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleParentHeightChange': (
          ('_ZN16QQuickGraphsItem24handleParentHeightChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'createSliceView': (
          ('_ZN16QQuickGraphsItem15createSliceViewEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'calculateSceneScalingFactors': (
          ('_ZN16QQuickGraphsItem28calculateSceneScalingFactorsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'calculateCategoryLabelPosition': (
          ('_ZN16QQuickGraphsItem30calculateCategoryLabelPositionEP15QAbstr'
           'act3DAxis9QVector3Di',
           ('address', 'value', 'QtGui:QVector3D'),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
               ('address', 'value', 'QtGui:QVector3D'),
               ('int', 'number', ''),
           )),
      ),
      'calculateCategoryGridLinePosition': (
          ('_ZN16QQuickGraphsItem33calculateCategoryGridLinePositionEP15QAb'
           'stract3DAxisi',
           ('float', 'number', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
               ('int', 'number', ''),
           )),
      ),
      'updateShadowQuality': (
          ('_ZN16QQuickGraphsItem19updateShadowQualityEN10QtGraphs3D13Shado'
           'wQualityE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGraphs:QtGraphs3D.ShadowQuality'),
           )),
      ),
      'updateSliceItemLabel': (
          ('_ZN16QQuickGraphsItem20updateSliceItemLabelERK7QString9QVector3'
           'D',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtGui:QVector3D'),
           )),
      ),
      'synchData': (
          ('_ZN16QQuickGraphsItem9synchDataEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateGraph': (
          ('_ZN16QQuickGraphsItem11updateGraphEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'toggleSliceGraph': (
          ('_ZN16QQuickGraphsItem16toggleSliceGraphEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateAxisRange': (
          ('_ZN16QQuickGraphsItem15updateAxisRangeEff',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
               ('float', 'number', ''),
           )),
      ),
      'updateAxisReversed': (
          ('_ZN16QQuickGraphsItem18updateAxisReversedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'updateSingleHighlightColor': (
          ('_ZN16QQuickGraphsItem26updateSingleHighlightColorEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateLightStrength': (
          ('_ZN16QQuickGraphsItem19updateLightStrengthEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleLabelCountChanged': (
          ('_ZN16QQuickGraphsItem23handleLabelCountChangedEP16QQuick3DRepea'
           'ter6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick3D:QQuick3DRepeater'),
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'getSeriesMultiAxis': (
          ('_ZN16QQuickGraphsItem18getSeriesMultiAxisEP17QAbstract3DSeriesN'
           '15QAbstract3DAxis15AxisOrientationE',
           ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DSeries'),
               ('int', 'enum', 'QtGraphs:QAbstract3DAxis.AxisOrientation'),
           )),
      ),
      'createDefaultAxis': (
          ('_ZN16QQuickGraphsItem17createDefaultAxisEN15QAbstract3DAxis15Ax'
           'isOrientationE',
           ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           (
               ('int', 'enum', 'QtGraphs:QAbstract3DAxis.AxisOrientation'),
           )),
      ),
      'startRecordingRemovesAndInserts': (
          ('_ZN16QQuickGraphsItem31startRecordingRemovesAndInsertsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def graphPositionQueryPending(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::graphPositionQueryPending() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#graphPositionQueryPending
    """
    #  bool QQuickGraphsItem::graphPositionQueryPending() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem25graphPositionQueryPendingEv',
    )

  def axisX(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *QQuickGraphsItem::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#axisX

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *QQuickGraphsItem::axisX() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem5axisXEv')
    return QAbstract3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *QQuickGraphsItem::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#axisY

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *QQuickGraphsItem::axisY() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem5axisYEv')
    return QAbstract3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *QQuickGraphsItem::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#axisZ

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *QQuickGraphsItem::axisZ() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem5axisZEv')
    return QAbstract3DAxis._cuteAt(address)

  def axes(self) -> QList[QAbstract3DAxis]:
    """
    Calls Qt's 'QList<QAbstract3DAxis *> QQuickGraphsItem::axes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#axes

    Returns
    -------

    QList[QAbstract3DAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DAxis *> QQuickGraphsItem::axes() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem4axesEv')
    return QList[QAbstract3DAxis]._cuteOwning(address)

  def renderingMode(self) -> QtGraphs3D.RenderingMode:
    """
    Calls Qt's 'QtGraphs3D::RenderingMode QQuickGraphsItem::renderingMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#renderingMode

    Returns
    -------

    QtGraphs3D.RenderingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.RenderingMode(number)' gives.
    """
    #  QtGraphs3D::RenderingMode QQuickGraphsItem::renderingMode() const
    ritual = 'ritual_ZNK16QQuickGraphsItem13renderingModeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem13renderingModeEv'
    return QtGraphs3D.RenderingMode(self.uglySide.call(ritual))

  def transparencyTechnique(self) -> QtGraphs3D.TransparencyTechnique:
    """
    Calls Qt's 'QtGraphs3D::TransparencyTechnique
    QQuickGraphsItem::transparencyTechnique() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#transparencyTechnique

    Returns
    -------

    QtGraphs3D.TransparencyTechnique
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.TransparencyTechnique(number)' gives.
    """
    #  QtGraphs3D::TransparencyTechnique
    #      QQuickGraphsItem::transparencyTechnique() const
    ritual = 'ritual_ZNK16QQuickGraphsItem21transparencyTechniqueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem21transparencyTechniqueEv'
    return QtGraphs3D.TransparencyTechnique(self.uglySide.call(ritual))

  def selectionMode(self) -> QtGraphs3D.SelectionFlags:
    """
    Calls Qt's 'QtGraphs3D::SelectionFlags QQuickGraphsItem::selectionMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#selectionMode

    Returns
    -------

    QtGraphs3D.SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  QtGraphs3D::SelectionFlags QQuickGraphsItem::selectionMode() const
    ritual = 'ritual_ZNK16QQuickGraphsItem13selectionModeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem13selectionModeEv'
    return QtGraphs3D.SelectionFlags(self.uglySide.call(ritual))

  def shadowQuality(self) -> QtGraphs3D.ShadowQuality:
    """
    Calls Qt's 'QtGraphs3D::ShadowQuality QQuickGraphsItem::shadowQuality()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#shadowQuality

    Returns
    -------

    QtGraphs3D.ShadowQuality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.ShadowQuality(number)' gives.
    """
    #  QtGraphs3D::ShadowQuality QQuickGraphsItem::shadowQuality() const
    ritual = 'ritual_ZNK16QQuickGraphsItem13shadowQualityEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem13shadowQualityEv'
    return QtGraphs3D.ShadowQuality(self.uglySide.call(ritual))

  def selectedElement(self) -> QtGraphs3D.ElementType:
    """
    Calls Qt's 'QtGraphs3D::ElementType QQuickGraphsItem::selectedElement()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#selectedElement

    Returns
    -------

    QtGraphs3D.ElementType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.ElementType(number)' gives.
    """
    #  QtGraphs3D::ElementType QQuickGraphsItem::selectedElement() const
    ritual = 'ritual_ZNK16QQuickGraphsItem15selectedElementEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem15selectedElementEv'
    return QtGraphs3D.ElementType(self.uglySide.call(ritual))

  def msaaSamples(self) -> int:
    """
    Calls Qt's 'int QQuickGraphsItem::msaaSamples() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#msaaSamples
    """
    #  int QQuickGraphsItem::msaaSamples() const
    ritual = 'ritual_ZNK16QQuickGraphsItem11msaaSamplesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem11msaaSamplesEv'
    return self.uglySide.call(ritual)

  def theme(self) -> Optional[QGraphsTheme]:
    """
    Calls Qt's 'QGraphsTheme *QQuickGraphsItem::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#theme

    Returns
    -------

    Optional[QGraphsTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphsTheme *QQuickGraphsItem::theme() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem5themeEv')
    return QGraphsTheme._cuteAt(address)

  def themes(self) -> QList[QGraphsTheme]:
    """
    Calls Qt's 'QList<QGraphsTheme *> QQuickGraphsItem::themes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#themes

    Returns
    -------

    QList[QGraphsTheme]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphsTheme *> QQuickGraphsItem::themes() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem6themesEv')
    return QList[QGraphsTheme]._cuteOwning(address)

  def isSlicingActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isSlicingActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isSlicingActive
    """
    #  bool QQuickGraphsItem::isSlicingActive() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem15isSlicingActiveEv',
    )

  def isCustomDataDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isCustomDataDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isCustomDataDirty
    """
    #  bool QQuickGraphsItem::isCustomDataDirty() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem17isCustomDataDirtyEv',
    )

  def isCustomItemDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isCustomItemDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isCustomItemDirty
    """
    #  bool QQuickGraphsItem::isCustomItemDirty() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem17isCustomItemDirtyEv',
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def isCustomLabelItem(self, item: Optional[QCustom3DItem]) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isCustomLabelItem(QCustom3DItem *item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isCustomLabelItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickGraphsItem::isCustomLabelItem(QCustom3DItem *item) const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem17isCustomLabelItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def isCustomVolumeItem(self, item: Optional[QCustom3DItem]) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isCustomVolumeItem(QCustom3DItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isCustomVolumeItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickGraphsItem::isCustomVolumeItem(QCustom3DItem *item) const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem18isCustomVolumeItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  def customItems(self) -> QList[QCustom3DItem]:
    """
    Calls Qt's 'QList<QCustom3DItem *> QQuickGraphsItem::customItems()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#customItems

    Returns
    -------

    QList[QCustom3DItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCustom3DItem *> QQuickGraphsItem::customItems() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem11customItemsEv',
    )
    from . import QCustom3DItem
    return QList[QCustom3DItem]._cuteOwning(address)

  def selectedLabelIndex(self) -> int:
    """
    Calls Qt's 'int QQuickGraphsItem::selectedLabelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#selectedLabelIndex
    """
    #  int QQuickGraphsItem::selectedLabelIndex() const
    ritual = 'ritual_ZNK16QQuickGraphsItem18selectedLabelIndexEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem18selectedLabelIndexEv'
    return self.uglySide.call(ritual)

  def selectedAxis(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *QQuickGraphsItem::selectedAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#selectedAxis

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *QQuickGraphsItem::selectedAxis() const
    ritual = 'ritual_ZNK16QQuickGraphsItem12selectedAxisEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem12selectedAxisEv'
    address = self.uglySide.call(ritual)
    return QAbstract3DAxis._cuteAt(address)

  def selectedCustomItemIndex(self) -> int:
    """
    Calls Qt's 'qsizetype QQuickGraphsItem::selectedCustomItemIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#selectedCustomItemIndex
    """
    #  qsizetype QQuickGraphsItem::selectedCustomItemIndex() const
    ritual = 'ritual_ZNK16QQuickGraphsItem23selectedCustomItemIndexEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem23selectedCustomItemIndexEv'
    return self.uglySide.call(ritual)

  def selectedCustomItem(self) -> Optional[QCustom3DItem]:
    """
    Calls Qt's 'QCustom3DItem *QQuickGraphsItem::selectedCustomItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#selectedCustomItem

    Returns
    -------

    Optional[QCustom3DItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DItem *QQuickGraphsItem::selectedCustomItem() const
    ritual = 'ritual_ZNK16QQuickGraphsItem18selectedCustomItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsItem18selectedCustomItemEv'
    address = self.uglySide.call(ritual)
    from . import QCustom3DItem
    return QCustom3DItem._cuteAt(address)

  def measureFps(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::measureFps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#measureFps
    """
    #  bool QQuickGraphsItem::measureFps() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem10measureFpsEv')

  def currentFps(self) -> int:
    """
    Calls Qt's 'int QQuickGraphsItem::currentFps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#currentFps
    """
    #  int QQuickGraphsItem::currentFps() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem10currentFpsEv')

  def isOrthoProjection(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isOrthoProjection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isOrthoProjection
    """
    #  bool QQuickGraphsItem::isOrthoProjection() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem17isOrthoProjectionEv',
    )

  def aspectRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickGraphsItem::aspectRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#aspectRatio
    """
    #  qreal QQuickGraphsItem::aspectRatio() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem11aspectRatioEv')

  def optimizationHint(self) -> QtGraphs3D.OptimizationHint:
    """
    Calls Qt's 'QtGraphs3D::OptimizationHint
    QQuickGraphsItem::optimizationHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#optimizationHint

    Returns
    -------

    QtGraphs3D.OptimizationHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.OptimizationHint(number)' gives.
    """
    #  QtGraphs3D::OptimizationHint QQuickGraphsItem::optimizationHint()
    #      const
    return QtGraphs3D.OptimizationHint(self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem16optimizationHintEv',
    ))

  def isPolar(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isPolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#isPolar
    """
    #  bool QQuickGraphsItem::isPolar() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem7isPolarEv')

  def labelMargin(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::labelMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#labelMargin
    """
    #  float QQuickGraphsItem::labelMargin() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem11labelMarginEv')

  def radialLabelOffset(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::radialLabelOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#radialLabelOffset
    """
    #  float QQuickGraphsItem::radialLabelOffset() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem17radialLabelOffsetEv',
    )

  def horizontalAspectRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickGraphsItem::horizontalAspectRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#horizontalAspectRatio
    """
    #  qreal QQuickGraphsItem::horizontalAspectRatio() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem21horizontalAspectRatioEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QQuickGraphsItem::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QQuickGraphsItem::locale() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def queriedGraphPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::queriedGraphPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#queriedGraphPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::queriedGraphPosition() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem20queriedGraphPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def margin(self) -> float:
    """
    Calls Qt's 'qreal QQuickGraphsItem::margin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#margin
    """
    #  qreal QQuickGraphsItem::margin() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem6marginEv')

  def cutoffMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickGraphsItem::cutoffMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#cutoffMargin
    """
    #  qreal QQuickGraphsItem::cutoffMargin() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem12cutoffMarginEv')

  def rootNode(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuickGraphsItem::rootNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#rootNode

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuickGraphsItem::rootNode() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem8rootNodeEv')
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def background(self) -> Optional[QQuick3DModel]:
    """
    Calls Qt's 'QQuick3DModel *QQuickGraphsItem::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#background

    Returns
    -------

    Optional[QQuick3DModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DModel *QQuickGraphsItem::background() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem10backgroundEv',
    )
    from ..QtQuick3D import QQuick3DModel
    return QQuick3DModel._cuteAt(address)

  def backgroundBB(self) -> Optional[QQuick3DModel]:
    """
    Calls Qt's 'QQuick3DModel *QQuickGraphsItem::backgroundBB() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#backgroundBB

    Returns
    -------

    Optional[QQuick3DModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DModel *QQuickGraphsItem::backgroundBB() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem12backgroundBBEv',
    )
    from ..QtQuick3D import QQuick3DModel
    return QQuick3DModel._cuteAt(address)

  def light(self) -> Optional[QQuick3DDirectionalLight]:
    """
    Calls Qt's 'QQuick3DDirectionalLight *QQuickGraphsItem::light() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#light

    Returns
    -------

    Optional[QQuick3DDirectionalLight]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DDirectionalLight *QQuickGraphsItem::light() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem5lightEv')
    from ..QtQuick3D import QQuick3DDirectionalLight
    return QQuick3DDirectionalLight._cuteAt(address)

  def repeaterX(self) -> Optional[QQuick3DRepeater]:
    """
    Calls Qt's 'QQuick3DRepeater *QQuickGraphsItem::repeaterX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#repeaterX

    Returns
    -------

    Optional[QQuick3DRepeater]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRepeater *QQuickGraphsItem::repeaterX() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem9repeaterXEv')
    from ..QtQuick3D import QQuick3DRepeater
    return QQuick3DRepeater._cuteAt(address)

  def repeaterY(self) -> Optional[QQuick3DRepeater]:
    """
    Calls Qt's 'QQuick3DRepeater *QQuickGraphsItem::repeaterY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#repeaterY

    Returns
    -------

    Optional[QQuick3DRepeater]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRepeater *QQuickGraphsItem::repeaterY() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem9repeaterYEv')
    from ..QtQuick3D import QQuick3DRepeater
    return QQuick3DRepeater._cuteAt(address)

  def repeaterZ(self) -> Optional[QQuick3DRepeater]:
    """
    Calls Qt's 'QQuick3DRepeater *QQuickGraphsItem::repeaterZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#repeaterZ

    Returns
    -------

    Optional[QQuick3DRepeater]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRepeater *QQuickGraphsItem::repeaterZ() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem9repeaterZEv')
    from ..QtQuick3D import QQuick3DRepeater
    return QQuick3DRepeater._cuteAt(address)

  def titleLabelX(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuickGraphsItem::titleLabelX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#titleLabelX

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuickGraphsItem::titleLabelX() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem11titleLabelXEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def titleLabelY(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuickGraphsItem::titleLabelY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#titleLabelY

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuickGraphsItem::titleLabelY() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem11titleLabelYEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def titleLabelZ(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuickGraphsItem::titleLabelZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#titleLabelZ

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuickGraphsItem::titleLabelZ() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem11titleLabelZEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def isXFlipped(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isXFlipped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#isXFlipped
    """
    #  bool QQuickGraphsItem::isXFlipped() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem10isXFlippedEv')

  def isYFlipped(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isYFlipped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#isYFlipped
    """
    #  bool QQuickGraphsItem::isYFlipped() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem10isYFlippedEv')

  def isZFlipped(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isZFlipped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#isZFlipped
    """
    #  bool QQuickGraphsItem::isZFlipped() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem10isZFlippedEv')

  def scaleWithBackground(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::scaleWithBackground() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#scaleWithBackground

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::scaleWithBackground() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem19scaleWithBackgroundEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def backgroundScaleMargin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::backgroundScaleMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#backgroundScaleMargin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::backgroundScaleMargin() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem21backgroundScaleMarginEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#rotation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::rotation() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem8rotationEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def scale(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#scale

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::scale() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem5scaleEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def translate(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::translate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#translate

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::translate() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsItem9translateEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def lineLengthScaleFactor(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::lineLengthScaleFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#lineLengthScaleFactor
    """
    #  float QQuickGraphsItem::lineLengthScaleFactor() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem21lineLengthScaleFactorEv',
    )

  def lineWidthScaleFactor(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::lineWidthScaleFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#lineWidthScaleFactor
    """
    #  float QQuickGraphsItem::lineWidthScaleFactor() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem20lineWidthScaleFactorEv',
    )

  def gridOffset(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::gridOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#gridOffset
    """
    #  float QQuickGraphsItem::gridOffset() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsItem10gridOffsetEv')

  def cameraPreset(self) -> QtGraphs3D.CameraPreset:
    """
    Calls Qt's 'QtGraphs3D::CameraPreset QQuickGraphsItem::cameraPreset()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraPreset

    Returns
    -------

    QtGraphs3D.CameraPreset
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.CameraPreset(number)' gives.
    """
    #  QtGraphs3D::CameraPreset QQuickGraphsItem::cameraPreset() const
    return QtGraphs3D.CameraPreset(self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem12cameraPresetEv',
    ))

  def cameraXRotation(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::cameraXRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraXRotation
    """
    #  float QQuickGraphsItem::cameraXRotation() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem15cameraXRotationEv',
    )

  def cameraYRotation(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::cameraYRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraYRotation
    """
    #  float QQuickGraphsItem::cameraYRotation() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem15cameraYRotationEv',
    )

  def minCameraXRotation(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::minCameraXRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#minCameraXRotation
    """
    #  float QQuickGraphsItem::minCameraXRotation() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem18minCameraXRotationEv',
    )

  def maxCameraXRotation(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::maxCameraXRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#maxCameraXRotation
    """
    #  float QQuickGraphsItem::maxCameraXRotation() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem18maxCameraXRotationEv',
    )

  def minCameraYRotation(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::minCameraYRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#minCameraYRotation
    """
    #  float QQuickGraphsItem::minCameraYRotation() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem18minCameraYRotationEv',
    )

  def maxCameraYRotation(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::maxCameraYRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#maxCameraYRotation
    """
    #  float QQuickGraphsItem::maxCameraYRotation() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem18maxCameraYRotationEv',
    )

  def dragMode(self) -> QtGraphs3D.DragMode:
    """
    Calls Qt's 'QtGraphs3D::DragMode QQuickGraphsItem::dragMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#dragMode

    Returns
    -------

    QtGraphs3D.DragMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.DragMode(number)' gives.
    """
    #  QtGraphs3D::DragMode QQuickGraphsItem::dragMode() const
    return QtGraphs3D.DragMode(self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem8dragModeEv',
    ))

  def cameraZoomLevel(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::cameraZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraZoomLevel
    """
    #  float QQuickGraphsItem::cameraZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem15cameraZoomLevelEv',
    )

  def minCameraZoomLevel(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::minCameraZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#minCameraZoomLevel
    """
    #  float QQuickGraphsItem::minCameraZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem18minCameraZoomLevelEv',
    )

  def maxCameraZoomLevel(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::maxCameraZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#maxCameraZoomLevel
    """
    #  float QQuickGraphsItem::maxCameraZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem18maxCameraZoomLevelEv',
    )

  def cameraTargetPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::cameraTargetPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraTargetPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::cameraTargetPosition() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem20cameraTargetPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def wrapCameraXRotation(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::wrapCameraXRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#wrapCameraXRotation
    """
    #  bool QQuickGraphsItem::wrapCameraXRotation() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem19wrapCameraXRotationEv',
    )

  def wrapCameraYRotation(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::wrapCameraYRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#wrapCameraYRotation
    """
    #  bool QQuickGraphsItem::wrapCameraYRotation() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem19wrapCameraYRotationEv',
    )

  def horizontalFlipFactor(self) -> int:
    """
    Calls Qt's 'int QQuickGraphsItem::horizontalFlipFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#horizontalFlipFactor
    """
    #  int QQuickGraphsItem::horizontalFlipFactor() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem20horizontalFlipFactorEv',
    )

  def ambientLightStrength(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::ambientLightStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#ambientLightStrength
    """
    #  float QQuickGraphsItem::ambientLightStrength() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem20ambientLightStrengthEv',
    )

  def lightStrength(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::lightStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#lightStrength
    """
    #  float QQuickGraphsItem::lightStrength() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem13lightStrengthEv',
    )

  def shadowStrength(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::shadowStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#shadowStrength
    """
    #  float QQuickGraphsItem::shadowStrength() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem14shadowStrengthEv',
    )

  def lightColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickGraphsItem::lightColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#lightColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickGraphsItem::lightColor() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem10lightColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def gridLineType(self) -> QtGraphs3D.GridLineType:
    """
    Calls Qt's 'QtGraphs3D::GridLineType QQuickGraphsItem::gridLineType()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#gridLineType

    Returns
    -------

    QtGraphs3D.GridLineType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.GridLineType(number)' gives.
    """
    #  QtGraphs3D::GridLineType QQuickGraphsItem::gridLineType() const
    return QtGraphs3D.GridLineType(self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem12gridLineTypeEv',
    ))

  def isSliceEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isSliceEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isSliceEnabled
    """
    #  bool QQuickGraphsItem::isSliceEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem14isSliceEnabledEv',
    )

  def isSliceActivatedChanged(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isSliceActivatedChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isSliceActivatedChanged
    """
    #  bool QQuickGraphsItem::isSliceActivatedChanged() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem23isSliceActivatedChangedEv',
    )

  def isSliceOrthoProjection(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isSliceOrthoProjection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isSliceOrthoProjection
    """
    #  bool QQuickGraphsItem::isSliceOrthoProjection() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem22isSliceOrthoProjectionEv',
    )

  def graphsInputHandler(self) -> Optional[QGraphsInputHandler]:
    """
    Calls Qt's 'QGraphsInputHandler *QQuickGraphsItem::graphsInputHandler()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#graphsInputHandler

    Returns
    -------

    Optional[QGraphsInputHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphsInputHandler *QQuickGraphsItem::graphsInputHandler() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsItem18graphsInputHandlerEv',
    )
    from . import QGraphsInputHandler
    return QGraphsInputHandler._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setQueriedGraphPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setQueriedGraphPosition(QVector3D
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setQueriedGraphPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::setQueriedGraphPosition(QVector3D position)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23setQueriedGraphPositionE9QVector3D',
        self._valueOf(position),
    )

  @overload(bool)
  def setGraphPositionQueryPending(self, pending: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setGraphPositionQueryPending(const
    bool &pending)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setGraphPositionQueryPending

    Parameters
    ----------

    pending : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setGraphPositionQueryPending(const bool
    #      &pending)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem28setGraphPositionQueryPendingERKb',
        pending,
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setAxisX(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::setAxisX(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem8setAxisXEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setAxisY(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::setAxisY(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem8setAxisYEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setAxisZ(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::setAxisZ(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem8setAxisZEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QtGraphs3D.RenderingMode)
  def setRenderingMode(self, mode: QtGraphs3D.RenderingMode) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::setRenderingMode(QtGraphs3D::RenderingMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setRenderingMode

    Parameters
    ----------

    mode : QtGraphs3D.RenderingMode
      Passed on as its number.
    """
    #  void QQuickGraphsItem::setRenderingMode(QtGraphs3D::RenderingMode
    #      mode)
    ritual = (
        'ritual_ZN16QQuickGraphsItem16setRenderingModeEN10QtGraphs3D13Rende'
        'ringModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem16setRenderingModeEN10QtGraphs3D1'
          '3RenderingModeE')
    self.uglySide.call(ritual, mode.value)

  @overload(QtGraphs3D.TransparencyTechnique)
  def setTransparencyTechnique(
      self,
      technique: QtGraphs3D.TransparencyTechnique,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setTransparencyTechnique(QtGraphs3D::
    TransparencyTechnique technique)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setTransparencyTechnique

    Parameters
    ----------

    technique : QtGraphs3D.TransparencyTechnique
      Passed on as its number.
    """
    #  void QQuickGraphsItem::setTransparencyTechnique(QtGraphs3D::
    #      TransparencyTechnique technique)
    ritual = (
        'ritual_ZN16QQuickGraphsItem24setTransparencyTechniqueEN10QtGraphs3'
        'D21TransparencyTechniqueE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem24setTransparencyTechniqueEN10QtG'
          'raphs3D21TransparencyTechniqueE')
    self.uglySide.call(ritual, technique.value)

  @overload(QtGraphs3D.SelectionFlags)
  def setSelectionMode(self, mode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::setSelectionMode(QtGraphs3D::SelectionFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setSelectionMode

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsItem::setSelectionMode(QtGraphs3D::SelectionFlags
    #      mode)
    ritual = (
        'ritual_ZN16QQuickGraphsItem16setSelectionModeE6QFlagsIN10QtGraphs3'
        'D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem16setSelectionModeE6QFlagsIN10QtG'
          'raphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(QtGraphs3D.ShadowQuality)
  def setShadowQuality(self, quality: QtGraphs3D.ShadowQuality) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::setShadowQuality(QtGraphs3D::ShadowQuality quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setShadowQuality

    Parameters
    ----------

    quality : QtGraphs3D.ShadowQuality
      Passed on as its number.
    """
    #  void QQuickGraphsItem::setShadowQuality(QtGraphs3D::ShadowQuality
    #      quality)
    ritual = (
        'ritual_ZN16QQuickGraphsItem16setShadowQualityEN10QtGraphs3D13Shado'
        'wQualityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem16setShadowQualityEN10QtGraphs3D1'
          '3ShadowQualityE')
    self.uglySide.call(ritual, quality.value)

  @overload(int)
  def setMsaaSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setMsaaSamples(int samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setMsaaSamples

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setMsaaSamples(int samples)
    ritual = 'ritual_ZN16QQuickGraphsItem14setMsaaSamplesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem14setMsaaSamplesEi'
    self.uglySide.call(ritual, samples)

  @overload(QGraphsTheme)
  @overload(NoneType)
  def setTheme(self, theme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setTheme(QGraphsTheme *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setTheme

    Parameters
    ----------

    theme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::setTheme(QGraphsTheme *theme)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem8setThemeEP12QGraphsTheme',
        self._addressOf(theme),
    )

  @overload(bool)
  def setSlicingActive(self, isSlicing: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setSlicingActive(bool isSlicing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setSlicingActive

    Parameters
    ----------

    isSlicing : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setSlicingActive(bool isSlicing)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem16setSlicingActiveEb', isSlicing,
    )

  @overload(bool)
  def setCustomDataDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setCustomDataDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCustomDataDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setCustomDataDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18setCustomDataDirtyEb', dirty,
    )

  @overload(bool)
  def setCustomItemDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setCustomItemDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCustomItemDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setCustomItemDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18setCustomItemDirtyEb', dirty,
    )

  @overload(bool)
  def setMeasureFps(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setMeasureFps(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setMeasureFps

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setMeasureFps(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem13setMeasureFpsEb', enable,
    )

  @overload(bool)
  def setOrthoProjection(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setOrthoProjection(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setOrthoProjection

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setOrthoProjection(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18setOrthoProjectionEb', enable,
    )

  @overload(float)
  def setAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setAspectRatio(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setAspectRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem14setAspectRatioEd', ratio,
    )

  @overload(QtGraphs3D.OptimizationHint)
  def setOptimizationHint(self, hint: QtGraphs3D.OptimizationHint) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::setOptimizationHint(QtGraphs3D::OptimizationHint
    hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setOptimizationHint

    Parameters
    ----------

    hint : QtGraphs3D.OptimizationHint
      Passed on as its number.
    """
    #  void
    #      QQuickGraphsItem::setOptimizationHint(QtGraphs3D::OptimizationHint
    #      hint)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem19setOptimizationHintEN10QtGraphs3D16Op'
        'timizationHintE',
        hint.value,
    )

  @overload(bool)
  def setPolar(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setPolar(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setPolar

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setPolar(bool enable)
    self.uglySide.call('ritual_ZN16QQuickGraphsItem8setPolarEb', enable)

  @overload(float)
  def setLabelMargin(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setLabelMargin(float offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setLabelMargin

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setLabelMargin(float offset)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem14setLabelMarginEf', offset,
    )

  @overload(float)
  def setRadialLabelOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setRadialLabelOffset(float offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setRadialLabelOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setRadialLabelOffset(float offset)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem20setRadialLabelOffsetEf', offset,
    )

  @overload(float)
  def setHorizontalAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setHorizontalAspectRatio(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setHorizontalAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setHorizontalAspectRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24setHorizontalAspectRatioEd', ratio,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(float)
  def setMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setMargin(qreal margin)
    self.uglySide.call('ritual_ZN16QQuickGraphsItem9setMarginEd', margin)

  @overload(float)
  def setCutoffMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setCutoffMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCutoffMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setCutoffMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15setCutoffMarginEd', margin,
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setCameraTarget(self, target: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setCameraTarget(QQuick3DNode
    *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCameraTarget

    Parameters
    ----------

    target : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::setCameraTarget(QQuick3DNode *target)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15setCameraTargetEP12QQuick3DNode',
        self._addressOf(target),
    )

  @overload(QQuick3DModel)
  @overload(NoneType)
  def setBackground(self, newBackground: Optional[QQuick3DModel]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setBackground(QQuick3DModel
    *newBackground)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setBackground

    Parameters
    ----------

    newBackground : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::setBackground(QQuick3DModel *newBackground)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem13setBackgroundEP13QQuick3DModel',
        self._addressOf(newBackground),
    )

  @overload(bool)
  def setXFlipped(self, xFlipped: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setXFlipped(bool xFlipped)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setXFlipped

    Parameters
    ----------

    xFlipped : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setXFlipped(bool xFlipped)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem11setXFlippedEb', xFlipped,
    )

  @overload(bool)
  def setYFlipped(self, yFlipped: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setYFlipped(bool yFlipped)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setYFlipped

    Parameters
    ----------

    yFlipped : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setYFlipped(bool yFlipped)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem11setYFlippedEb', yFlipped,
    )

  @overload(bool)
  def setZFlipped(self, zFlipped: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setZFlipped(bool zFlipped)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setZFlipped

    Parameters
    ----------

    zFlipped : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setZFlipped(bool zFlipped)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem11setZFlippedEb', zFlipped,
    )

  @overload(QVector3D)
  def setScaleWithBackground(self, scale: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setScaleWithBackground(QVector3D
    scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setScaleWithBackground

    Parameters
    ----------

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::setScaleWithBackground(QVector3D scale)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22setScaleWithBackgroundE9QVector3D',
        self._valueOf(scale),
    )

  @overload(QVector3D)
  def setBackgroundScaleMargin(self, margin: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setBackgroundScaleMargin(QVector3D
    margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setBackgroundScaleMargin

    Parameters
    ----------

    margin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::setBackgroundScaleMargin(QVector3D margin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24setBackgroundScaleMarginE9QVector3D',
        self._valueOf(margin),
    )

  @overload(QVector3D)
  def setRotation(self, rotation: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setRotation(QVector3D rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setRotation

    Parameters
    ----------

    rotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::setRotation(QVector3D rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem11setRotationE9QVector3D',
        self._valueOf(rotation),
    )

  @overload(QVector3D)
  def setScale(self, scale: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setScale(QVector3D scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setScale

    Parameters
    ----------

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::setScale(QVector3D scale)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem8setScaleE9QVector3D',
        self._valueOf(scale),
    )

  @overload(QVector3D)
  def setTranslate(self, translate: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setTranslate(QVector3D translate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setTranslate

    Parameters
    ----------

    translate : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::setTranslate(QVector3D translate)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12setTranslateE9QVector3D',
        self._valueOf(translate),
    )

  @overload(float)
  def setLineLengthScaleFactor(self, scaleFactor: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setLineLengthScaleFactor(float
    scaleFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setLineLengthScaleFactor

    Parameters
    ----------

    scaleFactor : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setLineLengthScaleFactor(float scaleFactor)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24setLineLengthScaleFactorEf',
        scaleFactor,
    )

  @overload(float)
  def setLineWidthScaleFactor(self, scaleFactor: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setLineWidthScaleFactor(float
    scaleFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setLineWidthScaleFactor

    Parameters
    ----------

    scaleFactor : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setLineWidthScaleFactor(float scaleFactor)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23setLineWidthScaleFactorEf',
        scaleFactor,
    )

  @overload(QtGraphs3D.CameraPreset)
  def setCameraPreset(self, preset: QtGraphs3D.CameraPreset) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::setCameraPreset(QtGraphs3D::CameraPreset preset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCameraPreset

    Parameters
    ----------

    preset : QtGraphs3D.CameraPreset
      Passed on as its number.
    """
    #  void QQuickGraphsItem::setCameraPreset(QtGraphs3D::CameraPreset
    #      preset)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15setCameraPresetEN10QtGraphs3D12Camera'
        'PresetE',
        preset.value,
    )

  @overload(float)
  def setCameraXRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setCameraXRotation(float rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCameraXRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setCameraXRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18setCameraXRotationEf', rotation,
    )

  @overload(float)
  def setCameraYRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setCameraYRotation(float rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCameraYRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setCameraYRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18setCameraYRotationEf', rotation,
    )

  @overload(float)
  def setMinCameraXRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setMinCameraXRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setMinCameraXRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setMinCameraXRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem21setMinCameraXRotationEf', rotation,
    )

  @overload(float)
  def setMaxCameraXRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setMaxCameraXRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setMaxCameraXRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setMaxCameraXRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem21setMaxCameraXRotationEf', rotation,
    )

  @overload(float)
  def setMinCameraYRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setMinCameraYRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setMinCameraYRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setMinCameraYRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem21setMinCameraYRotationEf', rotation,
    )

  @overload(float)
  def setMaxCameraYRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setMaxCameraYRotation(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setMaxCameraYRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setMaxCameraYRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem21setMaxCameraYRotationEf', rotation,
    )

  @overload(bool)
  def setZoomAtTargetEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setZoomAtTargetEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setZoomAtTargetEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setZoomAtTargetEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22setZoomAtTargetEnabledEb', enable,
    )

  @overload(bool)
  def setZoomEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setZoomEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setZoomEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setZoomEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem14setZoomEnabledEb', enable,
    )

  @overload(bool)
  def setSelectionEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setSelectionEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setSelectionEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setSelectionEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem19setSelectionEnabledEb', enable,
    )

  @overload(bool)
  def setRotationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setRotationEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setRotationEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setRotationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18setRotationEnabledEb', enable,
    )

  @overload(bool)
  def setPanEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setPanEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setPanEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setPanEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem13setPanEnabledEb', enable,
    )

  @overload(QtGraphs3D.DragMode)
  def setDragMode(self, newDragMode: QtGraphs3D.DragMode) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setDragMode(QtGraphs3D::DragMode
    newDragMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setDragMode

    Parameters
    ----------

    newDragMode : QtGraphs3D.DragMode
      Passed on as its number.
    """
    #  void QQuickGraphsItem::setDragMode(QtGraphs3D::DragMode newDragMode)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem11setDragModeEN10QtGraphs3D8DragModeE',
        newDragMode.value,
    )

  def setDefaultInputHandler(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setDefaultInputHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setDefaultInputHandler
    """
    #  void QQuickGraphsItem::setDefaultInputHandler()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22setDefaultInputHandlerEv',
    )

  @overload(Qt.MouseButtons)
  def setDragButton(self, button: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setDragButton(Qt::MouseButtons
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setDragButton

    Parameters
    ----------

    button : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QQuickGraphsItem::setDragButton(Qt::MouseButtons button)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem13setDragButtonE6QFlagsIN2Qt11MouseButt'
        'onEE',
        button.value,
    )

  @overload(Qt.MouseButtons)
  def setPanButton(self, button: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setPanButton(Qt::MouseButtons
    button)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setPanButton

    Parameters
    ----------

    button : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QQuickGraphsItem::setPanButton(Qt::MouseButtons button)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12setPanButtonE6QFlagsIN2Qt11MouseButto'
        'nEE',
        button.value,
    )

  @overload(float)
  def setCameraZoomLevel(self, level: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setCameraZoomLevel(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCameraZoomLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setCameraZoomLevel(float level)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18setCameraZoomLevelEf', level,
    )

  @overload(float)
  def setMinCameraZoomLevel(self, level: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setMinCameraZoomLevel(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setMinCameraZoomLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setMinCameraZoomLevel(float level)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem21setMinCameraZoomLevelEf', level,
    )

  @overload(float)
  def setMaxCameraZoomLevel(self, level: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setMaxCameraZoomLevel(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setMaxCameraZoomLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setMaxCameraZoomLevel(float level)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem21setMaxCameraZoomLevelEf', level,
    )

  @overload(QVector3D)
  def setCameraTargetPosition(self, target: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setCameraTargetPosition(QVector3D
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCameraTargetPosition

    Parameters
    ----------

    target : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::setCameraTargetPosition(QVector3D target)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23setCameraTargetPositionE9QVector3D',
        self._valueOf(target),
    )

  @overload(bool)
  def setWrapCameraXRotation(self, wrap: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setWrapCameraXRotation(bool wrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setWrapCameraXRotation

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setWrapCameraXRotation(bool wrap)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22setWrapCameraXRotationEb', wrap,
    )

  @overload(bool)
  def setWrapCameraYRotation(self, wrap: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setWrapCameraYRotation(bool wrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setWrapCameraYRotation

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setWrapCameraYRotation(bool wrap)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22setWrapCameraYRotationEb', wrap,
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
    Calls Qt's 'void QQuickGraphsItem::setCameraPosition(float horizontal,
    float vertical, float zoom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setCameraPosition

    Parameters
    ----------

    horizontal : float
      Passed on as it is.

    vertical : float
      Passed on as it is.

    zoom : float
      Passed on as it is. May be left out, as in Qt: it is then 100.0.
    """
    #  void QQuickGraphsItem::setCameraPosition(float horizontal, float
    #      vertical, float zoom)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem17setCameraPositionEfff',
        horizontal, vertical, zoom,
    )

  @overload(bool)
  def setSliceActivatedChanged(self, changed: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setSliceActivatedChanged(bool
    changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setSliceActivatedChanged

    Parameters
    ----------

    changed : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setSliceActivatedChanged(bool changed)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24setSliceActivatedChangedEb', changed,
    )

  @overload(int)
  def setHorizontalFlipFactor(self, newHorizontalFlipFactor: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setHorizontalFlipFactor(int
    newHorizontalFlipFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setHorizontalFlipFactor

    Parameters
    ----------

    newHorizontalFlipFactor : int
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setHorizontalFlipFactor(int
    #      newHorizontalFlipFactor)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23setHorizontalFlipFactorEi',
        newHorizontalFlipFactor,
    )

  @overload(float)
  def setAmbientLightStrength(self, newAmbientLightStrength: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setAmbientLightStrength(float
    newAmbientLightStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setAmbientLightStrength

    Parameters
    ----------

    newAmbientLightStrength : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setAmbientLightStrength(float
    #      newAmbientLightStrength)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23setAmbientLightStrengthEf',
        newAmbientLightStrength,
    )

  @overload(float)
  def setLightStrength(self, newLightStrength: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setLightStrength(float
    newLightStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setLightStrength

    Parameters
    ----------

    newLightStrength : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setLightStrength(float newLightStrength)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem16setLightStrengthEf', newLightStrength,
    )

  @overload(float)
  def setShadowStrength(self, newShadowStrength: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setShadowStrength(float
    newShadowStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setShadowStrength

    Parameters
    ----------

    newShadowStrength : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setShadowStrength(float newShadowStrength)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem17setShadowStrengthEf',
        newShadowStrength,
    )

  @overload(QColor)
  def setLightColor(self, newLightColor: QColor) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setLightColor(QColor newLightColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setLightColor

    Parameters
    ----------

    newLightColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::setLightColor(QColor newLightColor)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem13setLightColorE6QColor',
        self._valueOf(newLightColor),
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setParentNode(self, node: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setParentNode(QQuick3DNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setParentNode

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::setParentNode(QQuick3DNode *node)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem13setParentNodeEP12QQuick3DNode',
        self._addressOf(node),
    )

  @overload(bool)
  def setUserCameraRotationRange(self, userRotationRange: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setUserCameraRotationRange(bool
    userRotationRange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setUserCameraRotationRange

    Parameters
    ----------

    userRotationRange : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setUserCameraRotationRange(bool
    #      userRotationRange)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem26setUserCameraRotationRangeEb',
        userRotationRange,
    )

  @overload(bool)
  def setFloorGridInRange(self, inRange: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setFloorGridInRange(bool inRange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setFloorGridInRange

    Parameters
    ----------

    inRange : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setFloorGridInRange(bool inRange)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem19setFloorGridInRangeEb', inRange,
    )

  @overload(bool)
  def setVerticalSegmentLine(self, hasVerticalLine: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setVerticalSegmentLine(bool
    hasVerticalLine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setVerticalSegmentLine

    Parameters
    ----------

    hasVerticalLine : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setVerticalSegmentLine(bool hasVerticalLine)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22setVerticalSegmentLineEb',
        hasVerticalLine,
    )

  @overload(bool)
  def setItemSelected(self, selected: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setItemSelected(bool selected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setItemSelected

    Parameters
    ----------

    selected : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setItemSelected(bool selected)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15setItemSelectedEb', selected,
    )

  @overload(bool)
  def setSliceEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setSliceEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setSliceEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setSliceEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15setSliceEnabledEb', enabled,
    )

  @overload(bool)
  def setSliceOrthoProjection(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setSliceOrthoProjection(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setSliceOrthoProjection

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setSliceOrthoProjection(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23setSliceOrthoProjectionEb', enable,
    )

  @overload(bool)
  def setGridUpdated(self, updated: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setGridUpdated(bool updated)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#setGridUpdated

    Parameters
    ----------

    updated : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::setGridUpdated(bool updated)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem14setGridUpdatedEb', updated,
    )

  def setUpCamera(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setUpCamera()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setUpCamera
    """
    #  void QQuickGraphsItem::setUpCamera()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem11setUpCameraEv')

  def setUpLight(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::setUpLight()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#setUpLight
    """
    #  void QQuickGraphsItem::setUpLight()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem10setUpLightEv')

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
    'QQuickGraphsItem::QQuickGraphsItem(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#QQuickGraphsItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGraphsItem::QQuickGraphsItem(QQuickItem *parent)
    self._noteCreation(QQuickGraphsItem, lambda: Rituals.call(
        'ritual_ZN16QQuickGraphsItemC1EP10QQuickItem',
        self._addressOf(parent),
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

  def markDataDirty(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::markDataDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#markDataDirty
    """
    #  void QQuickGraphsItem::markDataDirty()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem13markDataDirtyEv')

  def markSeriesVisualsDirty(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::markSeriesVisualsDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#markSeriesVisualsDirty
    """
    #  void QQuickGraphsItem::markSeriesVisualsDirty()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22markSeriesVisualsDirtyEv',
    )

  def markSeriesItemLabelsDirty(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::markSeriesItemLabelsDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#markSeriesItemLabelsDirty
    """
    #  void QQuickGraphsItem::markSeriesItemLabelsDirty()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25markSeriesItemLabelsDirtyEv',
    )

  def emitNeedRender(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::emitNeedRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#emitNeedRender
    """
    #  void QQuickGraphsItem::emitNeedRender()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem14emitNeedRenderEv')

  @overload(QObject)
  @overload(NoneType)
  def handleAxisTitleChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisTitleChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisTitleChangedBySender(QObject *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem30handleAxisTitleChangedBySenderEP7QObj'
        'ect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem30handleAxisTitleChangedBySenderE'
          'P7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisLabelsChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisLabelsChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisLabelsChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem31handleAxisLabelsChangedBySenderEP7QOb'
        'ject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem31handleAxisLabelsChangedBySender'
          'EP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisRangeChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisRangeChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisRangeChangedBySender(QObject *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem30handleAxisRangeChangedBySenderEP7QObj'
        'ect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem30handleAxisRangeChangedBySenderE'
          'P7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisSegmentCountChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisSegmentCountChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisSegmentCountChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem37handleAxisSegmentCountChangedBySender'
        'EP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem37handleAxisSegmentCountChangedBy'
          'SenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisSubSegmentCountChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem40handleAxisSubSegmentCountChangedBySen'
        'derEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem40handleAxisSubSegmentCountChange'
          'dBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def handleAxisAutoAdjustRangeChangedInOrientation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      autoAdjust: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisAutoAdjustRangeChangedInOrientation(
    QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    autoAdjust : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisAutoAdjustRangeChangedInOrientation(
    #      QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem45handleAxisAutoAdjustRangeChangedInOri'
        'entationEN15QAbstract3DAxis15AxisOrientationEb',
        orientation.value, autoAdjust,
    )

  @overload(QObject)
  @overload(NoneType)
  def handleAxisLabelFormatChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisLabelFormatChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisLabelFormatChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem36handleAxisLabelFormatChangedBySenderE'
        'P7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem36handleAxisLabelFormatChangedByS'
          'enderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisReversedChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisReversedChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisReversedChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem33handleAxisReversedChangedBySenderEP7Q'
        'Object')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem33handleAxisReversedChangedBySend'
          'erEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisFormatterDirtyBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisFormatterDirtyBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisFormatterDirtyBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem32handleAxisFormatterDirtyBySenderEP7QO'
        'bject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem32handleAxisFormatterDirtyBySende'
          'rEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisLabelAutoRotationChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(
    #      QObject *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem42handleAxisLabelAutoRotationChangedByS'
        'enderEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem42handleAxisLabelAutoRotationChan'
          'gedBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisScaleLabelsByCountChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(
    #      QObject *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem43handleAxisScaleLabelsByCountChangedBy'
        'SenderEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem43handleAxisScaleLabelsByCountCha'
          'ngedBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisLabelSizeChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisLabelSizeChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisLabelSizeChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem34handleAxisLabelSizeChangedBySenderEP7'
        'QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem34handleAxisLabelSizeChangedBySen'
          'derEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisTitleVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem40handleAxisTitleVisibilityChangedBySen'
        'derEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem40handleAxisTitleVisibilityChange'
          'dBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisLabelVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem40handleAxisLabelVisibilityChangedBySen'
        'derEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem40handleAxisLabelVisibilityChange'
          'dBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisTitleFixedChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisTitleFixedChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisTitleFixedChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem35handleAxisTitleFixedChangedBySenderEP'
        '7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem35handleAxisTitleFixedChangedBySe'
          'nderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisTitleOffsetChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem36handleAxisTitleOffsetChangedBySenderE'
        'P7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem36handleAxisTitleOffsetChangedByS'
          'enderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleSeriesVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleSeriesVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleSeriesVisibilityChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsItem37handleSeriesVisibilityChangedBySender'
        'EP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem37handleSeriesVisibilityChangedBy'
          'SenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  def handleLightingModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleLightingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleLightingModeChanged
    """
    #  void QQuickGraphsItem::handleLightingModeChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25handleLightingModeChangedEv',
    )

  def adjustAxisRanges(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::adjustAxisRanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#adjustAxisRanges
    """
    #  void QQuickGraphsItem::adjustAxisRanges()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem16adjustAxisRangesEv')

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleMultiAxisChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleMultiAxisChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleMultiAxisChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleMultiAxisChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN16QQuickGraphsItem22handleMultiAxisChangedEP15QAbstract3D'
        'Axis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem22handleMultiAxisChangedEP15QAbst'
          'ract3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  def handleMultiAxisDirty(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleMultiAxisDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleMultiAxisDirty
    """
    #  void QQuickGraphsItem::handleMultiAxisDirty()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem20handleMultiAxisDirtyEv')

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def addSeriesInternal(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::addSeriesInternal(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#addSeriesInternal

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::addSeriesInternal(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN16QQuickGraphsItem17addSeriesInternalEP17QAbstract3DSerie'
        's')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem17addSeriesInternalEP17QAbstract3'
          'DSeries')
    self.uglySide.call(ritual, self._addressOf(series))

  @overload(int, QAbstract3DSeries)
  @overload(int, NoneType)
  def insertSeries(
      self,
      index: int,
      series: Optional[QAbstract3DSeries],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::insertSeries(qsizetype index,
    QAbstract3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#insertSeries

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::insertSeries(qsizetype index, QAbstract3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12insertSeriesExP17QAbstract3DSeries',
        index, self._addressOf(series),
    )

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def removeSeriesInternal(
      self,
      series: Optional[QAbstract3DSeries],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::removeSeriesInternal(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#removeSeriesInternal

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::removeSeriesInternal(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN16QQuickGraphsItem20removeSeriesInternalEP17QAbstract3DSe'
        'ries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem20removeSeriesInternalEP17QAbstra'
          'ct3DSeries')
    self.uglySide.call(ritual, self._addressOf(series))

  def seriesList(self) -> QList[QAbstract3DSeries]:
    """
    Calls Qt's 'QList<QAbstract3DSeries *> QQuickGraphsItem::seriesList()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#seriesList

    Returns
    -------

    QList[QAbstract3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DSeries *> QQuickGraphsItem::seriesList()
    address = self.uglySide.call('ritual_ZN16QQuickGraphsItem10seriesListEv')
    from . import QAbstract3DSeries
    return QList[QAbstract3DSeries]._cuteOwning(address)

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def addAxis(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::addAxis(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#addAxis

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::addAxis(QAbstract3DAxis *axis)
    ritual = 'ritual_ZN16QQuickGraphsItem7addAxisEP15QAbstract3DAxis'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem7addAxisEP15QAbstract3DAxis'
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def releaseAxis(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::releaseAxis(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#releaseAxis

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::releaseAxis(QAbstract3DAxis *axis)
    ritual = 'ritual_ZN16QQuickGraphsItem11releaseAxisEP15QAbstract3DAxis'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem11releaseAxisEP15QAbstract3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QtGraphs3D.ShadowQuality)
  def doSetShadowQuality(self, quality: QtGraphs3D.ShadowQuality) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::doSetShadowQuality(QtGraphs3D::ShadowQuality quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#doSetShadowQuality

    Parameters
    ----------

    quality : QtGraphs3D.ShadowQuality
      Passed on as its number.
    """
    #  void QQuickGraphsItem::doSetShadowQuality(QtGraphs3D::ShadowQuality
    #      quality)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18doSetShadowQualityEN10QtGraphs3D13Sha'
        'dowQualityE',
        quality.value,
    )

  @overload(QGraphsTheme)
  @overload(NoneType)
  def addTheme(self, theme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::addTheme(QGraphsTheme *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#addTheme

    Parameters
    ----------

    theme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::addTheme(QGraphsTheme *theme)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem8addThemeEP12QGraphsTheme',
        self._addressOf(theme),
    )

  @overload(QGraphsTheme)
  @overload(NoneType)
  def releaseTheme(self, theme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::releaseTheme(QGraphsTheme *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#releaseTheme

    Parameters
    ----------

    theme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::releaseTheme(QGraphsTheme *theme)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12releaseThemeEP12QGraphsTheme',
        self._addressOf(theme),
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def customTextureImage(self, item: Optional[QCustom3DItem]) -> QImage:
    """
    Calls Qt's 'QImage QQuickGraphsItem::customTextureImage(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#customTextureImage

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickGraphsItem::customTextureImage(QCustom3DItem *item)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18customTextureImageEP13QCustom3DItem',
        self._addressOf(item),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def scene(self) -> Optional[Q3DScene]:
    """
    Calls Qt's 'Q3DScene *QQuickGraphsItem::scene()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#scene

    Returns
    -------

    Optional[Q3DScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScene *QQuickGraphsItem::scene()
    address = self.uglySide.call('ritual_ZN16QQuickGraphsItem5sceneEv')
    from . import Q3DScene
    return Q3DScene._cuteAt(address)

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def hasSeries(self, series: Optional[QAbstract3DSeries]) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::hasSeries(QAbstract3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#hasSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickGraphsItem::hasSeries(QAbstract3DSeries *series)
    ritual = 'ritual_ZN16QQuickGraphsItem9hasSeriesEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem9hasSeriesEP17QAbstract3DSeries')
    return self.uglySide.call(ritual, self._addressOf(series))

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#clearSelection
    """
    #  void QQuickGraphsItem::clearSelection()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem14clearSelectionEv')

  def deleteCustomItems(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::deleteCustomItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#deleteCustomItems
    """
    #  void QQuickGraphsItem::deleteCustomItems()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem17deleteCustomItemsEv')

  @overload(QCustom3DItem)
  @overload(NoneType)
  def deleteCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::deleteCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#deleteCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::deleteCustomItem(QCustom3DItem *item)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem16deleteCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  @overload(QVector3D)
  def deleteCustomItem(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::deleteCustomItem(QVector3D position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#deleteCustomItem

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::deleteCustomItem(QVector3D position)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem16deleteCustomItemE9QVector3D',
        self._valueOf(position),
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def addCustomItem(self, item: Optional[QCustom3DItem]) -> int:
    """
    Calls Qt's 'qsizetype QQuickGraphsItem::addCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#addCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qsizetype QQuickGraphsItem::addCustomItem(QCustom3DItem *item)
    ritual = 'ritual_ZN16QQuickGraphsItem13addCustomItemEP13QCustom3DItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem13addCustomItemEP13QCustom3DItem')
    return self.uglySide.call(ritual, self._addressOf(item))

  def removeCustomItems(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::removeCustomItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#removeCustomItems
    """
    #  void QQuickGraphsItem::removeCustomItems()
    ritual = 'ritual_ZN16QQuickGraphsItem17removeCustomItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem17removeCustomItemsEv'
    self.uglySide.call(ritual)

  @overload(QCustom3DItem)
  @overload(NoneType)
  def removeCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::removeCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#removeCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::removeCustomItem(QCustom3DItem *item)
    ritual = 'ritual_ZN16QQuickGraphsItem16removeCustomItemEP13QCustom3DItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem16removeCustomItemEP13QCustom3DIt'
          'em')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QVector3D)
  def removeCustomItemAt(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::removeCustomItemAt(QVector3D
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#removeCustomItemAt

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::removeCustomItemAt(QVector3D position)
    ritual = 'ritual_ZN16QQuickGraphsItem18removeCustomItemAtE9QVector3D'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem18removeCustomItemAtE9QVector3D')
    self.uglySide.call(ritual, self._valueOf(position))

  @overload(QCustom3DItem)
  @overload(NoneType)
  def releaseCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::releaseCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#releaseCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::releaseCustomItem(QCustom3DItem *item)
    ritual = (
        'ritual_ZN16QQuickGraphsItem17releaseCustomItemEP13QCustom3DItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem17releaseCustomItemEP13QCustom3DI'
          'tem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN16QQuickGraphsItem14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QSizeF)
  def resizeViewports(self, viewportSize: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::resizeViewports(QSizeF viewportSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#resizeViewports

    Parameters
    ----------

    viewportSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::resizeViewports(QSizeF viewportSize)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15resizeViewportsE6QSizeF',
        self._valueOf(viewportSize),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def checkWindowList(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::checkWindowList(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#checkWindowList

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::checkWindowList(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15checkWindowListEP12QQuickWindow',
        self._addressOf(window),
    )

  def isReady(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isReady()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#isReady
    """
    #  bool QQuickGraphsItem::isReady()
    return self.uglySide.call('ritual_ZN16QQuickGraphsItem7isReadyEv')

  def cameraTarget(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuickGraphsItem::cameraTarget()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraTarget

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuickGraphsItem::cameraTarget()
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12cameraTargetEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  @overload(str)
  def createQmlCustomMaterial(
      self,
      fileName: str,
  ) -> Optional[QQuick3DCustomMaterial]:
    """
    Calls Qt's 'QQuick3DCustomMaterial
    *QQuickGraphsItem::createQmlCustomMaterial(const QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createQmlCustomMaterial

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QQuick3DCustomMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DCustomMaterial
    #      *QQuickGraphsItem::createQmlCustomMaterial(const QString
    #      &fileName)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23createQmlCustomMaterialERK7QString',
        fileName,
    )
    from ..QtQuick3D import QQuick3DCustomMaterial
    return QQuick3DCustomMaterial._cuteAt(address)

  def createPrincipledMaterial(self) -> Optional[QQuick3DPrincipledMaterial]:
    """
    Calls Qt's 'QQuick3DPrincipledMaterial
    *QQuickGraphsItem::createPrincipledMaterial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createPrincipledMaterial

    Returns
    -------

    Optional[QQuick3DPrincipledMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DPrincipledMaterial
    #      *QQuickGraphsItem::createPrincipledMaterial()
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24createPrincipledMaterialEv',
    )
    from ..QtQuick3D import QQuick3DPrincipledMaterial
    return QQuick3DPrincipledMaterial._cuteAt(address)

  def itemLabel(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickGraphsItem::itemLabel()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#itemLabel

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickGraphsItem::itemLabel()
    address = self.uglySide.call('ritual_ZN16QQuickGraphsItem9itemLabelEv')
    return QQuickItem._cuteAt(address)

  def sliceItemLabel(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuickGraphsItem::sliceItemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#sliceItemLabel

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuickGraphsItem::sliceItemLabel()
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem14sliceItemLabelEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def zoomAtTargetEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::zoomAtTargetEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#zoomAtTargetEnabled
    """
    #  bool QQuickGraphsItem::zoomAtTargetEnabled()
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem19zoomAtTargetEnabledEv',
    )

  def zoomEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::zoomEnabled()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#zoomEnabled
    """
    #  bool QQuickGraphsItem::zoomEnabled()
    return self.uglySide.call('ritual_ZN16QQuickGraphsItem11zoomEnabledEv')

  def selectionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::selectionEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#selectionEnabled
    """
    #  bool QQuickGraphsItem::selectionEnabled()
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem16selectionEnabledEv',
    )

  def rotationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::rotationEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#rotationEnabled
    """
    #  bool QQuickGraphsItem::rotationEnabled()
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15rotationEnabledEv',
    )

  def panEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::panEnabled()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#panEnabled
    """
    #  bool QQuickGraphsItem::panEnabled()
    return self.uglySide.call('ritual_ZN16QQuickGraphsItem10panEnabledEv')

  def unsetDefaultInputHandler(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::unsetDefaultInputHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#unsetDefaultInputHandler
    """
    #  void QQuickGraphsItem::unsetDefaultInputHandler()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24unsetDefaultInputHandlerEv',
    )

  def unsetDefaultTapHandler(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::unsetDefaultTapHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#unsetDefaultTapHandler
    """
    #  void QQuickGraphsItem::unsetDefaultTapHandler()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22unsetDefaultTapHandlerEv',
    )

  def unsetDefaultDragHandler(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::unsetDefaultDragHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#unsetDefaultDragHandler
    """
    #  void QQuickGraphsItem::unsetDefaultDragHandler()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23unsetDefaultDragHandlerEv',
    )

  def unsetDefaultWheelHandler(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::unsetDefaultWheelHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#unsetDefaultWheelHandler
    """
    #  void QQuickGraphsItem::unsetDefaultWheelHandler()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24unsetDefaultWheelHandlerEv',
    )

  def unsetDefaultPinchHandler(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::unsetDefaultPinchHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#unsetDefaultPinchHandler
    """
    #  void QQuickGraphsItem::unsetDefaultPinchHandler()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24unsetDefaultPinchHandlerEv',
    )

  @overload(QPoint)
  def graphPositionAt(self, point: QPoint) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::graphPositionAt(QPoint point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#graphPositionAt

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::graphPositionAt(QPoint point)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15graphPositionAtE6QPoint',
        self._valueOf(point),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QQuick3DRepeater, QColor)
  @overload(NoneType, QColor)
  def changeLabelBackgroundColor(
      self,
      repeater: Optional[QQuick3DRepeater],
      color: QColor,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::changeLabelBackgroundColor(QQuick3DRepeater *repeater,
    QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#changeLabelBackgroundColor

    Parameters
    ----------

    repeater : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::changeLabelBackgroundColor(QQuick3DRepeater
    #      *repeater, QColor color)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem26changeLabelBackgroundColorEP16QQuick3'
        'DRepeater6QColor',
        self._addressOf(repeater), self._valueOf(color),
    )

  @overload(QQuick3DRepeater, bool)
  @overload(NoneType, bool)
  def changeLabelBackgroundVisible(
      self,
      repeater: Optional[QQuick3DRepeater],
      visible: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::changeLabelBackgroundVisible(QQuick3DRepeater
    *repeater, const bool &visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#changeLabelBackgroundVisible

    Parameters
    ----------

    repeater : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    visible : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::changeLabelBackgroundVisible(QQuick3DRepeater
    #      *repeater, const bool &visible)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem28changeLabelBackgroundVisibleEP16QQuic'
        'k3DRepeaterRKb',
        self._addressOf(repeater), visible,
    )

  @overload(QQuick3DRepeater, bool)
  @overload(NoneType, bool)
  def changeLabelBorderVisible(
      self,
      repeater: Optional[QQuick3DRepeater],
      visible: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::changeLabelBorderVisible(QQuick3DRepeater *repeater,
    const bool &visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#changeLabelBorderVisible

    Parameters
    ----------

    repeater : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    visible : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::changeLabelBorderVisible(QQuick3DRepeater
    #      *repeater, const bool &visible)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24changeLabelBorderVisibleEP16QQuick3DR'
        'epeaterRKb',
        self._addressOf(repeater), visible,
    )

  @overload(QQuick3DRepeater, QColor)
  @overload(NoneType, QColor)
  def changeLabelTextColor(
      self,
      repeater: Optional[QQuick3DRepeater],
      color: QColor,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::changeLabelTextColor(QQuick3DRepeater
    *repeater, QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#changeLabelTextColor

    Parameters
    ----------

    repeater : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::changeLabelTextColor(QQuick3DRepeater
    #      *repeater, QColor color)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem20changeLabelTextColorEP16QQuick3DRepea'
        'ter6QColor',
        self._addressOf(repeater), self._valueOf(color),
    )

  @overload(QQuick3DRepeater, QFont)
  @overload(NoneType, QFont)
  def changeLabelFont(
      self,
      repeater: Optional[QQuick3DRepeater],
      font: QFont,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::changeLabelFont(QQuick3DRepeater
    *repeater, const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#changeLabelFont

    Parameters
    ----------

    repeater : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickGraphsItem::changeLabelFont(QQuick3DRepeater *repeater,
    #      const QFont &font)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15changeLabelFontEP16QQuick3DRepeaterRK'
        '5QFont',
        self._addressOf(repeater), self._valueOf(font),
    )

  @overload(QQuick3DRepeater, bool)
  @overload(NoneType, bool)
  def changeLabelsVisible(
      self,
      repeater: Optional[QQuick3DRepeater],
      visible: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::changeLabelsVisible(QQuick3DRepeater
    *repeater, const bool &visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#changeLabelsVisible

    Parameters
    ----------

    repeater : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    visible : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::changeLabelsVisible(QQuick3DRepeater *repeater,
    #      const bool &visible)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem19changeLabelsVisibleEP16QQuick3DRepeat'
        'erRKb',
        self._addressOf(repeater), visible,
    )

  @overload(QQuick3DRepeater, QColor)
  @overload(NoneType, QColor)
  def changeGridLineColor(
      self,
      repeater: Optional[QQuick3DRepeater],
      color: QColor,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::changeGridLineColor(QQuick3DRepeater
    *repeater, QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#changeGridLineColor

    Parameters
    ----------

    repeater : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::changeGridLineColor(QQuick3DRepeater *repeater,
    #      QColor color)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem19changeGridLineColorEP16QQuick3DRepeat'
        'er6QColor',
        self._addressOf(repeater), self._valueOf(color),
    )

  def updateTitleLabels(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateTitleLabels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateTitleLabels
    """
    #  void QQuickGraphsItem::updateTitleLabels()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem17updateTitleLabelsEv')

  @overload(QtGraphs3D.SelectionFlags)
  def updateSelectionMode(self, newMode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::updateSelectionMode(QtGraphs3D::SelectionFlags
    newMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateSelectionMode

    Parameters
    ----------

    newMode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsItem::updateSelectionMode(QtGraphs3D::SelectionFlags
    #      newMode)
    ritual = (
        'ritual_ZN16QQuickGraphsItem19updateSelectionModeE6QFlagsIN10QtGrap'
        'hs3D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem19updateSelectionModeE6QFlagsIN10'
          'QtGraphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, newMode.value)

  @overload(QPointF)
  def doPicking(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::doPicking(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#doPicking

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickGraphsItem::doPicking(QPointF point)
    ritual = 'ritual_ZN16QQuickGraphsItem9doPickingE7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem9doPickingE7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  @overload(QVector3D, QVector3D)
  def doRayPicking(self, origin: QVector3D, direction: QVector3D) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::doRayPicking(QVector3D origin,
    QVector3D direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#doRayPicking

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuickGraphsItem::doRayPicking(QVector3D origin, QVector3D
    #      direction)
    ritual = 'ritual_ZN16QQuickGraphsItem12doRayPickingE9QVector3DS0_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem12doRayPickingE9QVector3DS0_'
    return self.uglySide.call(
        ritual, self._valueOf(origin), self._valueOf(direction),
    )

  def minimizeMainGraph(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::minimizeMainGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#minimizeMainGraph
    """
    #  void QQuickGraphsItem::minimizeMainGraph()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem17minimizeMainGraphEv')

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisXChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisXChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisXChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisXChanged(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18handleAxisXChangedEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisYChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisYChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisYChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisYChanged(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18handleAxisYChangedEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisZChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisZChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisZChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleAxisZChanged(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18handleAxisZChangedEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  def handleFpsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleFpsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleFpsChanged
    """
    #  void QQuickGraphsItem::handleFpsChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem16handleFpsChangedEv')

  @overload(QObject)
  @overload(NoneType)
  def windowDestroyed(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::windowDestroyed(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#windowDestroyed

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::windowDestroyed(QObject *obj)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15windowDestroyedEP7QObject',
        self._addressOf(obj, 'QObject'),
    )

  @overload(str)
  def handleAxisTitleChanged(self, title: str) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisTitleChanged(const QString
    &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisTitleChanged

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGraphsItem::handleAxisTitleChanged(const QString &title)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22handleAxisTitleChangedERK7QString',
        title,
    )

  def handleAxisLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisLabelsChanged
    """
    #  void QQuickGraphsItem::handleAxisLabelsChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23handleAxisLabelsChangedEv',
    )

  @overload(float, float)
  def handleAxisRangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisRangeChanged(float min,
    float max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisRangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisRangeChanged(float min, float max)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22handleAxisRangeChangedEff', min, max,
    )

  @overload(int)
  def handleAxisSegmentCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisSegmentCountChanged(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisSegmentCountChanged(qsizetype count)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem29handleAxisSegmentCountChangedEx',
        count,
    )

  @overload(int)
  def handleAxisSubSegmentCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisSubSegmentCountChanged(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisSubSegmentCountChanged(qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem32handleAxisSubSegmentCountChangedEx',
        count,
    )

  @overload(bool)
  def handleAxisAutoAdjustRangeChanged(self, autoAdjust: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisAutoAdjustRangeChanged(bool
    autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    autoAdjust : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisAutoAdjustRangeChanged(bool
    #      autoAdjust)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem32handleAxisAutoAdjustRangeChangedEb',
        autoAdjust,
    )

  @overload(bool)
  def handleAxisScaleLabelsByCountChanged(self, adjust: bool) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisScaleLabelsByCountChanged(bool adjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    adjust : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisScaleLabelsByCountChanged(bool
    #      adjust)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem35handleAxisScaleLabelsByCountChangedEb',
        adjust,
    )

  @overload(float)
  def handleAxisLabelSizeChanged(self, size: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisLabelSizeChanged(qreal
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisLabelSizeChanged

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisLabelSizeChanged(qreal size)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem26handleAxisLabelSizeChangedEd', size,
    )

  @overload(str)
  def handleAxisLabelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisLabelFormatChanged(const
    QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisLabelFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGraphsItem::handleAxisLabelFormatChanged(const QString
    #      &format)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem28handleAxisLabelFormatChangedERK7QStri'
        'ng',
        format,
    )

  @overload(bool)
  def handleAxisReversedChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisReversedChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisReversedChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisReversedChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25handleAxisReversedChangedEb', enable,
    )

  def handleAxisFormatterDirty(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisFormatterDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisFormatterDirty
    """
    #  void QQuickGraphsItem::handleAxisFormatterDirty()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24handleAxisFormatterDirtyEv',
    )

  @overload(float)
  def handleAxisLabelAutoRotationChanged(self, angle: float) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleAxisLabelAutoRotationChanged(float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisLabelAutoRotationChanged(float angle)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem34handleAxisLabelAutoRotationChangedEf',
        angle,
    )

  @overload(bool)
  def handleAxisTitleVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisTitleVisibilityChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisTitleVisibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem32handleAxisTitleVisibilityChangedEb',
        visible,
    )

  @overload(bool)
  def handleAxisLabelVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisLabelVisibilityChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisLabelVisibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem32handleAxisLabelVisibilityChangedEb',
        visible,
    )

  @overload(bool)
  def handleAxisTitleFixedChanged(self, fixed: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisTitleFixedChanged(bool
    fixed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisTitleFixedChanged

    Parameters
    ----------

    fixed : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisTitleFixedChanged(bool fixed)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem27handleAxisTitleFixedChangedEb', fixed,
    )

  @overload(float)
  def handleAxisTitleOffsetChanged(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleAxisTitleOffsetChanged(float
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleAxisTitleOffsetChanged

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleAxisTitleOffsetChanged(float offset)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem28handleAxisTitleOffsetChangedEf',
        offset,
    )

  @overload(QPoint)
  def handleInputPositionChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleInputPositionChanged(QPoint
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleInputPositionChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::handleInputPositionChanged(QPoint position)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem26handleInputPositionChangedE6QPoint',
        self._valueOf(position),
    )

  @overload(bool)
  def handleSeriesVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleSeriesVisibilityChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleSeriesVisibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem29handleSeriesVisibilityChangedEb',
        visible,
    )

  @overload(bool)
  def handleItemLabelVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleItemLabelVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::handleItemLabelVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem29handleItemLabelVisibleChangedEb',
        visible,
    )

  @overload(bool, QObject)
  @overload(bool, NoneType)
  def handleItemLabelVisibleChangedBySender(
      self,
      visible: bool,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleItemLabelVisibleChangedBySender(bool visible,
    QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::handleItemLabelVisibleChangedBySender(bool
    #      visible, QObject *sender)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem37handleItemLabelVisibleChangedBySender'
        'EbP7QObject',
        visible, self._addressOf(sender, 'QObject'),
    )

  @overload(QGraphsTheme.ColorStyle)
  def handleThemeColorStyleChanged(
      self,
      style: QGraphsTheme.ColorStyle,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleThemeColorStyleChanged(QGraphsTheme::ColorStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleThemeColorStyleChanged

    Parameters
    ----------

    style : QGraphsTheme.ColorStyle
      Passed on as its number.
    """
    #  void QQuickGraphsItem::handleThemeColorStyleChanged(QGraphsTheme::
    #      ColorStyle style)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem28handleThemeColorStyleChangedEN12QGrap'
        'hsTheme10ColorStyleE',
        style.value,
    )

  @overload(QList[QColor])
  def handleThemeBaseColorsChanged(self, color: QList[QColor]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleThemeBaseColorsChanged(const
    QList<QColor> &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleThemeBaseColorsChanged

    Parameters
    ----------

    color : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickGraphsItem::handleThemeBaseColorsChanged(const
    #      QList<QColor> &color)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem28handleThemeBaseColorsChangedERK5QList'
        'I6QColorE',
        self._valueOf(color),
    )

  @overload(QList[QLinearGradient])
  def handleThemeBaseGradientsChanged(
      self,
      gradient: QList[QLinearGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleThemeBaseGradientsChanged(const
    QList<QLinearGradient> &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    gradient : QList[QLinearGradient]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickGraphsItem::handleThemeBaseGradientsChanged(const
    #      QList<QLinearGradient> &gradient)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem31handleThemeBaseGradientsChangedERK5QL'
        'istI15QLinearGradientE',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def handleThemeSingleHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleThemeSingleHighlightColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::handleThemeSingleHighlightColorChanged(QColor
    #      color)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem38handleThemeSingleHighlightColorChange'
        'dE6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def handleThemeSingleHighlightGradientChanged(
      self,
      gradient: QLinearGradient,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleThemeSingleHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QQuickGraphsItem::handleThemeSingleHighlightGradientChanged(const
    #      QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem41handleThemeSingleHighlightGradientCha'
        'ngedERK15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def handleThemeMultiHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleThemeMultiHighlightColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::handleThemeMultiHighlightColorChanged(QColor
    #      color)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem37handleThemeMultiHighlightColorChanged'
        'E6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def handleThemeMultiHighlightGradientChanged(
      self,
      gradient: QLinearGradient,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleThemeMultiHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QQuickGraphsItem::handleThemeMultiHighlightGradientChanged(const
    #      QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem40handleThemeMultiHighlightGradientChan'
        'gedERK15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(QGraphsTheme.Theme)
  def handleThemeTypeChanged(self, theme: QGraphsTheme.Theme) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleThemeTypeChanged(QGraphsTheme::Theme theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleThemeTypeChanged

    Parameters
    ----------

    theme : QGraphsTheme.Theme
      Passed on as its number.
    """
    #  void QQuickGraphsItem::handleThemeTypeChanged(QGraphsTheme::Theme
    #      theme)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22handleThemeTypeChangedEN12QGraphsThem'
        'e5ThemeE',
        theme.value,
    )

  @overload(QtGraphs3D.ShadowQuality)
  def handleRequestShadowQuality(
      self,
      quality: QtGraphs3D.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleRequestShadowQuality(QtGraphs3D::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleRequestShadowQuality

    Parameters
    ----------

    quality : QtGraphs3D.ShadowQuality
      Passed on as its number.
    """
    #  void QQuickGraphsItem::handleRequestShadowQuality(QtGraphs3D::
    #      ShadowQuality quality)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem26handleRequestShadowQualityEN10QtGraph'
        's3D13ShadowQualityE',
        quality.value,
    )

  def updateCustomItem(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateCustomItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateCustomItem
    """
    #  void QQuickGraphsItem::updateCustomItem()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem16updateCustomItemEv')

  @overload(QtGraphs3D.SelectionFlags)
  def selectionModeChanged(self, mode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::selectionModeChanged(QtGraphs3D::SelectionFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#selectionModeChanged

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsItem::selectionModeChanged(QtGraphs3D::SelectionFlags
    #      mode)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem20selectionModeChangedE6QFlagsIN10QtGra'
        'phs3D13SelectionFlagEE',
        mode.value,
    )

  @overload(QtGraphs3D.ShadowQuality)
  def shadowQualityChanged(self, quality: QtGraphs3D.ShadowQuality) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::shadowQualityChanged(QtGraphs3D::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#shadowQualityChanged

    Parameters
    ----------

    quality : QtGraphs3D.ShadowQuality
      Passed on as its number.
    """
    #  void QQuickGraphsItem::shadowQualityChanged(QtGraphs3D::ShadowQuality
    #      quality)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem20shadowQualityChangedEN10QtGraphs3D13S'
        'hadowQualityE',
        quality.value,
    )

  @overload(bool)
  def shadowsSupportedChanged(self, supported: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::shadowsSupportedChanged(bool
    supported)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#shadowsSupportedChanged

    Parameters
    ----------

    supported : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::shadowsSupportedChanged(bool supported)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23shadowsSupportedChangedEb', supported,
    )

  @overload(int)
  def msaaSamplesChanged(self, samples: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::msaaSamplesChanged(int samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#msaaSamplesChanged

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QQuickGraphsItem::msaaSamplesChanged(int samples)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18msaaSamplesChangedEi', samples,
    )

  @overload(QGraphsTheme)
  @overload(NoneType)
  def themeChanged(self, theme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::themeChanged(QGraphsTheme *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#themeChanged

    Parameters
    ----------

    theme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::themeChanged(QGraphsTheme *theme)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12themeChangedEP12QGraphsTheme',
        self._addressOf(theme),
    )

  @overload(QtGraphs3D.RenderingMode)
  def renderingModeChanged(self, mode: QtGraphs3D.RenderingMode) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::renderingModeChanged(QtGraphs3D::RenderingMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#renderingModeChanged

    Parameters
    ----------

    mode : QtGraphs3D.RenderingMode
      Passed on as its number.
    """
    #  void QQuickGraphsItem::renderingModeChanged(QtGraphs3D::RenderingMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem20renderingModeChangedEN10QtGraphs3D13R'
        'enderingModeE',
        mode.value,
    )

  @overload(QtGraphs3D.TransparencyTechnique)
  def transparencyTechniqueChanged(
      self,
      technique: QtGraphs3D.TransparencyTechnique,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::transparencyTechniqueChanged(QtGraphs3D::
    TransparencyTechnique technique)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#transparencyTechniqueChanged

    Parameters
    ----------

    technique : QtGraphs3D.TransparencyTechnique
      Passed on as its number.
    """
    #  void QQuickGraphsItem::transparencyTechniqueChanged(QtGraphs3D::
    #      TransparencyTechnique technique)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem28transparencyTechniqueChangedEN10QtGra'
        'phs3D21TransparencyTechniqueE',
        technique.value,
    )

  @overload(bool)
  def measureFpsChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::measureFpsChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#measureFpsChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::measureFpsChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem17measureFpsChangedEb', enabled,
    )

  @overload(int)
  def currentFpsChanged(self, fps: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::currentFpsChanged(int fps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#currentFpsChanged

    Parameters
    ----------

    fps : int
      Passed on as it is.
    """
    #  void QQuickGraphsItem::currentFpsChanged(int fps)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem17currentFpsChangedEi', fps,
    )

  @overload(QtGraphs3D.ElementType)
  def selectedElementChanged(self, type: QtGraphs3D.ElementType) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::selectedElementChanged(QtGraphs3D::ElementType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#selectedElementChanged

    Parameters
    ----------

    type : QtGraphs3D.ElementType
      Passed on as its number.
    """
    #  void QQuickGraphsItem::selectedElementChanged(QtGraphs3D::ElementType
    #      type)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22selectedElementChangedEN10QtGraphs3D1'
        '1ElementTypeE',
        type.value,
    )

  @overload(bool)
  def orthoProjectionChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::orthoProjectionChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#orthoProjectionChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::orthoProjectionChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22orthoProjectionChangedEb', enabled,
    )

  @overload(float)
  def aspectRatioChanged(self, ratio: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::aspectRatioChanged(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#aspectRatioChanged

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::aspectRatioChanged(qreal ratio)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18aspectRatioChangedEd', ratio,
    )

  @overload(QtGraphs3D.OptimizationHint)
  def optimizationHintChanged(
      self,
      hint: QtGraphs3D.OptimizationHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::optimizationHintChanged(QtGraphs3D::OptimizationHint
    hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#optimizationHintChanged

    Parameters
    ----------

    hint : QtGraphs3D.OptimizationHint
      Passed on as its number.
    """
    #  void QQuickGraphsItem::optimizationHintChanged(QtGraphs3D::
    #      OptimizationHint hint)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23optimizationHintChangedEN10QtGraphs3D'
        '16OptimizationHintE',
        hint.value,
    )

  @overload(bool)
  def polarChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::polarChanged(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#polarChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::polarChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12polarChangedEb', enabled,
    )

  @overload(float)
  def labelMarginChanged(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::labelMarginChanged(float margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#labelMarginChanged

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::labelMarginChanged(float margin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18labelMarginChangedEf', margin,
    )

  @overload(float)
  def radialLabelOffsetChanged(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::radialLabelOffsetChanged(float
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#radialLabelOffsetChanged

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::radialLabelOffsetChanged(float offset)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24radialLabelOffsetChangedEf', offset,
    )

  @overload(float)
  def horizontalAspectRatioChanged(self, ratio: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::horizontalAspectRatioChanged(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#horizontalAspectRatioChanged

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::horizontalAspectRatioChanged(qreal ratio)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem28horizontalAspectRatioChangedEd', ratio,
    )

  @overload(QLocale)
  def localeChanged(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::localeChanged(const QLocale &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#localeChanged

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::localeChanged(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem13localeChangedERK7QLocale',
        self._valueOf(locale),
    )

  @overload(QVector3D)
  def queriedGraphPositionChanged(self, data: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::queriedGraphPositionChanged(QVector3D
    data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#queriedGraphPositionChanged

    Parameters
    ----------

    data : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::queriedGraphPositionChanged(QVector3D data)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem27queriedGraphPositionChangedE9QVector3'
        'D',
        self._valueOf(data),
    )

  @overload(float)
  def marginChanged(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::marginChanged(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#marginChanged

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::marginChanged(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem13marginChangedEd', margin,
    )

  @overload(float)
  def cutoffMarginChanged(self, newMargin: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::cutoffMarginChanged(qreal newMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cutoffMarginChanged

    Parameters
    ----------

    newMargin : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::cutoffMarginChanged(qreal newMargin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem19cutoffMarginChangedEd', newMargin,
    )

  @overload(QtGraphs3D.CameraPreset)
  def cameraPresetChanged(self, preset: QtGraphs3D.CameraPreset) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::cameraPresetChanged(QtGraphs3D::CameraPreset preset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraPresetChanged

    Parameters
    ----------

    preset : QtGraphs3D.CameraPreset
      Passed on as its number.
    """
    #  void QQuickGraphsItem::cameraPresetChanged(QtGraphs3D::CameraPreset
    #      preset)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem19cameraPresetChangedEN10QtGraphs3D12Ca'
        'meraPresetE',
        preset.value,
    )

  @overload(float)
  def cameraXRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::cameraXRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraXRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::cameraXRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22cameraXRotationChangedEf', rotation,
    )

  @overload(float)
  def cameraYRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::cameraYRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraYRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::cameraYRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22cameraYRotationChangedEf', rotation,
    )

  @overload(float)
  def cameraZoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::cameraZoomLevelChanged(float
    zoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraZoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::cameraZoomLevelChanged(float zoomLevel)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22cameraZoomLevelChangedEf', zoomLevel,
    )

  @overload(QVector3D)
  def cameraTargetPositionChanged(self, target: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::cameraTargetPositionChanged(QVector3D
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#cameraTargetPositionChanged

    Parameters
    ----------

    target : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::cameraTargetPositionChanged(QVector3D target)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem27cameraTargetPositionChangedE9QVector3'
        'D',
        self._valueOf(target),
    )

  @overload(float)
  def minCameraZoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::minCameraZoomLevelChanged(float
    zoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#minCameraZoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::minCameraZoomLevelChanged(float zoomLevel)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25minCameraZoomLevelChangedEf',
        zoomLevel,
    )

  @overload(float)
  def maxCameraZoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::maxCameraZoomLevelChanged(float
    zoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#maxCameraZoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::maxCameraZoomLevelChanged(float zoomLevel)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25maxCameraZoomLevelChangedEf',
        zoomLevel,
    )

  @overload(float)
  def minCameraXRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::minCameraXRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#minCameraXRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::minCameraXRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25minCameraXRotationChangedEf', rotation,
    )

  @overload(float)
  def minCameraYRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::minCameraYRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#minCameraYRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::minCameraYRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25minCameraYRotationChangedEf', rotation,
    )

  @overload(float)
  def maxCameraXRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::maxCameraXRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#maxCameraXRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::maxCameraXRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25maxCameraXRotationChangedEf', rotation,
    )

  @overload(float)
  def maxCameraYRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::maxCameraYRotationChanged(float
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#maxCameraYRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::maxCameraYRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25maxCameraYRotationChangedEf', rotation,
    )

  @overload(bool)
  def wrapCameraXRotationChanged(self, wrap: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::wrapCameraXRotationChanged(bool
    wrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#wrapCameraXRotationChanged

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::wrapCameraXRotationChanged(bool wrap)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem26wrapCameraXRotationChangedEb', wrap,
    )

  @overload(bool)
  def wrapCameraYRotationChanged(self, wrap: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::wrapCameraYRotationChanged(bool
    wrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#wrapCameraYRotationChanged

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::wrapCameraYRotationChanged(bool wrap)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem26wrapCameraYRotationChangedEb', wrap,
    )

  def needRender(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::needRender()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#needRender
    """
    #  void QQuickGraphsItem::needRender()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem10needRenderEv')

  def themeTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::themeTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#themeTypeChanged
    """
    #  void QQuickGraphsItem::themeTypeChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem16themeTypeChangedEv')

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::axisXChanged(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::axisXChanged(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12axisXChangedEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::axisYChanged(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::axisYChanged(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12axisYChangedEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::axisZChanged(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::axisZChanged(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12axisZChangedEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QGraphsTheme)
  @overload(NoneType)
  def activeThemeChanged(self, activeTheme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::activeThemeChanged(QGraphsTheme
    *activeTheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#activeThemeChanged

    Parameters
    ----------

    activeTheme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::activeThemeChanged(QGraphsTheme *activeTheme)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18activeThemeChangedEP12QGraphsTheme',
        self._addressOf(activeTheme),
    )

  @overload(QEventPoint, Qt.MouseButton)
  def tapped(self, eventPoint: QEventPoint, button: Qt.MouseButton) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::tapped(QEventPoint eventPoint,
    Qt::MouseButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#tapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void QQuickGraphsItem::tapped(QEventPoint eventPoint, Qt::MouseButton
    #      button)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem6tappedE11QEventPointN2Qt11MouseButtonE',
        self._valueOf(eventPoint), button.value,
    )

  @overload(QEventPoint, Qt.MouseButton)
  def doubleTapped(
      self,
      eventPoint: QEventPoint,
      button: Qt.MouseButton,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::doubleTapped(QEventPoint eventPoint,
    Qt::MouseButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#doubleTapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void QQuickGraphsItem::doubleTapped(QEventPoint eventPoint,
    #      Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12doubleTappedE11QEventPointN2Qt11Mouse'
        'ButtonE',
        self._valueOf(eventPoint), button.value,
    )

  def longPressed(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::longPressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#longPressed
    """
    #  void QQuickGraphsItem::longPressed()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem11longPressedEv')

  @overload(QVector2D)
  def dragged(self, delta: QVector2D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::dragged(QVector2D delta)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#dragged

    Parameters
    ----------

    delta : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::dragged(QVector2D delta)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem7draggedE9QVector2D',
        self._valueOf(delta),
    )

  @overload(QQuickWheelEvent)
  @overload(NoneType)
  def wheel(self, event: Optional[QQuickWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::wheel(QQuickWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#wheel

    Parameters
    ----------

    event : Optional[QQuickWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::wheel(QQuickWheelEvent *event)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem5wheelEP16QQuickWheelEvent',
        self._addressOf(event),
    )

  @overload(float)
  def pinch(self, delta: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::pinch(qreal delta)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#pinch

    Parameters
    ----------

    delta : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::pinch(qreal delta)
    self.uglySide.call('ritual_ZN16QQuickGraphsItem5pinchEd', delta)

  @overload(QPoint)
  def mouseMove(self, mousePos: QPoint) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::mouseMove(QPoint mousePos)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#mouseMove

    Parameters
    ----------

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::mouseMove(QPoint mousePos)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem9mouseMoveE6QPoint',
        self._valueOf(mousePos),
    )

  @overload(bool)
  def zoomEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::zoomEnabledChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#zoomEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::zoomEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18zoomEnabledChangedEb', enable,
    )

  @overload(bool)
  def zoomAtTargetEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::zoomAtTargetEnabledChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#zoomAtTargetEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::zoomAtTargetEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem26zoomAtTargetEnabledChangedEb', enable,
    )

  @overload(bool)
  def rotationEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::rotationEnabledChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#rotationEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::rotationEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22rotationEnabledChangedEb', enable,
    )

  @overload(bool)
  def panEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::panEnabledChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#panEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::panEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem17panEnabledChangedEb', enable,
    )

  @overload(QtGraphs3D.DragMode)
  def dragModeChanged(self, newDragMode: QtGraphs3D.DragMode) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::dragModeChanged(QtGraphs3D::DragMode
    newDragMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#dragModeChanged

    Parameters
    ----------

    newDragMode : QtGraphs3D.DragMode
      Passed on as its number.
    """
    #  void QQuickGraphsItem::dragModeChanged(QtGraphs3D::DragMode
    #      newDragMode)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15dragModeChangedEN10QtGraphs3D8DragMod'
        'eE',
        newDragMode.value,
    )

  @overload(bool)
  def selectionEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::selectionEnabledChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#selectionEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::selectionEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23selectionEnabledChangedEb', enable,
    )

  def ambientLightStrengthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::ambientLightStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#ambientLightStrengthChanged
    """
    #  void QQuickGraphsItem::ambientLightStrengthChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem27ambientLightStrengthChangedEv',
    )

  def lightStrengthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::lightStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#lightStrengthChanged
    """
    #  void QQuickGraphsItem::lightStrengthChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem20lightStrengthChangedEv')

  def shadowStrengthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::shadowStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#shadowStrengthChanged
    """
    #  void QQuickGraphsItem::shadowStrengthChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem21shadowStrengthChangedEv',
    )

  def lightColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::lightColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#lightColorChanged
    """
    #  void QQuickGraphsItem::lightColorChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem17lightColorChangedEv')

  def gridLineTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::gridLineTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#gridLineTypeChanged
    """
    #  void QQuickGraphsItem::gridLineTypeChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem19gridLineTypeChangedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickGraphsItem::event(QEvent *event)
    ritual = 'ritual_ZN16QQuickGraphsItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def handleWindowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleWindowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleWindowChanged
    """
    #  void QQuickGraphsItem::handleWindowChanged()
    ritual = 'ritual_ZN16QQuickGraphsItem19handleWindowChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem19handleWindowChangedEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickGraphsItem::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN16QQuickGraphsItem10itemChangeEN10QQuickItem10ItemChangeE'
        'RKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem10itemChangeEN10QQuickItem10ItemC'
          'hangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def updateWindowParameters(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateWindowParameters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateWindowParameters
    """
    #  void QQuickGraphsItem::updateWindowParameters()
    ritual = 'ritual_ZN16QQuickGraphsItem22updateWindowParametersEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem22updateWindowParametersEv'
    self.uglySide.call(ritual)

  @overload(QtGraphs3D.SelectionFlags)
  def handleSelectionModeChange(
      self,
      mode: QtGraphs3D.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleSelectionModeChange(QtGraphs3D::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleSelectionModeChange

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsItem::handleSelectionModeChange(QtGraphs3D::
    #      SelectionFlags mode)
    ritual = (
        'ritual_ZN16QQuickGraphsItem25handleSelectionModeChangeE6QFlagsIN10'
        'QtGraphs3D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem25handleSelectionModeChangeE6QFla'
          'gsIN10QtGraphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(QtGraphs3D.ShadowQuality)
  def handleShadowQualityChange(
      self,
      quality: QtGraphs3D.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleShadowQualityChange(QtGraphs3D::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleShadowQualityChange

    Parameters
    ----------

    quality : QtGraphs3D.ShadowQuality
      Passed on as its number.
    """
    #  void QQuickGraphsItem::handleShadowQualityChange(QtGraphs3D::
    #      ShadowQuality quality)
    ritual = (
        'ritual_ZN16QQuickGraphsItem25handleShadowQualityChangeEN10QtGraphs'
        '3D13ShadowQualityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem25handleShadowQualityChangeEN10Qt'
          'Graphs3D13ShadowQualityE')
    self.uglySide.call(ritual, quality.value)

  @overload(QtGraphs3D.ElementType)
  def handleSelectedElementChange(
      self,
      type: QtGraphs3D.ElementType,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleSelectedElementChange(QtGraphs3D::ElementType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleSelectedElementChange

    Parameters
    ----------

    type : QtGraphs3D.ElementType
      Passed on as its number.
    """
    #  void QQuickGraphsItem::handleSelectedElementChange(QtGraphs3D::
    #      ElementType type)
    ritual = (
        'ritual_ZN16QQuickGraphsItem27handleSelectedElementChangeEN10QtGrap'
        'hs3D11ElementTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem27handleSelectedElementChangeEN10'
          'QtGraphs3D11ElementTypeE')
    self.uglySide.call(ritual, type.value)

  @overload(QtGraphs3D.OptimizationHint)
  def handleOptimizationHintChange(
      self,
      hint: QtGraphs3D.OptimizationHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleOptimizationHintChange(QtGraphs3D::
    OptimizationHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleOptimizationHintChange

    Parameters
    ----------

    hint : QtGraphs3D.OptimizationHint
      Passed on as its number.
    """
    #  void QQuickGraphsItem::handleOptimizationHintChange(QtGraphs3D::
    #      OptimizationHint hint)
    ritual = (
        'ritual_ZN16QQuickGraphsItem28handleOptimizationHintChangeEN10QtGra'
        'phs3D16OptimizationHintE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem28handleOptimizationHintChangeEN1'
          '0QtGraphs3D16OptimizationHintE')
    self.uglySide.call(ritual, hint.value)

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, ev: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::keyPressEvent(QKeyEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#keyPressEvent

    Parameters
    ----------

    ev : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::keyPressEvent(QKeyEvent *ev)
    ritual = 'ritual_ZN16QQuickGraphsItem13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  def handleThemeTypeChange(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleThemeTypeChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleThemeTypeChange
    """
    #  void QQuickGraphsItem::handleThemeTypeChange()
    ritual = 'ritual_ZN16QQuickGraphsItem21handleThemeTypeChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem21handleThemeTypeChangeEv'
    self.uglySide.call(ritual)

  def handleParentWidthChange(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleParentWidthChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleParentWidthChange
    """
    #  void QQuickGraphsItem::handleParentWidthChange()
    ritual = 'ritual_ZN16QQuickGraphsItem23handleParentWidthChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem23handleParentWidthChangeEv'
    self.uglySide.call(ritual)

  def handleParentHeightChange(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleParentHeightChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleParentHeightChange
    """
    #  void QQuickGraphsItem::handleParentHeightChange()
    ritual = 'ritual_ZN16QQuickGraphsItem24handleParentHeightChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem24handleParentHeightChangeEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#componentComplete
    """
    #  void QQuickGraphsItem::componentComplete()
    ritual = 'ritual_ZN16QQuickGraphsItem17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem17componentCompleteEv'
    self.uglySide.call(ritual)

  def checkSliceEnabled(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::checkSliceEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#checkSliceEnabled
    """
    #  void QQuickGraphsItem::checkSliceEnabled()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem17checkSliceEnabledEv')

  def isUserCameraRotationRange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isUserCameraRotationRange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isUserCameraRotationRange
    """
    #  bool QQuickGraphsItem::isUserCameraRotationRange()
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25isUserCameraRotationRangeEv',
    )

  def createSliceView(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::createSliceView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createSliceView
    """
    #  void QQuickGraphsItem::createSliceView()
    ritual = 'ritual_ZN16QQuickGraphsItem15createSliceViewEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem15createSliceViewEv'
    self.uglySide.call(ritual)

  @overload(QtGraphs3D.SliceCaptureType)
  def createOffscreenSliceView(
      self,
      sliceType: QtGraphs3D.SliceCaptureType,
  ) -> Optional[QQuick3DViewport]:
    """
    Calls Qt's 'QQuick3DViewport
    *QQuickGraphsItem::createOffscreenSliceView(QtGraphs3D::SliceCaptureType
    sliceType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createOffscreenSliceView

    Parameters
    ----------

    sliceType : QtGraphs3D.SliceCaptureType
      Passed on as its number.

    Returns
    -------

    Optional[QQuick3DViewport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DViewport
    #      *QQuickGraphsItem::createOffscreenSliceView(QtGraphs3D::
    #      SliceCaptureType sliceType)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem24createOffscreenSliceViewEN10QtGraphs3'
        'D16SliceCaptureTypeE',
        sliceType.value,
    )
    from ..QtQuick3D import QQuick3DViewport
    return QQuick3DViewport._cuteAt(address)

  @overload(QPoint)
  def handleGraphQueryPositionChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handleGraphQueryPositionChanged(QPoint
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::handleGraphQueryPositionChanged(QPoint
    #      position)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem31handleGraphQueryPositionChangedE6QPoi'
        'nt',
        self._valueOf(position),
    )

  @overload(QPoint)
  def handleSelectionQueryPositionChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleSelectionQueryPositionChanged(QPoint position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::handleSelectionQueryPositionChanged(QPoint
    #      position)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem35handleSelectionQueryPositionChangedE6'
        'QPoint',
        self._valueOf(position),
    )

  @overload(QRect)
  def handlePrimarySubViewportChanged(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::handlePrimarySubViewportChanged(const
    QRect rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QQuickGraphsItem::handlePrimarySubViewportChanged(const QRect
    #      rect)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem31handlePrimarySubViewportChangedE5QRec'
        't',
        self._valueOf(rect),
    )

  @overload(QRect)
  def handleSecondarySubViewportChanged(self, rect: QRect) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleSecondarySubViewportChanged(const QRect rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QQuickGraphsItem::handleSecondarySubViewportChanged(const QRect
    #      rect)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem33handleSecondarySubViewportChangedE5QR'
        'ect',
        self._valueOf(rect),
    )

  def graphNode(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuickGraphsItem::graphNode()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#graphNode

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuickGraphsItem::graphNode()
    address = self.uglySide.call('ritual_ZN16QQuickGraphsItem9graphNodeEv')
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def sliceView(self) -> Optional[QQuick3DViewport]:
    """
    Calls Qt's 'QQuick3DViewport *QQuickGraphsItem::sliceView()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#sliceView

    Returns
    -------

    Optional[QQuick3DViewport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DViewport *QQuickGraphsItem::sliceView()
    address = self.uglySide.call('ritual_ZN16QQuickGraphsItem9sliceViewEv')
    from ..QtQuick3D import QQuick3DViewport
    return QQuick3DViewport._cuteAt(address)

  @overload(str)
  def createRepeaterDelegateComponent(
      self,
      fileName: str,
  ) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent
    *QQuickGraphsItem::createRepeaterDelegateComponent(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickGraphsItem::createRepeaterDelegateComponent(const
    #      QString &fileName)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem31createRepeaterDelegateComponentERK7QS'
        'tring',
        fileName,
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  @overload()
  @overload(QQuick3DNode)
  @overload(NoneType)
  def createRepeater(
      self,
      parent: Optional[QQuick3DNode] = None,
  ) -> Optional[QQuick3DRepeater]:
    """
    Calls Qt's 'QQuick3DRepeater
    *QQuickGraphsItem::createRepeater(QQuick3DNode *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createRepeater

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QQuick3DRepeater]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRepeater *QQuickGraphsItem::createRepeater(QQuick3DNode
    #      *parent)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem14createRepeaterEP12QQuick3DNode',
        self._addressOf(parent),
    )
    from ..QtQuick3D import QQuick3DRepeater
    return QQuick3DRepeater._cuteAt(address)

  @overload()
  @overload(QQuick3DNode)
  @overload(NoneType)
  def createTitleLabel(
      self,
      parent: Optional[QQuick3DNode] = None,
  ) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuickGraphsItem::createTitleLabel(QQuick3DNode
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createTitleLabel

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuickGraphsItem::createTitleLabel(QQuick3DNode *parent)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem16createTitleLabelEP12QQuick3DNode',
        self._addressOf(parent),
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def createItemLabel(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::createItemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createItemLabel
    """
    #  void QQuickGraphsItem::createItemLabel()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem15createItemLabelEv')

  @overload(QVector3D, QVector3D, QQuaternion, float, QVector3D)
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, QAbstract3DAxis,
  )
  @overload(QVector3D, QVector3D, QQuaternion, float, QVector3D, NoneType)
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, QAbstract3DAxis,
      QQuick3DNode,
  )
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, QAbstract3DAxis,
      NoneType,
  )
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, NoneType,
      QQuick3DNode,
  )
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, NoneType,
      NoneType,
  )
  def updateXTitle(
      self,
      labelRotation: QVector3D,
      labelTrans: QVector3D,
      totalRotation: QQuaternion,
      labelsMaxWidth: float,
      scale: QVector3D,
      axis: Optional[QAbstract3DAxis] = None,
      label: Optional[QQuick3DNode] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateXTitle(QVector3D labelRotation,
    QVector3D labelTrans, const QQuaternion &totalRotation, float
    labelsMaxWidth, QVector3D scale, QAbstract3DAxis *axis, QQuick3DNode
    *label)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#updateXTitle

    Parameters
    ----------

    labelRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    labelTrans : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    totalRotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    labelsMaxWidth : float
      Passed on as it is.

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    label : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickGraphsItem::updateXTitle(QVector3D labelRotation, QVector3D
    #      labelTrans, const QQuaternion &totalRotation, float
    #      labelsMaxWidth, QVector3D scale, QAbstract3DAxis *axis,
    #      QQuick3DNode *label)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12updateXTitleE9QVector3DS0_RK11QQuater'
        'nionfS0_P15QAbstract3DAxisP12QQuick3DNode',
        self._valueOf(labelRotation), self._valueOf(labelTrans),
        self._valueOf(totalRotation), labelsMaxWidth, self._valueOf(scale),
        self._addressOf(axis), self._addressOf(label),
    )

  @overload(
      QVector3D, QVector3D, QVector3D, QVector3D, QQuaternion, QQuaternion,
      float, QVector3D,
  )
  @overload(
      QVector3D, QVector3D, QVector3D, QVector3D, QQuaternion, QQuaternion,
      float, QVector3D, QAbstract3DAxis,
  )
  @overload(
      QVector3D, QVector3D, QVector3D, QVector3D, QQuaternion, QQuaternion,
      float, QVector3D, NoneType,
  )
  @overload(
      QVector3D, QVector3D, QVector3D, QVector3D, QQuaternion, QQuaternion,
      float, QVector3D, QAbstract3DAxis, QQuick3DNode,
  )
  @overload(
      QVector3D, QVector3D, QVector3D, QVector3D, QQuaternion, QQuaternion,
      float, QVector3D, QAbstract3DAxis, NoneType,
  )
  @overload(
      QVector3D, QVector3D, QVector3D, QVector3D, QQuaternion, QQuaternion,
      float, QVector3D, NoneType, QQuick3DNode,
  )
  @overload(
      QVector3D, QVector3D, QVector3D, QVector3D, QQuaternion, QQuaternion,
      float, QVector3D, NoneType, NoneType,
  )
  def updateYTitle(
      self,
      sideLabelRotation: QVector3D,
      backLabelRotation: QVector3D,
      sideLabelTrans: QVector3D,
      backLabelTrans: QVector3D,
      totalSideRotation: QQuaternion,
      totalBackRotation: QQuaternion,
      labelsMaxWidth: float,
      scale: QVector3D,
      axis: Optional[QAbstract3DAxis] = None,
      label: Optional[QQuick3DNode] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateYTitle(QVector3D
    sideLabelRotation, QVector3D backLabelRotation, QVector3D sideLabelTrans,
    QVector3D backLabelTrans, const QQuaternion &totalSideRotation, const
    QQuaternion &totalBackRotation, float labelsMaxWidth, QVector3D scale,
    QAbstract3DAxis *axis, QQuick3DNode *label)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#updateYTitle

    Parameters
    ----------

    sideLabelRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    backLabelRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    sideLabelTrans : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    backLabelTrans : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    totalSideRotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    totalBackRotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    labelsMaxWidth : float
      Passed on as it is.

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    label : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickGraphsItem::updateYTitle(QVector3D sideLabelRotation,
    #      QVector3D backLabelRotation, QVector3D sideLabelTrans, QVector3D
    #      backLabelTrans, const QQuaternion &totalSideRotation, const
    #      QQuaternion &totalBackRotation, float labelsMaxWidth, QVector3D
    #      scale, QAbstract3DAxis *axis, QQuick3DNode *label)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12updateYTitleE9QVector3DS0_S0_S0_RK11Q'
        'QuaternionS3_fS0_P15QAbstract3DAxisP12QQuick3DNode',
        self._valueOf(sideLabelRotation), self._valueOf(backLabelRotation),
        self._valueOf(sideLabelTrans), self._valueOf(backLabelTrans),
        self._valueOf(totalSideRotation), self._valueOf(totalBackRotation),
        labelsMaxWidth, self._valueOf(scale), self._addressOf(axis),
        self._addressOf(label),
    )

  @overload(QVector3D, QVector3D, QQuaternion, float, QVector3D)
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, QAbstract3DAxis,
  )
  @overload(QVector3D, QVector3D, QQuaternion, float, QVector3D, NoneType)
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, QAbstract3DAxis,
      QQuick3DNode,
  )
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, QAbstract3DAxis,
      NoneType,
  )
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, NoneType,
      QQuick3DNode,
  )
  @overload(
      QVector3D, QVector3D, QQuaternion, float, QVector3D, NoneType,
      NoneType,
  )
  def updateZTitle(
      self,
      labelRotation: QVector3D,
      labelTrans: QVector3D,
      totalRotation: QQuaternion,
      labelsMaxWidth: float,
      scale: QVector3D,
      axis: Optional[QAbstract3DAxis] = None,
      label: Optional[QQuick3DNode] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateZTitle(QVector3D labelRotation,
    QVector3D labelTrans, const QQuaternion &totalRotation, float
    labelsMaxWidth, QVector3D scale, QAbstract3DAxis *axis, QQuick3DNode
    *label)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#updateZTitle

    Parameters
    ----------

    labelRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    labelTrans : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    totalRotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    labelsMaxWidth : float
      Passed on as it is.

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    label : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickGraphsItem::updateZTitle(QVector3D labelRotation, QVector3D
    #      labelTrans, const QQuaternion &totalRotation, float
    #      labelsMaxWidth, QVector3D scale, QAbstract3DAxis *axis,
    #      QQuick3DNode *label)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem12updateZTitleE9QVector3DS0_RK11QQuater'
        'nionfS0_P15QAbstract3DAxisP12QQuick3DNode',
        self._valueOf(labelRotation), self._valueOf(labelTrans),
        self._valueOf(totalRotation), labelsMaxWidth, self._valueOf(scale),
        self._addressOf(axis), self._addressOf(label),
    )

  def calculateSceneScalingFactors(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::calculateSceneScalingFactors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#calculateSceneScalingFactors
    """
    #  void QQuickGraphsItem::calculateSceneScalingFactors()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem28calculateSceneScalingFactorsEv',
    )

  @overload(QQuick3DNode, QVector3D, QVector3D)
  @overload(NoneType, QVector3D, QVector3D)
  def positionAndScaleLine(
      self,
      lineNode: Optional[QQuick3DNode],
      scale: QVector3D,
      position: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::positionAndScaleLine(QQuick3DNode
    *lineNode, QVector3D scale, QVector3D position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#positionAndScaleLine

    Parameters
    ----------

    lineNode : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::positionAndScaleLine(QQuick3DNode *lineNode,
    #      QVector3D scale, QVector3D position)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem20positionAndScaleLineEP12QQuick3DNode9'
        'QVector3DS2_',
        self._addressOf(lineNode), self._valueOf(scale),
        self._valueOf(position),
    )

  @overload(QStringList)
  def findLabelsMaxWidth(self, labels: QStringList) -> int:
    """
    Calls Qt's 'int QQuickGraphsItem::findLabelsMaxWidth(const QStringList
    &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#findLabelsMaxWidth

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  int QQuickGraphsItem::findLabelsMaxWidth(const QStringList &labels)
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18findLabelsMaxWidthERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(QAbstract3DAxis, QVector3D, int)
  @overload(NoneType, QVector3D, int)
  def calculateCategoryLabelPosition(
      self,
      axis: Optional[QAbstract3DAxis],
      labelPosition: QVector3D,
      index: int,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QQuickGraphsItem::calculateCategoryLabelPosition(QAbstract3DAxis *axis,
    QVector3D labelPosition, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    labelPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    index : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D
    #      QQuickGraphsItem::calculateCategoryLabelPosition(QAbstract3DAxis
    #      *axis, QVector3D labelPosition, int index)
    ritual = (
        'ritual_ZN16QQuickGraphsItem30calculateCategoryLabelPositionEP15QAb'
        'stract3DAxis9QVector3Di')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem30calculateCategoryLabelPositionE'
          'P15QAbstract3DAxis9QVector3Di')
    address = self.uglySide.call(
        ritual, self._addressOf(axis), self._valueOf(labelPosition), index,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QAbstract3DAxis, int)
  @overload(NoneType, int)
  def calculateCategoryGridLinePosition(
      self,
      axis: Optional[QAbstract3DAxis],
      index: int,
  ) -> float:
    """
    Calls Qt's 'float
    QQuickGraphsItem::calculateCategoryGridLinePosition(QAbstract3DAxis
    *axis, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  float QQuickGraphsItem::calculateCategoryGridLinePosition(
    #      QAbstract3DAxis *axis, int index)
    ritual = (
        'ritual_ZN16QQuickGraphsItem33calculateCategoryGridLinePositionEP15'
        'QAbstract3DAxisi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem33calculateCategoryGridLinePositi'
          'onEP15QAbstract3DAxisi')
    return self.uglySide.call(ritual, self._addressOf(axis), index)

  def calculatePolarBackgroundMargin(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::calculatePolarBackgroundMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html
    """
    #  float QQuickGraphsItem::calculatePolarBackgroundMargin()
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem30calculatePolarBackgroundMarginEv',
    )

  def updateGrid(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateGrid()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#updateGrid
    """
    #  void QQuickGraphsItem::updateGrid()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem10updateGridEv')

  def updateGridLineType(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateGridLineType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateGridLineType
    """
    #  void QQuickGraphsItem::updateGridLineType()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem18updateGridLineTypeEv')

  def updateLabels(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateLabels()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#updateLabels
    """
    #  void QQuickGraphsItem::updateLabels()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem12updateLabelsEv')

  @overload(float, float, float, Qt.Axis)
  def calculateLabelRotation(
      self,
      labelAutoAngle: float,
      fractionCamX: float,
      fractionCamY: float,
      axis: Qt.Axis,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::calculateLabelRotation(float
    labelAutoAngle, float fractionCamX, float fractionCamY, Qt::Axis axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#calculateLabelRotation

    Parameters
    ----------

    labelAutoAngle : float
      Passed on as it is.

    fractionCamX : float
      Passed on as it is.

    fractionCamY : float
      Passed on as it is.

    axis : Qt.Axis
      Passed on as its number.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::calculateLabelRotation(float
    #      labelAutoAngle, float fractionCamX, float fractionCamY, Qt::Axis
    #      axis)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22calculateLabelRotationEfffN2Qt4AxisE',
        labelAutoAngle, fractionCamX, fractionCamY, axis.value,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(float)
  def calculateLabelRotation(self, labelAutoAngle: float) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::calculateLabelRotation(float
    labelAutoAngle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#calculateLabelRotation

    Parameters
    ----------

    labelAutoAngle : float
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::calculateLabelRotation(float
    #      labelAutoAngle)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22calculateLabelRotationEf',
        labelAutoAngle,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload()
  @overload(QQuick3DModel)
  @overload(NoneType)
  @overload(QQuick3DModel, QtGraphs3D.SliceCaptureType)
  @overload(NoneType, QtGraphs3D.SliceCaptureType)
  def updateSliceGrid(
      self,
      sliceGrid: Optional[QQuick3DModel] = None,
      selectedFlag: QtGraphs3D.SliceCaptureType = (
          QtGraphs3D.SliceCaptureType.NoImage),
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateSliceGrid(QQuick3DModel
    *sliceGrid, QtGraphs3D::SliceCaptureType selectedFlag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateSliceGrid

    Parameters
    ----------

    sliceGrid : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    selectedFlag : QtGraphs3D.SliceCaptureType
      Passed on as its number. May be left out, as in Qt: it is then
      QtGraphs3D.SliceCaptureType.NoImage.
    """
    #  void QQuickGraphsItem::updateSliceGrid(QQuick3DModel *sliceGrid,
    #      QtGraphs3D::SliceCaptureType selectedFlag)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15updateSliceGridEP13QQuick3DModelN10Qt'
        'Graphs3D16SliceCaptureTypeE',
        self._addressOf(sliceGrid), selectedFlag.value,
    )

  @overload()
  @overload(QQuick3DRepeater)
  @overload(NoneType)
  @overload(QQuick3DRepeater, QQuick3DRepeater)
  @overload(QQuick3DRepeater, NoneType)
  @overload(NoneType, QQuick3DRepeater)
  @overload(NoneType, NoneType)
  @overload(QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode)
  @overload(QQuick3DRepeater, QQuick3DRepeater, NoneType)
  @overload(QQuick3DRepeater, NoneType, QQuick3DNode)
  @overload(QQuick3DRepeater, NoneType, NoneType)
  @overload(NoneType, QQuick3DRepeater, QQuick3DNode)
  @overload(NoneType, QQuick3DRepeater, NoneType)
  @overload(NoneType, NoneType, QQuick3DNode)
  @overload(NoneType, NoneType, NoneType)
  @overload(QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, QQuick3DNode)
  @overload(QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, NoneType)
  @overload(QQuick3DRepeater, QQuick3DRepeater, NoneType, QQuick3DNode)
  @overload(QQuick3DRepeater, QQuick3DRepeater, NoneType, NoneType)
  @overload(QQuick3DRepeater, NoneType, QQuick3DNode, QQuick3DNode)
  @overload(QQuick3DRepeater, NoneType, QQuick3DNode, NoneType)
  @overload(QQuick3DRepeater, NoneType, NoneType, QQuick3DNode)
  @overload(QQuick3DRepeater, NoneType, NoneType, NoneType)
  @overload(NoneType, QQuick3DRepeater, QQuick3DNode, QQuick3DNode)
  @overload(NoneType, QQuick3DRepeater, QQuick3DNode, NoneType)
  @overload(NoneType, QQuick3DRepeater, NoneType, QQuick3DNode)
  @overload(NoneType, QQuick3DRepeater, NoneType, NoneType)
  @overload(NoneType, NoneType, QQuick3DNode, QQuick3DNode)
  @overload(NoneType, NoneType, QQuick3DNode, NoneType)
  @overload(NoneType, NoneType, NoneType, QQuick3DNode)
  @overload(NoneType, NoneType, NoneType, NoneType)
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, QQuick3DNode,
      QQuick3DNode,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, QQuick3DNode,
      NoneType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, NoneType,
      QQuick3DNode,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, NoneType, NoneType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, NoneType, QQuick3DNode,
      QQuick3DNode,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, NoneType, QQuick3DNode, NoneType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, NoneType, NoneType, QQuick3DNode,
  )
  @overload(QQuick3DRepeater, QQuick3DRepeater, NoneType, NoneType, NoneType)
  @overload(
      QQuick3DRepeater, NoneType, QQuick3DNode, QQuick3DNode, QQuick3DNode,
  )
  @overload(QQuick3DRepeater, NoneType, QQuick3DNode, QQuick3DNode, NoneType)
  @overload(QQuick3DRepeater, NoneType, QQuick3DNode, NoneType, QQuick3DNode)
  @overload(QQuick3DRepeater, NoneType, QQuick3DNode, NoneType, NoneType)
  @overload(QQuick3DRepeater, NoneType, NoneType, QQuick3DNode, QQuick3DNode)
  @overload(QQuick3DRepeater, NoneType, NoneType, QQuick3DNode, NoneType)
  @overload(QQuick3DRepeater, NoneType, NoneType, NoneType, QQuick3DNode)
  @overload(QQuick3DRepeater, NoneType, NoneType, NoneType, NoneType)
  @overload(
      NoneType, QQuick3DRepeater, QQuick3DNode, QQuick3DNode, QQuick3DNode,
  )
  @overload(NoneType, QQuick3DRepeater, QQuick3DNode, QQuick3DNode, NoneType)
  @overload(NoneType, QQuick3DRepeater, QQuick3DNode, NoneType, QQuick3DNode)
  @overload(NoneType, QQuick3DRepeater, QQuick3DNode, NoneType, NoneType)
  @overload(NoneType, QQuick3DRepeater, NoneType, QQuick3DNode, QQuick3DNode)
  @overload(NoneType, QQuick3DRepeater, NoneType, QQuick3DNode, NoneType)
  @overload(NoneType, QQuick3DRepeater, NoneType, NoneType, QQuick3DNode)
  @overload(NoneType, QQuick3DRepeater, NoneType, NoneType, NoneType)
  @overload(NoneType, NoneType, QQuick3DNode, QQuick3DNode, QQuick3DNode)
  @overload(NoneType, NoneType, QQuick3DNode, QQuick3DNode, NoneType)
  @overload(NoneType, NoneType, QQuick3DNode, NoneType, QQuick3DNode)
  @overload(NoneType, NoneType, QQuick3DNode, NoneType, NoneType)
  @overload(NoneType, NoneType, NoneType, QQuick3DNode, QQuick3DNode)
  @overload(NoneType, NoneType, NoneType, QQuick3DNode, NoneType)
  @overload(NoneType, NoneType, NoneType, NoneType, QQuick3DNode)
  @overload(NoneType, NoneType, NoneType, NoneType, NoneType)
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, QQuick3DNode,
      QQuick3DNode, QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, QQuick3DNode,
      NoneType, QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, NoneType,
      QQuick3DNode, QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, QQuick3DNode, NoneType, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, NoneType, QQuick3DNode,
      QQuick3DNode, QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, NoneType, QQuick3DNode, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, NoneType, NoneType, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, QQuick3DRepeater, NoneType, NoneType, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, NoneType, QQuick3DNode, QQuick3DNode, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, NoneType, QQuick3DNode, QQuick3DNode, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, NoneType, QQuick3DNode, NoneType, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, NoneType, QQuick3DNode, NoneType, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, NoneType, NoneType, QQuick3DNode, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, NoneType, NoneType, QQuick3DNode, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, NoneType, NoneType, NoneType, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      QQuick3DRepeater, NoneType, NoneType, NoneType, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, QQuick3DRepeater, QQuick3DNode, QQuick3DNode, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, QQuick3DRepeater, QQuick3DNode, QQuick3DNode, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, QQuick3DRepeater, QQuick3DNode, NoneType, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, QQuick3DRepeater, QQuick3DNode, NoneType, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, QQuick3DRepeater, NoneType, QQuick3DNode, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, QQuick3DRepeater, NoneType, QQuick3DNode, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, QQuick3DRepeater, NoneType, NoneType, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, QQuick3DRepeater, NoneType, NoneType, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, NoneType, QQuick3DNode, QQuick3DNode, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, NoneType, QQuick3DNode, QQuick3DNode, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, NoneType, QQuick3DNode, NoneType, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, NoneType, QQuick3DNode, NoneType, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, NoneType, NoneType, QQuick3DNode, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, NoneType, NoneType, QQuick3DNode, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, NoneType, NoneType, NoneType, QQuick3DNode,
      QtGraphs3D.SliceCaptureType,
  )
  @overload(
      NoneType, NoneType, NoneType, NoneType, NoneType,
      QtGraphs3D.SliceCaptureType,
  )
  def updateSliceLabels(
      self,
      horizontalLabel: Optional[QQuick3DRepeater] = None,
      verticalLabel: Optional[QQuick3DRepeater] = None,
      horizontalTitle: Optional[QQuick3DNode] = None,
      verticalTitle: Optional[QQuick3DNode] = None,
      itemLabel: Optional[QQuick3DNode] = None,
      selectedFlag: QtGraphs3D.SliceCaptureType = (
          QtGraphs3D.SliceCaptureType.NoImage),
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateSliceLabels(QQuick3DRepeater
    *horizontalLabel, QQuick3DRepeater *verticalLabel, QQuick3DNode
    *horizontalTitle, QQuick3DNode *verticalTitle, QQuick3DNode *itemLabel,
    QtGraphs3D::SliceCaptureType selectedFlag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateSliceLabels

    Parameters
    ----------

    horizontalLabel : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    verticalLabel : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    horizontalTitle : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    verticalTitle : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    itemLabel : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    selectedFlag : QtGraphs3D.SliceCaptureType
      Passed on as its number. May be left out, as in Qt: it is then
      QtGraphs3D.SliceCaptureType.NoImage.
    """
    #  void QQuickGraphsItem::updateSliceLabels(QQuick3DRepeater
    #      *horizontalLabel, QQuick3DRepeater *verticalLabel, QQuick3DNode
    #      *horizontalTitle, QQuick3DNode *verticalTitle, QQuick3DNode
    #      *itemLabel, QtGraphs3D::SliceCaptureType selectedFlag)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem17updateSliceLabelsEP16QQuick3DRepeater'
        'S1_P12QQuick3DNodeS3_S3_N10QtGraphs3D16SliceCaptureTypeE',
        self._addressOf(horizontalLabel), self._addressOf(verticalLabel),
        self._addressOf(horizontalTitle), self._addressOf(verticalTitle),
        self._addressOf(itemLabel), selectedFlag.value,
    )

  def updateBackgroundColor(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateBackgroundColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateBackgroundColor
    """
    #  void QQuickGraphsItem::updateBackgroundColor()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem21updateBackgroundColorEv',
    )

  @overload(QtGraphs3D.ShadowQuality)
  def updateShadowQuality(self, quality: QtGraphs3D.ShadowQuality) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::updateShadowQuality(QtGraphs3D::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateShadowQuality

    Parameters
    ----------

    quality : QtGraphs3D.ShadowQuality
      Passed on as its number.
    """
    #  void QQuickGraphsItem::updateShadowQuality(QtGraphs3D::ShadowQuality
    #      quality)
    ritual = (
        'ritual_ZN16QQuickGraphsItem19updateShadowQualityEN10QtGraphs3D13Sh'
        'adowQualityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem19updateShadowQualityEN10QtGraphs'
          '3D13ShadowQualityE')
    self.uglySide.call(ritual, quality.value)

  @overload(QVector3D)
  def updateItemLabel(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateItemLabel(QVector3D position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateItemLabel

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::updateItemLabel(QVector3D position)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15updateItemLabelE9QVector3D',
        self._valueOf(position),
    )

  @overload(str, QVector3D)
  def updateSliceItemLabel(self, label: str, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateSliceItemLabel(const QString
    &label, QVector3D position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateSliceItemLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::updateSliceItemLabel(const QString &label,
    #      QVector3D position)
    ritual = (
        'ritual_ZN16QQuickGraphsItem20updateSliceItemLabelERK7QString9QVect'
        'or3D')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem20updateSliceItemLabelERK7QString'
          '9QVector3D')
    self.uglySide.call(ritual, label, self._valueOf(position))

  def synchData(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::synchData()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#synchData
    """
    #  void QQuickGraphsItem::synchData()
    ritual = 'ritual_ZN16QQuickGraphsItem9synchDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem9synchDataEv'
    self.uglySide.call(ritual)

  def updateGraph(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateGraph()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#updateGraph
    """
    #  void QQuickGraphsItem::updateGraph()
    ritual = 'ritual_ZN16QQuickGraphsItem11updateGraphEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem11updateGraphEv'
    self.uglySide.call(ritual)

  def toggleSliceGraph(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::toggleSliceGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#toggleSliceGraph
    """
    #  void QQuickGraphsItem::toggleSliceGraph()
    ritual = 'ritual_ZN16QQuickGraphsItem16toggleSliceGraphEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem16toggleSliceGraphEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DViewport)
  @overload(NoneType)
  def createSliceCamera(self, sliceView: Optional[QQuick3DViewport]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::createSliceCamera(QQuick3DViewport
    *sliceView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createSliceCamera

    Parameters
    ----------

    sliceView : Optional[QQuick3DViewport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::createSliceCamera(QQuick3DViewport *sliceView)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem17createSliceCameraEP16QQuick3DViewport',
        self._addressOf(sliceView),
    )

  @overload(float, float)
  def updateAxisRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateAxisRange(float min, float
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateAxisRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QQuickGraphsItem::updateAxisRange(float min, float max)
    ritual = 'ritual_ZN16QQuickGraphsItem15updateAxisRangeEff'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem15updateAxisRangeEff'
    self.uglySide.call(ritual, min, max)

  @overload(bool)
  def updateAxisReversed(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateAxisReversed(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateAxisReversed

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsItem::updateAxisReversed(bool enable)
    ritual = 'ritual_ZN16QQuickGraphsItem18updateAxisReversedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem18updateAxisReversedEb'
    self.uglySide.call(ritual, enable)

  def updateSingleHighlightColor(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateSingleHighlightColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateSingleHighlightColor
    """
    #  void QQuickGraphsItem::updateSingleHighlightColor()
    ritual = 'ritual_ZN16QQuickGraphsItem26updateSingleHighlightColorEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem26updateSingleHighlightColorEv')
    self.uglySide.call(ritual)

  def updateLightStrength(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateLightStrength()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateLightStrength
    """
    #  void QQuickGraphsItem::updateLightStrength()
    ritual = 'ritual_ZN16QQuickGraphsItem19updateLightStrengthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsItem19updateLightStrengthEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DRepeater, QColor)
  @overload(NoneType, QColor)
  def handleLabelCountChanged(
      self,
      repeater: Optional[QQuick3DRepeater],
      axisLabelColor: QColor,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::handleLabelCountChanged(QQuick3DRepeater *repeater,
    QColor axisLabelColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#handleLabelCountChanged

    Parameters
    ----------

    repeater : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    axisLabelColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickGraphsItem::handleLabelCountChanged(QQuick3DRepeater
    #      *repeater, QColor axisLabelColor)
    ritual = (
        'ritual_ZN16QQuickGraphsItem23handleLabelCountChangedEP16QQuick3DRe'
        'peater6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem23handleLabelCountChangedEP16QQui'
          'ck3DRepeater6QColor')
    self.uglySide.call(
        ritual, self._addressOf(repeater), self._valueOf(axisLabelColor),
    )

  def updateMultiAxis(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateMultiAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateMultiAxis
    """
    #  void QQuickGraphsItem::updateMultiAxis()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem15updateMultiAxisEv')

  @overload(int, QAbstract3DAxis)
  @overload(int, NoneType)
  def updateMultiAxisLabels(
      self,
      axisIndex: int,
      axis: Optional[QAbstract3DAxis],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateMultiAxisLabels(qsizetype
    axisIndex, QAbstract3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateMultiAxisLabels

    Parameters
    ----------

    axisIndex : int
      Passed on as it is.

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::updateMultiAxisLabels(qsizetype axisIndex,
    #      QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem21updateMultiAxisLabelsExP15QAbstract3D'
        'Axis',
        axisIndex, self._addressOf(axis),
    )

  @overload(int, QAbstract3DAxis)
  @overload(int, NoneType)
  def updateMultiAxisGrid(
      self,
      axisIndex: int,
      axis: Optional[QAbstract3DAxis],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateMultiAxisGrid(qsizetype
    axisIndex, QAbstract3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateMultiAxisGrid

    Parameters
    ----------

    axisIndex : int
      Passed on as it is.

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::updateMultiAxisGrid(qsizetype axisIndex,
    #      QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem19updateMultiAxisGridExP15QAbstract3DAx'
        'is',
        axisIndex, self._addressOf(axis),
    )

  @overload(QAbstract3DAxis.AxisOrientation, int)
  def releaseMultiAxis(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      index: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsItem::releaseMultiAxis(QAbstract3DAxis::AxisOrientation
    orientation, qsizetype index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#releaseMultiAxis

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    index : int
      Passed on as it is.
    """
    #  void QQuickGraphsItem::releaseMultiAxis(QAbstract3DAxis::
    #      AxisOrientation orientation, qsizetype index)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem16releaseMultiAxisEN15QAbstract3DAxis15'
        'AxisOrientationEx',
        orientation.value, index,
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def connectMultiAxis(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::connectMultiAxis(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#connectMultiAxis

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsItem::connectMultiAxis(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem16connectMultiAxisEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DSeries, QAbstract3DAxis.AxisOrientation)
  @overload(NoneType, QAbstract3DAxis.AxisOrientation)
  def getSeriesMultiAxis(
      self,
      series: Optional[QAbstract3DSeries],
      orientation: QAbstract3DAxis.AxisOrientation,
  ) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis
    *QQuickGraphsItem::getSeriesMultiAxis(QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#getSeriesMultiAxis

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis
    #      *QQuickGraphsItem::getSeriesMultiAxis(QAbstract3DSeries *series,
    #      QAbstract3DAxis::AxisOrientation orientation)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18getSeriesMultiAxisEP17QAbstract3DSeri'
        'esN15QAbstract3DAxis15AxisOrientationE',
        self._addressOf(series), orientation.value,
    )
    return QAbstract3DAxis._cuteAt(address)

  def isGridUpdated(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsItem::isGridUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#isGridUpdated
    """
    #  bool QQuickGraphsItem::isGridUpdated()
    return self.uglySide.call('ritual_ZN16QQuickGraphsItem13isGridUpdatedEv')

  @overload(QAbstract3DAxis.AxisOrientation)
  def createDefaultAxis(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
  ) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis
    *QQuickGraphsItem::createDefaultAxis(QAbstract3DAxis::AxisOrientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createDefaultAxis

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *QQuickGraphsItem::createDefaultAxis(QAbstract3DAxis::
    #      AxisOrientation orientation)
    ritual = (
        'ritual_ZN16QQuickGraphsItem17createDefaultAxisEN15QAbstract3DAxis1'
        '5AxisOrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem17createDefaultAxisEN15QAbstract3'
          'DAxis15AxisOrientationE')
    address = self.uglySide.call(ritual, orientation.value)
    return QAbstract3DAxis._cuteAt(address)

  def createDefaultValueAxis(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsItem::createDefaultValueAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createDefaultValueAxis

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsItem::createDefaultValueAxis()
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem22createDefaultValueAxisEv',
    )
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def createDefaultCategoryAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis
    *QQuickGraphsItem::createDefaultCategoryAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#createDefaultCategoryAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *QQuickGraphsItem::createDefaultCategoryAxis()
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem25createDefaultCategoryAxisEv',
    )
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def startRecordingRemovesAndInserts(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::startRecordingRemovesAndInserts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html
    """
    #  void QQuickGraphsItem::startRecordingRemovesAndInserts()
    ritual = 'ritual_ZN16QQuickGraphsItem31startRecordingRemovesAndInsertsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsItem31startRecordingRemovesAndInserts'
          'Ev')
    self.uglySide.call(ritual)

  def updateCamera(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateCamera()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsitem.html#updateCamera
    """
    #  void QQuickGraphsItem::updateCamera()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem12updateCameraEv')

  def updateRadialLabelOffset(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateRadialLabelOffset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateRadialLabelOffset
    """
    #  void QQuickGraphsItem::updateRadialLabelOffset()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem23updateRadialLabelOffsetEv',
    )

  def updateCustomData(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateCustomData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateCustomData
    """
    #  void QQuickGraphsItem::updateCustomData()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem16updateCustomDataEv')

  def updateCustomLabelsRotation(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateCustomLabelsRotation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateCustomLabelsRotation
    """
    #  void QQuickGraphsItem::updateCustomLabelsRotation()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem26updateCustomLabelsRotationEv',
    )

  @overload(float)
  def fontScaleFactor(self, pointSize: float) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::fontScaleFactor(float pointSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#fontScaleFactor

    Parameters
    ----------

    pointSize : float
      Passed on as it is.
    """
    #  float QQuickGraphsItem::fontScaleFactor(float pointSize)
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15fontScaleFactorEf', pointSize,
    )

  @overload(float)
  def labelAdjustment(self, width: float) -> float:
    """
    Calls Qt's 'float QQuickGraphsItem::labelAdjustment(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#labelAdjustment

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  float QQuickGraphsItem::labelAdjustment(float width)
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem15labelAdjustmentEf', width,
    )

  @overload(QVector3D)
  def graphPosToAbsolute(self, position: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsItem::graphPosToAbsolute(QVector3D
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#graphPosToAbsolute

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsItem::graphPosToAbsolute(QVector3D position)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsItem18graphPosToAbsoluteE9QVector3D',
        self._valueOf(position),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def updateSubViews(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateSubViews()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateSubViews
    """
    #  void QQuickGraphsItem::updateSubViews()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem14updateSubViewsEv')

  def updateCustomVolumes(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsItem::updateCustomVolumes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsitem.html#updateCustomVolumes
    """
    #  void QQuickGraphsItem::updateCustomVolumes()
    self.uglySide.call('ritual_ZN16QQuickGraphsItem19updateCustomVolumesEv')

  @staticmethod
  def appendCustomItemFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsItem::appendCustomItemFunc(QQmlListProperty<QCustom3DItem>
    *list, QCustom3DItem *item)': names 'QQmlListProperty<QCustom3DItem>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.appendCustomItemFunc' has no cute function yet. "
        "Qt's 'void "
        "QQuickGraphsItem::appendCustomItemFunc(QQmlListProperty<QCustom3DIt"
        "em> *list, QCustom3DItem *item)': names "
        "'QQmlListProperty<QCustom3DItem>', which has no cute class yet.")

  @staticmethod
  def atCustomItemFunc(*__, **_) -> Never:
    """
    Qt's 'QCustom3DItem
    *QQuickGraphsItem::atCustomItemFunc(QQmlListProperty<QCustom3DItem>
    *list, qsizetype index)': names 'QQmlListProperty<QCustom3DItem>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.atCustomItemFunc' has no cute function yet. Qt's "
        "'QCustom3DItem "
        "*QQuickGraphsItem::atCustomItemFunc(QQmlListProperty<QCustom3DItem>"
        " *list, qsizetype index)': names "
        "'QQmlListProperty<QCustom3DItem>', which has no cute class yet.")

  @staticmethod
  def clearCustomItemFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsItem::clearCustomItemFunc(QQmlListProperty<QCustom3DItem>
    *list)': names 'QQmlListProperty<QCustom3DItem>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.clearCustomItemFunc' has no cute function yet. "
        "Qt's 'void "
        "QQuickGraphsItem::clearCustomItemFunc(QQmlListProperty<QCustom3DIte"
        "m> *list)': names 'QQmlListProperty<QCustom3DItem>', which has no "
        "cute class yet.")

  @staticmethod
  def countCustomItemFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickGraphsItem::countCustomItemFunc(QQmlListProperty<QCustom3DItem>
    *list)': names 'QQmlListProperty<QCustom3DItem>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.countCustomItemFunc' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuickGraphsItem::countCustomItemFunc(QQmlListProperty<QCustom3DIte"
        "m> *list)': names 'QQmlListProperty<QCustom3DItem>', which has no "
        "cute class yet.")

  @staticmethod
  def createMultiAxis(*__, **_) -> Never:
    """
    Qt's 'MultiAxis QQuickGraphsItem::createMultiAxis(qsizetype axisIndex)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.createMultiAxis' has no cute function yet. Qt's "
        "'MultiAxis QQuickGraphsItem::createMultiAxis(qsizetype "
        "axisIndex)': gives a type Python has no way to take yet.")

  @staticmethod
  def createSliceFrame(*__, **_) -> Never:
    """
    Qt's 'QQuick3DModel *QQuickGraphsItem::createSliceFrame(Volume
    &volumeItem)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.createSliceFrame' has no cute function yet. Qt's "
        "'QQuick3DModel *QQuickGraphsItem::createSliceFrame(Volume "
        "&volumeItem)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createVolumeMaterial(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsItem::createVolumeMaterial(QCustom3DVolume
    *volume, Volume &volumeItem)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.createVolumeMaterial' has no cute function yet. "
        "Qt's 'void QQuickGraphsItem::createVolumeMaterial(QCustom3DVolume "
        "*volume, Volume &volumeItem)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def customItemList(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QCustom3DItem>
    QQuickGraphsItem::customItemList()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.customItemList' has no cute function yet. Qt's "
        "'QQmlListProperty<QCustom3DItem> "
        "QQuickGraphsItem::customItemList()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def getMultiAxis(*__, **_) -> Never:
    """
    Qt's 'MultiAxis QQuickGraphsItem::getMultiAxis(qsizetype axisIndex,
    QAbstract3DAxis *axis)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.getMultiAxis' has no cute function yet. Qt's "
        "'MultiAxis QQuickGraphsItem::getMultiAxis(qsizetype axisIndex, "
        "QAbstract3DAxis *axis)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def gridLineCountHelper(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsItem::gridLineCountHelper(QAbstract3DAxis *axis,
    qsizetype &lineCount, qsizetype &sublineCount)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.gridLineCountHelper' has no cute function yet. "
        "Qt's 'void QQuickGraphsItem::gridLineCountHelper(QAbstract3DAxis "
        "*axis, qsizetype &lineCount, qsizetype &sublineCount)': takes a "
        "number to change where it is.")

  @staticmethod
  def setAxisHelper(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsItem::setAxisHelper(QAbstract3DAxis::AxisOrientation
    orientation, QAbstract3DAxis *axis, QAbstract3DAxis **axisPtr)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.setAxisHelper' has no cute function yet. Qt's "
        "'void "
        "QQuickGraphsItem::setAxisHelper(QAbstract3DAxis::AxisOrientation "
        "orientation, QAbstract3DAxis *axis, QAbstract3DAxis **axisPtr)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setGridLineType(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsItem::setGridLineType(const
    QtGraphs3D::GridLineType &gridLineType)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.setGridLineType' has no cute function yet. Qt's "
        "'void QQuickGraphsItem::setGridLineType(const "
        "QtGraphs3D::GridLineType &gridLineType)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def updateSliceFrameMaterials(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsItem::updateSliceFrameMaterials(QCustom3DVolume
    *volume, Volume &volumeItem)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsItem.updateSliceFrameMaterials' has no cute function "
        "yet. Qt's 'void "
        "QQuickGraphsItem::updateSliceFrameMaterials(QCustom3DVolume "
        "*volume, Volume &volumeItem)': takes a type Python has no way to "
        "hand over yet.")
