"""
Qt3DExtras::QTextureAtlas binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DExtras::QTextureAtlas to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtOpenGL import QOpenGLTexture
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect, QRectF


class QTextureAtlas(Qt3DRender.QAbstractTexture):
  """
  The cute side of Qt's Qt3DExtras::QTextureAtlas: a plain Python object
  standing in front of one C++ Qt3DExtras::QTextureAtlas.

  It is built on the cute 'Qt3DRender::QAbstractTexture', as Qt's
  Qt3DExtras::QTextureAtlas is built on Qt's Qt3DRender::QAbstractTexture,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QTextureAtlas that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'pixelFormat',
  'setPixelFormat', 'removeImage', 'imageCount', 'hasImage', 'imagePosition',
  'imageTexCoords', 'imagePadding', 'd_func'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QTextureAtlas::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QTextureAtlas::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QTextureAtlas::~QTextureAtlas()': the destructor:
    Python never removes a C++ Qt3DExtras::QTextureAtlas.
  - Qt's 'const QTextureAtlasPrivate *Qt3DExtras::QTextureAtlas::d_func()
    const': takes in Python what 'QTextureAtlasPrivate
    *Qt3DExtras::QTextureAtlas::d_func()' takes.

  What has no ritual
  ------------------

  5 of the 19 functions Qt declares: 3 leans on 'Qt3DExtras; 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QTextureAtlas is created at the first use, not by
    'Qt3DExtras::QTextureAtlas(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QTextureAtlas.
  - Qt tells when it has removed the C++ Qt3DExtras::QTextureAtlas. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DExtras::QTextureAtlas that has no cute function
    yet, '__init__', 'addImage', holds a function that raises
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
  __qt_class__ = 'Qt3DExtras::QTextureAtlas'

  #  A C++ Qt3DExtras::QTextureAtlas Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QTextureAtlas'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QTextureAtlas::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QTextureAtlas::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QTextureAtlas10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pixelFormat(self) -> QOpenGLTexture.PixelFormat:
    """
    Calls Qt's 'QOpenGLTexture::PixelFormat
    Qt3DExtras::QTextureAtlas::pixelFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#pixelFormat

    Returns
    -------

    QOpenGLTexture.PixelFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLTexture.PixelFormat(number)' gives.
    """
    #  QOpenGLTexture::PixelFormat Qt3DExtras::QTextureAtlas::pixelFormat()
    #      const
    return QOpenGLTexture.PixelFormat(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QTextureAtlas11pixelFormatEv',
    ))

  def imageCount(self) -> int:
    """
    Calls Qt's 'qsizetype Qt3DExtras::QTextureAtlas::imageCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#imageCount
    """
    #  qsizetype Qt3DExtras::QTextureAtlas::imageCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QTextureAtlas10imageCountEv',
    )

  @overload(int)
  def hasImage(self, id: int) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QTextureAtlas::hasImage(TextureId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#hasImage

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  bool Qt3DExtras::QTextureAtlas::hasImage(TextureId id) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QTextureAtlas8hasImageEi', id,
    )

  @overload(int)
  def imagePosition(self, id: int) -> QRect:
    """
    Calls Qt's 'QRect Qt3DExtras::QTextureAtlas::imagePosition(TextureId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#imagePosition

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Qt3DExtras::QTextureAtlas::imagePosition(TextureId id) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QTextureAtlas13imagePositionEi', id,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int)
  def imageTexCoords(self, id: int) -> QRectF:
    """
    Calls Qt's 'QRectF Qt3DExtras::QTextureAtlas::imageTexCoords(TextureId
    id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#imageTexCoords

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF Qt3DExtras::QTextureAtlas::imageTexCoords(TextureId id) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QTextureAtlas14imageTexCoordsEi', id,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(int)
  def imagePadding(self, id: int) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QTextureAtlas::imagePadding(TextureId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#imagePadding

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  int Qt3DExtras::QTextureAtlas::imagePadding(TextureId id) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QTextureAtlas12imagePaddingEi', id,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpenGLTexture.PixelFormat)
  def setPixelFormat(self, fmt: QOpenGLTexture.PixelFormat) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QTextureAtlas::setPixelFormat(QOpenGLTexture::PixelFormat
    fmt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#setPixelFormat

    Parameters
    ----------

    fmt : QOpenGLTexture.PixelFormat
      Passed on as its number.
    """
    #  void Qt3DExtras::QTextureAtlas::setPixelFormat(QOpenGLTexture::
    #      PixelFormat fmt)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QTextureAtlas14setPixelFormatEN14QOpenGLTex'
        'ture11PixelFormatE',
        fmt.value,
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
    Qt's 'Qt3DExtras::QTextureAtlas::QTextureAtlas(Qt3DCore::QNode *parent)':
    leans on 'Qt3DExtras::QTextureAtlas::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QTextureAtlas.__init__' has no cute function yet. Qt's "
        "'Qt3DExtras::QTextureAtlas::QTextureAtlas(Qt3DCore::QNode "
        "*parent)': leans on "
        "'Qt3DExtras::QTextureAtlas::qt_metacall(QMetaObject::Call, int, "
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

  @overload(int)
  def removeImage(self, id: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTextureAtlas::removeImage(TextureId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#removeImage

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QTextureAtlas::removeImage(TextureId id)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QTextureAtlas11removeImageEi', id,
    )

  def d_func(self) -> Optional[Qt3DExtras.QTextureAtlasPrivate]:
    """
    Calls Qt's 'QTextureAtlasPrivate *Qt3DExtras::QTextureAtlas::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtextureatlas.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QTextureAtlasPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureAtlasPrivate *Qt3DExtras::QTextureAtlas::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QTextureAtlas6d_funcEv',
    )
    return Qt3DExtras.QTextureAtlasPrivate._cuteAt(address)

  @staticmethod
  def addImage(*__, **_) -> Never:
    """
    Qt's 'TextureId Qt3DExtras::QTextureAtlas::addImage(const QImage &image,
    int padding)': leans on
    'Qt3DExtras::QTextureAtlasGenerator::operator()()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QTextureAtlas.addImage' has no cute function yet. Qt's "
        "'TextureId Qt3DExtras::QTextureAtlas::addImage(const QImage "
        "&image, int padding)': leans on "
        "'Qt3DExtras::QTextureAtlasGenerator::operator()()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
