"""
Qt3DRender::Render::BlitFramebuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/blitframebuffer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::BlitFramebuffer to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BlitFramebuffer(Qt3DRender.Render.FrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::Render::BlitFramebuffer: a plain Python
  object standing in front of one C++ Qt3DRender::Render::BlitFramebuffer.

  It is built on the cute 'Qt3DRender::Render::FrameGraphNode', as Qt's
  Qt3DRender::Render::BlitFramebuffer is built on Qt's
  Qt3DRender::Render::FrameGraphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::BlitFramebuffer that has a
  ritual and that Python can call so far, 8 names in all: 'syncFromFrontEnd',
  'sourceRenderTargetId', 'destinationRenderTargetId', 'sourceRect',
  'destinationRect', 'sourceAttachmentPoint', 'destinationAttachmentPoint',
  'interpolationMethod'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::BlitFramebuffer is created at the first use,
    not by 'Qt3DRender::Render::BlitFramebuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::BlitFramebuffer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::BlitFramebuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sourceRenderTargetId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::BlitFramebuffer::sourceRenderTargetId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-blitframebuffer.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DRender::Render::BlitFramebuffer::sourceRenderTargetId() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15BlitFramebuffer20sourceRenderTarget'
        'IdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def destinationRenderTargetId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::BlitFramebuffer::destinationRenderTargetId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-blitframebuffer.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DRender::Render::BlitFramebuffer::destinationRenderTargetId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15BlitFramebuffer25destinationRenderT'
        'argetIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def sourceRect(self) -> QRect:
    """
    Calls Qt's 'QRect Qt3DRender::Render::BlitFramebuffer::sourceRect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-blitframebuffer.html#sourceRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Qt3DRender::Render::BlitFramebuffer::sourceRect() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15BlitFramebuffer10sourceRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def destinationRect(self) -> QRect:
    """
    Calls Qt's 'QRect Qt3DRender::Render::BlitFramebuffer::destinationRect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-blitframebuffer.html

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Qt3DRender::Render::BlitFramebuffer::destinationRect() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15BlitFramebuffer15destinationRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def sourceAttachmentPoint(
      self,
  ) -> Qt3DRender.QRenderTargetOutput.AttachmentPoint:
    """
    Calls Qt's 'Qt3DRender::QRenderTargetOutput::AttachmentPoint
    Qt3DRender::Render::BlitFramebuffer::sourceAttachmentPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-blitframebuffer.html

    Returns
    -------

    Qt3DRender.QRenderTargetOutput.AttachmentPoint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QRenderTargetOutput.AttachmentPoint(number)' gives.
    """
    #  Qt3DRender::QRenderTargetOutput::AttachmentPoint
    #      Qt3DRender::Render::BlitFramebuffer::sourceAttachmentPoint() const
    return Qt3DRender.QRenderTargetOutput.AttachmentPoint(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15BlitFramebuffer21sourceAttachmentPo'
        'intEv',
    ))

  def destinationAttachmentPoint(
      self,
  ) -> Qt3DRender.QRenderTargetOutput.AttachmentPoint:
    """
    Calls Qt's 'Qt3DRender::QRenderTargetOutput::AttachmentPoint
    Qt3DRender::Render::BlitFramebuffer::destinationAttachmentPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-blitframebuffer.html

    Returns
    -------

    Qt3DRender.QRenderTargetOutput.AttachmentPoint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QRenderTargetOutput.AttachmentPoint(number)' gives.
    """
    #  Qt3DRender::QRenderTargetOutput::AttachmentPoint
    #      Qt3DRender::Render::BlitFramebuffer::destinationAttachmentPoint()
    #      const
    return Qt3DRender.QRenderTargetOutput.AttachmentPoint(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15BlitFramebuffer26destinationAttachm'
        'entPointEv',
    ))

  def interpolationMethod(
      self,
  ) -> Qt3DRender.QBlitFramebuffer.InterpolationMethod:
    """
    Calls Qt's 'QBlitFramebuffer::InterpolationMethod
    Qt3DRender::Render::BlitFramebuffer::interpolationMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-blitframebuffer.html

    Returns
    -------

    Qt3DRender.QBlitFramebuffer.InterpolationMethod
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QBlitFramebuffer.InterpolationMethod(number)' gives.
    """
    #  QBlitFramebuffer::InterpolationMethod
    #      Qt3DRender::Render::BlitFramebuffer::interpolationMethod() const
    return Qt3DRender.QBlitFramebuffer.InterpolationMethod(
        self.uglySide.call(
            'ritual_ZNK10Qt3DRender6Render15BlitFramebuffer19interpolationM'
            'ethodEv',
        ))

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::BlitFramebuffer::BlitFramebuffer()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-blitframebuffer.html
    """
    #  Qt3DRender::Render::BlitFramebuffer::BlitFramebuffer()
    self._noteCreation(BlitFramebuffer, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render15BlitFramebufferC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::BlitFramebuffer::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-blitframebuffer.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::BlitFramebuffer::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render15BlitFramebuffer16syncFromFrontEndEPK'
        'N8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render15BlitFramebuffer16syncFromFront'
          'EndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
