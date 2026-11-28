"""
Qt3DRender::Render::RenderTargetOutput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/rendertargetoutput_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::RenderTargetOutput to be private: it declares
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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderTargetOutput(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::RenderTargetOutput: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::RenderTargetOutput.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::RenderTargetOutput is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RenderTargetOutput that has a
  ritual and that Python can call so far, 8 names in all: 'textureUuid',
  'mipLevel', 'layer', 'name', 'face', 'point', 'syncFromFrontEnd',
  'attachment'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const Attachment
    *Qt3DRender::Render::RenderTargetOutput::attachment() const': takes in
    Python what 'Attachment
    *Qt3DRender::Render::RenderTargetOutput::attachment()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RenderTargetOutput is created at the first
    use, not by 'Qt3DRender::Render::RenderTargetOutput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::RenderTargetOutput.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::RenderTargetOutput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def textureUuid(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::RenderTargetOutput::textureUuid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetoutput.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DRender::Render::RenderTargetOutput::textureUuid() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render18RenderTargetOutput11textureUuidEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def mipLevel(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::RenderTargetOutput::mipLevel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetoutput.html#mipLevel
    """
    #  int Qt3DRender::Render::RenderTargetOutput::mipLevel() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render18RenderTargetOutput8mipLevelEv',
    )

  def layer(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::RenderTargetOutput::layer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetoutput.html#layer
    """
    #  int Qt3DRender::Render::RenderTargetOutput::layer() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render18RenderTargetOutput5layerEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::Render::RenderTargetOutput::name()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetoutput.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::RenderTargetOutput::name() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render18RenderTargetOutput4nameEv',
    )

  def face(self) -> Qt3DRender.QAbstractTexture.CubeMapFace:
    """
    Calls Qt's 'QAbstractTexture::CubeMapFace
    Qt3DRender::Render::RenderTargetOutput::face() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetoutput.html#face

    Returns
    -------

    Qt3DRender.QAbstractTexture.CubeMapFace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.CubeMapFace(number)' gives.
    """
    #  QAbstractTexture::CubeMapFace
    #      Qt3DRender::Render::RenderTargetOutput::face() const
    return Qt3DRender.QAbstractTexture.CubeMapFace(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render18RenderTargetOutput4faceEv',
    ))

  def point(self) -> Qt3DRender.QRenderTargetOutput.AttachmentPoint:
    """
    Calls Qt's 'QRenderTargetOutput::AttachmentPoint
    Qt3DRender::Render::RenderTargetOutput::point() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetoutput.html#point

    Returns
    -------

    Qt3DRender.QRenderTargetOutput.AttachmentPoint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QRenderTargetOutput.AttachmentPoint(number)' gives.
    """
    #  QRenderTargetOutput::AttachmentPoint
    #      Qt3DRender::Render::RenderTargetOutput::point() const
    return Qt3DRender.QRenderTargetOutput.AttachmentPoint(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render18RenderTargetOutput5pointEv',
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
    'Qt3DRender::Render::RenderTargetOutput::RenderTargetOutput()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetoutput.html
    """
    #  Qt3DRender::Render::RenderTargetOutput::RenderTargetOutput()
    self._noteCreation(RenderTargetOutput, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render18RenderTargetOutputC1Ev',
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
    Qt3DRender::Render::RenderTargetOutput::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetoutput.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::RenderTargetOutput::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render18RenderTargetOutput16syncFromFrontEnd'
        'EPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render18RenderTargetOutput16syncFromFr'
          'ontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def attachment(self) -> Optional[Qt3DRender.Render.Attachment]:
    """
    Calls Qt's 'Attachment
    *Qt3DRender::Render::RenderTargetOutput::attachment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetoutput.html

    Returns
    -------

    Optional[Qt3DRender.Render.Attachment]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Attachment *Qt3DRender::Render::RenderTargetOutput::attachment()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18RenderTargetOutput10attachmentEv',
    )
    return Qt3DRender.Render.Attachment._cuteAt(address)
