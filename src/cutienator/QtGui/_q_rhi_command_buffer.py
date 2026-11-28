"""
QRhiCommandBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from . import QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QSize
  from . import QColor, QRhiBuffer, QRhiComputePipeline
  from . import QRhiDepthStencilClearValue, QRhiGraphicsPipeline
  from . import QRhiImplementation, QRhiNativeHandles, QRhiRenderTarget
  from . import QRhiResourceUpdateBatch, QRhiScissor, QRhiViewport
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QRhiBuffer = WAIT['QRhiBuffer']
  QRhiComputePipeline = WAIT['QRhiComputePipeline']
  QRhiDepthStencilClearValue = WAIT['QRhiDepthStencilClearValue']
  QRhiGraphicsPipeline = WAIT['QRhiGraphicsPipeline']
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiScissor = WAIT['QRhiScissor']
  QRhiViewport = WAIT['QRhiViewport']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiCommandBuffer(QRhiResource):
  """
  The cute side of Qt's QRhiCommandBuffer: a plain Python object standing in
  front of one C++ QRhiCommandBuffer.

  It is built on the cute 'QRhiResource', as Qt's QRhiCommandBuffer is built
  on Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiCommandBuffer that has a ritual and that Python
  can call so far, 25 names in all: 'resourceType', 'resourceUpdate',
  'beginPass', 'endPass', 'setGraphicsPipeline', 'setViewport', 'setScissor',
  'setBlendConstants', 'setStencilRef', 'setShadingRate', 'draw',
  'drawIndexed', 'drawIndirect', 'drawIndexedIndirect', 'debugMarkBegin',
  'debugMarkEnd', 'debugMarkMsg', 'beginComputePass', 'endComputePass',
  'setComputePipeline', 'dispatch', 'nativeHandles', 'beginExternal',
  'endExternal', 'lastCompletedGpuTime'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QRhiCommandBuffer::setShaderResources(QRhiShaderResourceBindings *srb,
    int dynamicOffsetCount, const DynamicOffset *dynamicOffsets)': names
    'QRhiCommandBuffer::DynamicOffset', which has no cute class yet.
  - Qt's 'void QRhiCommandBuffer::setVertexInput(int startBinding, int
    bindingCount, const VertexInput *bindings, QRhiBuffer *indexBuf, quint32
    indexOffset, IndexFormat indexFormat)': names
    'QRhiCommandBuffer::VertexInput', which has no cute class yet.

  What to expect
  --------------

  - The C++ QRhiCommandBuffer is created at the first use, not by
    'QRhiCommandBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiCommandBuffer.
  - Each name of Qt's QRhiCommandBuffer that has no cute function yet,
    'setShaderResources', 'setVertexInput', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRhiCommandBuffer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BeginPassFlag(CuteFlags):
    """
    The flags enum 'QRhiCommandBuffer::BeginPassFlag' of Qt, with the 2 names
    Qt gives in it. Qt names the type of its combinations
    'QRhiCommandBuffer::BeginPassFlags'.
    """

    ExternalContent = 0x1
    DoNotTrackResourcesForCompute = 0x2

  BeginPassFlags = BeginPassFlag

  class IndexFormat(CuteNum):
    """
    The enum 'QRhiCommandBuffer::IndexFormat' of Qt, with the 2 names Qt
    gives in it.
    """

    IndexUInt16 = Kee[int](0)
    IndexUInt32 = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiCommandBuffer'

  #  A C++ QRhiCommandBuffer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiCommandBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiCommandBuffer::resourceType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiCommandBuffer::resourceType() const
    ritual = 'ritual_ZNK17QRhiCommandBuffer12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QRhiCommandBuffer12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiGraphicsPipeline)
  @overload(NoneType)
  def setGraphicsPipeline(self, ps: Optional[QRhiGraphicsPipeline]) -> None:
    """
    Calls Qt's 'void
    QRhiCommandBuffer::setGraphicsPipeline(QRhiGraphicsPipeline *ps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#setGraphicsPipeline

    Parameters
    ----------

    ps : Optional[QRhiGraphicsPipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiCommandBuffer::setGraphicsPipeline(QRhiGraphicsPipeline *ps)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer19setGraphicsPipelineEP20QRhiGraphicsP'
        'ipeline',
        self._addressOf(ps),
    )

  @overload(QRhiViewport)
  def setViewport(self, viewport: QRhiViewport) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::setViewport(const QRhiViewport
    &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicommandbuffer.html#setViewport

    Parameters
    ----------

    viewport : QRhiViewport
      Passed on as a value: Qt reads the C++ QRhiViewport, which stays
      Python's own.
    """
    #  void QRhiCommandBuffer::setViewport(const QRhiViewport &viewport)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer11setViewportERK12QRhiViewport',
        self._valueOf(viewport),
    )

  @overload(QRhiScissor)
  def setScissor(self, scissor: QRhiScissor) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::setScissor(const QRhiScissor
    &scissor)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicommandbuffer.html#setScissor

    Parameters
    ----------

    scissor : QRhiScissor
      Passed on as a value: Qt reads the C++ QRhiScissor, which stays
      Python's own.
    """
    #  void QRhiCommandBuffer::setScissor(const QRhiScissor &scissor)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer10setScissorERK11QRhiScissor',
        self._valueOf(scissor),
    )

  @overload(QColor)
  def setBlendConstants(self, c: QColor) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::setBlendConstants(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#setBlendConstants

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QRhiCommandBuffer::setBlendConstants(const QColor &c)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer17setBlendConstantsERK6QColor',
        self._valueOf(c),
    )

  @overload(int)
  def setStencilRef(self, refValue: int) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::setStencilRef(quint32 refValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#setStencilRef

    Parameters
    ----------

    refValue : int
      Passed on as it is.
    """
    #  void QRhiCommandBuffer::setStencilRef(quint32 refValue)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer13setStencilRefEj', refValue,
    )

  @overload(QSize)
  def setShadingRate(self, coarsePixelSize: QSize) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::setShadingRate(const QSize
    &coarsePixelSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#setShadingRate

    Parameters
    ----------

    coarsePixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiCommandBuffer::setShadingRate(const QSize &coarsePixelSize)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer14setShadingRateERK5QSize',
        self._valueOf(coarsePixelSize),
    )

  @overload(QRhiComputePipeline)
  @overload(NoneType)
  def setComputePipeline(self, ps: Optional[QRhiComputePipeline]) -> None:
    """
    Calls Qt's 'void
    QRhiCommandBuffer::setComputePipeline(QRhiComputePipeline *ps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#setComputePipeline

    Parameters
    ----------

    ps : Optional[QRhiComputePipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiCommandBuffer::setComputePipeline(QRhiComputePipeline *ps)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer18setComputePipelineEP19QRhiComputePip'
        'eline',
        self._addressOf(ps),
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

  @overload(QRhiImplementation)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhiImplementation]) -> None:
    """
    Notes what was given, for Qt's
    'QRhiCommandBuffer::QRhiCommandBuffer(QRhiImplementation *rhi)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#QRhiCommandBuffer

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiCommandBuffer::QRhiCommandBuffer(QRhiImplementation *rhi)
    self._noteCreation(QRhiCommandBuffer, lambda: Rituals.call(
        'ritual_ZN17QRhiCommandBufferC1EP18QRhiImplementation',
        self._addressOf(rhi),
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

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def resourceUpdate(
      self,
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void
    QRhiCommandBuffer::resourceUpdate(QRhiResourceUpdateBatch
    *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#resourceUpdate

    Parameters
    ----------

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiCommandBuffer::resourceUpdate(QRhiResourceUpdateBatch
    #      *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer14resourceUpdateEP23QRhiResourceUpdate'
        'Batch',
        self._addressOf(resourceUpdates),
    )

  @overload(QRhiRenderTarget, QColor, QRhiDepthStencilClearValue)
  @overload(NoneType, QColor, QRhiDepthStencilClearValue)
  @overload(
      QRhiRenderTarget, QColor, QRhiDepthStencilClearValue,
      QRhiResourceUpdateBatch,
  )
  @overload(QRhiRenderTarget, QColor, QRhiDepthStencilClearValue, NoneType)
  @overload(
      NoneType, QColor, QRhiDepthStencilClearValue, QRhiResourceUpdateBatch,
  )
  @overload(NoneType, QColor, QRhiDepthStencilClearValue, NoneType)
  @overload(
      QRhiRenderTarget, QColor, QRhiDepthStencilClearValue,
      QRhiResourceUpdateBatch, BeginPassFlags,
  )
  @overload(
      QRhiRenderTarget, QColor, QRhiDepthStencilClearValue, NoneType,
      BeginPassFlags,
  )
  @overload(
      NoneType, QColor, QRhiDepthStencilClearValue, QRhiResourceUpdateBatch,
      BeginPassFlags,
  )
  @overload(
      NoneType, QColor, QRhiDepthStencilClearValue, NoneType, BeginPassFlags,
  )
  def beginPass(
      self,
      rt: Optional[QRhiRenderTarget],
      colorClearValue: QColor,
      depthStencilClearValue: QRhiDepthStencilClearValue,
      resourceUpdates: Optional[QRhiResourceUpdateBatch] = None,
      flags: BeginPassFlags = BeginPassFlags(),
  ) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::beginPass(QRhiRenderTarget *rt, const
    QColor &colorClearValue, const QRhiDepthStencilClearValue
    &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
    BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicommandbuffer.html#beginPass

    Parameters
    ----------

    rt : Optional[QRhiRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    colorClearValue : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    depthStencilClearValue : QRhiDepthStencilClearValue
      Passed on as a value: Qt reads the C++ QRhiDepthStencilClearValue,
      which stays Python's own.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : BeginPassFlags
      Passed on as its number. May be left out, as in Qt: it is then
      BeginPassFlags().
    """
    #  void QRhiCommandBuffer::beginPass(QRhiRenderTarget *rt, const QColor
    #      &colorClearValue, const QRhiDepthStencilClearValue
    #      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
    #      BeginPassFlags flags)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer9beginPassEP16QRhiRenderTargetRK6QColo'
        'rRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsIN'
        'S_13BeginPassFlagEE',
        self._addressOf(rt), self._valueOf(colorClearValue),
        self._valueOf(depthStencilClearValue),
        self._addressOf(resourceUpdates), flags.value,
    )

  @overload()
  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def endPass(
      self,
      resourceUpdates: Optional[QRhiResourceUpdateBatch] = None,
  ) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::endPass(QRhiResourceUpdateBatch
    *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicommandbuffer.html#endPass

    Parameters
    ----------

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QRhiCommandBuffer::endPass(QRhiResourceUpdateBatch
    #      *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer7endPassEP23QRhiResourceUpdateBatch',
        self._addressOf(resourceUpdates),
    )

  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  @overload(int, int, int, int)
  def draw(
      self,
      vertexCount: int,
      instanceCount: int = 1,
      firstVertex: int = 0,
      firstInstance: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::draw(quint32 vertexCount, quint32
    instanceCount, quint32 firstVertex, quint32 firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicommandbuffer.html#draw

    Parameters
    ----------

    vertexCount : int
      Passed on as it is.

    instanceCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    firstVertex : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    firstInstance : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QRhiCommandBuffer::draw(quint32 vertexCount, quint32
    #      instanceCount, quint32 firstVertex, quint32 firstInstance)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer4drawEjjjj',
        vertexCount, instanceCount, firstVertex, firstInstance,
    )

  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  @overload(int, int, int, int)
  @overload(int, int, int, int, int)
  def drawIndexed(
      self,
      indexCount: int,
      instanceCount: int = 1,
      firstIndex: int = 0,
      vertexOffset: int = 0,
      firstInstance: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::drawIndexed(quint32 indexCount,
    quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset, quint32
    firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicommandbuffer.html#drawIndexed

    Parameters
    ----------

    indexCount : int
      Passed on as it is.

    instanceCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    firstIndex : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    vertexOffset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    firstInstance : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QRhiCommandBuffer::drawIndexed(quint32 indexCount, quint32
    #      instanceCount, quint32 firstIndex, qint32 vertexOffset, quint32
    #      firstInstance)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer11drawIndexedEjjjij',
        indexCount, instanceCount, firstIndex, vertexOffset, firstInstance,
    )

  @overload(QRhiBuffer, int, int, int)
  @overload(NoneType, int, int, int)
  def drawIndirect(
      self,
      indirectBuffer: Optional[QRhiBuffer],
      indirectBufferOffset: int,
      drawCount: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::drawIndirect(QRhiBuffer
    *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount, quint32
    stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#drawIndirect

    Parameters
    ----------

    indirectBuffer : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indirectBufferOffset : int
      Passed on as it is.

    drawCount : int
      Passed on as it is.

    stride : int
      Passed on as it is.
    """
    #  void QRhiCommandBuffer::drawIndirect(QRhiBuffer *indirectBuffer,
    #      quint32 indirectBufferOffset, quint32 drawCount, quint32 stride)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer12drawIndirectEP10QRhiBufferjjj',
        self._addressOf(indirectBuffer), indirectBufferOffset, drawCount,
        stride,
    )

  @overload(QRhiBuffer, int, int, int)
  @overload(NoneType, int, int, int)
  def drawIndexedIndirect(
      self,
      indirectBuffer: Optional[QRhiBuffer],
      indirectBufferOffset: int,
      drawCount: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::drawIndexedIndirect(QRhiBuffer
    *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount, quint32
    stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#drawIndexedIndirect

    Parameters
    ----------

    indirectBuffer : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indirectBufferOffset : int
      Passed on as it is.

    drawCount : int
      Passed on as it is.

    stride : int
      Passed on as it is.
    """
    #  void QRhiCommandBuffer::drawIndexedIndirect(QRhiBuffer
    #      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
    #      quint32 stride)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer19drawIndexedIndirectEP10QRhiBufferjjj',
        self._addressOf(indirectBuffer), indirectBufferOffset, drawCount,
        stride,
    )

  @overload(QByteArray)
  def debugMarkBegin(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::debugMarkBegin(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#debugMarkBegin

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiCommandBuffer::debugMarkBegin(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer14debugMarkBeginERK10QByteArray',
        self._valueOf(name),
    )

  def debugMarkEnd(self) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::debugMarkEnd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#debugMarkEnd
    """
    #  void QRhiCommandBuffer::debugMarkEnd()
    self.uglySide.call('ritual_ZN17QRhiCommandBuffer12debugMarkEndEv')

  @overload(QByteArray)
  def debugMarkMsg(self, msg: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::debugMarkMsg(const QByteArray &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#debugMarkMsg

    Parameters
    ----------

    msg : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiCommandBuffer::debugMarkMsg(const QByteArray &msg)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer12debugMarkMsgERK10QByteArray',
        self._valueOf(msg),
    )

  @overload()
  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  @overload(QRhiResourceUpdateBatch, BeginPassFlags)
  @overload(NoneType, BeginPassFlags)
  def beginComputePass(
      self,
      resourceUpdates: Optional[QRhiResourceUpdateBatch] = None,
      flags: BeginPassFlags = BeginPassFlags(),
  ) -> None:
    """
    Calls Qt's 'void
    QRhiCommandBuffer::beginComputePass(QRhiResourceUpdateBatch
    *resourceUpdates, BeginPassFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#beginComputePass

    Parameters
    ----------

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : BeginPassFlags
      Passed on as its number. May be left out, as in Qt: it is then
      BeginPassFlags().
    """
    #  void QRhiCommandBuffer::beginComputePass(QRhiResourceUpdateBatch
    #      *resourceUpdates, BeginPassFlags flags)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer16beginComputePassEP23QRhiResourceUpda'
        'teBatch6QFlagsINS_13BeginPassFlagEE',
        self._addressOf(resourceUpdates), flags.value,
    )

  @overload()
  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def endComputePass(
      self,
      resourceUpdates: Optional[QRhiResourceUpdateBatch] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QRhiCommandBuffer::endComputePass(QRhiResourceUpdateBatch
    *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#endComputePass

    Parameters
    ----------

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QRhiCommandBuffer::endComputePass(QRhiResourceUpdateBatch
    #      *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer14endComputePassEP23QRhiResourceUpdate'
        'Batch',
        self._addressOf(resourceUpdates),
    )

  @overload(int, int, int)
  def dispatch(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::dispatch(int x, int y, int z)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicommandbuffer.html#dispatch

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QRhiCommandBuffer::dispatch(int x, int y, int z)
    self.uglySide.call('ritual_ZN17QRhiCommandBuffer8dispatchEiii', x, y, z)

  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles *QRhiCommandBuffer::nativeHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhiCommandBuffer::nativeHandles()
    address = self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer13nativeHandlesEv',
    )
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  def beginExternal(self) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::beginExternal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#beginExternal
    """
    #  void QRhiCommandBuffer::beginExternal()
    self.uglySide.call('ritual_ZN17QRhiCommandBuffer13beginExternalEv')

  def endExternal(self) -> None:
    """
    Calls Qt's 'void QRhiCommandBuffer::endExternal()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicommandbuffer.html#endExternal
    """
    #  void QRhiCommandBuffer::endExternal()
    self.uglySide.call('ritual_ZN17QRhiCommandBuffer11endExternalEv')

  def lastCompletedGpuTime(self) -> float:
    """
    Calls Qt's 'double QRhiCommandBuffer::lastCompletedGpuTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicommandbuffer.html#lastCompletedGpuTime
    """
    #  double QRhiCommandBuffer::lastCompletedGpuTime()
    return self.uglySide.call(
        'ritual_ZN17QRhiCommandBuffer20lastCompletedGpuTimeEv',
    )

  @staticmethod
  def setShaderResources(*__, **_) -> Never:
    """
    Qt's 'void
    QRhiCommandBuffer::setShaderResources(QRhiShaderResourceBindings *srb,
    int dynamicOffsetCount, const DynamicOffset *dynamicOffsets)': names
    'QRhiCommandBuffer::DynamicOffset', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiCommandBuffer.setShaderResources' has no cute function yet. "
        "Qt's 'void "
        "QRhiCommandBuffer::setShaderResources(QRhiShaderResourceBindings "
        "*srb, int dynamicOffsetCount, const DynamicOffset "
        "*dynamicOffsets)': names 'QRhiCommandBuffer::DynamicOffset', which "
        "has no cute class yet.")

  @staticmethod
  def setVertexInput(*__, **_) -> Never:
    """
    Qt's 'void QRhiCommandBuffer::setVertexInput(int startBinding, int
    bindingCount, const VertexInput *bindings, QRhiBuffer *indexBuf, quint32
    indexOffset, IndexFormat indexFormat)': names
    'QRhiCommandBuffer::VertexInput', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiCommandBuffer.setVertexInput' has no cute function yet. Qt's "
        "'void QRhiCommandBuffer::setVertexInput(int startBinding, int "
        "bindingCount, const VertexInput *bindings, QRhiBuffer *indexBuf, "
        "quint32 indexOffset, IndexFormat indexFormat)': names "
        "'QRhiCommandBuffer::VertexInput', which has no cute class yet.")
