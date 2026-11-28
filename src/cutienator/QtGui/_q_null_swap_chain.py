"""
QNullSwapChain binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QNullSwapChain to be private: it declares the class in a header
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
  from . import QRhiCommandBuffer, QRhiImplementation
  from . import QRhiRenderPassDescriptor, QRhiRenderTarget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNullSwapChain(QRhiSwapChain):
  """
  The cute side of Qt's QNullSwapChain: a plain Python object standing in
  front of one C++ QNullSwapChain.

  It is built on the cute 'QRhiSwapChain', as Qt's QNullSwapChain is built on
  Qt's QRhiSwapChain, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNullSwapChain that has a ritual and that Python can
  call so far, 7 names in all: 'destroy', 'currentFrameCommandBuffer',
  'currentFrameRenderTarget', 'surfacePixelSize', 'isFormatSupported',
  'newCompatibleRenderPassDescriptor', 'createOrResize'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNullSwapChain::~QNullSwapChain()': the destructor: Python never
    removes a C++ QNullSwapChain.

  What to expect
  --------------

  - The C++ QNullSwapChain is created at the first use, not by
    'QNullSwapChain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNullSwapChain.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNullSwapChain'

  #  A C++ QNullSwapChain Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNullSwapChain'

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
    'QNullSwapChain::QNullSwapChain(QRhiImplementation *rhi)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnullswapchain.html#QNullSwapChain

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QNullSwapChain::QNullSwapChain(QRhiImplementation *rhi)
    self._noteCreation(QNullSwapChain, lambda: Rituals.call(
        'ritual_ZN14QNullSwapChainC1EP18QRhiImplementation',
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
    Calls Qt's 'void QNullSwapChain::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qnullswapchain.html#destroy
    """
    #  void QNullSwapChain::destroy()
    ritual = 'ritual_ZN14QNullSwapChain7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QNullSwapChain7destroyEv'
    self.uglySide.call(ritual)

  def currentFrameCommandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer
    *QNullSwapChain::currentFrameCommandBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchain.html#currentFrameCommandBuffer

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer *QNullSwapChain::currentFrameCommandBuffer()
    ritual = 'ritual_ZN14QNullSwapChain25currentFrameCommandBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QNullSwapChain25currentFrameCommandBufferEv'
    address = self.uglySide.call(ritual)
    from . import QRhiCommandBuffer
    return QRhiCommandBuffer._cuteAt(address)

  def currentFrameRenderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget
    *QNullSwapChain::currentFrameRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchain.html#currentFrameRenderTarget

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QNullSwapChain::currentFrameRenderTarget()
    ritual = 'ritual_ZN14QNullSwapChain24currentFrameRenderTargetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QNullSwapChain24currentFrameRenderTargetEv'
    address = self.uglySide.call(ritual)
    from . import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  def surfacePixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QNullSwapChain::surfacePixelSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchain.html#surfacePixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QNullSwapChain::surfacePixelSize()
    ritual = 'ritual_ZN14QNullSwapChain16surfacePixelSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QNullSwapChain16surfacePixelSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QRhiSwapChain.Format)
  def isFormatSupported(self, f: QRhiSwapChain.Format) -> bool:
    """
    Calls Qt's 'bool QNullSwapChain::isFormatSupported(Format f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchain.html#isFormatSupported

    Parameters
    ----------

    f : QRhiSwapChain.Format
      Passed on as its number.
    """
    #  bool QNullSwapChain::isFormatSupported(Format f)
    ritual = (
        'ritual_ZN14QNullSwapChain17isFormatSupportedEN13QRhiSwapChain6Form'
        'atE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QNullSwapChain17isFormatSupportedEN13QRhiSwapChai'
          'n6FormatE')
    return self.uglySide.call(ritual, f.value)

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QNullSwapChain::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchain.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QNullSwapChain::newCompatibleRenderPassDescriptor()
    ritual = 'ritual_ZN14QNullSwapChain33newCompatibleRenderPassDescriptorEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QNullSwapChain33newCompatibleRenderPassDescriptor'
          'Ev')
    address = self.uglySide.call(ritual)
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def createOrResize(self) -> bool:
    """
    Calls Qt's 'bool QNullSwapChain::createOrResize()'.

    Qt's own words: https://doc.qt.io/qt-6/qnullswapchain.html#createOrResize
    """
    #  bool QNullSwapChain::createOrResize()
    ritual = 'ritual_ZN14QNullSwapChain14createOrResizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QNullSwapChain14createOrResizeEv'
    return self.uglySide.call(ritual)
