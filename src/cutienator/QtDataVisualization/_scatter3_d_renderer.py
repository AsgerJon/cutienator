"""
Scatter3DRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/scatter3drenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Scatter3DRenderer to be private: it declares the class in a
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

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QVector3D
  from . import Q3DCamera, Q3DScene, QAbstract3DSeries, QScatter3DSeries
  from . import SeriesRenderCache
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DCamera = WAIT['Q3DCamera']
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QScatter3DSeries = WAIT['QtDataVisualization:QScatter3DSeries']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scatter3DRenderer(Abstract3DRenderer):
  """
  The cute side of Qt's Scatter3DRenderer: a plain Python object standing in
  front of one C++ Scatter3DRenderer.

  It is built on the cute 'Abstract3DRenderer', as Qt's Scatter3DRenderer is
  built on Qt's Abstract3DRenderer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Scatter3DRenderer that has a ritual and that Python
  can call so far, 33 names in all: 'metaObject', 'tr', 'updateData',
  'updateSeries', 'createNewCache', 'updateScene', 'updateAxisLabels',
  'updateAxisTitleVisibility', 'updateOptimizationHint', 'updateMargin',
  'convertPositionToTranslation', 'clickedIndex', 'resetClickedStatus',
  'render', 'updateSelectedItem', 'contextCleanup', 'initializeOpenGL',
  'initShaders', 'initGradientShaders', 'initStaticSelectedItemShaders',
  'updateShadowQuality', 'updateTextures', 'drawScene', 'drawLabels',
  'loadBackgroundMesh', 'initSelectionShader', 'initBackgroundShaders',
  'initStaticPointShaders', 'initSelectionBuffer', 'initDepthShader',
  'updateDepthBuffer', 'initPointShader', 'calculateSceneScalingFactors'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Scatter3DRenderer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Scatter3DRenderer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Scatter3DRenderer::~Scatter3DRenderer()': the destructor: Python
    never removes a C++ Scatter3DRenderer.
  - Qt's 'void Scatter3DRenderer::updateItems(const
    QList<Scatter3DController::ChangeItem> &items)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void Scatter3DRenderer::fixCameraTarget(QVector3D &target)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void Scatter3DRenderer::getVisibleItemBounds(QVector3D &minBounds,
    QVector3D &maxBounds)': takes a type Python has no way to hand over yet.
  - Qt's 'void Scatter3DRenderer::fixMeshFileName(QString &fileName,
    QAbstract3DSeries::Mesh mesh)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void Scatter3DRenderer::calculateTranslation(ScatterRenderItem
    &item)': takes a type Python has no way to hand over yet.
  - Qt's 'void Scatter3DRenderer::updateRenderItem(const QScatterDataItem
    &dataItem, ScatterRenderItem &renderItem)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  6 of the 48 functions Qt declares: 2 not a gap; 2 forbidden; 1 takes or
  gives a type that cannot be passed yet; 1 leans on 'Abstract3DRenderer.

  What to expect
  --------------

  - The C++ Scatter3DRenderer is created at the first use, not by
    'Scatter3DRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Scatter3DRenderer.
  - Qt tells when it has removed the C++ Scatter3DRenderer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Scatter3DRenderer that has no cute function yet,
    '__init__', 'calculateTranslation', 'selectionColorToSeriesAndIndex',
    'updateItems', 'updateRenderItem', holds a function that raises
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
    Calls Qt's 'QString Scatter3DRenderer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3drenderer.html#tr

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
    #  QString Scatter3DRenderer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17Scatter3DRenderer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Scatter3DRenderer'

  #  A C++ Scatter3DRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Scatter3DRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Scatter3DRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3drenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Scatter3DRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17Scatter3DRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def clickedIndex(self) -> int:
    """
    Calls Qt's 'int Scatter3DRenderer::clickedIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#clickedIndex
    """
    #  int Scatter3DRenderer::clickedIndex() const
    return self.uglySide.call(
        'ritual_ZNK17Scatter3DRenderer12clickedIndexEv',
    )

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
    Qt's 'Scatter3DRenderer::Scatter3DRenderer(Scatter3DController
    *controller)': leans on 'Abstract3DRenderer::needRender()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Scatter3DRenderer.__init__' has no cute function yet. Qt's "
        "'Scatter3DRenderer::Scatter3DRenderer(Scatter3DController "
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
    Calls Qt's 'void Scatter3DRenderer::updateData()'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3drenderer.html#updateData
    """
    #  void Scatter3DRenderer::updateData()
    ritual = 'ritual_ZN17Scatter3DRenderer10updateDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer10updateDataEv'
    self.uglySide.call(ritual)

  @overload(QList[QAbstract3DSeries])
  def updateSeries(self, seriesList: QList[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::updateSeries(const
    QList<QAbstract3DSeries *> &seriesList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#updateSeries

    Parameters
    ----------

    seriesList : QList[QAbstract3DSeries]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Scatter3DRenderer::updateSeries(const QList<QAbstract3DSeries *>
    #      &seriesList)
    self.uglySide.call(
        'ritual_ZN17Scatter3DRenderer12updateSeriesERK5QListIP17QAbstract3D'
        'SeriesE',
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
    *Scatter3DRenderer::createNewCache(QAbstract3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#createNewCache

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
    #  SeriesRenderCache *Scatter3DRenderer::createNewCache(QAbstract3DSeries
    #      *series)
    ritual = (
        'ritual_ZN17Scatter3DRenderer14createNewCacheEP17QAbstract3DSeries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Scatter3DRenderer14createNewCacheEP17QAbstract3DS'
          'eries')
    address = self.uglySide.call(ritual, self._addressOf(series))
    from . import SeriesRenderCache
    return SeriesRenderCache._cuteAt(address)

  @overload(Q3DScene)
  @overload(NoneType)
  def updateScene(self, scene: Optional[Q3DScene]) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::updateScene(Q3DScene *scene)'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3drenderer.html#updateScene

    Parameters
    ----------

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scatter3DRenderer::updateScene(Q3DScene *scene)
    ritual = 'ritual_ZN17Scatter3DRenderer11updateSceneEP8Q3DScene'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer11updateSceneEP8Q3DScene'
    self.uglySide.call(ritual, self._addressOf(scene))

  @overload(QAbstract3DAxis.AxisOrientation, QStringList)
  def updateAxisLabels(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      labels: QStringList,
  ) -> None:
    """
    Calls Qt's 'void
    Scatter3DRenderer::updateAxisLabels(QAbstract3DAxis::AxisOrientation
    orientation, const QStringList &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#updateAxisLabels

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Scatter3DRenderer::updateAxisLabels(QAbstract3DAxis::
    #      AxisOrientation orientation, const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN17Scatter3DRenderer16updateAxisLabelsEN15QAbstract3DAxis1'
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
    Scatter3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::
    AxisOrientation orientation, bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#updateAxisTitleVisibility

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    visible : bool
      Passed on as it is.
    """
    #  void Scatter3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::
    #      AxisOrientation orientation, bool visible)
    ritual = (
        'ritual_ZN17Scatter3DRenderer25updateAxisTitleVisibilityEN15QAbstra'
        'ct3DAxis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Scatter3DRenderer25updateAxisTitleVisibilityEN15Q'
          'Abstract3DAxis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, visible)

  @overload(QAbstract3DGraph.OptimizationHints)
  def updateOptimizationHint(
      self,
      hint: QAbstract3DGraph.OptimizationHints,
  ) -> None:
    """
    Calls Qt's 'void
    Scatter3DRenderer::updateOptimizationHint(QAbstract3DGraph::
    OptimizationHints hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#updateOptimizationHint

    Parameters
    ----------

    hint : QAbstract3DGraph.OptimizationHints
      Passed on as its number.
    """
    #  void Scatter3DRenderer::updateOptimizationHint(QAbstract3DGraph::
    #      OptimizationHints hint)
    ritual = (
        'ritual_ZN17Scatter3DRenderer22updateOptimizationHintE6QFlagsIN16QA'
        'bstract3DGraph16OptimizationHintEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Scatter3DRenderer22updateOptimizationHintE6QFlags'
          'IN16QAbstract3DGraph16OptimizationHintEE')
    self.uglySide.call(ritual, hint.value)

  @overload(float)
  def updateMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::updateMargin(float margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#updateMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Scatter3DRenderer::updateMargin(float margin)
    ritual = 'ritual_ZN17Scatter3DRenderer12updateMarginEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer12updateMarginEf'
    self.uglySide.call(ritual, margin)

  @overload(QVector3D, bool)
  def convertPositionToTranslation(
      self,
      position: QVector3D,
      isAbsolute: bool,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Scatter3DRenderer::convertPositionToTranslation(const QVector3D
    &position, bool isAbsolute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html

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
    #  QVector3D Scatter3DRenderer::convertPositionToTranslation(const
    #      QVector3D &position, bool isAbsolute)
    ritual = (
        'ritual_ZN17Scatter3DRenderer28convertPositionToTranslationERK9QVec'
        'tor3Db')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Scatter3DRenderer28convertPositionToTranslationER'
          'K9QVector3Db')
    address = self.uglySide.call(ritual, self._valueOf(position), isAbsolute)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def resetClickedStatus(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::resetClickedStatus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#resetClickedStatus
    """
    #  void Scatter3DRenderer::resetClickedStatus()
    self.uglySide.call('ritual_ZN17Scatter3DRenderer18resetClickedStatusEv')

  @overload(int)
  def render(self, defaultFboHandle: int) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::render(GLuint defaultFboHandle)'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3drenderer.html#render

    Parameters
    ----------

    defaultFboHandle : int
      Passed on as it is.
    """
    #  void Scatter3DRenderer::render(GLuint defaultFboHandle)
    ritual = 'ritual_ZN17Scatter3DRenderer6renderEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer6renderEj'
    self.uglySide.call(ritual, defaultFboHandle)

  @overload(int, QScatter3DSeries)
  @overload(int, NoneType)
  def updateSelectedItem(
      self,
      index: int,
      series: Optional[QScatter3DSeries],
  ) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::updateSelectedItem(int index,
    QScatter3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#updateSelectedItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scatter3DRenderer::updateSelectedItem(int index, QScatter3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN17Scatter3DRenderer18updateSelectedItemEiP16QScatter3DSer'
        'ies',
        index, self._addressOf(series),
    )

  def contextCleanup(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::contextCleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#contextCleanup
    """
    #  void Scatter3DRenderer::contextCleanup()
    ritual = 'ritual_ZN17Scatter3DRenderer14contextCleanupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer14contextCleanupEv'
    self.uglySide.call(ritual)

  def initializeOpenGL(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::initializeOpenGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#initializeOpenGL
    """
    #  void Scatter3DRenderer::initializeOpenGL()
    ritual = 'ritual_ZN17Scatter3DRenderer16initializeOpenGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer16initializeOpenGLEv'
    self.uglySide.call(ritual)

  @overload(str, str)
  def initShaders(self, vertexShader: str, fragmentShader: str) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::initShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3drenderer.html#initShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Scatter3DRenderer::initShaders(const QString &vertexShader, const
    #      QString &fragmentShader)
    ritual = 'ritual_ZN17Scatter3DRenderer11initShadersERK7QStringS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer11initShadersERK7QStringS2_'
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  @overload(str, str)
  def initGradientShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::initGradientShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#initGradientShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Scatter3DRenderer::initGradientShaders(const QString
    #      &vertexShader, const QString &fragmentShader)
    ritual = (
        'ritual_ZN17Scatter3DRenderer19initGradientShadersERK7QStringS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Scatter3DRenderer19initGradientShadersERK7QString'
          'S2_')
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
    Calls Qt's 'void Scatter3DRenderer::initStaticSelectedItemShaders(const
    QString &vertexShader, const QString &fragmentShader, const QString
    &gradientVertexShader, const QString &gradientFragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html

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
    #  void Scatter3DRenderer::initStaticSelectedItemShaders(const QString
    #      &vertexShader, const QString &fragmentShader, const QString
    #      &gradientVertexShader, const QString &gradientFragmentShader)
    ritual = (
        'ritual_ZN17Scatter3DRenderer29initStaticSelectedItemShadersERK7QSt'
        'ringS2_S2_S2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Scatter3DRenderer29initStaticSelectedItemShadersE'
          'RK7QStringS2_S2_S2_')
    self.uglySide.call(
        ritual,
        vertexShader, fragmentShader, gradientVertexShader,
        gradientFragmentShader,
    )

  @overload(QAbstract3DGraph.ShadowQuality)
  def updateShadowQuality(
      self,
      quality: QAbstract3DGraph.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    Scatter3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#updateShadowQuality

    Parameters
    ----------

    quality : QAbstract3DGraph.ShadowQuality
      Passed on as its number.
    """
    #  void Scatter3DRenderer::updateShadowQuality(QAbstract3DGraph::
    #      ShadowQuality quality)
    ritual = (
        'ritual_ZN17Scatter3DRenderer19updateShadowQualityEN16QAbstract3DGr'
        'aph13ShadowQualityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Scatter3DRenderer19updateShadowQualityEN16QAbstra'
          'ct3DGraph13ShadowQualityE')
    self.uglySide.call(ritual, quality.value)

  def updateTextures(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::updateTextures()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#updateTextures
    """
    #  void Scatter3DRenderer::updateTextures()
    ritual = 'ritual_ZN17Scatter3DRenderer14updateTexturesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer14updateTexturesEv'
    self.uglySide.call(ritual)

  @overload(int)
  def drawScene(self, defaultFboHandle: int) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::drawScene(GLuint defaultFboHandle)'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3drenderer.html#drawScene

    Parameters
    ----------

    defaultFboHandle : int
      Passed on as it is.
    """
    #  void Scatter3DRenderer::drawScene(GLuint defaultFboHandle)
    self.uglySide.call(
        'ritual_ZN17Scatter3DRenderer9drawSceneEj', defaultFboHandle,
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
    Calls Qt's 'void Scatter3DRenderer::drawLabels(bool drawSelection, const
    Q3DCamera *activeCamera, const QMatrix4x4 &viewMatrix, const QMatrix4x4
    &projectionMatrix)'.

    Qt's own words: https://doc.qt.io/qt-6/scatter3drenderer.html#drawLabels

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
    #  void Scatter3DRenderer::drawLabels(bool drawSelection, const Q3DCamera
    #      *activeCamera, const QMatrix4x4 &viewMatrix, const QMatrix4x4
    #      &projectionMatrix)
    self.uglySide.call(
        'ritual_ZN17Scatter3DRenderer10drawLabelsEbPK9Q3DCameraRK10QMatrix4'
        'x4S5_',
        drawSelection, self._addressOf(activeCamera),
        self._valueOf(viewMatrix), self._valueOf(projectionMatrix),
    )

  def loadBackgroundMesh(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::loadBackgroundMesh()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#loadBackgroundMesh
    """
    #  void Scatter3DRenderer::loadBackgroundMesh()
    self.uglySide.call('ritual_ZN17Scatter3DRenderer18loadBackgroundMeshEv')

  def initSelectionShader(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::initSelectionShader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#initSelectionShader
    """
    #  void Scatter3DRenderer::initSelectionShader()
    self.uglySide.call('ritual_ZN17Scatter3DRenderer19initSelectionShaderEv')

  @overload(str, str)
  def initBackgroundShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::initBackgroundShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#initBackgroundShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Scatter3DRenderer::initBackgroundShaders(const QString
    #      &vertexShader, const QString &fragmentShader)
    ritual = (
        'ritual_ZN17Scatter3DRenderer21initBackgroundShadersERK7QStringS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Scatter3DRenderer21initBackgroundShadersERK7QStri'
          'ngS2_')
    self.uglySide.call(ritual, vertexShader, fragmentShader)

  @overload(str, str)
  def initStaticPointShaders(
      self,
      vertexShader: str,
      fragmentShader: str,
  ) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::initStaticPointShaders(const QString
    &vertexShader, const QString &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#initStaticPointShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Scatter3DRenderer::initStaticPointShaders(const QString
    #      &vertexShader, const QString &fragmentShader)
    self.uglySide.call(
        'ritual_ZN17Scatter3DRenderer22initStaticPointShadersERK7QStringS2_',
        vertexShader, fragmentShader,
    )

  def initSelectionBuffer(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::initSelectionBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#initSelectionBuffer
    """
    #  void Scatter3DRenderer::initSelectionBuffer()
    ritual = 'ritual_ZN17Scatter3DRenderer19initSelectionBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer19initSelectionBufferEv'
    self.uglySide.call(ritual)

  def initDepthShader(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::initDepthShader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#initDepthShader
    """
    #  void Scatter3DRenderer::initDepthShader()
    self.uglySide.call('ritual_ZN17Scatter3DRenderer15initDepthShaderEv')

  def updateDepthBuffer(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::updateDepthBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#updateDepthBuffer
    """
    #  void Scatter3DRenderer::updateDepthBuffer()
    ritual = 'ritual_ZN17Scatter3DRenderer17updateDepthBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Scatter3DRenderer17updateDepthBufferEv'
    self.uglySide.call(ritual)

  def initPointShader(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::initPointShader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html#initPointShader
    """
    #  void Scatter3DRenderer::initPointShader()
    self.uglySide.call('ritual_ZN17Scatter3DRenderer15initPointShaderEv')

  def calculateSceneScalingFactors(self) -> None:
    """
    Calls Qt's 'void Scatter3DRenderer::calculateSceneScalingFactors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatter3drenderer.html
    """
    #  void Scatter3DRenderer::calculateSceneScalingFactors()
    self.uglySide.call(
        'ritual_ZN17Scatter3DRenderer28calculateSceneScalingFactorsEv',
    )

  @staticmethod
  def calculateTranslation(*__, **_) -> Never:
    """
    Qt's 'void Scatter3DRenderer::calculateTranslation(ScatterRenderItem
    &item)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Scatter3DRenderer.calculateTranslation' has no cute function yet. "
        "Qt's 'void "
        "Scatter3DRenderer::calculateTranslation(ScatterRenderItem &item)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def selectionColorToSeriesAndIndex(*__, **_) -> Never:
    """
    Qt's 'void Scatter3DRenderer::selectionColorToSeriesAndIndex(const
    QVector4D &color, int &index, QAbstract3DSeries *&series)': takes or
    gives a type that cannot be passed yet: QAbstract3DSeries *&.
    """
    raise NotImplementedError(
        "'Scatter3DRenderer.selectionColorToSeriesAndIndex' has no cute "
        "function yet. Qt's 'void "
        "Scatter3DRenderer::selectionColorToSeriesAndIndex(const QVector4D "
        "&color, int &index, QAbstract3DSeries *&series)': takes or gives a "
        "type that cannot be passed yet: QAbstract3DSeries *&.")

  @staticmethod
  def updateItems(*__, **_) -> Never:
    """
    Qt's 'void Scatter3DRenderer::updateItems(const
    QList<Scatter3DController::ChangeItem> &items)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'Scatter3DRenderer.updateItems' has no cute function yet. Qt's "
        "'void Scatter3DRenderer::updateItems(const "
        "QList<Scatter3DController::ChangeItem> &items)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def updateRenderItem(*__, **_) -> Never:
    """
    Qt's 'void Scatter3DRenderer::updateRenderItem(const QScatterDataItem
    &dataItem, ScatterRenderItem &renderItem)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Scatter3DRenderer.updateRenderItem' has no cute function yet. "
        "Qt's 'void Scatter3DRenderer::updateRenderItem(const "
        "QScatterDataItem &dataItem, ScatterRenderItem &renderItem)': takes "
        "a type Python has no way to hand over yet.")
