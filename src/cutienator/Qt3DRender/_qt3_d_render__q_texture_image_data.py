"""
Qt3DRender::QTextureImageData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qtextureimagedata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtOpenGL import QOpenGLTexture
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QImage = WAIT['QImage']


class QTextureImageData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QTextureImageData: a plain Python object
  standing in front of one C++ Qt3DRender::QTextureImageData.

  C++ hands a Qt3DRender::QTextureImageData around as a copy, so every C++
  Qt3DRender::QTextureImageData behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QTextureImageData that has a ritual and
  that Python can call so far, 28 names in all: 'cleanup', 'isCompressed',
  'width', 'height', 'depth', 'layers', 'mipLevels', 'faces', 'setWidth',
  'setHeight', 'setDepth', 'setLayers', 'setMipLevels', 'setFaces',
  'alignment', 'setAlignment', 'target', 'format', 'pixelFormat',
  'pixelType', 'setTarget', 'setFormat', 'setPixelFormat', 'setPixelType',
  'setImage', 'setData', 'data', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QTextureImageData::~QTextureImageData()': the
    destructor: Python removes its C++ Qt3DRender::QTextureImageData by it,
    and has no other use for it.
  - Qt's 'QTextureImageData &Qt3DRender::QTextureImageData::operator=(const
    QTextureImageData &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'void Qt3DRender::QTextureImageData::setData(const QByteArray &data,
    std::function<QByteArray (QByteArray, int, int, int)> a1, bool
    isCompressed)': takes a type Python has no way to hand over yet.
  - Qt's 'Qt3DRender::QTextureImageData::QTextureImageData(
    QTextureImageDataPrivate &dd)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QTextureImageDataPrivate
    *Qt3DRender::QTextureImageData::d_func() const': takes in Python what
    'QTextureImageDataPrivate *Qt3DRender::QTextureImageData::d_func()'
    takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QTextureImageData is created at the first use, not by
    'Qt3DRender::QTextureImageData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QTextureImageData back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::QTextureImageData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QTextureImageData'

  #  Qt's '~Qt3DRender::QTextureImageData()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::QTextureImageData behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender17QTextureImageDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isCompressed(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QTextureImageData::isCompressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#isCompressed
    """
    #  bool Qt3DRender::QTextureImageData::isCompressed() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData12isCompressedEv',
    )

  def width(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageData::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#width
    """
    #  int Qt3DRender::QTextureImageData::width() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData5widthEv',
    )

  def height(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageData::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#height
    """
    #  int Qt3DRender::QTextureImageData::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData6heightEv',
    )

  def depth(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageData::depth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#depth
    """
    #  int Qt3DRender::QTextureImageData::depth() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData5depthEv',
    )

  def layers(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageData::layers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#layers
    """
    #  int Qt3DRender::QTextureImageData::layers() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData6layersEv',
    )

  def mipLevels(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageData::mipLevels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#mipLevels
    """
    #  int Qt3DRender::QTextureImageData::mipLevels() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData9mipLevelsEv',
    )

  def faces(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageData::faces() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#faces
    """
    #  int Qt3DRender::QTextureImageData::faces() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData5facesEv',
    )

  def alignment(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageData::alignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#alignment
    """
    #  int Qt3DRender::QTextureImageData::alignment() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData9alignmentEv',
    )

  def target(self) -> QOpenGLTexture.Target:
    """
    Calls Qt's 'QOpenGLTexture::Target
    Qt3DRender::QTextureImageData::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#target

    Returns
    -------

    QOpenGLTexture.Target
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLTexture.Target(number)' gives.
    """
    #  QOpenGLTexture::Target Qt3DRender::QTextureImageData::target() const
    return QOpenGLTexture.Target(self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData6targetEv',
    ))

  def format(self) -> QOpenGLTexture.TextureFormat:
    """
    Calls Qt's 'QOpenGLTexture::TextureFormat
    Qt3DRender::QTextureImageData::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#format

    Returns
    -------

    QOpenGLTexture.TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLTexture.TextureFormat(number)' gives.
    """
    #  QOpenGLTexture::TextureFormat Qt3DRender::QTextureImageData::format()
    #      const
    return QOpenGLTexture.TextureFormat(self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData6formatEv',
    ))

  def pixelFormat(self) -> QOpenGLTexture.PixelFormat:
    """
    Calls Qt's 'QOpenGLTexture::PixelFormat
    Qt3DRender::QTextureImageData::pixelFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#pixelFormat

    Returns
    -------

    QOpenGLTexture.PixelFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLTexture.PixelFormat(number)' gives.
    """
    #  QOpenGLTexture::PixelFormat
    #      Qt3DRender::QTextureImageData::pixelFormat() const
    return QOpenGLTexture.PixelFormat(self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData11pixelFormatEv',
    ))

  def pixelType(self) -> QOpenGLTexture.PixelType:
    """
    Calls Qt's 'QOpenGLTexture::PixelType
    Qt3DRender::QTextureImageData::pixelType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#pixelType

    Returns
    -------

    QOpenGLTexture.PixelType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLTexture.PixelType(number)' gives.
    """
    #  QOpenGLTexture::PixelType Qt3DRender::QTextureImageData::pixelType()
    #      const
    return QOpenGLTexture.PixelType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData9pixelTypeEv',
    ))

  @overload()
  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  def data(
      self,
      layer: int = 0,
      face: int = 0,
      mipmapLevel: int = 0,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::QTextureImageData::data(int layer, int
    face, int mipmapLevel) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#data

    Parameters
    ----------

    layer : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    face : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    mipmapLevel : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QTextureImageData::data(int layer, int face,
    #      int mipmapLevel) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QTextureImageData4dataEiii',
        layer, face, mipmapLevel,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setWidth(self, width: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageData::setWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImageData::setWidth(int width)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData8setWidthEi', width,
    )

  @overload(int)
  def setHeight(self, height: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageData::setHeight(int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setHeight

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImageData::setHeight(int height)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData9setHeightEi', height,
    )

  @overload(int)
  def setDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageData::setDepth(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImageData::setDepth(int depth)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData8setDepthEi', depth,
    )

  @overload(int)
  def setLayers(self, layers: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageData::setLayers(int layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setLayers

    Parameters
    ----------

    layers : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImageData::setLayers(int layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData9setLayersEi', layers,
    )

  @overload(int)
  def setMipLevels(self, mipLevels: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageData::setMipLevels(int
    mipLevels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setMipLevels

    Parameters
    ----------

    mipLevels : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImageData::setMipLevels(int mipLevels)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData12setMipLevelsEi',
        mipLevels,
    )

  @overload(int)
  def setFaces(self, faces: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageData::setFaces(int faces)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setFaces

    Parameters
    ----------

    faces : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImageData::setFaces(int faces)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData8setFacesEi', faces,
    )

  @overload(int)
  def setAlignment(self, alignment: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageData::setAlignment(int
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setAlignment

    Parameters
    ----------

    alignment : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImageData::setAlignment(int alignment)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData12setAlignmentEi',
        alignment,
    )

  @overload(QOpenGLTexture.Target)
  def setTarget(self, target: QOpenGLTexture.Target) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureImageData::setTarget(QOpenGLTexture::Target target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setTarget

    Parameters
    ----------

    target : QOpenGLTexture.Target
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureImageData::setTarget(QOpenGLTexture::Target
    #      target)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData9setTargetEN14QOpenGLTextu'
        're6TargetE',
        target.value,
    )

  @overload(QOpenGLTexture.TextureFormat)
  def setFormat(self, format: QOpenGLTexture.TextureFormat) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureImageData::setFormat(QOpenGLTexture::TextureFormat
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setFormat

    Parameters
    ----------

    format : QOpenGLTexture.TextureFormat
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureImageData::setFormat(QOpenGLTexture::
    #      TextureFormat format)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData9setFormatEN14QOpenGLTextu'
        're13TextureFormatE',
        format.value,
    )

  @overload(QOpenGLTexture.PixelFormat)
  def setPixelFormat(self, pixelFormat: QOpenGLTexture.PixelFormat) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureImageData::setPixelFormat(QOpenGLTexture::PixelFormat
    pixelFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setPixelFormat

    Parameters
    ----------

    pixelFormat : QOpenGLTexture.PixelFormat
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureImageData::setPixelFormat(QOpenGLTexture::
    #      PixelFormat pixelFormat)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData14setPixelFormatEN14QOpenG'
        'LTexture11PixelFormatE',
        pixelFormat.value,
    )

  @overload(QOpenGLTexture.PixelType)
  def setPixelType(self, pixelType: QOpenGLTexture.PixelType) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureImageData::setPixelType(QOpenGLTexture::PixelType
    pixelType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setPixelType

    Parameters
    ----------

    pixelType : QOpenGLTexture.PixelType
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureImageData::setPixelType(QOpenGLTexture::
    #      PixelType pixelType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData12setPixelTypeEN14QOpenGLT'
        'exture9PixelTypeE',
        pixelType.value,
    )

  @overload(QImage)
  def setImage(self, a0: QImage) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageData::setImage(const QImage
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setImage

    Parameters
    ----------

    a0 : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void Qt3DRender::QTextureImageData::setImage(const QImage &a0)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData8setImageERK6QImage',
        self._valueOf(a0),
    )

  @overload(QByteArray, int)
  @overload(QByteArray, int, bool)
  def setData(
      self,
      data: QByteArray,
      blockSize: int,
      isCompressed: bool = False,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageData::setData(const QByteArray
    &data, int blockSize, bool isCompressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    blockSize : int
      Passed on as it is.

    isCompressed : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void Qt3DRender::QTextureImageData::setData(const QByteArray &data,
    #      int blockSize, bool isCompressed)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData7setDataERK10QByteArrayib',
        self._valueOf(data), blockSize, isCompressed,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QTextureImageData::QTextureImageData()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html
    """
    #  Qt3DRender::QTextureImageData::QTextureImageData()
    self._noteCreation(QTextureImageData, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender17QTextureImageDataC1Ev',
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
    Calls Qt's 'void Qt3DRender::QTextureImageData::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#cleanup
    """
    #  void Qt3DRender::QTextureImageData::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender17QTextureImageData7cleanupEv')

  def d_func(self) -> Optional[Qt3DRender.QTextureImageDataPrivate]:
    """
    Calls Qt's 'QTextureImageDataPrivate
    *Qt3DRender::QTextureImageData::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedata.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QTextureImageDataPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureImageDataPrivate *Qt3DRender::QTextureImageData::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender17QTextureImageData6d_funcEv',
    )
    return Qt3DRender.QTextureImageDataPrivate._cuteAt(address)
