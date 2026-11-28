"""
QRhiSwapChain binding of the Qt C++
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
  from typing import Optional

  from ..QtCore import QSize
  from . import QRhiCommandBuffer, QRhiImplementation, QRhiRenderBuffer
  from . import QRhiRenderPassDescriptor, QRhiRenderTarget
  from . import QRhiShadingRateMap, QRhiSwapChainHdrInfo
  from . import QRhiSwapChainProxyData, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiRenderBuffer = WAIT['QRhiRenderBuffer']
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']
  QRhiShadingRateMap = WAIT['QRhiShadingRateMap']
  QRhiSwapChainProxyData = WAIT['QRhiSwapChainProxyData']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiSwapChain(QRhiResource):
  """
  The cute side of Qt's QRhiSwapChain: a plain Python object standing in
  front of one C++ QRhiSwapChain.

  It is built on the cute 'QRhiResource', as Qt's QRhiSwapChain is built on
  Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiSwapChain that has a ritual and that Python can
  call so far, 25 names in all: 'resourceType', 'window', 'setWindow',
  'proxyData', 'setProxyData', 'flags', 'setFlags', 'format', 'setFormat',
  'depthStencil', 'setDepthStencil', 'sampleCount', 'setSampleCount',
  'renderPassDescriptor', 'setRenderPassDescriptor', 'shadingRateMap',
  'setShadingRateMap', 'currentPixelSize', 'currentFrameCommandBuffer',
  'currentFrameRenderTarget', 'surfacePixelSize', 'isFormatSupported',
  'newCompatibleRenderPassDescriptor', 'createOrResize', 'hdrInfo'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QRhiSwapChain is created at the first use, not by
    'QRhiSwapChain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiSwapChain.
  """

  #  The enums Qt writes inside QRhiSwapChain, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QRhiSwapChain::Flag' of Qt, with the 6 names Qt gives in
    it. Qt names the type of its combinations 'QRhiSwapChain::Flags'.
    """

    SurfaceHasPreMulAlpha = 0x1
    SurfaceHasNonPreMulAlpha = 0x2
    sRGB = 0x4
    UsedAsTransferSource = 0x8
    NoVSync = 0x10
    MinimalBufferCount = 0x20

  Flags = Flag

  class Format(CuteNum):
    """
    The enum 'QRhiSwapChain::Format' of Qt, with the 4 names Qt gives in it.
    """

    SDR = Kee[int](0)
    HDRExtendedSrgbLinear = Kee[int](1)
    HDR10 = Kee[int](2)
    HDRExtendedDisplayP3Linear = Kee[int](3)

  class StereoTargetBuffer(CuteNum):
    """
    The enum 'QRhiSwapChain::StereoTargetBuffer' of Qt, with the 2 names Qt
    gives in it.
    """

    LeftBuffer = Kee[int](0)
    RightBuffer = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiSwapChain'

  #  A C++ QRhiSwapChain Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiSwapChain'

  #  The functions Qt calls itself that QRhiSwapChain is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'currentFrameCommandBuffer': (
          ('_ZN13QRhiSwapChain25currentFrameCommandBufferEv',
           ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           ()),
      ),
      'currentFrameRenderTarget': (
          ('_ZN13QRhiSwapChain24currentFrameRenderTargetEv',
           ('address', 'address', 'QtGui:QRhiRenderTarget'),
           ()),
          ('_ZN13QRhiSwapChain24currentFrameRenderTargetENS_18StereoTargetB'
           'ufferE',
           ('address', 'address', 'QtGui:QRhiRenderTarget'),
           (
               ('int', 'enum', 'QtGui:QRhiSwapChain.StereoTargetBuffer'),
           )),
      ),
      'surfacePixelSize': (
          ('_ZN13QRhiSwapChain16surfacePixelSizeEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
      'isFormatSupported': (
          ('_ZN13QRhiSwapChain17isFormatSupportedENS_6FormatE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QRhiSwapChain.Format'),
           )),
      ),
      'newCompatibleRenderPassDescriptor': (
          ('_ZN13QRhiSwapChain33newCompatibleRenderPassDescriptorEv',
           ('address', 'address', 'QtGui:QRhiRenderPassDescriptor'),
           ()),
      ),
      'createOrResize': (
          ('_ZN13QRhiSwapChain14createOrResizeEv',
           ('bool', 'number', ''),
           ()),
      ),
      'hdrInfo': (
          ('_ZN13QRhiSwapChain7hdrInfoEv',
           ('address', 'value', 'QtGui:QRhiSwapChainHdrInfo'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiSwapChain::resourceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiSwapChain::resourceType() const
    ritual = 'ritual_ZNK13QRhiSwapChain12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QRhiSwapChain12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QRhiSwapChain::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QRhiSwapChain::window() const
    address = self.uglySide.call('ritual_ZNK13QRhiSwapChain6windowEv')
    from . import QWindow
    return QWindow._cuteAt(address)

  def proxyData(self) -> QRhiSwapChainProxyData:
    """
    Calls Qt's 'QRhiSwapChainProxyData QRhiSwapChain::proxyData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#proxyData

    Returns
    -------

    QRhiSwapChainProxyData
      A new cute QRhiSwapChainProxyData around the copy Qt gave back. Python
      owns it.
    """
    #  QRhiSwapChainProxyData QRhiSwapChain::proxyData() const
    address = self.uglySide.call('ritual_ZNK13QRhiSwapChain9proxyDataEv')
    from . import QRhiSwapChainProxyData
    return QRhiSwapChainProxyData._cuteOwning(address)

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QRhiSwapChain::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QRhiSwapChain::flags() const
    return QRhiSwapChain.Flags(self.uglySide.call(
        'ritual_ZNK13QRhiSwapChain5flagsEv',
    ))

  def format(self) -> Format:
    """
    Calls Qt's 'Format QRhiSwapChain::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format QRhiSwapChain::format() const
    return QRhiSwapChain.Format(self.uglySide.call(
        'ritual_ZNK13QRhiSwapChain6formatEv',
    ))

  def depthStencil(self) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer *QRhiSwapChain::depthStencil() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#depthStencil

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer *QRhiSwapChain::depthStencil() const
    address = self.uglySide.call('ritual_ZNK13QRhiSwapChain12depthStencilEv')
    from . import QRhiRenderBuffer
    return QRhiRenderBuffer._cuteAt(address)

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QRhiSwapChain::sampleCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#sampleCount
    """
    #  int QRhiSwapChain::sampleCount() const
    return self.uglySide.call('ritual_ZNK13QRhiSwapChain11sampleCountEv')

  def renderPassDescriptor(self) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QRhiSwapChain::renderPassDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html#renderPassDescriptor

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor *QRhiSwapChain::renderPassDescriptor() const
    address = self.uglySide.call(
        'ritual_ZNK13QRhiSwapChain20renderPassDescriptorEv',
    )
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def shadingRateMap(self) -> Optional[QRhiShadingRateMap]:
    """
    Calls Qt's 'QRhiShadingRateMap *QRhiSwapChain::shadingRateMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#shadingRateMap

    Returns
    -------

    Optional[QRhiShadingRateMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShadingRateMap *QRhiSwapChain::shadingRateMap() const
    address = self.uglySide.call(
        'ritual_ZNK13QRhiSwapChain14shadingRateMapEv',
    )
    from . import QRhiShadingRateMap
    return QRhiShadingRateMap._cuteAt(address)

  def currentPixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QRhiSwapChain::currentPixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html#currentPixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiSwapChain::currentPixelSize() const
    address = self.uglySide.call(
        'ritual_ZNK13QRhiSwapChain16currentPixelSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWindow)
  @overload(NoneType)
  def setWindow(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QRhiSwapChain::setWindow(QWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#setWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiSwapChain::setWindow(QWindow *window)
    self.uglySide.call(
        'ritual_ZN13QRhiSwapChain9setWindowEP7QWindow',
        self._addressOf(window),
    )

  @overload(QRhiSwapChainProxyData)
  def setProxyData(self, d: QRhiSwapChainProxyData) -> None:
    """
    Calls Qt's 'void QRhiSwapChain::setProxyData(const QRhiSwapChainProxyData
    &d)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#setProxyData

    Parameters
    ----------

    d : QRhiSwapChainProxyData
      Passed on as a value: Qt reads the C++ QRhiSwapChainProxyData, which
      stays Python's own.
    """
    #  void QRhiSwapChain::setProxyData(const QRhiSwapChainProxyData &d)
    self.uglySide.call(
        'ritual_ZN13QRhiSwapChain12setProxyDataERK22QRhiSwapChainProxyData',
        self._valueOf(d),
    )

  @overload(Flags)
  def setFlags(self, f: Flags) -> None:
    """
    Calls Qt's 'void QRhiSwapChain::setFlags(Flags f)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#setFlags

    Parameters
    ----------

    f : Flags
      Passed on as its number.
    """
    #  void QRhiSwapChain::setFlags(Flags f)
    self.uglySide.call(
        'ritual_ZN13QRhiSwapChain8setFlagsE6QFlagsINS_4FlagEE', f.value,
    )

  @overload(Format)
  def setFormat(self, f: Format) -> None:
    """
    Calls Qt's 'void QRhiSwapChain::setFormat(Format f)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#setFormat

    Parameters
    ----------

    f : Format
      Passed on as its number.
    """
    #  void QRhiSwapChain::setFormat(Format f)
    self.uglySide.call(
        'ritual_ZN13QRhiSwapChain9setFormatENS_6FormatE', f.value,
    )

  @overload(QRhiRenderBuffer)
  @overload(NoneType)
  def setDepthStencil(self, ds: Optional[QRhiRenderBuffer]) -> None:
    """
    Calls Qt's 'void QRhiSwapChain::setDepthStencil(QRhiRenderBuffer *ds)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#setDepthStencil

    Parameters
    ----------

    ds : Optional[QRhiRenderBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiSwapChain::setDepthStencil(QRhiRenderBuffer *ds)
    self.uglySide.call(
        'ritual_ZN13QRhiSwapChain15setDepthStencilEP16QRhiRenderBuffer',
        self._addressOf(ds),
    )

  @overload(int)
  def setSampleCount(self, samples: int) -> None:
    """
    Calls Qt's 'void QRhiSwapChain::setSampleCount(int samples)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#setSampleCount

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QRhiSwapChain::setSampleCount(int samples)
    self.uglySide.call('ritual_ZN13QRhiSwapChain14setSampleCountEi', samples)

  @overload(QRhiRenderPassDescriptor)
  @overload(NoneType)
  def setRenderPassDescriptor(
      self,
      desc: Optional[QRhiRenderPassDescriptor],
  ) -> None:
    """
    Calls Qt's 'void
    QRhiSwapChain::setRenderPassDescriptor(QRhiRenderPassDescriptor *desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html#setRenderPassDescriptor

    Parameters
    ----------

    desc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiSwapChain::setRenderPassDescriptor(QRhiRenderPassDescriptor
    #      *desc)
    self.uglySide.call(
        'ritual_ZN13QRhiSwapChain23setRenderPassDescriptorEP24QRhiRenderPas'
        'sDescriptor',
        self._addressOf(desc),
    )

  @overload(QRhiShadingRateMap)
  @overload(NoneType)
  def setShadingRateMap(self, map: Optional[QRhiShadingRateMap]) -> None:
    """
    Calls Qt's 'void QRhiSwapChain::setShadingRateMap(QRhiShadingRateMap
    *map)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html#setShadingRateMap

    Parameters
    ----------

    map : Optional[QRhiShadingRateMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiSwapChain::setShadingRateMap(QRhiShadingRateMap *map)
    self.uglySide.call(
        'ritual_ZN13QRhiSwapChain17setShadingRateMapEP18QRhiShadingRateMap',
        self._addressOf(map),
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
    'QRhiSwapChain::QRhiSwapChain(QRhiImplementation *rhi)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#QRhiSwapChain

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiSwapChain::QRhiSwapChain(QRhiImplementation *rhi)
    self._noteCreation(QRhiSwapChain, lambda: Rituals.call(
        'ritual_ZN13QRhiSwapChainC1EP18QRhiImplementation',
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

  def currentFrameCommandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer
    *QRhiSwapChain::currentFrameCommandBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html#currentFrameCommandBuffer

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer *QRhiSwapChain::currentFrameCommandBuffer()
    address = self.uglySide.call(
        'ritual_ZN13QRhiSwapChain25currentFrameCommandBufferEv',
    )
    from . import QRhiCommandBuffer
    return QRhiCommandBuffer._cuteAt(address)

  @overload()
  def currentFrameRenderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget *QRhiSwapChain::currentFrameRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html#currentFrameRenderTarget

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QRhiSwapChain::currentFrameRenderTarget()
    address = self.uglySide.call(
        'ritual_ZN13QRhiSwapChain24currentFrameRenderTargetEv',
    )
    from . import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  @overload(StereoTargetBuffer)
  def currentFrameRenderTarget(
      self,
      targetBuffer: StereoTargetBuffer,
  ) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget
    *QRhiSwapChain::currentFrameRenderTarget(StereoTargetBuffer
    targetBuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html#currentFrameRenderTarget

    Parameters
    ----------

    targetBuffer : StereoTargetBuffer
      Passed on as its number.

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget
    #      *QRhiSwapChain::currentFrameRenderTarget(StereoTargetBuffer
    #      targetBuffer)
    ritual = (
        'ritual_ZN13QRhiSwapChain24currentFrameRenderTargetENS_18StereoTarg'
        'etBufferE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QRhiSwapChain24currentFrameRenderTargetENS_18Ster'
          'eoTargetBufferE')
    address = self.uglySide.call(ritual, targetBuffer.value)
    from . import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  def surfacePixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QRhiSwapChain::surfacePixelSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html#surfacePixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiSwapChain::surfacePixelSize()
    address = self.uglySide.call(
        'ritual_ZN13QRhiSwapChain16surfacePixelSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(Format)
  def isFormatSupported(self, f: Format) -> bool:
    """
    Calls Qt's 'bool QRhiSwapChain::isFormatSupported(Format f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html#isFormatSupported

    Parameters
    ----------

    f : Format
      Passed on as its number.
    """
    #  bool QRhiSwapChain::isFormatSupported(Format f)
    return self.uglySide.call(
        'ritual_ZN13QRhiSwapChain17isFormatSupportedENS_6FormatE', f.value,
    )

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QRhiSwapChain::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchain.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QRhiSwapChain::newCompatibleRenderPassDescriptor()
    address = self.uglySide.call(
        'ritual_ZN13QRhiSwapChain33newCompatibleRenderPassDescriptorEv',
    )
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def createOrResize(self) -> bool:
    """
    Calls Qt's 'bool QRhiSwapChain::createOrResize()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#createOrResize
    """
    #  bool QRhiSwapChain::createOrResize()
    return self.uglySide.call('ritual_ZN13QRhiSwapChain14createOrResizeEv')

  def hdrInfo(self) -> QRhiSwapChainHdrInfo:
    """
    Calls Qt's 'QRhiSwapChainHdrInfo QRhiSwapChain::hdrInfo()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiswapchain.html#hdrInfo

    Returns
    -------

    QRhiSwapChainHdrInfo
      A new cute QRhiSwapChainHdrInfo around the copy Qt gave back. Python
      owns it.
    """
    #  QRhiSwapChainHdrInfo QRhiSwapChain::hdrInfo()
    ritual = 'ritual_ZN13QRhiSwapChain7hdrInfoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QRhiSwapChain7hdrInfoEv'
    address = self.uglySide.call(ritual)
    from . import QRhiSwapChainHdrInfo
    return QRhiSwapChainHdrInfo._cuteOwning(address)
