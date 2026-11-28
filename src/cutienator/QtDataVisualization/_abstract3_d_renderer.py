"""
Abstract3DRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/abstract3drenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Abstract3DRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject, QStringList
from ..QtGui import QOpenGLFunctions
from . import QAbstract3DAxis, QAbstract3DGraph

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QVector3D, QVector4D
  from . import CustomRenderItem, Q3DScene, Q3DTheme, QAbstract3DSeries
  from . import QCustom3DItem, QValue3DAxisFormatter, SeriesRenderCache
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  CustomRenderItem = WAIT['CustomRenderItem']
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  Q3DTheme = WAIT['Q3DTheme']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QCustom3DItem = WAIT['QtDataVisualization:QCustom3DItem']
  QValue3DAxisFormatter = WAIT['QtDataVisualization:QValue3DAxisFormatter']
  QVector3D = WAIT['QVector3D']
  SeriesRenderCache = WAIT['SeriesRenderCache']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Abstract3DRenderer(QObject, QOpenGLFunctions):
  """
  The cute side of Qt's Abstract3DRenderer: a plain Python object standing in
  front of one C++ Abstract3DRenderer.

  It is built on the cute 'QObject', as Qt's Abstract3DRenderer is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QOpenGLFunctions' as well, as Qt's Abstract3DRenderer is built on Qt's
  QOpenGLFunctions too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Abstract3DRenderer that has a ritual and that Python
  can call so far, 69 names in all: 'metaObject', 'updateData',
  'updateSeries', 'updateCustomData', 'updateCustomItems',
  'updateCustomItemPositions', 'createNewCache', 'cleanCache', 'render',
  'updateTheme', 'updateSelectionMode', 'updateOptimizationHint',
  'updateScene', 'updateTextures', 'initSelectionBuffer',
  'updateDepthBuffer', 'updateShadowQuality', 'initShaders',
  'initGradientShaders', 'initStaticSelectedItemShaders',
  'initBackgroundShaders', 'initCustomItemShaders',
  'initVolumeTextureShaders', 'initLabelShaders',
  'initCursorPositionShaders', 'initCursorPositionBuffer', 'updateAxisType',
  'updateAxisTitle', 'updateAxisLabels', 'updateAxisRange',
  'updateAxisSegmentCount', 'updateAxisSubSegmentCount',
  'updateAxisLabelFormat', 'updateAxisReversed', 'updateAxisFormatter',
  'updateAxisLabelAutoRotation', 'updateAxisTitleVisibility',
  'updateAxisTitleFixed', 'modifiedSeriesList', 'addCustomItem',
  'updateCustomItem', 'updateAspectRatio', 'updateHorizontalAspectRatio',
  'updatePolar', 'updateRadialLabelOffset', 'updateMargin',
  'convertPositionToTranslation', 'isClickQueryResolved',
  'clearClickQueryResolved', 'cachedClickQuery', 'clickedSeries',
  'clickedType', 'isGraphPositionQueryResolved',
  'clearGraphPositionQueryResolved', 'queriedGraphPosition',
  'cachedGraphPositionQuery', 'setSelectionLabel', 'indexToSelectionColor',
  'needRender', 'requestShadowQuality', 'contextCleanup', 'initializeOpenGL',
  'reInitShaders', 'handleShadowQualityChange', 'handleResize',
  'lowerShadowQuality', 'calculateZoomLevel',
  'calculatePolarBackgroundMargin', 'recalculateCustomItemScalingAndPos'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Abstract3DRenderer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Abstract3DRenderer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Abstract3DRenderer::~Abstract3DRenderer()': the destructor: Python
    never removes a C++ Abstract3DRenderer.
  - Qt's 'void Abstract3DRenderer::updateSelectionState(SelectionState
    state)': names the enum 'Abstract3DRenderer::SelectionState', whose class
    cannot be named here.
  - Qt's 'void Abstract3DRenderer::fixMeshFileName(QString &fileName,
    QAbstract3DSeries::Mesh mesh)': takes a type Python has no way to hand
    over yet.
  - Qt's 'LabelItem &Abstract3DRenderer::selectionLabelItem()': gives a type
    Python has no way to take yet.
  - Qt's 'QString &Abstract3DRenderer::selectionLabel()': gives a type Python
    has no way to take yet.
  - Qt's 'AxisRenderCache
    &Abstract3DRenderer::axisCacheForOrientation(QAbstract3DAxis::
    AxisOrientation orientation)': gives a type Python has no way to take
    yet.
  - Qt's 'void Abstract3DRenderer::fixCameraTarget(QVector3D &target)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void Abstract3DRenderer::getVisibleItemBounds(QVector3D &minBounds,
    QVector3D &maxBounds)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  20 of the 99 functions Qt declares: 7 leans on 'ShaderHelper; 3 leans on
  'ObjectHelper; 2 not a gap; 2 Qt's library has no name for it, and its code
  in Qt's source does not compile apart from its file; 2 leans on 'Utils; 1
  the class is abstract, so C++ cannot make one, and the C++ class of ours
  does not fill in every function it leaves open; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied; 1 leans on
  'Abstract3DRenderer; 1 leans on 'Q3DCameraPrivate.

  What to expect
  --------------

  - The C++ Abstract3DRenderer is created at the first use, not by
    'Abstract3DRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Abstract3DRenderer.
  - Qt tells when it has removed the C++ Abstract3DRenderer. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Abstract3DRenderer that has no cute function yet,
    '__init__', 'axisCacheForOrientation', 'calculatePolarXZ',
    'drawAngularGrid', 'drawAxisTitleX', 'drawAxisTitleY', 'drawAxisTitleZ',
    'drawCustomItems', 'drawRadialGrid', 'drawVolumeSliceFrame',
    'fixCameraTarget', 'fixGradient', 'fixGradientAndGenerateTexture',
    'fixMeshFileName', 'generateBaseColorTexture', 'getVisibleItemBounds',
    'loadGridLineMesh', 'loadLabelMesh', 'loadPositionMapperMesh',
    'selectionLabel', 'selectionLabelItem', 'updateCameraViewport',
    'updateSelectionState', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Abstract3DRenderer'

  #  Qt's Abstract3DRenderer is built on more than one class. The part of a
  #  C++ Abstract3DRenderer that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QOpenGLFunctions': 'ritual_cast_Abstract3DRenderer_QOpenGLFunctions',
  }

  #  A C++ Abstract3DRenderer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Abstract3DRenderer'

  #  The functions Qt calls itself that Abstract3DRenderer is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'updateSeries': (
          'void Abstract3DRenderer::updateSeries(const '
          'QList<QAbstract3DSeries *> &)',
      ),
      'updateCustomData': (
          'void Abstract3DRenderer::updateCustomData(const '
          'QList<QCustom3DItem *> &)',
      ),
      'updateSelectionState': (
          'void Abstract3DRenderer::updateSelectionState(SelectionState)',
      ),
      'updateAxisLabels': (
          'void '
          'Abstract3DRenderer::updateAxisLabels(QAbstract3DAxis::AxisOrient'
          'ation, const QStringList &)',
      ),
      'modifiedSeriesList': (
          'void Abstract3DRenderer::modifiedSeriesList(const '
          'QList<QAbstract3DSeries *> &)',
      ),
      'fixMeshFileName': (
          'void Abstract3DRenderer::fixMeshFileName(QString &, '
          'QAbstract3DSeries::Mesh)',
      ),
      'fixCameraTarget': (
          'void Abstract3DRenderer::fixCameraTarget(QVector3D &)',
      ),
      'getVisibleItemBounds': (
          'void Abstract3DRenderer::getVisibleItemBounds(QVector3D &, '
          'QVector3D &)',
      ),
  }

  #  The functions Qt calls itself that Abstract3DRenderer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateData': (
          ('_ZN18Abstract3DRenderer10updateDataEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateCustomItems': (
          ('_ZN18Abstract3DRenderer17updateCustomItemsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateCustomItemPositions': (
          ('_ZN18Abstract3DRenderer25updateCustomItemPositionsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'createNewCache': (
          ('_ZN18Abstract3DRenderer14createNewCacheEP17QAbstract3DSeries',
           ('address', 'address', 'QtDataVisualization:SeriesRenderCache'),
           (
               ('address', 'address',
                'QtDataVisualization:QAbstract3DSeries'),
           )),
      ),
      'cleanCache': (
          ('_ZN18Abstract3DRenderer10cleanCacheEP17SeriesRenderCache',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDataVisualization:SeriesRenderCache'),
           )),
      ),
      'render': (
          ('_ZN18Abstract3DRenderer6renderEj',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'updateTheme': (
          ('_ZN18Abstract3DRenderer11updateThemeEP8Q3DTheme',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:Q3DTheme'),
           )),
      ),
      'updateSelectionMode': (
          ('_ZN18Abstract3DRenderer19updateSelectionModeE6QFlagsIN16QAbstra'
           'ct3DGraph13SelectionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'QtDataVisualization:QAbstract3DGraph.SelectionFlag'),
           )),
      ),
      'updateOptimizationHint': (
          ('_ZN18Abstract3DRenderer22updateOptimizationHintE6QFlagsIN16QAbs'
           'tract3DGraph16OptimizationHintEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'QtDataVisualization:QAbstract3DGraph.OptimizationHint'),
           )),
      ),
      'updateScene': (
          ('_ZN18Abstract3DRenderer11updateSceneEP8Q3DScene',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:Q3DScene'),
           )),
      ),
      'updateTextures': (
          ('_ZN18Abstract3DRenderer14updateTexturesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initSelectionBuffer': (
          ('_ZN18Abstract3DRenderer19initSelectionBufferEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateDepthBuffer': (
          ('_ZN18Abstract3DRenderer17updateDepthBufferEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateShadowQuality': (
          ('_ZN18Abstract3DRenderer19updateShadowQualityEN16QAbstract3DGrap'
           'h13ShadowQualityE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DGraph.ShadowQuality'),
           )),
      ),
      'initShaders': (
          ('_ZN18Abstract3DRenderer11initShadersERK7QStringS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'initGradientShaders': (
          ('_ZN18Abstract3DRenderer19initGradientShadersERK7QStringS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'initStaticSelectedItemShaders': (
          ('_ZN18Abstract3DRenderer29initStaticSelectedItemShadersERK7QStri'
           'ngS2_S2_S2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'initBackgroundShaders': (
          ('_ZN18Abstract3DRenderer21initBackgroundShadersERK7QStringS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'initCustomItemShaders': (
          ('_ZN18Abstract3DRenderer21initCustomItemShadersERK7QStringS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'initVolumeTextureShaders': (
          ('_ZN18Abstract3DRenderer24initVolumeTextureShadersERK7QStringS2_'
           'S2_S2_S2_S2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'initLabelShaders': (
          ('_ZN18Abstract3DRenderer16initLabelShadersERK7QStringS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'initCursorPositionShaders': (
          ('_ZN18Abstract3DRenderer25initCursorPositionShadersERK7QStringS2'
           '_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'initCursorPositionBuffer': (
          ('_ZN18Abstract3DRenderer24initCursorPositionBufferEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateAxisType': (
          ('_ZN18Abstract3DRenderer14updateAxisTypeEN15QAbstract3DAxis15Axi'
           'sOrientationENS0_8AxisTypeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisType'),
           )),
      ),
      'updateAxisTitle': (
          ('_ZN18Abstract3DRenderer15updateAxisTitleEN15QAbstract3DAxis15Ax'
           'isOrientationERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('address', 'text', ''),
           )),
      ),
      'updateAxisRange': (
          ('_ZN18Abstract3DRenderer15updateAxisRangeEN15QAbstract3DAxis15Ax'
           'isOrientationEff',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('float', 'number', ''),
               ('float', 'number', ''),
           )),
      ),
      'updateAxisSegmentCount': (
          ('_ZN18Abstract3DRenderer22updateAxisSegmentCountEN15QAbstract3DA'
           'xis15AxisOrientationEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('int', 'number', ''),
           )),
      ),
      'updateAxisSubSegmentCount': (
          ('_ZN18Abstract3DRenderer25updateAxisSubSegmentCountEN15QAbstract'
           '3DAxis15AxisOrientationEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('int', 'number', ''),
           )),
      ),
      'updateAxisLabelFormat': (
          ('_ZN18Abstract3DRenderer21updateAxisLabelFormatEN15QAbstract3DAx'
           'is15AxisOrientationERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('address', 'text', ''),
           )),
      ),
      'updateAxisReversed': (
          ('_ZN18Abstract3DRenderer18updateAxisReversedEN15QAbstract3DAxis1'
           '5AxisOrientationEb',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('bool', 'number', ''),
           )),
      ),
      'updateAxisFormatter': (
          ('_ZN18Abstract3DRenderer19updateAxisFormatterEN15QAbstract3DAxis'
           '15AxisOrientationEP21QValue3DAxisFormatter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('address', 'address',
                'QtDataVisualization:QValue3DAxisFormatter'),
           )),
      ),
      'updateAxisLabelAutoRotation': (
          ('_ZN18Abstract3DRenderer27updateAxisLabelAutoRotationEN15QAbstra'
           'ct3DAxis15AxisOrientationEf',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('float', 'number', ''),
           )),
      ),
      'updateAxisTitleVisibility': (
          ('_ZN18Abstract3DRenderer25updateAxisTitleVisibilityEN15QAbstract'
           '3DAxis15AxisOrientationEb',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('bool', 'number', ''),
           )),
      ),
      'updateAxisTitleFixed': (
          ('_ZN18Abstract3DRenderer20updateAxisTitleFixedEN15QAbstract3DAxi'
           's15AxisOrientationEb',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('bool', 'number', ''),
           )),
      ),
      'addCustomItem': (
          ('_ZN18Abstract3DRenderer13addCustomItemEP13QCustom3DItem',
           ('address', 'address', 'QtDataVisualization:CustomRenderItem'),
           (
               ('address', 'address', 'QtDataVisualization:QCustom3DItem'),
           )),
      ),
      'updateCustomItem': (
          ('_ZN18Abstract3DRenderer16updateCustomItemEP16CustomRenderItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDataVisualization:CustomRenderItem'),
           )),
      ),
      'updateAspectRatio': (
          ('_ZN18Abstract3DRenderer17updateAspectRatioEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'updateHorizontalAspectRatio': (
          ('_ZN18Abstract3DRenderer27updateHorizontalAspectRatioEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'updatePolar': (
          ('_ZN18Abstract3DRenderer11updatePolarEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'updateRadialLabelOffset': (
          ('_ZN18Abstract3DRenderer23updateRadialLabelOffsetEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'updateMargin': (
          ('_ZN18Abstract3DRenderer12updateMarginEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'convertPositionToTranslation': (
          ('_ZN18Abstract3DRenderer28convertPositionToTranslationERK9QVecto'
           'r3Db',
           ('address', 'value', 'QtGui:QVector3D'),
           (
               ('address', 'value', 'QtGui:QVector3D'),
               ('bool', 'number', ''),
           )),
      ),
      'contextCleanup': (
          ('_ZN18Abstract3DRenderer14contextCleanupEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initializeOpenGL': (
          ('_ZN18Abstract3DRenderer16initializeOpenGLEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleShadowQualityChange': (
          ('_ZN18Abstract3DRenderer25handleShadowQualityChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleResize': (
          ('_ZN18Abstract3DRenderer12handleResizeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'lowerShadowQuality': (
          ('_ZN18Abstract3DRenderer18lowerShadowQualityEv',
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
    Calls Qt's 'const QMetaObject *Abstract3DRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3drenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Abstract3DRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18Abstract3DRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isClickQueryResolved(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DRenderer::isClickQueryResolved() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#isClickQueryResolved
    """
    #  bool Abstract3DRenderer::isClickQueryResolved() const
    return self.uglySide.call(
        'ritual_ZNK18Abstract3DRenderer20isClickQueryResolvedEv',
    )

  def cachedClickQuery(self) -> QPoint:
    """
    Calls Qt's 'QPoint Abstract3DRenderer::cachedClickQuery() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#cachedClickQuery

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Abstract3DRenderer::cachedClickQuery() const
    address = self.uglySide.call(
        'ritual_ZNK18Abstract3DRenderer16cachedClickQueryEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def clickedSeries(self) -> Optional[QAbstract3DSeries]:
    """
    Calls Qt's 'QAbstract3DSeries *Abstract3DRenderer::clickedSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#clickedSeries

    Returns
    -------

    Optional[QAbstract3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DSeries *Abstract3DRenderer::clickedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK18Abstract3DRenderer13clickedSeriesEv',
    )
    from . import QAbstract3DSeries
    return QAbstract3DSeries._cuteAt(address)

  def isGraphPositionQueryResolved(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DRenderer::isGraphPositionQueryResolved()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html
    """
    #  bool Abstract3DRenderer::isGraphPositionQueryResolved() const
    return self.uglySide.call(
        'ritual_ZNK18Abstract3DRenderer28isGraphPositionQueryResolvedEv',
    )

  def queriedGraphPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Abstract3DRenderer::queriedGraphPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#queriedGraphPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Abstract3DRenderer::queriedGraphPosition() const
    address = self.uglySide.call(
        'ritual_ZNK18Abstract3DRenderer20queriedGraphPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def cachedGraphPositionQuery(self) -> QPoint:
    """
    Calls Qt's 'QPoint Abstract3DRenderer::cachedGraphPositionQuery() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#cachedGraphPositionQuery

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Abstract3DRenderer::cachedGraphPositionQuery() const
    address = self.uglySide.call(
        'ritual_ZNK18Abstract3DRenderer24cachedGraphPositionQueryEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSelectionLabel(self, label: str) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::setSelectionLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#setSelectionLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::setSelectionLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer17setSelectionLabelERK7QString', label,
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
    Qt's 'Abstract3DRenderer::Abstract3DRenderer(Abstract3DController
    *controller)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.__init__' has no cute function yet. Qt's "
        "'Abstract3DRenderer::Abstract3DRenderer(Abstract3DController "
        "*controller)': the class is abstract, so C++ cannot make one, and "
        "the C++ class of ours does not fill in every function it leaves "
        "open.")

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

  def updateData(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateData()'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3drenderer.html#updateData
    """
    #  void Abstract3DRenderer::updateData()
    self.uglySide.call('ritual_ZN18Abstract3DRenderer10updateDataEv')

  @overload(QList[QAbstract3DSeries])
  def updateSeries(self, seriesList: QList[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateSeries(const
    QList<QAbstract3DSeries *> &seriesList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateSeries

    Parameters
    ----------

    seriesList : QList[QAbstract3DSeries]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Abstract3DRenderer::updateSeries(const QList<QAbstract3DSeries *>
    #      &seriesList)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer12updateSeriesERK5QListIP17QAbstract3'
        'DSeriesE',
        self._valueOf(seriesList),
    )

  @overload(QList[QCustom3DItem])
  def updateCustomData(self, customItems: QList[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateCustomData(const
    QList<QCustom3DItem *> &customItems)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateCustomData

    Parameters
    ----------

    customItems : QList[QCustom3DItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Abstract3DRenderer::updateCustomData(const QList<QCustom3DItem *>
    #      &customItems)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer16updateCustomDataERK5QListIP13QCusto'
        'm3DItemE',
        self._valueOf(customItems),
    )

  def updateCustomItems(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateCustomItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateCustomItems
    """
    #  void Abstract3DRenderer::updateCustomItems()
    ritual = 'ritual_ZN18Abstract3DRenderer17updateCustomItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18Abstract3DRenderer17updateCustomItemsEv'
    self.uglySide.call(ritual)

  def updateCustomItemPositions(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateCustomItemPositions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateCustomItemPositions
    """
    #  void Abstract3DRenderer::updateCustomItemPositions()
    ritual = 'ritual_ZN18Abstract3DRenderer25updateCustomItemPositionsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer25updateCustomItemPositionsEv')
    self.uglySide.call(ritual)

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def createNewCache(
      self,
      series: Optional[QAbstract3DSeries],
  ) -> Optional[SeriesRenderCache]:
    """
    Calls Qt's 'SeriesRenderCache
    *Abstract3DRenderer::createNewCache(QAbstract3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#createNewCache

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[SeriesRenderCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SeriesRenderCache
    #      *Abstract3DRenderer::createNewCache(QAbstract3DSeries *series)
    address = self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer14createNewCacheEP17QAbstract3DSeries',
        self._addressOf(series),
    )
    from . import SeriesRenderCache
    return SeriesRenderCache._cuteAt(address)

  @overload(SeriesRenderCache)
  @overload(NoneType)
  def cleanCache(self, cache: Optional[SeriesRenderCache]) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::cleanCache(SeriesRenderCache
    *cache)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3drenderer.html#cleanCache

    Parameters
    ----------

    cache : Optional[SeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DRenderer::cleanCache(SeriesRenderCache *cache)
    ritual = 'ritual_ZN18Abstract3DRenderer10cleanCacheEP17SeriesRenderCache'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer10cleanCacheEP17SeriesRenderCac'
          'he')
    self.uglySide.call(ritual, self._addressOf(cache))

  @overload(int)
  def render(self, defaultFboHandle: int) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::render(GLuint defaultFboHandle)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3drenderer.html#render

    Parameters
    ----------

    defaultFboHandle : int
      Passed on as it is.
    """
    #  void Abstract3DRenderer::render(GLuint defaultFboHandle)
    ritual = 'ritual_ZN18Abstract3DRenderer6renderEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18Abstract3DRenderer6renderEj'
    self.uglySide.call(ritual, defaultFboHandle)

  @overload(Q3DTheme)
  @overload(NoneType)
  def updateTheme(self, theme: Optional[Q3DTheme]) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateTheme(Q3DTheme *theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateTheme

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DRenderer::updateTheme(Q3DTheme *theme)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer11updateThemeEP8Q3DTheme',
        self._addressOf(theme),
    )

  @overload(QAbstract3DGraph.SelectionFlags)
  def updateSelectionMode(
      self,
      newMode: QAbstract3DGraph.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateSelectionMode(QAbstract3DGraph::SelectionFlags
    newMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateSelectionMode

    Parameters
    ----------

    newMode : QAbstract3DGraph.SelectionFlags
      Passed on as its number.
    """
    #  void Abstract3DRenderer::updateSelectionMode(QAbstract3DGraph::
    #      SelectionFlags newMode)
    ritual = (
        'ritual_ZN18Abstract3DRenderer19updateSelectionModeE6QFlagsIN16QAbs'
        'tract3DGraph13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer19updateSelectionModeE6QFlagsIN'
          '16QAbstract3DGraph13SelectionFlagEE')
    self.uglySide.call(ritual, newMode.value)

  @overload(QAbstract3DGraph.OptimizationHints)
  def updateOptimizationHint(
      self,
      hint: QAbstract3DGraph.OptimizationHints,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateOptimizationHint(QAbstract3DGraph::
    OptimizationHints hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateOptimizationHint

    Parameters
    ----------

    hint : QAbstract3DGraph.OptimizationHints
      Passed on as its number.
    """
    #  void Abstract3DRenderer::updateOptimizationHint(QAbstract3DGraph::
    #      OptimizationHints hint)
    ritual = (
        'ritual_ZN18Abstract3DRenderer22updateOptimizationHintE6QFlagsIN16Q'
        'Abstract3DGraph16OptimizationHintEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer22updateOptimizationHintE6QFlag'
          'sIN16QAbstract3DGraph16OptimizationHintEE')
    self.uglySide.call(ritual, hint.value)

  @overload(Q3DScene)
  @overload(NoneType)
  def updateScene(self, scene: Optional[Q3DScene]) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateScene(Q3DScene *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateScene

    Parameters
    ----------

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DRenderer::updateScene(Q3DScene *scene)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer11updateSceneEP8Q3DScene',
        self._addressOf(scene),
    )

  def updateTextures(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateTextures()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateTextures
    """
    #  void Abstract3DRenderer::updateTextures()
    self.uglySide.call('ritual_ZN18Abstract3DRenderer14updateTexturesEv')

  def initSelectionBuffer(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initSelectionBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initSelectionBuffer
    """
    #  void Abstract3DRenderer::initSelectionBuffer()
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer19initSelectionBufferEv',
    )

  def updateDepthBuffer(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateDepthBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateDepthBuffer
    """
    #  void Abstract3DRenderer::updateDepthBuffer()
    self.uglySide.call('ritual_ZN18Abstract3DRenderer17updateDepthBufferEv')

  @overload(QAbstract3DGraph.ShadowQuality)
  def updateShadowQuality(
      self,
      quality: QAbstract3DGraph.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateShadowQuality

    Parameters
    ----------

    quality : QAbstract3DGraph.ShadowQuality
      Passed on as its number.
    """
    #  void Abstract3DRenderer::updateShadowQuality(QAbstract3DGraph::
    #      ShadowQuality quality)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer19updateShadowQualityEN16QAbstract3DG'
        'raph13ShadowQualityE',
        quality.value,
    )

  @overload(str, str)
  def initShaders(self, vertexShader: str, fragmentShader: str) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::initShaders(const QString &vertexShader,
    #      const QString &fragmentShader)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer11initShadersERK7QStringS2_',
        vertexShader, fragmentShader,
    )

  @overload(str, str)
  def initGradientShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initGradientShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initGradientShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::initGradientShaders(const QString
    #      &vertexShader, const QString &fragmentShader)
    ritual = (
        'ritual_ZN18Abstract3DRenderer19initGradientShadersERK7QStringS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer19initGradientShadersERK7QStrin'
          'gS2_')
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  @overload(str, str, str, str)
  def initStaticSelectedItemShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
      gradientVertexShader: str,
      gradientFragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initStaticSelectedItemShaders(const
    QString &vertexShader, const QString &fragmentShader, const QString
    &gradientVertexShader, const QString &gradientFragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.

    gradientVertexShader : str
      Passed on as it is: a QString is made of it for the call.

    gradientFragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::initStaticSelectedItemShaders(const QString
    #      &vertexShader, const QString &fragmentShader, const QString
    #      &gradientVertexShader, const QString &gradientFragmentShader)
    ritual = (
        'ritual_ZN18Abstract3DRenderer29initStaticSelectedItemShadersERK7QS'
        'tringS2_S2_S2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer29initStaticSelectedItemShaders'
          'ERK7QStringS2_S2_S2_')
    self.uglySide.call(
        ritual,
        vertexShader, fragmentShader, gradientVertexShader,
        gradientFragmentShader,
    )

  @overload(str, str)
  def initBackgroundShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initBackgroundShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initBackgroundShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::initBackgroundShaders(const QString
    #      &vertexShader, const QString &fragmentShader)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer21initBackgroundShadersERK7QStringS2_',
        vertexShader, fragmentShader,
    )

  @overload(str, str)
  def initCustomItemShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initCustomItemShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initCustomItemShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::initCustomItemShaders(const QString
    #      &vertexShader, const QString &fragmentShader)
    ritual = (
        'ritual_ZN18Abstract3DRenderer21initCustomItemShadersERK7QStringS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer21initCustomItemShadersERK7QStr'
          'ingS2_')
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  @overload(str, str, str, str, str, str)
  def initVolumeTextureShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
      fragmentLowDefShader: str,
      sliceShader: str,
      sliceFrameVertexShader: str,
      sliceFrameShader: str,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initVolumeTextureShaders(const
    QString &vertexShader, const QString &fragmentShader, const QString
    &fragmentLowDefShader, const QString &sliceShader, const QString
    &sliceFrameVertexShader, const QString &sliceFrameShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initVolumeTextureShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentLowDefShader : str
      Passed on as it is: a QString is made of it for the call.

    sliceShader : str
      Passed on as it is: a QString is made of it for the call.

    sliceFrameVertexShader : str
      Passed on as it is: a QString is made of it for the call.

    sliceFrameShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::initVolumeTextureShaders(const QString
    #      &vertexShader, const QString &fragmentShader, const QString
    #      &fragmentLowDefShader, const QString &sliceShader, const QString
    #      &sliceFrameVertexShader, const QString &sliceFrameShader)
    ritual = (
        'ritual_ZN18Abstract3DRenderer24initVolumeTextureShadersERK7QString'
        'S2_S2_S2_S2_S2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer24initVolumeTextureShadersERK7Q'
          'StringS2_S2_S2_S2_S2_')
    self.uglySide.call(
        ritual,
        vertexShader, fragmentShader, fragmentLowDefShader, sliceShader,
        sliceFrameVertexShader, sliceFrameShader,
    )

  @overload(str, str)
  def initLabelShaders(self, vertexShader: str, fragmentShader: str) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initLabelShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initLabelShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::initLabelShaders(const QString &vertexShader,
    #      const QString &fragmentShader)
    ritual = 'ritual_ZN18Abstract3DRenderer16initLabelShadersERK7QStringS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer16initLabelShadersERK7QStringS2'
          '_')
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  @overload(str, str)
  def initCursorPositionShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initCursorPositionShaders(const
    QString &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initCursorPositionShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::initCursorPositionShaders(const QString
    #      &vertexShader, const QString &fragmentShader)
    ritual = (
        'ritual_ZN18Abstract3DRenderer25initCursorPositionShadersERK7QStrin'
        'gS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer25initCursorPositionShadersERK7'
          'QStringS2_')
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  def initCursorPositionBuffer(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initCursorPositionBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initCursorPositionBuffer
    """
    #  void Abstract3DRenderer::initCursorPositionBuffer()
    ritual = 'ritual_ZN18Abstract3DRenderer24initCursorPositionBufferEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer24initCursorPositionBufferEv')
    self.uglySide.call(ritual)

  @overload(QAbstract3DAxis.AxisOrientation, QAbstract3DAxis.AxisType)
  def updateAxisType(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      type: QAbstract3DAxis.AxisType,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisType(QAbstract3DAxis::AxisOrientation
    orientation, QAbstract3DAxis::AxisType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisType

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    type : QAbstract3DAxis.AxisType
      Passed on as its number.
    """
    #  void Abstract3DRenderer::updateAxisType(QAbstract3DAxis::
    #      AxisOrientation orientation, QAbstract3DAxis::AxisType type)
    ritual = (
        'ritual_ZN18Abstract3DRenderer14updateAxisTypeEN15QAbstract3DAxis15'
        'AxisOrientationENS0_8AxisTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer14updateAxisTypeEN15QAbstract3D'
          'Axis15AxisOrientationENS0_8AxisTypeE')
    self.uglySide.call(ritual, orientation.value, type.value)

  @overload(QAbstract3DAxis.AxisOrientation, str)
  def updateAxisTitle(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      title: str,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisTitle(QAbstract3DAxis::AxisOrientation
    orientation, const QString &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisTitle

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::updateAxisTitle(QAbstract3DAxis::
    #      AxisOrientation orientation, const QString &title)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer15updateAxisTitleEN15QAbstract3DAxis1'
        '5AxisOrientationERK7QString',
        orientation.value, title,
    )

  @overload(QAbstract3DAxis.AxisOrientation, QStringList)
  def updateAxisLabels(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      labels: QStringList,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisLabels(QAbstract3DAxis::AxisOrientation
    orientation, const QStringList &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisLabels

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Abstract3DRenderer::updateAxisLabels(QAbstract3DAxis::
    #      AxisOrientation orientation, const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer16updateAxisLabelsEN15QAbstract3DAxis'
        '15AxisOrientationERK5QListI7QStringE',
        orientation.value, self._valueOf(labels),
    )

  @overload(QAbstract3DAxis.AxisOrientation, float, float)
  def updateAxisRange(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      min: float,
      max: float,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisRange(QAbstract3DAxis::AxisOrientation
    orientation, float min, float max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisRange

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateAxisRange(QAbstract3DAxis::
    #      AxisOrientation orientation, float min, float max)
    ritual = (
        'ritual_ZN18Abstract3DRenderer15updateAxisRangeEN15QAbstract3DAxis1'
        '5AxisOrientationEff')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer15updateAxisRangeEN15QAbstract3'
          'DAxis15AxisOrientationEff')
    self.uglySide.call(ritual, orientation.value, min, max)

  @overload(QAbstract3DAxis.AxisOrientation, int)
  def updateAxisSegmentCount(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisSegmentCount(QAbstract3DAxis::
    AxisOrientation orientation, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisSegmentCount

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    count : int
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateAxisSegmentCount(QAbstract3DAxis::
    #      AxisOrientation orientation, int count)
    ritual = (
        'ritual_ZN18Abstract3DRenderer22updateAxisSegmentCountEN15QAbstract'
        '3DAxis15AxisOrientationEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer22updateAxisSegmentCountEN15QAb'
          'stract3DAxis15AxisOrientationEi')
    self.uglySide.call(ritual, orientation.value, count)

  @overload(QAbstract3DAxis.AxisOrientation, int)
  def updateAxisSubSegmentCount(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisSubSegmentCount(QAbstract3DAxis::
    AxisOrientation orientation, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisSubSegmentCount

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    count : int
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateAxisSubSegmentCount(QAbstract3DAxis::
    #      AxisOrientation orientation, int count)
    ritual = (
        'ritual_ZN18Abstract3DRenderer25updateAxisSubSegmentCountEN15QAbstr'
        'act3DAxis15AxisOrientationEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer25updateAxisSubSegmentCountEN15'
          'QAbstract3DAxis15AxisOrientationEi')
    self.uglySide.call(ritual, orientation.value, count)

  @overload(QAbstract3DAxis.AxisOrientation, str)
  def updateAxisLabelFormat(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      format: str,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisLabelFormat(QAbstract3DAxis::
    AxisOrientation orientation, const QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisLabelFormat

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DRenderer::updateAxisLabelFormat(QAbstract3DAxis::
    #      AxisOrientation orientation, const QString &format)
    ritual = (
        'ritual_ZN18Abstract3DRenderer21updateAxisLabelFormatEN15QAbstract3'
        'DAxis15AxisOrientationERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer21updateAxisLabelFormatEN15QAbs'
          'tract3DAxis15AxisOrientationERK7QString')
    self.uglySide.call(ritual, orientation.value, format)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def updateAxisReversed(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      enable: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisReversed(QAbstract3DAxis::AxisOrientation
    orientation, bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisReversed

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    enable : bool
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateAxisReversed(QAbstract3DAxis::
    #      AxisOrientation orientation, bool enable)
    ritual = (
        'ritual_ZN18Abstract3DRenderer18updateAxisReversedEN15QAbstract3DAx'
        'is15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer18updateAxisReversedEN15QAbstra'
          'ct3DAxis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, enable)

  @overload(QAbstract3DAxis.AxisOrientation, QValue3DAxisFormatter)
  @overload(QAbstract3DAxis.AxisOrientation, NoneType)
  def updateAxisFormatter(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      formatter: Optional[QValue3DAxisFormatter],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisFormatter(QAbstract3DAxis::AxisOrientation
    orientation, QValue3DAxisFormatter *formatter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisFormatter

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    formatter : Optional[QValue3DAxisFormatter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DRenderer::updateAxisFormatter(QAbstract3DAxis::
    #      AxisOrientation orientation, QValue3DAxisFormatter *formatter)
    ritual = (
        'ritual_ZN18Abstract3DRenderer19updateAxisFormatterEN15QAbstract3DA'
        'xis15AxisOrientationEP21QValue3DAxisFormatter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer19updateAxisFormatterEN15QAbstr'
          'act3DAxis15AxisOrientationEP21QValue3DAxisFormatter')
    self.uglySide.call(ritual, orientation.value, self._addressOf(formatter))

  @overload(QAbstract3DAxis.AxisOrientation, float)
  def updateAxisLabelAutoRotation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      angle: float,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisLabelAutoRotation(QAbstract3DAxis::
    AxisOrientation orientation, float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    angle : float
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateAxisLabelAutoRotation(QAbstract3DAxis::
    #      AxisOrientation orientation, float angle)
    ritual = (
        'ritual_ZN18Abstract3DRenderer27updateAxisLabelAutoRotationEN15QAbs'
        'tract3DAxis15AxisOrientationEf')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer27updateAxisLabelAutoRotationEN'
          '15QAbstract3DAxis15AxisOrientationEf')
    self.uglySide.call(ritual, orientation.value, angle)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def updateAxisTitleVisibility(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      visible: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::
    AxisOrientation orientation, bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisTitleVisibility

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    visible : bool
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::
    #      AxisOrientation orientation, bool visible)
    ritual = (
        'ritual_ZN18Abstract3DRenderer25updateAxisTitleVisibilityEN15QAbstr'
        'act3DAxis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer25updateAxisTitleVisibilityEN15'
          'QAbstract3DAxis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, visible)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def updateAxisTitleFixed(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      fixed: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::updateAxisTitleFixed(QAbstract3DAxis::AxisOrientation
    orientation, bool fixed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAxisTitleFixed

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    fixed : bool
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateAxisTitleFixed(QAbstract3DAxis::
    #      AxisOrientation orientation, bool fixed)
    ritual = (
        'ritual_ZN18Abstract3DRenderer20updateAxisTitleFixedEN15QAbstract3D'
        'Axis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer20updateAxisTitleFixedEN15QAbst'
          'ract3DAxis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, fixed)

  @overload(QList[QAbstract3DSeries])
  def modifiedSeriesList(self, seriesList: QList[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::modifiedSeriesList(const
    QList<QAbstract3DSeries *> &seriesList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#modifiedSeriesList

    Parameters
    ----------

    seriesList : QList[QAbstract3DSeries]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Abstract3DRenderer::modifiedSeriesList(const
    #      QList<QAbstract3DSeries *> &seriesList)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer18modifiedSeriesListERK5QListIP17QAbs'
        'tract3DSeriesE',
        self._valueOf(seriesList),
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def addCustomItem(
      self,
      item: Optional[QCustom3DItem],
  ) -> Optional[CustomRenderItem]:
    """
    Calls Qt's 'CustomRenderItem
    *Abstract3DRenderer::addCustomItem(QCustom3DItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#addCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[CustomRenderItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  CustomRenderItem *Abstract3DRenderer::addCustomItem(QCustom3DItem
    #      *item)
    address = self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer13addCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )
    from . import CustomRenderItem
    return CustomRenderItem._cuteAt(address)

  @overload(CustomRenderItem)
  @overload(NoneType)
  def updateCustomItem(self, renderItem: Optional[CustomRenderItem]) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateCustomItem(CustomRenderItem
    *renderItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateCustomItem

    Parameters
    ----------

    renderItem : Optional[CustomRenderItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DRenderer::updateCustomItem(CustomRenderItem
    #      *renderItem)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer16updateCustomItemEP16CustomRenderIte'
        'm',
        self._addressOf(renderItem),
    )

  @overload(float)
  def updateAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateAspectRatio(float ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateAspectRatio(float ratio)
    ritual = 'ritual_ZN18Abstract3DRenderer17updateAspectRatioEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18Abstract3DRenderer17updateAspectRatioEf'
    self.uglySide.call(ritual, ratio)

  @overload(float)
  def updateHorizontalAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateHorizontalAspectRatio(float
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateHorizontalAspectRatio(float ratio)
    ritual = 'ritual_ZN18Abstract3DRenderer27updateHorizontalAspectRatioEf'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18Abstract3DRenderer27updateHorizontalAspectRatioEf')
    self.uglySide.call(ritual, ratio)

  @overload(bool)
  def updatePolar(self, enable: bool) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updatePolar(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updatePolar

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updatePolar(bool enable)
    ritual = 'ritual_ZN18Abstract3DRenderer11updatePolarEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18Abstract3DRenderer11updatePolarEb'
    self.uglySide.call(ritual, enable)

  @overload(float)
  def updateRadialLabelOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateRadialLabelOffset(float
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateRadialLabelOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateRadialLabelOffset(float offset)
    ritual = 'ritual_ZN18Abstract3DRenderer23updateRadialLabelOffsetEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18Abstract3DRenderer23updateRadialLabelOffsetEf'
    self.uglySide.call(ritual, offset)

  @overload(float)
  def updateMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::updateMargin(float margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#updateMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Abstract3DRenderer::updateMargin(float margin)
    ritual = 'ritual_ZN18Abstract3DRenderer12updateMarginEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18Abstract3DRenderer12updateMarginEf'
    self.uglySide.call(ritual, margin)

  @overload(QVector3D, bool)
  def convertPositionToTranslation(
      self,
      position: QVector3D,
      isAbsolute: bool,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Abstract3DRenderer::convertPositionToTranslation(const QVector3D
    &position, bool isAbsolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    isAbsolute : bool
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Abstract3DRenderer::convertPositionToTranslation(const
    #      QVector3D &position, bool isAbsolute)
    address = self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer28convertPositionToTranslationERK9QVe'
        'ctor3Db',
        self._valueOf(position), isAbsolute,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def clearClickQueryResolved(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::clearClickQueryResolved()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#clearClickQueryResolved
    """
    #  void Abstract3DRenderer::clearClickQueryResolved()
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer23clearClickQueryResolvedEv',
    )

  def clickedType(self) -> QAbstract3DGraph.ElementType:
    """
    Calls Qt's 'QAbstract3DGraph::ElementType
    Abstract3DRenderer::clickedType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#clickedType

    Returns
    -------

    QAbstract3DGraph.ElementType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstract3DGraph.ElementType(number)' gives.
    """
    #  QAbstract3DGraph::ElementType Abstract3DRenderer::clickedType()
    return QAbstract3DGraph.ElementType(self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer11clickedTypeEv',
    ))

  def clearGraphPositionQueryResolved(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::clearGraphPositionQueryResolved()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html
    """
    #  void Abstract3DRenderer::clearGraphPositionQueryResolved()
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer31clearGraphPositionQueryResolvedEv',
    )

  @overload(int)
  def indexToSelectionColor(self, index: int) -> QVector4D:
    """
    Calls Qt's 'QVector4D Abstract3DRenderer::indexToSelectionColor(GLint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#indexToSelectionColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D Abstract3DRenderer::indexToSelectionColor(GLint index)
    address = self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer21indexToSelectionColorEi', index,
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def needRender(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::needRender()'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3drenderer.html#needRender
    """
    #  void Abstract3DRenderer::needRender()
    self.uglySide.call('ritual_ZN18Abstract3DRenderer10needRenderEv')

  @overload(QAbstract3DGraph.ShadowQuality)
  def requestShadowQuality(
      self,
      quality: QAbstract3DGraph.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::requestShadowQuality(QAbstract3DGraph::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#requestShadowQuality

    Parameters
    ----------

    quality : QAbstract3DGraph.ShadowQuality
      Passed on as its number.
    """
    #  void Abstract3DRenderer::requestShadowQuality(QAbstract3DGraph::
    #      ShadowQuality quality)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer20requestShadowQualityEN16QAbstract3D'
        'Graph13ShadowQualityE',
        quality.value,
    )

  def contextCleanup(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::contextCleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#contextCleanup
    """
    #  void Abstract3DRenderer::contextCleanup()
    ritual = 'ritual_ZN18Abstract3DRenderer14contextCleanupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18Abstract3DRenderer14contextCleanupEv'
    self.uglySide.call(ritual)

  def initializeOpenGL(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::initializeOpenGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#initializeOpenGL
    """
    #  void Abstract3DRenderer::initializeOpenGL()
    self.uglySide.call('ritual_ZN18Abstract3DRenderer16initializeOpenGLEv')

  def reInitShaders(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::reInitShaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#reInitShaders
    """
    #  void Abstract3DRenderer::reInitShaders()
    self.uglySide.call('ritual_ZN18Abstract3DRenderer13reInitShadersEv')

  def handleShadowQualityChange(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::handleShadowQualityChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#handleShadowQualityChange
    """
    #  void Abstract3DRenderer::handleShadowQualityChange()
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer25handleShadowQualityChangeEv',
    )

  def handleResize(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::handleResize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#handleResize
    """
    #  void Abstract3DRenderer::handleResize()
    ritual = 'ritual_ZN18Abstract3DRenderer12handleResizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18Abstract3DRenderer12handleResizeEv'
    self.uglySide.call(ritual)

  def lowerShadowQuality(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::lowerShadowQuality()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#lowerShadowQuality
    """
    #  void Abstract3DRenderer::lowerShadowQuality()
    self.uglySide.call('ritual_ZN18Abstract3DRenderer18lowerShadowQualityEv')

  def calculateZoomLevel(self) -> None:
    """
    Calls Qt's 'void Abstract3DRenderer::calculateZoomLevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html#calculateZoomLevel
    """
    #  void Abstract3DRenderer::calculateZoomLevel()
    self.uglySide.call('ritual_ZN18Abstract3DRenderer18calculateZoomLevelEv')

  def calculatePolarBackgroundMargin(self) -> float:
    """
    Calls Qt's 'float Abstract3DRenderer::calculatePolarBackgroundMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html
    """
    #  float Abstract3DRenderer::calculatePolarBackgroundMargin()
    return self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer30calculatePolarBackgroundMarginEv',
    )

  @overload(CustomRenderItem)
  @overload(NoneType)
  def recalculateCustomItemScalingAndPos(
      self,
      item: Optional[CustomRenderItem],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DRenderer::recalculateCustomItemScalingAndPos(CustomRenderItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3drenderer.html

    Parameters
    ----------

    item : Optional[CustomRenderItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DRenderer::recalculateCustomItemScalingAndPos(
    #      CustomRenderItem *item)
    self.uglySide.call(
        'ritual_ZN18Abstract3DRenderer34recalculateCustomItemScalingAndPosE'
        'P16CustomRenderItem',
        self._addressOf(item),
    )

  @staticmethod
  def axisCacheForOrientation(*__, **_) -> Never:
    """
    Qt's 'AxisRenderCache
    &Abstract3DRenderer::axisCacheForOrientation(QAbstract3DAxis::
    AxisOrientation orientation)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.axisCacheForOrientation' has no cute function "
        "yet. Qt's 'AxisRenderCache "
        "&Abstract3DRenderer::axisCacheForOrientation(QAbstract3DAxis::AxisO"
        "rientation orientation)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def calculatePolarXZ(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::calculatePolarXZ(const QVector3D &dataPos,
    float &x, float &z) const': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'doublePi'.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.calculatePolarXZ' has no cute function yet. "
        "Qt's 'void Abstract3DRenderer::calculatePolarXZ(const QVector3D "
        "&dataPos, float &x, float &z) const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'doublePi'.")

  @staticmethod
  def drawAngularGrid(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::drawAngularGrid(ShaderHelper *shader,
    float yFloorLinePos, const QMatrix4x4 &projectionViewMatrix, const
    QMatrix4x4 &depthMatrix)': leans on 'ShaderHelper::setUniformValue(int,
    QMatrix4x4 const&)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.drawAngularGrid' has no cute function yet. "
        "Qt's 'void Abstract3DRenderer::drawAngularGrid(ShaderHelper "
        "*shader, float yFloorLinePos, const QMatrix4x4 "
        "&projectionViewMatrix, const QMatrix4x4 &depthMatrix)': leans on "
        "'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def drawAxisTitleX(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::drawAxisTitleX(const QVector3D
    &labelRotation, const QVector3D &labelTrans, const QQuaternion
    &totalRotation, AbstractRenderItem &dummyItem, const Q3DCamera
    *activeCamera, float labelsMaxWidth, const QMatrix4x4 &viewMatrix, const
    QMatrix4x4 &projectionMatrix, ShaderHelper *shader, bool radial)': leans
    on 'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.drawAxisTitleX' has no cute function yet. Qt's "
        "'void Abstract3DRenderer::drawAxisTitleX(const QVector3D "
        "&labelRotation, const QVector3D &labelTrans, const QQuaternion "
        "&totalRotation, AbstractRenderItem &dummyItem, const Q3DCamera "
        "*activeCamera, float labelsMaxWidth, const QMatrix4x4 &viewMatrix, "
        "const QMatrix4x4 &projectionMatrix, ShaderHelper *shader, bool "
        "radial)': leans on 'ShaderHelper::setUniformValue(int, QMatrix4x4 "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def drawAxisTitleY(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::drawAxisTitleY(const QVector3D
    &sideLabelRotation, const QVector3D &backLabelRotation, const QVector3D
    &sideLabelTrans, const QVector3D &backLabelTrans, const QQuaternion
    &totalSideRotation, const QQuaternion &totalBackRotation,
    AbstractRenderItem &dummyItem, const Q3DCamera *activeCamera, float
    labelsMaxWidth, const QMatrix4x4 &viewMatrix, const QMatrix4x4
    &projectionMatrix, ShaderHelper *shader)': leans on
    'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.drawAxisTitleY' has no cute function yet. Qt's "
        "'void Abstract3DRenderer::drawAxisTitleY(const QVector3D "
        "&sideLabelRotation, const QVector3D &backLabelRotation, const "
        "QVector3D &sideLabelTrans, const QVector3D &backLabelTrans, const "
        "QQuaternion &totalSideRotation, const QQuaternion "
        "&totalBackRotation, AbstractRenderItem &dummyItem, const Q3DCamera "
        "*activeCamera, float labelsMaxWidth, const QMatrix4x4 &viewMatrix, "
        "const QMatrix4x4 &projectionMatrix, ShaderHelper *shader)': leans "
        "on 'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def drawAxisTitleZ(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::drawAxisTitleZ(const QVector3D
    &labelRotation, const QVector3D &labelTrans, const QQuaternion
    &totalRotation, AbstractRenderItem &dummyItem, const Q3DCamera
    *activeCamera, float labelsMaxWidth, const QMatrix4x4 &viewMatrix, const
    QMatrix4x4 &projectionMatrix, ShaderHelper *shader)': leans on
    'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.drawAxisTitleZ' has no cute function yet. Qt's "
        "'void Abstract3DRenderer::drawAxisTitleZ(const QVector3D "
        "&labelRotation, const QVector3D &labelTrans, const QQuaternion "
        "&totalRotation, AbstractRenderItem &dummyItem, const Q3DCamera "
        "*activeCamera, float labelsMaxWidth, const QMatrix4x4 &viewMatrix, "
        "const QMatrix4x4 &projectionMatrix, ShaderHelper *shader)': leans "
        "on 'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def drawCustomItems(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::drawCustomItems(RenderingState state,
    ShaderHelper *regularShader, const QMatrix4x4 &viewMatrix, const
    QMatrix4x4 &projectionViewMatrix, const QMatrix4x4
    &depthProjectionViewMatrix, GLuint depthTexture, GLfloat shadowQuality,
    GLfloat reflection)': leans on 'ShaderHelper::setUniformValue(int,
    QMatrix4x4 const&)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.drawCustomItems' has no cute function yet. "
        "Qt's 'void Abstract3DRenderer::drawCustomItems(RenderingState "
        "state, ShaderHelper *regularShader, const QMatrix4x4 &viewMatrix, "
        "const QMatrix4x4 &projectionViewMatrix, const QMatrix4x4 "
        "&depthProjectionViewMatrix, GLuint depthTexture, GLfloat "
        "shadowQuality, GLfloat reflection)': leans on "
        "'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def drawRadialGrid(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::drawRadialGrid(ShaderHelper *shader, float
    yFloorLinePos, const QMatrix4x4 &projectionViewMatrix, const QMatrix4x4
    &depthMatrix)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'polarGridRoundness'.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.drawRadialGrid' has no cute function yet. Qt's "
        "'void Abstract3DRenderer::drawRadialGrid(ShaderHelper *shader, "
        "float yFloorLinePos, const QMatrix4x4 &projectionViewMatrix, const "
        "QMatrix4x4 &depthMatrix)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'polarGridRoundness'.")

  @staticmethod
  def drawVolumeSliceFrame(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::drawVolumeSliceFrame(const
    CustomRenderItem *item, Qt::Axis axis, const QMatrix4x4
    &projectionViewMatrix)': leans on 'ShaderHelper::setUniformValue(int,
    QMatrix4x4 const&)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.drawVolumeSliceFrame' has no cute function "
        "yet. Qt's 'void Abstract3DRenderer::drawVolumeSliceFrame(const "
        "CustomRenderItem *item, Qt::Axis axis, const QMatrix4x4 "
        "&projectionViewMatrix)': leans on "
        "'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def fixCameraTarget(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::fixCameraTarget(QVector3D &target)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.fixCameraTarget' has no cute function yet. "
        "Qt's 'void Abstract3DRenderer::fixCameraTarget(QVector3D "
        "&target)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def fixGradient(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::fixGradient(QLinearGradient *gradient,
    GLuint *gradientTexture)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.fixGradient' has no cute function yet. Qt's "
        "'void Abstract3DRenderer::fixGradient(QLinearGradient *gradient, "
        "GLuint *gradientTexture)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def fixGradientAndGenerateTexture(*__, **_) -> Never:
    """
    Qt's 'void
    Abstract3DRenderer::fixGradientAndGenerateTexture(QLinearGradient
    *gradient, GLuint *gradientTexture)': leans on 'Utils::isOpenGLES()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.fixGradientAndGenerateTexture' has no cute "
        "function yet. Qt's 'void "
        "Abstract3DRenderer::fixGradientAndGenerateTexture(QLinearGradient "
        "*gradient, GLuint *gradientTexture)': leans on "
        "'Utils::isOpenGLES()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def fixMeshFileName(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::fixMeshFileName(QString &fileName,
    QAbstract3DSeries::Mesh mesh)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.fixMeshFileName' has no cute function yet. "
        "Qt's 'void Abstract3DRenderer::fixMeshFileName(QString &fileName, "
        "QAbstract3DSeries::Mesh mesh)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def generateBaseColorTexture(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::generateBaseColorTexture(const QColor
    &color, GLuint *texture)': leans on 'Utils::isOpenGLES()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.generateBaseColorTexture' has no cute function "
        "yet. Qt's 'void Abstract3DRenderer::generateBaseColorTexture(const "
        "QColor &color, GLuint *texture)': leans on 'Utils::isOpenGLES()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def getVisibleItemBounds(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::getVisibleItemBounds(QVector3D &minBounds,
    QVector3D &maxBounds)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.getVisibleItemBounds' has no cute function "
        "yet. Qt's 'void Abstract3DRenderer::getVisibleItemBounds(QVector3D "
        "&minBounds, QVector3D &maxBounds)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def loadGridLineMesh(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::loadGridLineMesh()': leans on
    'ObjectHelper::getObjectHelper(Abstract3DRenderer const*, QString
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.loadGridLineMesh' has no cute function yet. "
        "Qt's 'void Abstract3DRenderer::loadGridLineMesh()': leans on "
        "'ObjectHelper::getObjectHelper(Abstract3DRenderer const*, QString "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def loadLabelMesh(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::loadLabelMesh()': leans on
    'ObjectHelper::getObjectHelper(Abstract3DRenderer const*, QString
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.loadLabelMesh' has no cute function yet. Qt's "
        "'void Abstract3DRenderer::loadLabelMesh()': leans on "
        "'ObjectHelper::getObjectHelper(Abstract3DRenderer const*, QString "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def loadPositionMapperMesh(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::loadPositionMapperMesh()': leans on
    'ObjectHelper::getObjectHelper(Abstract3DRenderer const*, QString
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.loadPositionMapperMesh' has no cute function "
        "yet. Qt's 'void Abstract3DRenderer::loadPositionMapperMesh()': "
        "leans on 'ObjectHelper::getObjectHelper(Abstract3DRenderer const*, "
        "QString const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def selectionLabel(*__, **_) -> Never:
    """
    Qt's 'QString &Abstract3DRenderer::selectionLabel()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.selectionLabel' has no cute function yet. Qt's "
        "'QString &Abstract3DRenderer::selectionLabel()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def selectionLabelItem(*__, **_) -> Never:
    """
    Qt's 'LabelItem &Abstract3DRenderer::selectionLabelItem()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.selectionLabelItem' has no cute function yet. "
        "Qt's 'LabelItem &Abstract3DRenderer::selectionLabelItem()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def updateCameraViewport(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::updateCameraViewport()': leans on
    'Q3DCameraPrivate::viewMatrixChanged(QMatrix4x4 const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.updateCameraViewport' has no cute function "
        "yet. Qt's 'void Abstract3DRenderer::updateCameraViewport()': leans "
        "on 'Q3DCameraPrivate::viewMatrixChanged(QMatrix4x4 const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def updateSelectionState(*__, **_) -> Never:
    """
    Qt's 'void Abstract3DRenderer::updateSelectionState(SelectionState
    state)': names the enum 'Abstract3DRenderer::SelectionState', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'Abstract3DRenderer.updateSelectionState' has no cute function "
        "yet. Qt's 'void "
        "Abstract3DRenderer::updateSelectionState(SelectionState state)': "
        "names the enum 'Abstract3DRenderer::SelectionState', whose class "
        "cannot be named here.")
