"""
Qt3DRender::Render::TextureImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/textureimage_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::TextureImage to be private: it declares the
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
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TextureImage(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::TextureImage: a plain Python
  object standing in front of one C++ Qt3DRender::Render::TextureImage.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::TextureImage is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::TextureImage that has a ritual
  and that Python can call so far, 7 names in all: 'cleanup',
  'syncFromFrontEnd', 'layer', 'mipLevel', 'face', 'isDirty', 'unsetDirty'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::TextureImage::~TextureImage()': the destructor:
    Python never removes a C++ Qt3DRender::Render::TextureImage.
  - Qt's 'QTextureImageDataGeneratorPtr
    Qt3DRender::Render::TextureImage::dataGenerator() const': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::TextureImage is created at the first use, not
    by 'Qt3DRender::Render::TextureImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::TextureImage.
  - Each name of Qt's Qt3DRender::Render::TextureImage that has no cute
    function yet, 'dataGenerator', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::TextureImage'

  #  A C++ Qt3DRender::Render::TextureImage Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_TextureImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def layer(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::TextureImage::layer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-textureimage.html#layer
    """
    #  int Qt3DRender::Render::TextureImage::layer() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12TextureImage5layerEv',
    )

  def mipLevel(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::TextureImage::mipLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-textureimage.html#mipLevel
    """
    #  int Qt3DRender::Render::TextureImage::mipLevel() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12TextureImage8mipLevelEv',
    )

  def face(self) -> Qt3DRender.QAbstractTexture.CubeMapFace:
    """
    Calls Qt's 'QAbstractTexture::CubeMapFace
    Qt3DRender::Render::TextureImage::face() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-textureimage.html#face

    Returns
    -------

    Qt3DRender.QAbstractTexture.CubeMapFace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.CubeMapFace(number)' gives.
    """
    #  QAbstractTexture::CubeMapFace Qt3DRender::Render::TextureImage::face()
    #      const
    return Qt3DRender.QAbstractTexture.CubeMapFace(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12TextureImage4faceEv',
    ))

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::TextureImage::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-textureimage.html#isDirty
    """
    #  bool Qt3DRender::Render::TextureImage::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12TextureImage7isDirtyEv',
    )

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
    'Qt3DRender::Render::TextureImage::TextureImage()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-textureimage.html#TextureImage
    """
    #  Qt3DRender::Render::TextureImage::TextureImage()
    self._noteCreation(TextureImage, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12TextureImageC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::TextureImage::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-textureimage.html#cleanup
    """
    #  void Qt3DRender::Render::TextureImage::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12TextureImage7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::TextureImage::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-textureimage.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::TextureImage::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render12TextureImage16syncFromFrontEndEPKN8Q'
        't3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render12TextureImage16syncFromFrontEnd'
          'EPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def unsetDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::TextureImage::unsetDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-textureimage.html#unsetDirty
    """
    #  void Qt3DRender::Render::TextureImage::unsetDirty()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12TextureImage10unsetDirtyEv',
    )

  @staticmethod
  def dataGenerator(*__, **_) -> Never:
    """
    Qt's 'QTextureImageDataGeneratorPtr
    Qt3DRender::Render::TextureImage::dataGenerator() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.TextureImage.dataGenerator' has no cute "
        "function yet. Qt's 'QTextureImageDataGeneratorPtr "
        "Qt3DRender::Render::TextureImage::dataGenerator() const': gives a "
        "type Python has no way to take yet.")
