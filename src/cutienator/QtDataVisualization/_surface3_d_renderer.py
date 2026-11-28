"""
Surface3DRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/surface3drenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Surface3DRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import Abstract3DRenderer, QAbstract3DAxis, QAbstract3DGraph

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QPointF
  from ..QtGui import QMatrix4x4, QVector3D
  from . import Q3DCamera, Q3DScene, QAbstract3DSeries, QSurface3DSeries
  from . import SeriesRenderCache, SurfaceSeriesRenderCache
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DCamera = WAIT['Q3DCamera']
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QSurface3DSeries = WAIT['QtDataVisualization:QSurface3DSeries']
  QVector3D = WAIT['QVector3D']
  SeriesRenderCache = WAIT['SeriesRenderCache']
  SurfaceSeriesRenderCache = WAIT['SurfaceSeriesRenderCache']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Surface3DRenderer(Abstract3DRenderer):
  """
  The cute side of Qt's Surface3DRenderer: a plain Python object standing in
  front of one C++ Surface3DRenderer.

  It is built on the cute 'Abstract3DRenderer', as Qt's Surface3DRenderer is
  built on Qt's Abstract3DRenderer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Surface3DRenderer that has a ritual and that Python
  can call so far, 45 names in all: 'metaObject', 'tr', 'updateData',
  'updateSeries', 'updateSurfaceTextures', 'createNewCache', 'cleanCache',
  'updateSelectionMode', 'updateScene', 'updateSlicingActive',
  'updateSelectedPoint', 'updateFlipHorizontalGrid', 'clickedPosition',
  'resetClickedStatus', 'convertPositionToTranslation', 'updateAxisLabels',
  'updateAxisTitleVisibility', 'updateMargin', 'render', 'contextCleanup',
  'initializeOpenGL', 'flatShadingSupportedChanged', 'checkFlatSupport',
  'updateObjects', 'updateSliceDataModel', 'mapCoordsToSampleSpace',
  'updateSliceObject', 'updateShadowQuality', 'updateTextures',
  'initShaders', 'loadBackgroundMesh', 'drawSlicedScene', 'drawScene',
  'drawLabels', 'calculateSceneScalingFactors', 'initBackgroundShaders',
  'initSelectionShaders', 'initSurfaceShaders', 'initSelectionBuffer',
  'initDepthShader', 'updateSelectionTextures', 'surfacePointSelected',
  'updateSelectionPoint', 'selectionIdToSurfacePoint', 'updateDepthBuffer'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Surface3DRenderer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Surface3DRenderer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Surface3DRenderer::~Surface3DRenderer()': the destructor: Python
    never removes a C++ Surface3DRenderer.
  - Qt's 'void Surface3DRenderer::updateRows(const
    QList<Surface3DController::ChangeRow> &rows)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void Surface3DRenderer::updateItems(const
    QList<Surface3DController::ChangeItem> &points)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void Surface3DRenderer::fixCameraTarget(QVector3D &target)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void Surface3DRenderer::getVisibleItemBounds(QVector3D &minBounds,
    QVector3D &maxBounds)': takes a type Python has no way to hand over yet.
  - Qt's 'void Surface3DRenderer::findMatchingRow(float z, int &sample, int
    direction, QSurfaceDataArray &dataArray)': takes a number to change where
    it is.
  - Qt's 'void Surface3DRenderer::findMatchingColumn(float x, int &sample,
    int direction, QSurfaceDataArray &dataArray)': takes a number to change
    where it is.
  - Qt's 'QRect Surface3DRenderer::calculateSampleRect(const
    QSurfaceDataArray &array)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void
    Surface3DRenderer::createSelectionTexture(SurfaceSeriesRenderCache
    *cache, uint &lastSelectionId)': takes a number to change where it is.
  - Qt's 'void Surface3DRenderer::idToRGBA(uint id, uchar *r, uchar *g, uchar
    *b, uchar *a)': takes a number to change where it is.
  - Qt's 'void Surface3DRenderer::fillIdCorner(uchar *p, uchar r, uchar g,
    uchar b, uchar a)': takes a number to change where it is.

  What has no ritual
  ------------------

  6 of the 64 functions Qt declares: 3 not a gap; 2 forbidden; 1 leans on
  'Abstract3DRenderer.

  What to expect
  --------------

  - The C++ Surface3DRenderer is created at the first use, not by
    'Surface3DRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Surface3DRenderer.
  - Qt tells when it has removed the C++ Surface3DRenderer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Surface3DRenderer that has no cute function yet,
    '__init__', 'calculateSampleRect', 'createSelectionTexture',
    'fillIdCorner', 'findMatchingColumn', 'findMatchingRow', 'idToRGBA',
    'updateItems', 'updateRows', holds a function that raises
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
    Calls Qt's 'QString Surface3DRenderer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/surface3drenderer.html#tr

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
    #  QString Surface3DRenderer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17Surface3DRenderer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Surface3DRenderer'

  #  A C++ Surface3DRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Surface3DRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Surface3DRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/surface3drenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Surface3DRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17Surface3DRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def clickedPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint Surface3DRenderer::clickedPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#clickedPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Surface3DRenderer::clickedPosition() const
    address = self.uglySide.call(
        'ritual_ZNK17Surface3DRenderer15clickedPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'Surface3DRenderer::Surface3DRenderer(Surface3DController
    *controller)': leans on 'Abstract3DRenderer::needRender()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Surface3DRenderer.__init__' has no cute function yet. Qt's "
        "'Surface3DRenderer::Surface3DRenderer(Surface3DController "
        "*controller)': leans on 'Abstract3DRenderer::needRender()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
    Calls Qt's 'void Surface3DRenderer::updateData()'.

    Qt's own words: https://doc.qt.io/qt-6/surface3drenderer.html#updateData
    """
    #  void Surface3DRenderer::updateData()
    ritual = 'ritual_ZN17Surface3DRenderer10updateDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer10updateDataEv'
    self.uglySide.call(ritual)

  @overload(QList[QAbstract3DSeries])
  def updateSeries(self, seriesList: QList[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateSeries(const
    QList<QAbstract3DSeries *> &seriesList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateSeries

    Parameters
    ----------

    seriesList : QList[QAbstract3DSeries]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Surface3DRenderer::updateSeries(const QList<QAbstract3DSeries *>
    #      &seriesList)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer12updateSeriesERK5QListIP17QAbstract3D'
        'SeriesE',
        self._valueOf(seriesList),
    )

  @overload(QList[QSurface3DSeries])
  def updateSurfaceTextures(
      self,
      seriesList: QList[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DRenderer::updateSurfaceTextures(QList<QSurface3DSeries *>
    seriesList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateSurfaceTextures

    Parameters
    ----------

    seriesList : QList[QSurface3DSeries]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Surface3DRenderer::updateSurfaceTextures(QList<QSurface3DSeries
    #      *> seriesList)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer21updateSurfaceTexturesE5QListIP16QSur'
        'face3DSeriesE',
        self._valueOf(seriesList),
    )

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def createNewCache(
      self,
      series: Optional[QAbstract3DSeries],
  ) -> Optional[SeriesRenderCache]:
    """
    Calls Qt's 'SeriesRenderCache
    *Surface3DRenderer::createNewCache(QAbstract3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#createNewCache

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
    #  SeriesRenderCache *Surface3DRenderer::createNewCache(QAbstract3DSeries
    #      *series)
    ritual = (
        'ritual_ZN17Surface3DRenderer14createNewCacheEP17QAbstract3DSeries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Surface3DRenderer14createNewCacheEP17QAbstract3DS'
          'eries')
    address = self.uglySide.call(ritual, self._addressOf(series))
    from . import SeriesRenderCache
    return SeriesRenderCache._cuteAt(address)

  @overload(SeriesRenderCache)
  @overload(NoneType)
  def cleanCache(self, cache: Optional[SeriesRenderCache]) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::cleanCache(SeriesRenderCache
    *cache)'.

    Qt's own words: https://doc.qt.io/qt-6/surface3drenderer.html#cleanCache

    Parameters
    ----------

    cache : Optional[SeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Surface3DRenderer::cleanCache(SeriesRenderCache *cache)
    ritual = 'ritual_ZN17Surface3DRenderer10cleanCacheEP17SeriesRenderCache'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Surface3DRenderer10cleanCacheEP17SeriesRenderCach'
          'e')
    self.uglySide.call(ritual, self._addressOf(cache))

  @overload(QAbstract3DGraph.SelectionFlags)
  def updateSelectionMode(
      self,
      mode: QAbstract3DGraph.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DRenderer::updateSelectionMode(QAbstract3DGraph::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateSelectionMode

    Parameters
    ----------

    mode : QAbstract3DGraph.SelectionFlags
      Passed on as its number.
    """
    #  void Surface3DRenderer::updateSelectionMode(QAbstract3DGraph::
    #      SelectionFlags mode)
    ritual = (
        'ritual_ZN17Surface3DRenderer19updateSelectionModeE6QFlagsIN16QAbst'
        'ract3DGraph13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Surface3DRenderer19updateSelectionModeE6QFlagsIN1'
          '6QAbstract3DGraph13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(Q3DScene)
  @overload(NoneType)
  def updateScene(self, scene: Optional[Q3DScene]) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateScene(Q3DScene *scene)'.

    Qt's own words: https://doc.qt.io/qt-6/surface3drenderer.html#updateScene

    Parameters
    ----------

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Surface3DRenderer::updateScene(Q3DScene *scene)
    ritual = 'ritual_ZN17Surface3DRenderer11updateSceneEP8Q3DScene'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer11updateSceneEP8Q3DScene'
    self.uglySide.call(ritual, self._addressOf(scene))

  @overload(bool)
  def updateSlicingActive(self, isSlicing: bool) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateSlicingActive(bool isSlicing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateSlicingActive

    Parameters
    ----------

    isSlicing : bool
      Passed on as it is.
    """
    #  void Surface3DRenderer::updateSlicingActive(bool isSlicing)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer19updateSlicingActiveEb', isSlicing,
    )

  @overload(QPoint, QSurface3DSeries)
  @overload(QPoint, NoneType)
  def updateSelectedPoint(
      self,
      position: QPoint,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateSelectedPoint(const QPoint
    &position, QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateSelectedPoint

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Surface3DRenderer::updateSelectedPoint(const QPoint &position,
    #      QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer19updateSelectedPointERK6QPointP16QSur'
        'face3DSeries',
        self._valueOf(position), self._addressOf(series),
    )

  @overload(bool)
  def updateFlipHorizontalGrid(self, flip: bool) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateFlipHorizontalGrid(bool flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateFlipHorizontalGrid

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void Surface3DRenderer::updateFlipHorizontalGrid(bool flip)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer24updateFlipHorizontalGridEb', flip,
    )

  def resetClickedStatus(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::resetClickedStatus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#resetClickedStatus
    """
    #  void Surface3DRenderer::resetClickedStatus()
    self.uglySide.call('ritual_ZN17Surface3DRenderer18resetClickedStatusEv')

  @overload(QVector3D, bool)
  def convertPositionToTranslation(
      self,
      position: QVector3D,
      isAbsolute: bool,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Surface3DRenderer::convertPositionToTranslation(const QVector3D
    &position, bool isAbsolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html

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
    #  QVector3D Surface3DRenderer::convertPositionToTranslation(const
    #      QVector3D &position, bool isAbsolute)
    ritual = (
        'ritual_ZN17Surface3DRenderer28convertPositionToTranslationERK9QVec'
        'tor3Db')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Surface3DRenderer28convertPositionToTranslationER'
          'K9QVector3Db')
    address = self.uglySide.call(ritual, self._valueOf(position), isAbsolute)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QAbstract3DAxis.AxisOrientation, QStringList)
  def updateAxisLabels(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      labels: QStringList,
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DRenderer::updateAxisLabels(QAbstract3DAxis::AxisOrientation
    orientation, const QStringList &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateAxisLabels

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Surface3DRenderer::updateAxisLabels(QAbstract3DAxis::
    #      AxisOrientation orientation, const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer16updateAxisLabelsEN15QAbstract3DAxis1'
        '5AxisOrientationERK5QListI7QStringE',
        orientation.value, self._valueOf(labels),
    )

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def updateAxisTitleVisibility(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      visible: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::
    AxisOrientation orientation, bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateAxisTitleVisibility

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    visible : bool
      Passed on as it is.
    """
    #  void Surface3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::
    #      AxisOrientation orientation, bool visible)
    ritual = (
        'ritual_ZN17Surface3DRenderer25updateAxisTitleVisibilityEN15QAbstra'
        'ct3DAxis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Surface3DRenderer25updateAxisTitleVisibilityEN15Q'
          'Abstract3DAxis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, visible)

  @overload(float)
  def updateMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateMargin(float margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Surface3DRenderer::updateMargin(float margin)
    ritual = 'ritual_ZN17Surface3DRenderer12updateMarginEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer12updateMarginEf'
    self.uglySide.call(ritual, margin)

  @overload()
  @overload(int)
  def render(self, defaultFboHandle: int = 0) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::render(GLuint defaultFboHandle)'.

    Qt's own words: https://doc.qt.io/qt-6/surface3drenderer.html#render

    Parameters
    ----------

    defaultFboHandle : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void Surface3DRenderer::render(GLuint defaultFboHandle)
    ritual = 'ritual_ZN17Surface3DRenderer6renderEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer6renderEj'
    self.uglySide.call(ritual, defaultFboHandle)

  def contextCleanup(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::contextCleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#contextCleanup
    """
    #  void Surface3DRenderer::contextCleanup()
    ritual = 'ritual_ZN17Surface3DRenderer14contextCleanupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer14contextCleanupEv'
    self.uglySide.call(ritual)

  def initializeOpenGL(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::initializeOpenGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#initializeOpenGL
    """
    #  void Surface3DRenderer::initializeOpenGL()
    ritual = 'ritual_ZN17Surface3DRenderer16initializeOpenGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer16initializeOpenGLEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def flatShadingSupportedChanged(self, supported: bool) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::flatShadingSupportedChanged(bool
    supported)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#flatShadingSupportedChanged

    Parameters
    ----------

    supported : bool
      Passed on as it is.
    """
    #  void Surface3DRenderer::flatShadingSupportedChanged(bool supported)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer27flatShadingSupportedChangedEb',
        supported,
    )

  @overload(SurfaceSeriesRenderCache)
  @overload(NoneType)
  def checkFlatSupport(
      self,
      cache: Optional[SurfaceSeriesRenderCache],
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DRenderer::checkFlatSupport(SurfaceSeriesRenderCache *cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#checkFlatSupport

    Parameters
    ----------

    cache : Optional[SurfaceSeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Surface3DRenderer::checkFlatSupport(SurfaceSeriesRenderCache
    #      *cache)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer16checkFlatSupportEP24SurfaceSeriesRen'
        'derCache',
        self._addressOf(cache),
    )

  @overload(SurfaceSeriesRenderCache, bool)
  @overload(NoneType, bool)
  def updateObjects(
      self,
      cache: Optional[SurfaceSeriesRenderCache],
      dimensionChanged: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DRenderer::updateObjects(SurfaceSeriesRenderCache *cache, bool
    dimensionChanged)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateObjects

    Parameters
    ----------

    cache : Optional[SurfaceSeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dimensionChanged : bool
      Passed on as it is.
    """
    #  void Surface3DRenderer::updateObjects(SurfaceSeriesRenderCache *cache,
    #      bool dimensionChanged)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer13updateObjectsEP24SurfaceSeriesRender'
        'Cacheb',
        self._addressOf(cache), dimensionChanged,
    )

  @overload(QPoint)
  def updateSliceDataModel(self, point: QPoint) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateSliceDataModel(const QPoint
    &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateSliceDataModel

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Surface3DRenderer::updateSliceDataModel(const QPoint &point)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer20updateSliceDataModelERK6QPoint',
        self._valueOf(point),
    )

  @overload(SurfaceSeriesRenderCache, QPointF)
  @overload(NoneType, QPointF)
  def mapCoordsToSampleSpace(
      self,
      cache: Optional[SurfaceSeriesRenderCache],
      coords: QPointF,
  ) -> QPoint:
    """
    Calls Qt's 'QPoint
    Surface3DRenderer::mapCoordsToSampleSpace(SurfaceSeriesRenderCache
    *cache, const QPointF &coords)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#mapCoordsToSampleSpace

    Parameters
    ----------

    cache : Optional[SurfaceSeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coords : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint
    #      Surface3DRenderer::mapCoordsToSampleSpace(SurfaceSeriesRenderCache
    #      *cache, const QPointF &coords)
    address = self.uglySide.call(
        'ritual_ZN17Surface3DRenderer22mapCoordsToSampleSpaceEP24SurfaceSer'
        'iesRenderCacheRK7QPointF',
        self._addressOf(cache), self._valueOf(coords, 'QPointF'),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(SurfaceSeriesRenderCache, QPoint)
  @overload(NoneType, QPoint)
  def updateSliceObject(
      self,
      cache: Optional[SurfaceSeriesRenderCache],
      point: QPoint,
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DRenderer::updateSliceObject(SurfaceSeriesRenderCache *cache,
    const QPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateSliceObject

    Parameters
    ----------

    cache : Optional[SurfaceSeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Surface3DRenderer::updateSliceObject(SurfaceSeriesRenderCache
    #      *cache, const QPoint &point)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer17updateSliceObjectEP24SurfaceSeriesRe'
        'nderCacheRK6QPoint',
        self._addressOf(cache), self._valueOf(point),
    )

  @overload(QAbstract3DGraph.ShadowQuality)
  def updateShadowQuality(
      self,
      quality: QAbstract3DGraph.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateShadowQuality

    Parameters
    ----------

    quality : QAbstract3DGraph.ShadowQuality
      Passed on as its number.
    """
    #  void Surface3DRenderer::updateShadowQuality(QAbstract3DGraph::
    #      ShadowQuality quality)
    ritual = (
        'ritual_ZN17Surface3DRenderer19updateShadowQualityEN16QAbstract3DGr'
        'aph13ShadowQualityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Surface3DRenderer19updateShadowQualityEN16QAbstra'
          'ct3DGraph13ShadowQualityE')
    self.uglySide.call(ritual, quality.value)

  def updateTextures(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateTextures()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateTextures
    """
    #  void Surface3DRenderer::updateTextures()
    ritual = 'ritual_ZN17Surface3DRenderer14updateTexturesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer14updateTexturesEv'
    self.uglySide.call(ritual)

  @overload(str, str)
  def initShaders(self, vertexShader: str, fragmentShader: str) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::initShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words: https://doc.qt.io/qt-6/surface3drenderer.html#initShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Surface3DRenderer::initShaders(const QString &vertexShader, const
    #      QString &fragmentShader)
    ritual = 'ritual_ZN17Surface3DRenderer11initShadersERK7QStringS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer11initShadersERK7QStringS2_'
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  def loadBackgroundMesh(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::loadBackgroundMesh()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#loadBackgroundMesh
    """
    #  void Surface3DRenderer::loadBackgroundMesh()
    self.uglySide.call('ritual_ZN17Surface3DRenderer18loadBackgroundMeshEv')

  def drawSlicedScene(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::drawSlicedScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#drawSlicedScene
    """
    #  void Surface3DRenderer::drawSlicedScene()
    self.uglySide.call('ritual_ZN17Surface3DRenderer15drawSlicedSceneEv')

  @overload(int)
  def drawScene(self, defaultFboHandle: int) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::drawScene(GLuint defaultFboHandle)'.

    Qt's own words: https://doc.qt.io/qt-6/surface3drenderer.html#drawScene

    Parameters
    ----------

    defaultFboHandle : int
      Passed on as it is.
    """
    #  void Surface3DRenderer::drawScene(GLuint defaultFboHandle)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer9drawSceneEj', defaultFboHandle,
    )

  @overload(bool, Q3DCamera, QMatrix4x4, QMatrix4x4)
  @overload(bool, NoneType, QMatrix4x4, QMatrix4x4)
  def drawLabels(
      self,
      drawSelection: bool,
      activeCamera: Optional[Q3DCamera],
      viewMatrix: QMatrix4x4,
      projectionMatrix: QMatrix4x4,
  ) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::drawLabels(bool drawSelection, const
    Q3DCamera *activeCamera, const QMatrix4x4 &viewMatrix, const QMatrix4x4
    &projectionMatrix)'.

    Qt's own words: https://doc.qt.io/qt-6/surface3drenderer.html#drawLabels

    Parameters
    ----------

    drawSelection : bool
      Passed on as it is.

    activeCamera : Optional[Q3DCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    projectionMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Surface3DRenderer::drawLabels(bool drawSelection, const Q3DCamera
    #      *activeCamera, const QMatrix4x4 &viewMatrix, const QMatrix4x4
    #      &projectionMatrix)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer10drawLabelsEbPK9Q3DCameraRK10QMatrix4'
        'x4S5_',
        drawSelection, self._addressOf(activeCamera),
        self._valueOf(viewMatrix), self._valueOf(projectionMatrix),
    )

  def calculateSceneScalingFactors(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::calculateSceneScalingFactors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html
    """
    #  void Surface3DRenderer::calculateSceneScalingFactors()
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer28calculateSceneScalingFactorsEv',
    )

  @overload(str, str)
  def initBackgroundShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::initBackgroundShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#initBackgroundShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Surface3DRenderer::initBackgroundShaders(const QString
    #      &vertexShader, const QString &fragmentShader)
    ritual = (
        'ritual_ZN17Surface3DRenderer21initBackgroundShadersERK7QStringS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Surface3DRenderer21initBackgroundShadersERK7QStri'
          'ngS2_')
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  def initSelectionShaders(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::initSelectionShaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#initSelectionShaders
    """
    #  void Surface3DRenderer::initSelectionShaders()
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer20initSelectionShadersEv',
    )

  def initSurfaceShaders(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::initSurfaceShaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#initSurfaceShaders
    """
    #  void Surface3DRenderer::initSurfaceShaders()
    self.uglySide.call('ritual_ZN17Surface3DRenderer18initSurfaceShadersEv')

  def initSelectionBuffer(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::initSelectionBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#initSelectionBuffer
    """
    #  void Surface3DRenderer::initSelectionBuffer()
    ritual = 'ritual_ZN17Surface3DRenderer19initSelectionBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer19initSelectionBufferEv'
    self.uglySide.call(ritual)

  def initDepthShader(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::initDepthShader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#initDepthShader
    """
    #  void Surface3DRenderer::initDepthShader()
    self.uglySide.call('ritual_ZN17Surface3DRenderer15initDepthShaderEv')

  def updateSelectionTextures(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateSelectionTextures()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateSelectionTextures
    """
    #  void Surface3DRenderer::updateSelectionTextures()
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer23updateSelectionTexturesEv',
    )

  @overload(QPoint)
  def surfacePointSelected(self, point: QPoint) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::surfacePointSelected(const QPoint
    &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#surfacePointSelected

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Surface3DRenderer::surfacePointSelected(const QPoint &point)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer20surfacePointSelectedERK6QPoint',
        self._valueOf(point),
    )

  @overload(SurfaceSeriesRenderCache, QPoint, bool)
  @overload(NoneType, QPoint, bool)
  def updateSelectionPoint(
      self,
      cache: Optional[SurfaceSeriesRenderCache],
      point: QPoint,
      label: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Surface3DRenderer::updateSelectionPoint(SurfaceSeriesRenderCache *cache,
    const QPoint &point, bool label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateSelectionPoint

    Parameters
    ----------

    cache : Optional[SurfaceSeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    label : bool
      Passed on as it is.
    """
    #  void Surface3DRenderer::updateSelectionPoint(SurfaceSeriesRenderCache
    #      *cache, const QPoint &point, bool label)
    self.uglySide.call(
        'ritual_ZN17Surface3DRenderer20updateSelectionPointEP24SurfaceSerie'
        'sRenderCacheRK6QPointb',
        self._addressOf(cache), self._valueOf(point), label,
    )

  @overload(int)
  def selectionIdToSurfacePoint(self, id: int) -> QPoint:
    """
    Calls Qt's 'QPoint Surface3DRenderer::selectionIdToSurfacePoint(uint
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#selectionIdToSurfacePoint

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Surface3DRenderer::selectionIdToSurfacePoint(uint id)
    address = self.uglySide.call(
        'ritual_ZN17Surface3DRenderer25selectionIdToSurfacePointEj', id,
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def updateDepthBuffer(self) -> None:
    """
    Calls Qt's 'void Surface3DRenderer::updateDepthBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/surface3drenderer.html#updateDepthBuffer
    """
    #  void Surface3DRenderer::updateDepthBuffer()
    ritual = 'ritual_ZN17Surface3DRenderer17updateDepthBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Surface3DRenderer17updateDepthBufferEv'
    self.uglySide.call(ritual)

  @staticmethod
  def calculateSampleRect(*__, **_) -> Never:
    """
    Qt's 'QRect Surface3DRenderer::calculateSampleRect(const
    QSurfaceDataArray &array)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Surface3DRenderer.calculateSampleRect' has no cute function yet. "
        "Qt's 'QRect Surface3DRenderer::calculateSampleRect(const "
        "QSurfaceDataArray &array)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def createSelectionTexture(*__, **_) -> Never:
    """
    Qt's 'void
    Surface3DRenderer::createSelectionTexture(SurfaceSeriesRenderCache
    *cache, uint &lastSelectionId)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'Surface3DRenderer.createSelectionTexture' has no cute function "
        "yet. Qt's 'void "
        "Surface3DRenderer::createSelectionTexture(SurfaceSeriesRenderCache "
        "*cache, uint &lastSelectionId)': takes a number to change where it "
        "is.")

  @staticmethod
  def fillIdCorner(*__, **_) -> Never:
    """
    Qt's 'void Surface3DRenderer::fillIdCorner(uchar *p, uchar r, uchar g,
    uchar b, uchar a)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'Surface3DRenderer.fillIdCorner' has no cute function yet. Qt's "
        "'void Surface3DRenderer::fillIdCorner(uchar *p, uchar r, uchar g, "
        "uchar b, uchar a)': takes a number to change where it is.")

  @staticmethod
  def findMatchingColumn(*__, **_) -> Never:
    """
    Qt's 'void Surface3DRenderer::findMatchingColumn(float x, int &sample,
    int direction, QSurfaceDataArray &dataArray)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'Surface3DRenderer.findMatchingColumn' has no cute function yet. "
        "Qt's 'void Surface3DRenderer::findMatchingColumn(float x, int "
        "&sample, int direction, QSurfaceDataArray &dataArray)': takes a "
        "number to change where it is.")

  @staticmethod
  def findMatchingRow(*__, **_) -> Never:
    """
    Qt's 'void Surface3DRenderer::findMatchingRow(float z, int &sample, int
    direction, QSurfaceDataArray &dataArray)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'Surface3DRenderer.findMatchingRow' has no cute function yet. Qt's "
        "'void Surface3DRenderer::findMatchingRow(float z, int &sample, int "
        "direction, QSurfaceDataArray &dataArray)': takes a number to "
        "change where it is.")

  @staticmethod
  def idToRGBA(*__, **_) -> Never:
    """
    Qt's 'void Surface3DRenderer::idToRGBA(uint id, uchar *r, uchar *g, uchar
    *b, uchar *a)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'Surface3DRenderer.idToRGBA' has no cute function yet. Qt's 'void "
        "Surface3DRenderer::idToRGBA(uint id, uchar *r, uchar *g, uchar *b, "
        "uchar *a)': takes a number to change where it is.")

  @staticmethod
  def updateItems(*__, **_) -> Never:
    """
    Qt's 'void Surface3DRenderer::updateItems(const
    QList<Surface3DController::ChangeItem> &points)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'Surface3DRenderer.updateItems' has no cute function yet. Qt's "
        "'void Surface3DRenderer::updateItems(const "
        "QList<Surface3DController::ChangeItem> &points)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def updateRows(*__, **_) -> Never:
    """
    Qt's 'void Surface3DRenderer::updateRows(const
    QList<Surface3DController::ChangeRow> &rows)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Surface3DRenderer.updateRows' has no cute function yet. Qt's "
        "'void Surface3DRenderer::updateRows(const "
        "QList<Surface3DController::ChangeRow> &rows)': takes a type Python "
        "has no way to hand over yet.")
