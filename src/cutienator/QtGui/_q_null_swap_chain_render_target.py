"""
QNullSwapChainRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QNullSwapChainRenderTarget to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class QNullSwapChainRenderTarget(QRhiSwapChainRenderTarget):
  """
  The cute side of Qt's QNullSwapChainRenderTarget: a plain Python object
  standing in front of one C++ QNullSwapChainRenderTarget.

  It is built on the cute 'QRhiSwapChainRenderTarget', as Qt's
  QNullSwapChainRenderTarget is built on Qt's QRhiSwapChainRenderTarget, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QNullSwapChainRenderTarget that has a ritual and
  that Python can call so far, 4 names in all: 'destroy', 'pixelSize',
  'devicePixelRatio', 'sampleCount'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNullSwapChainRenderTarget::~QNullSwapChainRenderTarget()': the
    destructor: Python never removes a C++ QNullSwapChainRenderTarget.

  What to expect
  --------------

  - The C++ QNullSwapChainRenderTarget is created at the first use, not by
    'QNullSwapChainRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNullSwapChainRenderTarget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNullSwapChainRenderTarget'

  #  A C++ QNullSwapChainRenderTarget Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNullSwapChainRenderTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QNullSwapChainRenderTarget::pixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchainrendertarget.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QNullSwapChainRenderTarget::pixelSize() const
    ritual = 'ritual_ZNK26QNullSwapChainRenderTarget9pixelSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QNullSwapChainRenderTarget9pixelSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'float QNullSwapChainRenderTarget::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchainrendertarget.html#devicePixelRatio
    """
    #  float QNullSwapChainRenderTarget::devicePixelRatio() const
    ritual = 'ritual_ZNK26QNullSwapChainRenderTarget16devicePixelRatioEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QNullSwapChainRenderTarget16devicePixelRatioEv')
    return self.uglySide.call(ritual)

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QNullSwapChainRenderTarget::sampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchainrendertarget.html#sampleCount
    """
    #  int QNullSwapChainRenderTarget::sampleCount() const
    ritual = 'ritual_ZNK26QNullSwapChainRenderTarget11sampleCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QNullSwapChainRenderTarget11sampleCountEv'
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
    'QNullSwapChainRenderTarget::QNullSwapChainRenderTarget(
    QRhiImplementation *rhi, QRhiSwapChain *swapchain)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchainrendertarget.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    swapchain : Optional[QRhiSwapChain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QNullSwapChainRenderTarget::QNullSwapChainRenderTarget(
    #      QRhiImplementation *rhi, QRhiSwapChain *swapchain)
    self._noteCreation(QNullSwapChainRenderTarget, lambda: Rituals.call(
        'ritual_ZN26QNullSwapChainRenderTargetC1EP18QRhiImplementationP13QR'
        'hiSwapChain',
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
    Calls Qt's 'void QNullSwapChainRenderTarget::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullswapchainrendertarget.html#destroy
    """
    #  void QNullSwapChainRenderTarget::destroy()
    ritual = 'ritual_ZN26QNullSwapChainRenderTarget7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QNullSwapChainRenderTarget7destroyEv'
    self.uglySide.call(ritual)
