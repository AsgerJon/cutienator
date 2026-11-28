"""
QVkSwapChainRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVkSwapChainRenderTarget to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiSwapChainRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QRhiImplementation, QRhiSwapChain
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiSwapChain = WAIT['QRhiSwapChain']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVkSwapChainRenderTarget(QRhiSwapChainRenderTarget):
  """
  The cute side of Qt's QVkSwapChainRenderTarget: a plain Python object
  standing in front of one C++ QVkSwapChainRenderTarget.

  It is built on the cute 'QRhiSwapChainRenderTarget', as Qt's
  QVkSwapChainRenderTarget is built on Qt's QRhiSwapChainRenderTarget, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QVkSwapChainRenderTarget that has a ritual and that
  Python can call so far, 4 names in all: 'destroy', 'pixelSize',
  'devicePixelRatio', 'sampleCount'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVkSwapChainRenderTarget::~QVkSwapChainRenderTarget()': the
    destructor: Python never removes a C++ QVkSwapChainRenderTarget.

  What to expect
  --------------

  - The C++ QVkSwapChainRenderTarget is created at the first use, not by
    'QVkSwapChainRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVkSwapChainRenderTarget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVkSwapChainRenderTarget'

  #  A C++ QVkSwapChainRenderTarget Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVkSwapChainRenderTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QVkSwapChainRenderTarget::pixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchainrendertarget.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVkSwapChainRenderTarget::pixelSize() const
    ritual = 'ritual_ZNK24QVkSwapChainRenderTarget9pixelSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QVkSwapChainRenderTarget9pixelSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'float QVkSwapChainRenderTarget::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchainrendertarget.html#devicePixelRatio
    """
    #  float QVkSwapChainRenderTarget::devicePixelRatio() const
    ritual = 'ritual_ZNK24QVkSwapChainRenderTarget16devicePixelRatioEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QVkSwapChainRenderTarget16devicePixelRatioEv'
    return self.uglySide.call(ritual)

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QVkSwapChainRenderTarget::sampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchainrendertarget.html#sampleCount
    """
    #  int QVkSwapChainRenderTarget::sampleCount() const
    ritual = 'ritual_ZNK24QVkSwapChainRenderTarget11sampleCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QVkSwapChainRenderTarget11sampleCountEv'
    return self.uglySide.call(ritual)

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

  @overload(QRhiImplementation, QRhiSwapChain)
  @overload(QRhiImplementation, NoneType)
  @overload(NoneType, QRhiSwapChain)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      swapchain: Optional[QRhiSwapChain],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QVkSwapChainRenderTarget::QVkSwapChainRenderTarget(QRhiImplementation
    *rhi, QRhiSwapChain *swapchain)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchainrendertarget.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    swapchain : Optional[QRhiSwapChain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QVkSwapChainRenderTarget::QVkSwapChainRenderTarget(QRhiImplementation
    #      *rhi, QRhiSwapChain *swapchain)
    self._noteCreation(QVkSwapChainRenderTarget, lambda: Rituals.call(
        'ritual_ZN24QVkSwapChainRenderTargetC1EP18QRhiImplementationP13QRhi'
        'SwapChain',
        self._addressOf(rhi), self._addressOf(swapchain),
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
    Calls Qt's 'void QVkSwapChainRenderTarget::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkswapchainrendertarget.html#destroy
    """
    #  void QVkSwapChainRenderTarget::destroy()
    ritual = 'ritual_ZN24QVkSwapChainRenderTarget7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QVkSwapChainRenderTarget7destroyEv'
    self.uglySide.call(ritual)
