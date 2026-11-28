"""
QMetalSwapChain binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QMetalSwapChain to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QRhiSwapChain

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from . import QRhiCommandBuffer, QRhiRenderPassDescriptor, QRhiRenderTarget
  from . import QRhiSwapChainHdrInfo


class QMetalSwapChain(QRhiSwapChain):
  """
  The cute side of Qt's QMetalSwapChain: a plain Python object standing in
  front of one C++ QMetalSwapChain.

  It is built on the cute 'QRhiSwapChain', as Qt's QMetalSwapChain is built
  on Qt's QRhiSwapChain, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMetalSwapChain that has a ritual and that Python
  can call so far, 8 names in all: 'destroy', 'currentFrameCommandBuffer',
  'currentFrameRenderTarget', 'surfacePixelSize', 'isFormatSupported',
  'newCompatibleRenderPassDescriptor', 'createOrResize', 'hdrInfo'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QMetalSwapChain is created at the first use, not by
    'QMetalSwapChain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetalSwapChain.
  - Each name of Qt's QMetalSwapChain that has no cute function yet,
    '__init__', 'chooseFormats', 'waitUntilCompleted', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetalSwapChain'

  #  A C++ QMetalSwapChain Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMetalSwapChain'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QMetalSwapChain::QMetalSwapChain(QRhiImplementation *rhi)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QMetalSwapChain.__init__' has no cute function yet. Qt's "
        "'QMetalSwapChain::QMetalSwapChain(QRhiImplementation *rhi)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

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
    Calls Qt's 'void QMetalSwapChain::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qmetalswapchain.html#destroy
    """
    #  void QMetalSwapChain::destroy()
    self.uglySide.call('ritual_ZN15QMetalSwapChain7destroyEv')

  def currentFrameCommandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer
    *QMetalSwapChain::currentFrameCommandBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalswapchain.html#currentFrameCommandBuffer

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer *QMetalSwapChain::currentFrameCommandBuffer()
    address = self.uglySide.call(
        'ritual_ZN15QMetalSwapChain25currentFrameCommandBufferEv',
    )
    from . import QRhiCommandBuffer
    return QRhiCommandBuffer._cuteAt(address)

  def currentFrameRenderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget
    *QMetalSwapChain::currentFrameRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalswapchain.html#currentFrameRenderTarget

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QMetalSwapChain::currentFrameRenderTarget()
    address = self.uglySide.call(
        'ritual_ZN15QMetalSwapChain24currentFrameRenderTargetEv',
    )
    from . import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  def surfacePixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QMetalSwapChain::surfacePixelSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalswapchain.html#surfacePixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMetalSwapChain::surfacePixelSize()
    address = self.uglySide.call(
        'ritual_ZN15QMetalSwapChain16surfacePixelSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QRhiSwapChain.Format)
  def isFormatSupported(self, f: QRhiSwapChain.Format) -> bool:
    """
    Calls Qt's 'bool QMetalSwapChain::isFormatSupported(Format f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalswapchain.html#isFormatSupported

    Parameters
    ----------

    f : QRhiSwapChain.Format
      Passed on as its number.
    """
    #  bool QMetalSwapChain::isFormatSupported(Format f)
    return self.uglySide.call(
        'ritual_ZN15QMetalSwapChain17isFormatSupportedEN13QRhiSwapChain6For'
        'matE',
        f.value,
    )

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QMetalSwapChain::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalswapchain.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QMetalSwapChain::newCompatibleRenderPassDescriptor()
    address = self.uglySide.call(
        'ritual_ZN15QMetalSwapChain33newCompatibleRenderPassDescriptorEv',
    )
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def createOrResize(self) -> bool:
    """
    Calls Qt's 'bool QMetalSwapChain::createOrResize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalswapchain.html#createOrResize
    """
    #  bool QMetalSwapChain::createOrResize()
    return self.uglySide.call('ritual_ZN15QMetalSwapChain14createOrResizeEv')

  def hdrInfo(self) -> QRhiSwapChainHdrInfo:
    """
    Calls Qt's 'QRhiSwapChainHdrInfo QMetalSwapChain::hdrInfo()'.

    Qt's own words: https://doc.qt.io/qt-6/qmetalswapchain.html#hdrInfo

    Returns
    -------

    QRhiSwapChainHdrInfo
      A new cute QRhiSwapChainHdrInfo around the copy Qt gave back. Python
      owns it.
    """
    #  QRhiSwapChainHdrInfo QMetalSwapChain::hdrInfo()
    address = self.uglySide.call('ritual_ZN15QMetalSwapChain7hdrInfoEv')
    from . import QRhiSwapChainHdrInfo
    return QRhiSwapChainHdrInfo._cuteOwning(address)

  @staticmethod
  def chooseFormats(*__, **_) -> Never:
    """
    Qt's 'void QMetalSwapChain::chooseFormats()': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QMetalSwapChain.chooseFormats' has no cute function yet. Qt's "
        "'void QMetalSwapChain::chooseFormats()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def waitUntilCompleted(*__, **_) -> Never:
    """
    Qt's 'void QMetalSwapChain::waitUntilCompleted(int slot)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QMetalSwapChain.waitUntilCompleted' has no cute function yet. "
        "Qt's 'void QMetalSwapChain::waitUntilCompleted(int slot)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
