"""
Qt3DRender::QShaderImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qshaderimage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShaderImage(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QShaderImage: a plain Python object
  standing in front of one C++ Qt3DRender::QShaderImage.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DRender::QShaderImage
  is built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QShaderImage that has a ritual and that
  Python can call so far, 21 names in all: 'metaObject', 'tr', 'texture',
  'layered', 'mipLevel', 'layer', 'access', 'format', 'setTexture',
  'setLayered', 'setMipLevel', 'setLayer', 'setAccess', 'setFormat',
  'textureChanged', 'layeredChanged', 'mipLevelChanged', 'layerChanged',
  'accessChanged', 'formatChanged', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QShaderImage::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QShaderImage::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QShaderImage::~QShaderImage()': the destructor: Python
    never removes a C++ Qt3DRender::QShaderImage.
  - Qt's 'const QShaderImagePrivate *Qt3DRender::QShaderImage::d_func()
    const': takes in Python what 'QShaderImagePrivate
    *Qt3DRender::QShaderImage::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QShaderImage is created at the first use, not by
    'Qt3DRender::QShaderImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QShaderImage.
  - Qt tells when it has removed the C++ Qt3DRender::QShaderImage. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QShaderImage, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Access(CuteNum):
    """
    The enum 'Qt3DRender::QShaderImage::Access' of Qt, with the 3 names Qt
    gives in it.
    """

    ReadOnly = Kee[int](0)
    WriteOnly = Kee[int](1)
    ReadWrite = Kee[int](2)

  class ImageFormat(CuteNum):
    """
    The enum 'Qt3DRender::QShaderImage::ImageFormat' of Qt, with the 41 names
    Qt gives in it.
    """

    NoFormat = Kee[int](0)
    Automatic = Kee[int](1)
    R8_UNorm = Kee[int](33321)
    RG8_UNorm = Kee[int](33323)
    RGBA8_UNorm = Kee[int](32856)
    R16_UNorm = Kee[int](33322)
    RG16_UNorm = Kee[int](33324)
    RGBA16_UNorm = Kee[int](32859)
    R8_SNorm = Kee[int](36756)
    RG8_SNorm = Kee[int](36757)
    RGBA8_SNorm = Kee[int](36759)
    R16_SNorm = Kee[int](36760)
    RG16_SNorm = Kee[int](36761)
    RGBA16_SNorm = Kee[int](36763)
    R8U = Kee[int](33330)
    RG8U = Kee[int](33336)
    RGBA8U = Kee[int](36220)
    R16U = Kee[int](33332)
    RG16U = Kee[int](33338)
    RGBA16U = Kee[int](36214)
    R32U = Kee[int](33334)
    RG32U = Kee[int](33340)
    RGBA32U = Kee[int](36208)
    R8I = Kee[int](33329)
    RG8I = Kee[int](33335)
    RGBA8I = Kee[int](36238)
    R16I = Kee[int](33331)
    RG16I = Kee[int](33337)
    RGBA16I = Kee[int](36232)
    R32I = Kee[int](33333)
    RG32I = Kee[int](33339)
    RGBA32I = Kee[int](36226)
    R16F = Kee[int](33325)
    RG16F = Kee[int](33327)
    RGBA16F = Kee[int](34842)
    R32F = Kee[int](33326)
    RG32F = Kee[int](33328)
    RGBA32F = Kee[int](34836)
    RG11B10F = Kee[int](35898)
    RGB10A2 = Kee[int](32857)
    RGB10A2U = Kee[int](36975)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QShaderImage::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QShaderImage::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender12QShaderImage2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QShaderImage'

  #  A C++ Qt3DRender::QShaderImage Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QShaderImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QShaderImage::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QShaderImage::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QShaderImage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def texture(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DRender::QShaderImage::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#texture

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture *Qt3DRender::QShaderImage::texture()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QShaderImage7textureEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def layered(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QShaderImage::layered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#layered
    """
    #  bool Qt3DRender::QShaderImage::layered() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QShaderImage7layeredEv',
    )

  def mipLevel(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QShaderImage::mipLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#mipLevel
    """
    #  int Qt3DRender::QShaderImage::mipLevel() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QShaderImage8mipLevelEv',
    )

  def layer(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QShaderImage::layer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#layer
    """
    #  int Qt3DRender::QShaderImage::layer() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender12QShaderImage5layerEv')

  def access(self) -> Access:
    """
    Calls Qt's 'Access Qt3DRender::QShaderImage::access() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#access

    Returns
    -------

    Access
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Access(number)' gives.
    """
    #  Access Qt3DRender::QShaderImage::access() const
    return QShaderImage.Access(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QShaderImage6accessEv',
    ))

  def format(self) -> ImageFormat:
    """
    Calls Qt's 'ImageFormat Qt3DRender::QShaderImage::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#format

    Returns
    -------

    ImageFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ImageFormat(number)'
      gives.
    """
    #  ImageFormat Qt3DRender::QShaderImage::format() const
    return QShaderImage.ImageFormat(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QShaderImage6formatEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setTexture(
      self,
      texture: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderImage::setTexture(Qt3DRender::QAbstractTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#setTexture

    Parameters
    ----------

    texture : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QShaderImage::setTexture(Qt3DRender::QAbstractTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage10setTextureEPNS_16QAbstractTex'
        'tureE',
        self._addressOf(texture),
    )

  @overload(bool)
  def setLayered(self, layered: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::setLayered(bool layered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#setLayered

    Parameters
    ----------

    layered : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QShaderImage::setLayered(bool layered)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage10setLayeredEb', layered,
    )

  @overload(int)
  def setMipLevel(self, mipLevel: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::setMipLevel(int mipLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#setMipLevel

    Parameters
    ----------

    mipLevel : int
      Passed on as it is.
    """
    #  void Qt3DRender::QShaderImage::setMipLevel(int mipLevel)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage11setMipLevelEi', mipLevel,
    )

  @overload(int)
  def setLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::setLayer(int layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#setLayer

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void Qt3DRender::QShaderImage::setLayer(int layer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage8setLayerEi', layer,
    )

  @overload(Access)
  def setAccess(self, access: Access) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::setAccess(Access access)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#setAccess

    Parameters
    ----------

    access : Access
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderImage::setAccess(Access access)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage9setAccessENS0_6AccessE',
        access.value,
    )

  @overload(ImageFormat)
  def setFormat(self, format: ImageFormat) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::setFormat(ImageFormat
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#setFormat

    Parameters
    ----------

    format : ImageFormat
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderImage::setFormat(ImageFormat format)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage9setFormatENS0_11ImageFormatE',
        format.value,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QShaderImage::QShaderImage(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#QShaderImage

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QShaderImage::QShaderImage(Qt3DCore::QNode *parent)
    self._noteCreation(QShaderImage, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender12QShaderImageC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def textureChanged(
      self,
      texture: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderImage::textureChanged(Qt3DRender::QAbstractTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#textureChanged

    Parameters
    ----------

    texture : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QShaderImage::textureChanged(Qt3DRender::
    #      QAbstractTexture *texture)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage14textureChangedEPNS_16QAbstrac'
        'tTextureE',
        self._addressOf(texture),
    )

  @overload(bool)
  def layeredChanged(self, layered: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::layeredChanged(bool layered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#layeredChanged

    Parameters
    ----------

    layered : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QShaderImage::layeredChanged(bool layered)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage14layeredChangedEb', layered,
    )

  @overload(int)
  def mipLevelChanged(self, mipLevel: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::mipLevelChanged(int
    mipLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#mipLevelChanged

    Parameters
    ----------

    mipLevel : int
      Passed on as it is.
    """
    #  void Qt3DRender::QShaderImage::mipLevelChanged(int mipLevel)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage15mipLevelChangedEi', mipLevel,
    )

  @overload(int)
  def layerChanged(self, layer: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::layerChanged(int layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#layerChanged

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void Qt3DRender::QShaderImage::layerChanged(int layer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage12layerChangedEi', layer,
    )

  @overload(Access)
  def accessChanged(self, access: Access) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::accessChanged(Access access)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#accessChanged

    Parameters
    ----------

    access : Access
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderImage::accessChanged(Access access)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage13accessChangedENS0_6AccessE',
        access.value,
    )

  @overload(ImageFormat)
  def formatChanged(self, format: ImageFormat) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderImage::formatChanged(ImageFormat
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#formatChanged

    Parameters
    ----------

    format : ImageFormat
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderImage::formatChanged(ImageFormat format)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage13formatChangedENS0_11ImageForm'
        'atE',
        format.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QShaderImagePrivate]:
    """
    Calls Qt's 'QShaderImagePrivate *Qt3DRender::QShaderImage::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderimage.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QShaderImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShaderImagePrivate *Qt3DRender::QShaderImage::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderImage6d_funcEv',
    )
    return Qt3DRender.QShaderImagePrivate._cuteAt(address)
