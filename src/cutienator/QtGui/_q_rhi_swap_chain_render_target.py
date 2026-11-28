"""
QRhiSwapChainRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiRenderTarget, QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

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


class QRhiSwapChainRenderTarget(QRhiRenderTarget):
  """
  The cute side of Qt's QRhiSwapChainRenderTarget: a plain Python object
  standing in front of one C++ QRhiSwapChainRenderTarget.

  It is built on the cute 'QRhiRenderTarget', as Qt's
  QRhiSwapChainRenderTarget is built on Qt's QRhiRenderTarget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiSwapChainRenderTarget that has a ritual and that
  Python can call so far, 2 names in all: 'resourceType', 'swapChain'. It can
  be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QRhiSwapChainRenderTarget is created at the first use, not by
    'QRhiSwapChainRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiSwapChainRenderTarget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiSwapChainRenderTarget'

  #  A C++ QRhiSwapChainRenderTarget Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiSwapChainRenderTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiSwapChainRenderTarget::resourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchainrendertarget.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiSwapChainRenderTarget::resourceType() const
    ritual = 'ritual_ZNK25QRhiSwapChainRenderTarget12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QRhiSwapChainRenderTarget12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def swapChain(self) -> Optional[QRhiSwapChain]:
    """
    Calls Qt's 'QRhiSwapChain *QRhiSwapChainRenderTarget::swapChain() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchainrendertarget.html#swapChain

    Returns
    -------

    Optional[QRhiSwapChain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSwapChain *QRhiSwapChainRenderTarget::swapChain() const
    address = self.uglySide.call(
        'ritual_ZNK25QRhiSwapChainRenderTarget9swapChainEv',
    )
    from . import QRhiSwapChain
    return QRhiSwapChain._cuteAt(address)

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
      swapchain_: Optional[QRhiSwapChain],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiSwapChainRenderTarget::QRhiSwapChainRenderTarget(QRhiImplementation
    *rhi, QRhiSwapChain *swapchain_)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiswapchainrendertarget.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    swapchain_ : Optional[QRhiSwapChain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiSwapChainRenderTarget::QRhiSwapChainRenderTarget(
    #      QRhiImplementation *rhi, QRhiSwapChain *swapchain_)
    self._noteCreation(QRhiSwapChainRenderTarget, lambda: Rituals.call(
        'ritual_ZN25QRhiSwapChainRenderTargetC1EP18QRhiImplementationP13QRh'
        'iSwapChain',
        self._addressOf(rhi), self._addressOf(swapchain_),
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
