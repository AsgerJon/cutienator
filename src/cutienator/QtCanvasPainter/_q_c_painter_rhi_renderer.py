"""
QCPainterRhiRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterrhirenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QCPainterRhiRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QRhiTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QMatrix4x4
  from . import QCPainterEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']


class QCPainterRhiRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCPainterRhiRenderer: a plain Python object standing
  in front of one C++ QCPainterRhiRenderer.

  What exists
  -----------

  Every function of Qt's QCPainterRhiRenderer that has a ritual and that
  Python can call so far, 4 names in all: 'isValid', 'engine',
  'setCustomMatrix', 'resetDebugCounters'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QCPainterRhiRenderer::textureFormatInfo(QRhiTexture::Format
    format, QSize size, quint32 *bpl, quint32 *byteSize, quint32
    *bytesPerPixel)': takes a number to change where it is.

  What has no ritual
  ------------------

  69 of the 75 functions Qt declares: 59 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 9 leans on
  'QCPainterRhiRenderer; 1 the compiler refuses its ritual as it would be
  written here.

  What to expect
  --------------

  - The C++ QCPainterRhiRenderer is created at the first use, not by
    'QCPainterRhiRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCPainterRhiRenderer.
  - Each name of Qt's QCPainterRhiRenderer that has no cute function yet,
    'allocCall', 'allocCommonUniforms', 'allocIndices', 'allocPaths',
    'allocTexture', 'allocVerts', 'beginPrepare', 'beginPrepareAndPaint',
    'bindPipeline', 'canvasRenderTarget', 'clearStencil',
    'commitResourceUpdates', 'create', 'createCanvas', 'createRhiContext',
    'createSrb', 'customUniformPtr', 'destroy', 'destroyCanvas',
    'endPrepare', 'endPrepareAndPaint', 'findTexture', 'flags',
    'flagsCacheProps', 'grabCanvas', 'hasDrawCalls', 'isOffscreenCanvasYUp',
    'isPathCachedForFill', 'isPathCachedForStroke', 'isYUpInNDC', 'pipeline',
    'populateColorFont', 'populateFont', 'populateFontFromShapedText',
    'prepareCustomPaint', 'preparePaint', 'recordCanvasRenderPass',
    'recordRenderPass', 'removePathGroup', 'render', 'renderCreate',
    'renderCreateNativeTexture', 'renderCreateTexture', 'renderDelete',
    'renderDeleteTexture', 'renderFill', 'renderStencil', 'renderStroke',
    'renderTextFill', 'renderTextFillCustom', 'renderUpdateNativeTexture',
    'renderUpdateTexture', 'resetForNewFrame', 'resetForPass',
    'resourceUpdateBatch', 'sampler', 'setFlag', 'setViewport',
    'syncDebugCounters', 'testFlag', 'textureFormatInfo', 'transferFillGeom',
    'transferPathsFromCachedPathGroup', 'transferStrokeGeom', 'uniformPtr',
    'updateVertUniforms', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QCPainterRhiRenderer, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class RenderFlag(CuteFlags):
    """
    The flags enum 'QCPainterRhiRenderer::RenderFlag' of Qt, with the 7 names
    Qt gives in it. Qt names the type of its combinations
    'QCPainterRhiRenderer::RenderFlags'.
    """

    Antialiasing = 0x1
    StencilStrokes = 0x2
    TransformedClipping = 0x8
    SimpleClipping = 0x10
    DepthTest = 0x20
    CustomMatrix = 0x40
    WindingEnforce = 0x80

  RenderFlags = RenderFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCPainterRhiRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCPainterRhiRenderer::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterrhirenderer.html#isValid
    """
    #  bool QCPainterRhiRenderer::isValid() const
    return self.uglySide.call('ritual_ZNK20QCPainterRhiRenderer7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMatrix4x4)
  def setCustomMatrix(self, matrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QCPainterRhiRenderer::setCustomMatrix(const QMatrix4x4
    &matrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterrhirenderer.html#setCustomMatrix

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QCPainterRhiRenderer::setCustomMatrix(const QMatrix4x4 &matrix)
    self.uglySide.call(
        'ritual_ZN20QCPainterRhiRenderer15setCustomMatrixERK10QMatrix4x4',
        self._valueOf(matrix),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCPainterRhiRenderer::QCPainterRhiRenderer()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterrhirenderer.html#QCPainterRhiRenderer
    """
    #  QCPainterRhiRenderer::QCPainterRhiRenderer()
    self._noteCreation(QCPainterRhiRenderer, lambda: Rituals.call(
        'ritual_ZN20QCPainterRhiRendererC1Ev',
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

  def engine(self) -> Optional[QCPainterEngine]:
    """
    Calls Qt's 'QCPainterEngine *QCPainterRhiRenderer::engine()'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterrhirenderer.html#engine

    Returns
    -------

    Optional[QCPainterEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCPainterEngine *QCPainterRhiRenderer::engine()
    address = self.uglySide.call('ritual_ZN20QCPainterRhiRenderer6engineEv')
    from . import QCPainterEngine
    return QCPainterEngine._cuteAt(address)

  def resetDebugCounters(self) -> None:
    """
    Calls Qt's 'void QCPainterRhiRenderer::resetDebugCounters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterrhirenderer.html#resetDebugCounters
    """
    #  void QCPainterRhiRenderer::resetDebugCounters()
    self.uglySide.call(
        'ritual_ZN20QCPainterRhiRenderer18resetDebugCountersEv',
    )

  @staticmethod
  def allocCall(*__, **_) -> Never:
    """
    Qt's 'QCRHICall *QCPainterRhiRenderer::allocCall()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.allocCall' has no cute function yet. Qt's "
        "'QCRHICall *QCPainterRhiRenderer::allocCall()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def allocCommonUniforms(*__, **_) -> Never:
    """
    Qt's 'int QCPainterRhiRenderer::allocCommonUniforms(int count)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.allocCommonUniforms' has no cute function "
        "yet. Qt's 'int QCPainterRhiRenderer::allocCommonUniforms(int "
        "count)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QCRHIContext'.")

  @staticmethod
  def allocIndices(*__, **_) -> Never:
    """
    Qt's 'int QCPainterRhiRenderer::allocIndices(int count)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.allocIndices' has no cute function yet. Qt's "
        "'int QCPainterRhiRenderer::allocIndices(int count)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def allocPaths(*__, **_) -> Never:
    """
    Qt's 'int QCPainterRhiRenderer::allocPaths(int count)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.allocPaths' has no cute function yet. Qt's "
        "'int QCPainterRhiRenderer::allocPaths(int count)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def allocTexture(*__, **_) -> Never:
    """
    Qt's 'QCRHITexture *QCPainterRhiRenderer::allocTexture()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.allocTexture' has no cute function yet. Qt's "
        "'QCRHITexture *QCPainterRhiRenderer::allocTexture()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def allocVerts(*__, **_) -> Never:
    """
    Qt's 'int QCPainterRhiRenderer::allocVerts(int count)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.allocVerts' has no cute function yet. Qt's "
        "'int QCPainterRhiRenderer::allocVerts(int count)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def beginPrepare(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::beginPrepare(QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt, float devicePixelRatio)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.beginPrepare' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::beginPrepare(QRhiCommandBuffer *cb, "
        "QRhiRenderTarget *rt, float devicePixelRatio)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def beginPrepareAndPaint(*__, **_) -> Never:
    """
    - Qt's 'void QCPainterRhiRenderer::beginPrepareAndPaint(QRhiCommandBuffer
      *cb, QRhiRenderTarget *rt)': leans on
      'QCPainterRhiRenderer::beginPrepare(QRhiCommandBuffer*,
      QRhiRenderTarget*, float)', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    - Qt's 'void QCPainterRhiRenderer::beginPrepareAndPaint(QRhiCommandBuffer
      *cb, QRhiRenderTarget *rt, float logicalWidth, float logicalHeight,
      float dpr)': leans on
      'QCPainterRhiRenderer::beginPrepare(QRhiCommandBuffer*,
      QRhiRenderTarget*, float)', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.beginPrepareAndPaint' has no cute function "
        "yet. Qt's 'void "
        "QCPainterRhiRenderer::beginPrepareAndPaint(QRhiCommandBuffer *cb, "
        "QRhiRenderTarget *rt)': leans on "
        "'QCPainterRhiRenderer::beginPrepare(QRhiCommandBuffer*, "
        "QRhiRenderTarget*, float)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken. Qt's "
        "'void QCPainterRhiRenderer::beginPrepareAndPaint(QRhiCommandBuffer "
        "*cb, QRhiRenderTarget *rt, float logicalWidth, float "
        "logicalHeight, float dpr)': leans on "
        "'QCPainterRhiRenderer::beginPrepare(QRhiCommandBuffer*, "
        "QRhiRenderTarget*, float)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def bindPipeline(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::bindPipeline(QCRHICall *call, int
    pipelineIndex, int srbIndex, const QRhiCommandBuffer::DynamicOffset
    &vertDynamicOffset, const QRhiCommandBuffer::DynamicOffset
    &dynamicOffset, bool indexedDraw, bool *needsViewport)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.bindPipeline' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::bindPipeline(QCRHICall *call, int "
        "pipelineIndex, int srbIndex, const "
        "QRhiCommandBuffer::DynamicOffset &vertDynamicOffset, const "
        "QRhiCommandBuffer::DynamicOffset &dynamicOffset, bool indexedDraw, "
        "bool *needsViewport)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def canvasRenderTarget(*__, **_) -> Never:
    """
    Qt's 'QRhiRenderTarget *QCPainterRhiRenderer::canvasRenderTarget(const
    QCanvasOffscreenCanvas &canvas)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: incomplete
    type 'QCanvasOffscreenCanvasPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.canvasRenderTarget' has no cute function "
        "yet. Qt's 'QRhiRenderTarget "
        "*QCPainterRhiRenderer::canvasRenderTarget(const "
        "QCanvasOffscreenCanvas &canvas)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "incomplete type 'QCanvasOffscreenCanvasPrivate' named in nested "
        "name specifier.")

  @staticmethod
  def clearStencil(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::clearStencil(const QCState &state)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.clearStencil' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::clearStencil(const QCState &state)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QCRHIContext'.")

  @staticmethod
  def commitResourceUpdates(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::commitResourceUpdates()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.commitResourceUpdates' has no cute function "
        "yet. Qt's 'void QCPainterRhiRenderer::commitResourceUpdates()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QCRHIContext'.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::create(QRhi *rhi, QCanvasPainter
    *painter)': leans on 'QCPainterRhiRenderer::renderDelete()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.create' has no cute function yet. Qt's 'void "
        "QCPainterRhiRenderer::create(QRhi *rhi, QCanvasPainter *painter)': "
        "leans on 'QCPainterRhiRenderer::renderDelete()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def createCanvas(*__, **_) -> Never:
    """
    Qt's 'QCanvasOffscreenCanvas QCPainterRhiRenderer::createCanvas(QSize
    pixelSize, int sampleCount, QCanvasOffscreenCanvas::Flags flags)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.createCanvas' has no cute function yet. Qt's "
        "'QCanvasOffscreenCanvas QCPainterRhiRenderer::createCanvas(QSize "
        "pixelSize, int sampleCount, QCanvasOffscreenCanvas::Flags flags)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QCRHIContext'.")

  @staticmethod
  def createRhiContext(*__, **_) -> Never:
    """
    Qt's 'QCContext *QCPainterRhiRenderer::createRhiContext(QRhi *rhi)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: allocation of incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.createRhiContext' has no cute function yet. "
        "Qt's 'QCContext *QCPainterRhiRenderer::createRhiContext(QRhi "
        "*rhi)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: allocation of "
        "incomplete type 'QCRHIContext'.")

  @staticmethod
  def createSrb(*__, **_) -> Never:
    """
    Qt's 'QRhiShaderResourceBindings *QCPainterRhiRenderer::createSrb(int
    brushImage, int fontImage)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.createSrb' has no cute function yet. Qt's "
        "'QRhiShaderResourceBindings *QCPainterRhiRenderer::createSrb(int "
        "brushImage, int fontImage)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def customUniformPtr(*__, **_) -> Never:
    """
    Qt's 'QCanvasCustomBrushPrivate::CommonUniforms
    *QCPainterRhiRenderer::customUniformPtr(int i) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.customUniformPtr' has no cute function yet. "
        "Qt's 'QCanvasCustomBrushPrivate::CommonUniforms "
        "*QCPainterRhiRenderer::customUniformPtr(int i) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def destroy(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::destroy()': leans on
    'QCPainterRhiRenderer::renderDelete()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.destroy' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::destroy()': leans on "
        "'QCPainterRhiRenderer::renderDelete()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def destroyCanvas(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::destroyCanvas(QCanvasOffscreenCanvas
    &canvas)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: incomplete type
    'QCanvasOffscreenCanvasPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.destroyCanvas' has no cute function yet. "
        "Qt's 'void "
        "QCPainterRhiRenderer::destroyCanvas(QCanvasOffscreenCanvas "
        "&canvas)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: incomplete type "
        "'QCanvasOffscreenCanvasPrivate' named in nested name specifier.")

  @staticmethod
  def endPrepare(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::endPrepare()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.endPrepare' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::endPrepare()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def endPrepareAndPaint(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::endPrepareAndPaint()': leans on
    'QCPainterRhiRenderer::endPrepare()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.endPrepareAndPaint' has no cute function "
        "yet. Qt's 'void QCPainterRhiRenderer::endPrepareAndPaint()': leans "
        "on 'QCPainterRhiRenderer::endPrepare()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def findTexture(*__, **_) -> Never:
    """
    - Qt's 'QCRHITexture *QCPainterRhiRenderer::findTexture(QRhiTexture
      *texture) const': Qt's library has no name for it, and its code in Qt's
      source does not compile apart from its file: member access into
      incomplete type 'QCRHIContext'.
    - Qt's 'QCRHITexture *QCPainterRhiRenderer::findTexture(int id) const':
      Qt's library has no name for it, and its code in Qt's source does not
      compile apart from its file: member access into incomplete type
      'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.findTexture' has no cute function yet. Qt's "
        "'QCRHITexture *QCPainterRhiRenderer::findTexture(QRhiTexture "
        "*texture) const': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QCRHIContext'. Qt's 'QCRHITexture "
        "*QCPainterRhiRenderer::findTexture(int id) const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def flags(*__, **_) -> Never:
    """
    Qt's 'RenderFlags QCPainterRhiRenderer::flags() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.flags' has no cute function yet. Qt's "
        "'RenderFlags QCPainterRhiRenderer::flags() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def flagsCacheProps(*__, **_) -> Never:
    """
    Qt's 'int QCPainterRhiRenderer::flagsCacheProps() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.flagsCacheProps' has no cute function yet. "
        "Qt's 'int QCPainterRhiRenderer::flagsCacheProps() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def grabCanvas(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::grabCanvas(const QCanvasOffscreenCanvas
    &canvas, const QObject *context, QtPrivate::SlotObjUniquePtr callback,
    QRhiCommandBuffer *maybeCb)': the compiler refuses its ritual as it would
    be written here: call to deleted constructor of
    'QtPrivate::SlotObjUniquePtr' (aka 'std::unique_ptr<QSlotObjectBase,
    QSlotObjectBase::Deleter>').
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.grabCanvas' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::grabCanvas(const "
        "QCanvasOffscreenCanvas &canvas, const QObject *context, "
        "QtPrivate::SlotObjUniquePtr callback, QRhiCommandBuffer "
        "*maybeCb)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of 'QtPrivate::SlotObjUniquePtr' "
        "(aka 'std::unique_ptr<QSlotObjectBase, QSlotObjectBase::Deleter>')."
    )

  @staticmethod
  def hasDrawCalls(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterRhiRenderer::hasDrawCalls() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.hasDrawCalls' has no cute function yet. Qt's "
        "'bool QCPainterRhiRenderer::hasDrawCalls() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def isOffscreenCanvasYUp(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterRhiRenderer::isOffscreenCanvasYUp() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.isOffscreenCanvasYUp' has no cute function "
        "yet. Qt's 'bool QCPainterRhiRenderer::isOffscreenCanvasYUp() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QCRHIContext'.")

  @staticmethod
  def isPathCachedForFill(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterRhiRenderer::isPathCachedForFill(QCanvasPath *path,
    int pathGroup, const QCState &state)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.isPathCachedForFill' has no cute function "
        "yet. Qt's 'bool "
        "QCPainterRhiRenderer::isPathCachedForFill(QCanvasPath *path, int "
        "pathGroup, const QCState &state)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def isPathCachedForStroke(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterRhiRenderer::isPathCachedForStroke(QCanvasPath *path,
    int pathGroup, const QCState &state)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.isPathCachedForStroke' has no cute function "
        "yet. Qt's 'bool "
        "QCPainterRhiRenderer::isPathCachedForStroke(QCanvasPath *path, int "
        "pathGroup, const QCState &state)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def isYUpInNDC(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterRhiRenderer::isYUpInNDC() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.isYUpInNDC' has no cute function yet. Qt's "
        "'bool QCPainterRhiRenderer::isYUpInNDC() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def pipeline(*__, **_) -> Never:
    """
    Qt's 'QRhiGraphicsPipeline *QCPainterRhiRenderer::pipeline(const
    QCRHIPipelineStateKey &key, QRhiRenderPassDescriptor *rpDesc,
    QRhiShaderResourceBindings *srb)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.pipeline' has no cute function yet. Qt's "
        "'QRhiGraphicsPipeline *QCPainterRhiRenderer::pipeline(const "
        "QCRHIPipelineStateKey &key, QRhiRenderPassDescriptor *rpDesc, "
        "QRhiShaderResourceBindings *srb)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def populateColorFont(*__, **_) -> Never:
    """
    Qt's 'int
    QCPainterRhiRenderer::populateColorFont(QCRhiDistanceFieldGlyphCache::
    VertexList &vertices, QCRhiDistanceFieldGlyphCache::IndexList &indices)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.populateColorFont' has no cute function yet. "
        "Qt's 'int "
        "QCPainterRhiRenderer::populateColorFont(QCRhiDistanceFieldGlyphCach"
        "e::VertexList &vertices, QCRhiDistanceFieldGlyphCache::IndexList "
        "&indices)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QCRHIContext'.")

  @staticmethod
  def populateFont(*__, **_) -> Never:
    """
    Qt's 'int QCPainterRhiRenderer::populateFont(const QFont &font, const
    QRectF &rect, const QString &text,
    QCRhiDistanceFieldGlyphCache::VertexList &vertices,
    QCRhiDistanceFieldGlyphCache::IndexList &indices)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.populateFont' has no cute function yet. Qt's "
        "'int QCPainterRhiRenderer::populateFont(const QFont &font, const "
        "QRectF &rect, const QString &text, "
        "QCRhiDistanceFieldGlyphCache::VertexList &vertices, "
        "QCRhiDistanceFieldGlyphCache::IndexList &indices)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def populateFontFromShapedText(*__, **_) -> Never:
    """
    Qt's 'int QCPainterRhiRenderer::populateFontFromShapedText(QFontEngine
    *fontEngine, const quint32 *glyphIndexes, const QFixedPoint
    *glyphPositions, int glyphCount, QCRhiDistanceFieldGlyphCache::VertexList
    &vertices, QCRhiDistanceFieldGlyphCache::IndexList &indices)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.populateFontFromShapedText' has no cute "
        "function yet. Qt's 'int "
        "QCPainterRhiRenderer::populateFontFromShapedText(QFontEngine "
        "*fontEngine, const quint32 *glyphIndexes, const QFixedPoint "
        "*glyphPositions, int glyphCount, "
        "QCRhiDistanceFieldGlyphCache::VertexList &vertices, "
        "QCRhiDistanceFieldGlyphCache::IndexList &indices)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def prepareCustomPaint(*__, **_) -> Never:
    """
    Qt's 'void
    QCPainterRhiRenderer::prepareCustomPaint(QCanvasCustomBrushPrivate::
    CommonUniforms *frag, const QCPaint &paint, QCanvasCustomBrushPrivate
    *privBrush, const QCState &state, float width, float aa, float strokeThr,
    float fontAlphaMin, float fontAlphaMax)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.prepareCustomPaint' has no cute function "
        "yet. Qt's 'void "
        "QCPainterRhiRenderer::prepareCustomPaint(QCanvasCustomBrushPrivate:"
        ":CommonUniforms *frag, const QCPaint &paint, "
        "QCanvasCustomBrushPrivate *privBrush, const QCState &state, float "
        "width, float aa, float strokeThr, float fontAlphaMin, float "
        "fontAlphaMax)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QCRHIContext'.")

  @staticmethod
  def preparePaint(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::preparePaint(QCRHICommonUniforms *frag,
    const QCPaint &paint, const QCState &state, float width, float aa, float
    strokeThr, float fontAlphaMin, float fontAlphaMax)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QCRHICommonUniforms'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.preparePaint' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::preparePaint(QCRHICommonUniforms "
        "*frag, const QCPaint &paint, const QCState &state, float width, "
        "float aa, float strokeThr, float fontAlphaMin, float "
        "fontAlphaMax)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QCRHICommonUniforms'.")

  @staticmethod
  def recordCanvasRenderPass(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::recordCanvasRenderPass(QRhiCommandBuffer
    *cb, const QCanvasOffscreenCanvas &canvas)': leans on
    'QCPainterRhiRenderer::canvasRenderTarget(QCanvasOffscreenCanvas
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.recordCanvasRenderPass' has no cute function "
        "yet. Qt's 'void "
        "QCPainterRhiRenderer::recordCanvasRenderPass(QRhiCommandBuffer "
        "*cb, const QCanvasOffscreenCanvas &canvas)': leans on "
        "'QCPainterRhiRenderer::canvasRenderTarget(QCanvasOffscreenCanvas "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def recordRenderPass(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::recordRenderPass(QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt, QColor clearColor)': leans on
    'QCPainterRhiRenderer::render()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.recordRenderPass' has no cute function yet. "
        "Qt's 'void "
        "QCPainterRhiRenderer::recordRenderPass(QRhiCommandBuffer *cb, "
        "QRhiRenderTarget *rt, QColor clearColor)': leans on "
        "'QCPainterRhiRenderer::render()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def removePathGroup(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::removePathGroup(int pathGroup)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.removePathGroup' has no cute function yet. "
        "Qt's 'void QCPainterRhiRenderer::removePathGroup(int pathGroup)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QCRHIContext'.")

  @staticmethod
  def render(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::render()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.render' has no cute function yet. Qt's 'void "
        "QCPainterRhiRenderer::render()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def renderCreate(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterRhiRenderer::renderCreate()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderCreate' has no cute function yet. Qt's "
        "'bool QCPainterRhiRenderer::renderCreate()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def renderCreateNativeTexture(*__, **_) -> Never:
    """
    Qt's 'QCRHITexture
    *QCPainterRhiRenderer::renderCreateNativeTexture(QRhiTexture *texture,
    QCanvasPainter::ImageFlags flags)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderCreateNativeTexture' has no cute "
        "function yet. Qt's 'QCRHITexture "
        "*QCPainterRhiRenderer::renderCreateNativeTexture(QRhiTexture "
        "*texture, QCanvasPainter::ImageFlags flags)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def renderCreateTexture(*__, **_) -> Never:
    """
    Qt's 'int QCPainterRhiRenderer::renderCreateTexture(QCTextureFormat type,
    int w, int h, QCanvasPainter::ImageFlags imageFlags, const uchar *data)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderCreateTexture' has no cute function "
        "yet. Qt's 'int "
        "QCPainterRhiRenderer::renderCreateTexture(QCTextureFormat type, "
        "int w, int h, QCanvasPainter::ImageFlags imageFlags, const uchar "
        "*data)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QCRHIContext'.")

  @staticmethod
  def renderDelete(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::renderDelete()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderDelete' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::renderDelete()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def renderDeleteTexture(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterRhiRenderer::renderDeleteTexture(int image)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderDeleteTexture' has no cute function "
        "yet. Qt's 'bool QCPainterRhiRenderer::renderDeleteTexture(int "
        "image)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QCRHIContext'.")

  @staticmethod
  def renderFill(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::renderFill(const QCPaint &paint, const
    QCState &state, const QRectF &bounds,
    std::optional<QCRhiUncachedPathDrawArgs> uncachedPathInfo,
    std::optional<QCRhiCachedPathDrawArgs> cachedPathInfo,
    QCanvasPainter::FillRule fillRule)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QCRHICall'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderFill' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::renderFill(const QCPaint &paint, const "
        "QCState &state, const QRectF &bounds, "
        "std::optional<QCRhiUncachedPathDrawArgs> uncachedPathInfo, "
        "std::optional<QCRhiCachedPathDrawArgs> cachedPathInfo, "
        "QCanvasPainter::FillRule fillRule)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QCRHICall'.")

  @staticmethod
  def renderStencil(*__, **_) -> Never:
    """
    - Qt's 'void QCPainterRhiRenderer::renderStencil(const QCState &state,
      const QList<QRectF> &rects)': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: member access
      into incomplete type 'QCRHICall'.
    - Qt's 'void QCPainterRhiRenderer::renderStencil(const QCState &state,
      const QVectorPath &clipPath)': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: member access
      into incomplete type 'QCRHICall'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderStencil' has no cute function yet. "
        "Qt's 'void QCPainterRhiRenderer::renderStencil(const QCState "
        "&state, const QList<QRectF> &rects)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QCRHICall'. Qt's 'void "
        "QCPainterRhiRenderer::renderStencil(const QCState &state, const "
        "QVectorPath &clipPath)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QCRHICall'.")

  @staticmethod
  def renderStroke(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::renderStroke(const QCPaint &paint, const
    QCState &state, float strokeWidth,
    std::optional<QCRhiUncachedPathDrawArgs> uncachedPathInfo,
    std::optional<QCRhiCachedPathDrawArgs> cachedPathInfo)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QCRHICall'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderStroke' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::renderStroke(const QCPaint &paint, "
        "const QCState &state, float strokeWidth, "
        "std::optional<QCRhiUncachedPathDrawArgs> uncachedPathInfo, "
        "std::optional<QCRhiCachedPathDrawArgs> cachedPathInfo)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QCRHICall'.")

  @staticmethod
  def renderTextFill(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::renderTextFill(const QCPaint &paint,
    const QCState &state, const QCRhiDistanceFieldGlyphCache::VertexList
    &verts, const QCRhiDistanceFieldGlyphCache::IndexList &indices, bool
    colorGlyphs)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QCRHICall'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderTextFill' has no cute function yet. "
        "Qt's 'void QCPainterRhiRenderer::renderTextFill(const QCPaint "
        "&paint, const QCState &state, const "
        "QCRhiDistanceFieldGlyphCache::VertexList &verts, const "
        "QCRhiDistanceFieldGlyphCache::IndexList &indices, bool "
        "colorGlyphs)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QCRHICall'.")

  @staticmethod
  def renderTextFillCustom(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::renderTextFillCustom(const QCPaint
    &paint, const QCState &state, QCanvasCustomBrushPrivate *privBrush, const
    QCRhiDistanceFieldGlyphCache::VertexList &verts, const
    QCRhiDistanceFieldGlyphCache::IndexList &indices)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QCRHICall'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderTextFillCustom' has no cute function "
        "yet. Qt's 'void QCPainterRhiRenderer::renderTextFillCustom(const "
        "QCPaint &paint, const QCState &state, QCanvasCustomBrushPrivate "
        "*privBrush, const QCRhiDistanceFieldGlyphCache::VertexList &verts, "
        "const QCRhiDistanceFieldGlyphCache::IndexList &indices)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QCRHICall'.")

  @staticmethod
  def renderUpdateNativeTexture(*__, **_) -> Never:
    """
    Qt's 'QCRHITexture
    *QCPainterRhiRenderer::renderUpdateNativeTexture(QRhiTexture *oldTexture,
    QRhiTexture *texture)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderUpdateNativeTexture' has no cute "
        "function yet. Qt's 'QCRHITexture "
        "*QCPainterRhiRenderer::renderUpdateNativeTexture(QRhiTexture "
        "*oldTexture, QRhiTexture *texture)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def renderUpdateTexture(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterRhiRenderer::renderUpdateTexture(int image, int x,
    int y, int w, int h, const uchar *data)': leans on
    'QCPainterRhiRenderer::findTexture(int) const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.renderUpdateTexture' has no cute function "
        "yet. Qt's 'bool QCPainterRhiRenderer::renderUpdateTexture(int "
        "image, int x, int y, int w, int h, const uchar *data)': leans on "
        "'QCPainterRhiRenderer::findTexture(int) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def resetForNewFrame(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::resetForNewFrame()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.resetForNewFrame' has no cute function yet. "
        "Qt's 'void QCPainterRhiRenderer::resetForNewFrame()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def resetForPass(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::resetForPass()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.resetForPass' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::resetForPass()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def resourceUpdateBatch(*__, **_) -> Never:
    """
    Qt's 'QRhiResourceUpdateBatch
    *QCPainterRhiRenderer::resourceUpdateBatch()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.resourceUpdateBatch' has no cute function "
        "yet. Qt's 'QRhiResourceUpdateBatch "
        "*QCPainterRhiRenderer::resourceUpdateBatch()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def sampler(*__, **_) -> Never:
    """
    Qt's 'QRhiSampler *QCPainterRhiRenderer::sampler(const QCRHISamplerDesc
    &samplerDescription)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: field has incomplete
    type 'QCRHISamplerDesc'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.sampler' has no cute function yet. Qt's "
        "'QRhiSampler *QCPainterRhiRenderer::sampler(const QCRHISamplerDesc "
        "&samplerDescription)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: field "
        "has incomplete type 'QCRHISamplerDesc'.")

  @staticmethod
  def setFlag(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::setFlag(RenderFlags flag, bool enable)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.setFlag' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::setFlag(RenderFlags flag, bool "
        "enable)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QCRHIContext'.")

  @staticmethod
  def setViewport(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::setViewport(float x, float y, float
    width, float height)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.setViewport' has no cute function yet. Qt's "
        "'void QCPainterRhiRenderer::setViewport(float x, float y, float "
        "width, float height)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QCRHIContext'.")

  @staticmethod
  def syncDebugCounters(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::syncDebugCounters()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.syncDebugCounters' has no cute function yet. "
        "Qt's 'void QCPainterRhiRenderer::syncDebugCounters()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def testFlag(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterRhiRenderer::testFlag(RenderFlag flag) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.testFlag' has no cute function yet. Qt's "
        "'bool QCPainterRhiRenderer::testFlag(RenderFlag flag) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QCRHIContext'.")

  @staticmethod
  def textureFormatInfo(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::textureFormatInfo(QRhiTexture::Format
    format, QSize size, quint32 *bpl, quint32 *byteSize, quint32
    *bytesPerPixel)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.textureFormatInfo' has no cute function yet. "
        "Qt's 'void "
        "QCPainterRhiRenderer::textureFormatInfo(QRhiTexture::Format "
        "format, QSize size, quint32 *bpl, quint32 *byteSize, quint32 "
        "*bytesPerPixel)': takes a number to change where it is.")

  @staticmethod
  def transferFillGeom(*__, **_) -> Never:
    """
    Qt's 'int QCPainterRhiRenderer::transferFillGeom(QCRHICall *call, int
    vertexCount, const QCVertex *vertices, int indexCount, int pathCount,
    const QCPath *pathInfos)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: member access into
    incomplete type 'QCRHICall'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.transferFillGeom' has no cute function yet. "
        "Qt's 'int QCPainterRhiRenderer::transferFillGeom(QCRHICall *call, "
        "int vertexCount, const QCVertex *vertices, int indexCount, int "
        "pathCount, const QCPath *pathInfos)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QCRHICall'.")

  @staticmethod
  def transferPathsFromCachedPathGroup(*__, **_) -> Never:
    """
    Qt's 'void
    QCPainterRhiRenderer::transferPathsFromCachedPathGroup(QCRHICall *call,
    int pathCount, const QCRHIPath *paths)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QCRHICall'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.transferPathsFromCachedPathGroup' has no "
        "cute function yet. Qt's 'void "
        "QCPainterRhiRenderer::transferPathsFromCachedPathGroup(QCRHICall "
        "*call, int pathCount, const QCRHIPath *paths)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QCRHICall'.")

  @staticmethod
  def transferStrokeGeom(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::transferStrokeGeom(QCRHICall *call, int
    vertexCount, const QCVertex *vertices, int pathCount, const QCPath
    *pathInfos)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QCRHICall'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.transferStrokeGeom' has no cute function "
        "yet. Qt's 'void QCPainterRhiRenderer::transferStrokeGeom(QCRHICall "
        "*call, int vertexCount, const QCVertex *vertices, int pathCount, "
        "const QCPath *pathInfos)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QCRHICall'.")

  @staticmethod
  def uniformPtr(*__, **_) -> Never:
    """
    Qt's 'QCRHICommonUniforms *QCPainterRhiRenderer::uniformPtr(int i)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.uniformPtr' has no cute function yet. Qt's "
        "'QCRHICommonUniforms *QCPainterRhiRenderer::uniformPtr(int i) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QCRHIContext'.")

  @staticmethod
  def updateVertUniforms(*__, **_) -> Never:
    """
    Qt's 'void QCPainterRhiRenderer::updateVertUniforms(QCRHICall *call,
    const QTransform &transform)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'QCRHIContext'.
    """
    raise NotImplementedError(
        "'QCPainterRhiRenderer.updateVertUniforms' has no cute function "
        "yet. Qt's 'void QCPainterRhiRenderer::updateVertUniforms(QCRHICall "
        "*call, const QTransform &transform)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QCRHIContext'.")
