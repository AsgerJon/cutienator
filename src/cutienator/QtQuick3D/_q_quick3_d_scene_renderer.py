"""
QQuick3DSceneRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DSceneRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from ..QtQuick3DRuntimeRender import QSSGRenderNode
  from . import QQuick3DRenderStats, QQuick3DViewport
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DViewport = WAIT['QQuick3DViewport']
  QRect = WAIT['QRect']
  QSSGRenderNode = WAIT['QSSGRenderNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DSceneRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DSceneRenderer: a plain Python object standing
  in front of one C++ QQuick3DSceneRenderer.

  C++ hands a QQuick3DSceneRenderer around as a copy, so every C++
  QQuick3DSceneRenderer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuick3DSceneRenderer that has a ritual and that
  Python can call so far, 13 names in all: 'beginFrame', 'endFrame',
  'rhiPrepare', 'rhiRender', 'invalidateFramebufferObject', 'surfaceSize',
  'releaseCachedResources', 'setGlobalPickingEnabled', 'renderStats',
  'releaseAaDependentRhiResources', 'addNodeToLayer', 'removeNodeFromLayer',
  'maybeSetupLightmapBaking'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DSceneRenderer::QQuick3DSceneRenderer(const
    std::shared_ptr<QSSGRenderContextInterface> &rci)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QQuick3DSceneRenderer::~QQuick3DSceneRenderer()': the destructor:
    Python removes its C++ QQuick3DSceneRenderer by it, and has no other use
    for it.
  - Qt's 'QSSGRenderLayer::TonemapMode
    QQuick3DSceneRenderer::getTonemapMode(const QQuick3DSceneEnvironment
    &environment)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<QSSGRenderRay>
    QQuick3DSceneRenderer::getRayFromViewportPos(const QPointF &pos)': gives
    a type Python has no way to take yet.
  - Qt's 'PickResultList QQuick3DSceneRenderer::syncPick(const QSSGRenderRay
    &ray)': gives a type Python has no way to take yet.
  - Qt's 'PickResultList QQuick3DSceneRenderer::syncPickOne(const
    QSSGRenderRay &ray, QSSGRenderNode *node)': gives a type Python has no
    way to take yet.
  - Qt's 'PickResultList QQuick3DSceneRenderer::syncPickSubset(const
    QSSGRenderRay &ray, QVarLengthArray<QSSGRenderNode *> subset)': takes a
    type Python has no way to hand over yet.
  - Qt's 'PickResultList QQuick3DSceneRenderer::syncPickAll(const
    QSSGRenderRay &ray)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<QSSGRenderPickResult>
    QQuick3DSceneRenderer::syncPickClosestPoint(const QVector3D &center,
    float radiusSquared, QSSGRenderNode *node)': gives a type Python has no
    way to take yet.
  - Qt's 'QList<const QSSGRenderNode *>
    QQuick3DSceneRenderer::syncPickInFrustum(const QSSGFrustum &frustum)':
    gives a type Python has no way to take yet.
  - Qt's 'void QQuick3DSceneRenderer::updateLayerNode(QSSGRenderLayer
    &layerNode, const QQuick3DViewport &view3D, const
    QList<QSSGRenderGraphObject *> &resourceLoaders)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuick3DSceneRenderer is created at the first use, not by
    'QQuick3DSceneRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DSceneRenderer back gives a copy the ritual
    made for Python, in a new cute QQuick3DSceneRenderer.
  - Each name of Qt's QQuick3DSceneRenderer that has no cute function yet,
    '__init__', 'getRayFromViewportPos', 'getTonemapMode',
    'renderToRhiTexture', 'syncPick', 'syncPickAll', 'syncPickClosestPoint',
    'syncPickInFrustum', 'syncPickOne', 'syncPickSubset', 'synchronize',
    'updateLayerNode', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DSceneRenderer'

  #  Qt's '~QQuick3DSceneRenderer()'. Naming it makes this a value class:
  #  Python owns every C++ QQuick3DSceneRenderer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQuick3DSceneRendererD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def surfaceSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuick3DSceneRenderer::surfaceSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#surfaceSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuick3DSceneRenderer::surfaceSize() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DSceneRenderer11surfaceSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setGlobalPickingEnabled(self, isEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSceneRenderer::setGlobalPickingEnabled(bool
    isEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#setGlobalPickingEnabled

    Parameters
    ----------

    isEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSceneRenderer::setGlobalPickingEnabled(bool isEnabled)
    self.uglySide.call(
        'ritual_ZN21QQuick3DSceneRenderer23setGlobalPickingEnabledEb',
        isEnabled,
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
    Qt's 'QQuick3DSceneRenderer::QQuick3DSceneRenderer(const
    std::shared_ptr<QSSGRenderContextInterface> &rci)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.__init__' has no cute function yet. Qt's "
        "'QQuick3DSceneRenderer::QQuick3DSceneRenderer(const "
        "std::shared_ptr<QSSGRenderContextInterface> &rci)': takes a type "
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

  def beginFrame(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneRenderer::beginFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#beginFrame
    """
    #  void QQuick3DSceneRenderer::beginFrame()
    self.uglySide.call('ritual_ZN21QQuick3DSceneRenderer10beginFrameEv')

  def endFrame(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneRenderer::endFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#endFrame
    """
    #  void QQuick3DSceneRenderer::endFrame()
    self.uglySide.call('ritual_ZN21QQuick3DSceneRenderer8endFrameEv')

  @overload(QRect, float)
  def rhiPrepare(self, viewport: QRect, displayPixelRatio: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneRenderer::rhiPrepare(const QRect &viewport,
    qreal displayPixelRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#rhiPrepare

    Parameters
    ----------

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    displayPixelRatio : float
      Passed on as it is.
    """
    #  void QQuick3DSceneRenderer::rhiPrepare(const QRect &viewport, qreal
    #      displayPixelRatio)
    self.uglySide.call(
        'ritual_ZN21QQuick3DSceneRenderer10rhiPrepareERK5QRectd',
        self._valueOf(viewport), displayPixelRatio,
    )

  def rhiRender(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneRenderer::rhiRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#rhiRender
    """
    #  void QQuick3DSceneRenderer::rhiRender()
    self.uglySide.call('ritual_ZN21QQuick3DSceneRenderer9rhiRenderEv')

  def invalidateFramebufferObject(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneRenderer::invalidateFramebufferObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html
    """
    #  void QQuick3DSceneRenderer::invalidateFramebufferObject()
    self.uglySide.call(
        'ritual_ZN21QQuick3DSceneRenderer27invalidateFramebufferObjectEv',
    )

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneRenderer::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#releaseCachedResources
    """
    #  void QQuick3DSceneRenderer::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN21QQuick3DSceneRenderer22releaseCachedResourcesEv',
    )

  def renderStats(self) -> Optional[QQuick3DRenderStats]:
    """
    Calls Qt's 'QQuick3DRenderStats *QQuick3DSceneRenderer::renderStats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#renderStats

    Returns
    -------

    Optional[QQuick3DRenderStats]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRenderStats *QQuick3DSceneRenderer::renderStats()
    address = self.uglySide.call(
        'ritual_ZN21QQuick3DSceneRenderer11renderStatsEv',
    )
    from . import QQuick3DRenderStats
    return QQuick3DRenderStats._cuteAt(address)

  def releaseAaDependentRhiResources(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneRenderer::releaseAaDependentRhiResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html
    """
    #  void QQuick3DSceneRenderer::releaseAaDependentRhiResources()
    self.uglySide.call(
        'ritual_ZN21QQuick3DSceneRenderer30releaseAaDependentRhiResourcesEv',
    )

  @overload(QSSGRenderNode)
  @overload(NoneType)
  def addNodeToLayer(self, node: Optional[QSSGRenderNode]) -> None:
    """
    Calls Qt's 'void QQuick3DSceneRenderer::addNodeToLayer(QSSGRenderNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#addNodeToLayer

    Parameters
    ----------

    node : Optional[QSSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneRenderer::addNodeToLayer(QSSGRenderNode *node)
    self.uglySide.call(
        'ritual_ZN21QQuick3DSceneRenderer14addNodeToLayerEP14QSSGRenderNode',
        self._addressOf(node),
    )

  @overload(QSSGRenderNode)
  @overload(NoneType)
  def removeNodeFromLayer(self, node: Optional[QSSGRenderNode]) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneRenderer::removeNodeFromLayer(QSSGRenderNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html#removeNodeFromLayer

    Parameters
    ----------

    node : Optional[QSSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneRenderer::removeNodeFromLayer(QSSGRenderNode *node)
    self.uglySide.call(
        'ritual_ZN21QQuick3DSceneRenderer19removeNodeFromLayerEP14QSSGRende'
        'rNode',
        self._addressOf(node),
    )

  @overload(QQuick3DViewport)
  @overload(NoneType)
  def maybeSetupLightmapBaking(
      self,
      view3D: Optional[QQuick3DViewport],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneRenderer::maybeSetupLightmapBaking(QQuick3DViewport
    *view3D)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenerenderer.html

    Parameters
    ----------

    view3D : Optional[QQuick3DViewport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneRenderer::maybeSetupLightmapBaking(QQuick3DViewport
    #      *view3D)
    self.uglySide.call(
        'ritual_ZN21QQuick3DSceneRenderer24maybeSetupLightmapBakingEP16QQui'
        'ck3DViewport',
        self._addressOf(view3D),
    )

  @staticmethod
  def getRayFromViewportPos(*__, **_) -> Never:
    """
    Qt's 'std::optional<QSSGRenderRay>
    QQuick3DSceneRenderer::getRayFromViewportPos(const QPointF &pos)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.getRayFromViewportPos' has no cute function "
        "yet. Qt's 'std::optional<QSSGRenderRay> "
        "QQuick3DSceneRenderer::getRayFromViewportPos(const QPointF &pos)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def getTonemapMode(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderLayer::TonemapMode
    QQuick3DSceneRenderer::getTonemapMode(const QQuick3DSceneEnvironment
    &environment)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.getTonemapMode' has no cute function yet. "
        "Qt's 'QSSGRenderLayer::TonemapMode "
        "QQuick3DSceneRenderer::getTonemapMode(const "
        "QQuick3DSceneEnvironment &environment)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def renderToRhiTexture(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture *QQuick3DSceneRenderer::renderToRhiTexture(QQuickWindow
    *qw)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'QSSG_prepareFrame_entry'.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.renderToRhiTexture' has no cute function "
        "yet. Qt's 'QRhiTexture "
        "*QQuick3DSceneRenderer::renderToRhiTexture(QQuickWindow *qw)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QSSG_prepareFrame_entry'.")

  @staticmethod
  def syncPick(*__, **_) -> Never:
    """
    Qt's 'PickResultList QQuick3DSceneRenderer::syncPick(const QSSGRenderRay
    &ray)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.syncPick' has no cute function yet. Qt's "
        "'PickResultList QQuick3DSceneRenderer::syncPick(const "
        "QSSGRenderRay &ray)': gives a type Python has no way to take yet.")

  @staticmethod
  def syncPickAll(*__, **_) -> Never:
    """
    Qt's 'PickResultList QQuick3DSceneRenderer::syncPickAll(const
    QSSGRenderRay &ray)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.syncPickAll' has no cute function yet. Qt's "
        "'PickResultList QQuick3DSceneRenderer::syncPickAll(const "
        "QSSGRenderRay &ray)': gives a type Python has no way to take yet.")

  @staticmethod
  def syncPickClosestPoint(*__, **_) -> Never:
    """
    Qt's 'std::optional<QSSGRenderPickResult>
    QQuick3DSceneRenderer::syncPickClosestPoint(const QVector3D &center,
    float radiusSquared, QSSGRenderNode *node)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.syncPickClosestPoint' has no cute function "
        "yet. Qt's 'std::optional<QSSGRenderPickResult> "
        "QQuick3DSceneRenderer::syncPickClosestPoint(const QVector3D "
        "&center, float radiusSquared, QSSGRenderNode *node)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def syncPickInFrustum(*__, **_) -> Never:
    """
    Qt's 'QList<const QSSGRenderNode *>
    QQuick3DSceneRenderer::syncPickInFrustum(const QSSGFrustum &frustum)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.syncPickInFrustum' has no cute function "
        "yet. Qt's 'QList<const QSSGRenderNode *> "
        "QQuick3DSceneRenderer::syncPickInFrustum(const QSSGFrustum "
        "&frustum)': gives a type Python has no way to take yet.")

  @staticmethod
  def syncPickOne(*__, **_) -> Never:
    """
    Qt's 'PickResultList QQuick3DSceneRenderer::syncPickOne(const
    QSSGRenderRay &ray, QSSGRenderNode *node)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.syncPickOne' has no cute function yet. Qt's "
        "'PickResultList QQuick3DSceneRenderer::syncPickOne(const "
        "QSSGRenderRay &ray, QSSGRenderNode *node)': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def syncPickSubset(*__, **_) -> Never:
    """
    Qt's 'PickResultList QQuick3DSceneRenderer::syncPickSubset(const
    QSSGRenderRay &ray, QVarLengthArray<QSSGRenderNode *> subset)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.syncPickSubset' has no cute function yet. "
        "Qt's 'PickResultList QQuick3DSceneRenderer::syncPickSubset(const "
        "QSSGRenderRay &ray, QVarLengthArray<QSSGRenderNode *> subset)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def synchronize(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSceneRenderer::synchronize(QQuick3DViewport *view3D,
    const QSize &size, float dpr)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QSSG_synchronize'; did you mean 'synchronize'?.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.synchronize' has no cute function yet. Qt's "
        "'void QQuick3DSceneRenderer::synchronize(QQuick3DViewport *view3D, "
        "const QSize &size, float dpr)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'QSSG_synchronize'; did you mean "
        "'synchronize'?.")

  @staticmethod
  def updateLayerNode(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSceneRenderer::updateLayerNode(QSSGRenderLayer
    &layerNode, const QQuick3DViewport &view3D, const
    QList<QSSGRenderGraphObject *> &resourceLoaders)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneRenderer.updateLayerNode' has no cute function yet. "
        "Qt's 'void QQuick3DSceneRenderer::updateLayerNode(QSSGRenderLayer "
        "&layerNode, const QQuick3DViewport &view3D, const "
        "QList<QSSGRenderGraphObject *> &resourceLoaders)': takes a type "
        "Python has no way to hand over yet.")
