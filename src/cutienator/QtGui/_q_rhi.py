"""
QRhi binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QRhiBuffer, QRhiRenderBuffer, QRhiSampler, QRhiTexture
from . import QRhiTextureRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QSize, QThread
  from . import QMatrix4x4, QRhiAdapter, QRhiComputePipeline, QRhiDriverInfo
  from . import QRhiGraphicsPipeline, QRhiInitParams, QRhiNativeHandles
  from . import QRhiResourceUpdateBatch, QRhiShaderResourceBindings
  from . import QRhiShadingRateMap, QRhiStats, QRhiSwapChain
  from . import QRhiSwapChainProxyData, QRhiTextureRenderTargetDescription
  from . import QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QRhiAdapter = WAIT['QRhiAdapter']
  QRhiInitParams = WAIT['QRhiInitParams']
  QRhiNativeHandles = WAIT['QRhiNativeHandles']
  QRhiSwapChain = WAIT['QRhiSwapChain']
  QRhiTextureRenderTargetDescription = WAIT['QRhiTextureRenderTargetDescription']
  QSize = WAIT['QSize']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhi(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhi: a plain Python object standing in front of one
  C++ QRhi.

  What exists
  -----------

  Every function of Qt's QRhi that has a ritual and that Python can call so
  far, 45 names in all: 'create', 'probe', 'enumerateAdapters', 'backend',
  'backendName', 'driverInfo', 'thread', 'newGraphicsPipeline',
  'newComputePipeline', 'newShaderResourceBindings', 'newBuffer',
  'newRenderBuffer', 'newTexture', 'newTextureArray', 'newSampler',
  'newShadingRateMap', 'newTextureRenderTarget', 'newSwapChain', 'endFrame',
  'isRecordingFrame', 'currentFrameSlot', 'endOffscreenFrame', 'finish',
  'nextResourceUpdateBatch', 'ubufAlignment', 'ubufAligned',
  'mipLevelsForSize', 'sizeForMipLevel', 'isYUpInFramebuffer', 'isYUpInNDC',
  'isClipDepthZeroToOne', 'clipSpaceCorrMatrix', 'isTextureFormatSupported',
  'isFeatureSupported', 'resourceLimit', 'nativeHandles',
  'makeThreadLocalNativeContextCurrent', 'setQueueSubmitParams',
  'releaseCachedResources', 'isDeviceLost', 'pipelineCacheData',
  'setPipelineCacheData', 'statistics', 'updateSwapChainProxyData',
  'supportedShadingRates'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhi::~QRhi()': the destructor: Python never removes a C++ QRhi.
  - Qt's 'void QRhi::addCleanupCallback(const CleanupCallback &callback)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QRhi::addCleanupCallback(const void *key, const
    CleanupCallback &callback)': names 'void', which has no cute class yet.
  - Qt's 'void QRhi::removeCleanupCallback(const void *key)': names 'void',
    which has no cute class yet.
  - Qt's 'FrameOpResult QRhi::beginFrame(QRhiSwapChain *swapChain,
    BeginFrameFlags flags)': names the enum 'QRhi::BeginFrameFlag', whose
    class cannot be named here.
  - Qt's 'FrameOpResult QRhi::beginOffscreenFrame(QRhiCommandBuffer **cb,
    BeginFrameFlags flags)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<int> QRhi::supportedSampleCounts() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 58 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QRhi is created at the first use, not by 'QRhi(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhi.
  - Each name of Qt's QRhi that has no cute function yet,
    'addCleanupCallback', 'beginFrame', 'beginOffscreenFrame',
    'removeCleanupCallback', 'supportedSampleCounts', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRhi, each a class in here as in C++, and the
  #  names Qt has for the combinations of its flags enums.

  class EndFrameFlag(CuteFlags):
    """
    The flags enum 'QRhi::EndFrameFlag' of Qt, with the 1 names Qt gives in
    it. Qt names the type of its combinations 'QRhi::EndFrameFlags'.
    """

    SkipPresent = 0x1

  EndFrameFlags = EndFrameFlag

  class Feature(CuteNum):
    """The enum 'QRhi::Feature' of Qt, with the 53 names Qt gives in it."""

    MultisampleTexture = Kee[int](1)
    MultisampleRenderBuffer = Kee[int](2)
    DebugMarkers = Kee[int](3)
    Timestamps = Kee[int](4)
    Instancing = Kee[int](5)
    CustomInstanceStepRate = Kee[int](6)
    PrimitiveRestart = Kee[int](7)
    NonDynamicUniformBuffers = Kee[int](8)
    NonFourAlignedEffectiveIndexBufferOffset = Kee[int](9)
    NPOTTextureRepeat = Kee[int](10)
    RedOrAlpha8IsRed = Kee[int](11)
    ElementIndexUint = Kee[int](12)
    Compute = Kee[int](13)
    WideLines = Kee[int](14)
    VertexShaderPointSize = Kee[int](15)
    BaseVertex = Kee[int](16)
    BaseInstance = Kee[int](17)
    TriangleFanTopology = Kee[int](18)
    ReadBackNonUniformBuffer = Kee[int](19)
    ReadBackNonBaseMipLevel = Kee[int](20)
    TexelFetch = Kee[int](21)
    RenderToNonBaseMipLevel = Kee[int](22)
    IntAttributes = Kee[int](23)
    ScreenSpaceDerivatives = Kee[int](24)
    ReadBackAnyTextureFormat = Kee[int](25)
    PipelineCacheDataLoadSave = Kee[int](26)
    ImageDataStride = Kee[int](27)
    RenderBufferImport = Kee[int](28)
    ThreeDimensionalTextures = Kee[int](29)
    RenderTo3DTextureSlice = Kee[int](30)
    TextureArrays = Kee[int](31)
    Tessellation = Kee[int](32)
    GeometryShader = Kee[int](33)
    TextureArrayRange = Kee[int](34)
    NonFillPolygonMode = Kee[int](35)
    OneDimensionalTextures = Kee[int](36)
    OneDimensionalTextureMipmaps = Kee[int](37)
    HalfAttributes = Kee[int](38)
    RenderToOneDimensionalTexture = Kee[int](39)
    ThreeDimensionalTextureMipmaps = Kee[int](40)
    MultiView = Kee[int](41)
    TextureViewFormat = Kee[int](42)
    ResolveDepthStencil = Kee[int](43)
    VariableRateShading = Kee[int](44)
    VariableRateShadingMap = Kee[int](45)
    VariableRateShadingMapWithTexture = Kee[int](46)
    PerRenderTargetBlending = Kee[int](47)
    SampleVariables = Kee[int](48)
    InstanceIndexIncludesBaseInstance = Kee[int](49)
    DepthClamp = Kee[int](50)
    DrawIndirect = Kee[int](51)
    DrawIndirectMulti = Kee[int](52)
    ShaderDrawParameters = Kee[int](53)

  class Flag(CuteFlags):
    """
    The flags enum 'QRhi::Flag' of Qt, with the 5 names Qt gives in it. Qt
    names the type of its combinations 'QRhi::Flags'.
    """

    EnableDebugMarkers = 0x1
    PreferSoftwareRenderer = 0x2
    EnablePipelineCacheDataSave = 0x4
    EnableTimestamps = 0x8
    SuppressSmokeTestWarnings = 0x10

  Flags = Flag

  class FrameOpResult(CuteNum):
    """
    The enum 'QRhi::FrameOpResult' of Qt, with the 4 names Qt gives in it.
    """

    FrameOpSuccess = Kee[int](0)
    FrameOpError = Kee[int](1)
    FrameOpSwapChainOutOfDate = Kee[int](2)
    FrameOpDeviceLost = Kee[int](3)

  class Implementation(CuteNum):
    """
    The enum 'QRhi::Implementation' of Qt, with the 6 names Qt gives in it.
    """

    Null = Kee[int](0)
    Vulkan = Kee[int](1)
    OpenGLES2 = Kee[int](2)
    D3D11 = Kee[int](3)
    Metal = Kee[int](4)
    D3D12 = Kee[int](5)

  class ResourceLimit(CuteNum):
    """
    The enum 'QRhi::ResourceLimit' of Qt, with the 15 names Qt gives in it.
    """

    TextureSizeMin = Kee[int](1)
    TextureSizeMax = Kee[int](2)
    MaxColorAttachments = Kee[int](3)
    FramesInFlight = Kee[int](4)
    MaxAsyncReadbackFrames = Kee[int](5)
    MaxThreadGroupsPerDimension = Kee[int](6)
    MaxThreadsPerThreadGroup = Kee[int](7)
    MaxThreadGroupX = Kee[int](8)
    MaxThreadGroupY = Kee[int](9)
    MaxThreadGroupZ = Kee[int](10)
    TextureArraySizeMax = Kee[int](11)
    MaxUniformBufferRange = Kee[int](12)
    MaxVertexInputs = Kee[int](13)
    MaxVertexOutputs = Kee[int](14)
    ShadingRateImageTileSize = Kee[int](15)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Implementation, QRhiInitParams)
  @overload(Implementation, NoneType)
  @overload(Implementation, QRhiInitParams, Flags)
  @overload(Implementation, NoneType, Flags)
  @overload(Implementation, QRhiInitParams, Flags, QRhiNativeHandles)
  @overload(Implementation, QRhiInitParams, Flags, NoneType)
  @overload(Implementation, NoneType, Flags, QRhiNativeHandles)
  @overload(Implementation, NoneType, Flags, NoneType)
  def create(
      impl: Implementation,
      params: Optional[QRhiInitParams],
      flags: Flags = Flags(),
      importDevice: Optional[QRhiNativeHandles] = None,
  ) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QRhi::create(Implementation impl, QRhiInitParams
    *params, Flags flags, QRhiNativeHandles *importDevice)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#create

    Parameters
    ----------

    impl : Implementation
      Passed on as its number.

    params : Optional[QRhiInitParams]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Flags
      Passed on as its number. May be left out, as in Qt: it is then Flags().

    importDevice : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QRhi::create(Implementation impl, QRhiInitParams *params, Flags
    #      flags, QRhiNativeHandles *importDevice)
    address = Rituals.call(
        'ritual_ZN4QRhi6createENS_14ImplementationEP14QRhiInitParams6QFlags'
        'INS_4FlagEEP17QRhiNativeHandles',
        impl.value, CuteMixin._addressOf(params), flags.value,
        CuteMixin._addressOf(importDevice),
    )
    return QRhi._cuteAt(address)

  @staticmethod
  @overload(
      Implementation, QRhiInitParams, Flags, QRhiNativeHandles, QRhiAdapter,
  )
  @overload(
      Implementation, QRhiInitParams, Flags, QRhiNativeHandles, NoneType,
  )
  @overload(Implementation, QRhiInitParams, Flags, NoneType, QRhiAdapter)
  @overload(Implementation, QRhiInitParams, Flags, NoneType, NoneType)
  @overload(Implementation, NoneType, Flags, QRhiNativeHandles, QRhiAdapter)
  @overload(Implementation, NoneType, Flags, QRhiNativeHandles, NoneType)
  @overload(Implementation, NoneType, Flags, NoneType, QRhiAdapter)
  @overload(Implementation, NoneType, Flags, NoneType, NoneType)
  def create(
      impl: Implementation,
      params: Optional[QRhiInitParams],
      flags: Flags,
      importDevice: Optional[QRhiNativeHandles],
      adapter: Optional[QRhiAdapter],
  ) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QRhi::create(Implementation impl, QRhiInitParams
    *params, Flags flags, QRhiNativeHandles *importDevice, QRhiAdapter
    *adapter)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#create

    Parameters
    ----------

    impl : Implementation
      Passed on as its number.

    params : Optional[QRhiInitParams]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Flags
      Passed on as its number.

    importDevice : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    adapter : Optional[QRhiAdapter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QRhi::create(Implementation impl, QRhiInitParams *params, Flags
    #      flags, QRhiNativeHandles *importDevice, QRhiAdapter *adapter)
    address = Rituals.call(
        'ritual_ZN4QRhi6createENS_14ImplementationEP14QRhiInitParams6QFlags'
        'INS_4FlagEEP17QRhiNativeHandlesP11QRhiAdapter',
        impl.value, CuteMixin._addressOf(params), flags.value,
        CuteMixin._addressOf(importDevice), CuteMixin._addressOf(adapter),
    )
    return QRhi._cuteAt(address)

  @staticmethod
  @overload(Implementation, QRhiInitParams)
  @overload(Implementation, NoneType)
  def probe(impl: Implementation, params: Optional[QRhiInitParams]) -> bool:
    """
    Calls Qt's 'bool QRhi::probe(Implementation impl, QRhiInitParams
    *params)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#probe

    Parameters
    ----------

    impl : Implementation
      Passed on as its number.

    params : Optional[QRhiInitParams]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRhi::probe(Implementation impl, QRhiInitParams *params)
    return Rituals.call(
        'ritual_ZN4QRhi5probeENS_14ImplementationEP14QRhiInitParams',
        impl.value, CuteMixin._addressOf(params),
    )

  @staticmethod
  @overload(Implementation, QRhiInitParams)
  @overload(Implementation, NoneType)
  @overload(Implementation, QRhiInitParams, QRhiNativeHandles)
  @overload(Implementation, QRhiInitParams, NoneType)
  @overload(Implementation, NoneType, QRhiNativeHandles)
  @overload(Implementation, NoneType, NoneType)
  def enumerateAdapters(
      impl: Implementation,
      params: Optional[QRhiInitParams],
      nativeHandles: Optional[QRhiNativeHandles] = None,
  ) -> QList[QRhiAdapter]:
    """
    Calls Qt's 'AdapterList QRhi::enumerateAdapters(Implementation impl,
    QRhiInitParams *params, QRhiNativeHandles *nativeHandles)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#enumerateAdapters

    Parameters
    ----------

    impl : Implementation
      Passed on as its number.

    params : Optional[QRhiInitParams]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    nativeHandles : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QList[QRhiAdapter]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  AdapterList QRhi::enumerateAdapters(Implementation impl,
    #      QRhiInitParams *params, QRhiNativeHandles *nativeHandles)
    address = Rituals.call(
        'ritual_ZN4QRhi17enumerateAdaptersENS_14ImplementationEP14QRhiInitP'
        'aramsP17QRhiNativeHandles',
        impl.value, CuteMixin._addressOf(params),
        CuteMixin._addressOf(nativeHandles),
    )
    from . import QRhiAdapter
    return QList[QRhiAdapter]._cuteOwning(address)

  @staticmethod
  @overload(QSize)
  def mipLevelsForSize(size: QSize) -> int:
    """
    Calls Qt's 'int QRhi::mipLevelsForSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#mipLevelsForSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  int QRhi::mipLevelsForSize(const QSize &size)
    return Rituals.call(
        'ritual_ZN4QRhi16mipLevelsForSizeERK5QSize',
        CuteMixin._valueOf(size),
    )

  @staticmethod
  @overload(int, QSize)
  def sizeForMipLevel(mipLevel: int, baseLevelSize: QSize) -> QSize:
    """
    Calls Qt's 'QSize QRhi::sizeForMipLevel(int mipLevel, const QSize
    &baseLevelSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#sizeForMipLevel

    Parameters
    ----------

    mipLevel : int
      Passed on as it is.

    baseLevelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhi::sizeForMipLevel(int mipLevel, const QSize &baseLevelSize)
    address = Rituals.call(
        'ritual_ZN4QRhi15sizeForMipLevelEiRK5QSize',
        mipLevel, CuteMixin._valueOf(baseLevelSize),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @staticmethod
  @overload(Implementation, QWindow)
  @overload(Implementation, NoneType)
  def updateSwapChainProxyData(
      impl: Implementation,
      window: Optional[QWindow],
  ) -> QRhiSwapChainProxyData:
    """
    Calls Qt's 'QRhiSwapChainProxyData
    QRhi::updateSwapChainProxyData(Implementation impl, QWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#updateSwapChainProxyData

    Parameters
    ----------

    impl : Implementation
      Passed on as its number.

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRhiSwapChainProxyData
      A new cute QRhiSwapChainProxyData around the copy Qt gave back. Python
      owns it.
    """
    #  QRhiSwapChainProxyData QRhi::updateSwapChainProxyData(Implementation
    #      impl, QWindow *window)
    address = Rituals.call(
        'ritual_ZN4QRhi24updateSwapChainProxyDataENS_14ImplementationEP7QWi'
        'ndow',
        impl.value, CuteMixin._addressOf(window),
    )
    from . import QRhiSwapChainProxyData
    return QRhiSwapChainProxyData._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhi'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def backend(self) -> Implementation:
    """
    Calls Qt's 'Implementation QRhi::backend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#backend

    Returns
    -------

    Implementation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Implementation(number)'
      gives.
    """
    #  Implementation QRhi::backend() const
    return QRhi.Implementation(self.uglySide.call(
        'ritual_ZNK4QRhi7backendEv',
    ))

  @overload()
  def backendName(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QRhi::backendName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#backendName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QRhi::backendName() const
    chars = self.uglySide.call('ritual_ZNK4QRhi11backendNameEv')
    return None if chars is None else chars.decode()

  @staticmethod
  @overload(Implementation)
  def backendName(impl: Implementation) -> Optional[str]:
    """
    Calls Qt's 'const char *QRhi::backendName(Implementation impl)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#backendName

    Parameters
    ----------

    impl : Implementation
      Passed on as its number.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QRhi::backendName(Implementation impl)
    chars = Rituals.call(
        'ritual_ZN4QRhi11backendNameENS_14ImplementationE', impl.value,
    )
    return None if chars is None else chars.decode()

  def driverInfo(self) -> QRhiDriverInfo:
    """
    Calls Qt's 'QRhiDriverInfo QRhi::driverInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#driverInfo

    Returns
    -------

    QRhiDriverInfo
      A new cute QRhiDriverInfo around the copy Qt gave back. Python owns it.
    """
    #  QRhiDriverInfo QRhi::driverInfo() const
    address = self.uglySide.call('ritual_ZNK4QRhi10driverInfoEv')
    from . import QRhiDriverInfo
    return QRhiDriverInfo._cuteOwning(address)

  def thread(self) -> Optional[QThread]:
    """
    Calls Qt's 'QThread *QRhi::thread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#thread

    Returns
    -------

    Optional[QThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThread *QRhi::thread() const
    address = self.uglySide.call('ritual_ZNK4QRhi6threadEv')
    from ..QtCore import QThread
    return QThread._cuteAt(address)

  def isRecordingFrame(self) -> bool:
    """
    Calls Qt's 'bool QRhi::isRecordingFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#isRecordingFrame
    """
    #  bool QRhi::isRecordingFrame() const
    return self.uglySide.call('ritual_ZNK4QRhi16isRecordingFrameEv')

  def currentFrameSlot(self) -> int:
    """
    Calls Qt's 'int QRhi::currentFrameSlot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#currentFrameSlot
    """
    #  int QRhi::currentFrameSlot() const
    return self.uglySide.call('ritual_ZNK4QRhi16currentFrameSlotEv')

  def ubufAlignment(self) -> int:
    """
    Calls Qt's 'int QRhi::ubufAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#ubufAlignment
    """
    #  int QRhi::ubufAlignment() const
    return self.uglySide.call('ritual_ZNK4QRhi13ubufAlignmentEv')

  @overload(int)
  def ubufAligned(self, v: int) -> int:
    """
    Calls Qt's 'int QRhi::ubufAligned(int v) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#ubufAligned

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  int QRhi::ubufAligned(int v) const
    return self.uglySide.call('ritual_ZNK4QRhi11ubufAlignedEi', v)

  def isYUpInFramebuffer(self) -> bool:
    """
    Calls Qt's 'bool QRhi::isYUpInFramebuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#isYUpInFramebuffer
    """
    #  bool QRhi::isYUpInFramebuffer() const
    return self.uglySide.call('ritual_ZNK4QRhi18isYUpInFramebufferEv')

  def isYUpInNDC(self) -> bool:
    """
    Calls Qt's 'bool QRhi::isYUpInNDC() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#isYUpInNDC
    """
    #  bool QRhi::isYUpInNDC() const
    return self.uglySide.call('ritual_ZNK4QRhi10isYUpInNDCEv')

  def isClipDepthZeroToOne(self) -> bool:
    """
    Calls Qt's 'bool QRhi::isClipDepthZeroToOne() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#isClipDepthZeroToOne
    """
    #  bool QRhi::isClipDepthZeroToOne() const
    return self.uglySide.call('ritual_ZNK4QRhi20isClipDepthZeroToOneEv')

  def clipSpaceCorrMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QRhi::clipSpaceCorrMatrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#clipSpaceCorrMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QRhi::clipSpaceCorrMatrix() const
    address = self.uglySide.call('ritual_ZNK4QRhi19clipSpaceCorrMatrixEv')
    from . import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QRhiTexture.Format)
  @overload(QRhiTexture.Format, QRhiTexture.Flags)
  def isTextureFormatSupported(
      self,
      format: QRhiTexture.Format,
      flags: QRhiTexture.Flags = QRhiTexture.Flags(),
  ) -> bool:
    """
    Calls Qt's 'bool QRhi::isTextureFormatSupported(QRhiTexture::Format
    format, QRhiTexture::Flags flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#isTextureFormatSupported

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    flags : QRhiTexture.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QRhiTexture.Flags().
    """
    #  bool QRhi::isTextureFormatSupported(QRhiTexture::Format format,
    #      QRhiTexture::Flags flags) const
    return self.uglySide.call(
        'ritual_ZNK4QRhi24isTextureFormatSupportedEN11QRhiTexture6FormatE6Q'
        'FlagsINS0_4FlagEE',
        format.value, flags.value,
    )

  @overload(Feature)
  def isFeatureSupported(self, feature: Feature) -> bool:
    """
    Calls Qt's 'bool QRhi::isFeatureSupported(QRhi::Feature feature) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#isFeatureSupported

    Parameters
    ----------

    feature : Feature
      Passed on as its number.
    """
    #  bool QRhi::isFeatureSupported(QRhi::Feature feature) const
    return self.uglySide.call(
        'ritual_ZNK4QRhi18isFeatureSupportedENS_7FeatureE', feature.value,
    )

  @overload(ResourceLimit)
  def resourceLimit(self, limit: ResourceLimit) -> int:
    """
    Calls Qt's 'int QRhi::resourceLimit(ResourceLimit limit) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#resourceLimit

    Parameters
    ----------

    limit : ResourceLimit
      Passed on as its number.
    """
    #  int QRhi::resourceLimit(ResourceLimit limit) const
    return self.uglySide.call(
        'ritual_ZNK4QRhi13resourceLimitENS_13ResourceLimitE', limit.value,
    )

  def isDeviceLost(self) -> bool:
    """
    Calls Qt's 'bool QRhi::isDeviceLost() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#isDeviceLost
    """
    #  bool QRhi::isDeviceLost() const
    return self.uglySide.call('ritual_ZNK4QRhi12isDeviceLostEv')

  def statistics(self) -> QRhiStats:
    """
    Calls Qt's 'QRhiStats QRhi::statistics() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#statistics

    Returns
    -------

    QRhiStats
      A new cute QRhiStats around the copy Qt gave back. Python owns it.
    """
    #  QRhiStats QRhi::statistics() const
    address = self.uglySide.call('ritual_ZNK4QRhi10statisticsEv')
    from . import QRhiStats
    return QRhiStats._cuteOwning(address)

  @overload(int)
  def supportedShadingRates(self, sampleCount: int) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QRhi::supportedShadingRates(int sampleCount)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#supportedShadingRates

    Parameters
    ----------

    sampleCount : int
      Passed on as it is.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QRhi::supportedShadingRates(int sampleCount) const
    address = self.uglySide.call(
        'ritual_ZNK4QRhi21supportedShadingRatesEi', sampleCount,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiNativeHandles)
  @overload(NoneType)
  def setQueueSubmitParams(
      self,
      params: Optional[QRhiNativeHandles],
  ) -> None:
    """
    Calls Qt's 'void QRhi::setQueueSubmitParams(QRhiNativeHandles *params)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#setQueueSubmitParams

    Parameters
    ----------

    params : Optional[QRhiNativeHandles]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhi::setQueueSubmitParams(QRhiNativeHandles *params)
    self.uglySide.call(
        'ritual_ZN4QRhi20setQueueSubmitParamsEP17QRhiNativeHandles',
        self._addressOf(params),
    )

  @overload(QByteArray)
  def setPipelineCacheData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QRhi::setPipelineCacheData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#setPipelineCacheData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhi::setPipelineCacheData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN4QRhi20setPipelineCacheDataERK10QByteArray',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QRhi::QRhi()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#QRhi
    """
    #  QRhi::QRhi()
    self._noteCreation(QRhi, lambda: Rituals.call('ritual_ZN4QRhiC1Ev'))

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

  def newGraphicsPipeline(self) -> Optional[QRhiGraphicsPipeline]:
    """
    Calls Qt's 'QRhiGraphicsPipeline *QRhi::newGraphicsPipeline()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newGraphicsPipeline

    Returns
    -------

    Optional[QRhiGraphicsPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiGraphicsPipeline *QRhi::newGraphicsPipeline()
    address = self.uglySide.call('ritual_ZN4QRhi19newGraphicsPipelineEv')
    from . import QRhiGraphicsPipeline
    return QRhiGraphicsPipeline._cuteAt(address)

  def newComputePipeline(self) -> Optional[QRhiComputePipeline]:
    """
    Calls Qt's 'QRhiComputePipeline *QRhi::newComputePipeline()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newComputePipeline

    Returns
    -------

    Optional[QRhiComputePipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiComputePipeline *QRhi::newComputePipeline()
    address = self.uglySide.call('ritual_ZN4QRhi18newComputePipelineEv')
    from . import QRhiComputePipeline
    return QRhiComputePipeline._cuteAt(address)

  def newShaderResourceBindings(
      self,
  ) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings
    *QRhi::newShaderResourceBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhi.html#newShaderResourceBindings

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings *QRhi::newShaderResourceBindings()
    address = self.uglySide.call(
        'ritual_ZN4QRhi25newShaderResourceBindingsEv',
    )
    from . import QRhiShaderResourceBindings
    return QRhiShaderResourceBindings._cuteAt(address)

  @overload(QRhiBuffer.Type, QRhiBuffer.UsageFlags, int)
  def newBuffer(
      self,
      type: QRhiBuffer.Type,
      usage: QRhiBuffer.UsageFlags,
      size: int,
  ) -> Optional[QRhiBuffer]:
    """
    Calls Qt's 'QRhiBuffer *QRhi::newBuffer(QRhiBuffer::Type type,
    QRhiBuffer::UsageFlags usage, quint32 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newBuffer

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
    #  QRhiBuffer *QRhi::newBuffer(QRhiBuffer::Type type,
    #      QRhiBuffer::UsageFlags usage, quint32 size)
    address = self.uglySide.call(
        'ritual_ZN4QRhi9newBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlag'
        'EEj',
        type.value, usage.value, size,
    )
    return QRhiBuffer._cuteAt(address)

  @overload(QRhiRenderBuffer.Type, QSize)
  @overload(QRhiRenderBuffer.Type, QSize, int)
  @overload(QRhiRenderBuffer.Type, QSize, int, QRhiRenderBuffer.Flags)
  @overload(
      QRhiRenderBuffer.Type, QSize, int, QRhiRenderBuffer.Flags,
      QRhiTexture.Format,
  )
  def newRenderBuffer(
      self,
      type: QRhiRenderBuffer.Type,
      pixelSize: QSize,
      sampleCount: int = 1,
      flags: QRhiRenderBuffer.Flags = QRhiRenderBuffer.Flags(),
      backingFormatHint: QRhiTexture.Format = (
          QRhiTexture.Format.UnknownFormat),
  ) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer
    *QRhi::newRenderBuffer(QRhiRenderBuffer::Type type, const QSize
    &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
    QRhiTexture::Format backingFormatHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newRenderBuffer

    Parameters
    ----------

    type : QRhiRenderBuffer.Type
      Passed on as its number.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    flags : QRhiRenderBuffer.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QRhiRenderBuffer.Flags().

    backingFormatHint : QRhiTexture.Format
      Passed on as its number. May be left out, as in Qt: it is then
      QRhiTexture.Format.UnknownFormat.

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer *QRhi::newRenderBuffer(QRhiRenderBuffer::Type type,
    #      const QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags
    #      flags, QRhiTexture::Format backingFormatHint)
    address = self.uglySide.call(
        'ritual_ZN4QRhi15newRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei'
        '6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE',
        type.value, self._valueOf(pixelSize), sampleCount, flags.value,
        backingFormatHint.value,
    )
    return QRhiRenderBuffer._cuteAt(address)

  @overload(QRhiTexture.Format, QSize)
  @overload(QRhiTexture.Format, QSize, int)
  @overload(QRhiTexture.Format, QSize, int, QRhiTexture.Flags)
  def newTexture(
      self,
      format: QRhiTexture.Format,
      pixelSize: QSize,
      sampleCount: int = 1,
      flags: QRhiTexture.Flags = QRhiTexture.Flags(),
  ) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhi::newTexture(QRhiTexture::Format format,
    const QSize &pixelSize, int sampleCount, QRhiTexture::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newTexture

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    flags : QRhiTexture.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QRhiTexture.Flags().

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhi::newTexture(QRhiTexture::Format format, const QSize
    #      &pixelSize, int sampleCount, QRhiTexture::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN4QRhi10newTextureEN11QRhiTexture6FormatERK5QSizei6QFlagsI'
        'NS0_4FlagEE',
        format.value, self._valueOf(pixelSize), sampleCount, flags.value,
    )
    return QRhiTexture._cuteAt(address)

  @overload(QRhiTexture.Format, int, int, int)
  @overload(QRhiTexture.Format, int, int, int, int)
  @overload(QRhiTexture.Format, int, int, int, int, QRhiTexture.Flags)
  def newTexture(
      self,
      format: QRhiTexture.Format,
      width: int,
      height: int,
      depth: int,
      sampleCount: int = 1,
      flags: QRhiTexture.Flags = QRhiTexture.Flags(),
  ) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhi::newTexture(QRhiTexture::Format format, int
    width, int height, int depth, int sampleCount, QRhiTexture::Flags
    flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newTexture

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.

    sampleCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    flags : QRhiTexture.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QRhiTexture.Flags().

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhi::newTexture(QRhiTexture::Format format, int width,
    #      int height, int depth, int sampleCount, QRhiTexture::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN4QRhi10newTextureEN11QRhiTexture6FormatEiiii6QFlagsINS0_4'
        'FlagEE',
        format.value, width, height, depth, sampleCount, flags.value,
    )
    return QRhiTexture._cuteAt(address)

  @overload(QRhiTexture.Format, int, QSize)
  @overload(QRhiTexture.Format, int, QSize, int)
  @overload(QRhiTexture.Format, int, QSize, int, QRhiTexture.Flags)
  def newTextureArray(
      self,
      format: QRhiTexture.Format,
      arraySize: int,
      pixelSize: QSize,
      sampleCount: int = 1,
      flags: QRhiTexture.Flags = QRhiTexture.Flags(),
  ) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhi::newTextureArray(QRhiTexture::Format
    format, int arraySize, const QSize &pixelSize, int sampleCount,
    QRhiTexture::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newTextureArray

    Parameters
    ----------

    format : QRhiTexture.Format
      Passed on as its number.

    arraySize : int
      Passed on as it is.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    flags : QRhiTexture.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QRhiTexture.Flags().

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhi::newTextureArray(QRhiTexture::Format format, int
    #      arraySize, const QSize &pixelSize, int sampleCount,
    #      QRhiTexture::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN4QRhi15newTextureArrayEN11QRhiTexture6FormatEiRK5QSizei6Q'
        'FlagsINS0_4FlagEE',
        format.value, arraySize, self._valueOf(pixelSize), sampleCount,
        flags.value,
    )
    return QRhiTexture._cuteAt(address)

  @overload(
      QRhiSampler.Filter, QRhiSampler.Filter, QRhiSampler.Filter,
      QRhiSampler.AddressMode, QRhiSampler.AddressMode,
  )
  @overload(
      QRhiSampler.Filter, QRhiSampler.Filter, QRhiSampler.Filter,
      QRhiSampler.AddressMode, QRhiSampler.AddressMode,
      QRhiSampler.AddressMode,
  )
  def newSampler(
      self,
      magFilter: QRhiSampler.Filter,
      minFilter: QRhiSampler.Filter,
      mipmapMode: QRhiSampler.Filter,
      addressU: QRhiSampler.AddressMode,
      addressV: QRhiSampler.AddressMode,
      addressW: QRhiSampler.AddressMode = QRhiSampler.AddressMode.Repeat,
  ) -> Optional[QRhiSampler]:
    """
    Calls Qt's 'QRhiSampler *QRhi::newSampler(QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode addressU, QRhiSampler::AddressMode addressV,
    QRhiSampler::AddressMode addressW)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newSampler

    Parameters
    ----------

    magFilter : QRhiSampler.Filter
      Passed on as its number.

    minFilter : QRhiSampler.Filter
      Passed on as its number.

    mipmapMode : QRhiSampler.Filter
      Passed on as its number.

    addressU : QRhiSampler.AddressMode
      Passed on as its number.

    addressV : QRhiSampler.AddressMode
      Passed on as its number.

    addressW : QRhiSampler.AddressMode
      Passed on as its number. May be left out, as in Qt: it is then
      QRhiSampler.AddressMode.Repeat.

    Returns
    -------

    Optional[QRhiSampler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSampler *QRhi::newSampler(QRhiSampler::Filter magFilter,
    #      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
    #      QRhiSampler::AddressMode addressU, QRhiSampler::AddressMode
    #      addressV, QRhiSampler::AddressMode addressW)
    address = self.uglySide.call(
        'ritual_ZN4QRhi10newSamplerEN11QRhiSampler6FilterES1_S1_NS0_11Addre'
        'ssModeES2_S2_',
        magFilter.value, minFilter.value, mipmapMode.value, addressU.value,
        addressV.value, addressW.value,
    )
    return QRhiSampler._cuteAt(address)

  def newShadingRateMap(self) -> Optional[QRhiShadingRateMap]:
    """
    Calls Qt's 'QRhiShadingRateMap *QRhi::newShadingRateMap()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newShadingRateMap

    Returns
    -------

    Optional[QRhiShadingRateMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShadingRateMap *QRhi::newShadingRateMap()
    address = self.uglySide.call('ritual_ZN4QRhi17newShadingRateMapEv')
    from . import QRhiShadingRateMap
    return QRhiShadingRateMap._cuteAt(address)

  @overload(QRhiTextureRenderTargetDescription)
  @overload(
      QRhiTextureRenderTargetDescription, QRhiTextureRenderTarget.Flags,
  )
  def newTextureRenderTarget(
      self,
      desc: QRhiTextureRenderTargetDescription,
      flags: QRhiTextureRenderTarget.Flags = QRhiTextureRenderTarget.Flags(),
  ) -> Optional[QRhiTextureRenderTarget]:
    """
    Calls Qt's 'QRhiTextureRenderTarget *QRhi::newTextureRenderTarget(const
    QRhiTextureRenderTargetDescription &desc, QRhiTextureRenderTarget::Flags
    flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newTextureRenderTarget

    Parameters
    ----------

    desc : QRhiTextureRenderTargetDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureRenderTargetDescription, which stays Python's own.

    flags : QRhiTextureRenderTarget.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QRhiTextureRenderTarget.Flags().

    Returns
    -------

    Optional[QRhiTextureRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTextureRenderTarget *QRhi::newTextureRenderTarget(const
    #      QRhiTextureRenderTargetDescription &desc,
    #      QRhiTextureRenderTarget::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN4QRhi22newTextureRenderTargetERK34QRhiTextureRenderTarget'
        'Description6QFlagsIN23QRhiTextureRenderTarget4FlagEE',
        self._valueOf(desc), flags.value,
    )
    return QRhiTextureRenderTarget._cuteAt(address)

  def newSwapChain(self) -> Optional[QRhiSwapChain]:
    """
    Calls Qt's 'QRhiSwapChain *QRhi::newSwapChain()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#newSwapChain

    Returns
    -------

    Optional[QRhiSwapChain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSwapChain *QRhi::newSwapChain()
    address = self.uglySide.call('ritual_ZN4QRhi12newSwapChainEv')
    from . import QRhiSwapChain
    return QRhiSwapChain._cuteAt(address)

  @overload(QRhiSwapChain)
  @overload(NoneType)
  @overload(QRhiSwapChain, EndFrameFlags)
  @overload(NoneType, EndFrameFlags)
  def endFrame(
      self,
      swapChain: Optional[QRhiSwapChain],
      flags: EndFrameFlags = EndFrameFlags(),
  ) -> FrameOpResult:
    """
    Calls Qt's 'FrameOpResult QRhi::endFrame(QRhiSwapChain *swapChain,
    EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#endFrame

    Parameters
    ----------

    swapChain : Optional[QRhiSwapChain]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : EndFrameFlags
      Passed on as its number. May be left out, as in Qt: it is then
      EndFrameFlags().

    Returns
    -------

    FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FrameOpResult(number)'
      gives.
    """
    #  FrameOpResult QRhi::endFrame(QRhiSwapChain *swapChain, EndFrameFlags
    #      flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN4QRhi8endFrameEP13QRhiSwapChain6QFlagsINS_12EndFrameFlagE'
        'E',
        self._addressOf(swapChain), flags.value,
    ))

  @overload()
  @overload(EndFrameFlags)
  def endOffscreenFrame(
      self,
      flags: EndFrameFlags = EndFrameFlags(),
  ) -> FrameOpResult:
    """
    Calls Qt's 'FrameOpResult QRhi::endOffscreenFrame(EndFrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#endOffscreenFrame

    Parameters
    ----------

    flags : EndFrameFlags
      Passed on as its number. May be left out, as in Qt: it is then
      EndFrameFlags().

    Returns
    -------

    FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FrameOpResult(number)'
      gives.
    """
    #  FrameOpResult QRhi::endOffscreenFrame(EndFrameFlags flags)
    return QRhi.FrameOpResult(self.uglySide.call(
        'ritual_ZN4QRhi17endOffscreenFrameE6QFlagsINS_12EndFrameFlagEE',
        flags.value,
    ))

  def finish(self) -> FrameOpResult:
    """
    Calls Qt's 'QRhi::FrameOpResult QRhi::finish()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#finish

    Returns
    -------

    FrameOpResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FrameOpResult(number)'
      gives.
    """
    #  QRhi::FrameOpResult QRhi::finish()
    return QRhi.FrameOpResult(self.uglySide.call('ritual_ZN4QRhi6finishEv'))

  def nextResourceUpdateBatch(self) -> Optional[QRhiResourceUpdateBatch]:
    """
    Calls Qt's 'QRhiResourceUpdateBatch *QRhi::nextResourceUpdateBatch()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#nextResourceUpdateBatch

    Returns
    -------

    Optional[QRhiResourceUpdateBatch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiResourceUpdateBatch *QRhi::nextResourceUpdateBatch()
    address = self.uglySide.call('ritual_ZN4QRhi23nextResourceUpdateBatchEv')
    from . import QRhiResourceUpdateBatch
    return QRhiResourceUpdateBatch._cuteAt(address)

  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles *QRhi::nativeHandles()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QRhi::nativeHandles()
    address = self.uglySide.call('ritual_ZN4QRhi13nativeHandlesEv')
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  def makeThreadLocalNativeContextCurrent(self) -> bool:
    """
    Calls Qt's 'bool QRhi::makeThreadLocalNativeContextCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhi.html#makeThreadLocalNativeContextCurrent
    """
    #  bool QRhi::makeThreadLocalNativeContextCurrent()
    return self.uglySide.call(
        'ritual_ZN4QRhi35makeThreadLocalNativeContextCurrentEv',
    )

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QRhi::releaseCachedResources()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#releaseCachedResources
    """
    #  void QRhi::releaseCachedResources()
    self.uglySide.call('ritual_ZN4QRhi22releaseCachedResourcesEv')

  def pipelineCacheData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRhi::pipelineCacheData()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhi.html#pipelineCacheData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRhi::pipelineCacheData()
    address = self.uglySide.call('ritual_ZN4QRhi17pipelineCacheDataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def addCleanupCallback(*__, **_) -> Never:
    """
    - Qt's 'void QRhi::addCleanupCallback(const CleanupCallback &callback)':
      takes a type Python has no way to hand over yet.
    - Qt's 'void QRhi::addCleanupCallback(const void *key, const
      CleanupCallback &callback)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhi.addCleanupCallback' has no cute function yet. Qt's 'void "
        "QRhi::addCleanupCallback(const CleanupCallback &callback)': takes "
        "a type Python has no way to hand over yet. Qt's 'void "
        "QRhi::addCleanupCallback(const void *key, const CleanupCallback "
        "&callback)': names 'void', which has no cute class yet.")

  @staticmethod
  def beginFrame(*__, **_) -> Never:
    """
    Qt's 'FrameOpResult QRhi::beginFrame(QRhiSwapChain *swapChain,
    BeginFrameFlags flags)': names the enum 'QRhi::BeginFrameFlag', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QRhi.beginFrame' has no cute function yet. Qt's 'FrameOpResult "
        "QRhi::beginFrame(QRhiSwapChain *swapChain, BeginFrameFlags "
        "flags)': names the enum 'QRhi::BeginFrameFlag', whose class cannot "
        "be named here.")

  @staticmethod
  def beginOffscreenFrame(*__, **_) -> Never:
    """
    Qt's 'FrameOpResult QRhi::beginOffscreenFrame(QRhiCommandBuffer **cb,
    BeginFrameFlags flags)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRhi.beginOffscreenFrame' has no cute function yet. Qt's "
        "'FrameOpResult QRhi::beginOffscreenFrame(QRhiCommandBuffer **cb, "
        "BeginFrameFlags flags)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def removeCleanupCallback(*__, **_) -> Never:
    """
    Qt's 'void QRhi::removeCleanupCallback(const void *key)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhi.removeCleanupCallback' has no cute function yet. Qt's 'void "
        "QRhi::removeCleanupCallback(const void *key)': names 'void', which "
        "has no cute class yet.")

  @staticmethod
  def supportedSampleCounts(*__, **_) -> Never:
    """
    Qt's 'QList<int> QRhi::supportedSampleCounts() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRhi.supportedSampleCounts' has no cute function yet. Qt's "
        "'QList<int> QRhi::supportedSampleCounts() const': gives a type "
        "Python has no way to take yet.")
