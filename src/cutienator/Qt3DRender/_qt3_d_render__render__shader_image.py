"""
Qt3DRender::Render::ShaderImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/shaderimage_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::ShaderImage to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
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


class ShaderImage(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::ShaderImage: a plain Python
  object standing in front of one C++ Qt3DRender::Render::ShaderImage.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::ShaderImage is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ShaderImage that has a ritual
  and that Python can call so far, 8 names in all: 'cleanup',
  'syncFromFrontEnd', 'textureId', 'mipLevel', 'layer', 'layered', 'access',
  'format'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ShaderImage is created at the first use, not
    by 'Qt3DRender::Render::ShaderImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::ShaderImage.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::ShaderImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def textureId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::ShaderImage::textureId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderimage.html#textureId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::ShaderImage::textureId() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render11ShaderImage9textureIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def mipLevel(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::ShaderImage::mipLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderimage.html#mipLevel
    """
    #  int Qt3DRender::Render::ShaderImage::mipLevel() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render11ShaderImage8mipLevelEv',
    )

  def layer(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::ShaderImage::layer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderimage.html#layer
    """
    #  int Qt3DRender::Render::ShaderImage::layer() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render11ShaderImage5layerEv',
    )

  def layered(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::ShaderImage::layered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderimage.html#layered
    """
    #  bool Qt3DRender::Render::ShaderImage::layered() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render11ShaderImage7layeredEv',
    )

  def access(self) -> Qt3DRender.QShaderImage.Access:
    """
    Calls Qt's 'QShaderImage::Access
    Qt3DRender::Render::ShaderImage::access() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderimage.html#access

    Returns
    -------

    Qt3DRender.QShaderImage.Access
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QShaderImage.Access(number)' gives.
    """
    #  QShaderImage::Access Qt3DRender::Render::ShaderImage::access() const
    return Qt3DRender.QShaderImage.Access(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render11ShaderImage6accessEv',
    ))

  def format(self) -> Qt3DRender.QShaderImage.ImageFormat:
    """
    Calls Qt's 'QShaderImage::ImageFormat
    Qt3DRender::Render::ShaderImage::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderimage.html#format

    Returns
    -------

    Qt3DRender.QShaderImage.ImageFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QShaderImage.ImageFormat(number)' gives.
    """
    #  QShaderImage::ImageFormat Qt3DRender::Render::ShaderImage::format()
    #      const
    return Qt3DRender.QShaderImage.ImageFormat(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render11ShaderImage6formatEv',
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
    'Qt3DRender::Render::ShaderImage::ShaderImage()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderimage.html#ShaderImage
    """
    #  Qt3DRender::Render::ShaderImage::ShaderImage()
    self._noteCreation(ShaderImage, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render11ShaderImageC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ShaderImage::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderimage.html#cleanup
    """
    #  void Qt3DRender::Render::ShaderImage::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render11ShaderImage7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ShaderImage::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderimage.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ShaderImage::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render11ShaderImage16syncFromFrontEndEPKN8Qt'
        '3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render11ShaderImage16syncFromFrontEndE'
          'PKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
