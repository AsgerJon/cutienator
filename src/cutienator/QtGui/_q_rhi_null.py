"""
QRhiNull binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QRhiNull to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QRhi, QRhiBuffer, QRhiCommandBuffer, QRhiImplementation
from . import QRhiRenderBuffer, QRhiResourceUpdateBatchPrivate, QRhiSampler
from . import QRhiTexture, QRhiTextureRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QSize
  from . import QColor, QMatrix4x4, QRhiComputePipeline
  from . import QRhiDepthStencilClearValue, QRhiDriverInfo
  from . import QRhiGraphicsPipeline, QRhiNativeHandles, QRhiNullInitParams
  from . import QRhiRenderTarget, QRhiResourceUpdateBatch, QRhiScissor
  from . import QRhiShaderResourceBindings, QRhiShadingRateMap, QRhiStats
  from . import QRhiSwapChain, QRhiTextureRenderTargetDescription
  from . import QRhiViewport
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QRhiComputePipeline = WAIT['QRhiComputePipeline']
  QRhiDepthStencilClearValue = WAIT['QRhiDepthStencilClearValue']
  QRhiGraphicsPipeline = WAIT['QRhiGraphicsPipeline']
  QRhiNativeHandles = WAIT['QRhiNativeHandles']
  QRhiNullInitParams = WAIT['QRhiNullInitParams']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiScissor = WAIT['QRhiScissor']
  QRhiSwapChain = WAIT['QRhiSwapChain']
  QRhiTextureRenderTargetDescription = WAIT['QRhiTextureRenderTargetDescription']
  QRhiViewport = WAIT['QRhiViewport']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiNull(QRhiImplementation):
  """
  The cute side of Qt's QRhiNull: a plain Python object standing in front of
  one C++ QRhiNull.

  It is built on the cute 'QRhiImplementation', as Qt's QRhiNull is built on
  Qt's QRhiImplementation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiNull that has a ritual and that Python can call
  so far, 59 names in all: 'create', 'destroy', 'createGraphicsPipeline',
  'createComputePipeline', 'createShaderResourceBindings', 'createBuffer',
  'createRenderBuffer', 'createTexture', 'createSampler',
  'createTextureRenderTarget', 'createShadingRateMap', 'createSwapChain',
  'endFrame', 'endOffscreenFrame', 'finish', 'resourceUpdate', 'beginPass',
  'endPass', 'setGraphicsPipeline', 'setViewport', 'setScissor',
  'setBlendConstants', 'setStencilRef', 'setShadingRate', 'draw',
  'drawIndexed', 'drawIndirect', 'drawIndexedIndirect', 'debugMarkBegin',
  'debugMarkEnd', 'debugMarkMsg', 'beginComputePass', 'endComputePass',
  'setComputePipeline', 'dispatch', 'nativeHandles', 'beginExternal',
  'endExternal', 'lastCompletedGpuTime', 'supportedShadingRates',
  'ubufAlignment', 'isYUpInFramebuffer', 'isYUpInNDC',
  'isClipDepthZeroToOne', 'clipSpaceCorrMatrix', 'isTextureFormatSupported',
  'isFeatureSupported', 'resourceLimit', 'driverInfo', 'statistics',
  'makeThreadLocalNativeContextCurrent', 'setQueueSubmitParams',
  'releaseCachedResources', 'isDeviceLost', 'pipelineCacheData',
  'setPipelineCacheData', 'simulateTextureUpload', 'simulateTextureCopy',
  'simulateTextureGenMips'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhi::FrameOpResult QRhiNull::beginFrame(QRhiSwapChain *swapChain,
    QRhi::BeginFrameFlags flags)': names the enum 'QRhi::BeginFrameFlag',
    whose class cannot be named here.
  - Qt's 'QRhi::FrameOpResult QRhiNull::beginOffscreenFrame(QRhiCommandBuffer
    **cb, QRhi::BeginFrameFlags flags)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QRhiNull::setShaderResources(QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb, int dynamicOffsetCount, const
    QRhiCommandBuffer::DynamicOffset *dynamicOffsets)': names
    'QRhiCommandBuffer::DynamicOffset', which has no cute class yet.
  - Qt's 'void QRhiNull::setVertexInput(QRhiCommandBuffer *cb, int
    startBinding, int bindingCount, const QRhiCommandBuffer::VertexInput
    *bindings, QRhiBuffer *indexBuf, quint32 indexOffset,
    QRhiCommandBuffer::IndexFormat indexFormat)': names
    'QRhiCommandBuffer::VertexInput', which has no cute class yet.
  - Qt's 'QList<int> QRhiNull::supportedSampleCounts() const': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ QRhiNull is created at the first use, not by 'QRhiNull(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiNull.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiNull'

  #  A C++ QRhiNull Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiNull'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def supportedShadingRates(self, sampleCount: int) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QRhiNull::supportedShadingRates(int sampleCount)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#supportedShadingRates

    Parameters
    ----------

    sampleCount : int
      Passed on as it is.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QRhiNull::supportedShadingRates(int sampleCount) const
    address = self.uglySide.call(
        'ritual_ZNK8QRhiNull21supportedShadingRatesEi', sampleCount,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  def ubufAlignment(self) -> int:
    """
    Calls Qt's 'int QRhiNull::ubufAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#ubufAlignment
    """
    #  int QRhiNull::ubufAlignment() const
    ritual = 'ritual_ZNK8QRhiNull13ubufAlignmentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QRhiNull13ubufAlignmentEv'
    return self.uglySide.call(ritual)

  def isYUpInFramebuffer(self) -> bool:
    """
    Calls Qt's 'bool QRhiNull::isYUpInFramebuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#isYUpInFramebuffer
    """
    #  bool QRhiNull::isYUpInFramebuffer() const
    ritual = 'ritual_ZNK8QRhiNull18isYUpInFramebufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QRhiNull18isYUpInFramebufferEv'
    return self.uglySide.call(ritual)

  def isYUpInNDC(self) -> bool:
    """
    Calls Qt's 'bool QRhiNull::isYUpInNDC() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#isYUpInNDC
    """
    #  bool QRhiNull::isYUpInNDC() const
    ritual = 'ritual_ZNK8QRhiNull10isYUpInNDCEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QRhiNull10isYUpInNDCEv'
    return self.uglySide.call(ritual)

  def isClipDepthZeroToOne(self) -> bool:
    """
    Calls Qt's 'bool QRhiNull::isClipDepthZeroToOne() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#isClipDepthZeroToOne
    """
    #  bool QRhiNull::isClipDepthZeroToOne() const
    ritual = 'ritual_ZNK8QRhiNull20isClipDepthZeroToOneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QRhiNull20isClipDepthZeroToOneEv'
    return self.uglySide.call(ritual)

  def clipSpaceCorrMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QRhiNull::clipSpaceCorrMatrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#clipSpaceCorrMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QRhiNull::clipSpaceCorrMatrix() const
    ritual = 'ritual_ZNK8QRhiNull19clipSpaceCorrMatrixEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QRhiNull19clipSpaceCorrMatrixEv'
    address = self.uglySide.call(ritual)
    from . import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QRhiTexture.Format, QRhiTexture.Flags)
  def isTextureFormatSupported(
      self,
      format: QRhiTexture.Format,
      flags: QRhiTexture.Flags,
  ) -> bool:
    """
    Calls Qt's 'bool QRhiNull::isTextureFormatSupported(QRhiTexture::Format
    format, QRhiTexture::Flags flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#isTextureFormatSupported

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    flags : QRhiTexture.Flags
      Passed on as its number.
    """
    #  bool QRhiNull::isTextureFormatSupported(QRhiTexture::Format format,
    #      QRhiTexture::Flags flags) const
    ritual = (
        'ritual_ZNK8QRhiNull24isTextureFormatSupportedEN11QRhiTexture6Forma'
        'tE6QFlagsINS0_4FlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QRhiNull24isTextureFormatSupportedEN11QRhiTexture'
          '6FormatE6QFlagsINS0_4FlagEE')
    return self.uglySide.call(ritual, format.value, flags.value)

  @overload(QRhi.Feature)
  def isFeatureSupported(self, feature: QRhi.Feature) -> bool:
    """
    Calls Qt's 'bool QRhiNull::isFeatureSupported(QRhi::Feature feature)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#isFeatureSupported

    Parameters
    ----------

    feature : QRhi.Feature
      Passed on as its number.
    """
    #  bool QRhiNull::isFeatureSupported(QRhi::Feature feature) const
    ritual = 'ritual_ZNK8QRhiNull18isFeatureSupportedEN4QRhi7FeatureE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QRhiNull18isFeatureSupportedEN4QRhi7FeatureE'
    return self.uglySide.call(ritual, feature.value)

  @overload(QRhi.ResourceLimit)
  def resourceLimit(self, limit: QRhi.ResourceLimit) -> int:
    """
    Calls Qt's 'int QRhiNull::resourceLimit(QRhi::ResourceLimit limit)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#resourceLimit

    Parameters
    ----------

    limit : QRhi.ResourceLimit
      Passed on as its number.
    """
    #  int QRhiNull::resourceLimit(QRhi::ResourceLimit limit) const
    ritual = 'ritual_ZNK8QRhiNull13resourceLimitEN4QRhi13ResourceLimitE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QRhiNull13resourceLimitEN4QRhi13ResourceLimitE')
    return self.uglySide.call(ritual, limit.value)

  def driverInfo(self) -> QRhiDriverInfo:
    """
    Calls Qt's 'QRhiDriverInfo QRhiNull::driverInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#driverInfo

    Returns
    -------

    QRhiDriverInfo
      A new cute QRhiDriverInfo around the copy Qt gave back. Python owns it.
    """
    #  QRhiDriverInfo QRhiNull::driverInfo() const
    ritual = 'ritual_ZNK8QRhiNull10driverInfoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QRhiNull10driverInfoEv'
    address = self.uglySide.call(ritual)
    from . import QRhiDriverInfo
    return QRhiDriverInfo._cuteOwning(address)

  def isDeviceLost(self) -> bool:
    """
    Calls Qt's 'bool QRhiNull::isDeviceLost() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#isDeviceLost
    """
    #  bool QRhiNull::isDeviceLost() const
    ritual = 'ritual_ZNK8QRhiNull12isDeviceLostEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QRhiNull12isDeviceLostEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiCommandBuffer, QRhiGraphicsPipeline)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiGraphicsPipeline)
  @overload(NoneType, NoneType)
  def setGraphicsPipeline(
      self,
      cb: Optional[QRhiCommandBuffer],
      ps: Optional[QRhiGraphicsPipeline],
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::setGraphicsPipeline(QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#setGraphicsPipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiGraphicsPipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiNull::setGraphicsPipeline(QRhiCommandBuffer *cb,
    #      QRhiGraphicsPipeline *ps)
    ritual = (
        'ritual_ZN8QRhiNull19setGraphicsPipelineEP17QRhiCommandBufferP20QRh'
        'iGraphicsPipeline')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull19setGraphicsPipelineEP17QRhiCommandBuffer'
          'P20QRhiGraphicsPipeline')
    self.uglySide.call(ritual, self._addressOf(cb), self._addressOf(ps))

  @overload(QRhiCommandBuffer, QRhiViewport)
  @overload(NoneType, QRhiViewport)
  def setViewport(
      self,
      cb: Optional[QRhiCommandBuffer],
      viewport: QRhiViewport,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::setViewport(QRhiCommandBuffer *cb, const
    QRhiViewport &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#setViewport

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewport : QRhiViewport
      Passed on as a value: Qt reads the C++ QRhiViewport, which stays
      Python's own.
    """
    #  void QRhiNull::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
    #      &viewport)
    ritual = (
        'ritual_ZN8QRhiNull11setViewportEP17QRhiCommandBufferRK12QRhiViewpo'
        'rt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull11setViewportEP17QRhiCommandBufferRK12QRhi'
          'Viewport')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(viewport))

  @overload(QRhiCommandBuffer, QRhiScissor)
  @overload(NoneType, QRhiScissor)
  def setScissor(
      self,
      cb: Optional[QRhiCommandBuffer],
      scissor: QRhiScissor,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::setScissor(QRhiCommandBuffer *cb, const
    QRhiScissor &scissor)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#setScissor

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scissor : QRhiScissor
      Passed on as a value: Qt reads the C++ QRhiScissor, which stays
      Python's own.
    """
    #  void QRhiNull::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
    #      &scissor)
    ritual = (
        'ritual_ZN8QRhiNull10setScissorEP17QRhiCommandBufferRK11QRhiScissor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull10setScissorEP17QRhiCommandBufferRK11QRhiS'
          'cissor')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(scissor))

  @overload(QRhiCommandBuffer, QColor)
  @overload(NoneType, QColor)
  def setBlendConstants(
      self,
      cb: Optional[QRhiCommandBuffer],
      c: QColor,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::setBlendConstants(QRhiCommandBuffer *cb, const
    QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#setBlendConstants

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QRhiNull::setBlendConstants(QRhiCommandBuffer *cb, const QColor
    #      &c)
    ritual = (
        'ritual_ZN8QRhiNull17setBlendConstantsEP17QRhiCommandBufferRK6QColo'
        'r')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull17setBlendConstantsEP17QRhiCommandBufferRK'
          '6QColor')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(c))

  @overload(QRhiCommandBuffer, int)
  @overload(NoneType, int)
  def setStencilRef(
      self,
      cb: Optional[QRhiCommandBuffer],
      refValue: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::setStencilRef(QRhiCommandBuffer *cb, quint32
    refValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#setStencilRef

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    refValue : int
      Passed on as it is.
    """
    #  void QRhiNull::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
    ritual = 'ritual_ZN8QRhiNull13setStencilRefEP17QRhiCommandBufferj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull13setStencilRefEP17QRhiCommandBufferj'
    self.uglySide.call(ritual, self._addressOf(cb), refValue)

  @overload(QRhiCommandBuffer, QSize)
  @overload(NoneType, QSize)
  def setShadingRate(
      self,
      cb: Optional[QRhiCommandBuffer],
      coarsePixelSize: QSize,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::setShadingRate(QRhiCommandBuffer *cb, const
    QSize &coarsePixelSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#setShadingRate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coarsePixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiNull::setShadingRate(QRhiCommandBuffer *cb, const QSize
    #      &coarsePixelSize)
    ritual = (
        'ritual_ZN8QRhiNull14setShadingRateEP17QRhiCommandBufferRK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull14setShadingRateEP17QRhiCommandBufferRK5QS'
          'ize')
    self.uglySide.call(
        ritual, self._addressOf(cb), self._valueOf(coarsePixelSize),
    )

  @overload(QRhiCommandBuffer, QRhiComputePipeline)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiComputePipeline)
  @overload(NoneType, NoneType)
  def setComputePipeline(
      self,
      cb: Optional[QRhiCommandBuffer],
      ps: Optional[QRhiComputePipeline],
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::setComputePipeline(QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#setComputePipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiComputePipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiNull::setComputePipeline(QRhiCommandBuffer *cb,
    #      QRhiComputePipeline *ps)
    ritual = (
        'ritual_ZN8QRhiNull18setComputePipelineEP17QRhiCommandBufferP19QRhi'
        'ComputePipeline')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull18setComputePipelineEP17QRhiCommandBufferP'
          '19QRhiComputePipeline')
    self.uglySide.call(ritual, self._addressOf(cb), self._addressOf(ps))

  @overload(QRhiNativeHandles)
  @overload(NoneType)
  def setQueueSubmitParams(
      self,
      params: Optional[QRhiNativeHandles],
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::setQueueSubmitParams(QRhiNativeHandles
    *params)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#setQueueSubmitParams

    Parameters
    ----------

    params : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiNull::setQueueSubmitParams(QRhiNativeHandles *params)
    ritual = 'ritual_ZN8QRhiNull20setQueueSubmitParamsEP17QRhiNativeHandles'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull20setQueueSubmitParamsEP17QRhiNativeHandle'
          's')
    self.uglySide.call(ritual, self._addressOf(params))

  @overload(QByteArray)
  def setPipelineCacheData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiNull::setPipelineCacheData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#setPipelineCacheData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiNull::setPipelineCacheData(const QByteArray &data)
    ritual = 'ritual_ZN8QRhiNull20setPipelineCacheDataERK10QByteArray'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull20setPipelineCacheDataERK10QByteArray'
    self.uglySide.call(ritual, self._valueOf(data))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiNullInitParams)
  @overload(NoneType)
  def __init__(self, params: Optional[QRhiNullInitParams]) -> None:
    """
    Notes what was given, for Qt's 'QRhiNull::QRhiNull(QRhiNullInitParams
    *params)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#QRhiNull

    Parameters
    ----------

    params : Optional[QRhiNullInitParams]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiNull::QRhiNull(QRhiNullInitParams *params)
    self._noteCreation(QRhiNull, lambda: Rituals.call(
        'ritual_ZN8QRhiNullC1EP18QRhiNullInitParams',
        self._addressOf(params),
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

  @overload(QRhi.Flags)
  def create(self, flags: QRhi.Flags) -> bool:
    """
    Calls Qt's 'bool QRhiNull::create(QRhi::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#create

    Parameters
    ----------

    flags : QRhi.Flags
      Passed on as its number.
    """
    #  bool QRhiNull::create(QRhi::Flags flags)
    ritual = 'ritual_ZN8QRhiNull6createE6QFlagsIN4QRhi4FlagEE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull6createE6QFlagsIN4QRhi4FlagEE'
    return self.uglySide.call(ritual, flags.value)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QRhiNull::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#destroy
    """
    #  void QRhiNull::destroy()
    ritual = 'ritual_ZN8QRhiNull7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull7destroyEv'
    self.uglySide.call(ritual)

  def createGraphicsPipeline(self) -> Optional[QRhiGraphicsPipeline]:
    """
    Calls Qt's 'QRhiGraphicsPipeline *QRhiNull::createGraphicsPipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#createGraphicsPipeline

    Returns
    -------

    Optional[QRhiGraphicsPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiGraphicsPipeline *QRhiNull::createGraphicsPipeline()
    ritual = 'ritual_ZN8QRhiNull22createGraphicsPipelineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull22createGraphicsPipelineEv'
    address = self.uglySide.call(ritual)
    from . import QRhiGraphicsPipeline
    return QRhiGraphicsPipeline._cuteAt(address)

  def createComputePipeline(self) -> Optional[QRhiComputePipeline]:
    """
    Calls Qt's 'QRhiComputePipeline *QRhiNull::createComputePipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#createComputePipeline

    Returns
    -------

    Optional[QRhiComputePipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiComputePipeline *QRhiNull::createComputePipeline()
    ritual = 'ritual_ZN8QRhiNull21createComputePipelineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull21createComputePipelineEv'
    address = self.uglySide.call(ritual)
    from . import QRhiComputePipeline
    return QRhiComputePipeline._cuteAt(address)

  def createShaderResourceBindings(
      self,
  ) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings
    *QRhiNull::createShaderResourceBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#createShaderResourceBindings

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings *QRhiNull::createShaderResourceBindings()
    ritual = 'ritual_ZN8QRhiNull28createShaderResourceBindingsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull28createShaderResourceBindingsEv'
    address = self.uglySide.call(ritual)
    from . import QRhiShaderResourceBindings
    return QRhiShaderResourceBindings._cuteAt(address)

  @overload(QRhiBuffer.Type, QRhiBuffer.UsageFlags, int)
  def createBuffer(
      self,
      type: QRhiBuffer.Type,
      usage: QRhiBuffer.UsageFlags,
      size: int,
  ) -> Optional[QRhiBuffer]:
    """
    Calls Qt's 'QRhiBuffer *QRhiNull::createBuffer(QRhiBuffer::Type type,
    QRhiBuffer::UsageFlags usage, quint32 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#createBuffer

    Parameters
    ----------

    type : QRhiBuffer.Type
      Passed on as its number.

    usage : QRhiBuffer.UsageFlags
      Passed on as its number.

    size : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiBuffer *QRhiNull::createBuffer(QRhiBuffer::Type type,
    #      QRhiBuffer::UsageFlags usage, quint32 size)
    ritual = (
        'ritual_ZN8QRhiNull12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9U'
        'sageFlagEEj')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull12createBufferEN10QRhiBuffer4TypeE6QFlagsI'
          'NS0_9UsageFlagEEj')
    address = self.uglySide.call(ritual, type.value, usage.value, size)
    return QRhiBuffer._cuteAt(address)

  @overload(
      QRhiRenderBuffer.Type, QSize, int, QRhiRenderBuffer.Flags,
      QRhiTexture.Format,
  )
  def createRenderBuffer(
      self,
      type: QRhiRenderBuffer.Type,
      pixelSize: QSize,
      sampleCount: int,
      flags: QRhiRenderBuffer.Flags,
      backingFormatHint: QRhiTexture.Format,
  ) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer
    *QRhiNull::createRenderBuffer(QRhiRenderBuffer::Type type, const QSize
    &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
    QRhiTexture::Format backingFormatHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#createRenderBuffer

    Parameters
    ----------

    type : QRhiRenderBuffer.Type
      Passed on as its number.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is.

    flags : QRhiRenderBuffer.Flags
      Passed on as its number.

    backingFormatHint : QRhiTexture.Format
      Passed on as its number.

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer *QRhiNull::createRenderBuffer(QRhiRenderBuffer::Type
    #      type, const QSize &pixelSize, int sampleCount,
    #      QRhiRenderBuffer::Flags flags, QRhiTexture::Format
    #      backingFormatHint)
    ritual = (
        'ritual_ZN8QRhiNull18createRenderBufferEN16QRhiRenderBuffer4TypeERK'
        '5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull18createRenderBufferEN16QRhiRenderBuffer4T'
          'ypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE')
    address = self.uglySide.call(
        ritual,
        type.value, self._valueOf(pixelSize), sampleCount, flags.value,
        backingFormatHint.value,
    )
    return QRhiRenderBuffer._cuteAt(address)

  @overload(QRhiTexture.Format, QSize, int, int, int, QRhiTexture.Flags)
  def createTexture(
      self,
      format: QRhiTexture.Format,
      pixelSize: QSize,
      depth: int,
      arraySize: int,
      sampleCount: int,
      flags: QRhiTexture.Flags,
  ) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhiNull::createTexture(QRhiTexture::Format
    format, const QSize &pixelSize, int depth, int arraySize, int
    sampleCount, QRhiTexture::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#createTexture

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    depth : int
      Passed on as it is.

    arraySize : int
      Passed on as it is.

    sampleCount : int
      Passed on as it is.

    flags : QRhiTexture.Flags
      Passed on as its number.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhiNull::createTexture(QRhiTexture::Format format, const
    #      QSize &pixelSize, int depth, int arraySize, int sampleCount,
    #      QRhiTexture::Flags flags)
    ritual = (
        'ritual_ZN8QRhiNull13createTextureEN11QRhiTexture6FormatERK5QSizeii'
        'i6QFlagsINS0_4FlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull13createTextureEN11QRhiTexture6FormatERK5Q'
          'Sizeiii6QFlagsINS0_4FlagEE')
    address = self.uglySide.call(
        ritual,
        format.value, self._valueOf(pixelSize), depth, arraySize,
        sampleCount, flags.value,
    )
    return QRhiTexture._cuteAt(address)

  @overload(
      QRhiSampler.Filter, QRhiSampler.Filter, QRhiSampler.Filter,
      QRhiSampler.AddressMode, QRhiSampler.AddressMode,
      QRhiSampler.AddressMode,
  )
  def createSampler(
      self,
      magFilter: QRhiSampler.Filter,
      minFilter: QRhiSampler.Filter,
      mipmapMode: QRhiSampler.Filter,
      u: QRhiSampler.AddressMode,
      v: QRhiSampler.AddressMode,
      w: QRhiSampler.AddressMode,
  ) -> Optional[QRhiSampler]:
    """
    Calls Qt's 'QRhiSampler *QRhiNull::createSampler(QRhiSampler::Filter
    magFilter, QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#createSampler

    Parameters
    ----------

    magFilter : QRhiSampler.Filter
      Passed on as its number.

    minFilter : QRhiSampler.Filter
      Passed on as its number.

    mipmapMode : QRhiSampler.Filter
      Passed on as its number.

    u : QRhiSampler.AddressMode
      Passed on as its number.

    v : QRhiSampler.AddressMode
      Passed on as its number.

    w : QRhiSampler.AddressMode
      Passed on as its number.

    Returns
    -------

    Optional[QRhiSampler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSampler *QRhiNull::createSampler(QRhiSampler::Filter magFilter,
    #      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    #      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
    #      QRhiSampler::AddressMode w)
    ritual = (
        'ritual_ZN8QRhiNull13createSamplerEN11QRhiSampler6FilterES1_S1_NS0_'
        '11AddressModeES2_S2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull13createSamplerEN11QRhiSampler6FilterES1_S'
          '1_NS0_11AddressModeES2_S2_')
    address = self.uglySide.call(
        ritual,
        magFilter.value, minFilter.value, mipmapMode.value, u.value, v.value,
        w.value,
    )
    return QRhiSampler._cuteAt(address)

  @overload(
      QRhiTextureRenderTargetDescription, QRhiTextureRenderTarget.Flags,
  )
  def createTextureRenderTarget(
      self,
      desc: QRhiTextureRenderTargetDescription,
      flags: QRhiTextureRenderTarget.Flags,
  ) -> Optional[QRhiTextureRenderTarget]:
    """
    Calls Qt's 'QRhiTextureRenderTarget
    *QRhiNull::createTextureRenderTarget(const
    QRhiTextureRenderTargetDescription &desc, QRhiTextureRenderTarget::Flags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#createTextureRenderTarget

    Parameters
    ----------

    desc : QRhiTextureRenderTargetDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureRenderTargetDescription, which stays Python's own.

    flags : QRhiTextureRenderTarget.Flags
      Passed on as its number.

    Returns
    -------

    Optional[QRhiTextureRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTextureRenderTarget *QRhiNull::createTextureRenderTarget(const
    #      QRhiTextureRenderTargetDescription &desc,
    #      QRhiTextureRenderTarget::Flags flags)
    ritual = (
        'ritual_ZN8QRhiNull25createTextureRenderTargetERK34QRhiTextureRende'
        'rTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull25createTextureRenderTargetERK34QRhiTextur'
          'eRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagE'
          'E')
    address = self.uglySide.call(ritual, self._valueOf(desc), flags.value)
    return QRhiTextureRenderTarget._cuteAt(address)

  def createShadingRateMap(self) -> Optional[QRhiShadingRateMap]:
    """
    Calls Qt's 'QRhiShadingRateMap *QRhiNull::createShadingRateMap()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#createShadingRateMap

    Returns
    -------

    Optional[QRhiShadingRateMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShadingRateMap *QRhiNull::createShadingRateMap()
    ritual = 'ritual_ZN8QRhiNull20createShadingRateMapEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull20createShadingRateMapEv'
    address = self.uglySide.call(ritual)
    from . import QRhiShadingRateMap
    return QRhiShadingRateMap._cuteAt(address)

  def createSwapChain(self) -> Optional[QRhiSwapChain]:
    """
    Calls Qt's 'QRhiSwapChain *QRhiNull::createSwapChain()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#createSwapChain

    Returns
    -------

    Optional[QRhiSwapChain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSwapChain *QRhiNull::createSwapChain()
    ritual = 'ritual_ZN8QRhiNull15createSwapChainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull15createSwapChainEv'
    address = self.uglySide.call(ritual)
    from . import QRhiSwapChain
    return QRhiSwapChain._cuteAt(address)

  @overload(QRhiSwapChain, QRhi.EndFrameFlags)
  @overload(NoneType, QRhi.EndFrameFlags)
  def endFrame(
      self,
      swapChain: Optional[QRhiSwapChain],
      flags: QRhi.EndFrameFlags,
  ) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult QRhiNull::endFrame(QRhiSwapChain
    *swapChain, QRhi::EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#endFrame

    Parameters
    ----------

    swapChain : Optional[QRhiSwapChain]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QRhi.EndFrameFlags
      Passed on as its number.

    Returns
    -------

    QRhi.FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.FrameOpResult(number)' gives.
    """
    #  QRhi::FrameOpResult QRhiNull::endFrame(QRhiSwapChain *swapChain,
    #      QRhi::EndFrameFlags flags)
    ritual = (
        'ritual_ZN8QRhiNull8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFra'
        'meFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12'
          'EndFrameFlagEE')
    return QRhi.FrameOpResult(self.uglySide.call(
        ritual, self._addressOf(swapChain), flags.value,
    ))

  @overload(QRhi.EndFrameFlags)
  def endOffscreenFrame(
      self,
      flags: QRhi.EndFrameFlags,
  ) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult
    QRhiNull::endOffscreenFrame(QRhi::EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#endOffscreenFrame

    Parameters
    ----------

    flags : QRhi.EndFrameFlags
      Passed on as its number.

    Returns
    -------

    QRhi.FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.FrameOpResult(number)' gives.
    """
    #  QRhi::FrameOpResult QRhiNull::endOffscreenFrame(QRhi::EndFrameFlags
    #      flags)
    ritual = (
        'ritual_ZN8QRhiNull17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFlag'
        'EE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull17endOffscreenFrameE6QFlagsIN4QRhi12EndFra'
          'meFlagEE')
    return QRhi.FrameOpResult(self.uglySide.call(ritual, flags.value))

  def finish(self) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult QRhiNull::finish()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#finish

    Returns
    -------

    QRhi.FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.FrameOpResult(number)' gives.
    """
    #  QRhi::FrameOpResult QRhiNull::finish()
    ritual = 'ritual_ZN8QRhiNull6finishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull6finishEv'
    return QRhi.FrameOpResult(self.uglySide.call(ritual))

  @overload(QRhiCommandBuffer, QRhiResourceUpdateBatch)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def resourceUpdate(
      self,
      cb: Optional[QRhiCommandBuffer],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::resourceUpdate(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#resourceUpdate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiNull::resourceUpdate(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    ritual = (
        'ritual_ZN8QRhiNull14resourceUpdateEP17QRhiCommandBufferP23QRhiReso'
        'urceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull14resourceUpdateEP17QRhiCommandBufferP23QR'
          'hiResourceUpdateBatch')
    self.uglySide.call(
        ritual, self._addressOf(cb), self._addressOf(resourceUpdates),
    )

  @overload(
      QRhiCommandBuffer, QRhiRenderTarget, QColor,
      QRhiDepthStencilClearValue, QRhiResourceUpdateBatch,
      QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      QRhiCommandBuffer, QRhiRenderTarget, QColor,
      QRhiDepthStencilClearValue, NoneType, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      QRhiCommandBuffer, NoneType, QColor, QRhiDepthStencilClearValue,
      QRhiResourceUpdateBatch, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      QRhiCommandBuffer, NoneType, QColor, QRhiDepthStencilClearValue,
      NoneType, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      NoneType, QRhiRenderTarget, QColor, QRhiDepthStencilClearValue,
      QRhiResourceUpdateBatch, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      NoneType, QRhiRenderTarget, QColor, QRhiDepthStencilClearValue,
      NoneType, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      NoneType, NoneType, QColor, QRhiDepthStencilClearValue,
      QRhiResourceUpdateBatch, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(
      NoneType, NoneType, QColor, QRhiDepthStencilClearValue, NoneType,
      QRhiCommandBuffer.BeginPassFlags,
  )
  def beginPass(
      self,
      cb: Optional[QRhiCommandBuffer],
      rt: Optional[QRhiRenderTarget],
      colorClearValue: QColor,
      depthStencilClearValue: QRhiDepthStencilClearValue,
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
      flags: QRhiCommandBuffer.BeginPassFlags,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::beginPass(QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt, const QColor &colorClearValue, const
    QRhiDepthStencilClearValue &depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#beginPass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

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
      object.

    flags : QRhiCommandBuffer.BeginPassFlags
      Passed on as its number.
    """
    #  void QRhiNull::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
    #      const QColor &colorClearValue, const QRhiDepthStencilClearValue
    #      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    ritual = (
        'ritual_ZN8QRhiNull9beginPassEP17QRhiCommandBufferP16QRhiRenderTarg'
        'etRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatc'
        'h6QFlagsINS0_13BeginPassFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull9beginPassEP17QRhiCommandBufferP16QRhiRend'
          'erTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUp'
          'dateBatch6QFlagsINS0_13BeginPassFlagEE')
    self.uglySide.call(
        ritual,
        self._addressOf(cb), self._addressOf(rt),
        self._valueOf(colorClearValue),
        self._valueOf(depthStencilClearValue),
        self._addressOf(resourceUpdates), flags.value,
    )

  @overload(QRhiCommandBuffer, QRhiResourceUpdateBatch)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def endPass(
      self,
      cb: Optional[QRhiCommandBuffer],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::endPass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#endPass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiNull::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
    #      *resourceUpdates)
    ritual = (
        'ritual_ZN8QRhiNull7endPassEP17QRhiCommandBufferP23QRhiResourceUpda'
        'teBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull7endPassEP17QRhiCommandBufferP23QRhiResour'
          'ceUpdateBatch')
    self.uglySide.call(
        ritual, self._addressOf(cb), self._addressOf(resourceUpdates),
    )

  @overload(QRhiCommandBuffer, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  def draw(
      self,
      cb: Optional[QRhiCommandBuffer],
      vertexCount: int,
      instanceCount: int,
      firstVertex: int,
      firstInstance: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::draw(QRhiCommandBuffer *cb, quint32
    vertexCount, quint32 instanceCount, quint32 firstVertex, quint32
    firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#draw

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    vertexCount : int
      Passed on as it is.

    instanceCount : int
      Passed on as it is.

    firstVertex : int
      Passed on as it is.

    firstInstance : int
      Passed on as it is.
    """
    #  void QRhiNull::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
    #      quint32 instanceCount, quint32 firstVertex, quint32 firstInstance)
    ritual = 'ritual_ZN8QRhiNull4drawEP17QRhiCommandBufferjjjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull4drawEP17QRhiCommandBufferjjjj'
    self.uglySide.call(
        ritual,
        self._addressOf(cb), vertexCount, instanceCount, firstVertex,
        firstInstance,
    )

  @overload(QRhiCommandBuffer, int, int, int, int, int)
  @overload(NoneType, int, int, int, int, int)
  def drawIndexed(
      self,
      cb: Optional[QRhiCommandBuffer],
      indexCount: int,
      instanceCount: int,
      firstIndex: int,
      vertexOffset: int,
      firstInstance: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::drawIndexed(QRhiCommandBuffer *cb, quint32
    indexCount, quint32 instanceCount, quint32 firstIndex, qint32
    vertexOffset, quint32 firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#drawIndexed

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indexCount : int
      Passed on as it is.

    instanceCount : int
      Passed on as it is.

    firstIndex : int
      Passed on as it is.

    vertexOffset : int
      Passed on as it is.

    firstInstance : int
      Passed on as it is.
    """
    #  void QRhiNull::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
    #      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
    #      quint32 firstInstance)
    ritual = 'ritual_ZN8QRhiNull11drawIndexedEP17QRhiCommandBufferjjjij'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull11drawIndexedEP17QRhiCommandBufferjjjij')
    self.uglySide.call(
        ritual,
        self._addressOf(cb), indexCount, instanceCount, firstIndex,
        vertexOffset, firstInstance,
    )

  @overload(QRhiCommandBuffer, QRhiBuffer, int, int, int)
  @overload(QRhiCommandBuffer, NoneType, int, int, int)
  @overload(NoneType, QRhiBuffer, int, int, int)
  @overload(NoneType, NoneType, int, int, int)
  def drawIndirect(
      self,
      cb: Optional[QRhiCommandBuffer],
      indirectBuffer: Optional[QRhiBuffer],
      indirectBufferOffset: int,
      drawCount: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount, quint32
    stride)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#drawIndirect

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

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
    #  void QRhiNull::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    #      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
    #      quint32 stride)
    ritual = (
        'ritual_ZN8QRhiNull12drawIndirectEP17QRhiCommandBufferP10QRhiBuffer'
        'jjj')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull12drawIndirectEP17QRhiCommandBufferP10QRhi'
          'Bufferjjj')
    self.uglySide.call(
        ritual,
        self._addressOf(cb), self._addressOf(indirectBuffer),
        indirectBufferOffset, drawCount, stride,
    )

  @overload(QRhiCommandBuffer, QRhiBuffer, int, int, int)
  @overload(QRhiCommandBuffer, NoneType, int, int, int)
  @overload(NoneType, QRhiBuffer, int, int, int)
  @overload(NoneType, NoneType, int, int, int)
  def drawIndexedIndirect(
      self,
      cb: Optional[QRhiCommandBuffer],
      indirectBuffer: Optional[QRhiBuffer],
      indirectBufferOffset: int,
      drawCount: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::drawIndexedIndirect(QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer, quint32 indirectBufferOffset, quint32
    drawCount, quint32 stride)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#drawIndexedIndirect

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

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
    #  void QRhiNull::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    #      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
    #      quint32 stride)
    ritual = (
        'ritual_ZN8QRhiNull19drawIndexedIndirectEP17QRhiCommandBufferP10QRh'
        'iBufferjjj')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull19drawIndexedIndirectEP17QRhiCommandBuffer'
          'P10QRhiBufferjjj')
    self.uglySide.call(
        ritual,
        self._addressOf(cb), self._addressOf(indirectBuffer),
        indirectBufferOffset, drawCount, stride,
    )

  @overload(QRhiCommandBuffer, QByteArray)
  @overload(NoneType, QByteArray)
  def debugMarkBegin(
      self,
      cb: Optional[QRhiCommandBuffer],
      name: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::debugMarkBegin(QRhiCommandBuffer *cb, const
    QByteArray &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#debugMarkBegin

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiNull::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
    #      &name)
    ritual = (
        'ritual_ZN8QRhiNull14debugMarkBeginEP17QRhiCommandBufferRK10QByteAr'
        'ray')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull14debugMarkBeginEP17QRhiCommandBufferRK10Q'
          'ByteArray')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(name))

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def debugMarkEnd(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiNull::debugMarkEnd(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#debugMarkEnd

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiNull::debugMarkEnd(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN8QRhiNull12debugMarkEndEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull12debugMarkEndEP17QRhiCommandBuffer'
    self.uglySide.call(ritual, self._addressOf(cb))

  @overload(QRhiCommandBuffer, QByteArray)
  @overload(NoneType, QByteArray)
  def debugMarkMsg(
      self,
      cb: Optional[QRhiCommandBuffer],
      msg: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::debugMarkMsg(QRhiCommandBuffer *cb, const
    QByteArray &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#debugMarkMsg

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    msg : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiNull::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
    #      &msg)
    ritual = (
        'ritual_ZN8QRhiNull12debugMarkMsgEP17QRhiCommandBufferRK10QByteArra'
        'y')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull12debugMarkMsgEP17QRhiCommandBufferRK10QBy'
          'teArray')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(msg))

  @overload(
      QRhiCommandBuffer, QRhiResourceUpdateBatch,
      QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(QRhiCommandBuffer, NoneType, QRhiCommandBuffer.BeginPassFlags)
  @overload(
      NoneType, QRhiResourceUpdateBatch, QRhiCommandBuffer.BeginPassFlags,
  )
  @overload(NoneType, NoneType, QRhiCommandBuffer.BeginPassFlags)
  def beginComputePass(
      self,
      cb: Optional[QRhiCommandBuffer],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
      flags: QRhiCommandBuffer.BeginPassFlags,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::beginComputePass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#beginComputePass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QRhiCommandBuffer.BeginPassFlags
      Passed on as its number.
    """
    #  void QRhiNull::beginComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    ritual = (
        'ritual_ZN8QRhiNull16beginComputePassEP17QRhiCommandBufferP23QRhiRe'
        'sourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull16beginComputePassEP17QRhiCommandBufferP23'
          'QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE')
    self.uglySide.call(
        ritual,
        self._addressOf(cb), self._addressOf(resourceUpdates), flags.value,
    )

  @overload(QRhiCommandBuffer, QRhiResourceUpdateBatch)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def endComputePass(
      self,
      cb: Optional[QRhiCommandBuffer],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::endComputePass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#endComputePass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiNull::endComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    ritual = (
        'ritual_ZN8QRhiNull14endComputePassEP17QRhiCommandBufferP23QRhiReso'
        'urceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull14endComputePassEP17QRhiCommandBufferP23QR'
          'hiResourceUpdateBatch')
    self.uglySide.call(
        ritual, self._addressOf(cb), self._addressOf(resourceUpdates),
    )

  @overload(QRhiCommandBuffer, int, int, int)
  @overload(NoneType, int, int, int)
  def dispatch(
      self,
      cb: Optional[QRhiCommandBuffer],
      x: int,
      y: int,
      z: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::dispatch(QRhiCommandBuffer *cb, int x, int y,
    int z)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#dispatch

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QRhiNull::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
    ritual = 'ritual_ZN8QRhiNull8dispatchEP17QRhiCommandBufferiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull8dispatchEP17QRhiCommandBufferiii'
    self.uglySide.call(ritual, self._addressOf(cb), x, y, z)

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def nativeHandles(
      self,
      cb: Optional[QRhiCommandBuffer],
  ) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles
    *QRhiNull::nativeHandles(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#nativeHandles

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhiNull::nativeHandles(QRhiCommandBuffer
    #      *cb)
    ritual = 'ritual_ZN8QRhiNull13nativeHandlesEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull13nativeHandlesEP17QRhiCommandBuffer'
    address = self.uglySide.call(ritual, self._addressOf(cb))
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload()
  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles *QRhiNull::nativeHandles()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhiNull::nativeHandles()
    ritual = 'ritual_ZN8QRhiNull13nativeHandlesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull13nativeHandlesEv'
    address = self.uglySide.call(ritual)
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def beginExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiNull::beginExternal(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#beginExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiNull::beginExternal(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN8QRhiNull13beginExternalEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull13beginExternalEP17QRhiCommandBuffer'
    self.uglySide.call(ritual, self._addressOf(cb))

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def endExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiNull::endExternal(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#endExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiNull::endExternal(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN8QRhiNull11endExternalEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull11endExternalEP17QRhiCommandBuffer'
    self.uglySide.call(ritual, self._addressOf(cb))

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def lastCompletedGpuTime(self, cb: Optional[QRhiCommandBuffer]) -> float:
    """
    Calls Qt's 'double QRhiNull::lastCompletedGpuTime(QRhiCommandBuffer
    *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#lastCompletedGpuTime

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  double QRhiNull::lastCompletedGpuTime(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN8QRhiNull20lastCompletedGpuTimeEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull20lastCompletedGpuTimeEP17QRhiCommandBuffe'
          'r')
    return self.uglySide.call(ritual, self._addressOf(cb))

  def statistics(self) -> QRhiStats:
    """
    Calls Qt's 'QRhiStats QRhiNull::statistics()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#statistics

    Returns
    -------

    QRhiStats
      A new cute QRhiStats around the copy Qt gave back. Python owns it.
    """
    #  QRhiStats QRhiNull::statistics()
    ritual = 'ritual_ZN8QRhiNull10statisticsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull10statisticsEv'
    address = self.uglySide.call(ritual)
    from . import QRhiStats
    return QRhiStats._cuteOwning(address)

  def makeThreadLocalNativeContextCurrent(self) -> bool:
    """
    Calls Qt's 'bool QRhiNull::makeThreadLocalNativeContextCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#makeThreadLocalNativeContextCurrent
    """
    #  bool QRhiNull::makeThreadLocalNativeContextCurrent()
    ritual = 'ritual_ZN8QRhiNull35makeThreadLocalNativeContextCurrentEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8QRhiNull35makeThreadLocalNativeContextCurrentEv')
    return self.uglySide.call(ritual)

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QRhiNull::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#releaseCachedResources
    """
    #  void QRhiNull::releaseCachedResources()
    ritual = 'ritual_ZN8QRhiNull22releaseCachedResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull22releaseCachedResourcesEv'
    self.uglySide.call(ritual)

  def pipelineCacheData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRhiNull::pipelineCacheData()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#pipelineCacheData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRhiNull::pipelineCacheData()
    ritual = 'ritual_ZN8QRhiNull17pipelineCacheDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QRhiNull17pipelineCacheDataEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QRhiResourceUpdateBatchPrivate.TextureOp)
  def simulateTextureUpload(
      self,
      u: QRhiResourceUpdateBatchPrivate.TextureOp,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::simulateTextureUpload(const
    QRhiResourceUpdateBatchPrivate::TextureOp &u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#simulateTextureUpload

    Parameters
    ----------

    u : QRhiResourceUpdateBatchPrivate.TextureOp
      Passed on as a value: Qt reads the C++
      QRhiResourceUpdateBatchPrivate::TextureOp, which stays Python's own.
    """
    #  void QRhiNull::simulateTextureUpload(const
    #      QRhiResourceUpdateBatchPrivate::TextureOp &u)
    self.uglySide.call(
        'ritual_ZN8QRhiNull21simulateTextureUploadERKN30QRhiResourceUpdateB'
        'atchPrivate9TextureOpE',
        self._valueOf(u),
    )

  @overload(QRhiResourceUpdateBatchPrivate.TextureOp)
  def simulateTextureCopy(
      self,
      u: QRhiResourceUpdateBatchPrivate.TextureOp,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::simulateTextureCopy(const
    QRhiResourceUpdateBatchPrivate::TextureOp &u)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhinull.html#simulateTextureCopy

    Parameters
    ----------

    u : QRhiResourceUpdateBatchPrivate.TextureOp
      Passed on as a value: Qt reads the C++
      QRhiResourceUpdateBatchPrivate::TextureOp, which stays Python's own.
    """
    #  void QRhiNull::simulateTextureCopy(const
    #      QRhiResourceUpdateBatchPrivate::TextureOp &u)
    self.uglySide.call(
        'ritual_ZN8QRhiNull19simulateTextureCopyERKN30QRhiResourceUpdateBat'
        'chPrivate9TextureOpE',
        self._valueOf(u),
    )

  @overload(QRhiResourceUpdateBatchPrivate.TextureOp)
  def simulateTextureGenMips(
      self,
      u: QRhiResourceUpdateBatchPrivate.TextureOp,
  ) -> None:
    """
    Calls Qt's 'void QRhiNull::simulateTextureGenMips(const
    QRhiResourceUpdateBatchPrivate::TextureOp &u)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhinull.html#simulateTextureGenMips

    Parameters
    ----------

    u : QRhiResourceUpdateBatchPrivate.TextureOp
      Passed on as a value: Qt reads the C++
      QRhiResourceUpdateBatchPrivate::TextureOp, which stays Python's own.
    """
    #  void QRhiNull::simulateTextureGenMips(const
    #      QRhiResourceUpdateBatchPrivate::TextureOp &u)
    self.uglySide.call(
        'ritual_ZN8QRhiNull22simulateTextureGenMipsERKN30QRhiResourceUpdate'
        'BatchPrivate9TextureOpE',
        self._valueOf(u),
    )
