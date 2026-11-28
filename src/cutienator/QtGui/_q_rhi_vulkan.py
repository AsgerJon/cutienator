"""
QRhiVulkan binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QRhiVulkan to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QRhi, QRhiBuffer, QRhiCommandBuffer, QRhiImplementation
from . import QRhiPassResourceTracker, QRhiRenderBuffer, QRhiSampler
from . import QRhiTexture, QRhiTextureRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QSize
  from . import QColor, QMatrix4x4, QRhiAdapter, QRhiComputePipeline
  from . import QRhiDepthStencilClearValue, QRhiDriverInfo
  from . import QRhiGraphicsPipeline, QRhiNativeHandles, QRhiRenderTarget
  from . import QRhiResourceUpdateBatch, QRhiScissor
  from . import QRhiShaderResourceBindings, QRhiShadingRateMap, QRhiStats
  from . import QRhiSwapChain, QRhiTextureRenderTargetDescription
  from . import QRhiViewport, QVkBuffer, QVkCommandBuffer, QVkRenderBuffer
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
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiScissor = WAIT['QRhiScissor']
  QRhiSwapChain = WAIT['QRhiSwapChain']
  QRhiTextureRenderTargetDescription = WAIT['QRhiTextureRenderTargetDescription']
  QRhiViewport = WAIT['QRhiViewport']
  QSize = WAIT['QSize']
  QVkBuffer = WAIT['QVkBuffer']
  QVkCommandBuffer = WAIT['QVkCommandBuffer']
  QVkRenderBuffer = WAIT['QVkRenderBuffer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiVulkan(QRhiImplementation):
  """
  The cute side of Qt's QRhiVulkan: a plain Python object standing in front
  of one C++ QRhiVulkan.

  It is built on the cute 'QRhiImplementation', as Qt's QRhiVulkan is built
  on Qt's QRhiImplementation, and has everything that class has.

  C++ hands a QRhiVulkan around as a copy, so every C++ QRhiVulkan behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiVulkan that has a ritual and that Python can
  call so far, 61 names in all: 'create', 'destroy',
  'enumerateAdaptersBeforeCreate', 'createGraphicsPipeline',
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
  'setPipelineCacheData', 'enqueueTransitionPassResources',
  'trackedRegisterBuffer', 'depthStencilExplicitBarrier',
  'printDeviceLossErrorInfo'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhi::FrameOpResult QRhiVulkan::beginFrame(QRhiSwapChain
    *swapChain, QRhi::BeginFrameFlags flags)': names the enum
    'QRhi::BeginFrameFlag', whose class cannot be named here.
  - Qt's 'QRhi::FrameOpResult
    QRhiVulkan::beginOffscreenFrame(QRhiCommandBuffer **cb,
    QRhi::BeginFrameFlags flags)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QRhiVulkan::setShaderResources(QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb, int dynamicOffsetCount, const
    QRhiCommandBuffer::DynamicOffset *dynamicOffsets)': names
    'QRhiCommandBuffer::DynamicOffset', which has no cute class yet.
  - Qt's 'void QRhiVulkan::setVertexInput(QRhiCommandBuffer *cb, int
    startBinding, int bindingCount, const QRhiCommandBuffer::VertexInput
    *bindings, QRhiBuffer *indexBuf, quint32 indexOffset,
    QRhiCommandBuffer::IndexFormat indexFormat)': names
    'QRhiCommandBuffer::VertexInput', which has no cute class yet.
  - Qt's 'QList<int> QRhiVulkan::supportedSampleCounts() const': gives a type
    Python has no way to take yet.
  - Qt's 'VkDeviceSize QRhiVulkan::subresUploadByteSize(const
    QRhiTextureSubresourceUploadDescription &subresDesc) const': gives a type
    Python has no way to take yet.
  - Qt's 'void QRhiVulkan::setObjectName(uint64_t object, VkObjectType type,
    const QByteArray &name, int slot)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QRhiVulkan::subresourceBarrier(QVkCommandBuffer *cbD, VkImage
    image, VkImageLayout oldLayout, VkImageLayout newLayout, VkAccessFlags
    srcAccess, VkAccessFlags dstAccess, VkPipelineStageFlags srcStage,
    VkPipelineStageFlags dstStage, int startLayer, int layerCount, int
    startLevel, int levelCount)': names 'struct VkImage_T', which has no cute
    class yet.
  - Qt's 'double QRhiVulkan::elapsedSecondsFromTimestamp(quint64 *timestamp,
    bool *ok)': takes a number to change where it is.
  - Qt's 'void QRhiVulkan::printExtraErrorInfo(VkResult err)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QRhiVulkan::~QRhiVulkan()': the destructor: Python removes its C++
    QRhiVulkan by it, and has no other use for it.

  What has no ritual
  ------------------

  34 of the 107 functions Qt declares: 31 Qt's library has no name for it,
  and its code in Qt's source does not compile apart from its file; 3 leans
  on 'QRhiVulkan.

  What to expect
  --------------

  - The C++ QRhiVulkan is created at the first use, not by 'QRhiVulkan(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiVulkan back gives a copy the ritual made for
    Python, in a new cute QRhiVulkan.
  - Each name of Qt's QRhiVulkan that has no cute function yet, '__init__',
    'activateTextureRenderTarget', 'allocateDescriptorSet',
    'chooseTransientImageMemType', 'createDefaultRenderPass',
    'createDescriptorPool', 'createOffscreenRenderPass', 'createShader',
    'createTransientImage', 'effectiveSampleCountBits',
    'elapsedSecondsFromTimestamp', 'endAndEnqueueSecondaryCommandBuffer',
    'endAndSubmitPrimaryCommandBuffer', 'enqueueResourceUpdates',
    'ensureCommandPoolForNewFrame', 'ensurePipelineCache',
    'executeBufferHostWritesForSlot', 'executeDeferredReleases',
    'finishActiveReadbacks', 'optimalDepthStencilFormat', 'prepareNewFrame',
    'prepareUploadSubres', 'printExtraErrorInfo',
    'recordPrimaryCommandBuffer', 'recordTransitionPassResources',
    'recreateSwapChain', 'releaseSwapChainResources', 'setAllocationName',
    'setDefaultScissor', 'setObjectName', 'startPrimaryCommandBuffer',
    'startSecondaryCommandBuffer', 'subresUploadByteSize',
    'subresourceBarrier', 'trackedBufferBarrier', 'trackedImageBarrier',
    'trackedRegisterTexture', 'updateShaderResourceBindings',
    'waitCommandCompletion', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QRhiVulkan, each a class in here as in C++.

  class BufferReadback(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiVulkan::BufferReadback: a plain Python object
    standing in front of one C++ QRhiVulkan::BufferReadback.

    C++ hands a QRhiVulkan::BufferReadback around as a copy, so every C++
    QRhiVulkan::BufferReadback behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QRhiVulkan::BufferReadback yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiVulkan::BufferReadback::~BufferReadback()': the destructor:
      Python removes its C++ QRhiVulkan::BufferReadback by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QRhiVulkan::BufferReadback is created at the first use, not by
      'QRhiVulkan::BufferReadback(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiVulkan::BufferReadback back gives a copy the
      ritual made for Python, in a new cute QRhiVulkan::BufferReadback.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiVulkan::BufferReadback'

    #  Qt's '~QRhiVulkan::BufferReadback()'. Naming it makes this a value
    #  class: Python owns every C++ QRhiVulkan::BufferReadback behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QRhiVulkan14BufferReadbackD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class DeferredReleaseEntry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiVulkan::DeferredReleaseEntry: a plain Python
    object standing in front of one C++ QRhiVulkan::DeferredReleaseEntry.

    C++ hands a QRhiVulkan::DeferredReleaseEntry around as a copy, so every
    C++ QRhiVulkan::DeferredReleaseEntry behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QRhiVulkan::DeferredReleaseEntry yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiVulkan::DeferredReleaseEntry::~DeferredReleaseEntry()': the
      destructor: Python removes its C++ QRhiVulkan::DeferredReleaseEntry by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiVulkan::DeferredReleaseEntry is created at the first use,
      not by 'QRhiVulkan::DeferredReleaseEntry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiVulkan::DeferredReleaseEntry back gives a copy
      the ritual made for Python, in a new cute
      QRhiVulkan::DeferredReleaseEntry.
    """

    #  The enums Qt writes inside QRhiVulkan::DeferredReleaseEntry, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class Type(CuteNum):
      """
      The enum 'QRhiVulkan::DeferredReleaseEntry::Type' of Qt, with the 10
      names Qt gives in it.
      """

      Pipeline = Kee[int](0)
      ShaderResourceBindings = Kee[int](1)
      Buffer = Kee[int](2)
      RenderBuffer = Kee[int](3)
      Texture = Kee[int](4)
      Sampler = Kee[int](5)
      TextureRenderTarget = Kee[int](6)
      RenderPass = Kee[int](7)
      StagingBuffer = Kee[int](8)
      SecondaryCommandBuffer = Kee[int](9)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiVulkan::DeferredReleaseEntry'

    #  Qt's '~QRhiVulkan::DeferredReleaseEntry()'. Naming it makes this a
    #  value class: Python owns every C++ QRhiVulkan::DeferredReleaseEntry
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QRhiVulkan20DeferredReleaseEntryD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class DescriptorPoolData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiVulkan::DescriptorPoolData: a plain Python
    object standing in front of one C++ QRhiVulkan::DescriptorPoolData.

    C++ hands a QRhiVulkan::DescriptorPoolData around as a copy, so every C++
    QRhiVulkan::DescriptorPoolData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QRhiVulkan::DescriptorPoolData yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QRhiVulkan::DescriptorPoolData::DescriptorPoolData(VkDescriptorPool
      pool_)': names 'struct VkDescriptorPool_T', which has no cute class
      yet.
    - Qt's 'QRhiVulkan::DescriptorPoolData::~DescriptorPoolData()': the
      destructor: Python removes its C++ QRhiVulkan::DescriptorPoolData by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiVulkan::DescriptorPoolData is created at the first use, not
      by 'QRhiVulkan::DescriptorPoolData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiVulkan::DescriptorPoolData back gives a copy
      the ritual made for Python, in a new cute
      QRhiVulkan::DescriptorPoolData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiVulkan::DescriptorPoolData'

    #  Qt's '~QRhiVulkan::DescriptorPoolData()'. Naming it makes this a value
    #  class: Python owns every C++ QRhiVulkan::DescriptorPoolData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QRhiVulkan18DescriptorPoolDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QRhiVulkan::DescriptorPoolData::DescriptorPoolData()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhivulkan-descriptorpooldata.html
      """
      #  QRhiVulkan::DescriptorPoolData::DescriptorPoolData()
      self._noteCreation(QRhiVulkan.DescriptorPoolData, lambda: Rituals.call(
          'ritual_ZN10QRhiVulkan18DescriptorPoolDataC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class OffscreenFrame(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiVulkan::OffscreenFrame: a plain Python object
    standing in front of one C++ QRhiVulkan::OffscreenFrame.

    C++ hands a QRhiVulkan::OffscreenFrame around as a copy, so every C++
    QRhiVulkan::OffscreenFrame behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QRhiVulkan::OffscreenFrame yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiVulkan::OffscreenFrame::~OffscreenFrame()': the destructor:
      Python removes its C++ QRhiVulkan::OffscreenFrame by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QRhiVulkan::OffscreenFrame is created at the first use, not by
      'QRhiVulkan::OffscreenFrame(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiVulkan::OffscreenFrame back gives a copy the
      ritual made for Python, in a new cute QRhiVulkan::OffscreenFrame.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRhiImplementation = WAIT['QRhiImplementation']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiVulkan::OffscreenFrame'

    #  Qt's '~QRhiVulkan::OffscreenFrame()'. Naming it makes this a value
    #  class: Python owns every C++ QRhiVulkan::OffscreenFrame behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QRhiVulkan14OffscreenFrameD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QRhiImplementation)
    @overload(NoneType)
    def __init__(self, rhi: Optional[QRhiImplementation]) -> None:
      """
      Notes what was given, for Qt's
      'QRhiVulkan::OffscreenFrame::OffscreenFrame(QRhiImplementation *rhi)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhivulkan-offscreenframe.html#OffscreenFrame

      Parameters
      ----------

      rhi : Optional[QRhiImplementation]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QRhiVulkan::OffscreenFrame::OffscreenFrame(QRhiImplementation *rhi)
      self._noteCreation(QRhiVulkan.OffscreenFrame, lambda: Rituals.call(
          'ritual_ZN10QRhiVulkan14OffscreenFrameC1EP18QRhiImplementation',
          self._addressOf(rhi),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class TextureReadback(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiVulkan::TextureReadback: a plain Python object
    standing in front of one C++ QRhiVulkan::TextureReadback.

    C++ hands a QRhiVulkan::TextureReadback around as a copy, so every C++
    QRhiVulkan::TextureReadback behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QRhiVulkan::TextureReadback yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiVulkan::TextureReadback::~TextureReadback()': the destructor:
      Python removes its C++ QRhiVulkan::TextureReadback by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QRhiVulkan::TextureReadback is created at the first use, not by
      'QRhiVulkan::TextureReadback(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiVulkan::TextureReadback back gives a copy the
      ritual made for Python, in a new cute QRhiVulkan::TextureReadback.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiVulkan::TextureReadback'

    #  Qt's '~QRhiVulkan::TextureReadback()'. Naming it makes this a value
    #  class: Python owns every C++ QRhiVulkan::TextureReadback behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QRhiVulkan15TextureReadbackD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiVulkan'

  #  A C++ QRhiVulkan Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiVulkan'

  #  Qt's '~QRhiVulkan()'. Naming it makes this a value class: Python owns
  #  every C++ QRhiVulkan behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QRhiVulkanD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiNativeHandles)
  @overload(NoneType)
  def enumerateAdaptersBeforeCreate(
      self,
      nativeHandles: Optional[QRhiNativeHandles],
  ) -> QList[QRhiAdapter]:
    """
    Calls Qt's 'QRhi::AdapterList
    QRhiVulkan::enumerateAdaptersBeforeCreate(QRhiNativeHandles
    *nativeHandles) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#enumerateAdaptersBeforeCreate

    Parameters
    ----------

    nativeHandles : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QRhiAdapter]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QRhi::AdapterList
    #      QRhiVulkan::enumerateAdaptersBeforeCreate(QRhiNativeHandles
    #      *nativeHandles) const
    address = self.uglySide.call(
        'ritual_ZNK10QRhiVulkan29enumerateAdaptersBeforeCreateEP17QRhiNativ'
        'eHandles',
        self._addressOf(nativeHandles),
    )
    from . import QRhiAdapter
    return QList[QRhiAdapter]._cuteOwning(address)

  @overload(int)
  def supportedShadingRates(self, sampleCount: int) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QRhiVulkan::supportedShadingRates(int
    sampleCount) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#supportedShadingRates

    Parameters
    ----------

    sampleCount : int
      Passed on as it is.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QRhiVulkan::supportedShadingRates(int sampleCount) const
    address = self.uglySide.call(
        'ritual_ZNK10QRhiVulkan21supportedShadingRatesEi', sampleCount,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  def ubufAlignment(self) -> int:
    """
    Calls Qt's 'int QRhiVulkan::ubufAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#ubufAlignment
    """
    #  int QRhiVulkan::ubufAlignment() const
    ritual = 'ritual_ZNK10QRhiVulkan13ubufAlignmentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QRhiVulkan13ubufAlignmentEv'
    return self.uglySide.call(ritual)

  def isYUpInFramebuffer(self) -> bool:
    """
    Calls Qt's 'bool QRhiVulkan::isYUpInFramebuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#isYUpInFramebuffer
    """
    #  bool QRhiVulkan::isYUpInFramebuffer() const
    ritual = 'ritual_ZNK10QRhiVulkan18isYUpInFramebufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QRhiVulkan18isYUpInFramebufferEv'
    return self.uglySide.call(ritual)

  def isYUpInNDC(self) -> bool:
    """
    Calls Qt's 'bool QRhiVulkan::isYUpInNDC() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#isYUpInNDC
    """
    #  bool QRhiVulkan::isYUpInNDC() const
    ritual = 'ritual_ZNK10QRhiVulkan10isYUpInNDCEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QRhiVulkan10isYUpInNDCEv'
    return self.uglySide.call(ritual)

  def isClipDepthZeroToOne(self) -> bool:
    """
    Calls Qt's 'bool QRhiVulkan::isClipDepthZeroToOne() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#isClipDepthZeroToOne
    """
    #  bool QRhiVulkan::isClipDepthZeroToOne() const
    ritual = 'ritual_ZNK10QRhiVulkan20isClipDepthZeroToOneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QRhiVulkan20isClipDepthZeroToOneEv'
    return self.uglySide.call(ritual)

  def clipSpaceCorrMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QRhiVulkan::clipSpaceCorrMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#clipSpaceCorrMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QRhiVulkan::clipSpaceCorrMatrix() const
    ritual = 'ritual_ZNK10QRhiVulkan19clipSpaceCorrMatrixEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QRhiVulkan19clipSpaceCorrMatrixEv'
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
    Calls Qt's 'bool QRhiVulkan::isTextureFormatSupported(QRhiTexture::Format
    format, QRhiTexture::Flags flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#isTextureFormatSupported

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    flags : QRhiTexture.Flags
      Passed on as its number.
    """
    #  bool QRhiVulkan::isTextureFormatSupported(QRhiTexture::Format format,
    #      QRhiTexture::Flags flags) const
    return self.uglySide.call(
        'ritual_ZNK10QRhiVulkan24isTextureFormatSupportedEN11QRhiTexture6Fo'
        'rmatE6QFlagsINS0_4FlagEE',
        format.value, flags.value,
    )

  @overload(QRhi.Feature)
  def isFeatureSupported(self, feature: QRhi.Feature) -> bool:
    """
    Calls Qt's 'bool QRhiVulkan::isFeatureSupported(QRhi::Feature feature)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#isFeatureSupported

    Parameters
    ----------

    feature : QRhi.Feature
      Passed on as its number.
    """
    #  bool QRhiVulkan::isFeatureSupported(QRhi::Feature feature) const
    ritual = 'ritual_ZNK10QRhiVulkan18isFeatureSupportedEN4QRhi7FeatureE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QRhiVulkan18isFeatureSupportedEN4QRhi7FeatureE')
    return self.uglySide.call(ritual, feature.value)

  @overload(QRhi.ResourceLimit)
  def resourceLimit(self, limit: QRhi.ResourceLimit) -> int:
    """
    Calls Qt's 'int QRhiVulkan::resourceLimit(QRhi::ResourceLimit limit)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#resourceLimit

    Parameters
    ----------

    limit : QRhi.ResourceLimit
      Passed on as its number.
    """
    #  int QRhiVulkan::resourceLimit(QRhi::ResourceLimit limit) const
    ritual = 'ritual_ZNK10QRhiVulkan13resourceLimitEN4QRhi13ResourceLimitE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QRhiVulkan13resourceLimitEN4QRhi13ResourceLimitE')
    return self.uglySide.call(ritual, limit.value)

  def driverInfo(self) -> QRhiDriverInfo:
    """
    Calls Qt's 'QRhiDriverInfo QRhiVulkan::driverInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#driverInfo

    Returns
    -------

    QRhiDriverInfo
      A new cute QRhiDriverInfo around the copy Qt gave back. Python owns it.
    """
    #  QRhiDriverInfo QRhiVulkan::driverInfo() const
    ritual = 'ritual_ZNK10QRhiVulkan10driverInfoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QRhiVulkan10driverInfoEv'
    address = self.uglySide.call(ritual)
    from . import QRhiDriverInfo
    return QRhiDriverInfo._cuteOwning(address)

  def isDeviceLost(self) -> bool:
    """
    Calls Qt's 'bool QRhiVulkan::isDeviceLost() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#isDeviceLost
    """
    #  bool QRhiVulkan::isDeviceLost() const
    ritual = 'ritual_ZNK10QRhiVulkan12isDeviceLostEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QRhiVulkan12isDeviceLostEv'
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
    Calls Qt's 'void QRhiVulkan::setGraphicsPipeline(QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#setGraphicsPipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiGraphicsPipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::setGraphicsPipeline(QRhiCommandBuffer *cb,
    #      QRhiGraphicsPipeline *ps)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan19setGraphicsPipelineEP17QRhiCommandBufferP20'
        'QRhiGraphicsPipeline',
        self._addressOf(cb), self._addressOf(ps),
    )

  @overload(QRhiCommandBuffer, QRhiViewport)
  @overload(NoneType, QRhiViewport)
  def setViewport(
      self,
      cb: Optional[QRhiCommandBuffer],
      viewport: QRhiViewport,
  ) -> None:
    """
    Calls Qt's 'void QRhiVulkan::setViewport(QRhiCommandBuffer *cb, const
    QRhiViewport &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#setViewport

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewport : QRhiViewport
      Passed on as a value: Qt reads the C++ QRhiViewport, which stays
      Python's own.
    """
    #  void QRhiVulkan::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
    #      &viewport)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan11setViewportEP17QRhiCommandBufferRK12QRhiVie'
        'wport',
        self._addressOf(cb), self._valueOf(viewport),
    )

  @overload(QRhiCommandBuffer, QRhiScissor)
  @overload(NoneType, QRhiScissor)
  def setScissor(
      self,
      cb: Optional[QRhiCommandBuffer],
      scissor: QRhiScissor,
  ) -> None:
    """
    Calls Qt's 'void QRhiVulkan::setScissor(QRhiCommandBuffer *cb, const
    QRhiScissor &scissor)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#setScissor

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scissor : QRhiScissor
      Passed on as a value: Qt reads the C++ QRhiScissor, which stays
      Python's own.
    """
    #  void QRhiVulkan::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
    #      &scissor)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan10setScissorEP17QRhiCommandBufferRK11QRhiScis'
        'sor',
        self._addressOf(cb), self._valueOf(scissor),
    )

  @overload(QRhiCommandBuffer, QColor)
  @overload(NoneType, QColor)
  def setBlendConstants(
      self,
      cb: Optional[QRhiCommandBuffer],
      c: QColor,
  ) -> None:
    """
    Calls Qt's 'void QRhiVulkan::setBlendConstants(QRhiCommandBuffer *cb,
    const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#setBlendConstants

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QRhiVulkan::setBlendConstants(QRhiCommandBuffer *cb, const QColor
    #      &c)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan17setBlendConstantsEP17QRhiCommandBufferRK6QC'
        'olor',
        self._addressOf(cb), self._valueOf(c),
    )

  @overload(QRhiCommandBuffer, int)
  @overload(NoneType, int)
  def setStencilRef(
      self,
      cb: Optional[QRhiCommandBuffer],
      refValue: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiVulkan::setStencilRef(QRhiCommandBuffer *cb, quint32
    refValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#setStencilRef

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    refValue : int
      Passed on as it is.
    """
    #  void QRhiVulkan::setStencilRef(QRhiCommandBuffer *cb, quint32
    #      refValue)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan13setStencilRefEP17QRhiCommandBufferj',
        self._addressOf(cb), refValue,
    )

  @overload(QRhiCommandBuffer, QSize)
  @overload(NoneType, QSize)
  def setShadingRate(
      self,
      cb: Optional[QRhiCommandBuffer],
      coarsePixelSize: QSize,
  ) -> None:
    """
    Calls Qt's 'void QRhiVulkan::setShadingRate(QRhiCommandBuffer *cb, const
    QSize &coarsePixelSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#setShadingRate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coarsePixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiVulkan::setShadingRate(QRhiCommandBuffer *cb, const QSize
    #      &coarsePixelSize)
    ritual = (
        'ritual_ZN10QRhiVulkan14setShadingRateEP17QRhiCommandBufferRK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QRhiVulkan14setShadingRateEP17QRhiCommandBufferRK'
          '5QSize')
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
    Calls Qt's 'void QRhiVulkan::setComputePipeline(QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#setComputePipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiComputePipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::setComputePipeline(QRhiCommandBuffer *cb,
    #      QRhiComputePipeline *ps)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan18setComputePipelineEP17QRhiCommandBufferP19Q'
        'RhiComputePipeline',
        self._addressOf(cb), self._addressOf(ps),
    )

  @overload(QRhiNativeHandles)
  @overload(NoneType)
  def setQueueSubmitParams(
      self,
      params: Optional[QRhiNativeHandles],
  ) -> None:
    """
    Calls Qt's 'void QRhiVulkan::setQueueSubmitParams(QRhiNativeHandles
    *params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#setQueueSubmitParams

    Parameters
    ----------

    params : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::setQueueSubmitParams(QRhiNativeHandles *params)
    ritual = (
        'ritual_ZN10QRhiVulkan20setQueueSubmitParamsEP17QRhiNativeHandles')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QRhiVulkan20setQueueSubmitParamsEP17QRhiNativeHan'
          'dles')
    self.uglySide.call(ritual, self._addressOf(params))

  @overload(QByteArray)
  def setPipelineCacheData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiVulkan::setPipelineCacheData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#setPipelineCacheData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiVulkan::setPipelineCacheData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan20setPipelineCacheDataERK10QByteArray',
        self._valueOf(data),
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
    Qt's 'QRhiVulkan::QRhiVulkan(QRhiVulkanInitParams *params,
    QRhiVulkanNativeHandles *importParams)': leans on
    'QRhiVulkan::beginFrame(QRhiSwapChain*, QFlags<QRhi::BeginFrameFlag>)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QRhiVulkan.__init__' has no cute function yet. Qt's "
        "'QRhiVulkan::QRhiVulkan(QRhiVulkanInitParams *params, "
        "QRhiVulkanNativeHandles *importParams)': leans on "
        "'QRhiVulkan::beginFrame(QRhiSwapChain*, "
        "QFlags<QRhi::BeginFrameFlag>)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'bool QRhiVulkan::create(QRhi::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#create

    Parameters
    ----------

    flags : QRhi.Flags
      Passed on as its number.
    """
    #  bool QRhiVulkan::create(QRhi::Flags flags)
    return self.uglySide.call(
        'ritual_ZN10QRhiVulkan6createE6QFlagsIN4QRhi4FlagEE', flags.value,
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QRhiVulkan::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#destroy
    """
    #  void QRhiVulkan::destroy()
    self.uglySide.call('ritual_ZN10QRhiVulkan7destroyEv')

  def createGraphicsPipeline(self) -> Optional[QRhiGraphicsPipeline]:
    """
    Calls Qt's 'QRhiGraphicsPipeline *QRhiVulkan::createGraphicsPipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#createGraphicsPipeline

    Returns
    -------

    Optional[QRhiGraphicsPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiGraphicsPipeline *QRhiVulkan::createGraphicsPipeline()
    address = self.uglySide.call(
        'ritual_ZN10QRhiVulkan22createGraphicsPipelineEv',
    )
    from . import QRhiGraphicsPipeline
    return QRhiGraphicsPipeline._cuteAt(address)

  def createComputePipeline(self) -> Optional[QRhiComputePipeline]:
    """
    Calls Qt's 'QRhiComputePipeline *QRhiVulkan::createComputePipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#createComputePipeline

    Returns
    -------

    Optional[QRhiComputePipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiComputePipeline *QRhiVulkan::createComputePipeline()
    address = self.uglySide.call(
        'ritual_ZN10QRhiVulkan21createComputePipelineEv',
    )
    from . import QRhiComputePipeline
    return QRhiComputePipeline._cuteAt(address)

  def createShaderResourceBindings(
      self,
  ) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings
    *QRhiVulkan::createShaderResourceBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#createShaderResourceBindings

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings *QRhiVulkan::createShaderResourceBindings()
    address = self.uglySide.call(
        'ritual_ZN10QRhiVulkan28createShaderResourceBindingsEv',
    )
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
    Calls Qt's 'QRhiBuffer *QRhiVulkan::createBuffer(QRhiBuffer::Type type,
    QRhiBuffer::UsageFlags usage, quint32 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#createBuffer

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
    #  QRhiBuffer *QRhiVulkan::createBuffer(QRhiBuffer::Type type,
    #      QRhiBuffer::UsageFlags usage, quint32 size)
    address = self.uglySide.call(
        'ritual_ZN10QRhiVulkan12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0'
        '_9UsageFlagEEj',
        type.value, usage.value, size,
    )
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
    *QRhiVulkan::createRenderBuffer(QRhiRenderBuffer::Type type, const QSize
    &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
    QRhiTexture::Format backingFormatHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#createRenderBuffer

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
    #  QRhiRenderBuffer
    #      *QRhiVulkan::createRenderBuffer(QRhiRenderBuffer::Type type, const
    #      QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
    #      QRhiTexture::Format backingFormatHint)
    address = self.uglySide.call(
        'ritual_ZN10QRhiVulkan18createRenderBufferEN16QRhiRenderBuffer4Type'
        'ERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE',
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
    Calls Qt's 'QRhiTexture *QRhiVulkan::createTexture(QRhiTexture::Format
    format, const QSize &pixelSize, int depth, int arraySize, int
    sampleCount, QRhiTexture::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#createTexture

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
    #  QRhiTexture *QRhiVulkan::createTexture(QRhiTexture::Format format,
    #      const QSize &pixelSize, int depth, int arraySize, int sampleCount,
    #      QRhiTexture::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN10QRhiVulkan13createTextureEN11QRhiTexture6FormatERK5QSiz'
        'eiii6QFlagsINS0_4FlagEE',
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
    Calls Qt's 'QRhiSampler *QRhiVulkan::createSampler(QRhiSampler::Filter
    magFilter, QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#createSampler

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
    #  QRhiSampler *QRhiVulkan::createSampler(QRhiSampler::Filter magFilter,
    #      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    #      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
    #      QRhiSampler::AddressMode w)
    address = self.uglySide.call(
        'ritual_ZN10QRhiVulkan13createSamplerEN11QRhiSampler6FilterES1_S1_N'
        'S0_11AddressModeES2_S2_',
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
    *QRhiVulkan::createTextureRenderTarget(const
    QRhiTextureRenderTargetDescription &desc, QRhiTextureRenderTarget::Flags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#createTextureRenderTarget

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
    #  QRhiTextureRenderTarget *QRhiVulkan::createTextureRenderTarget(const
    #      QRhiTextureRenderTargetDescription &desc,
    #      QRhiTextureRenderTarget::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN10QRhiVulkan25createTextureRenderTargetERK34QRhiTextureRe'
        'nderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE',
        self._valueOf(desc), flags.value,
    )
    return QRhiTextureRenderTarget._cuteAt(address)

  def createShadingRateMap(self) -> Optional[QRhiShadingRateMap]:
    """
    Calls Qt's 'QRhiShadingRateMap *QRhiVulkan::createShadingRateMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#createShadingRateMap

    Returns
    -------

    Optional[QRhiShadingRateMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShadingRateMap *QRhiVulkan::createShadingRateMap()
    ritual = 'ritual_ZN10QRhiVulkan20createShadingRateMapEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiVulkan20createShadingRateMapEv'
    address = self.uglySide.call(ritual)
    from . import QRhiShadingRateMap
    return QRhiShadingRateMap._cuteAt(address)

  def createSwapChain(self) -> Optional[QRhiSwapChain]:
    """
    Calls Qt's 'QRhiSwapChain *QRhiVulkan::createSwapChain()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#createSwapChain

    Returns
    -------

    Optional[QRhiSwapChain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSwapChain *QRhiVulkan::createSwapChain()
    address = self.uglySide.call('ritual_ZN10QRhiVulkan15createSwapChainEv')
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
    Calls Qt's 'QRhi::FrameOpResult QRhiVulkan::endFrame(QRhiSwapChain
    *swapChain, QRhi::EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#endFrame

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
    #  QRhi::FrameOpResult QRhiVulkan::endFrame(QRhiSwapChain *swapChain,
    #      QRhi::EndFrameFlags flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN10QRhiVulkan8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12End'
        'FrameFlagEE',
        self._addressOf(swapChain), flags.value,
    ))

  @overload(QRhi.EndFrameFlags)
  def endOffscreenFrame(
      self,
      flags: QRhi.EndFrameFlags,
  ) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult
    QRhiVulkan::endOffscreenFrame(QRhi::EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#endOffscreenFrame

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
    #  QRhi::FrameOpResult QRhiVulkan::endOffscreenFrame(QRhi::EndFrameFlags
    #      flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN10QRhiVulkan17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameF'
        'lagEE',
        flags.value,
    ))

  def finish(self) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult QRhiVulkan::finish()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#finish

    Returns
    -------

    QRhi.FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.FrameOpResult(number)' gives.
    """
    #  QRhi::FrameOpResult QRhiVulkan::finish()
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN10QRhiVulkan6finishEv',
    ))

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
    Calls Qt's 'void QRhiVulkan::resourceUpdate(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#resourceUpdate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::resourceUpdate(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan14resourceUpdateEP17QRhiCommandBufferP23QRhiR'
        'esourceUpdateBatch',
        self._addressOf(cb), self._addressOf(resourceUpdates),
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
    Calls Qt's 'void QRhiVulkan::beginPass(QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt, const QColor &colorClearValue, const
    QRhiDepthStencilClearValue &depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#beginPass

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
    #  void QRhiVulkan::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget
    #      *rt, const QColor &colorClearValue, const
    #      QRhiDepthStencilClearValue &depthStencilClearValue,
    #      QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan9beginPassEP17QRhiCommandBufferP16QRhiRenderT'
        'argetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateB'
        'atch6QFlagsINS0_13BeginPassFlagEE',
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
    Calls Qt's 'void QRhiVulkan::endPass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#endPass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::endPass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan7endPassEP17QRhiCommandBufferP23QRhiResourceU'
        'pdateBatch',
        self._addressOf(cb), self._addressOf(resourceUpdates),
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
    Calls Qt's 'void QRhiVulkan::draw(QRhiCommandBuffer *cb, quint32
    vertexCount, quint32 instanceCount, quint32 firstVertex, quint32
    firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#draw

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
    #  void QRhiVulkan::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
    #      quint32 instanceCount, quint32 firstVertex, quint32 firstInstance)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan4drawEP17QRhiCommandBufferjjjj',
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
    Calls Qt's 'void QRhiVulkan::drawIndexed(QRhiCommandBuffer *cb, quint32
    indexCount, quint32 instanceCount, quint32 firstIndex, qint32
    vertexOffset, quint32 firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#drawIndexed

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
    #  void QRhiVulkan::drawIndexed(QRhiCommandBuffer *cb, quint32
    #      indexCount, quint32 instanceCount, quint32 firstIndex, qint32
    #      vertexOffset, quint32 firstInstance)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan11drawIndexedEP17QRhiCommandBufferjjjij',
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
    Calls Qt's 'void QRhiVulkan::drawIndirect(QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer, quint32 indirectBufferOffset, quint32
    drawCount, quint32 stride)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#drawIndirect

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
    #  void QRhiVulkan::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    #      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
    #      quint32 stride)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan12drawIndirectEP17QRhiCommandBufferP10QRhiBuf'
        'ferjjj',
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
    Calls Qt's 'void QRhiVulkan::drawIndexedIndirect(QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer, quint32 indirectBufferOffset, quint32
    drawCount, quint32 stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#drawIndexedIndirect

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
    #  void QRhiVulkan::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    #      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
    #      quint32 stride)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan19drawIndexedIndirectEP17QRhiCommandBufferP10'
        'QRhiBufferjjj',
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
    Calls Qt's 'void QRhiVulkan::debugMarkBegin(QRhiCommandBuffer *cb, const
    QByteArray &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#debugMarkBegin

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiVulkan::debugMarkBegin(QRhiCommandBuffer *cb, const
    #      QByteArray &name)
    ritual = (
        'ritual_ZN10QRhiVulkan14debugMarkBeginEP17QRhiCommandBufferRK10QByt'
        'eArray')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QRhiVulkan14debugMarkBeginEP17QRhiCommandBufferRK'
          '10QByteArray')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(name))

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def debugMarkEnd(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiVulkan::debugMarkEnd(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#debugMarkEnd

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::debugMarkEnd(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN10QRhiVulkan12debugMarkEndEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiVulkan12debugMarkEndEP17QRhiCommandBuffer'
    self.uglySide.call(ritual, self._addressOf(cb))

  @overload(QRhiCommandBuffer, QByteArray)
  @overload(NoneType, QByteArray)
  def debugMarkMsg(
      self,
      cb: Optional[QRhiCommandBuffer],
      msg: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiVulkan::debugMarkMsg(QRhiCommandBuffer *cb, const
    QByteArray &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#debugMarkMsg

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    msg : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiVulkan::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
    #      &msg)
    ritual = (
        'ritual_ZN10QRhiVulkan12debugMarkMsgEP17QRhiCommandBufferRK10QByteA'
        'rray')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QRhiVulkan12debugMarkMsgEP17QRhiCommandBufferRK10'
          'QByteArray')
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
    Calls Qt's 'void QRhiVulkan::beginComputePass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#beginComputePass

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
    #  void QRhiVulkan::beginComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan16beginComputePassEP17QRhiCommandBufferP23QRh'
        'iResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE',
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
    Calls Qt's 'void QRhiVulkan::endComputePass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#endComputePass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::endComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan14endComputePassEP17QRhiCommandBufferP23QRhiR'
        'esourceUpdateBatch',
        self._addressOf(cb), self._addressOf(resourceUpdates),
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
    Calls Qt's 'void QRhiVulkan::dispatch(QRhiCommandBuffer *cb, int x, int
    y, int z)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#dispatch

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
    #  void QRhiVulkan::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan8dispatchEP17QRhiCommandBufferiii',
        self._addressOf(cb), x, y, z,
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def nativeHandles(
      self,
      cb: Optional[QRhiCommandBuffer],
  ) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles
    *QRhiVulkan::nativeHandles(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#nativeHandles

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
    #  const QRhiNativeHandles *QRhiVulkan::nativeHandles(QRhiCommandBuffer
    #      *cb)
    ritual = 'ritual_ZN10QRhiVulkan13nativeHandlesEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QRhiVulkan13nativeHandlesEP17QRhiCommandBuffer')
    address = self.uglySide.call(ritual, self._addressOf(cb))
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload()
  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles *QRhiVulkan::nativeHandles()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhiVulkan::nativeHandles()
    ritual = 'ritual_ZN10QRhiVulkan13nativeHandlesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiVulkan13nativeHandlesEv'
    address = self.uglySide.call(ritual)
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def beginExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiVulkan::beginExternal(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#beginExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::beginExternal(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan13beginExternalEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def endExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiVulkan::endExternal(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#endExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::endExternal(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan11endExternalEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def lastCompletedGpuTime(self, cb: Optional[QRhiCommandBuffer]) -> float:
    """
    Calls Qt's 'double QRhiVulkan::lastCompletedGpuTime(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#lastCompletedGpuTime

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  double QRhiVulkan::lastCompletedGpuTime(QRhiCommandBuffer *cb)
    ritual = (
        'ritual_ZN10QRhiVulkan20lastCompletedGpuTimeEP17QRhiCommandBuffer')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QRhiVulkan20lastCompletedGpuTimeEP17QRhiCommandBu'
          'ffer')
    return self.uglySide.call(ritual, self._addressOf(cb))

  def statistics(self) -> QRhiStats:
    """
    Calls Qt's 'QRhiStats QRhiVulkan::statistics()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#statistics

    Returns
    -------

    QRhiStats
      A new cute QRhiStats around the copy Qt gave back. Python owns it.
    """
    #  QRhiStats QRhiVulkan::statistics()
    address = self.uglySide.call('ritual_ZN10QRhiVulkan10statisticsEv')
    from . import QRhiStats
    return QRhiStats._cuteOwning(address)

  def makeThreadLocalNativeContextCurrent(self) -> bool:
    """
    Calls Qt's 'bool QRhiVulkan::makeThreadLocalNativeContextCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html
    """
    #  bool QRhiVulkan::makeThreadLocalNativeContextCurrent()
    ritual = 'ritual_ZN10QRhiVulkan35makeThreadLocalNativeContextCurrentEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QRhiVulkan35makeThreadLocalNativeContextCurrentEv')
    return self.uglySide.call(ritual)

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QRhiVulkan::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#releaseCachedResources
    """
    #  void QRhiVulkan::releaseCachedResources()
    ritual = 'ritual_ZN10QRhiVulkan22releaseCachedResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiVulkan22releaseCachedResourcesEv'
    self.uglySide.call(ritual)

  def pipelineCacheData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRhiVulkan::pipelineCacheData()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivulkan.html#pipelineCacheData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRhiVulkan::pipelineCacheData()
    address = self.uglySide.call(
        'ritual_ZN10QRhiVulkan17pipelineCacheDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QVkCommandBuffer)
  @overload(NoneType)
  def enqueueTransitionPassResources(
      self,
      cbD: Optional[QVkCommandBuffer],
  ) -> None:
    """
    Calls Qt's 'void
    QRhiVulkan::enqueueTransitionPassResources(QVkCommandBuffer *cbD)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#enqueueTransitionPassResources

    Parameters
    ----------

    cbD : Optional[QVkCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::enqueueTransitionPassResources(QVkCommandBuffer *cbD)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan30enqueueTransitionPassResourcesEP16QVkComman'
        'dBuffer',
        self._addressOf(cbD),
    )

  @overload(
      QRhiPassResourceTracker, QVkBuffer, int,
      QRhiPassResourceTracker.BufferAccess,
      QRhiPassResourceTracker.BufferStage,
  )
  @overload(
      QRhiPassResourceTracker, NoneType, int,
      QRhiPassResourceTracker.BufferAccess,
      QRhiPassResourceTracker.BufferStage,
  )
  @overload(
      NoneType, QVkBuffer, int, QRhiPassResourceTracker.BufferAccess,
      QRhiPassResourceTracker.BufferStage,
  )
  @overload(
      NoneType, NoneType, int, QRhiPassResourceTracker.BufferAccess,
      QRhiPassResourceTracker.BufferStage,
  )
  def trackedRegisterBuffer(
      self,
      passResTracker: Optional[QRhiPassResourceTracker],
      bufD: Optional[QVkBuffer],
      slot: int,
      access: QRhiPassResourceTracker.BufferAccess,
      stage: QRhiPassResourceTracker.BufferStage,
  ) -> None:
    """
    Calls Qt's 'void
    QRhiVulkan::trackedRegisterBuffer(QRhiPassResourceTracker
    *passResTracker, QVkBuffer *bufD, int slot,
    QRhiPassResourceTracker::BufferAccess access,
    QRhiPassResourceTracker::BufferStage stage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#trackedRegisterBuffer

    Parameters
    ----------

    passResTracker : Optional[QRhiPassResourceTracker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bufD : Optional[QVkBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slot : int
      Passed on as it is.

    access : QRhiPassResourceTracker.BufferAccess
      Passed on as its number.

    stage : QRhiPassResourceTracker.BufferStage
      Passed on as its number.
    """
    #  void QRhiVulkan::trackedRegisterBuffer(QRhiPassResourceTracker
    #      *passResTracker, QVkBuffer *bufD, int slot,
    #      QRhiPassResourceTracker::BufferAccess access,
    #      QRhiPassResourceTracker::BufferStage stage)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan21trackedRegisterBufferEP23QRhiPassResourceTr'
        'ackerP9QVkBufferiNS0_12BufferAccessENS0_11BufferStageE',
        self._addressOf(passResTracker), self._addressOf(bufD), slot,
        access.value, stage.value,
    )

  @overload(QVkCommandBuffer, QVkRenderBuffer)
  @overload(QVkCommandBuffer, NoneType)
  @overload(NoneType, QVkRenderBuffer)
  @overload(NoneType, NoneType)
  def depthStencilExplicitBarrier(
      self,
      cbD: Optional[QVkCommandBuffer],
      rbD: Optional[QVkRenderBuffer],
  ) -> None:
    """
    Calls Qt's 'void QRhiVulkan::depthStencilExplicitBarrier(QVkCommandBuffer
    *cbD, QVkRenderBuffer *rbD)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#depthStencilExplicitBarrier

    Parameters
    ----------

    cbD : Optional[QVkCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rbD : Optional[QVkRenderBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiVulkan::depthStencilExplicitBarrier(QVkCommandBuffer *cbD,
    #      QVkRenderBuffer *rbD)
    self.uglySide.call(
        'ritual_ZN10QRhiVulkan27depthStencilExplicitBarrierEP16QVkCommandBu'
        'fferP15QVkRenderBuffer',
        self._addressOf(cbD), self._addressOf(rbD),
    )

  def printDeviceLossErrorInfo(self) -> None:
    """
    Calls Qt's 'void QRhiVulkan::printDeviceLossErrorInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkan.html#printDeviceLossErrorInfo
    """
    #  void QRhiVulkan::printDeviceLossErrorInfo() const
    self.uglySide.call('ritual_ZNK10QRhiVulkan24printDeviceLossErrorInfoEv')

  @staticmethod
  def activateTextureRenderTarget(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::activateTextureRenderTarget(QVkCommandBuffer *cbD,
    QVkTextureRenderTarget *rtD)': leans on
    'QRhiVulkan::trackedRegisterTexture(QRhiPassResourceTracker*,
    QVkTexture*, QRhiPassResourceTracker::TextureAccess,
    QRhiPassResourceTracker::TextureStage)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRhiVulkan.activateTextureRenderTarget' has no cute function yet. "
        "Qt's 'void "
        "QRhiVulkan::activateTextureRenderTarget(QVkCommandBuffer *cbD, "
        "QVkTextureRenderTarget *rtD)': leans on "
        "'QRhiVulkan::trackedRegisterTexture(QRhiPassResourceTracker*, "
        "QVkTexture*, QRhiPassResourceTracker::TextureAccess, "
        "QRhiPassResourceTracker::TextureStage)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def allocateDescriptorSet(*__, **_) -> Never:
    """
    Qt's 'bool QRhiVulkan::allocateDescriptorSet(VkDescriptorSetAllocateInfo
    *allocInfo, VkDescriptorSet *result, int *resultPoolIndex)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.allocateDescriptorSet' has no cute function yet. Qt's "
        "'bool "
        "QRhiVulkan::allocateDescriptorSet(VkDescriptorSetAllocateInfo "
        "*allocInfo, VkDescriptorSet *result, int *resultPoolIndex)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QVulkanDeviceFunctions'.")

  @staticmethod
  def chooseTransientImageMemType(*__, **_) -> Never:
    """
    Qt's 'uint32_t QRhiVulkan::chooseTransientImageMemType(VkImage img,
    uint32_t startIndex)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QVulkanFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.chooseTransientImageMemType' has no cute function yet. "
        "Qt's 'uint32_t QRhiVulkan::chooseTransientImageMemType(VkImage "
        "img, uint32_t startIndex)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QVulkanFunctions'.")

  @staticmethod
  def createDefaultRenderPass(*__, **_) -> Never:
    """
    Qt's 'bool QRhiVulkan::createDefaultRenderPass(QVkRenderPassDescriptor
    *rpD, bool hasDepthStencil, VkSampleCountFlagBits samples, VkFormat
    colorFormat, QRhiShadingRateMap *shadingRateMap)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.createDefaultRenderPass' has no cute function yet. "
        "Qt's 'bool "
        "QRhiVulkan::createDefaultRenderPass(QVkRenderPassDescriptor *rpD, "
        "bool hasDepthStencil, VkSampleCountFlagBits samples, VkFormat "
        "colorFormat, QRhiShadingRateMap *shadingRateMap)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QVulkanDeviceFunctions'.")

  @staticmethod
  def createDescriptorPool(*__, **_) -> Never:
    """
    Qt's 'VkResult QRhiVulkan::createDescriptorPool(VkDescriptorPool *pool)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.createDescriptorPool' has no cute function yet. Qt's "
        "'VkResult QRhiVulkan::createDescriptorPool(VkDescriptorPool "
        "*pool)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def createOffscreenRenderPass(*__, **_) -> Never:
    """
    Qt's 'bool QRhiVulkan::createOffscreenRenderPass(QVkRenderPassDescriptor
    *rpD, const QRhiColorAttachment *colorAttachmentsBegin, const
    QRhiColorAttachment *colorAttachmentsEnd, bool preserveColor, bool
    preserveDs, bool storeDs, QRhiRenderBuffer *depthStencilBuffer,
    QRhiTexture *depthTexture, QRhiTexture *depthResolveTexture, int
    depthLayer, QRhiShadingRateMap *shadingRateMap)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'fillRenderPassCreateInfo'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.createOffscreenRenderPass' has no cute function yet. "
        "Qt's 'bool "
        "QRhiVulkan::createOffscreenRenderPass(QVkRenderPassDescriptor "
        "*rpD, const QRhiColorAttachment *colorAttachmentsBegin, const "
        "QRhiColorAttachment *colorAttachmentsEnd, bool preserveColor, bool "
        "preserveDs, bool storeDs, QRhiRenderBuffer *depthStencilBuffer, "
        "QRhiTexture *depthTexture, QRhiTexture *depthResolveTexture, int "
        "depthLayer, QRhiShadingRateMap *shadingRateMap)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'fillRenderPassCreateInfo'.")

  @staticmethod
  def createShader(*__, **_) -> Never:
    """
    Qt's 'VkShaderModule QRhiVulkan::createShader(const QByteArray &spirv)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.createShader' has no cute function yet. Qt's "
        "'VkShaderModule QRhiVulkan::createShader(const QByteArray "
        "&spirv)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def createTransientImage(*__, **_) -> Never:
    """
    Qt's 'bool QRhiVulkan::createTransientImage(VkFormat format, const QSize
    &pixelSize, VkImageUsageFlags usage, VkImageAspectFlags aspectMask,
    VkSampleCountFlagBits samples, VkDeviceMemory *mem, VkImage *images,
    VkImageView *views, int count)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.createTransientImage' has no cute function yet. Qt's "
        "'bool QRhiVulkan::createTransientImage(VkFormat format, const "
        "QSize &pixelSize, VkImageUsageFlags usage, VkImageAspectFlags "
        "aspectMask, VkSampleCountFlagBits samples, VkDeviceMemory *mem, "
        "VkImage *images, VkImageView *views, int count)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QVulkanDeviceFunctions'.")

  @staticmethod
  def effectiveSampleCountBits(*__, **_) -> Never:
    """
    Qt's 'VkSampleCountFlagBits QRhiVulkan::effectiveSampleCountBits(int
    sampleCount)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'qvk_sampleCounts'; did you mean 'sampleCount'?.
    """
    raise NotImplementedError(
        "'QRhiVulkan.effectiveSampleCountBits' has no cute function yet. "
        "Qt's 'VkSampleCountFlagBits "
        "QRhiVulkan::effectiveSampleCountBits(int sampleCount)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qvk_sampleCounts'; did you mean 'sampleCount'?.")

  @staticmethod
  def elapsedSecondsFromTimestamp(*__, **_) -> Never:
    """
    Qt's 'double QRhiVulkan::elapsedSecondsFromTimestamp(quint64 *timestamp,
    bool *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QRhiVulkan.elapsedSecondsFromTimestamp' has no cute function yet. "
        "Qt's 'double QRhiVulkan::elapsedSecondsFromTimestamp(quint64 "
        "*timestamp, bool *ok)': takes a number to change where it is.")

  @staticmethod
  def endAndEnqueueSecondaryCommandBuffer(*__, **_) -> Never:
    """
    Qt's 'void
    QRhiVulkan::endAndEnqueueSecondaryCommandBuffer(VkCommandBuffer cb,
    QVkCommandBuffer *cbD)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.endAndEnqueueSecondaryCommandBuffer' has no cute "
        "function yet. Qt's 'void "
        "QRhiVulkan::endAndEnqueueSecondaryCommandBuffer(VkCommandBuffer "
        "cb, QVkCommandBuffer *cbD)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def endAndSubmitPrimaryCommandBuffer(*__, **_) -> Never:
    """
    Qt's 'QRhi::FrameOpResult
    QRhiVulkan::endAndSubmitPrimaryCommandBuffer(VkCommandBuffer cb, VkFence
    cmdFence, VkSemaphore *waitSem, VkSemaphore *signalSem)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.endAndSubmitPrimaryCommandBuffer' has no cute function "
        "yet. Qt's 'QRhi::FrameOpResult "
        "QRhiVulkan::endAndSubmitPrimaryCommandBuffer(VkCommandBuffer cb, "
        "VkFence cmdFence, VkSemaphore *waitSem, VkSemaphore *signalSem)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def enqueueResourceUpdates(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::enqueueResourceUpdates(QVkCommandBuffer *cbD,
    QRhiResourceUpdateBatch *resourceUpdates)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'VmaAllocationCreateInfo'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.enqueueResourceUpdates' has no cute function yet. Qt's "
        "'void QRhiVulkan::enqueueResourceUpdates(QVkCommandBuffer *cbD, "
        "QRhiResourceUpdateBatch *resourceUpdates)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'VmaAllocationCreateInfo'.")

  @staticmethod
  def ensureCommandPoolForNewFrame(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::ensureCommandPoolForNewFrame()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.ensureCommandPoolForNewFrame' has no cute function "
        "yet. Qt's 'void QRhiVulkan::ensureCommandPoolForNewFrame()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QVulkanDeviceFunctions'.")

  @staticmethod
  def ensurePipelineCache(*__, **_) -> Never:
    """
    Qt's 'bool QRhiVulkan::ensurePipelineCache(const void *initialData,
    size_t initialDataSize)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: member access into
    incomplete type 'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.ensurePipelineCache' has no cute function yet. Qt's "
        "'bool QRhiVulkan::ensurePipelineCache(const void *initialData, "
        "size_t initialDataSize)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def executeBufferHostWritesForSlot(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::executeBufferHostWritesForSlot(QVkBuffer *bufD,
    int slot)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'VmaAllocation'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.executeBufferHostWritesForSlot' has no cute function "
        "yet. Qt's 'void "
        "QRhiVulkan::executeBufferHostWritesForSlot(QVkBuffer *bufD, int "
        "slot)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'VmaAllocation'.")

  @staticmethod
  def executeDeferredReleases(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::executeDeferredReleases(bool forced)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.executeDeferredReleases' has no cute function yet. "
        "Qt's 'void QRhiVulkan::executeDeferredReleases(bool forced)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QVulkanDeviceFunctions'.")

  @staticmethod
  def finishActiveReadbacks(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::finishActiveReadbacks(bool forced)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'toVmaAllocator'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.finishActiveReadbacks' has no cute function yet. Qt's "
        "'void QRhiVulkan::finishActiveReadbacks(bool forced)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'toVmaAllocator'.")

  @staticmethod
  def optimalDepthStencilFormat(*__, **_) -> Never:
    """
    Qt's 'VkFormat QRhiVulkan::optimalDepthStencilFormat()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QVulkanFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.optimalDepthStencilFormat' has no cute function yet. "
        "Qt's 'VkFormat QRhiVulkan::optimalDepthStencilFormat()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QVulkanFunctions'.")

  @staticmethod
  def prepareNewFrame(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::prepareNewFrame(QRhiCommandBuffer *cb)': leans on
    'QRhiVulkan::finishActiveReadbacks(bool)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRhiVulkan.prepareNewFrame' has no cute function yet. Qt's 'void "
        "QRhiVulkan::prepareNewFrame(QRhiCommandBuffer *cb)': leans on "
        "'QRhiVulkan::finishActiveReadbacks(bool)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def prepareUploadSubres(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::prepareUploadSubres(QVkTexture *texD, int layer,
    int level, const QRhiTextureSubresourceUploadDescription &subresDesc,
    size_t *curOfs, void *mp, BufferImageCopyList *copyInfos)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'aligned'; did you mean
    'alignof'?.
    """
    raise NotImplementedError(
        "'QRhiVulkan.prepareUploadSubres' has no cute function yet. Qt's "
        "'void QRhiVulkan::prepareUploadSubres(QVkTexture *texD, int layer, "
        "int level, const QRhiTextureSubresourceUploadDescription "
        "&subresDesc, size_t *curOfs, void *mp, BufferImageCopyList "
        "*copyInfos)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'aligned'; did you mean 'alignof'?.")

  @staticmethod
  def printExtraErrorInfo(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::printExtraErrorInfo(VkResult err)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRhiVulkan.printExtraErrorInfo' has no cute function yet. Qt's "
        "'void QRhiVulkan::printExtraErrorInfo(VkResult err)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def recordPrimaryCommandBuffer(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::recordPrimaryCommandBuffer(QVkCommandBuffer
    *cbD)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.recordPrimaryCommandBuffer' has no cute function yet. "
        "Qt's 'void QRhiVulkan::recordPrimaryCommandBuffer(QVkCommandBuffer "
        "*cbD)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def recordTransitionPassResources(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::recordTransitionPassResources(QVkCommandBuffer
    *cbD, const QRhiPassResourceTracker &tracker)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'toVkAccess'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.recordTransitionPassResources' has no cute function "
        "yet. Qt's 'void "
        "QRhiVulkan::recordTransitionPassResources(QVkCommandBuffer *cbD, "
        "const QRhiPassResourceTracker &tracker)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'toVkAccess'.")

  @staticmethod
  def recreateSwapChain(*__, **_) -> Never:
    """
    Qt's 'bool QRhiVulkan::recreateSwapChain(QRhiSwapChain *swapChain)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.recreateSwapChain' has no cute function yet. Qt's "
        "'bool QRhiVulkan::recreateSwapChain(QRhiSwapChain *swapChain)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def releaseSwapChainResources(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::releaseSwapChainResources(QRhiSwapChain
    *swapChain)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.releaseSwapChainResources' has no cute function yet. "
        "Qt's 'void QRhiVulkan::releaseSwapChainResources(QRhiSwapChain "
        "*swapChain)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def setAllocationName(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::setAllocationName(QVkAlloc allocation, const
    QByteArray &name, int slot)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'toVmaAllocator'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.setAllocationName' has no cute function yet. Qt's "
        "'void QRhiVulkan::setAllocationName(QVkAlloc allocation, const "
        "QByteArray &name, int slot)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'toVmaAllocator'.")

  @staticmethod
  def setDefaultScissor(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::setDefaultScissor(QVkCommandBuffer *cbD)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.setDefaultScissor' has no cute function yet. Qt's "
        "'void QRhiVulkan::setDefaultScissor(QVkCommandBuffer *cbD)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QVulkanDeviceFunctions'.")

  @staticmethod
  def setObjectName(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::setObjectName(uint64_t object, VkObjectType type,
    const QByteArray &name, int slot)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QRhiVulkan.setObjectName' has no cute function yet. Qt's 'void "
        "QRhiVulkan::setObjectName(uint64_t object, VkObjectType type, "
        "const QByteArray &name, int slot)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def startPrimaryCommandBuffer(*__, **_) -> Never:
    """
    Qt's 'QRhi::FrameOpResult
    QRhiVulkan::startPrimaryCommandBuffer(VkCommandBuffer *cb)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.startPrimaryCommandBuffer' has no cute function yet. "
        "Qt's 'QRhi::FrameOpResult "
        "QRhiVulkan::startPrimaryCommandBuffer(VkCommandBuffer *cb)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QVulkanDeviceFunctions'.")

  @staticmethod
  def startSecondaryCommandBuffer(*__, **_) -> Never:
    """
    Qt's 'VkCommandBuffer
    QRhiVulkan::startSecondaryCommandBuffer(QVkRenderTargetData *rtD)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.startSecondaryCommandBuffer' has no cute function yet. "
        "Qt's 'VkCommandBuffer "
        "QRhiVulkan::startSecondaryCommandBuffer(QVkRenderTargetData "
        "*rtD)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QVulkanDeviceFunctions'.")

  @staticmethod
  def subresUploadByteSize(*__, **_) -> Never:
    """
    Qt's 'VkDeviceSize QRhiVulkan::subresUploadByteSize(const
    QRhiTextureSubresourceUploadDescription &subresDesc) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRhiVulkan.subresUploadByteSize' has no cute function yet. Qt's "
        "'VkDeviceSize QRhiVulkan::subresUploadByteSize(const "
        "QRhiTextureSubresourceUploadDescription &subresDesc) const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def subresourceBarrier(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::subresourceBarrier(QVkCommandBuffer *cbD, VkImage
    image, VkImageLayout oldLayout, VkImageLayout newLayout, VkAccessFlags
    srcAccess, VkAccessFlags dstAccess, VkPipelineStageFlags srcStage,
    VkPipelineStageFlags dstStage, int startLayer, int layerCount, int
    startLevel, int levelCount)': names 'struct VkImage_T', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QRhiVulkan.subresourceBarrier' has no cute function yet. Qt's "
        "'void QRhiVulkan::subresourceBarrier(QVkCommandBuffer *cbD, "
        "VkImage image, VkImageLayout oldLayout, VkImageLayout newLayout, "
        "VkAccessFlags srcAccess, VkAccessFlags dstAccess, "
        "VkPipelineStageFlags srcStage, VkPipelineStageFlags dstStage, int "
        "startLayer, int layerCount, int startLevel, int levelCount)': "
        "names 'struct VkImage_T', which has no cute class yet.")

  @staticmethod
  def trackedBufferBarrier(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::trackedBufferBarrier(QVkCommandBuffer *cbD,
    QVkBuffer *bufD, int slot, VkAccessFlags access, VkPipelineStageFlags
    stage)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'accessIsWrite'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.trackedBufferBarrier' has no cute function yet. Qt's "
        "'void QRhiVulkan::trackedBufferBarrier(QVkCommandBuffer *cbD, "
        "QVkBuffer *bufD, int slot, VkAccessFlags access, "
        "VkPipelineStageFlags stage)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'accessIsWrite'.")

  @staticmethod
  def trackedImageBarrier(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::trackedImageBarrier(QVkCommandBuffer *cbD,
    QVkTexture *texD, VkImageLayout layout, VkAccessFlags access,
    VkPipelineStageFlags stage)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'accessIsWrite'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.trackedImageBarrier' has no cute function yet. Qt's "
        "'void QRhiVulkan::trackedImageBarrier(QVkCommandBuffer *cbD, "
        "QVkTexture *texD, VkImageLayout layout, VkAccessFlags access, "
        "VkPipelineStageFlags stage)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'accessIsWrite'.")

  @staticmethod
  def trackedRegisterTexture(*__, **_) -> Never:
    """
    Qt's 'void QRhiVulkan::trackedRegisterTexture(QRhiPassResourceTracker
    *passResTracker, QVkTexture *texD, QRhiPassResourceTracker::TextureAccess
    access, QRhiPassResourceTracker::TextureStage stage)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'toVkAccess'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.trackedRegisterTexture' has no cute function yet. Qt's "
        "'void QRhiVulkan::trackedRegisterTexture(QRhiPassResourceTracker "
        "*passResTracker, QVkTexture *texD, "
        "QRhiPassResourceTracker::TextureAccess access, "
        "QRhiPassResourceTracker::TextureStage stage)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'toVkAccess'.")

  @staticmethod
  def updateShaderResourceBindings(*__, **_) -> Never:
    """
    Qt's 'void
    QRhiVulkan::updateShaderResourceBindings(QRhiShaderResourceBindings
    *srb)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'aligned'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.updateShaderResourceBindings' has no cute function "
        "yet. Qt's 'void "
        "QRhiVulkan::updateShaderResourceBindings(QRhiShaderResourceBindings"
        " *srb)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'aligned'.")

  @staticmethod
  def waitCommandCompletion(*__, **_) -> Never:
    """
    Qt's 'QRhi::FrameOpResult QRhiVulkan::waitCommandCompletion(int
    frameSlot)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QVulkanDeviceFunctions'.
    """
    raise NotImplementedError(
        "'QRhiVulkan.waitCommandCompletion' has no cute function yet. Qt's "
        "'QRhi::FrameOpResult QRhiVulkan::waitCommandCompletion(int "
        "frameSlot)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QVulkanDeviceFunctions'.")
