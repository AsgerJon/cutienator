"""
QSGRhiAtlasTexture::Texture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGRhiAtlasTexture::Texture to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGRhiAtlasTexture, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect, QRectF, QSize
  from ..QtGui import QImage, QRhiResourceUpdateBatch
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Texture(QSGRhiAtlasTexture.TextureBase):
  """
  The cute side of Qt's QSGRhiAtlasTexture::Texture: a plain Python object
  standing in front of one C++ QSGRhiAtlasTexture::Texture.

  It is built on the cute 'QSGRhiAtlasTexture::TextureBase', as Qt's
  QSGRhiAtlasTexture::Texture is built on Qt's
  QSGRhiAtlasTexture::TextureBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiAtlasTexture::Texture that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'textureSize',
  'setHasAlphaChannel', 'hasAlphaChannel', 'hasMipmaps',
  'normalizedTextureSubRect', 'atlasSubRect', 'atlasSubRectWithoutPadding',
  'removedFromAtlas', 'releaseImage', 'image'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGRhiAtlasTexture::Texture::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QSGRhiAtlasTexture::Texture::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGRhiAtlasTexture::Texture::~Texture()': the destructor: Python
    never removes a C++ QSGRhiAtlasTexture::Texture.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'QSGRhiAtlasTexture.

  What to expect
  --------------

  - The C++ QSGRhiAtlasTexture::Texture is created at the first use, not by
    'QSGRhiAtlasTexture::Texture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiAtlasTexture::Texture.
  - Qt tells when it has removed the C++ QSGRhiAtlasTexture::Texture. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGRhiAtlasTexture::Texture that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiAtlasTexture::Texture'

  #  A C++ QSGRhiAtlasTexture::Texture Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRhiAtlasTexture_Texture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGRhiAtlasTexture::Texture::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGRhiAtlasTexture::Texture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture7Texture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGRhiAtlasTexture::Texture::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGRhiAtlasTexture::Texture::textureSize() const
    ritual = 'ritual_ZNK18QSGRhiAtlasTexture7Texture11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSGRhiAtlasTexture7Texture11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiAtlasTexture::Texture::hasAlphaChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html#hasAlphaChannel
    """
    #  bool QSGRhiAtlasTexture::Texture::hasAlphaChannel() const
    ritual = 'ritual_ZNK18QSGRhiAtlasTexture7Texture15hasAlphaChannelEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QSGRhiAtlasTexture7Texture15hasAlphaChannelEv')
    return self.uglySide.call(ritual)

  def hasMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiAtlasTexture::Texture::hasMipmaps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html#hasMipmaps
    """
    #  bool QSGRhiAtlasTexture::Texture::hasMipmaps() const
    ritual = 'ritual_ZNK18QSGRhiAtlasTexture7Texture10hasMipmapsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSGRhiAtlasTexture7Texture10hasMipmapsEv'
    return self.uglySide.call(ritual)

  def normalizedTextureSubRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF
    QSGRhiAtlasTexture::Texture::normalizedTextureSubRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGRhiAtlasTexture::Texture::normalizedTextureSubRect() const
    ritual = (
        'ritual_ZNK18QSGRhiAtlasTexture7Texture24normalizedTextureSubRectEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QSGRhiAtlasTexture7Texture24normalizedTextureSub'
          'RectEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def atlasSubRect(self) -> QRect:
    """
    Calls Qt's 'QRect QSGRhiAtlasTexture::Texture::atlasSubRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html#atlasSubRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSGRhiAtlasTexture::Texture::atlasSubRect() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture7Texture12atlasSubRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def atlasSubRectWithoutPadding(self) -> QRect:
    """
    Calls Qt's 'QRect
    QSGRhiAtlasTexture::Texture::atlasSubRectWithoutPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSGRhiAtlasTexture::Texture::atlasSubRectWithoutPadding() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture7Texture26atlasSubRectWithoutPadding'
        'Ev',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def removedFromAtlas(
      self,
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QSGRhiAtlasTexture::Texture::removedFromAtlas(QRhiResourceUpdateBatch
    *resourceUpdates) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html#removedFromAtlas

    Parameters
    ----------

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGRhiAtlasTexture::Texture::removedFromAtlas(
    #      QRhiResourceUpdateBatch *resourceUpdates) const
    ritual = (
        'ritual_ZNK18QSGRhiAtlasTexture7Texture16removedFromAtlasEP23QRhiRe'
        'sourceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QSGRhiAtlasTexture7Texture16removedFromAtlasEP23'
          'QRhiResourceUpdateBatch')
    address = self.uglySide.call(ritual, self._addressOf(resourceUpdates))
    return QSGTexture._cuteAt(address)

  def image(self) -> QImage:
    """
    Calls Qt's 'const QImage &QSGRhiAtlasTexture::Texture::image() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  const QImage &QSGRhiAtlasTexture::Texture::image() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture7Texture5imageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHasAlphaChannel(self, alpha: bool) -> None:
    """
    Calls Qt's 'void QSGRhiAtlasTexture::Texture::setHasAlphaChannel(bool
    alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html#setHasAlphaChannel

    Parameters
    ----------

    alpha : bool
      Passed on as it is.
    """
    #  void QSGRhiAtlasTexture::Texture::setHasAlphaChannel(bool alpha)
    self.uglySide.call(
        'ritual_ZN18QSGRhiAtlasTexture7Texture18setHasAlphaChannelEb', alpha,
    )

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
    Qt's 'QSGRhiAtlasTexture::Texture::Texture(Atlas *atlas, const QRect
    &textureRect, const QImage &image)': leans on
    'QSGRhiAtlasTexture::Texture::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGRhiAtlasTexture.Texture.__init__' has no cute function yet. "
        "Qt's 'QSGRhiAtlasTexture::Texture::Texture(Atlas *atlas, const "
        "QRect &textureRect, const QImage &image)': leans on "
        "'QSGRhiAtlasTexture::Texture::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def releaseImage(self) -> None:
    """
    Calls Qt's 'void QSGRhiAtlasTexture::Texture::releaseImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texture.html#releaseImage
    """
    #  void QSGRhiAtlasTexture::Texture::releaseImage()
    self.uglySide.call(
        'ritual_ZN18QSGRhiAtlasTexture7Texture12releaseImageEv',
    )
