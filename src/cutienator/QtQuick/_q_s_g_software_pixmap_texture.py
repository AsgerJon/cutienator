"""
QSGSoftwarePixmapTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepixmaptexture_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwarePixmapTexture to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QPixmap


class QSGSoftwarePixmapTexture(QSGTexture):
  """
  The cute side of Qt's QSGSoftwarePixmapTexture: a plain Python object
  standing in front of one C++ QSGSoftwarePixmapTexture.

  It is built on the cute 'QSGTexture', as Qt's QSGSoftwarePixmapTexture is
  built on Qt's QSGTexture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwarePixmapTexture that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'comparisonKey',
  'textureSize', 'hasAlphaChannel', 'hasMipmaps', 'pixmap'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGSoftwarePixmapTexture::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QSGSoftwarePixmapTexture::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 2 not a gap; 2 leans on 'vtable for
  QSGSoftwarePixmapTexture', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'QSGSoftwarePixmapTexture.

  What to expect
  --------------

  - The C++ QSGSoftwarePixmapTexture is created at the first use, not by
    'QSGSoftwarePixmapTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwarePixmapTexture.
  - Qt tells when it has removed the C++ QSGSoftwarePixmapTexture. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGSoftwarePixmapTexture that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwarePixmapTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGSoftwarePixmapTexture::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaptexture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGSoftwarePixmapTexture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QSGSoftwarePixmapTexture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def comparisonKey(self) -> int:
    """
    Calls Qt's 'qint64 QSGSoftwarePixmapTexture::comparisonKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaptexture.html#comparisonKey
    """
    #  qint64 QSGSoftwarePixmapTexture::comparisonKey() const
    ritual = 'ritual_ZNK24QSGSoftwarePixmapTexture13comparisonKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSGSoftwarePixmapTexture13comparisonKeyEv'
    return self.uglySide.call(ritual)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGSoftwarePixmapTexture::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaptexture.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGSoftwarePixmapTexture::textureSize() const
    ritual = 'ritual_ZNK24QSGSoftwarePixmapTexture11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSGSoftwarePixmapTexture11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwarePixmapTexture::hasAlphaChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaptexture.html#hasAlphaChannel
    """
    #  bool QSGSoftwarePixmapTexture::hasAlphaChannel() const
    ritual = 'ritual_ZNK24QSGSoftwarePixmapTexture15hasAlphaChannelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSGSoftwarePixmapTexture15hasAlphaChannelEv'
    return self.uglySide.call(ritual)

  def hasMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwarePixmapTexture::hasMipmaps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaptexture.html#hasMipmaps
    """
    #  bool QSGSoftwarePixmapTexture::hasMipmaps() const
    ritual = 'ritual_ZNK24QSGSoftwarePixmapTexture10hasMipmapsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSGSoftwarePixmapTexture10hasMipmapsEv'
    return self.uglySide.call(ritual)

  def pixmap(self) -> QPixmap:
    """
    Calls Qt's 'const QPixmap &QSGSoftwarePixmapTexture::pixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepixmaptexture.html#pixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  const QPixmap &QSGSoftwarePixmapTexture::pixmap() const
    address = self.uglySide.call(
        'ritual_ZNK24QSGSoftwarePixmapTexture6pixmapEv',
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

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
    - Qt's 'QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QImage
      &image, uint flags)': leans on 'vtable for QSGSoftwarePixmapTexture',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's 'QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QPixmap
      &pixmap)': leans on 'vtable for QSGSoftwarePixmapTexture', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwarePixmapTexture.__init__' has no cute function yet. Qt's "
        "'QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QImage "
        "&image, uint flags)': leans on 'vtable for "
        "QSGSoftwarePixmapTexture', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken. Qt's "
        "'QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QPixmap "
        "&pixmap)': leans on 'vtable for QSGSoftwarePixmapTexture', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
