"""
QRhiImplementation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QRhiImplementation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QRhi, QRhiBuffer, QRhiCommandBuffer, QRhiRenderBuffer
from . import QRhiSampler, QRhiShaderResourceBinding, QRhiTexture
from . import QRhiTextureRenderTarget, QRhiVertexInputAttribute
from . import QShaderDescription

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QPoint, QSize
  from . import QColor, QMatrix4x4, QRhiAdapter, QRhiComputePipeline
  from . import QRhiDepthStencilClearValue, QRhiDriverInfo
  from . import QRhiGraphicsPipeline, QRhiNativeHandles, QRhiRenderTarget
  from . import QRhiResource, QRhiResourceUpdateBatch, QRhiScissor
  from . import QRhiShaderResourceBindings, QRhiShadingRateMap, QRhiStats
  from . import QRhiSwapChain, QRhiTextureRenderTargetDescription
  from . import QRhiViewport
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QPoint = WAIT['QPoint']
  QRhiAdapter = WAIT['QRhiAdapter']
  QRhiComputePipeline = WAIT['QRhiComputePipeline']
  QRhiDepthStencilClearValue = WAIT['QRhiDepthStencilClearValue']
  QRhiGraphicsPipeline = WAIT['QRhiGraphicsPipeline']
  QRhiNativeHandles = WAIT['QRhiNativeHandles']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QRhiResource = WAIT['QRhiResource']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiScissor = WAIT['QRhiScissor']
  QRhiShaderResourceBindings = WAIT['QRhiShaderResourceBindings']
  QRhiSwapChain = WAIT['QRhiSwapChain']
  QRhiTextureRenderTargetDescription = WAIT['QRhiTextureRenderTargetDescription']
  QRhiViewport = WAIT['QRhiViewport']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiImplementation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiImplementation: a plain Python object standing in
  front of one C++ QRhiImplementation.

  What exists
  -----------

  Every function of Qt's QRhiImplementation that has a ritual and that Python
  can call so far, 78 names in all: 'create', 'destroy',
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
  'endExternal', 'lastCompletedGpuTime', 'ubufAlignment',
  'supportedShadingRates', 'isYUpInFramebuffer', 'isYUpInNDC',
  'isClipDepthZeroToOne', 'clipSpaceCorrMatrix', 'isTextureFormatSupported',
  'isFeatureSupported', 'resourceLimit', 'driverInfo', 'statistics',
  'makeThreadLocalNativeContextCurrent', 'setQueueSubmitParams',
  'releaseCachedResources', 'isDeviceLost', 'pipelineCacheData',
  'setPipelineCacheData', 'prepareForCreate', 'isCompressedFormat',
  'isStencilSupportingFormat', 'registerResource', 'unregisterResource',
  'addDeleteLater', 'sanityCheckGraphicsPipeline',
  'sanityCheckShaderResourceBindings', 'sanityCheckResourceOwnership',
  'updateLayoutDesc', 'pipelineCacheRhiId', 'pipelineCreationStart',
  'pipelineCreationEnd', 'totalPipelineCreationTime',
  'shaderDescVariableFormatToVertexInputFormat',
  'byteSizePerVertexForVertexInputFormat', 'shaderResourceBindingData',
  'sortedBindingLessThan', 'clampedSubResourceUploadSize',
  'clampedSubResourceUploadSizeForSourceData', 'runCleanup'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiImplementation::~QRhiImplementation()': the destructor: Python
    never removes a C++ QRhiImplementation.
  - Qt's 'QRhi::FrameOpResult QRhiImplementation::beginFrame(QRhiSwapChain
    *swapChain, QRhi::BeginFrameFlags flags)': names the enum
    'QRhi::BeginFrameFlag', whose class cannot be named here.
  - Qt's 'QRhi::FrameOpResult
    QRhiImplementation::beginOffscreenFrame(QRhiCommandBuffer **cb,
    QRhi::BeginFrameFlags flags)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QRhiImplementation::setShaderResources(QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb, int dynamicOffsetCount, const
    QRhiCommandBuffer::DynamicOffset *dynamicOffsets)': names
    'QRhiCommandBuffer::DynamicOffset', which has no cute class yet.
  - Qt's 'void QRhiImplementation::setVertexInput(QRhiCommandBuffer *cb, int
    startBinding, int bindingCount, const QRhiCommandBuffer::VertexInput
    *bindings, QRhiBuffer *indexBuf, quint32 indexOffset,
    QRhiCommandBuffer::IndexFormat indexFormat)': names
    'QRhiCommandBuffer::VertexInput', which has no cute class yet.
  - Qt's 'QList<int> QRhiImplementation::supportedSampleCounts() const':
    gives a type Python has no way to take yet.
  - Qt's 'bool QRhiImplementation::compressedFormatInfo(QRhiTexture::Format
    format, const QSize &size, quint32 *bpl, quint32 *byteSize, QSize
    *blockDim) const': takes a number to change where it is.
  - Qt's 'bool QRhiImplementation::textureFormatInfo(QRhiTexture::Format
    format, const QSize &size, quint32 *bpl, quint32 *byteSize, quint32
    *bytesPerPixel) const': takes a number to change where it is.
  - Qt's 'void QRhiImplementation::addCleanupCallback(const
    QRhi::CleanupCallback &callback)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QRhiImplementation::addCleanupCallback(const void *key, const
    QRhi::CleanupCallback &callback)': names 'void', which has no cute class
    yet.
  - Qt's 'void QRhiImplementation::removeCleanupCallback(const void *key)':
    names 'void', which has no cute class yet.
  - Qt's 'QRhiShaderResourceBinding::Data
    *QRhiImplementation::shaderResourceBindingData(QRhiShaderResourceBinding
    &binding)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 93 functions Qt declares: 1 leans on 'QRhiMetal; 1 leans on
  'QRHI_LOG_INFO()', which Qt's source does not mark for use from outside Qt
  and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QRhiImplementation is created at the first use, not by
    'QRhiImplementation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiImplementation.
  - Each name of Qt's QRhiImplementation that has no cute function yet,
    'addCleanupCallback', 'beginFrame', 'beginOffscreenFrame',
    'compressedFormatInfo', 'effectiveSampleCount', 'newInstance',
    'removeCleanupCallback', 'setShaderResources', 'setVertexInput',
    'supportedSampleCounts', 'textureFormatInfo', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRhiShaderResourceBinding)
  def shaderResourceBindingData(
      binding: QRhiShaderResourceBinding,
  ) -> Optional[QRhiShaderResourceBinding.Data]:
    """
    Calls Qt's 'const QRhiShaderResourceBinding::Data
    *QRhiImplementation::shaderResourceBindingData(const
    QRhiShaderResourceBinding &binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#shaderResourceBindingData

    Parameters
    ----------

    binding : QRhiShaderResourceBinding
      Passed on as a value: Qt reads the C++ QRhiShaderResourceBinding, which
      stays Python's own.

    Returns
    -------

    Optional[QRhiShaderResourceBinding.Data]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderResourceBinding::Data
    #      *QRhiImplementation::shaderResourceBindingData(const
    #      QRhiShaderResourceBinding &binding)
    address = Rituals.call(
        'ritual_ZN18QRhiImplementation25shaderResourceBindingDataERK25QRhiS'
        'haderResourceBinding',
        CuteMixin._valueOf(binding),
    )
    return QRhiShaderResourceBinding.Data._cuteAt(address)

  @staticmethod
  @overload(QRhiShaderResourceBinding, QRhiShaderResourceBinding)
  def sortedBindingLessThan(
      a: QRhiShaderResourceBinding,
      b: QRhiShaderResourceBinding,
  ) -> bool:
    """
    Calls Qt's 'bool QRhiImplementation::sortedBindingLessThan(const
    QRhiShaderResourceBinding &a, const QRhiShaderResourceBinding &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#sortedBindingLessThan

    Parameters
    ----------

    a : QRhiShaderResourceBinding
      Passed on as a value: Qt reads the C++ QRhiShaderResourceBinding, which
      stays Python's own.

    b : QRhiShaderResourceBinding
      Passed on as a value: Qt reads the C++ QRhiShaderResourceBinding, which
      stays Python's own.
    """
    #  bool QRhiImplementation::sortedBindingLessThan(const
    #      QRhiShaderResourceBinding &a, const QRhiShaderResourceBinding &b)
    return Rituals.call(
        'ritual_ZN18QRhiImplementation21sortedBindingLessThanERK25QRhiShade'
        'rResourceBindingS2_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiImplementation'

  #  A C++ QRhiImplementation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiImplementation'

  #  The functions Qt calls itself that QRhiImplementation is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'enumerateAdaptersBeforeCreate': (
          'QRhi::AdapterList '
          'QRhiImplementation::enumerateAdaptersBeforeCreate(QRhiNativeHand'
          'les *) const',
      ),
      'beginOffscreenFrame': (
          'QRhi::FrameOpResult '
          'QRhiImplementation::beginOffscreenFrame(QRhiCommandBuffer **, '
          'QRhi::BeginFrameFlags)',
      ),
      'setShaderResources': (
          'void QRhiImplementation::setShaderResources(QRhiCommandBuffer '
          '*, QRhiShaderResourceBindings *, int, const '
          'QRhiCommandBuffer::DynamicOffset *)',
      ),
      'setVertexInput': (
          'void QRhiImplementation::setVertexInput(QRhiCommandBuffer *, '
          'int, int, const QRhiCommandBuffer::VertexInput *, QRhiBuffer *, '
          'quint32, QRhiCommandBuffer::IndexFormat)',
      ),
      'supportedSampleCounts': (
          'QList<int> QRhiImplementation::supportedSampleCounts() const',
      ),
      'supportedShadingRates': (
          'QList<QSize> QRhiImplementation::supportedShadingRates(int) '
          'const',
      ),
  }

  #  The functions Qt calls itself that QRhiImplementation is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN18QRhiImplementation6createE6QFlagsIN4QRhi4FlagEE',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtGui:QRhi.Flag'),
           )),
      ),
      'destroy': (
          ('_ZN18QRhiImplementation7destroyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'createGraphicsPipeline': (
          ('_ZN18QRhiImplementation22createGraphicsPipelineEv',
           ('address', 'address', 'QtGui:QRhiGraphicsPipeline'),
           ()),
      ),
      'createComputePipeline': (
          ('_ZN18QRhiImplementation21createComputePipelineEv',
           ('address', 'address', 'QtGui:QRhiComputePipeline'),
           ()),
      ),
      'createShaderResourceBindings': (
          ('_ZN18QRhiImplementation28createShaderResourceBindingsEv',
           ('address', 'address', 'QtGui:QRhiShaderResourceBindings'),
           ()),
      ),
      'createBuffer': (
          ('_ZN18QRhiImplementation12createBufferEN10QRhiBuffer4TypeE6QFlag'
           'sINS0_9UsageFlagEEj',
           ('address', 'address', 'QtGui:QRhiBuffer'),
           (
               ('int', 'enum', 'QtGui:QRhiBuffer.Type'),
               ('int', 'flags', 'QtGui:QRhiBuffer.UsageFlag'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'createRenderBuffer': (
          ('_ZN18QRhiImplementation18createRenderBufferEN16QRhiRenderBuffer'
           '4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE',
           ('address', 'address', 'QtGui:QRhiRenderBuffer'),
           (
               ('int', 'enum', 'QtGui:QRhiRenderBuffer.Type'),
               ('address', 'value', 'QtCore:QSize'),
               ('int', 'number', ''),
               ('int', 'flags', 'QtGui:QRhiRenderBuffer.Flag'),
               ('int', 'enum', 'QtGui:QRhiTexture.Format'),
           )),
      ),
      'createTexture': (
          ('_ZN18QRhiImplementation13createTextureEN11QRhiTexture6FormatERK'
           '5QSizeiii6QFlagsINS0_4FlagEE',
           ('address', 'address', 'QtGui:QRhiTexture'),
           (
               ('int', 'enum', 'QtGui:QRhiTexture.Format'),
               ('address', 'value', 'QtCore:QSize'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'flags', 'QtGui:QRhiTexture.Flag'),
           )),
      ),
      'createSampler': (
          ('_ZN18QRhiImplementation13createSamplerEN11QRhiSampler6FilterES1'
           '_S1_NS0_11AddressModeES2_S2_',
           ('address', 'address', 'QtGui:QRhiSampler'),
           (
               ('int', 'enum', 'QtGui:QRhiSampler.Filter'),
               ('int', 'enum', 'QtGui:QRhiSampler.Filter'),
               ('int', 'enum', 'QtGui:QRhiSampler.Filter'),
               ('int', 'enum', 'QtGui:QRhiSampler.AddressMode'),
               ('int', 'enum', 'QtGui:QRhiSampler.AddressMode'),
               ('int', 'enum', 'QtGui:QRhiSampler.AddressMode'),
           )),
      ),
      'createTextureRenderTarget': (
          ('_ZN18QRhiImplementation25createTextureRenderTargetERK34QRhiText'
           'ureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4Fl'
           'agEE',
           ('address', 'address', 'QtGui:QRhiTextureRenderTarget'),
           (
               ('address', 'value',
                'QtGui:QRhiTextureRenderTargetDescription'),
               ('int', 'flags', 'QtGui:QRhiTextureRenderTarget.Flag'),
           )),
      ),
      'createShadingRateMap': (
          ('_ZN18QRhiImplementation20createShadingRateMapEv',
           ('address', 'address', 'QtGui:QRhiShadingRateMap'),
           ()),
      ),
      'createSwapChain': (
          ('_ZN18QRhiImplementation15createSwapChainEv',
           ('address', 'address', 'QtGui:QRhiSwapChain'),
           ()),
      ),
      'beginFrame': (
          ('_ZN18QRhiImplementation10beginFrameEP13QRhiSwapChain6QFlagsIN4Q'
           'Rhi14BeginFrameFlagEE',
           ('int', 'enum', 'QtGui:QRhi.FrameOpResult'),
           (
               ('address', 'address', 'QtGui:QRhiSwapChain'),
               ('int', 'flags', 'QtGui:QRhi.BeginFrameFlag'),
           )),
      ),
      'endFrame': (
          ('_ZN18QRhiImplementation8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi'
           '12EndFrameFlagEE',
           ('int', 'enum', 'QtGui:QRhi.FrameOpResult'),
           (
               ('address', 'address', 'QtGui:QRhiSwapChain'),
               ('int', 'flags', 'QtGui:QRhi.EndFrameFlag'),
           )),
      ),
      'endOffscreenFrame': (
          ('_ZN18QRhiImplementation17endOffscreenFrameE6QFlagsIN4QRhi12EndF'
           'rameFlagEE',
           ('int', 'enum', 'QtGui:QRhi.FrameOpResult'),
           (
               ('int', 'flags', 'QtGui:QRhi.EndFrameFlag'),
           )),
      ),
      'finish': (
          ('_ZN18QRhiImplementation6finishEv',
           ('int', 'enum', 'QtGui:QRhi.FrameOpResult'),
           ()),
      ),
      'resourceUpdate': (
          ('_ZN18QRhiImplementation14resourceUpdateEP17QRhiCommandBufferP23'
           'QRhiResourceUpdateBatch',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'address', 'QtGui:QRhiResourceUpdateBatch'),
           )),
      ),
      'beginPass': (
          ('_ZN18QRhiImplementation9beginPassEP17QRhiCommandBufferP16QRhiRe'
           'nderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourc'
           'eUpdateBatch6QFlagsINS0_13BeginPassFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'address', 'QtGui:QRhiRenderTarget'),
               ('address', 'value', 'QtGui:QColor'),
               ('address', 'value', 'QtGui:QRhiDepthStencilClearValue'),
               ('address', 'address', 'QtGui:QRhiResourceUpdateBatch'),
               ('int', 'flags', 'QtGui:QRhiCommandBuffer.BeginPassFlag'),
           )),
      ),
      'endPass': (
          ('_ZN18QRhiImplementation7endPassEP17QRhiCommandBufferP23QRhiReso'
           'urceUpdateBatch',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'address', 'QtGui:QRhiResourceUpdateBatch'),
           )),
      ),
      'setGraphicsPipeline': (
          ('_ZN18QRhiImplementation19setGraphicsPipelineEP17QRhiCommandBuff'
           'erP20QRhiGraphicsPipeline',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'address', 'QtGui:QRhiGraphicsPipeline'),
           )),
      ),
      'setViewport': (
          ('_ZN18QRhiImplementation11setViewportEP17QRhiCommandBufferRK12QR'
           'hiViewport',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'value', 'QtGui:QRhiViewport'),
           )),
      ),
      'setScissor': (
          ('_ZN18QRhiImplementation10setScissorEP17QRhiCommandBufferRK11QRh'
           'iScissor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'value', 'QtGui:QRhiScissor'),
           )),
      ),
      'setBlendConstants': (
          ('_ZN18QRhiImplementation17setBlendConstantsEP17QRhiCommandBuffer'
           'RK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'setStencilRef': (
          ('_ZN18QRhiImplementation13setStencilRefEP17QRhiCommandBufferj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'setShadingRate': (
          ('_ZN18QRhiImplementation14setShadingRateEP17QRhiCommandBufferRK5'
           'QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'draw': (
          ('_ZN18QRhiImplementation4drawEP17QRhiCommandBufferjjjj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'drawIndexed': (
          ('_ZN18QRhiImplementation11drawIndexedEP17QRhiCommandBufferjjjij',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
               ('int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'drawIndirect': (
          ('_ZN18QRhiImplementation12drawIndirectEP17QRhiCommandBufferP10QR'
           'hiBufferjjj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'address', 'QtGui:QRhiBuffer'),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'drawIndexedIndirect': (
          ('_ZN18QRhiImplementation19drawIndexedIndirectEP17QRhiCommandBuff'
           'erP10QRhiBufferjjj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'address', 'QtGui:QRhiBuffer'),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'debugMarkBegin': (
          ('_ZN18QRhiImplementation14debugMarkBeginEP17QRhiCommandBufferRK1'
           '0QByteArray',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'debugMarkEnd': (
          ('_ZN18QRhiImplementation12debugMarkEndEP17QRhiCommandBuffer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
      ),
      'debugMarkMsg': (
          ('_ZN18QRhiImplementation12debugMarkMsgEP17QRhiCommandBufferRK10Q'
           'ByteArray',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'beginComputePass': (
          ('_ZN18QRhiImplementation16beginComputePassEP17QRhiCommandBufferP'
           '23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'address', 'QtGui:QRhiResourceUpdateBatch'),
               ('int', 'flags', 'QtGui:QRhiCommandBuffer.BeginPassFlag'),
           )),
      ),
      'endComputePass': (
          ('_ZN18QRhiImplementation14endComputePassEP17QRhiCommandBufferP23'
           'QRhiResourceUpdateBatch',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'address', 'QtGui:QRhiResourceUpdateBatch'),
           )),
      ),
      'setComputePipeline': (
          ('_ZN18QRhiImplementation18setComputePipelineEP17QRhiCommandBuffe'
           'rP19QRhiComputePipeline',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('address', 'address', 'QtGui:QRhiComputePipeline'),
           )),
      ),
      'dispatch': (
          ('_ZN18QRhiImplementation8dispatchEP17QRhiCommandBufferiii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'nativeHandles': (
          ('_ZN18QRhiImplementation13nativeHandlesEP17QRhiCommandBuffer',
           ('address', 'address', 'QtGui:QRhiNativeHandles'),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
          ('_ZN18QRhiImplementation13nativeHandlesEv',
           ('address', 'address', 'QtGui:QRhiNativeHandles'),
           ()),
      ),
      'beginExternal': (
          ('_ZN18QRhiImplementation13beginExternalEP17QRhiCommandBuffer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
      ),
      'endExternal': (
          ('_ZN18QRhiImplementation11endExternalEP17QRhiCommandBuffer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
      ),
      'lastCompletedGpuTime': (
          ('_ZN18QRhiImplementation20lastCompletedGpuTimeEP17QRhiCommandBuf'
           'fer',
           ('double', 'number', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
      ),
      'ubufAlignment': (
          ('_ZNK18QRhiImplementation13ubufAlignmentEv',
           ('int', 'number', ''),
           ()),
      ),
      'isYUpInFramebuffer': (
          ('_ZNK18QRhiImplementation18isYUpInFramebufferEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isYUpInNDC': (
          ('_ZNK18QRhiImplementation10isYUpInNDCEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isClipDepthZeroToOne': (
          ('_ZNK18QRhiImplementation20isClipDepthZeroToOneEv',
           ('bool', 'number', ''),
           ()),
      ),
      'clipSpaceCorrMatrix': (
          ('_ZNK18QRhiImplementation19clipSpaceCorrMatrixEv',
           ('address', 'value', 'QtGui:QMatrix4x4'),
           ()),
      ),
      'isTextureFormatSupported': (
          ('_ZNK18QRhiImplementation24isTextureFormatSupportedEN11QRhiTextu'
           're6FormatE6QFlagsINS0_4FlagEE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QRhiTexture.Format'),
               ('int', 'flags', 'QtGui:QRhiTexture.Flag'),
           )),
      ),
      'isFeatureSupported': (
          ('_ZNK18QRhiImplementation18isFeatureSupportedEN4QRhi7FeatureE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QRhi.Feature'),
           )),
      ),
      'resourceLimit': (
          ('_ZNK18QRhiImplementation13resourceLimitEN4QRhi13ResourceLimitE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QRhi.ResourceLimit'),
           )),
      ),
      'driverInfo': (
          ('_ZNK18QRhiImplementation10driverInfoEv',
           ('address', 'value', 'QtGui:QRhiDriverInfo'),
           ()),
      ),
      'statistics': (
          ('_ZN18QRhiImplementation10statisticsEv',
           ('address', 'value', 'QtGui:QRhiStats'),
           ()),
      ),
      'makeThreadLocalNativeContextCurrent': (
          ('_ZN18QRhiImplementation35makeThreadLocalNativeContextCurrentEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setQueueSubmitParams': (
          ('_ZN18QRhiImplementation20setQueueSubmitParamsEP17QRhiNativeHand'
           'les',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiNativeHandles'),
           )),
      ),
      'releaseCachedResources': (
          ('_ZN18QRhiImplementation22releaseCachedResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isDeviceLost': (
          ('_ZNK18QRhiImplementation12isDeviceLostEv',
           ('bool', 'number', ''),
           ()),
      ),
      'pipelineCacheData': (
          ('_ZN18QRhiImplementation17pipelineCacheDataEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'setPipelineCacheData': (
          ('_ZN18QRhiImplementation20setPipelineCacheDataERK10QByteArray',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
  }

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
    QRhiImplementation::enumerateAdaptersBeforeCreate(QRhiNativeHandles
    *nativeHandles) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html

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
    #  QRhi::AdapterList QRhiImplementation::enumerateAdaptersBeforeCreate(
    #      QRhiNativeHandles *nativeHandles) const
    address = self.uglySide.call(
        'ritual_ZNK18QRhiImplementation29enumerateAdaptersBeforeCreateEP17Q'
        'RhiNativeHandles',
        self._addressOf(nativeHandles),
    )
    from . import QRhiAdapter
    return QList[QRhiAdapter]._cuteOwning(address)

  def ubufAlignment(self) -> int:
    """
    Calls Qt's 'int QRhiImplementation::ubufAlignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#ubufAlignment
    """
    #  int QRhiImplementation::ubufAlignment() const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation13ubufAlignmentEv',
    )

  @overload(int)
  def supportedShadingRates(self, sampleCount: int) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QRhiImplementation::supportedShadingRates(int
    sampleCount) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#supportedShadingRates

    Parameters
    ----------

    sampleCount : int
      Passed on as it is.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QRhiImplementation::supportedShadingRates(int
    #      sampleCount) const
    address = self.uglySide.call(
        'ritual_ZNK18QRhiImplementation21supportedShadingRatesEi',
        sampleCount,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  def isYUpInFramebuffer(self) -> bool:
    """
    Calls Qt's 'bool QRhiImplementation::isYUpInFramebuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#isYUpInFramebuffer
    """
    #  bool QRhiImplementation::isYUpInFramebuffer() const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation18isYUpInFramebufferEv',
    )

  def isYUpInNDC(self) -> bool:
    """
    Calls Qt's 'bool QRhiImplementation::isYUpInNDC() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#isYUpInNDC
    """
    #  bool QRhiImplementation::isYUpInNDC() const
    return self.uglySide.call('ritual_ZNK18QRhiImplementation10isYUpInNDCEv')

  def isClipDepthZeroToOne(self) -> bool:
    """
    Calls Qt's 'bool QRhiImplementation::isClipDepthZeroToOne() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#isClipDepthZeroToOne
    """
    #  bool QRhiImplementation::isClipDepthZeroToOne() const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation20isClipDepthZeroToOneEv',
    )

  def clipSpaceCorrMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QRhiImplementation::clipSpaceCorrMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#clipSpaceCorrMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QRhiImplementation::clipSpaceCorrMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK18QRhiImplementation19clipSpaceCorrMatrixEv',
    )
    from . import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QRhiTexture.Format, QRhiTexture.Flags)
  def isTextureFormatSupported(
      self,
      format: QRhiTexture.Format,
      flags: QRhiTexture.Flags,
  ) -> bool:
    """
    Calls Qt's 'bool
    QRhiImplementation::isTextureFormatSupported(QRhiTexture::Format format,
    QRhiTexture::Flags flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#isTextureFormatSupported

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    flags : QRhiTexture.Flags
      Passed on as its number.
    """
    #  bool QRhiImplementation::isTextureFormatSupported(QRhiTexture::Format
    #      format, QRhiTexture::Flags flags) const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation24isTextureFormatSupportedEN11QRhiTe'
        'xture6FormatE6QFlagsINS0_4FlagEE',
        format.value, flags.value,
    )

  @overload(QRhi.Feature)
  def isFeatureSupported(self, feature: QRhi.Feature) -> bool:
    """
    Calls Qt's 'bool QRhiImplementation::isFeatureSupported(QRhi::Feature
    feature) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#isFeatureSupported

    Parameters
    ----------

    feature : QRhi.Feature
      Passed on as its number.
    """
    #  bool QRhiImplementation::isFeatureSupported(QRhi::Feature feature)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation18isFeatureSupportedEN4QRhi7FeatureE',
        feature.value,
    )

  @overload(QRhi.ResourceLimit)
  def resourceLimit(self, limit: QRhi.ResourceLimit) -> int:
    """
    Calls Qt's 'int QRhiImplementation::resourceLimit(QRhi::ResourceLimit
    limit) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#resourceLimit

    Parameters
    ----------

    limit : QRhi.ResourceLimit
      Passed on as its number.
    """
    #  int QRhiImplementation::resourceLimit(QRhi::ResourceLimit limit) const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation13resourceLimitEN4QRhi13ResourceLimi'
        'tE',
        limit.value,
    )

  def driverInfo(self) -> QRhiDriverInfo:
    """
    Calls Qt's 'QRhiDriverInfo QRhiImplementation::driverInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#driverInfo

    Returns
    -------

    QRhiDriverInfo
      A new cute QRhiDriverInfo around the copy Qt gave back. Python owns it.
    """
    #  QRhiDriverInfo QRhiImplementation::driverInfo() const
    address = self.uglySide.call(
        'ritual_ZNK18QRhiImplementation10driverInfoEv',
    )
    from . import QRhiDriverInfo
    return QRhiDriverInfo._cuteOwning(address)

  def isDeviceLost(self) -> bool:
    """
    Calls Qt's 'bool QRhiImplementation::isDeviceLost() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#isDeviceLost
    """
    #  bool QRhiImplementation::isDeviceLost() const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation12isDeviceLostEv',
    )

  @overload(QRhiTexture.Format)
  def isCompressedFormat(self, format: QRhiTexture.Format) -> bool:
    """
    Calls Qt's 'bool
    QRhiImplementation::isCompressedFormat(QRhiTexture::Format format)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#isCompressedFormat

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.
    """
    #  bool QRhiImplementation::isCompressedFormat(QRhiTexture::Format
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation18isCompressedFormatEN11QRhiTexture6'
        'FormatE',
        format.value,
    )

  @overload(QRhiTexture.Format)
  def isStencilSupportingFormat(self, format: QRhiTexture.Format) -> bool:
    """
    Calls Qt's 'bool
    QRhiImplementation::isStencilSupportingFormat(QRhiTexture::Format format)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#isStencilSupportingFormat

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.
    """
    #  bool QRhiImplementation::isStencilSupportingFormat(QRhiTexture::Format
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation25isStencilSupportingFormatEN11QRhiT'
        'exture6FormatE',
        format.value,
    )

  def pipelineCacheRhiId(self) -> int:
    """
    Calls Qt's 'quint32 QRhiImplementation::pipelineCacheRhiId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#pipelineCacheRhiId
    """
    #  quint32 QRhiImplementation::pipelineCacheRhiId() const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation18pipelineCacheRhiIdEv',
    )

  def totalPipelineCreationTime(self) -> int:
    """
    Calls Qt's 'qint64 QRhiImplementation::totalPipelineCreationTime()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#totalPipelineCreationTime
    """
    #  qint64 QRhiImplementation::totalPipelineCreationTime() const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation25totalPipelineCreationTimeEv',
    )

  @overload(QShaderDescription.VariableType)
  def shaderDescVariableFormatToVertexInputFormat(
      self,
      type: QShaderDescription.VariableType,
  ) -> QRhiVertexInputAttribute.Format:
    """
    Calls Qt's 'QRhiVertexInputAttribute::Format
    QRhiImplementation::shaderDescVariableFormatToVertexInputFormat(
    QShaderDescription::VariableType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html

    Parameters
    ----------

    type : QShaderDescription.VariableType
      Passed on as its number.

    Returns
    -------

    QRhiVertexInputAttribute.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiVertexInputAttribute.Format(number)' gives.
    """
    #  QRhiVertexInputAttribute::Format
    #      QRhiImplementation::shaderDescVariableFormatToVertexInputFormat(
    #      QShaderDescription::VariableType type) const
    return QRhiVertexInputAttribute.Format(self.uglySide.call(
        'ritual_ZNK18QRhiImplementation43shaderDescVariableFormatToVertexIn'
        'putFormatEN18QShaderDescription12VariableTypeE',
        type.value,
    ))

  @overload(QRhiVertexInputAttribute.Format)
  def byteSizePerVertexForVertexInputFormat(
      self,
      format: QRhiVertexInputAttribute.Format,
  ) -> int:
    """
    Calls Qt's 'quint32
    QRhiImplementation::byteSizePerVertexForVertexInputFormat(
    QRhiVertexInputAttribute::Format format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html

    Parameters
    ----------

    format : QRhiVertexInputAttribute.Format
      Passed on as its number.
    """
    #  quint32 QRhiImplementation::byteSizePerVertexForVertexInputFormat(
    #      QRhiVertexInputAttribute::Format format) const
    return self.uglySide.call(
        'ritual_ZNK18QRhiImplementation37byteSizePerVertexForVertexInputFor'
        'matEN24QRhiVertexInputAttribute6FormatE',
        format.value,
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
    Calls Qt's 'void
    QRhiImplementation::setGraphicsPipeline(QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#setGraphicsPipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiGraphicsPipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::setGraphicsPipeline(QRhiCommandBuffer *cb,
    #      QRhiGraphicsPipeline *ps)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation19setGraphicsPipelineEP17QRhiCommandB'
        'ufferP20QRhiGraphicsPipeline',
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
    Calls Qt's 'void QRhiImplementation::setViewport(QRhiCommandBuffer *cb,
    const QRhiViewport &viewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#setViewport

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewport : QRhiViewport
      Passed on as a value: Qt reads the C++ QRhiViewport, which stays
      Python's own.
    """
    #  void QRhiImplementation::setViewport(QRhiCommandBuffer *cb, const
    #      QRhiViewport &viewport)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation11setViewportEP17QRhiCommandBufferRK1'
        '2QRhiViewport',
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
    Calls Qt's 'void QRhiImplementation::setScissor(QRhiCommandBuffer *cb,
    const QRhiScissor &scissor)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#setScissor

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scissor : QRhiScissor
      Passed on as a value: Qt reads the C++ QRhiScissor, which stays
      Python's own.
    """
    #  void QRhiImplementation::setScissor(QRhiCommandBuffer *cb, const
    #      QRhiScissor &scissor)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation10setScissorEP17QRhiCommandBufferRK11'
        'QRhiScissor',
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
    Calls Qt's 'void QRhiImplementation::setBlendConstants(QRhiCommandBuffer
    *cb, const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#setBlendConstants

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QRhiImplementation::setBlendConstants(QRhiCommandBuffer *cb,
    #      const QColor &c)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation17setBlendConstantsEP17QRhiCommandBuf'
        'ferRK6QColor',
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
    Calls Qt's 'void QRhiImplementation::setStencilRef(QRhiCommandBuffer *cb,
    quint32 refValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#setStencilRef

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    refValue : int
      Passed on as it is.
    """
    #  void QRhiImplementation::setStencilRef(QRhiCommandBuffer *cb, quint32
    #      refValue)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation13setStencilRefEP17QRhiCommandBufferj',
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
    Calls Qt's 'void QRhiImplementation::setShadingRate(QRhiCommandBuffer
    *cb, const QSize &coarsePixelSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#setShadingRate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coarsePixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiImplementation::setShadingRate(QRhiCommandBuffer *cb, const
    #      QSize &coarsePixelSize)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation14setShadingRateEP17QRhiCommandBuffer'
        'RK5QSize',
        self._addressOf(cb), self._valueOf(coarsePixelSize),
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
    Calls Qt's 'void QRhiImplementation::setComputePipeline(QRhiCommandBuffer
    *cb, QRhiComputePipeline *ps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#setComputePipeline

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QRhiComputePipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::setComputePipeline(QRhiCommandBuffer *cb,
    #      QRhiComputePipeline *ps)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation18setComputePipelineEP17QRhiCommandBu'
        'fferP19QRhiComputePipeline',
        self._addressOf(cb), self._addressOf(ps),
    )

  @overload(QRhiNativeHandles)
  @overload(NoneType)
  def setQueueSubmitParams(
      self,
      params: Optional[QRhiNativeHandles],
  ) -> None:
    """
    Calls Qt's 'void
    QRhiImplementation::setQueueSubmitParams(QRhiNativeHandles *params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#setQueueSubmitParams

    Parameters
    ----------

    params : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::setQueueSubmitParams(QRhiNativeHandles
    #      *params)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation20setQueueSubmitParamsEP17QRhiNativeH'
        'andles',
        self._addressOf(params),
    )

  @overload(QByteArray)
  def setPipelineCacheData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiImplementation::setPipelineCacheData(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#setPipelineCacheData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiImplementation::setPipelineCacheData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation20setPipelineCacheDataERK10QByteArray',
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
    Calls Qt's 'bool QRhiImplementation::create(QRhi::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#create

    Parameters
    ----------

    flags : QRhi.Flags
      Passed on as its number.
    """
    #  bool QRhiImplementation::create(QRhi::Flags flags)
    return self.uglySide.call(
        'ritual_ZN18QRhiImplementation6createE6QFlagsIN4QRhi4FlagEE',
        flags.value,
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QRhiImplementation::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#destroy
    """
    #  void QRhiImplementation::destroy()
    self.uglySide.call('ritual_ZN18QRhiImplementation7destroyEv')

  def createGraphicsPipeline(self) -> Optional[QRhiGraphicsPipeline]:
    """
    Calls Qt's 'QRhiGraphicsPipeline
    *QRhiImplementation::createGraphicsPipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#createGraphicsPipeline

    Returns
    -------

    Optional[QRhiGraphicsPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiGraphicsPipeline *QRhiImplementation::createGraphicsPipeline()
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation22createGraphicsPipelineEv',
    )
    from . import QRhiGraphicsPipeline
    return QRhiGraphicsPipeline._cuteAt(address)

  def createComputePipeline(self) -> Optional[QRhiComputePipeline]:
    """
    Calls Qt's 'QRhiComputePipeline
    *QRhiImplementation::createComputePipeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#createComputePipeline

    Returns
    -------

    Optional[QRhiComputePipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiComputePipeline *QRhiImplementation::createComputePipeline()
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation21createComputePipelineEv',
    )
    from . import QRhiComputePipeline
    return QRhiComputePipeline._cuteAt(address)

  def createShaderResourceBindings(
      self,
  ) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings
    *QRhiImplementation::createShaderResourceBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings
    #      *QRhiImplementation::createShaderResourceBindings()
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation28createShaderResourceBindingsEv',
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
    Calls Qt's 'QRhiBuffer *QRhiImplementation::createBuffer(QRhiBuffer::Type
    type, QRhiBuffer::UsageFlags usage, quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#createBuffer

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
    #  QRhiBuffer *QRhiImplementation::createBuffer(QRhiBuffer::Type type,
    #      QRhiBuffer::UsageFlags usage, quint32 size)
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation12createBufferEN10QRhiBuffer4TypeE6QF'
        'lagsINS0_9UsageFlagEEj',
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
    *QRhiImplementation::createRenderBuffer(QRhiRenderBuffer::Type type,
    const QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
    QRhiTexture::Format backingFormatHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#createRenderBuffer

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
    #      *QRhiImplementation::createRenderBuffer(QRhiRenderBuffer::Type
    #      type, const QSize &pixelSize, int sampleCount,
    #      QRhiRenderBuffer::Flags flags, QRhiTexture::Format
    #      backingFormatHint)
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation18createRenderBufferEN16QRhiRenderBuf'
        'fer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE',
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
    Calls Qt's 'QRhiTexture
    *QRhiImplementation::createTexture(QRhiTexture::Format format, const
    QSize &pixelSize, int depth, int arraySize, int sampleCount,
    QRhiTexture::Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#createTexture

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
    #  QRhiTexture *QRhiImplementation::createTexture(QRhiTexture::Format
    #      format, const QSize &pixelSize, int depth, int arraySize, int
    #      sampleCount, QRhiTexture::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation13createTextureEN11QRhiTexture6Format'
        'ERK5QSizeiii6QFlagsINS0_4FlagEE',
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
    Calls Qt's 'QRhiSampler
    *QRhiImplementation::createSampler(QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#createSampler

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
    #  QRhiSampler *QRhiImplementation::createSampler(QRhiSampler::Filter
    #      magFilter, QRhiSampler::Filter minFilter, QRhiSampler::Filter
    #      mipmapMode, QRhiSampler::AddressMode u, QRhiSampler::AddressMode
    #      v, QRhiSampler::AddressMode w)
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation13createSamplerEN11QRhiSampler6Filter'
        'ES1_S1_NS0_11AddressModeES2_S2_',
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
    *QRhiImplementation::createTextureRenderTarget(const
    QRhiTextureRenderTargetDescription &desc, QRhiTextureRenderTarget::Flags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#createTextureRenderTarget

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
    #  QRhiTextureRenderTarget
    #      *QRhiImplementation::createTextureRenderTarget(const
    #      QRhiTextureRenderTargetDescription &desc,
    #      QRhiTextureRenderTarget::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation25createTextureRenderTargetERK34QRhiT'
        'extureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4Fl'
        'agEE',
        self._valueOf(desc), flags.value,
    )
    return QRhiTextureRenderTarget._cuteAt(address)

  def createShadingRateMap(self) -> Optional[QRhiShadingRateMap]:
    """
    Calls Qt's 'QRhiShadingRateMap
    *QRhiImplementation::createShadingRateMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#createShadingRateMap

    Returns
    -------

    Optional[QRhiShadingRateMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShadingRateMap *QRhiImplementation::createShadingRateMap()
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation20createShadingRateMapEv',
    )
    from . import QRhiShadingRateMap
    return QRhiShadingRateMap._cuteAt(address)

  def createSwapChain(self) -> Optional[QRhiSwapChain]:
    """
    Calls Qt's 'QRhiSwapChain *QRhiImplementation::createSwapChain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#createSwapChain

    Returns
    -------

    Optional[QRhiSwapChain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSwapChain *QRhiImplementation::createSwapChain()
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation15createSwapChainEv',
    )
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
    Calls Qt's 'QRhi::FrameOpResult
    QRhiImplementation::endFrame(QRhiSwapChain *swapChain,
    QRhi::EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#endFrame

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
    #  QRhi::FrameOpResult QRhiImplementation::endFrame(QRhiSwapChain
    #      *swapChain, QRhi::EndFrameFlags flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN18QRhiImplementation8endFrameEP13QRhiSwapChain6QFlagsIN4Q'
        'Rhi12EndFrameFlagEE',
        self._addressOf(swapChain), flags.value,
    ))

  @overload(QRhi.EndFrameFlags)
  def endOffscreenFrame(
      self,
      flags: QRhi.EndFrameFlags,
  ) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult
    QRhiImplementation::endOffscreenFrame(QRhi::EndFrameFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#endOffscreenFrame

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
    #  QRhi::FrameOpResult
    #      QRhiImplementation::endOffscreenFrame(QRhi::EndFrameFlags flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN18QRhiImplementation17endOffscreenFrameE6QFlagsIN4QRhi12E'
        'ndFrameFlagEE',
        flags.value,
    ))

  def finish(self) -> QRhi.FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult QRhiImplementation::finish()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#finish

    Returns
    -------

    QRhi.FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.FrameOpResult(number)' gives.
    """
    #  QRhi::FrameOpResult QRhiImplementation::finish()
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN18QRhiImplementation6finishEv',
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
    Calls Qt's 'void QRhiImplementation::resourceUpdate(QRhiCommandBuffer
    *cb, QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#resourceUpdate

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::resourceUpdate(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation14resourceUpdateEP17QRhiCommandBuffer'
        'P23QRhiResourceUpdateBatch',
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
    Calls Qt's 'void QRhiImplementation::beginPass(QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt, const QColor &colorClearValue, const
    QRhiDepthStencilClearValue &depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#beginPass

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
    #  void QRhiImplementation::beginPass(QRhiCommandBuffer *cb,
    #      QRhiRenderTarget *rt, const QColor &colorClearValue, const
    #      QRhiDepthStencilClearValue &depthStencilClearValue,
    #      QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation9beginPassEP17QRhiCommandBufferP16QRh'
        'iRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourc'
        'eUpdateBatch6QFlagsINS0_13BeginPassFlagEE',
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
    Calls Qt's 'void QRhiImplementation::endPass(QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#endPass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::endPass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation7endPassEP17QRhiCommandBufferP23QRhiR'
        'esourceUpdateBatch',
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
    Calls Qt's 'void QRhiImplementation::draw(QRhiCommandBuffer *cb, quint32
    vertexCount, quint32 instanceCount, quint32 firstVertex, quint32
    firstInstance)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#draw

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
    #  void QRhiImplementation::draw(QRhiCommandBuffer *cb, quint32
    #      vertexCount, quint32 instanceCount, quint32 firstVertex, quint32
    #      firstInstance)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation4drawEP17QRhiCommandBufferjjjj',
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
    Calls Qt's 'void QRhiImplementation::drawIndexed(QRhiCommandBuffer *cb,
    quint32 indexCount, quint32 instanceCount, quint32 firstIndex, qint32
    vertexOffset, quint32 firstInstance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#drawIndexed

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
    #  void QRhiImplementation::drawIndexed(QRhiCommandBuffer *cb, quint32
    #      indexCount, quint32 instanceCount, quint32 firstIndex, qint32
    #      vertexOffset, quint32 firstInstance)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation11drawIndexedEP17QRhiCommandBufferjjj'
        'ij',
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
      offset: int,
      drawCount: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void QRhiImplementation::drawIndirect(QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer, quint32 offset, quint32 drawCount, quint32
    stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#drawIndirect

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indirectBuffer : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    drawCount : int
      Passed on as it is.

    stride : int
      Passed on as it is.
    """
    #  void QRhiImplementation::drawIndirect(QRhiCommandBuffer *cb,
    #      QRhiBuffer *indirectBuffer, quint32 offset, quint32 drawCount,
    #      quint32 stride)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation12drawIndirectEP17QRhiCommandBufferP1'
        '0QRhiBufferjjj',
        self._addressOf(cb), self._addressOf(indirectBuffer), offset,
        drawCount, stride,
    )

  @overload(QRhiCommandBuffer, QRhiBuffer, int, int, int)
  @overload(QRhiCommandBuffer, NoneType, int, int, int)
  @overload(NoneType, QRhiBuffer, int, int, int)
  @overload(NoneType, NoneType, int, int, int)
  def drawIndexedIndirect(
      self,
      cb: Optional[QRhiCommandBuffer],
      indirectBuffer: Optional[QRhiBuffer],
      offset: int,
      drawCount: int,
      stride: int,
  ) -> None:
    """
    Calls Qt's 'void
    QRhiImplementation::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
    *indirectBuffer, quint32 offset, quint32 drawCount, quint32 stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#drawIndexedIndirect

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indirectBuffer : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    drawCount : int
      Passed on as it is.

    stride : int
      Passed on as it is.
    """
    #  void QRhiImplementation::drawIndexedIndirect(QRhiCommandBuffer *cb,
    #      QRhiBuffer *indirectBuffer, quint32 offset, quint32 drawCount,
    #      quint32 stride)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation19drawIndexedIndirectEP17QRhiCommandB'
        'ufferP10QRhiBufferjjj',
        self._addressOf(cb), self._addressOf(indirectBuffer), offset,
        drawCount, stride,
    )

  @overload(QRhiCommandBuffer, QByteArray)
  @overload(NoneType, QByteArray)
  def debugMarkBegin(
      self,
      cb: Optional[QRhiCommandBuffer],
      name: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiImplementation::debugMarkBegin(QRhiCommandBuffer
    *cb, const QByteArray &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#debugMarkBegin

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiImplementation::debugMarkBegin(QRhiCommandBuffer *cb, const
    #      QByteArray &name)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation14debugMarkBeginEP17QRhiCommandBuffer'
        'RK10QByteArray',
        self._addressOf(cb), self._valueOf(name),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def debugMarkEnd(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiImplementation::debugMarkEnd(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#debugMarkEnd

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::debugMarkEnd(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation12debugMarkEndEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer, QByteArray)
  @overload(NoneType, QByteArray)
  def debugMarkMsg(
      self,
      cb: Optional[QRhiCommandBuffer],
      msg: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QRhiImplementation::debugMarkMsg(QRhiCommandBuffer *cb,
    const QByteArray &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#debugMarkMsg

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    msg : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiImplementation::debugMarkMsg(QRhiCommandBuffer *cb, const
    #      QByteArray &msg)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation12debugMarkMsgEP17QRhiCommandBufferRK'
        '10QByteArray',
        self._addressOf(cb), self._valueOf(msg),
    )

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
    Calls Qt's 'void QRhiImplementation::beginComputePass(QRhiCommandBuffer
    *cb, QRhiResourceUpdateBatch *resourceUpdates,
    QRhiCommandBuffer::BeginPassFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#beginComputePass

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
    #  void QRhiImplementation::beginComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates,
    #      QRhiCommandBuffer::BeginPassFlags flags)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation16beginComputePassEP17QRhiCommandBuff'
        'erP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE',
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
    Calls Qt's 'void QRhiImplementation::endComputePass(QRhiCommandBuffer
    *cb, QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#endComputePass

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::endComputePass(QRhiCommandBuffer *cb,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation14endComputePassEP17QRhiCommandBuffer'
        'P23QRhiResourceUpdateBatch',
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
    Calls Qt's 'void QRhiImplementation::dispatch(QRhiCommandBuffer *cb, int
    x, int y, int z)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#dispatch

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
    #  void QRhiImplementation::dispatch(QRhiCommandBuffer *cb, int x, int y,
    #      int z)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation8dispatchEP17QRhiCommandBufferiii',
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
    *QRhiImplementation::nativeHandles(QRhiCommandBuffer *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#nativeHandles

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
    #  const QRhiNativeHandles
    #      *QRhiImplementation::nativeHandles(QRhiCommandBuffer *cb)
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation13nativeHandlesEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload()
  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles
    *QRhiImplementation::nativeHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhiImplementation::nativeHandles()
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation13nativeHandlesEv',
    )
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def beginExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiImplementation::beginExternal(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#beginExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::beginExternal(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation13beginExternalEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def endExternal(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QRhiImplementation::endExternal(QRhiCommandBuffer *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#endExternal

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::endExternal(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation11endExternalEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def lastCompletedGpuTime(self, cb: Optional[QRhiCommandBuffer]) -> float:
    """
    Calls Qt's 'double
    QRhiImplementation::lastCompletedGpuTime(QRhiCommandBuffer *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#lastCompletedGpuTime

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  double QRhiImplementation::lastCompletedGpuTime(QRhiCommandBuffer *cb)
    return self.uglySide.call(
        'ritual_ZN18QRhiImplementation20lastCompletedGpuTimeEP17QRhiCommand'
        'Buffer',
        self._addressOf(cb),
    )

  def statistics(self) -> QRhiStats:
    """
    Calls Qt's 'QRhiStats QRhiImplementation::statistics()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#statistics

    Returns
    -------

    QRhiStats
      A new cute QRhiStats around the copy Qt gave back. Python owns it.
    """
    #  QRhiStats QRhiImplementation::statistics()
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation10statisticsEv',
    )
    from . import QRhiStats
    return QRhiStats._cuteOwning(address)

  def makeThreadLocalNativeContextCurrent(self) -> bool:
    """
    Calls Qt's 'bool
    QRhiImplementation::makeThreadLocalNativeContextCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html
    """
    #  bool QRhiImplementation::makeThreadLocalNativeContextCurrent()
    return self.uglySide.call(
        'ritual_ZN18QRhiImplementation35makeThreadLocalNativeContextCurrent'
        'Ev',
    )

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QRhiImplementation::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#releaseCachedResources
    """
    #  void QRhiImplementation::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation22releaseCachedResourcesEv',
    )

  def pipelineCacheData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRhiImplementation::pipelineCacheData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#pipelineCacheData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRhiImplementation::pipelineCacheData()
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation17pipelineCacheDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QRhi, QRhi.Implementation, QRhi.Flags, QRhiAdapter)
  @overload(QRhi, QRhi.Implementation, QRhi.Flags, NoneType)
  @overload(NoneType, QRhi.Implementation, QRhi.Flags, QRhiAdapter)
  @overload(NoneType, QRhi.Implementation, QRhi.Flags, NoneType)
  def prepareForCreate(
      self,
      rhi: Optional[QRhi],
      impl: QRhi.Implementation,
      flags: QRhi.Flags,
      adapter: Optional[QRhiAdapter],
  ) -> None:
    """
    Calls Qt's 'void QRhiImplementation::prepareForCreate(QRhi *rhi,
    QRhi::Implementation impl, QRhi::Flags flags, QRhiAdapter *adapter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#prepareForCreate

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    impl : QRhi.Implementation
      Passed on as its number.

    flags : QRhi.Flags
      Passed on as its number.

    adapter : Optional[QRhiAdapter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::prepareForCreate(QRhi *rhi,
    #      QRhi::Implementation impl, QRhi::Flags flags, QRhiAdapter
    #      *adapter)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation16prepareForCreateEP4QRhiNS0_14Implem'
        'entationE6QFlagsINS0_4FlagEEP11QRhiAdapter',
        self._addressOf(rhi), impl.value, flags.value,
        self._addressOf(adapter),
    )

  @overload(QRhiResource)
  @overload(NoneType)
  @overload(QRhiResource, bool)
  @overload(NoneType, bool)
  def registerResource(
      self,
      res: Optional[QRhiResource],
      ownsNativeResources: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QRhiImplementation::registerResource(QRhiResource *res,
    bool ownsNativeResources)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#registerResource

    Parameters
    ----------

    res : Optional[QRhiResource]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ownsNativeResources : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QRhiImplementation::registerResource(QRhiResource *res, bool
    #      ownsNativeResources)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation16registerResourceEP12QRhiResourceb',
        self._addressOf(res), ownsNativeResources,
    )

  @overload(QRhiResource)
  @overload(NoneType)
  def unregisterResource(self, res: Optional[QRhiResource]) -> None:
    """
    Calls Qt's 'void QRhiImplementation::unregisterResource(QRhiResource
    *res)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#unregisterResource

    Parameters
    ----------

    res : Optional[QRhiResource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::unregisterResource(QRhiResource *res)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation18unregisterResourceEP12QRhiResource',
        self._addressOf(res),
    )

  @overload(QRhiResource)
  @overload(NoneType)
  def addDeleteLater(self, res: Optional[QRhiResource]) -> None:
    """
    Calls Qt's 'void QRhiImplementation::addDeleteLater(QRhiResource *res)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#addDeleteLater

    Parameters
    ----------

    res : Optional[QRhiResource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::addDeleteLater(QRhiResource *res)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation14addDeleteLaterEP12QRhiResource',
        self._addressOf(res),
    )

  @overload(QRhiGraphicsPipeline)
  @overload(NoneType)
  def sanityCheckGraphicsPipeline(
      self,
      ps: Optional[QRhiGraphicsPipeline],
  ) -> bool:
    """
    Calls Qt's 'bool
    QRhiImplementation::sanityCheckGraphicsPipeline(QRhiGraphicsPipeline
    *ps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html

    Parameters
    ----------

    ps : Optional[QRhiGraphicsPipeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRhiImplementation::sanityCheckGraphicsPipeline(
    #      QRhiGraphicsPipeline *ps)
    return self.uglySide.call(
        'ritual_ZN18QRhiImplementation27sanityCheckGraphicsPipelineEP20QRhi'
        'GraphicsPipeline',
        self._addressOf(ps),
    )

  @overload(QRhiShaderResourceBindings)
  @overload(NoneType)
  def sanityCheckShaderResourceBindings(
      self,
      srb: Optional[QRhiShaderResourceBindings],
  ) -> bool:
    """
    Calls Qt's 'bool QRhiImplementation::sanityCheckShaderResourceBindings(
    QRhiShaderResourceBindings *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html

    Parameters
    ----------

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRhiImplementation::sanityCheckShaderResourceBindings(
    #      QRhiShaderResourceBindings *srb)
    return self.uglySide.call(
        'ritual_ZN18QRhiImplementation33sanityCheckShaderResourceBindingsEP'
        '26QRhiShaderResourceBindings',
        self._addressOf(srb),
    )

  @overload(QRhiResource)
  @overload(NoneType)
  def sanityCheckResourceOwnership(
      self,
      maybeResource: Optional[QRhiResource],
  ) -> bool:
    """
    Calls Qt's 'bool
    QRhiImplementation::sanityCheckResourceOwnership(QRhiResource
    *maybeResource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html

    Parameters
    ----------

    maybeResource : Optional[QRhiResource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRhiImplementation::sanityCheckResourceOwnership(QRhiResource
    #      *maybeResource)
    return self.uglySide.call(
        'ritual_ZN18QRhiImplementation28sanityCheckResourceOwnershipEP12QRh'
        'iResource',
        self._addressOf(maybeResource),
    )

  @overload(QRhiShaderResourceBindings)
  @overload(NoneType)
  def updateLayoutDesc(
      self,
      srb: Optional[QRhiShaderResourceBindings],
  ) -> None:
    """
    Calls Qt's 'void
    QRhiImplementation::updateLayoutDesc(QRhiShaderResourceBindings *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#updateLayoutDesc

    Parameters
    ----------

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiImplementation::updateLayoutDesc(QRhiShaderResourceBindings
    #      *srb)
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation16updateLayoutDescEP26QRhiShaderResou'
        'rceBindings',
        self._addressOf(srb),
    )

  def pipelineCreationStart(self) -> None:
    """
    Calls Qt's 'void QRhiImplementation::pipelineCreationStart()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#pipelineCreationStart
    """
    #  void QRhiImplementation::pipelineCreationStart()
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation21pipelineCreationStartEv',
    )

  def pipelineCreationEnd(self) -> None:
    """
    Calls Qt's 'void QRhiImplementation::pipelineCreationEnd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html#pipelineCreationEnd
    """
    #  void QRhiImplementation::pipelineCreationEnd()
    self.uglySide.call(
        'ritual_ZN18QRhiImplementation19pipelineCreationEndEv',
    )

  @overload(QSize, QPoint, int, QSize)
  @overload(QSize, QPoint, int, QSize, bool)
  def clampedSubResourceUploadSize(
      self,
      size: QSize,
      dstPos: QPoint,
      level: int,
      textureSizeAtLevelZero: QSize,
      warn: bool = True,
  ) -> QSize:
    """
    Calls Qt's 'QSize QRhiImplementation::clampedSubResourceUploadSize(QSize
    size, QPoint dstPos, int level, QSize textureSizeAtLevelZero, bool
    warn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    dstPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    level : int
      Passed on as it is.

    textureSizeAtLevelZero : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    warn : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiImplementation::clampedSubResourceUploadSize(QSize size,
    #      QPoint dstPos, int level, QSize textureSizeAtLevelZero, bool warn)
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation28clampedSubResourceUploadSizeE5QSize'
        '6QPointiS0_b',
        self._valueOf(size), self._valueOf(dstPos), level,
        self._valueOf(textureSizeAtLevelZero), warn,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QSize, int, int, int)
  @overload(QSize, int, int, int, bool)
  def clampedSubResourceUploadSizeForSourceData(
      self,
      size: QSize,
      bpl: int,
      bytesPerPixel: int,
      dataSize: int,
      warn: bool = True,
  ) -> QSize:
    """
    Calls Qt's 'QSize
    QRhiImplementation::clampedSubResourceUploadSizeForSourceData(QSize size,
    quint32 bpl, quint32 bytesPerPixel, qsizetype dataSize, bool warn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiimplementation.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    bpl : int
      Passed on as it is.

    bytesPerPixel : int
      Passed on as it is.

    dataSize : int
      Passed on as it is.

    warn : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiImplementation::clampedSubResourceUploadSizeForSourceData(
    #      QSize size, quint32 bpl, quint32 bytesPerPixel, qsizetype
    #      dataSize, bool warn)
    address = self.uglySide.call(
        'ritual_ZN18QRhiImplementation41clampedSubResourceUploadSizeForSour'
        'ceDataE5QSizejjxb',
        self._valueOf(size), bpl, bytesPerPixel, dataSize, warn,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def runCleanup(self) -> None:
    """
    Calls Qt's 'void QRhiImplementation::runCleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiimplementation.html#runCleanup
    """
    #  void QRhiImplementation::runCleanup()
    self.uglySide.call('ritual_ZN18QRhiImplementation10runCleanupEv')

  @staticmethod
  def addCleanupCallback(*__, **_) -> Never:
    """
    - Qt's 'void QRhiImplementation::addCleanupCallback(const
      QRhi::CleanupCallback &callback)': takes a type Python has no way to
      hand over yet.
    - Qt's 'void QRhiImplementation::addCleanupCallback(const void *key,
      const QRhi::CleanupCallback &callback)': names 'void', which has no
      cute class yet.
    """
    raise NotImplementedError(
        "'QRhiImplementation.addCleanupCallback' has no cute function yet. "
        "Qt's 'void QRhiImplementation::addCleanupCallback(const "
        "QRhi::CleanupCallback &callback)': takes a type Python has no way "
        "to hand over yet. Qt's 'void "
        "QRhiImplementation::addCleanupCallback(const void *key, const "
        "QRhi::CleanupCallback &callback)': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def beginFrame(*__, **_) -> Never:
    """
    Qt's 'QRhi::FrameOpResult QRhiImplementation::beginFrame(QRhiSwapChain
    *swapChain, QRhi::BeginFrameFlags flags)': names the enum
    'QRhi::BeginFrameFlag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QRhiImplementation.beginFrame' has no cute function yet. Qt's "
        "'QRhi::FrameOpResult QRhiImplementation::beginFrame(QRhiSwapChain "
        "*swapChain, QRhi::BeginFrameFlags flags)': names the enum "
        "'QRhi::BeginFrameFlag', whose class cannot be named here.")

  @staticmethod
  def beginOffscreenFrame(*__, **_) -> Never:
    """
    Qt's 'QRhi::FrameOpResult
    QRhiImplementation::beginOffscreenFrame(QRhiCommandBuffer **cb,
    QRhi::BeginFrameFlags flags)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QRhiImplementation.beginOffscreenFrame' has no cute function yet. "
        "Qt's 'QRhi::FrameOpResult "
        "QRhiImplementation::beginOffscreenFrame(QRhiCommandBuffer **cb, "
        "QRhi::BeginFrameFlags flags)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def compressedFormatInfo(*__, **_) -> Never:
    """
    Qt's 'bool QRhiImplementation::compressedFormatInfo(QRhiTexture::Format
    format, const QSize &size, quint32 *bpl, quint32 *byteSize, QSize
    *blockDim) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QRhiImplementation.compressedFormatInfo' has no cute function "
        "yet. Qt's 'bool "
        "QRhiImplementation::compressedFormatInfo(QRhiTexture::Format "
        "format, const QSize &size, quint32 *bpl, quint32 *byteSize, QSize "
        "*blockDim) const': takes a number to change where it is.")

  @staticmethod
  def effectiveSampleCount(*__, **_) -> Never:
    """
    Qt's 'int QRhiImplementation::effectiveSampleCount(int sampleCount)
    const': leans on 'QRHI_LOG_INFO()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRhiImplementation.effectiveSampleCount' has no cute function "
        "yet. Qt's 'int QRhiImplementation::effectiveSampleCount(int "
        "sampleCount) const': leans on 'QRHI_LOG_INFO()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def newInstance(*__, **_) -> Never:
    """
    Qt's 'QRhiImplementation
    *QRhiImplementation::newInstance(QRhi::Implementation impl,
    QRhiInitParams *params, QRhiNativeHandles *importDevice)': leans on
    'QRhiMetal::QRhiMetal(QRhiMetalInitParams*, QRhiMetalNativeHandles*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QRhiImplementation.newInstance' has no cute function yet. Qt's "
        "'QRhiImplementation "
        "*QRhiImplementation::newInstance(QRhi::Implementation impl, "
        "QRhiInitParams *params, QRhiNativeHandles *importDevice)': leans "
        "on 'QRhiMetal::QRhiMetal(QRhiMetalInitParams*, "
        "QRhiMetalNativeHandles*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def removeCleanupCallback(*__, **_) -> Never:
    """
    Qt's 'void QRhiImplementation::removeCleanupCallback(const void *key)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiImplementation.removeCleanupCallback' has no cute function "
        "yet. Qt's 'void QRhiImplementation::removeCleanupCallback(const "
        "void *key)': names 'void', which has no cute class yet.")

  @staticmethod
  def setShaderResources(*__, **_) -> Never:
    """
    Qt's 'void QRhiImplementation::setShaderResources(QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb, int dynamicOffsetCount, const
    QRhiCommandBuffer::DynamicOffset *dynamicOffsets)': names
    'QRhiCommandBuffer::DynamicOffset', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiImplementation.setShaderResources' has no cute function yet. "
        "Qt's 'void "
        "QRhiImplementation::setShaderResources(QRhiCommandBuffer *cb, "
        "QRhiShaderResourceBindings *srb, int dynamicOffsetCount, const "
        "QRhiCommandBuffer::DynamicOffset *dynamicOffsets)': names "
        "'QRhiCommandBuffer::DynamicOffset', which has no cute class yet.")

  @staticmethod
  def setVertexInput(*__, **_) -> Never:
    """
    Qt's 'void QRhiImplementation::setVertexInput(QRhiCommandBuffer *cb, int
    startBinding, int bindingCount, const QRhiCommandBuffer::VertexInput
    *bindings, QRhiBuffer *indexBuf, quint32 indexOffset,
    QRhiCommandBuffer::IndexFormat indexFormat)': names
    'QRhiCommandBuffer::VertexInput', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiImplementation.setVertexInput' has no cute function yet. Qt's "
        "'void QRhiImplementation::setVertexInput(QRhiCommandBuffer *cb, "
        "int startBinding, int bindingCount, const "
        "QRhiCommandBuffer::VertexInput *bindings, QRhiBuffer *indexBuf, "
        "quint32 indexOffset, QRhiCommandBuffer::IndexFormat indexFormat)': "
        "names 'QRhiCommandBuffer::VertexInput', which has no cute class "
        "yet.")

  @staticmethod
  def supportedSampleCounts(*__, **_) -> Never:
    """
    Qt's 'QList<int> QRhiImplementation::supportedSampleCounts() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRhiImplementation.supportedSampleCounts' has no cute function "
        "yet. Qt's 'QList<int> QRhiImplementation::supportedSampleCounts() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def textureFormatInfo(*__, **_) -> Never:
    """
    Qt's 'bool QRhiImplementation::textureFormatInfo(QRhiTexture::Format
    format, const QSize &size, quint32 *bpl, quint32 *byteSize, quint32
    *bytesPerPixel) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QRhiImplementation.textureFormatInfo' has no cute function yet. "
        "Qt's 'bool "
        "QRhiImplementation::textureFormatInfo(QRhiTexture::Format format, "
        "const QSize &size, quint32 *bpl, quint32 *byteSize, quint32 "
        "*bytesPerPixel) const': takes a number to change where it is.")
