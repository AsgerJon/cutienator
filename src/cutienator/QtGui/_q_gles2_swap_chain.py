"""
QGles2SwapChain binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGles2SwapChain to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiSwapChain

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QGles2SwapChainRenderTarget, QRhiCommandBuffer
  from . import QRhiImplementation, QRhiRenderPassDescriptor
  from . import QRhiRenderTarget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGles2SwapChainRenderTarget = WAIT['QGles2SwapChainRenderTarget']
  QRhiImplementation = WAIT['QRhiImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGles2SwapChain(QRhiSwapChain):
  """
  The cute side of Qt's QGles2SwapChain: a plain Python object standing in
  front of one C++ QGles2SwapChain.

  It is built on the cute 'QRhiSwapChain', as Qt's QGles2SwapChain is built
  on Qt's QRhiSwapChain, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGles2SwapChain that has a ritual and that Python
  can call so far, 8 names in all: 'destroy', 'currentFrameCommandBuffer',
  'currentFrameRenderTarget', 'surfacePixelSize', 'isFormatSupported',
  'newCompatibleRenderPassDescriptor', 'createOrResize',
  'initSwapChainRenderTarget'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGles2SwapChain::~QGles2SwapChain()': the destructor: Python never
    removes a C++ QGles2SwapChain.

  What to expect
  --------------

  - The C++ QGles2SwapChain is created at the first use, not by
    'QGles2SwapChain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGles2SwapChain.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGles2SwapChain'

  #  A C++ QGles2SwapChain Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGles2SwapChain'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QGles2SwapChain::QGles2SwapChain(QRhiImplementation *rhi)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchain.html#QGles2SwapChain

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGles2SwapChain::QGles2SwapChain(QRhiImplementation *rhi)
    self._noteCreation(QGles2SwapChain, lambda: Rituals.call(
        'ritual_ZN15QGles2SwapChainC1EP18QRhiImplementation',
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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QGles2SwapChain::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2swapchain.html#destroy
    """
    #  void QGles2SwapChain::destroy()
    ritual = 'ritual_ZN15QGles2SwapChain7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGles2SwapChain7destroyEv'
    self.uglySide.call(ritual)

  def currentFrameCommandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer
    *QGles2SwapChain::currentFrameCommandBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchain.html#currentFrameCommandBuffer

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer *QGles2SwapChain::currentFrameCommandBuffer()
    ritual = 'ritual_ZN15QGles2SwapChain25currentFrameCommandBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGles2SwapChain25currentFrameCommandBufferEv'
    address = self.uglySide.call(ritual)
    from . import QRhiCommandBuffer
    return QRhiCommandBuffer._cuteAt(address)

  @overload()
  def currentFrameRenderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget
    *QGles2SwapChain::currentFrameRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchain.html#currentFrameRenderTarget

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QGles2SwapChain::currentFrameRenderTarget()
    ritual = 'ritual_ZN15QGles2SwapChain24currentFrameRenderTargetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGles2SwapChain24currentFrameRenderTargetEv'
    address = self.uglySide.call(ritual)
    from . import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  @overload(QRhiSwapChain.StereoTargetBuffer)
  def currentFrameRenderTarget(
      self,
      targetBuffer: QRhiSwapChain.StereoTargetBuffer,
  ) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget
    *QGles2SwapChain::currentFrameRenderTarget(StereoTargetBuffer
    targetBuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchain.html#currentFrameRenderTarget

    Parameters
    ----------

    targetBuffer : QRhiSwapChain.StereoTargetBuffer
      Passed on as its number.

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget
    #      *QGles2SwapChain::currentFrameRenderTarget(StereoTargetBuffer
    #      targetBuffer)
    ritual = (
        'ritual_ZN15QGles2SwapChain24currentFrameRenderTargetEN13QRhiSwapCh'
        'ain18StereoTargetBufferE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QGles2SwapChain24currentFrameRenderTargetEN13QRhi'
          'SwapChain18StereoTargetBufferE')
    address = self.uglySide.call(ritual, targetBuffer.value)
    from . import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  def surfacePixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QGles2SwapChain::surfacePixelSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchain.html#surfacePixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGles2SwapChain::surfacePixelSize()
    ritual = 'ritual_ZN15QGles2SwapChain16surfacePixelSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGles2SwapChain16surfacePixelSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QRhiSwapChain.Format)
  def isFormatSupported(self, f: QRhiSwapChain.Format) -> bool:
    """
    Calls Qt's 'bool QGles2SwapChain::isFormatSupported(Format f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchain.html#isFormatSupported

    Parameters
    ----------

    f : QRhiSwapChain.Format
      Passed on as its number.
    """
    #  bool QGles2SwapChain::isFormatSupported(Format f)
    ritual = (
        'ritual_ZN15QGles2SwapChain17isFormatSupportedEN13QRhiSwapChain6For'
        'matE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QGles2SwapChain17isFormatSupportedEN13QRhiSwapCha'
          'in6FormatE')
    return self.uglySide.call(ritual, f.value)

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QGles2SwapChain::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchain.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QGles2SwapChain::newCompatibleRenderPassDescriptor()
    ritual = (
        'ritual_ZN15QGles2SwapChain33newCompatibleRenderPassDescriptorEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QGles2SwapChain33newCompatibleRenderPassDescripto'
          'rEv')
    address = self.uglySide.call(ritual)
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def createOrResize(self) -> bool:
    """
    Calls Qt's 'bool QGles2SwapChain::createOrResize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchain.html#createOrResize
    """
    #  bool QGles2SwapChain::createOrResize()
    ritual = 'ritual_ZN15QGles2SwapChain14createOrResizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGles2SwapChain14createOrResizeEv'
    return self.uglySide.call(ritual)

  @overload(QGles2SwapChainRenderTarget)
  @overload(NoneType)
  def initSwapChainRenderTarget(
      self,
      rt: Optional[QGles2SwapChainRenderTarget],
  ) -> None:
    """
    Calls Qt's 'void
    QGles2SwapChain::initSwapChainRenderTarget(QGles2SwapChainRenderTarget
    *rt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchain.html#initSwapChainRenderTarget

    Parameters
    ----------

    rt : Optional[QGles2SwapChainRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGles2SwapChain::initSwapChainRenderTarget(
    #      QGles2SwapChainRenderTarget *rt)
    self.uglySide.call(
        'ritual_ZN15QGles2SwapChain25initSwapChainRenderTargetEP27QGles2Swa'
        'pChainRenderTarget',
        self._addressOf(rt),
    )
