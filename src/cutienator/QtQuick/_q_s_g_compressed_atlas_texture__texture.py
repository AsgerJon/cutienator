"""
QSGCompressedAtlasTexture::Texture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcompressedatlastexture_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGCompressedAtlasTexture::Texture to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGRhiAtlasTexture, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QRectF, QSize
  from ..QtGui import QRhiResourceUpdateBatch
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
  The cute side of Qt's QSGCompressedAtlasTexture::Texture: a plain Python
  object standing in front of one C++ QSGCompressedAtlasTexture::Texture.

  It is built on the cute 'QSGRhiAtlasTexture::TextureBase', as Qt's
  QSGCompressedAtlasTexture::Texture is built on Qt's
  QSGRhiAtlasTexture::TextureBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGCompressedAtlasTexture::Texture that has a ritual
  and that Python can call so far, 8 names in all: 'metaObject',
  'textureSize', 'hasAlphaChannel', 'hasMipmaps', 'normalizedTextureSubRect',
  'removedFromAtlas', 'data', 'sizeInBytes'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGCompressedAtlasTexture::Texture::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QSGCompressedAtlasTexture::Texture::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGCompressedAtlasTexture::Texture::~Texture()': the destructor:
    Python never removes a C++ QSGCompressedAtlasTexture::Texture.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 leans on
  'QSGCompressedAtlasTexture.

  What to expect
  --------------

  - The C++ QSGCompressedAtlasTexture::Texture is created at the first use,
    not by 'QSGCompressedAtlasTexture::Texture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGCompressedAtlasTexture::Texture.
  - Qt tells when it has removed the C++ QSGCompressedAtlasTexture::Texture.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGCompressedAtlasTexture::Texture that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QSGCompressedAtlasTexture::Texture'

  #  A C++ QSGCompressedAtlasTexture::Texture Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGCompressedAtlasTexture_Texture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QSGCompressedAtlasTexture::Texture::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-texture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGCompressedAtlasTexture::Texture::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QSGCompressedAtlasTexture7Texture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGCompressedAtlasTexture::Texture::textureSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-texture.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGCompressedAtlasTexture::Texture::textureSize() const
    ritual = 'ritual_ZNK25QSGCompressedAtlasTexture7Texture11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QSGCompressedAtlasTexture7Texture11textureSizeEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QSGCompressedAtlasTexture::Texture::hasAlphaChannel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-texture.html
    """
    #  bool QSGCompressedAtlasTexture::Texture::hasAlphaChannel() const
    ritual = (
        'ritual_ZNK25QSGCompressedAtlasTexture7Texture15hasAlphaChannelEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QSGCompressedAtlasTexture7Texture15hasAlphaChann'
          'elEv')
    return self.uglySide.call(ritual)

  def hasMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QSGCompressedAtlasTexture::Texture::hasMipmaps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-texture.html#hasMipmaps
    """
    #  bool QSGCompressedAtlasTexture::Texture::hasMipmaps() const
    ritual = 'ritual_ZNK25QSGCompressedAtlasTexture7Texture10hasMipmapsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QSGCompressedAtlasTexture7Texture10hasMipmapsEv')
    return self.uglySide.call(ritual)

  def normalizedTextureSubRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF
    QSGCompressedAtlasTexture::Texture::normalizedTextureSubRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-texture.html

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGCompressedAtlasTexture::Texture::normalizedTextureSubRect()
    #      const
    ritual = (
        'ritual_ZNK25QSGCompressedAtlasTexture7Texture24normalizedTextureSu'
        'bRectEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QSGCompressedAtlasTexture7Texture24normalizedTex'
          'tureSubRectEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def removedFromAtlas(
      self,
      a0: Optional[QRhiResourceUpdateBatch],
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QSGCompressedAtlasTexture::Texture::removedFromAtlas(
    QRhiResourceUpdateBatch *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-texture.html

    Parameters
    ----------

    a0 : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGCompressedAtlasTexture::Texture::removedFromAtlas(
    #      QRhiResourceUpdateBatch *a0) const
    ritual = (
        'ritual_ZNK25QSGCompressedAtlasTexture7Texture16removedFromAtlasEP2'
        '3QRhiResourceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QSGCompressedAtlasTexture7Texture16removedFromAt'
          'lasEP23QRhiResourceUpdateBatch')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    return QSGTexture._cuteAt(address)

  def data(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QSGCompressedAtlasTexture::Texture::data()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-texture.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QSGCompressedAtlasTexture::Texture::data() const
    address = self.uglySide.call(
        'ritual_ZNK25QSGCompressedAtlasTexture7Texture4dataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def sizeInBytes(self) -> int:
    """
    Calls Qt's 'int QSGCompressedAtlasTexture::Texture::sizeInBytes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-texture.html#sizeInBytes
    """
    #  int QSGCompressedAtlasTexture::Texture::sizeInBytes() const
    return self.uglySide.call(
        'ritual_ZNK25QSGCompressedAtlasTexture7Texture11sizeInBytesEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSGCompressedAtlasTexture::Texture::Texture(Atlas *atlas, const
    QRect &textureRect, QByteArrayView data, const QSize &size)': leans on
    'QSGCompressedAtlasTexture::Texture::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGCompressedAtlasTexture.Texture.__init__' has no cute function "
        "yet. Qt's 'QSGCompressedAtlasTexture::Texture::Texture(Atlas "
        "*atlas, const QRect &textureRect, QByteArrayView data, const QSize "
        "&size)': leans on "
        "'QSGCompressedAtlasTexture::Texture::qt_metacall(QMetaObject::Call,"
        " int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
