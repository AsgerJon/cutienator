"""
Bars3DRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/bars3drenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Bars3DRenderer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import Abstract3DController, Abstract3DRenderer, QAbstract3DAxis
from . import QAbstract3DGraph

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QSizeF
  from ..QtGui import QMatrix4x4, QVector3D, QVector4D
  from . import BarSeriesRenderCache, Q3DCamera, Q3DScene, QAbstract3DSeries
  from . import QBar3DSeries, SeriesRenderCache
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  BarSeriesRenderCache = WAIT['BarSeriesRenderCache']
  Q3DCamera = WAIT['Q3DCamera']
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QBar3DSeries = WAIT['QtDataVisualization:QBar3DSeries']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QPoint = WAIT['QPoint']
  QSizeF = WAIT['QSizeF']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Bars3DRenderer(Abstract3DRenderer):
  """
  The cute side of Qt's Bars3DRenderer: a plain Python object standing in
  front of one C++ Bars3DRenderer.

  It is built on the cute 'Abstract3DRenderer', as Qt's Bars3DRenderer is
  built on Qt's Abstract3DRenderer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Bars3DRenderer that has a ritual and that Python can
  call so far, 43 names in all: 'metaObject', 'tr', 'updateData',
  'updateSeries', 'createNewCache', 'updateScene', 'render',
  'convertPositionToTranslation', 'updateAspectRatio', 'updateFloorLevel',
  'updateMargin', 'contextCleanup', 'initializeOpenGL',
  'updateMultiSeriesScaling', 'updateBarSpecs', 'updateBarSeriesMargin',
  'updateSlicingActive', 'updateSelectedBar', 'clickedPosition',
  'resetClickedStatus', 'updateAxisRange', 'updateAxisReversed',
  'initShaders', 'initGradientShaders', 'updateShadowQuality',
  'updateTextures', 'drawSlicedScene', 'drawScene', 'drawLabels',
  'drawBackground', 'drawGridLines', 'loadBackgroundMesh',
  'initSelectionShader', 'initBackgroundShaders', 'initSelectionBuffer',
  'initDepthShader', 'updateDepthBuffer', 'calculateSceneScalingFactors',
  'calculateHeightAdjustment', 'calculateSeriesStartPosition', 'isSelected',
  'selectionColorToArrayPosition', 'selectionColorToSeries'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Bars3DRenderer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int Bars3DRenderer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Bars3DRenderer::~Bars3DRenderer()': the destructor: Python never
    removes a C++ Bars3DRenderer.
  - Qt's 'void Bars3DRenderer::updateRows(const
    QList<Bars3DController::ChangeRow> &rows)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void Bars3DRenderer::updateItems(const
    QList<Bars3DController::ChangeItem> &items)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void Bars3DRenderer::fixCameraTarget(QVector3D &target)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void Bars3DRenderer::getVisibleItemBounds(QVector3D &minBounds,
    QVector3D &maxBounds)': takes a type Python has no way to hand over yet.
  - Qt's 'void Bars3DRenderer::fixMeshFileName(QString &fileName,
    QAbstract3DSeries::Mesh mesh)': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool Bars3DRenderer::drawBars(BarRenderItem **selectedBar, const
    QMatrix4x4 &depthProjectionViewMatrix, const QMatrix4x4
    &projectionViewMatrix, const QMatrix4x4 &viewMatrix, GLint startRow,
    GLint stopRow, GLint stepRow, GLint startBar, GLint stopBar, GLint
    stepBar, GLfloat reflection)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void Bars3DRenderer::updateRenderRow(const QBarDataRow *dataRow,
    BarRenderItemRow &renderRow)': names 'QBarDataRow', which has no cute
    class yet.
  - Qt's 'void Bars3DRenderer::updateRenderItem(const QBarDataItem &dataItem,
    BarRenderItem &renderItem)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  5 of the 59 functions Qt declares: 2 not a gap; 2 forbidden; 1 leans on
  'Abstract3DRenderer.

  What to expect
  --------------

  - The C++ Bars3DRenderer is created at the first use, not by
    'Bars3DRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Bars3DRenderer.
  - Qt tells when it has removed the C++ Bars3DRenderer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Bars3DRenderer that has no cute function yet,
    '__init__', 'drawBars', 'updateItems', 'updateRenderItem',
    'updateRenderRow', 'updateRows', holds a function that raises
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
    Calls Qt's 'QString Bars3DRenderer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#tr

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
    #  QString Bars3DRenderer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14Bars3DRenderer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Bars3DRenderer'

  #  A C++ Bars3DRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Bars3DRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Bars3DRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Bars3DRenderer::metaObject() const
    address = self.uglySide.call('ritual_ZNK14Bars3DRenderer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def clickedPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint Bars3DRenderer::clickedPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#clickedPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Bars3DRenderer::clickedPosition() const
    address = self.uglySide.call(
        'ritual_ZNK14Bars3DRenderer15clickedPositionEv',
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
    Qt's 'Bars3DRenderer::Bars3DRenderer(Bars3DController *controller)':
    leans on 'Abstract3DRenderer::needRender()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Bars3DRenderer.__init__' has no cute function yet. Qt's "
        "'Bars3DRenderer::Bars3DRenderer(Bars3DController *controller)': "
        "leans on 'Abstract3DRenderer::needRender()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    Calls Qt's 'void Bars3DRenderer::updateData()'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#updateData
    """
    #  void Bars3DRenderer::updateData()
    ritual = 'ritual_ZN14Bars3DRenderer10updateDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer10updateDataEv'
    self.uglySide.call(ritual)

  @overload(QList[QAbstract3DSeries])
  def updateSeries(self, seriesList: QList[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateSeries(const
    QList<QAbstract3DSeries *> &seriesList)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#updateSeries

    Parameters
    ----------

    seriesList : QList[QAbstract3DSeries]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Bars3DRenderer::updateSeries(const QList<QAbstract3DSeries *>
    #      &seriesList)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer12updateSeriesERK5QListIP17QAbstract3DSer'
        'iesE',
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
    *Bars3DRenderer::createNewCache(QAbstract3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#createNewCache

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
    #  SeriesRenderCache *Bars3DRenderer::createNewCache(QAbstract3DSeries
    #      *series)
    ritual = 'ritual_ZN14Bars3DRenderer14createNewCacheEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14Bars3DRenderer14createNewCacheEP17QAbstract3DSeri'
          'es')
    address = self.uglySide.call(ritual, self._addressOf(series))
    from . import SeriesRenderCache
    return SeriesRenderCache._cuteAt(address)

  @overload(Q3DScene)
  @overload(NoneType)
  def updateScene(self, scene: Optional[Q3DScene]) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateScene(Q3DScene *scene)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#updateScene

    Parameters
    ----------

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DRenderer::updateScene(Q3DScene *scene)
    ritual = 'ritual_ZN14Bars3DRenderer11updateSceneEP8Q3DScene'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer11updateSceneEP8Q3DScene'
    self.uglySide.call(ritual, self._addressOf(scene))

  @overload()
  @overload(int)
  def render(self, defaultFboHandle: int = 0) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::render(GLuint defaultFboHandle)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#render

    Parameters
    ----------

    defaultFboHandle : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void Bars3DRenderer::render(GLuint defaultFboHandle)
    ritual = 'ritual_ZN14Bars3DRenderer6renderEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer6renderEj'
    self.uglySide.call(ritual, defaultFboHandle)

  @overload(QVector3D, bool)
  def convertPositionToTranslation(
      self,
      position: QVector3D,
      isAbsolute: bool,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D Bars3DRenderer::convertPositionToTranslation(const
    QVector3D &position, bool isAbsolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#convertPositionToTranslation

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
    #  QVector3D Bars3DRenderer::convertPositionToTranslation(const QVector3D
    #      &position, bool isAbsolute)
    ritual = (
        'ritual_ZN14Bars3DRenderer28convertPositionToTranslationERK9QVector'
        '3Db')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14Bars3DRenderer28convertPositionToTranslationERK9Q'
          'Vector3Db')
    address = self.uglySide.call(ritual, self._valueOf(position), isAbsolute)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(float)
  def updateAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateAspectRatio(float ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Bars3DRenderer::updateAspectRatio(float ratio)
    ritual = 'ritual_ZN14Bars3DRenderer17updateAspectRatioEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer17updateAspectRatioEf'
    self.uglySide.call(ritual, ratio)

  @overload(float)
  def updateFloorLevel(self, level: float) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateFloorLevel(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateFloorLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void Bars3DRenderer::updateFloorLevel(float level)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer16updateFloorLevelEf', level,
    )

  @overload(float)
  def updateMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateMargin(float margin)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#updateMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Bars3DRenderer::updateMargin(float margin)
    ritual = 'ritual_ZN14Bars3DRenderer12updateMarginEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer12updateMarginEf'
    self.uglySide.call(ritual, margin)

  def contextCleanup(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::contextCleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#contextCleanup
    """
    #  void Bars3DRenderer::contextCleanup()
    ritual = 'ritual_ZN14Bars3DRenderer14contextCleanupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer14contextCleanupEv'
    self.uglySide.call(ritual)

  def initializeOpenGL(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::initializeOpenGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#initializeOpenGL
    """
    #  void Bars3DRenderer::initializeOpenGL()
    ritual = 'ritual_ZN14Bars3DRenderer16initializeOpenGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer16initializeOpenGLEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def updateMultiSeriesScaling(self, uniform: bool) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateMultiSeriesScaling(bool uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateMultiSeriesScaling

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void Bars3DRenderer::updateMultiSeriesScaling(bool uniform)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer24updateMultiSeriesScalingEb', uniform,
    )

  @overload()
  @overload(float)
  @overload(float, QSizeF)
  @overload(float, QSizeF, bool)
  def updateBarSpecs(
      self,
      thicknessRatio: float = 1.0,
      spacing: Optional[QSizeF] = None,
      relative: bool = True,
  ) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateBarSpecs(GLfloat thicknessRatio,
    const QSizeF &spacing, bool relative)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#updateBarSpecs

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    spacing : Optional[QSizeF]
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own. May be left out, as in Qt: a new 'QSizeF(1.0, 1.0)' is then passed
      on.

    relative : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void Bars3DRenderer::updateBarSpecs(GLfloat thicknessRatio, const
    #      QSizeF &spacing, bool relative)
    if spacing is None:
      from ..QtCore import QSizeF
      spacing = QSizeF(1.0, 1.0)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer14updateBarSpecsEfRK6QSizeFb',
        thicknessRatio, self._valueOf(spacing), relative,
    )

  @overload(QSizeF)
  def updateBarSeriesMargin(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateBarSeriesMargin(const QSizeF
    &margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateBarSeriesMargin

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Bars3DRenderer::updateBarSeriesMargin(const QSizeF &margin)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer21updateBarSeriesMarginERK6QSizeF',
        self._valueOf(margin),
    )

  @overload(bool)
  def updateSlicingActive(self, isSlicing: bool) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateSlicingActive(bool isSlicing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateSlicingActive

    Parameters
    ----------

    isSlicing : bool
      Passed on as it is.
    """
    #  void Bars3DRenderer::updateSlicingActive(bool isSlicing)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer19updateSlicingActiveEb', isSlicing,
    )

  @overload(QPoint, QBar3DSeries)
  @overload(QPoint, NoneType)
  def updateSelectedBar(
      self,
      position: QPoint,
      series: Optional[QBar3DSeries],
  ) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateSelectedBar(const QPoint
    &position, QBar3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateSelectedBar

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bars3DRenderer::updateSelectedBar(const QPoint &position,
    #      QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer17updateSelectedBarERK6QPointP12QBar3DSer'
        'ies',
        self._valueOf(position), self._addressOf(series),
    )

  def resetClickedStatus(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::resetClickedStatus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#resetClickedStatus
    """
    #  void Bars3DRenderer::resetClickedStatus()
    self.uglySide.call('ritual_ZN14Bars3DRenderer18resetClickedStatusEv')

  @overload(QAbstract3DAxis.AxisOrientation, float, float)
  def updateAxisRange(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      min: float,
      max: float,
  ) -> None:
    """
    Calls Qt's 'void
    Bars3DRenderer::updateAxisRange(QAbstract3DAxis::AxisOrientation
    orientation, float min, float max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateAxisRange

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void Bars3DRenderer::updateAxisRange(QAbstract3DAxis::AxisOrientation
    #      orientation, float min, float max)
    ritual = (
        'ritual_ZN14Bars3DRenderer15updateAxisRangeEN15QAbstract3DAxis15Axi'
        'sOrientationEff')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14Bars3DRenderer15updateAxisRangeEN15QAbstract3DAxi'
          's15AxisOrientationEff')
    self.uglySide.call(ritual, orientation.value, min, max)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def updateAxisReversed(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      enable: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Bars3DRenderer::updateAxisReversed(QAbstract3DAxis::AxisOrientation
    orientation, bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateAxisReversed

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    enable : bool
      Passed on as it is.
    """
    #  void Bars3DRenderer::updateAxisReversed(QAbstract3DAxis::
    #      AxisOrientation orientation, bool enable)
    ritual = (
        'ritual_ZN14Bars3DRenderer18updateAxisReversedEN15QAbstract3DAxis15'
        'AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14Bars3DRenderer18updateAxisReversedEN15QAbstract3D'
          'Axis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, enable)

  @overload(str, str)
  def initShaders(self, vertexShader: str, fragmentShader: str) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::initShaders(const QString &vertexShader,
    const QString &fragmentShader)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#initShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Bars3DRenderer::initShaders(const QString &vertexShader, const
    #      QString &fragmentShader)
    ritual = 'ritual_ZN14Bars3DRenderer11initShadersERK7QStringS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer11initShadersERK7QStringS2_'
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  @overload(str, str)
  def initGradientShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::initGradientShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#initGradientShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Bars3DRenderer::initGradientShaders(const QString &vertexShader,
    #      const QString &fragmentShader)
    ritual = 'ritual_ZN14Bars3DRenderer19initGradientShadersERK7QStringS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14Bars3DRenderer19initGradientShadersERK7QStringS2_')
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  @overload(QAbstract3DGraph.ShadowQuality)
  def updateShadowQuality(
      self,
      quality: QAbstract3DGraph.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    Bars3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateShadowQuality

    Parameters
    ----------

    quality : QAbstract3DGraph.ShadowQuality
      Passed on as its number.
    """
    #  void Bars3DRenderer::updateShadowQuality(QAbstract3DGraph::
    #      ShadowQuality quality)
    ritual = (
        'ritual_ZN14Bars3DRenderer19updateShadowQualityEN16QAbstract3DGraph'
        '13ShadowQualityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14Bars3DRenderer19updateShadowQualityEN16QAbstract3'
          'DGraph13ShadowQualityE')
    self.uglySide.call(ritual, quality.value)

  def updateTextures(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateTextures()'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#updateTextures
    """
    #  void Bars3DRenderer::updateTextures()
    ritual = 'ritual_ZN14Bars3DRenderer14updateTexturesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer14updateTexturesEv'
    self.uglySide.call(ritual)

  def drawSlicedScene(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::drawSlicedScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#drawSlicedScene
    """
    #  void Bars3DRenderer::drawSlicedScene()
    self.uglySide.call('ritual_ZN14Bars3DRenderer15drawSlicedSceneEv')

  @overload(int)
  def drawScene(self, defaultFboHandle: int) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::drawScene(GLuint defaultFboHandle)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#drawScene

    Parameters
    ----------

    defaultFboHandle : int
      Passed on as it is.
    """
    #  void Bars3DRenderer::drawScene(GLuint defaultFboHandle)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer9drawSceneEj', defaultFboHandle,
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
    Calls Qt's 'void Bars3DRenderer::drawLabels(bool drawSelection, const
    Q3DCamera *activeCamera, const QMatrix4x4 &viewMatrix, const QMatrix4x4
    &projectionMatrix)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#drawLabels

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
    #  void Bars3DRenderer::drawLabels(bool drawSelection, const Q3DCamera
    #      *activeCamera, const QMatrix4x4 &viewMatrix, const QMatrix4x4
    #      &projectionMatrix)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer10drawLabelsEbPK9Q3DCameraRK10QMatrix4x4S'
        '5_',
        drawSelection, self._addressOf(activeCamera),
        self._valueOf(viewMatrix), self._valueOf(projectionMatrix),
    )

  @overload(float, QMatrix4x4, QMatrix4x4, QMatrix4x4)
  @overload(float, QMatrix4x4, QMatrix4x4, QMatrix4x4, bool)
  @overload(float, QMatrix4x4, QMatrix4x4, QMatrix4x4, bool, bool)
  def drawBackground(
      self,
      backgroundRotation: float,
      depthProjectionViewMatrix: QMatrix4x4,
      projectionViewMatrix: QMatrix4x4,
      viewMatrix: QMatrix4x4,
      reflectingDraw: bool = False,
      drawingSelectionBuffer: bool = False,
  ) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::drawBackground(GLfloat
    backgroundRotation, const QMatrix4x4 &depthProjectionViewMatrix, const
    QMatrix4x4 &projectionViewMatrix, const QMatrix4x4 &viewMatrix, bool
    reflectingDraw, bool drawingSelectionBuffer)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#drawBackground

    Parameters
    ----------

    backgroundRotation : float
      Passed on as it is.

    depthProjectionViewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    projectionViewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    viewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    reflectingDraw : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    drawingSelectionBuffer : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void Bars3DRenderer::drawBackground(GLfloat backgroundRotation, const
    #      QMatrix4x4 &depthProjectionViewMatrix, const QMatrix4x4
    #      &projectionViewMatrix, const QMatrix4x4 &viewMatrix, bool
    #      reflectingDraw, bool drawingSelectionBuffer)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer14drawBackgroundEfRK10QMatrix4x4S2_S2_bb',
        backgroundRotation, self._valueOf(depthProjectionViewMatrix),
        self._valueOf(projectionViewMatrix), self._valueOf(viewMatrix),
        reflectingDraw, drawingSelectionBuffer,
    )

  @overload(QMatrix4x4, QMatrix4x4, QMatrix4x4)
  def drawGridLines(
      self,
      depthProjectionViewMatrix: QMatrix4x4,
      projectionViewMatrix: QMatrix4x4,
      viewMatrix: QMatrix4x4,
  ) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::drawGridLines(const QMatrix4x4
    &depthProjectionViewMatrix, const QMatrix4x4 &projectionViewMatrix, const
    QMatrix4x4 &viewMatrix)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#drawGridLines

    Parameters
    ----------

    depthProjectionViewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    projectionViewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    viewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Bars3DRenderer::drawGridLines(const QMatrix4x4
    #      &depthProjectionViewMatrix, const QMatrix4x4
    #      &projectionViewMatrix, const QMatrix4x4 &viewMatrix)
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer13drawGridLinesERK10QMatrix4x4S2_S2_',
        self._valueOf(depthProjectionViewMatrix),
        self._valueOf(projectionViewMatrix), self._valueOf(viewMatrix),
    )

  def loadBackgroundMesh(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::loadBackgroundMesh()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#loadBackgroundMesh
    """
    #  void Bars3DRenderer::loadBackgroundMesh()
    self.uglySide.call('ritual_ZN14Bars3DRenderer18loadBackgroundMeshEv')

  def initSelectionShader(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::initSelectionShader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#initSelectionShader
    """
    #  void Bars3DRenderer::initSelectionShader()
    self.uglySide.call('ritual_ZN14Bars3DRenderer19initSelectionShaderEv')

  @overload(str, str)
  def initBackgroundShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::initBackgroundShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#initBackgroundShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Bars3DRenderer::initBackgroundShaders(const QString
    #      &vertexShader, const QString &fragmentShader)
    ritual = 'ritual_ZN14Bars3DRenderer21initBackgroundShadersERK7QStringS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14Bars3DRenderer21initBackgroundShadersERK7QStringS'
          '2_')
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  def initSelectionBuffer(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::initSelectionBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#initSelectionBuffer
    """
    #  void Bars3DRenderer::initSelectionBuffer()
    ritual = 'ritual_ZN14Bars3DRenderer19initSelectionBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer19initSelectionBufferEv'
    self.uglySide.call(ritual)

  def initDepthShader(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::initDepthShader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#initDepthShader
    """
    #  void Bars3DRenderer::initDepthShader()
    self.uglySide.call('ritual_ZN14Bars3DRenderer15initDepthShaderEv')

  def updateDepthBuffer(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::updateDepthBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#updateDepthBuffer
    """
    #  void Bars3DRenderer::updateDepthBuffer()
    ritual = 'ritual_ZN14Bars3DRenderer17updateDepthBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14Bars3DRenderer17updateDepthBufferEv'
    self.uglySide.call(ritual)

  def calculateSceneScalingFactors(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::calculateSceneScalingFactors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#calculateSceneScalingFactors
    """
    #  void Bars3DRenderer::calculateSceneScalingFactors()
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer28calculateSceneScalingFactorsEv',
    )

  def calculateHeightAdjustment(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::calculateHeightAdjustment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#calculateHeightAdjustment
    """
    #  void Bars3DRenderer::calculateHeightAdjustment()
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer25calculateHeightAdjustmentEv',
    )

  def calculateSeriesStartPosition(self) -> None:
    """
    Calls Qt's 'void Bars3DRenderer::calculateSeriesStartPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#calculateSeriesStartPosition
    """
    #  void Bars3DRenderer::calculateSeriesStartPosition()
    self.uglySide.call(
        'ritual_ZN14Bars3DRenderer28calculateSeriesStartPositionEv',
    )

  @overload(int, int, BarSeriesRenderCache)
  @overload(int, int, NoneType)
  def isSelected(
      self,
      row: int,
      bar: int,
      cache: Optional[BarSeriesRenderCache],
  ) -> Abstract3DController.SelectionType:
    """
    Calls Qt's 'Abstract3DController::SelectionType
    Bars3DRenderer::isSelected(int row, int bar, const BarSeriesRenderCache
    *cache)'.

    Qt's own words: https://doc.qt.io/qt-6/bars3drenderer.html#isSelected

    Parameters
    ----------

    row : int
      Passed on as it is.

    bar : int
      Passed on as it is.

    cache : Optional[BarSeriesRenderCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Abstract3DController.SelectionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Abstract3DController.SelectionType(number)' gives.
    """
    #  Abstract3DController::SelectionType Bars3DRenderer::isSelected(int
    #      row, int bar, const BarSeriesRenderCache *cache)
    return Abstract3DController.SelectionType(self.uglySide.call(
        'ritual_ZN14Bars3DRenderer10isSelectedEiiPK20BarSeriesRenderCache',
        row, bar, self._addressOf(cache),
    ))

  @overload(QVector4D)
  def selectionColorToArrayPosition(
      self,
      selectionColor: QVector4D,
  ) -> QPoint:
    """
    Calls Qt's 'QPoint Bars3DRenderer::selectionColorToArrayPosition(const
    QVector4D &selectionColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#selectionColorToArrayPosition

    Parameters
    ----------

    selectionColor : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Bars3DRenderer::selectionColorToArrayPosition(const QVector4D
    #      &selectionColor)
    address = self.uglySide.call(
        'ritual_ZN14Bars3DRenderer29selectionColorToArrayPositionERK9QVecto'
        'r4D',
        self._valueOf(selectionColor),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QVector4D)
  def selectionColorToSeries(
      self,
      selectionColor: QVector4D,
  ) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *Bars3DRenderer::selectionColorToSeries(const
    QVector4D &selectionColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/bars3drenderer.html#selectionColorToSeries

    Parameters
    ----------

    selectionColor : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *Bars3DRenderer::selectionColorToSeries(const QVector4D
    #      &selectionColor)
    address = self.uglySide.call(
        'ritual_ZN14Bars3DRenderer22selectionColorToSeriesERK9QVector4D',
        self._valueOf(selectionColor),
    )
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  @staticmethod
  def drawBars(*__, **_) -> Never:
    """
    Qt's 'bool Bars3DRenderer::drawBars(BarRenderItem **selectedBar, const
    QMatrix4x4 &depthProjectionViewMatrix, const QMatrix4x4
    &projectionViewMatrix, const QMatrix4x4 &viewMatrix, GLint startRow,
    GLint stopRow, GLint stepRow, GLint startBar, GLint stopBar, GLint
    stepBar, GLfloat reflection)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Bars3DRenderer.drawBars' has no cute function yet. Qt's 'bool "
        "Bars3DRenderer::drawBars(BarRenderItem **selectedBar, const "
        "QMatrix4x4 &depthProjectionViewMatrix, const QMatrix4x4 "
        "&projectionViewMatrix, const QMatrix4x4 &viewMatrix, GLint "
        "startRow, GLint stopRow, GLint stepRow, GLint startBar, GLint "
        "stopBar, GLint stepBar, GLfloat reflection)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def updateItems(*__, **_) -> Never:
    """
    Qt's 'void Bars3DRenderer::updateItems(const
    QList<Bars3DController::ChangeItem> &items)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Bars3DRenderer.updateItems' has no cute function yet. Qt's 'void "
        "Bars3DRenderer::updateItems(const "
        "QList<Bars3DController::ChangeItem> &items)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def updateRenderItem(*__, **_) -> Never:
    """
    Qt's 'void Bars3DRenderer::updateRenderItem(const QBarDataItem &dataItem,
    BarRenderItem &renderItem)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Bars3DRenderer.updateRenderItem' has no cute function yet. Qt's "
        "'void Bars3DRenderer::updateRenderItem(const QBarDataItem "
        "&dataItem, BarRenderItem &renderItem)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def updateRenderRow(*__, **_) -> Never:
    """
    Qt's 'void Bars3DRenderer::updateRenderRow(const QBarDataRow *dataRow,
    BarRenderItemRow &renderRow)': names 'QBarDataRow', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'Bars3DRenderer.updateRenderRow' has no cute function yet. Qt's "
        "'void Bars3DRenderer::updateRenderRow(const QBarDataRow *dataRow, "
        "BarRenderItemRow &renderRow)': names 'QBarDataRow', which has no "
        "cute class yet.")

  @staticmethod
  def updateRows(*__, **_) -> Never:
    """
    Qt's 'void Bars3DRenderer::updateRows(const
    QList<Bars3DController::ChangeRow> &rows)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Bars3DRenderer.updateRows' has no cute function yet. Qt's 'void "
        "Bars3DRenderer::updateRows(const "
        "QList<Bars3DController::ChangeRow> &rows)': takes a type Python "
        "has no way to hand over yet.")
