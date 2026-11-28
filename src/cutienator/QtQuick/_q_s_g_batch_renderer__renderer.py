"""
QSGBatchRenderer::Renderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::Renderer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGBatchRenderer, QSGNode, QSGRenderer, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from ..QtGui import QRhiCommandBuffer, QRhiGraphicsPipeline, QRhiTexture
  from . import QSGClipNode, QSGDefaultRenderContext, QSGGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QSGClipNode = WAIT['QSGClipNode']
  QSGDefaultRenderContext = WAIT['QSGDefaultRenderContext']
  QSGGeometry = WAIT['QSGGeometry']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Renderer(QSGRenderer):
  """
  The cute side of Qt's QSGBatchRenderer::Renderer: a plain Python object
  standing in front of one C++ QSGBatchRenderer::Renderer.

  It is built on the cute 'QSGRenderer', as Qt's QSGBatchRenderer::Renderer
  is built on Qt's QSGRenderer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::Renderer that has a ritual and
  that Python can call so far, 43 names in all: 'nodeChanged', 'render',
  'prepareInline', 'renderInline', 'releaseCachedResources',
  'destroyGraphicsResources', 'map', 'unmap', 'buildRenderListsFromScratch',
  'buildRenderListsForTaggedRoots', 'tagSubRoots', 'buildRenderLists',
  'deleteRemovedElements', 'prepareOpaqueBatches', 'checkOverlap',
  'prepareAlphaBatches', 'invalidateBatchAndOverlappingRenderOrders',
  'uploadBatch', 'dummyTexture', 'checkLineWidth', 'setViewportAndScissors',
  'setGraphicsPipeline', 'applyClipStateToGraphicsState',
  'buildStencilPipeline', 'updateClipState', 'enqueueStencilDraw',
  'renderRhiRenderNode', 'changeBatchRoot', 'registerBatchRoot',
  'removeBatchRootFromParent', 'nodeChangedBatchRoot',
  'turnNodeIntoBatchRoot', 'nodeWasRemoved', 'nodeWasAdded', 'batchRootInfo',
  'newBatch', 'invalidateAndRecycleBatch', 'releaseElement',
  'setVisualizationMode', 'hasVisualizationModeWithContinuousUpdate',
  'mergedIndexElemSize', 'useDepthBuffer', 'setStateForDepthPostPass'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGBatchRenderer::Renderer::~Renderer()': the destructor: Python
    never removes a C++ QSGBatchRenderer::Renderer.
  - Qt's 'void
    QSGBatchRenderer::Renderer::prepareRenderPass(RenderPassContext *ctx)':
    names 'QSGBatchRenderer::Renderer::RenderPassContext', which has no cute
    class yet.
  - Qt's 'void QSGBatchRenderer::Renderer::beginRenderPass(RenderPassContext
    *ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', which has
    no cute class yet.
  - Qt's 'void QSGBatchRenderer::Renderer::recordRenderPass(RenderPassContext
    *ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', which has
    no cute class yet.
  - Qt's 'void QSGBatchRenderer::Renderer::endRenderPass(RenderPassContext
    *ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', which has
    no cute class yet.
  - Qt's 'void QSGBatchRenderer::Renderer::cleanupBatches(QDataBuffer<Batch
    *> *batches)': names 'QDataBuffer<QSGBatchRenderer::Batch *>', which has
    no cute class yet.
  - Qt's 'void QSGBatchRenderer::Renderer::uploadMergedElement(Element *e,
    int vaOffset, char **vertexData, char **zData, char **indexData, void
    *iBasePtr, int *indexCount)': takes a type Python has no way to hand over
    yet.
  - Qt's 'bool QSGBatchRenderer::Renderer::ensurePipelineState(Element *e,
    const ShaderManager::Shader *sms, bool depthPostPass)': names
    'QSGBatchRenderer::ShaderManager::Shader', which has no cute class yet.
  - Qt's 'void
    QSGBatchRenderer::Renderer::updateMaterialDynamicData(ShaderManager::
    Shader *sms, QSGMaterialShader::RenderState &renderState, QSGMaterial
    *material, const Batch *batch, Element *e, int ubufOffset, char
    *directUpdatePtr)': names 'QSGBatchRenderer::ShaderManager::Shader',
    which has no cute class yet.
  - Qt's 'void
    QSGBatchRenderer::Renderer::updateMaterialStaticData(ShaderManager::
    Shader *sms, QSGMaterialShader::RenderState &renderState, QSGMaterial
    *material, Batch *batch, bool *gstateChanged)': names
    'QSGBatchRenderer::ShaderManager::Shader', which has no cute class yet.
  - Qt's 'bool QSGBatchRenderer::Renderer::prepareRenderMergedBatch(Batch
    *batch, PreparedRenderBatch *renderBatch)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
  - Qt's 'void
    QSGBatchRenderer::Renderer::renderMergedBatch(PreparedRenderBatch
    *renderBatch, bool depthPostPass)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
  - Qt's 'bool QSGBatchRenderer::Renderer::prepareRenderUnmergedBatch(Batch
    *batch, PreparedRenderBatch *renderBatch)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
  - Qt's 'void
    QSGBatchRenderer::Renderer::renderUnmergedBatch(PreparedRenderBatch
    *renderBatch, bool depthPostPass)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
  - Qt's 'bool QSGBatchRenderer::Renderer::prepareRhiRenderNode(Batch *batch,
    PreparedRenderBatch *renderBatch)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
  - Qt's 'void
    QSGBatchRenderer::Renderer::setActiveRhiShader(QSGMaterialShader
    *program, ShaderManager::Shader *shader)': names
    'QSGBatchRenderer::ShaderManager::Shader', which has no cute class yet.
  - Qt's 'void QSGBatchRenderer::Renderer::nodeWasTransformed(Node *node, int
    *vertexCount)': takes a number to change where it is.

  What has no ritual
  ------------------

  6 of the 67 functions Qt declares: 6 not a gap.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::Renderer is created at the first use, not by
    'QSGBatchRenderer::Renderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGBatchRenderer::Renderer.
  - Qt tells when it has removed the C++ QSGBatchRenderer::Renderer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGBatchRenderer::Renderer that has no cute function
    yet, 'beginRenderPass', 'cleanupBatches', 'endRenderPass',
    'ensurePipelineState', 'nodeWasTransformed', 'prepareRenderMergedBatch',
    'prepareRenderPass', 'prepareRenderUnmergedBatch',
    'prepareRhiRenderNode', 'recordRenderPass', 'renderMergedBatch',
    'renderUnmergedBatch', 'setActiveRhiShader', 'updateMaterialDynamicData',
    'updateMaterialStaticData', 'uploadMergedElement', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::Renderer'

  #  A C++ QSGBatchRenderer::Renderer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGBatchRenderer_Renderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasVisualizationModeWithContinuousUpdate(self) -> bool:
    """
    Calls Qt's 'bool
    QSGBatchRenderer::Renderer::hasVisualizationModeWithContinuousUpdate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html
    """
    #  bool QSGBatchRenderer::Renderer::
    #      hasVisualizationModeWithContinuousUpdate() const
    ritual = (
        'ritual_ZNK16QSGBatchRenderer8Renderer40hasVisualizationModeWithCon'
        'tinuousUpdateEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QSGBatchRenderer8Renderer40hasVisualizationModeW'
          'ithContinuousUpdateEv')
    return self.uglySide.call(ritual)

  def mergedIndexElemSize(self) -> int:
    """
    Calls Qt's 'int QSGBatchRenderer::Renderer::mergedIndexElemSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#mergedIndexElemSize
    """
    #  int QSGBatchRenderer::Renderer::mergedIndexElemSize() const
    return self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer8Renderer19mergedIndexElemSizeEv',
    )

  def useDepthBuffer(self) -> bool:
    """
    Calls Qt's 'bool QSGBatchRenderer::Renderer::useDepthBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#useDepthBuffer
    """
    #  bool QSGBatchRenderer::Renderer::useDepthBuffer() const
    return self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer8Renderer14useDepthBufferEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiCommandBuffer, WAIT['QSGBatchRenderer.Batch'])
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, WAIT['QSGBatchRenderer.Batch'])
  @overload(NoneType, NoneType)
  def setViewportAndScissors(
      self,
      cb: Optional[QRhiCommandBuffer],
      batch: Optional[QSGBatchRenderer.Batch],
  ) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::Renderer::setViewportAndScissors(QRhiCommandBuffer *cb,
    const Batch *batch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    batch : Optional[QSGBatchRenderer.Batch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::setViewportAndScissors(
    #      QRhiCommandBuffer *cb, const Batch *batch)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer22setViewportAndScissorsEP17QR'
        'hiCommandBufferPKNS_5BatchE',
        self._addressOf(cb), self._addressOf(batch),
    )

  @overload(
      QRhiCommandBuffer, WAIT['QSGBatchRenderer.Batch'],
      WAIT['QSGBatchRenderer.Element'],
  )
  @overload(QRhiCommandBuffer, WAIT['QSGBatchRenderer.Batch'], NoneType)
  @overload(QRhiCommandBuffer, NoneType, WAIT['QSGBatchRenderer.Element'])
  @overload(QRhiCommandBuffer, NoneType, NoneType)
  @overload(
      NoneType, WAIT['QSGBatchRenderer.Batch'],
      WAIT['QSGBatchRenderer.Element'],
  )
  @overload(NoneType, WAIT['QSGBatchRenderer.Batch'], NoneType)
  @overload(NoneType, NoneType, WAIT['QSGBatchRenderer.Element'])
  @overload(NoneType, NoneType, NoneType)
  @overload(
      QRhiCommandBuffer, WAIT['QSGBatchRenderer.Batch'],
      WAIT['QSGBatchRenderer.Element'], bool,
  )
  @overload(
      QRhiCommandBuffer, WAIT['QSGBatchRenderer.Batch'], NoneType, bool,
  )
  @overload(
      QRhiCommandBuffer, NoneType, WAIT['QSGBatchRenderer.Element'], bool,
  )
  @overload(QRhiCommandBuffer, NoneType, NoneType, bool)
  @overload(
      NoneType, WAIT['QSGBatchRenderer.Batch'],
      WAIT['QSGBatchRenderer.Element'], bool,
  )
  @overload(NoneType, WAIT['QSGBatchRenderer.Batch'], NoneType, bool)
  @overload(NoneType, NoneType, WAIT['QSGBatchRenderer.Element'], bool)
  @overload(NoneType, NoneType, NoneType, bool)
  def setGraphicsPipeline(
      self,
      cb: Optional[QRhiCommandBuffer],
      batch: Optional[QSGBatchRenderer.Batch],
      e: Optional[QSGBatchRenderer.Element],
      depthPostPass: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::Renderer::setGraphicsPipeline(QRhiCommandBuffer *cb,
    const Batch *batch, Element *e, bool depthPostPass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#setGraphicsPipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    batch : Optional[QSGBatchRenderer.Batch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QSGBatchRenderer.Element]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    depthPostPass : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSGBatchRenderer::Renderer::setGraphicsPipeline(QRhiCommandBuffer
    #      *cb, const Batch *batch, Element *e, bool depthPostPass)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer19setGraphicsPipelineEP17QRhiC'
        'ommandBufferPKNS_5BatchEPNS_7ElementEb',
        self._addressOf(cb), self._addressOf(batch), self._addressOf(e),
        depthPostPass,
    )

  @overload(QByteArray)
  def setVisualizationMode(self, mode: QByteArray) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::setVisualizationMode(const
    QByteArray &mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html

    Parameters
    ----------

    mode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSGBatchRenderer::Renderer::setVisualizationMode(const QByteArray
    #      &mode)
    ritual = (
        'ritual_ZN16QSGBatchRenderer8Renderer20setVisualizationModeERK10QBy'
        'teArray')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSGBatchRenderer8Renderer20setVisualizationModeER'
          'K10QByteArray')
    self.uglySide.call(ritual, self._valueOf(mode))

  def setStateForDepthPostPass(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::setStateForDepthPostPass()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html
    """
    #  void QSGBatchRenderer::Renderer::setStateForDepthPostPass()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer24setStateForDepthPostPassEv',
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

  @overload(QSGDefaultRenderContext)
  @overload(NoneType)
  @overload(QSGDefaultRenderContext, QSGRendererInterface.RenderMode)
  @overload(NoneType, QSGRendererInterface.RenderMode)
  def __init__(
      self,
      ctx: Optional[QSGDefaultRenderContext],
      renderMode: QSGRendererInterface.RenderMode = (
          QSGRendererInterface.RenderMode.RenderMode2D),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSGBatchRenderer::Renderer::Renderer(QSGDefaultRenderContext *ctx,
    QSGRendererInterface::RenderMode renderMode)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#Renderer

    Parameters
    ----------

    ctx : Optional[QSGDefaultRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    renderMode : QSGRendererInterface.RenderMode
      Passed on as its number. May be left out, as in Qt: it is then
      QSGRendererInterface.RenderMode.RenderMode2D.
    """
    #  QSGBatchRenderer::Renderer::Renderer(QSGDefaultRenderContext *ctx,
    #      QSGRendererInterface::RenderMode renderMode)
    self._noteCreation(Renderer, lambda: Rituals.call(
        'ritual_ZN16QSGBatchRenderer8RendererC1EP23QSGDefaultRenderContextN'
        '20QSGRendererInterface10RenderModeE',
        self._addressOf(ctx), renderMode.value,
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

  @overload(QSGNode, QSGNode.DirtyState)
  @overload(NoneType, QSGNode.DirtyState)
  def nodeChanged(
      self,
      node: Optional[QSGNode],
      state: QSGNode.DirtyState,
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::nodeChanged(QSGNode *node,
    QSGNode::DirtyState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#nodeChanged

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : QSGNode.DirtyState
      Passed on as its number.
    """
    #  void QSGBatchRenderer::Renderer::nodeChanged(QSGNode *node,
    #      QSGNode::DirtyState state)
    ritual = (
        'ritual_ZN16QSGBatchRenderer8Renderer11nodeChangedEP7QSGNode6QFlags'
        'INS1_13DirtyStateBitEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSGBatchRenderer8Renderer11nodeChangedEP7QSGNode6'
          'QFlagsINS1_13DirtyStateBitEE')
    self.uglySide.call(ritual, self._addressOf(node, 'QSGNode'), state.value)

  def render(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::render()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#render
    """
    #  void QSGBatchRenderer::Renderer::render()
    ritual = 'ritual_ZN16QSGBatchRenderer8Renderer6renderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGBatchRenderer8Renderer6renderEv'
    self.uglySide.call(ritual)

  def prepareInline(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::prepareInline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#prepareInline
    """
    #  void QSGBatchRenderer::Renderer::prepareInline()
    ritual = 'ritual_ZN16QSGBatchRenderer8Renderer13prepareInlineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGBatchRenderer8Renderer13prepareInlineEv'
    self.uglySide.call(ritual)

  def renderInline(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::renderInline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#renderInline
    """
    #  void QSGBatchRenderer::Renderer::renderInline()
    ritual = 'ritual_ZN16QSGBatchRenderer8Renderer12renderInlineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGBatchRenderer8Renderer12renderInlineEv'
    self.uglySide.call(ritual)

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html
    """
    #  void QSGBatchRenderer::Renderer::releaseCachedResources()
    ritual = 'ritual_ZN16QSGBatchRenderer8Renderer22releaseCachedResourcesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSGBatchRenderer8Renderer22releaseCachedResources'
          'Ev')
    self.uglySide.call(ritual)

  def destroyGraphicsResources(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::destroyGraphicsResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html
    """
    #  void QSGBatchRenderer::Renderer::destroyGraphicsResources()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer24destroyGraphicsResourcesEv',
    )

  @overload(WAIT['QSGBatchRenderer.Buffer'], int)
  @overload(NoneType, int)
  @overload(WAIT['QSGBatchRenderer.Buffer'], int, bool)
  @overload(NoneType, int, bool)
  def map(
      self,
      buffer: Optional[QSGBatchRenderer.Buffer],
      byteSize: int,
      isIndexBuf: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::map(Buffer *buffer, quint32
    byteSize, bool isIndexBuf)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#map

    Parameters
    ----------

    buffer : Optional[QSGBatchRenderer.Buffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    byteSize : int
      Passed on as it is.

    isIndexBuf : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSGBatchRenderer::Renderer::map(Buffer *buffer, quint32 byteSize,
    #      bool isIndexBuf)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer3mapEPNS_6BufferEjb',
        self._addressOf(buffer), byteSize, isIndexBuf,
    )

  @overload(WAIT['QSGBatchRenderer.Buffer'])
  @overload(NoneType)
  @overload(WAIT['QSGBatchRenderer.Buffer'], bool)
  @overload(NoneType, bool)
  def unmap(
      self,
      buffer: Optional[QSGBatchRenderer.Buffer],
      isIndexBuf: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::unmap(Buffer *buffer, bool
    isIndexBuf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#unmap

    Parameters
    ----------

    buffer : Optional[QSGBatchRenderer.Buffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isIndexBuf : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSGBatchRenderer::Renderer::unmap(Buffer *buffer, bool
    #      isIndexBuf)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer5unmapEPNS_6BufferEb',
        self._addressOf(buffer), isIndexBuf,
    )

  def buildRenderListsFromScratch(self) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::Renderer::buildRenderListsFromScratch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html
    """
    #  void QSGBatchRenderer::Renderer::buildRenderListsFromScratch()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer27buildRenderListsFromScratchE'
        'v',
    )

  def buildRenderListsForTaggedRoots(self) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::Renderer::buildRenderListsForTaggedRoots()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html
    """
    #  void QSGBatchRenderer::Renderer::buildRenderListsForTaggedRoots()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer30buildRenderListsForTaggedRoo'
        'tsEv',
    )

  @overload(WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType)
  def tagSubRoots(self, node: Optional[QSGBatchRenderer.Node]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::tagSubRoots(Node *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#tagSubRoots

    Parameters
    ----------

    node : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::tagSubRoots(Node *node)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer11tagSubRootsEPNS_4NodeE',
        self._addressOf(node),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def buildRenderLists(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::buildRenderLists(QSGNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#buildRenderLists

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::buildRenderLists(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer16buildRenderListsEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
    )

  def deleteRemovedElements(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::deleteRemovedElements()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html
    """
    #  void QSGBatchRenderer::Renderer::deleteRemovedElements()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer21deleteRemovedElementsEv',
    )

  def prepareOpaqueBatches(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::prepareOpaqueBatches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html
    """
    #  void QSGBatchRenderer::Renderer::prepareOpaqueBatches()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer20prepareOpaqueBatchesEv',
    )

  @overload(int, int, WAIT['QSGBatchRenderer.Rect'])
  def checkOverlap(
      self,
      first: int,
      last: int,
      bounds: QSGBatchRenderer.Rect,
  ) -> bool:
    """
    Calls Qt's 'bool QSGBatchRenderer::Renderer::checkOverlap(int first, int
    last, const Rect &bounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#checkOverlap

    Parameters
    ----------

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.

    bounds : QSGBatchRenderer.Rect
      Passed on as a value: Qt reads the C++ QSGBatchRenderer::Rect, which
      stays Python's own.
    """
    #  bool QSGBatchRenderer::Renderer::checkOverlap(int first, int last,
    #      const Rect &bounds)
    return self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer12checkOverlapEiiRKNS_4RectE',
        first, last, self._valueOf(bounds),
    )

  def prepareAlphaBatches(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::prepareAlphaBatches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#prepareAlphaBatches
    """
    #  void QSGBatchRenderer::Renderer::prepareAlphaBatches()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer19prepareAlphaBatchesEv',
    )

  @overload(WAIT['QSGBatchRenderer.Batch'])
  @overload(NoneType)
  def invalidateBatchAndOverlappingRenderOrders(
      self,
      batch: Optional[QSGBatchRenderer.Batch],
  ) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::Renderer::invalidateBatchAndOverlappingRenderOrders(
    Batch *batch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html

    Parameters
    ----------

    batch : Optional[QSGBatchRenderer.Batch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::
    #      invalidateBatchAndOverlappingRenderOrders(Batch *batch)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer41invalidateBatchAndOverlappin'
        'gRenderOrdersEPNS_5BatchE',
        self._addressOf(batch),
    )

  @overload(WAIT['QSGBatchRenderer.Batch'])
  @overload(NoneType)
  def uploadBatch(self, b: Optional[QSGBatchRenderer.Batch]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::uploadBatch(Batch *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#uploadBatch

    Parameters
    ----------

    b : Optional[QSGBatchRenderer.Batch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::uploadBatch(Batch *b)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer11uploadBatchEPNS_5BatchE',
        self._addressOf(b),
    )

  def dummyTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSGBatchRenderer::Renderer::dummyTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#dummyTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSGBatchRenderer::Renderer::dummyTexture()
    address = self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer12dummyTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  @overload(QSGGeometry)
  @overload(NoneType)
  def checkLineWidth(self, g: Optional[QSGGeometry]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::checkLineWidth(QSGGeometry
    *g)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#checkLineWidth

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::checkLineWidth(QSGGeometry *g)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer14checkLineWidthEP11QSGGeometr'
        'y',
        self._addressOf(g),
    )

  def applyClipStateToGraphicsState(self) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::Renderer::applyClipStateToGraphicsState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html
    """
    #  void QSGBatchRenderer::Renderer::applyClipStateToGraphicsState()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer29applyClipStateToGraphicsStat'
        'eEv',
    )

  @overload(WAIT['QSGBatchRenderer.Batch'], bool)
  @overload(NoneType, bool)
  def buildStencilPipeline(
      self,
      batch: Optional[QSGBatchRenderer.Batch],
      firstStencilClipInBatch: bool,
  ) -> Optional[QRhiGraphicsPipeline]:
    """
    Calls Qt's 'QRhiGraphicsPipeline
    *QSGBatchRenderer::Renderer::buildStencilPipeline(const Batch *batch,
    bool firstStencilClipInBatch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html

    Parameters
    ----------

    batch : Optional[QSGBatchRenderer.Batch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstStencilClipInBatch : bool
      Passed on as it is.

    Returns
    -------

    Optional[QRhiGraphicsPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiGraphicsPipeline
    #      *QSGBatchRenderer::Renderer::buildStencilPipeline(const Batch
    #      *batch, bool firstStencilClipInBatch)
    address = self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer20buildStencilPipelineEPKNS_5B'
        'atchEb',
        self._addressOf(batch), firstStencilClipInBatch,
    )
    from ..QtGui import QRhiGraphicsPipeline
    return QRhiGraphicsPipeline._cuteAt(address)

  @overload(QSGClipNode, WAIT['QSGBatchRenderer.Batch'])
  @overload(QSGClipNode, NoneType)
  @overload(NoneType, WAIT['QSGBatchRenderer.Batch'])
  @overload(NoneType, NoneType)
  def updateClipState(
      self,
      clipList: Optional[QSGClipNode],
      batch: Optional[QSGBatchRenderer.Batch],
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::updateClipState(const
    QSGClipNode *clipList, Batch *batch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#updateClipState

    Parameters
    ----------

    clipList : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    batch : Optional[QSGBatchRenderer.Batch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::updateClipState(const QSGClipNode
    #      *clipList, Batch *batch)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer15updateClipStateEPK11QSGClipN'
        'odePNS_5BatchE',
        self._addressOf(clipList), self._addressOf(batch),
    )

  @overload(WAIT['QSGBatchRenderer.Batch'])
  @overload(NoneType)
  def enqueueStencilDraw(
      self,
      batch: Optional[QSGBatchRenderer.Batch],
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::enqueueStencilDraw(const
    Batch *batch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#enqueueStencilDraw

    Parameters
    ----------

    batch : Optional[QSGBatchRenderer.Batch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::enqueueStencilDraw(const Batch
    #      *batch)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer18enqueueStencilDrawEPKNS_5Bat'
        'chE',
        self._addressOf(batch),
    )

  @overload(WAIT['QSGBatchRenderer.Batch'])
  @overload(NoneType)
  def renderRhiRenderNode(
      self,
      batch: Optional[QSGBatchRenderer.Batch],
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::renderRhiRenderNode(const
    Batch *batch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#renderRhiRenderNode

    Parameters
    ----------

    batch : Optional[QSGBatchRenderer.Batch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::renderRhiRenderNode(const Batch
    #      *batch)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer19renderRhiRenderNodeEPKNS_5Ba'
        'tchE',
        self._addressOf(batch),
    )

  @overload(WAIT['QSGBatchRenderer.Node'], WAIT['QSGBatchRenderer.Node'])
  @overload(WAIT['QSGBatchRenderer.Node'], NoneType)
  @overload(NoneType, WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType, NoneType)
  def changeBatchRoot(
      self,
      node: Optional[QSGBatchRenderer.Node],
      newRoot: Optional[QSGBatchRenderer.Node],
  ) -> bool:
    """
    Calls Qt's 'bool QSGBatchRenderer::Renderer::changeBatchRoot(Node *node,
    Node *newRoot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#changeBatchRoot

    Parameters
    ----------

    node : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newRoot : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGBatchRenderer::Renderer::changeBatchRoot(Node *node, Node
    #      *newRoot)
    return self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer15changeBatchRootEPNS_4NodeES2'
        '_',
        self._addressOf(node), self._addressOf(newRoot),
    )

  @overload(WAIT['QSGBatchRenderer.Node'], WAIT['QSGBatchRenderer.Node'])
  @overload(WAIT['QSGBatchRenderer.Node'], NoneType)
  @overload(NoneType, WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType, NoneType)
  def registerBatchRoot(
      self,
      childRoot: Optional[QSGBatchRenderer.Node],
      parentRoot: Optional[QSGBatchRenderer.Node],
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::registerBatchRoot(Node
    *childRoot, Node *parentRoot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#registerBatchRoot

    Parameters
    ----------

    childRoot : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentRoot : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::registerBatchRoot(Node *childRoot,
    #      Node *parentRoot)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer17registerBatchRootEPNS_4NodeE'
        'S2_',
        self._addressOf(childRoot), self._addressOf(parentRoot),
    )

  @overload(WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType)
  def removeBatchRootFromParent(
      self,
      childRoot: Optional[QSGBatchRenderer.Node],
  ) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::Renderer::removeBatchRootFromParent(Node *childRoot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html

    Parameters
    ----------

    childRoot : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::removeBatchRootFromParent(Node
    #      *childRoot)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer25removeBatchRootFromParentEPN'
        'S_4NodeE',
        self._addressOf(childRoot),
    )

  @overload(WAIT['QSGBatchRenderer.Node'], WAIT['QSGBatchRenderer.Node'])
  @overload(WAIT['QSGBatchRenderer.Node'], NoneType)
  @overload(NoneType, WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType, NoneType)
  def nodeChangedBatchRoot(
      self,
      node: Optional[QSGBatchRenderer.Node],
      root: Optional[QSGBatchRenderer.Node],
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::nodeChangedBatchRoot(Node
    *node, Node *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html

    Parameters
    ----------

    node : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    root : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::nodeChangedBatchRoot(Node *node, Node
    #      *root)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer20nodeChangedBatchRootEPNS_4No'
        'deES2_',
        self._addressOf(node), self._addressOf(root),
    )

  @overload(WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType)
  def turnNodeIntoBatchRoot(
      self,
      node: Optional[QSGBatchRenderer.Node],
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::turnNodeIntoBatchRoot(Node
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html

    Parameters
    ----------

    node : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::turnNodeIntoBatchRoot(Node *node)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer21turnNodeIntoBatchRootEPNS_4N'
        'odeE',
        self._addressOf(node),
    )

  @overload(WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType)
  def nodeWasRemoved(self, node: Optional[QSGBatchRenderer.Node]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::nodeWasRemoved(Node *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#nodeWasRemoved

    Parameters
    ----------

    node : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::nodeWasRemoved(Node *node)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer14nodeWasRemovedEPNS_4NodeE',
        self._addressOf(node),
    )

  @overload(QSGNode, WAIT['QSGBatchRenderer.Node'])
  @overload(QSGNode, NoneType)
  @overload(NoneType, WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType, NoneType)
  def nodeWasAdded(
      self,
      node: Optional[QSGNode],
      shadowParent: Optional[QSGBatchRenderer.Node],
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::nodeWasAdded(QSGNode *node,
    Node *shadowParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#nodeWasAdded

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    shadowParent : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::nodeWasAdded(QSGNode *node, Node
    #      *shadowParent)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer12nodeWasAddedEP7QSGNodePNS_4N'
        'odeE',
        self._addressOf(node, 'QSGNode'), self._addressOf(shadowParent),
    )

  @overload(WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType)
  def batchRootInfo(
      self,
      node: Optional[QSGBatchRenderer.Node],
  ) -> Optional[QSGBatchRenderer.BatchRootInfo]:
    """
    Calls Qt's 'BatchRootInfo *QSGBatchRenderer::Renderer::batchRootInfo(Node
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#batchRootInfo

    Parameters
    ----------

    node : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGBatchRenderer.BatchRootInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  BatchRootInfo *QSGBatchRenderer::Renderer::batchRootInfo(Node *node)
    address = self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer13batchRootInfoEPNS_4NodeE',
        self._addressOf(node),
    )
    return QSGBatchRenderer.BatchRootInfo._cuteAt(address)

  def newBatch(self) -> Optional[QSGBatchRenderer.Batch]:
    """
    Calls Qt's 'Batch *QSGBatchRenderer::Renderer::newBatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#newBatch

    Returns
    -------

    Optional[QSGBatchRenderer.Batch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Batch *QSGBatchRenderer::Renderer::newBatch()
    address = self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer8newBatchEv',
    )
    return QSGBatchRenderer.Batch._cuteAt(address)

  @overload(WAIT['QSGBatchRenderer.Batch'])
  @overload(NoneType)
  def invalidateAndRecycleBatch(
      self,
      b: Optional[QSGBatchRenderer.Batch],
  ) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::Renderer::invalidateAndRecycleBatch(Batch *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html

    Parameters
    ----------

    b : Optional[QSGBatchRenderer.Batch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Renderer::invalidateAndRecycleBatch(Batch *b)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer25invalidateAndRecycleBatchEPN'
        'S_5BatchE',
        self._addressOf(b),
    )

  @overload(WAIT['QSGBatchRenderer.Element'])
  @overload(NoneType)
  @overload(WAIT['QSGBatchRenderer.Element'], bool)
  @overload(NoneType, bool)
  def releaseElement(
      self,
      e: Optional[QSGBatchRenderer.Element],
      inDestructor: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Renderer::releaseElement(Element *e,
    bool inDestructor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-renderer.html#releaseElement

    Parameters
    ----------

    e : Optional[QSGBatchRenderer.Element]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inDestructor : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSGBatchRenderer::Renderer::releaseElement(Element *e, bool
    #      inDestructor)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer8Renderer14releaseElementEPNS_7ElementE'
        'b',
        self._addressOf(e), inDestructor,
    )

  @staticmethod
  def beginRenderPass(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Renderer::beginRenderPass(RenderPassContext
    *ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.beginRenderPass' has no cute function "
        "yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::beginRenderPass(RenderPassContext "
        "*ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', "
        "which has no cute class yet.")

  @staticmethod
  def cleanupBatches(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Renderer::cleanupBatches(QDataBuffer<Batch
    *> *batches)': names 'QDataBuffer<QSGBatchRenderer::Batch *>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.cleanupBatches' has no cute function "
        "yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::cleanupBatches(QDataBuffer<Batch *> "
        "*batches)': names 'QDataBuffer<QSGBatchRenderer::Batch *>', which "
        "has no cute class yet.")

  @staticmethod
  def endRenderPass(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Renderer::endRenderPass(RenderPassContext
    *ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.endRenderPass' has no cute function "
        "yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::endRenderPass(RenderPassContext "
        "*ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', "
        "which has no cute class yet.")

  @staticmethod
  def ensurePipelineState(*__, **_) -> Never:
    """
    Qt's 'bool QSGBatchRenderer::Renderer::ensurePipelineState(Element *e,
    const ShaderManager::Shader *sms, bool depthPostPass)': names
    'QSGBatchRenderer::ShaderManager::Shader', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.ensurePipelineState' has no cute "
        "function yet. Qt's 'bool "
        "QSGBatchRenderer::Renderer::ensurePipelineState(Element *e, const "
        "ShaderManager::Shader *sms, bool depthPostPass)': names "
        "'QSGBatchRenderer::ShaderManager::Shader', which has no cute class "
        "yet.")

  @staticmethod
  def nodeWasTransformed(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Renderer::nodeWasTransformed(Node *node, int
    *vertexCount)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.nodeWasTransformed' has no cute "
        "function yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::nodeWasTransformed(Node *node, int "
        "*vertexCount)': takes a number to change where it is.")

  @staticmethod
  def prepareRenderMergedBatch(*__, **_) -> Never:
    """
    Qt's 'bool QSGBatchRenderer::Renderer::prepareRenderMergedBatch(Batch
    *batch, PreparedRenderBatch *renderBatch)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.prepareRenderMergedBatch' has no cute "
        "function yet. Qt's 'bool "
        "QSGBatchRenderer::Renderer::prepareRenderMergedBatch(Batch *batch, "
        "PreparedRenderBatch *renderBatch)': names "
        "'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no "
        "cute class yet.")

  @staticmethod
  def prepareRenderPass(*__, **_) -> Never:
    """
    Qt's 'void
    QSGBatchRenderer::Renderer::prepareRenderPass(RenderPassContext *ctx)':
    names 'QSGBatchRenderer::Renderer::RenderPassContext', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.prepareRenderPass' has no cute function "
        "yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::prepareRenderPass(RenderPassContext "
        "*ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', "
        "which has no cute class yet.")

  @staticmethod
  def prepareRenderUnmergedBatch(*__, **_) -> Never:
    """
    Qt's 'bool QSGBatchRenderer::Renderer::prepareRenderUnmergedBatch(Batch
    *batch, PreparedRenderBatch *renderBatch)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.prepareRenderUnmergedBatch' has no cute "
        "function yet. Qt's 'bool "
        "QSGBatchRenderer::Renderer::prepareRenderUnmergedBatch(Batch "
        "*batch, PreparedRenderBatch *renderBatch)': names "
        "'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no "
        "cute class yet.")

  @staticmethod
  def prepareRhiRenderNode(*__, **_) -> Never:
    """
    Qt's 'bool QSGBatchRenderer::Renderer::prepareRhiRenderNode(Batch *batch,
    PreparedRenderBatch *renderBatch)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.prepareRhiRenderNode' has no cute "
        "function yet. Qt's 'bool "
        "QSGBatchRenderer::Renderer::prepareRhiRenderNode(Batch *batch, "
        "PreparedRenderBatch *renderBatch)': names "
        "'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no "
        "cute class yet.")

  @staticmethod
  def recordRenderPass(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Renderer::recordRenderPass(RenderPassContext
    *ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.recordRenderPass' has no cute function "
        "yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::recordRenderPass(RenderPassContext "
        "*ctx)': names 'QSGBatchRenderer::Renderer::RenderPassContext', "
        "which has no cute class yet.")

  @staticmethod
  def renderMergedBatch(*__, **_) -> Never:
    """
    Qt's 'void
    QSGBatchRenderer::Renderer::renderMergedBatch(PreparedRenderBatch
    *renderBatch, bool depthPostPass)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.renderMergedBatch' has no cute function "
        "yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::renderMergedBatch(PreparedRenderBatch "
        "*renderBatch, bool depthPostPass)': names "
        "'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no "
        "cute class yet.")

  @staticmethod
  def renderUnmergedBatch(*__, **_) -> Never:
    """
    Qt's 'void
    QSGBatchRenderer::Renderer::renderUnmergedBatch(PreparedRenderBatch
    *renderBatch, bool depthPostPass)': names
    'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.renderUnmergedBatch' has no cute "
        "function yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::renderUnmergedBatch(PreparedRenderBatch"
        " *renderBatch, bool depthPostPass)': names "
        "'QSGBatchRenderer::Renderer::PreparedRenderBatch', which has no "
        "cute class yet.")

  @staticmethod
  def setActiveRhiShader(*__, **_) -> Never:
    """
    Qt's 'void
    QSGBatchRenderer::Renderer::setActiveRhiShader(QSGMaterialShader
    *program, ShaderManager::Shader *shader)': names
    'QSGBatchRenderer::ShaderManager::Shader', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.setActiveRhiShader' has no cute "
        "function yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::setActiveRhiShader(QSGMaterialShader "
        "*program, ShaderManager::Shader *shader)': names "
        "'QSGBatchRenderer::ShaderManager::Shader', which has no cute class "
        "yet.")

  @staticmethod
  def updateMaterialDynamicData(*__, **_) -> Never:
    """
    Qt's 'void
    QSGBatchRenderer::Renderer::updateMaterialDynamicData(ShaderManager::
    Shader *sms, QSGMaterialShader::RenderState &renderState, QSGMaterial
    *material, const Batch *batch, Element *e, int ubufOffset, char
    *directUpdatePtr)': names 'QSGBatchRenderer::ShaderManager::Shader',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.updateMaterialDynamicData' has no cute "
        "function yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::updateMaterialDynamicData(ShaderManager"
        "::Shader *sms, QSGMaterialShader::RenderState &renderState, "
        "QSGMaterial *material, const Batch *batch, Element *e, int "
        "ubufOffset, char *directUpdatePtr)': names "
        "'QSGBatchRenderer::ShaderManager::Shader', which has no cute class "
        "yet.")

  @staticmethod
  def updateMaterialStaticData(*__, **_) -> Never:
    """
    Qt's 'void
    QSGBatchRenderer::Renderer::updateMaterialStaticData(ShaderManager::
    Shader *sms, QSGMaterialShader::RenderState &renderState, QSGMaterial
    *material, Batch *batch, bool *gstateChanged)': names
    'QSGBatchRenderer::ShaderManager::Shader', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.updateMaterialStaticData' has no cute "
        "function yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::updateMaterialStaticData(ShaderManager:"
        ":Shader *sms, QSGMaterialShader::RenderState &renderState, "
        "QSGMaterial *material, Batch *batch, bool *gstateChanged)': names "
        "'QSGBatchRenderer::ShaderManager::Shader', which has no cute class "
        "yet.")

  @staticmethod
  def uploadMergedElement(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Renderer::uploadMergedElement(Element *e,
    int vaOffset, char **vertexData, char **zData, char **indexData, void
    *iBasePtr, int *indexCount)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Renderer.uploadMergedElement' has no cute "
        "function yet. Qt's 'void "
        "QSGBatchRenderer::Renderer::uploadMergedElement(Element *e, int "
        "vaOffset, char **vertexData, char **zData, char **indexData, void "
        "*iBasePtr, int *indexCount)': takes a type Python has no way to "
        "hand over yet.")
