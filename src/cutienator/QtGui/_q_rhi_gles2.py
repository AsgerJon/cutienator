"""
QRhiGles2 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QRhiGles2 to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGles2Buffer, QGles2Texture, QRhi, QRhiBuffer
from . import QRhiCommandBuffer, QRhiImplementation, QRhiPassResourceTracker
from . import QRhiRenderBuffer, QRhiSampler, QRhiTexture
from . import QRhiTextureRenderTarget, QShader, QShaderDescription

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QSize
  from . import QColor, QGles2CommandBuffer, QMatrix4x4, QRhiComputePipeline
  from . import QRhiDepthStencilClearValue, QRhiDriverInfo
  from . import QRhiGraphicsPipeline, QRhiNativeHandles, QRhiRenderTarget
  from . import QRhiResourceUpdateBatch, QRhiScissor
  from . import QRhiShaderResourceBindings, QRhiShadingRateMap, QRhiStats
  from . import QRhiSwapChain, QRhiTextureRenderTargetDescription
  from . import QRhiTextureSubresourceUploadDescription, QRhiViewport
  from . import QShaderVersion, QSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QGles2CommandBuffer = WAIT['QGles2CommandBuffer']
  QRhiComputePipeline = WAIT['QRhiComputePipeline']
  QRhiDepthStencilClearValue = WAIT['QRhiDepthStencilClearValue']
  QRhiGraphicsPipeline = WAIT['QRhiGraphicsPipeline']
  QRhiNativeHandles = WAIT['QRhiNativeHandles']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiScissor = WAIT['QRhiScissor']
  QRhiSwapChain = WAIT['QRhiSwapChain']
  QRhiTextureRenderTargetDescription = WAIT['QRhiTextureRenderTargetDescription']
  QRhiTextureSubresourceUploadDescription = WAIT['QRhiTextureSubresourceUploadDescription']
  QRhiViewport = WAIT['QRhiViewport']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiGles2(QRhiImplementation):
  """
  The cute side of Qt's QRhiGles2: a plain Python object standing in front of
  one C++ QRhiGles2.

  It is built on the cute 'QRhiImplementation', as Qt's QRhiGles2 is built on
  Qt's QRhiImplementation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiGles2 that has a ritual and that Python can call
  so far, 69 names in all: 'create', 'destroy', 'createGraphicsPipeline',
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
  'setPipelineCacheData', 'evaluateFallbackSurface',
  'executeDeferredReleases', 'trackedBufferBarrier', 'trackedImageBarrier',
  'enqueueSubresUpload', 'enqueueResourceUpdates', 'trackedRegisterBuffer',
  'enqueueBarriersForPass', 'glslVersionsToTry', 'linkProgram',
  'sanityCheckVertexFragmentInterface', 'isProgramBinaryDiskCacheEnabled',
  'trySaveToPipelineCache'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhi::FrameOpResult QRhiGles2::beginFrame(QRhiSwapChain *swapChain,
    QRhi::BeginFrameFlags flags)': names the enum 'QRhi::BeginFrameFlag',
    whose class cannot be named here.
  - Qt's 'QRhi::FrameOpResult
    QRhiGles2::beginOffscreenFrame(QRhiCommandBuffer **cb,
    QRhi::BeginFrameFlags flags)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QRhiGles2::setShaderResources(QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb, int dynamicOffsetCount, const
    QRhiCommandBuffer::DynamicOffset *dynamicOffsets)': names
    'QRhiCommandBuffer::DynamicOffset', which has no cute class yet.
  - Qt's 'void QRhiGles2::setVertexInput(QRhiCommandBuffer *cb, int
    startBinding, int bindingCount, const QRhiCommandBuffer::VertexInput
    *bindings, QRhiBuffer *indexBuf, quint32 indexOffset,
    QRhiCommandBuffer::IndexFormat indexFormat)': names
    'QRhiCommandBuffer::VertexInput', which has no cute class yet.
  - Qt's 'QList<int> QRhiGles2::supportedSampleCounts() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QRhiGles2::bindCombinedSampler(QGles2CommandBuffer *cbD,
    QGles2Texture *texD, QGles2Sampler *samplerD, void *ps, uint
    psGeneration, int glslLocation, int *texUnit, bool
    *activeTexUnitAltered)': names 'void', which has no cute class yet.
  - Qt's 'std::optional<QShaderVersion> QRhiGles2::commonGlslEsVersion(const
    QRhiShaderStage *stages, int stageCount) const': gives a type Python has
    no way to take yet.
  - Qt's 'QByteArray QRhiGles2::shaderSource(const QRhiShaderStage
    &shaderStage, QShaderVersion *shaderVersion,
    std::optional<QShaderVersion> commonVersion)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QRhiGles2::compileShader(GLuint program, const QRhiShaderStage
    &shaderStage, QShaderVersion *shaderVersion,
    std::optional<QShaderVersion> commonVersion)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QRhiGles2::registerUniformIfActive(const
    QShaderDescription::BlockVariable &var, const QByteArray &namePrefix, int
    binding, int baseOffset, GLuint program, ActiveUniformLocationTracker
    *activeUniformLocations, QGles2UniformDescriptionVector *dst)': names
    'QRhiGles2::ActiveUniformLocationTracker', which has no cute class yet.
  - Qt's 'void QRhiGles2::gatherUniforms(GLuint program, const
    QShaderDescription::UniformBlock &ub, ActiveUniformLocationTracker
    *activeUniformLocations, QGles2UniformDescriptionVector *dst)': names
    'QRhiGles2::ActiveUniformLocationTracker', which has no cute class yet.
  - Qt's 'void QRhiGles2::gatherSamplers(GLuint program, const
    QShaderDescription::InOutVariable &v, QGles2SamplerDescriptionVector
    *dst)': names 'QGles2SamplerDescriptionVector', which has no cute class
    yet.
  - Qt's 'void QRhiGles2::gatherGeneratedSamplers(GLuint program, const
    QShader::SeparateToCombinedImageSamplerMapping &mapping,
    QGles2SamplerDescriptionVector *dst)': names
    'QGles2SamplerDescriptionVector', which has no cute class yet.

  What has no ritual
  ------------------

  9 of the 92 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QRhiGles2.

  What to expect
  --------------

  - The C++ QRhiGles2 is created at the first use, not by 'QRhiGles2(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiGles2.
  - Each name of Qt's QRhiGles2 that has no cute function yet, '__init__',
    'bindCombinedSampler', 'bindShaderResources', 'commonGlslEsVersion',
    'compileShader', 'enqueueBindFramebuffer', 'ensureContext',
    'executeBindGraphicsPipeline', 'executeCommandBuffer',
    'gatherGeneratedSamplers', 'gatherSamplers', 'gatherUniforms',
    'registerUniformIfActive', 'shaderSource', 'trackedRegisterTexture',
    'tryLoadFromDiskOrPipelineCache', 'trySaveToDiskCache', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRhiGles2, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ProgramCacheResult(CuteNum):
    """
    The enum 'QRhiGles2::ProgramCacheResult' of Qt, with the 3 names Qt gives
    in it.
    """

    ProgramCacheHit = Kee[int](0)
    ProgramCacheMiss = Kee[int](1)
    ProgramCacheError = Kee[int](2)

  #  The classes Qt writes inside QRhiGles2, each a class in here as in C++.

  class Caps(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiGles2::Caps: a plain Python object standing in
    front of one C++ QRhiGles2::Caps.

    C++ hands a QRhiGles2::Caps around as a copy, so every C++
    QRhiGles2::Caps behind a cute one is Python's own: it is removed, by the
    ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiGles2::Caps yet. It can be made from Python, in 1
    way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiGles2::Caps::~Caps()': the destructor: Python removes its C++
      QRhiGles2::Caps by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiGles2::Caps is created at the first use, not by
      'QRhiGles2::Caps(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiGles2::Caps back gives a copy the ritual made
      for Python, in a new cute QRhiGles2::Caps.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiGles2::Caps'

    #  Qt's '~QRhiGles2::Caps()'. Naming it makes this a value class: Python
    #  owns every C++ QRhiGles2::Caps behind a cute one, and removes it by
    #  this ritual.
    __delete_ritual__ = 'ritual_ZN9QRhiGles24CapsD1Ev'

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
      Notes what was given, for Qt's 'QRhiGles2::Caps::Caps()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qrhigles2-caps.html#Caps
      """
      #  QRhiGles2::Caps::Caps()
      self._noteCreation(QRhiGles2.Caps, lambda: Rituals.call(
          'ritual_ZN9QRhiGles24CapsC1Ev',
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

  class DeferredReleaseEntry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiGles2::DeferredReleaseEntry: a plain Python
    object standing in front of one C++ QRhiGles2::DeferredReleaseEntry.

    C++ hands a QRhiGles2::DeferredReleaseEntry around as a copy, so every
    C++ QRhiGles2::DeferredReleaseEntry behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QRhiGles2::DeferredReleaseEntry yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiGles2::DeferredReleaseEntry::~DeferredReleaseEntry()': the
      destructor: Python removes its C++ QRhiGles2::DeferredReleaseEntry by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiGles2::DeferredReleaseEntry is created at the first use,
      not by 'QRhiGles2::DeferredReleaseEntry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiGles2::DeferredReleaseEntry back gives a copy
      the ritual made for Python, in a new cute
      QRhiGles2::DeferredReleaseEntry.
    """

    #  The enums Qt writes inside QRhiGles2::DeferredReleaseEntry, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class Type(CuteNum):
      """
      The enum 'QRhiGles2::DeferredReleaseEntry::Type' of Qt, with the 5
      names Qt gives in it.
      """

      Buffer = Kee[int](0)
      Pipeline = Kee[int](1)
      Texture = Kee[int](2)
      RenderBuffer = Kee[int](3)
      TextureRenderTarget = Kee[int](4)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiGles2::DeferredReleaseEntry'

    #  Qt's '~QRhiGles2::DeferredReleaseEntry()'. Naming it makes this a
    #  value class: Python owns every C++ QRhiGles2::DeferredReleaseEntry
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QRhiGles220DeferredReleaseEntryD1Ev'

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

  class OffscreenFrame(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiGles2::OffscreenFrame: a plain Python object
    standing in front of one C++ QRhiGles2::OffscreenFrame.

    What exists
    -----------

    No function of Qt's QRhiGles2::OffscreenFrame yet. It can be made from
    Python, in 1 way; see '__init__'.

    What to expect
    --------------

    - The C++ QRhiGles2::OffscreenFrame is created at the first use, not by
      'QRhiGles2::OffscreenFrame(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QRhiGles2::OffscreenFrame.
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
    __qt_class__ = 'QRhiGles2::OffscreenFrame'

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
      'QRhiGles2::OffscreenFrame::OffscreenFrame(QRhiImplementation *rhi)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhigles2-offscreenframe.html#OffscreenFrame

      Parameters
      ----------

      rhi : Optional[QRhiImplementation]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QRhiGles2::OffscreenFrame::OffscreenFrame(QRhiImplementation *rhi)
      self._noteCreation(QRhiGles2.OffscreenFrame, lambda: Rituals.call(
          'ritual_ZN9QRhiGles214OffscreenFrameC1EP18QRhiImplementation',
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

  class PipelineCacheData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiGles2::PipelineCacheData: a plain Python object
    standing in front of one C++ QRhiGles2::PipelineCacheData.

    C++ hands a QRhiGles2::PipelineCacheData around as a copy, so every C++
    QRhiGles2::PipelineCacheData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QRhiGles2::PipelineCacheData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiGles2::PipelineCacheData::~PipelineCacheData()': the
      destructor: Python removes its C++ QRhiGles2::PipelineCacheData by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiGles2::PipelineCacheData is created at the first use, not
      by 'QRhiGles2::PipelineCacheData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiGles2::PipelineCacheData back gives a copy the
      ritual made for Python, in a new cute QRhiGles2::PipelineCacheData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiGles2::PipelineCacheData'

    #  Qt's '~QRhiGles2::PipelineCacheData()'. Naming it makes this a value
    #  class: Python owns every C++ QRhiGles2::PipelineCacheData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QRhiGles217PipelineCacheDataD1Ev'

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

  class Scratch(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiGles2::Scratch: a plain Python object standing
    in front of one C++ QRhiGles2::Scratch.

    C++ hands a QRhiGles2::Scratch around as a copy, so every C++
    QRhiGles2::Scratch behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiGles2::Scratch yet. None can be made from Python:
    one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiGles2::Scratch::~Scratch()': the destructor: Python removes
      its C++ QRhiGles2::Scratch by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiGles2::Scratch is created at the first use, not by
      'QRhiGles2::Scratch(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiGles2::Scratch back gives a copy the ritual
      made for Python, in a new cute QRhiGles2::Scratch.
    """

    #  The classes Qt writes inside QRhiGles2::Scratch, each a class in here
    #  as in C++.

    class SeparateSampler(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QRhiGles2::Scratch::SeparateSampler: a plain
      Python object standing in front of one C++
      QRhiGles2::Scratch::SeparateSampler.

      C++ hands a QRhiGles2::Scratch::SeparateSampler around as a copy, so
      every C++ QRhiGles2::Scratch::SeparateSampler behind a cute one is
      Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QRhiGles2::Scratch::SeparateSampler yet. None can
      be made from Python: one comes out of a function of another class that
      gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QRhiGles2::Scratch::SeparateSampler::~SeparateSampler()': the
        destructor: Python removes its C++
        QRhiGles2::Scratch::SeparateSampler by it, and has no other use for
        it.

      What to expect
      --------------

      - The C++ QRhiGles2::Scratch::SeparateSampler is created at the first
        use, not by 'QRhiGles2::Scratch::SeparateSampler(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QRhiGles2::Scratch::SeparateSampler back gives a
        copy the ritual made for Python, in a new cute
        QRhiGles2::Scratch::SeparateSampler.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QRhiGles2::Scratch::SeparateSampler'

      #  Qt's '~QRhiGles2::Scratch::SeparateSampler()'. Naming it makes this
      #  a value class: Python owns every C++
      #  QRhiGles2::Scratch::SeparateSampler behind a cute one, and removes
      #  it by this ritual.
      __delete_ritual__ = 'ritual_ZN9QRhiGles27Scratch15SeparateSamplerD1Ev'

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    class SeparateTexture(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QRhiGles2::Scratch::SeparateTexture: a plain
      Python object standing in front of one C++
      QRhiGles2::Scratch::SeparateTexture.

      C++ hands a QRhiGles2::Scratch::SeparateTexture around as a copy, so
      every C++ QRhiGles2::Scratch::SeparateTexture behind a cute one is
      Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QRhiGles2::Scratch::SeparateTexture yet. None can
      be made from Python: one comes out of a function of another class that
      gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QRhiGles2::Scratch::SeparateTexture::~SeparateTexture()': the
        destructor: Python removes its C++
        QRhiGles2::Scratch::SeparateTexture by it, and has no other use for
        it.

      What to expect
      --------------

      - The C++ QRhiGles2::Scratch::SeparateTexture is created at the first
        use, not by 'QRhiGles2::Scratch::SeparateTexture(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QRhiGles2::Scratch::SeparateTexture back gives a
        copy the ritual made for Python, in a new cute
        QRhiGles2::Scratch::SeparateTexture.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QRhiGles2::Scratch::SeparateTexture'

      #  Qt's '~QRhiGles2::Scratch::SeparateTexture()'. Naming it makes this
      #  a value class: Python owns every C++
      #  QRhiGles2::Scratch::SeparateTexture behind a cute one, and removes
      #  it by this ritual.
      __delete_ritual__ = 'ritual_ZN9QRhiGles27Scratch15SeparateTextureD1Ev'

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    class data32_t(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QRhiGles2::Scratch::data32_t: a plain Python
      object standing in front of one C++ QRhiGles2::Scratch::data32_t.

      C++ hands a QRhiGles2::Scratch::data32_t around as a copy, so every C++
      QRhiGles2::Scratch::data32_t behind a cute one is Python's own: it is
      removed, by the ritual named in '__delete_ritual__', when the cute
      object goes.

      What exists
      -----------

      No function of Qt's QRhiGles2::Scratch::data32_t yet. None can be made
      from Python: one comes out of a function of another class that gives
      one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QRhiGles2::Scratch::data32_t::~data32_t()': the destructor:
        Python removes its C++ QRhiGles2::Scratch::data32_t by it, and has no
        other use for it.

      What to expect
      --------------

      - The C++ QRhiGles2::Scratch::data32_t is created at the first use, not
        by 'QRhiGles2::Scratch::data32_t(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QRhiGles2::Scratch::data32_t back gives a copy
        the ritual made for Python, in a new cute
        QRhiGles2::Scratch::data32_t.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QRhiGles2::Scratch::data32_t'

      #  Qt's '~QRhiGles2::Scratch::data32_t()'. Naming it makes this a value
      #  class: Python owns every C++ QRhiGles2::Scratch::data32_t behind a
      #  cute one, and removes it by this ritual.
      __delete_ritual__ = 'ritual_ZN9QRhiGles27Scratch8data32_tD1Ev'

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiGles2::Scratch'

    #  Qt's '~QRhiGles2::Scratch()'. Naming it makes this a value class:
    #  Python owns every C++ QRhiGles2::Scratch behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QRhiGles27ScratchD1Ev'

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
  __qt_class__ = 'QRhiGles2'

  #  A C++ QRhiGles2 Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiGles2'

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
    Calls Qt's 'QList<QSize> QRhiGles2::supportedShadingRates(int
    sampleCount) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#supportedShadingRates

    Parameters
    ----------

    sampleCount : int
      Passed on as it is.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QRhiGles2::supportedShadingRates(int sampleCount) const
    address = self.uglySide.call(
        'ritual_ZNK9QRhiGles221supportedShadingRatesEi', sampleCount,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  def ubufAlignment(self) -> int:
    """
    Calls Qt's 'int QRhiGles2::ubufAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#ubufAlignment
    """
    #  int QRhiGles2::ubufAlignment() const
    ritual = 'ritual_ZNK9QRhiGles213ubufAlignmentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QRhiGles213ubufAlignmentEv'
    return self.uglySide.call(ritual)

  def isYUpInFramebuffer(self) -> bool:
    """
    Calls Qt's 'bool QRhiGles2::isYUpInFramebuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#isYUpInFramebuffer
    """
    #  bool QRhiGles2::isYUpInFramebuffer() const
    ritual = 'ritual_ZNK9QRhiGles218isYUpInFramebufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QRhiGles218isYUpInFramebufferEv'
    return self.uglySide.call(ritual)

  def isYUpInNDC(self) -> bool:
    """
    Calls Qt's 'bool QRhiGles2::isYUpInNDC() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#isYUpInNDC
    """
    #  bool QRhiGles2::isYUpInNDC() const
    ritual = 'ritual_ZNK9QRhiGles210isYUpInNDCEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QRhiGles210isYUpInNDCEv'
    return self.uglySide.call(ritual)

  def isClipDepthZeroToOne(self) -> bool:
    """
    Calls Qt's 'bool QRhiGles2::isClipDepthZeroToOne() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#isClipDepthZeroToOne
    """
    #  bool QRhiGles2::isClipDepthZeroToOne() const
    ritual = 'ritual_ZNK9QRhiGles220isClipDepthZeroToOneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QRhiGles220isClipDepthZeroToOneEv'
    return self.uglySide.call(ritual)

  def clipSpaceCorrMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QRhiGles2::clipSpaceCorrMatrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#clipSpaceCorrMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QRhiGles2::clipSpaceCorrMatrix() const
    ritual = 'ritual_ZNK9QRhiGles219clipSpaceCorrMatrixEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QRhiGles219clipSpaceCorrMatrixEv'
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
    Calls Qt's 'bool QRhiGles2::isTextureFormatSupported(QRhiTexture::Format
    format, QRhiTexture::Flags flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#isTextureFormatSupported

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    flags : QRhiTexture.Flags
      Passed on as its number.
    """
    #  bool QRhiGles2::isTextureFormatSupported(QRhiTexture::Format format,
    #      QRhiTexture::Flags flags) const
    return self.uglySide.call(
        'ritual_ZNK9QRhiGles224isTextureFormatSupportedEN11QRhiTexture6Form'
        'atE6QFlagsINS0_4FlagEE',
        format.value, flags.value,
    )

  @overload(QRhi.Feature)
  def isFeatureSupported(self, feature: QRhi.Feature) -> bool:
    """
    Calls Qt's 'bool QRhiGles2::isFeatureSupported(QRhi::Feature feature)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#isFeatureSupported

    Parameters
    ----------

    feature : QRhi.Feature
      Passed on as its number.
    """
    #  bool QRhiGles2::isFeatureSupported(QRhi::Feature feature) const
    ritual = 'ritual_ZNK9QRhiGles218isFeatureSupportedEN4QRhi7FeatureE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QRhiGles218isFeatureSupportedEN4QRhi7FeatureE'
    return self.uglySide.call(ritual, feature.value)

  @overload(QRhi.ResourceLimit)
  def resourceLimit(self, limit: QRhi.ResourceLimit) -> int:
    """
    Calls Qt's 'int QRhiGles2::resourceLimit(QRhi::ResourceLimit limit)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#resourceLimit

    Parameters
    ----------

    limit : QRhi.ResourceLimit
      Passed on as its number.
    """
    #  int QRhiGles2::resourceLimit(QRhi::ResourceLimit limit) const
    ritual = 'ritual_ZNK9QRhiGles213resourceLimitEN4QRhi13ResourceLimitE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9QRhiGles213resourceLimitEN4QRhi13ResourceLimitE')
    return self.uglySide.call(ritual, limit.value)

  def driverInfo(self) -> QRhiDriverInfo:
    """
    Calls Qt's 'QRhiDriverInfo QRhiGles2::driverInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#driverInfo

    Returns
    -------

    QRhiDriverInfo
      A new cute QRhiDriverInfo around the copy Qt gave back. Python owns it.
    """
    #  QRhiDriverInfo QRhiGles2::driverInfo() const
    ritual = 'ritual_ZNK9QRhiGles210driverInfoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QRhiGles210driverInfoEv'
    address = self.uglySide.call(ritual)
    from . import QRhiDriverInfo
    return QRhiDriverInfo._cuteOwning(address)

  def isDeviceLost(self) -> bool:
    """
    Calls Qt's 'bool QRhiGles2::isDeviceLost() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#isDeviceLost
    """
    #  bool QRhiGles2::isDeviceLost() const
    ritual = 'ritual_ZNK9QRhiGles212isDeviceLostEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QRhiGles212isDeviceLostEv'
    return self.uglySide.call(ritual)

  def evaluateFallbackSurface(self) -> Optional[QSurface]:
    """
    Calls Qt's 'QSurface *QRhiGles2::evaluateFallbackSurface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#evaluateFallbackSurface

    Returns
    -------

    Optional[QSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface *QRhiGles2::evaluateFallbackSurface() const
    address = self.uglySide.call(
        'ritual_ZNK9QRhiGles223evaluateFallbackSurfaceEv',
    )
    from . import QSurface
    return QSurface._cuteAt(address)

  def glslVersionsToTry(self) -> QList[QShaderVersion]:
    """
    Calls Qt's 'QList<QShaderVersion> QRhiGles2::glslVersionsToTry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#glslVersionsToTry

    Returns
    -------

    QList[QShaderVersion]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QShaderVersion> QRhiGles2::glslVersionsToTry() const
    address = self.uglySide.call('ritual_ZNK9QRhiGles217glslVersionsToTryEv')
    from . import QShaderVersion
    return QList[QShaderVersion]._cuteOwning(address)

  def isProgramBinaryDiskCacheEnabled(self) -> bool:
    """
    Calls Qt's 'bool QRhiGles2::isProgramBinaryDiskCacheEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#isProgramBinaryDiskCacheEnabled
    """
    #  bool QRhiGles2::isProgramBinaryDiskCacheEnabled() const
    return self.uglySide.call(
        'ritual_ZNK9QRhiGles231isProgramBinaryDiskCacheEnabledEv',
    )

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
    Calls Qt's 'void QRhiGles2::setGraphicsPipeline(QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#setGraphicsPipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiGraphicsPipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::setGraphicsPipeline(QRhiCommandBuffer *cb,
    #      QRhiGraphicsPipeline *ps)
    ritual = (
        'ritual_ZN9QRhiGles219setGraphicsPipelineEP17QRhiCommandBufferP20QR'
        'hiGraphicsPipeline')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles219setGraphicsPipelineEP17QRhiCommandBuffe'
          'rP20QRhiGraphicsPipeline')
    self.uglySide.call(ritual, self._addressOf(cb), self._addressOf(ps))

  @overload(QRhiCommandBuffer, QRhiViewport)
  @overload(NoneType, QRhiViewport)
  def setViewport(
      self,
      cb: Optional[QRhiCommandBuffer],
      viewport: QRhiViewport,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::setViewport(QRhiCommandBuffer *cb, const
    QRhiViewport &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#setViewport

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewport : QRhiViewport
      Passed on as a value: Qt reads the C++ QRhiViewport, which stays
      Python's own.
    """
    #  void QRhiGles2::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
    #      &viewport)
    ritual = (
        'ritual_ZN9QRhiGles211setViewportEP17QRhiCommandBufferRK12QRhiViewp'
        'ort')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles211setViewportEP17QRhiCommandBufferRK12QRh'
          'iViewport')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(viewport))

  @overload(QRhiCommandBuffer, QRhiScissor)
  @overload(NoneType, QRhiScissor)
  def setScissor(
      self,
      cb: Optional[QRhiCommandBuffer],
      scissor: QRhiScissor,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::setScissor(QRhiCommandBuffer *cb, const
    QRhiScissor &scissor)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#setScissor

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scissor : QRhiScissor
      Passed on as a value: Qt reads the C++ QRhiScissor, which stays
      Python's own.
    """
    #  void QRhiGles2::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
    #      &scissor)
    ritual = (
        'ritual_ZN9QRhiGles210setScissorEP17QRhiCommandBufferRK11QRhiScisso'
        'r')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles210setScissorEP17QRhiCommandBufferRK11QRhi'
          'Scissor')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(scissor))

  @overload(QRhiCommandBuffer, QColor)
  @overload(NoneType, QColor)
  def setBlendConstants(
      self,
      cb: Optional[QRhiCommandBuffer],
      c: QColor,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::setBlendConstants(QRhiCommandBuffer *cb,
    const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#setBlendConstants

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QRhiGles2::setBlendConstants(QRhiCommandBuffer *cb, const QColor
    #      &c)
    ritual = (
        'ritual_ZN9QRhiGles217setBlendConstantsEP17QRhiCommandBufferRK6QCol'
        'or')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles217setBlendConstantsEP17QRhiCommandBufferR'
          'K6QColor')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(c))

  @overload(QRhiCommandBuffer, int)
  @overload(NoneType, int)
  def setStencilRef(
      self,
      cb: Optional[QRhiCommandBuffer],
      refValue: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::setStencilRef(QRhiCommandBuffer *cb, quint32
    refValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#setStencilRef

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    refValue : int
      Passed on as it is.
    """
    #  void QRhiGles2::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
    ritual = 'ritual_ZN9QRhiGles213setStencilRefEP17QRhiCommandBufferj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles213setStencilRefEP17QRhiCommandBufferj'
    self.uglySide.call(ritual, self._addressOf(cb), refValue)

  @overload(QRhiCommandBuffer, QSize)
  @overload(NoneType, QSize)
  def setShadingRate(
      self,
      cb: Optional[QRhiCommandBuffer],
      coarsePixelSize: QSize,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::setShadingRate(QRhiCommandBuffer *cb, const
    QSize &coarsePixelSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#setShadingRate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coarsePixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiGles2::setShadingRate(QRhiCommandBuffer *cb, const QSize
    #      &coarsePixelSize)
    ritual = (
        'ritual_ZN9QRhiGles214setShadingRateEP17QRhiCommandBufferRK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles214setShadingRateEP17QRhiCommandBufferRK5Q'
          'Size')
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
    Calls Qt's 'void QRhiGles2::setComputePipeline(QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#setComputePipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiComputePipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::setComputePipeline(QRhiCommandBuffer *cb,
    #      QRhiComputePipeline *ps)
    ritual = (
        'ritual_ZN9QRhiGles218setComputePipelineEP17QRhiCommandBufferP19QRh'
        'iComputePipeline')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles218setComputePipelineEP17QRhiCommandBuffer'
          'P19QRhiComputePipeline')
    self.uglySide.call(ritual, self._addressOf(cb), self._addressOf(ps))

  @overload(QRhiNativeHandles)
  @overload(NoneType)
  def setQueueSubmitParams(
      self,
      params: Optional[QRhiNativeHandles],
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::setQueueSubmitParams(QRhiNativeHandles
    *params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#setQueueSubmitParams

    Parameters
    ----------

    params : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::setQueueSubmitParams(QRhiNativeHandles *params)
    ritual = 'ritual_ZN9QRhiGles220setQueueSubmitParamsEP17QRhiNativeHandles'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles220setQueueSubmitParamsEP17QRhiNativeHandl'
          'es')
    self.uglySide.call(ritual, self._addressOf(params))

  @overload(QByteArray)
  def setPipelineCacheData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiGles2::setPipelineCacheData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#setPipelineCacheData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiGles2::setPipelineCacheData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN9QRhiGles220setPipelineCacheDataERK10QByteArray',
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
    Qt's 'QRhiGles2::QRhiGles2(QRhiGles2InitParams *params,
    QRhiGles2NativeHandles *importDevice)': leans on
    'QRhiGles2::endExternal(QRhiCommandBuffer*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRhiGles2.__init__' has no cute function yet. Qt's "
        "'QRhiGles2::QRhiGles2(QRhiGles2InitParams *params, "
        "QRhiGles2NativeHandles *importDevice)': leans on "
        "'QRhiGles2::endExternal(QRhiCommandBuffer*)', which Qt's source "
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

  @overload(QRhi.Flags)
  def create(self, flags: QRhi.Flags) -> bool:
    """
    Calls Qt's 'bool QRhiGles2::create(QRhi::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#create

    Parameters
    ----------

    flags : QRhi.Flags
      Passed on as its number.
    """
    #  bool QRhiGles2::create(QRhi::Flags flags)
    return self.uglySide.call(
        'ritual_ZN9QRhiGles26createE6QFlagsIN4QRhi4FlagEE', flags.value,
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QRhiGles2::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#destroy
    """
    #  void QRhiGles2::destroy()
    ritual = 'ritual_ZN9QRhiGles27destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles27destroyEv'
    self.uglySide.call(ritual)

  def createGraphicsPipeline(self) -> Optional[QRhiGraphicsPipeline]:
    """
    Calls Qt's 'QRhiGraphicsPipeline *QRhiGles2::createGraphicsPipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#createGraphicsPipeline

    Returns
    -------

    Optional[QRhiGraphicsPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiGraphicsPipeline *QRhiGles2::createGraphicsPipeline()
    address = self.uglySide.call(
        'ritual_ZN9QRhiGles222createGraphicsPipelineEv',
    )
    from . import QRhiGraphicsPipeline
    return QRhiGraphicsPipeline._cuteAt(address)

  def createComputePipeline(self) -> Optional[QRhiComputePipeline]:
    """
    Calls Qt's 'QRhiComputePipeline *QRhiGles2::createComputePipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#createComputePipeline

    Returns
    -------

    Optional[QRhiComputePipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiComputePipeline *QRhiGles2::createComputePipeline()
    address = self.uglySide.call(
        'ritual_ZN9QRhiGles221createComputePipelineEv',
    )
    from . import QRhiComputePipeline
    return QRhiComputePipeline._cuteAt(address)

  def createShaderResourceBindings(
      self,
  ) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings
    *QRhiGles2::createShaderResourceBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#createShaderResourceBindings

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings *QRhiGles2::createShaderResourceBindings()
    ritual = 'ritual_ZN9QRhiGles228createShaderResourceBindingsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles228createShaderResourceBindingsEv'
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
    Calls Qt's 'QRhiBuffer *QRhiGles2::createBuffer(QRhiBuffer::Type type,
    QRhiBuffer::UsageFlags usage, quint32 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#createBuffer

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
    #  QRhiBuffer *QRhiGles2::createBuffer(QRhiBuffer::Type type,
    #      QRhiBuffer::UsageFlags usage, quint32 size)
    ritual = (
        'ritual_ZN9QRhiGles212createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9'
        'UsageFlagEEj')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles212createBufferEN10QRhiBuffer4TypeE6QFlags'
          'INS0_9UsageFlagEEj')
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
    *QRhiGles2::createRenderBuffer(QRhiRenderBuffer::Type type, const QSize
    &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
    QRhiTexture::Format backingFormatHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#createRenderBuffer

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
    #  QRhiRenderBuffer *QRhiGles2::createRenderBuffer(QRhiRenderBuffer::Type
    #      type, const QSize &pixelSize, int sampleCount,
    #      QRhiRenderBuffer::Flags flags, QRhiTexture::Format
    #      backingFormatHint)
    address = self.uglySide.call(
        'ritual_ZN9QRhiGles218createRenderBufferEN16QRhiRenderBuffer4TypeER'
        'K5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE',
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
    Calls Qt's 'QRhiTexture *QRhiGles2::createTexture(QRhiTexture::Format
    format, const QSize &pixelSize, int depth, int arraySize, int
    sampleCount, QRhiTexture::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#createTexture

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
    #  QRhiTexture *QRhiGles2::createTexture(QRhiTexture::Format format,
    #      const QSize &pixelSize, int depth, int arraySize, int sampleCount,
    #      QRhiTexture::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN9QRhiGles213createTextureEN11QRhiTexture6FormatERK5QSizei'
        'ii6QFlagsINS0_4FlagEE',
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
    Calls Qt's 'QRhiSampler *QRhiGles2::createSampler(QRhiSampler::Filter
    magFilter, QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#createSampler

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
    #  QRhiSampler *QRhiGles2::createSampler(QRhiSampler::Filter magFilter,
    #      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    #      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
    #      QRhiSampler::AddressMode w)
    address = self.uglySide.call(
        'ritual_ZN9QRhiGles213createSamplerEN11QRhiSampler6FilterES1_S1_NS0'
        '_11AddressModeES2_S2_',
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
    *QRhiGles2::createTextureRenderTarget(const
    QRhiTextureRenderTargetDescription &desc, QRhiTextureRenderTarget::Flags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#createTextureRenderTarget

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
    #  QRhiTextureRenderTarget *QRhiGles2::createTextureRenderTarget(const
    #      QRhiTextureRenderTargetDescription &desc,
    #      QRhiTextureRenderTarget::Flags flags)
    ritual = (
        'ritual_ZN9QRhiGles225createTextureRenderTargetERK34QRhiTextureRend'
        'erTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles225createTextureRenderTargetERK34QRhiTextu'
          'reRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4Flag'
          'EE')
    address = self.uglySide.call(ritual, self._valueOf(desc), flags.value)
    return QRhiTextureRenderTarget._cuteAt(address)

  def createShadingRateMap(self) -> Optional[QRhiShadingRateMap]:
    """
    Calls Qt's 'QRhiShadingRateMap *QRhiGles2::createShadingRateMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#createShadingRateMap

    Returns
    -------

    Optional[QRhiShadingRateMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShadingRateMap *QRhiGles2::createShadingRateMap()
    ritual = 'ritual_ZN9QRhiGles220createShadingRateMapEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles220createShadingRateMapEv'
    address = self.uglySide.call(ritual)
    from . import QRhiShadingRateMap
    return QRhiShadingRateMap._cuteAt(address)

  def createSwapChain(self) -> Optional[QRhiSwapChain]:
    """
    Calls Qt's 'QRhiSwapChain *QRhiGles2::createSwapChain()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#createSwapChain

    Returns
    -------

    Optional[QRhiSwapChain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSwapChain *QRhiGles2::createSwapChain()
    ritual = 'ritual_ZN9QRhiGles215createSwapChainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles215createSwapChainEv'
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
    Calls Qt's 'QRhi::FrameOpResult QRhiGles2::endFrame(QRhiSwapChain
    *swapChain, QRhi::EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#endFrame

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
    #  QRhi::FrameOpResult QRhiGles2::endFrame(QRhiSwapChain *swapChain,
    #      QRhi::EndFrameFlags flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN9QRhiGles28endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFr'
        'ameFlagEE',
        self._addressOf(swapChain), flags.value,
    ))

  @overload(QRhi.EndFrameFlags)
  def endOffscreenFrame(
      self,
      flags: QRhi.EndFrameFlags,
  ) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult
    QRhiGles2::endOffscreenFrame(QRhi::EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#endOffscreenFrame

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
    #  QRhi::FrameOpResult QRhiGles2::endOffscreenFrame(QRhi::EndFrameFlags
    #      flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN9QRhiGles217endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFla'
        'gEE',
        flags.value,
    ))

  def finish(self) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult QRhiGles2::finish()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#finish

    Returns
    -------

    QRhi.FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.FrameOpResult(number)' gives.
    """
    #  QRhi::FrameOpResult QRhiGles2::finish()
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN9QRhiGles26finishEv',
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
    Calls Qt's 'void QRhiGles2::resourceUpdate(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#resourceUpdate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::resourceUpdate(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    ritual = (
        'ritual_ZN9QRhiGles214resourceUpdateEP17QRhiCommandBufferP23QRhiRes'
        'ourceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles214resourceUpdateEP17QRhiCommandBufferP23Q'
          'RhiResourceUpdateBatch')
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
    Calls Qt's 'void QRhiGles2::beginPass(QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt, const QColor &colorClearValue, const
    QRhiDepthStencilClearValue &depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#beginPass

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
    #  void QRhiGles2::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
    #      const QColor &colorClearValue, const QRhiDepthStencilClearValue
    #      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    self.uglySide.call(
        'ritual_ZN9QRhiGles29beginPassEP17QRhiCommandBufferP16QRhiRenderTar'
        'getRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBat'
        'ch6QFlagsINS0_13BeginPassFlagEE',
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
    Calls Qt's 'void QRhiGles2::endPass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#endPass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
    #      *resourceUpdates)
    ritual = (
        'ritual_ZN9QRhiGles27endPassEP17QRhiCommandBufferP23QRhiResourceUpd'
        'ateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles27endPassEP17QRhiCommandBufferP23QRhiResou'
          'rceUpdateBatch')
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
    Calls Qt's 'void QRhiGles2::draw(QRhiCommandBuffer *cb, quint32
    vertexCount, quint32 instanceCount, quint32 firstVertex, quint32
    firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#draw

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
    #  void QRhiGles2::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
    #      quint32 instanceCount, quint32 firstVertex, quint32 firstInstance)
    ritual = 'ritual_ZN9QRhiGles24drawEP17QRhiCommandBufferjjjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles24drawEP17QRhiCommandBufferjjjj'
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
    Calls Qt's 'void QRhiGles2::drawIndexed(QRhiCommandBuffer *cb, quint32
    indexCount, quint32 instanceCount, quint32 firstIndex, qint32
    vertexOffset, quint32 firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#drawIndexed

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
    #  void QRhiGles2::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
    #      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
    #      quint32 firstInstance)
    ritual = 'ritual_ZN9QRhiGles211drawIndexedEP17QRhiCommandBufferjjjij'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles211drawIndexedEP17QRhiCommandBufferjjjij')
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
    Calls Qt's 'void QRhiGles2::drawIndirect(QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer, quint32 indirectBufferOffset, quint32
    drawCount, quint32 stride)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#drawIndirect

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
    #  void QRhiGles2::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    #      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
    #      quint32 stride)
    ritual = (
        'ritual_ZN9QRhiGles212drawIndirectEP17QRhiCommandBufferP10QRhiBuffe'
        'rjjj')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles212drawIndirectEP17QRhiCommandBufferP10QRh'
          'iBufferjjj')
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
    Calls Qt's 'void QRhiGles2::drawIndexedIndirect(QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer, quint32 indirectBufferOffset, quint32
    drawCount, quint32 stride)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#drawIndexedIndirect

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
    #  void QRhiGles2::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    #      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
    #      quint32 stride)
    ritual = (
        'ritual_ZN9QRhiGles219drawIndexedIndirectEP17QRhiCommandBufferP10QR'
        'hiBufferjjj')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles219drawIndexedIndirectEP17QRhiCommandBuffe'
          'rP10QRhiBufferjjj')
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
    Calls Qt's 'void QRhiGles2::debugMarkBegin(QRhiCommandBuffer *cb, const
    QByteArray &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#debugMarkBegin

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiGles2::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
    #      &name)
    ritual = (
        'ritual_ZN9QRhiGles214debugMarkBeginEP17QRhiCommandBufferRK10QByteA'
        'rray')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles214debugMarkBeginEP17QRhiCommandBufferRK10'
          'QByteArray')
    self.uglySide.call(ritual, self._addressOf(cb), self._valueOf(name))

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def debugMarkEnd(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiGles2::debugMarkEnd(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#debugMarkEnd

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::debugMarkEnd(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN9QRhiGles212debugMarkEndEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles212debugMarkEndEP17QRhiCommandBuffer'
    self.uglySide.call(ritual, self._addressOf(cb))

  @overload(QRhiCommandBuffer, QByteArray)
  @overload(NoneType, QByteArray)
  def debugMarkMsg(
      self,
      cb: Optional[QRhiCommandBuffer],
      msg: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::debugMarkMsg(QRhiCommandBuffer *cb, const
    QByteArray &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#debugMarkMsg

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    msg : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiGles2::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
    #      &msg)
    ritual = (
        'ritual_ZN9QRhiGles212debugMarkMsgEP17QRhiCommandBufferRK10QByteArr'
        'ay')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles212debugMarkMsgEP17QRhiCommandBufferRK10QB'
          'yteArray')
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
    Calls Qt's 'void QRhiGles2::beginComputePass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#beginComputePass

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
    #  void QRhiGles2::beginComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    ritual = (
        'ritual_ZN9QRhiGles216beginComputePassEP17QRhiCommandBufferP23QRhiR'
        'esourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles216beginComputePassEP17QRhiCommandBufferP2'
          '3QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE')
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
    Calls Qt's 'void QRhiGles2::endComputePass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#endComputePass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::endComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    ritual = (
        'ritual_ZN9QRhiGles214endComputePassEP17QRhiCommandBufferP23QRhiRes'
        'ourceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles214endComputePassEP17QRhiCommandBufferP23Q'
          'RhiResourceUpdateBatch')
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
    Calls Qt's 'void QRhiGles2::dispatch(QRhiCommandBuffer *cb, int x, int y,
    int z)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#dispatch

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
    #  void QRhiGles2::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
    self.uglySide.call(
        'ritual_ZN9QRhiGles28dispatchEP17QRhiCommandBufferiii',
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
    *QRhiGles2::nativeHandles(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#nativeHandles

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
    #  const QRhiNativeHandles *QRhiGles2::nativeHandles(QRhiCommandBuffer
    #      *cb)
    ritual = 'ritual_ZN9QRhiGles213nativeHandlesEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles213nativeHandlesEP17QRhiCommandBuffer'
    address = self.uglySide.call(ritual, self._addressOf(cb))
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload()
  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles *QRhiGles2::nativeHandles()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhiGles2::nativeHandles()
    ritual = 'ritual_ZN9QRhiGles213nativeHandlesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles213nativeHandlesEv'
    address = self.uglySide.call(ritual)
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def beginExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiGles2::beginExternal(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#beginExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::beginExternal(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN9QRhiGles213beginExternalEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def endExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiGles2::endExternal(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#endExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::endExternal(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN9QRhiGles211endExternalEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def lastCompletedGpuTime(self, cb: Optional[QRhiCommandBuffer]) -> float:
    """
    Calls Qt's 'double QRhiGles2::lastCompletedGpuTime(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#lastCompletedGpuTime

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  double QRhiGles2::lastCompletedGpuTime(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN9QRhiGles220lastCompletedGpuTimeEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles220lastCompletedGpuTimeEP17QRhiCommandBuff'
          'er')
    return self.uglySide.call(ritual, self._addressOf(cb))

  def statistics(self) -> QRhiStats:
    """
    Calls Qt's 'QRhiStats QRhiGles2::statistics()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#statistics

    Returns
    -------

    QRhiStats
      A new cute QRhiStats around the copy Qt gave back. Python owns it.
    """
    #  QRhiStats QRhiGles2::statistics()
    ritual = 'ritual_ZN9QRhiGles210statisticsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles210statisticsEv'
    address = self.uglySide.call(ritual)
    from . import QRhiStats
    return QRhiStats._cuteOwning(address)

  def makeThreadLocalNativeContextCurrent(self) -> bool:
    """
    Calls Qt's 'bool QRhiGles2::makeThreadLocalNativeContextCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#makeThreadLocalNativeContextCurrent
    """
    #  bool QRhiGles2::makeThreadLocalNativeContextCurrent()
    ritual = 'ritual_ZN9QRhiGles235makeThreadLocalNativeContextCurrentEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QRhiGles235makeThreadLocalNativeContextCurrentEv')
    return self.uglySide.call(ritual)

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QRhiGles2::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#releaseCachedResources
    """
    #  void QRhiGles2::releaseCachedResources()
    ritual = 'ritual_ZN9QRhiGles222releaseCachedResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QRhiGles222releaseCachedResourcesEv'
    self.uglySide.call(ritual)

  def pipelineCacheData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRhiGles2::pipelineCacheData()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#pipelineCacheData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRhiGles2::pipelineCacheData()
    address = self.uglySide.call('ritual_ZN9QRhiGles217pipelineCacheDataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def executeDeferredReleases(self) -> None:
    """
    Calls Qt's 'void QRhiGles2::executeDeferredReleases()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#executeDeferredReleases
    """
    #  void QRhiGles2::executeDeferredReleases()
    self.uglySide.call('ritual_ZN9QRhiGles223executeDeferredReleasesEv')

  @overload(QGles2CommandBuffer, QGles2Buffer, QGles2Buffer.Access)
  @overload(QGles2CommandBuffer, NoneType, QGles2Buffer.Access)
  @overload(NoneType, QGles2Buffer, QGles2Buffer.Access)
  @overload(NoneType, NoneType, QGles2Buffer.Access)
  def trackedBufferBarrier(
      self,
      cbD: Optional[QGles2CommandBuffer],
      bufD: Optional[QGles2Buffer],
      access: QGles2Buffer.Access,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::trackedBufferBarrier(QGles2CommandBuffer
    *cbD, QGles2Buffer *bufD, QGles2Buffer::Access access)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#trackedBufferBarrier

    Parameters
    ----------

    cbD : Optional[QGles2CommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bufD : Optional[QGles2Buffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    access : QGles2Buffer.Access
      Passed on as its number.
    """
    #  void QRhiGles2::trackedBufferBarrier(QGles2CommandBuffer *cbD,
    #      QGles2Buffer *bufD, QGles2Buffer::Access access)
    self.uglySide.call(
        'ritual_ZN9QRhiGles220trackedBufferBarrierEP19QGles2CommandBufferP1'
        '2QGles2BufferNS2_6AccessE',
        self._addressOf(cbD), self._addressOf(bufD), access.value,
    )

  @overload(QGles2CommandBuffer, QGles2Texture, QGles2Texture.Access)
  @overload(QGles2CommandBuffer, NoneType, QGles2Texture.Access)
  @overload(NoneType, QGles2Texture, QGles2Texture.Access)
  @overload(NoneType, NoneType, QGles2Texture.Access)
  def trackedImageBarrier(
      self,
      cbD: Optional[QGles2CommandBuffer],
      texD: Optional[QGles2Texture],
      access: QGles2Texture.Access,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::trackedImageBarrier(QGles2CommandBuffer *cbD,
    QGles2Texture *texD, QGles2Texture::Access access)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#trackedImageBarrier

    Parameters
    ----------

    cbD : Optional[QGles2CommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    texD : Optional[QGles2Texture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    access : QGles2Texture.Access
      Passed on as its number.
    """
    #  void QRhiGles2::trackedImageBarrier(QGles2CommandBuffer *cbD,
    #      QGles2Texture *texD, QGles2Texture::Access access)
    self.uglySide.call(
        'ritual_ZN9QRhiGles219trackedImageBarrierEP19QGles2CommandBufferP13'
        'QGles2TextureNS2_6AccessE',
        self._addressOf(cbD), self._addressOf(texD), access.value,
    )

  @overload(
      QGles2Texture, QGles2CommandBuffer, int, int,
      QRhiTextureSubresourceUploadDescription,
  )
  @overload(
      QGles2Texture, NoneType, int, int,
      QRhiTextureSubresourceUploadDescription,
  )
  @overload(
      NoneType, QGles2CommandBuffer, int, int,
      QRhiTextureSubresourceUploadDescription,
  )
  @overload(
      NoneType, NoneType, int, int, QRhiTextureSubresourceUploadDescription,
  )
  def enqueueSubresUpload(
      self,
      texD: Optional[QGles2Texture],
      cbD: Optional[QGles2CommandBuffer],
      layer: int,
      level: int,
      subresDesc: QRhiTextureSubresourceUploadDescription,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::enqueueSubresUpload(QGles2Texture *texD,
    QGles2CommandBuffer *cbD, int layer, int level, const
    QRhiTextureSubresourceUploadDescription &subresDesc)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#enqueueSubresUpload

    Parameters
    ----------

    texD : Optional[QGles2Texture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cbD : Optional[QGles2CommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layer : int
      Passed on as it is.

    level : int
      Passed on as it is.

    subresDesc : QRhiTextureSubresourceUploadDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureSubresourceUploadDescription, which stays Python's own.
    """
    #  void QRhiGles2::enqueueSubresUpload(QGles2Texture *texD,
    #      QGles2CommandBuffer *cbD, int layer, int level, const
    #      QRhiTextureSubresourceUploadDescription &subresDesc)
    self.uglySide.call(
        'ritual_ZN9QRhiGles219enqueueSubresUploadEP13QGles2TextureP19QGles2'
        'CommandBufferiiRK39QRhiTextureSubresourceUploadDescription',
        self._addressOf(texD), self._addressOf(cbD), layer, level,
        self._valueOf(subresDesc),
    )

  @overload(QRhiCommandBuffer, QRhiResourceUpdateBatch)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def enqueueResourceUpdates(
      self,
      cb: Optional[QRhiCommandBuffer],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::enqueueResourceUpdates(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#enqueueResourceUpdates

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::enqueueResourceUpdates(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN9QRhiGles222enqueueResourceUpdatesEP17QRhiCommandBufferP2'
        '3QRhiResourceUpdateBatch',
        self._addressOf(cb), self._addressOf(resourceUpdates),
    )

  @overload(
      QRhiPassResourceTracker, QGles2Buffer,
      QRhiPassResourceTracker.BufferAccess,
      QRhiPassResourceTracker.BufferStage,
  )
  @overload(
      QRhiPassResourceTracker, NoneType,
      QRhiPassResourceTracker.BufferAccess,
      QRhiPassResourceTracker.BufferStage,
  )
  @overload(
      NoneType, QGles2Buffer, QRhiPassResourceTracker.BufferAccess,
      QRhiPassResourceTracker.BufferStage,
  )
  @overload(
      NoneType, NoneType, QRhiPassResourceTracker.BufferAccess,
      QRhiPassResourceTracker.BufferStage,
  )
  def trackedRegisterBuffer(
      self,
      passResTracker: Optional[QRhiPassResourceTracker],
      bufD: Optional[QGles2Buffer],
      access: QRhiPassResourceTracker.BufferAccess,
      stage: QRhiPassResourceTracker.BufferStage,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::trackedRegisterBuffer(QRhiPassResourceTracker
    *passResTracker, QGles2Buffer *bufD,
    QRhiPassResourceTracker::BufferAccess access,
    QRhiPassResourceTracker::BufferStage stage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#trackedRegisterBuffer

    Parameters
    ----------

    passResTracker : Optional[QRhiPassResourceTracker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bufD : Optional[QGles2Buffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    access : QRhiPassResourceTracker.BufferAccess
      Passed on as its number.

    stage : QRhiPassResourceTracker.BufferStage
      Passed on as its number.
    """
    #  void QRhiGles2::trackedRegisterBuffer(QRhiPassResourceTracker
    #      *passResTracker, QGles2Buffer *bufD,
    #      QRhiPassResourceTracker::BufferAccess access,
    #      QRhiPassResourceTracker::BufferStage stage)
    self.uglySide.call(
        'ritual_ZN9QRhiGles221trackedRegisterBufferEP23QRhiPassResourceTrac'
        'kerP12QGles2BufferNS0_12BufferAccessENS0_11BufferStageE',
        self._addressOf(passResTracker), self._addressOf(bufD), access.value,
        stage.value,
    )

  @overload(QGles2CommandBuffer)
  @overload(NoneType)
  def enqueueBarriersForPass(
      self,
      cbD: Optional[QGles2CommandBuffer],
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::enqueueBarriersForPass(QGles2CommandBuffer
    *cbD)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#enqueueBarriersForPass

    Parameters
    ----------

    cbD : Optional[QGles2CommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGles2::enqueueBarriersForPass(QGles2CommandBuffer *cbD)
    self.uglySide.call(
        'ritual_ZN9QRhiGles222enqueueBarriersForPassEP19QGles2CommandBuffer',
        self._addressOf(cbD),
    )

  @overload(int)
  def linkProgram(self, program: int) -> bool:
    """
    Calls Qt's 'bool QRhiGles2::linkProgram(GLuint program)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigles2.html#linkProgram

    Parameters
    ----------

    program : int
      Passed on as it is.
    """
    #  bool QRhiGles2::linkProgram(GLuint program)
    return self.uglySide.call('ritual_ZN9QRhiGles211linkProgramEj', program)

  @overload(QShaderDescription, QShaderDescription)
  def sanityCheckVertexFragmentInterface(
      self,
      vsDesc: QShaderDescription,
      fsDesc: QShaderDescription,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::sanityCheckVertexFragmentInterface(const
    QShaderDescription &vsDesc, const QShaderDescription &fsDesc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#sanityCheckVertexFragmentInterface

    Parameters
    ----------

    vsDesc : QShaderDescription
      Passed on as a value: Qt reads the C++ QShaderDescription, which stays
      Python's own.

    fsDesc : QShaderDescription
      Passed on as a value: Qt reads the C++ QShaderDescription, which stays
      Python's own.
    """
    #  void QRhiGles2::sanityCheckVertexFragmentInterface(const
    #      QShaderDescription &vsDesc, const QShaderDescription &fsDesc)
    self.uglySide.call(
        'ritual_ZN9QRhiGles234sanityCheckVertexFragmentInterfaceERK18QShade'
        'rDescriptionS2_',
        self._valueOf(vsDesc), self._valueOf(fsDesc),
    )

  @overload(int, QByteArray)
  @overload(int, QByteArray, bool)
  def trySaveToPipelineCache(
      self,
      program: int,
      cacheKey: QByteArray,
      force: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QRhiGles2::trySaveToPipelineCache(GLuint program, const
    QByteArray &cacheKey, bool force)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigles2.html#trySaveToPipelineCache

    Parameters
    ----------

    program : int
      Passed on as it is.

    cacheKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    force : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QRhiGles2::trySaveToPipelineCache(GLuint program, const
    #      QByteArray &cacheKey, bool force)
    self.uglySide.call(
        'ritual_ZN9QRhiGles222trySaveToPipelineCacheEjRK10QByteArrayb',
        program, self._valueOf(cacheKey), force,
    )

  @staticmethod
  def bindCombinedSampler(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::bindCombinedSampler(QGles2CommandBuffer *cbD,
    QGles2Texture *texD, QGles2Sampler *samplerD, void *ps, uint
    psGeneration, int glslLocation, int *texUnit, bool
    *activeTexUnitAltered)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiGles2.bindCombinedSampler' has no cute function yet. Qt's "
        "'void QRhiGles2::bindCombinedSampler(QGles2CommandBuffer *cbD, "
        "QGles2Texture *texD, QGles2Sampler *samplerD, void *ps, uint "
        "psGeneration, int glslLocation, int *texUnit, bool "
        "*activeTexUnitAltered)': names 'void', which has no cute class yet."
    )

  @staticmethod
  def bindShaderResources(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::bindShaderResources(QGles2CommandBuffer *cbD,
    QRhiGraphicsPipeline *maybeGraphicsPs, QRhiComputePipeline
    *maybeComputePs, QRhiShaderResourceBindings *srb, const uint
    *dynOfsPairs, int dynOfsCount)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qrhi_std140_to_packed'.
    """
    raise NotImplementedError(
        "'QRhiGles2.bindShaderResources' has no cute function yet. Qt's "
        "'void QRhiGles2::bindShaderResources(QGles2CommandBuffer *cbD, "
        "QRhiGraphicsPipeline *maybeGraphicsPs, QRhiComputePipeline "
        "*maybeComputePs, QRhiShaderResourceBindings *srb, const uint "
        "*dynOfsPairs, int dynOfsCount)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'qrhi_std140_to_packed'.")

  @staticmethod
  def commonGlslEsVersion(*__, **_) -> Never:
    """
    Qt's 'std::optional<QShaderVersion> QRhiGles2::commonGlslEsVersion(const
    QRhiShaderStage *stages, int stageCount) const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QRhiGles2.commonGlslEsVersion' has no cute function yet. Qt's "
        "'std::optional<QShaderVersion> "
        "QRhiGles2::commonGlslEsVersion(const QRhiShaderStage *stages, int "
        "stageCount) const': gives a type Python has no way to take yet.")

  @staticmethod
  def compileShader(*__, **_) -> Never:
    """
    Qt's 'bool QRhiGles2::compileShader(GLuint program, const QRhiShaderStage
    &shaderStage, QShaderVersion *shaderVersion,
    std::optional<QShaderVersion> commonVersion)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QRhiGles2.compileShader' has no cute function yet. Qt's 'bool "
        "QRhiGles2::compileShader(GLuint program, const QRhiShaderStage "
        "&shaderStage, QShaderVersion *shaderVersion, "
        "std::optional<QShaderVersion> commonVersion)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def enqueueBindFramebuffer(*__, **_) -> Never:
    """
    Qt's 'QGles2RenderTargetData
    *QRhiGles2::enqueueBindFramebuffer(QRhiRenderTarget *rt,
    QGles2CommandBuffer *cbD, bool *wantsColorClear, bool *wantsDsClear)':
    leans on 'QRhiGles2::trackedRegisterTexture(QRhiPassResourceTracker*,
    QGles2Texture*, QRhiPassResourceTracker::TextureAccess,
    QRhiPassResourceTracker::TextureStage)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRhiGles2.enqueueBindFramebuffer' has no cute function yet. Qt's "
        "'QGles2RenderTargetData "
        "*QRhiGles2::enqueueBindFramebuffer(QRhiRenderTarget *rt, "
        "QGles2CommandBuffer *cbD, bool *wantsColorClear, bool "
        "*wantsDsClear)': leans on "
        "'QRhiGles2::trackedRegisterTexture(QRhiPassResourceTracker*, "
        "QGles2Texture*, QRhiPassResourceTracker::TextureAccess, "
        "QRhiPassResourceTracker::TextureStage)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def ensureContext(*__, **_) -> Never:
    """
    Qt's 'bool QRhiGles2::ensureContext(QSurface *surface) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'currentSurfaceForCurrentContext'.
    """
    raise NotImplementedError(
        "'QRhiGles2.ensureContext' has no cute function yet. Qt's 'bool "
        "QRhiGles2::ensureContext(QSurface *surface) const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'currentSurfaceForCurrentContext'.")

  @staticmethod
  def executeBindGraphicsPipeline(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::executeBindGraphicsPipeline(QGles2CommandBuffer
    *cbD, QGles2GraphicsPipeline *psD)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'toGlBlendFactor'; did you mean 'VkBlendFactor'?.
    """
    raise NotImplementedError(
        "'QRhiGles2.executeBindGraphicsPipeline' has no cute function yet. "
        "Qt's 'void "
        "QRhiGles2::executeBindGraphicsPipeline(QGles2CommandBuffer *cbD, "
        "QGles2GraphicsPipeline *psD)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'toGlBlendFactor'; did you mean "
        "'VkBlendFactor'?.")

  @staticmethod
  def executeCommandBuffer(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::executeCommandBuffer(QRhiCommandBuffer *cb)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'CommandBufferExecTrackedState'.
    """
    raise NotImplementedError(
        "'QRhiGles2.executeCommandBuffer' has no cute function yet. Qt's "
        "'void QRhiGles2::executeCommandBuffer(QRhiCommandBuffer *cb)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'CommandBufferExecTrackedState'.")

  @staticmethod
  def gatherGeneratedSamplers(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::gatherGeneratedSamplers(GLuint program, const
    QShader::SeparateToCombinedImageSamplerMapping &mapping,
    QGles2SamplerDescriptionVector *dst)': names
    'QGles2SamplerDescriptionVector', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiGles2.gatherGeneratedSamplers' has no cute function yet. Qt's "
        "'void QRhiGles2::gatherGeneratedSamplers(GLuint program, const "
        "QShader::SeparateToCombinedImageSamplerMapping &mapping, "
        "QGles2SamplerDescriptionVector *dst)': names "
        "'QGles2SamplerDescriptionVector', which has no cute class yet.")

  @staticmethod
  def gatherSamplers(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::gatherSamplers(GLuint program, const
    QShaderDescription::InOutVariable &v, QGles2SamplerDescriptionVector
    *dst)': names 'QGles2SamplerDescriptionVector', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QRhiGles2.gatherSamplers' has no cute function yet. Qt's 'void "
        "QRhiGles2::gatherSamplers(GLuint program, const "
        "QShaderDescription::InOutVariable &v, "
        "QGles2SamplerDescriptionVector *dst)': names "
        "'QGles2SamplerDescriptionVector', which has no cute class yet.")

  @staticmethod
  def gatherUniforms(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::gatherUniforms(GLuint program, const
    QShaderDescription::UniformBlock &ub, ActiveUniformLocationTracker
    *activeUniformLocations, QGles2UniformDescriptionVector *dst)': names
    'QRhiGles2::ActiveUniformLocationTracker', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiGles2.gatherUniforms' has no cute function yet. Qt's 'void "
        "QRhiGles2::gatherUniforms(GLuint program, const "
        "QShaderDescription::UniformBlock &ub, ActiveUniformLocationTracker "
        "*activeUniformLocations, QGles2UniformDescriptionVector *dst)': "
        "names 'QRhiGles2::ActiveUniformLocationTracker', which has no cute "
        "class yet.")

  @staticmethod
  def registerUniformIfActive(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::registerUniformIfActive(const
    QShaderDescription::BlockVariable &var, const QByteArray &namePrefix, int
    binding, int baseOffset, GLuint program, ActiveUniformLocationTracker
    *activeUniformLocations, QGles2UniformDescriptionVector *dst)': names
    'QRhiGles2::ActiveUniformLocationTracker', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiGles2.registerUniformIfActive' has no cute function yet. Qt's "
        "'void QRhiGles2::registerUniformIfActive(const "
        "QShaderDescription::BlockVariable &var, const QByteArray "
        "&namePrefix, int binding, int baseOffset, GLuint program, "
        "ActiveUniformLocationTracker *activeUniformLocations, "
        "QGles2UniformDescriptionVector *dst)': names "
        "'QRhiGles2::ActiveUniformLocationTracker', which has no cute class "
        "yet.")

  @staticmethod
  def shaderSource(*__, **_) -> Never:
    """
    Qt's 'QByteArray QRhiGles2::shaderSource(const QRhiShaderStage
    &shaderStage, QShaderVersion *shaderVersion,
    std::optional<QShaderVersion> commonVersion)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QRhiGles2.shaderSource' has no cute function yet. Qt's "
        "'QByteArray QRhiGles2::shaderSource(const QRhiShaderStage "
        "&shaderStage, QShaderVersion *shaderVersion, "
        "std::optional<QShaderVersion> commonVersion)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def trackedRegisterTexture(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::trackedRegisterTexture(QRhiPassResourceTracker
    *passResTracker, QGles2Texture *texD,
    QRhiPassResourceTracker::TextureAccess access,
    QRhiPassResourceTracker::TextureStage stage)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'toPassTrackerUsageState'; did you mean
    'QRhiPassResourceTracker::toPassTrackerBufferStage'?.
    """
    raise NotImplementedError(
        "'QRhiGles2.trackedRegisterTexture' has no cute function yet. Qt's "
        "'void QRhiGles2::trackedRegisterTexture(QRhiPassResourceTracker "
        "*passResTracker, QGles2Texture *texD, "
        "QRhiPassResourceTracker::TextureAccess access, "
        "QRhiPassResourceTracker::TextureStage stage)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'toPassTrackerUsageState'; did you mean "
        "'QRhiPassResourceTracker::toPassTrackerBufferStage'?.")

  @staticmethod
  def tryLoadFromDiskOrPipelineCache(*__, **_) -> Never:
    """
    Qt's 'ProgramCacheResult QRhiGles2::tryLoadFromDiskOrPipelineCache(const
    QRhiShaderStage *stages, int stageCount, GLuint program, const
    QVector<QShaderDescription::InOutVariable> &inputVars, QByteArray
    *cacheKey, std::optional<QShaderVersion> commonVersion)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'isGraphicsStage'.
    """
    raise NotImplementedError(
        "'QRhiGles2.tryLoadFromDiskOrPipelineCache' has no cute function "
        "yet. Qt's 'ProgramCacheResult "
        "QRhiGles2::tryLoadFromDiskOrPipelineCache(const QRhiShaderStage "
        "*stages, int stageCount, GLuint program, const "
        "QVector<QShaderDescription::InOutVariable> &inputVars, QByteArray "
        "*cacheKey, std::optional<QShaderVersion> commonVersion)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'isGraphicsStage'.")

  @staticmethod
  def trySaveToDiskCache(*__, **_) -> Never:
    """
    Qt's 'void QRhiGles2::trySaveToDiskCache(GLuint program, const QByteArray
    &cacheKey)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'qrhi_programBinaryCache'.
    """
    raise NotImplementedError(
        "'QRhiGles2.trySaveToDiskCache' has no cute function yet. Qt's "
        "'void QRhiGles2::trySaveToDiskCache(GLuint program, const "
        "QByteArray &cacheKey)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qrhi_programBinaryCache'.")
