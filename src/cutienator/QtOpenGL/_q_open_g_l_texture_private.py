"""
QOpenGLTexturePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QOpenGLTexturePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QOpenGLTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLTexturePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLTexturePrivate: a plain Python object standing
  in front of one C++ QOpenGLTexturePrivate.

  C++ hands a QOpenGLTexturePrivate around as a copy, so every C++
  QOpenGLTexturePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLTexturePrivate that has a ritual and that
  Python can call so far, 15 names in all: 'q_func', 'destroy', 'bind',
  'release', 'isBound', 'allocateStorage', 'allocateMutableStorage',
  'allocateImmutableStorage', 'setWrapMode', 'wrapMode', 'createTextureView',
  'evaluateMipLevels', 'maximumMipLevelCount', 'mipLevelSize',
  'isUsingImmutableStorage'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLTexturePrivate::~QOpenGLTexturePrivate()': the destructor:
    Python removes its C++ QOpenGLTexturePrivate by it, and has no other use
    for it.
  - Qt's 'const QOpenGLTexture *QOpenGLTexturePrivate::q_func() const': takes
    in Python what 'QOpenGLTexture *QOpenGLTexturePrivate::q_func()' takes.
  - Qt's 'void QOpenGLTexturePrivate::setData(int mipLevel, int layer, int
    layerCount, QOpenGLTexture::CubeMapFace cubeFace,
    QOpenGLTexture::PixelFormat sourceFormat, QOpenGLTexture::PixelType
    sourceType, const void *data, const QOpenGLPixelTransferOptions *const
    options)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLTexturePrivate::setData(int xOffset, int yOffset, int
    zOffset, int width, int height, int depth, int mipLevel, int layer, int
    layerCount, QOpenGLTexture::CubeMapFace cubeFace,
    QOpenGLTexture::PixelFormat sourceFormat, QOpenGLTexture::PixelType
    sourceType, const void *data, const QOpenGLPixelTransferOptions *const
    options)': names 'void', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 28 functions Qt declares: 2 leans on 'QOpenGLTextureHelper; 1
  cannot be called and cannot be called through the meta-object and cannot be
  copied; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file.

  What to expect
  --------------

  - The C++ QOpenGLTexturePrivate is created at the first use, not by
    'QOpenGLTexturePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLTexturePrivate back gives a copy the ritual
    made for Python, in a new cute QOpenGLTexturePrivate.
  - Each name of Qt's QOpenGLTexturePrivate that has no cute function yet,
    'create', 'initializeOpenGLFunctions', 'resetFuncs', 'setCompressedData',
    'setData', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, int)
  def mipLevelSize(mipLevel: int, baseLevelSize: int) -> int:
    """
    Calls Qt's 'int QOpenGLTexturePrivate::mipLevelSize(int mipLevel, int
    baseLevelSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#mipLevelSize

    Parameters
    ----------

    mipLevel : int
      Passed on as it is.

    baseLevelSize : int
      Passed on as it is.
    """
    #  int QOpenGLTexturePrivate::mipLevelSize(int mipLevel, int
    #      baseLevelSize)
    return Rituals.call(
        'ritual_ZN21QOpenGLTexturePrivate12mipLevelSizeEii',
        mipLevel, baseLevelSize,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLTexturePrivate'

  #  Qt's '~QOpenGLTexturePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLTexturePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QOpenGLTexturePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def isBound(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexturePrivate::isBound() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureprivate.html#isBound
    """
    #  bool QOpenGLTexturePrivate::isBound() const
    return self.uglySide.call('ritual_ZNK21QOpenGLTexturePrivate7isBoundEv')

  @overload(int)
  def isBound(self, unit: int) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexturePrivate::isBound(uint unit) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureprivate.html#isBound

    Parameters
    ----------

    unit : int
      Passed on as it is.
    """
    #  bool QOpenGLTexturePrivate::isBound(uint unit) const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGLTexturePrivate7isBoundEj', unit,
    )

  @overload(QOpenGLTexture.CoordinateDirection)
  def wrapMode(
      self,
      direction: QOpenGLTexture.CoordinateDirection,
  ) -> QOpenGLTexture.WrapMode:
    """
    Calls Qt's 'QOpenGLTexture::WrapMode
    QOpenGLTexturePrivate::wrapMode(QOpenGLTexture::CoordinateDirection
    direction) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#wrapMode

    Parameters
    ----------

    direction : QOpenGLTexture.CoordinateDirection
      Passed on as its number.

    Returns
    -------

    QOpenGLTexture.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLTexture.WrapMode(number)' gives.
    """
    #  QOpenGLTexture::WrapMode
    #      QOpenGLTexturePrivate::wrapMode(QOpenGLTexture::
    #      CoordinateDirection direction) const
    return QOpenGLTexture.WrapMode(self.uglySide.call(
        'ritual_ZNK21QOpenGLTexturePrivate8wrapModeEN14QOpenGLTexture19Coor'
        'dinateDirectionE',
        direction.value,
    ))

  @overload(
      QOpenGLTexture.Target, QOpenGLTexture.TextureFormat, int, int, int,
      int,
  )
  def createTextureView(
      self,
      target: QOpenGLTexture.Target,
      viewFormat: QOpenGLTexture.TextureFormat,
      minimumMipmapLevel: int,
      maximumMipmapLevel: int,
      minimumLayer: int,
      maximumLayer: int,
  ) -> Optional[QOpenGLTexture]:
    """
    Calls Qt's 'QOpenGLTexture
    *QOpenGLTexturePrivate::createTextureView(QOpenGLTexture::Target target,
    QOpenGLTexture::TextureFormat viewFormat, int minimumMipmapLevel, int
    maximumMipmapLevel, int minimumLayer, int maximumLayer) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#createTextureView

    Parameters
    ----------

    target : QOpenGLTexture.Target
      Passed on as its number.

    viewFormat : QOpenGLTexture.TextureFormat
      Passed on as its number.

    minimumMipmapLevel : int
      Passed on as it is.

    maximumMipmapLevel : int
      Passed on as it is.

    minimumLayer : int
      Passed on as it is.

    maximumLayer : int
      Passed on as it is.

    Returns
    -------

    Optional[QOpenGLTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLTexture
    #      *QOpenGLTexturePrivate::createTextureView(QOpenGLTexture::Target
    #      target, QOpenGLTexture::TextureFormat viewFormat, int
    #      minimumMipmapLevel, int maximumMipmapLevel, int minimumLayer, int
    #      maximumLayer) const
    address = self.uglySide.call(
        'ritual_ZNK21QOpenGLTexturePrivate17createTextureViewEN14QOpenGLTex'
        'ture6TargetENS0_13TextureFormatEiiii',
        target.value, viewFormat.value, minimumMipmapLevel,
        maximumMipmapLevel, minimumLayer, maximumLayer,
    )
    return QOpenGLTexture._cuteAt(address)

  def evaluateMipLevels(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexturePrivate::evaluateMipLevels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#evaluateMipLevels
    """
    #  int QOpenGLTexturePrivate::evaluateMipLevels() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGLTexturePrivate17evaluateMipLevelsEv',
    )

  def maximumMipLevelCount(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexturePrivate::maximumMipLevelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#maximumMipLevelCount
    """
    #  int QOpenGLTexturePrivate::maximumMipLevelCount() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGLTexturePrivate20maximumMipLevelCountEv',
    )

  def isUsingImmutableStorage(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexturePrivate::isUsingImmutableStorage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#isUsingImmutableStorage
    """
    #  bool QOpenGLTexturePrivate::isUsingImmutableStorage() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGLTexturePrivate23isUsingImmutableStorageEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpenGLTexture.WrapMode)
  def setWrapMode(self, mode: QOpenGLTexture.WrapMode) -> None:
    """
    Calls Qt's 'void
    QOpenGLTexturePrivate::setWrapMode(QOpenGLTexture::WrapMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#setWrapMode

    Parameters
    ----------

    mode : QOpenGLTexture.WrapMode
      Passed on as its number.
    """
    #  void QOpenGLTexturePrivate::setWrapMode(QOpenGLTexture::WrapMode mode)
    self.uglySide.call(
        'ritual_ZN21QOpenGLTexturePrivate11setWrapModeEN14QOpenGLTexture8Wr'
        'apModeE',
        mode.value,
    )

  @overload(QOpenGLTexture.CoordinateDirection, QOpenGLTexture.WrapMode)
  def setWrapMode(
      self,
      direction: QOpenGLTexture.CoordinateDirection,
      mode: QOpenGLTexture.WrapMode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLTexturePrivate::setWrapMode(QOpenGLTexture::CoordinateDirection
    direction, QOpenGLTexture::WrapMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#setWrapMode

    Parameters
    ----------

    direction : QOpenGLTexture.CoordinateDirection
      Passed on as its number.

    mode : QOpenGLTexture.WrapMode
      Passed on as its number.
    """
    #  void QOpenGLTexturePrivate::setWrapMode(QOpenGLTexture::
    #      CoordinateDirection direction, QOpenGLTexture::WrapMode mode)
    self.uglySide.call(
        'ritual_ZN21QOpenGLTexturePrivate11setWrapModeEN14QOpenGLTexture19C'
        'oordinateDirectionENS0_8WrapModeE',
        direction.value, mode.value,
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

  @overload(QOpenGLTexture.Target, QOpenGLTexture)
  @overload(QOpenGLTexture.Target, NoneType)
  def __init__(
      self,
      textureTarget: QOpenGLTexture.Target,
      qq: Optional[QOpenGLTexture],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLTexturePrivate::QOpenGLTexturePrivate(QOpenGLTexture::Target
    textureTarget, QOpenGLTexture *qq)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#QOpenGLTexturePrivate

    Parameters
    ----------

    textureTarget : QOpenGLTexture.Target
      Passed on as its number.

    qq : Optional[QOpenGLTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLTexturePrivate::QOpenGLTexturePrivate(QOpenGLTexture::Target
    #      textureTarget, QOpenGLTexture *qq)
    self._noteCreation(QOpenGLTexturePrivate, lambda: Rituals.call(
        'ritual_ZN21QOpenGLTexturePrivateC1EN14QOpenGLTexture6TargetEPS0_',
        textureTarget.value, self._addressOf(qq),
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

  def q_func(self) -> Optional[QOpenGLTexture]:
    """
    Calls Qt's 'QOpenGLTexture *QOpenGLTexturePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureprivate.html#q_func

    Returns
    -------

    Optional[QOpenGLTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLTexture *QOpenGLTexturePrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QOpenGLTexturePrivate6q_funcEv')
    return QOpenGLTexture._cuteAt(address)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QOpenGLTexturePrivate::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureprivate.html#destroy
    """
    #  void QOpenGLTexturePrivate::destroy()
    self.uglySide.call('ritual_ZN21QOpenGLTexturePrivate7destroyEv')

  @overload()
  def bind(self) -> None:
    """
    Calls Qt's 'void QOpenGLTexturePrivate::bind()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureprivate.html#bind
    """
    #  void QOpenGLTexturePrivate::bind()
    self.uglySide.call('ritual_ZN21QOpenGLTexturePrivate4bindEv')

  @overload(int)
  @overload(int, QOpenGLTexture.TextureUnitReset)
  def bind(
      self,
      unit: int,
      reset: QOpenGLTexture.TextureUnitReset = (
          QOpenGLTexture.TextureUnitReset.DontResetTextureUnit),
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexturePrivate::bind(uint unit,
    QOpenGLTexture::TextureUnitReset reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureprivate.html#bind

    Parameters
    ----------

    unit : int
      Passed on as it is.

    reset : QOpenGLTexture.TextureUnitReset
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLTexture.TextureUnitReset.DontResetTextureUnit.
    """
    #  void QOpenGLTexturePrivate::bind(uint unit,
    #      QOpenGLTexture::TextureUnitReset reset)
    self.uglySide.call(
        'ritual_ZN21QOpenGLTexturePrivate4bindEjN14QOpenGLTexture16TextureU'
        'nitResetE',
        unit, reset.value,
    )

  @overload()
  def release(self) -> None:
    """
    Calls Qt's 'void QOpenGLTexturePrivate::release()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureprivate.html#release
    """
    #  void QOpenGLTexturePrivate::release()
    self.uglySide.call('ritual_ZN21QOpenGLTexturePrivate7releaseEv')

  @overload(int)
  @overload(int, QOpenGLTexture.TextureUnitReset)
  def release(
      self,
      unit: int,
      reset: QOpenGLTexture.TextureUnitReset = (
          QOpenGLTexture.TextureUnitReset.DontResetTextureUnit),
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexturePrivate::release(uint unit,
    QOpenGLTexture::TextureUnitReset reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureprivate.html#release

    Parameters
    ----------

    unit : int
      Passed on as it is.

    reset : QOpenGLTexture.TextureUnitReset
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLTexture.TextureUnitReset.DontResetTextureUnit.
    """
    #  void QOpenGLTexturePrivate::release(uint unit,
    #      QOpenGLTexture::TextureUnitReset reset)
    self.uglySide.call(
        'ritual_ZN21QOpenGLTexturePrivate7releaseEjN14QOpenGLTexture16Textu'
        'reUnitResetE',
        unit, reset.value,
    )

  @overload(QOpenGLTexture.PixelFormat, QOpenGLTexture.PixelType)
  def allocateStorage(
      self,
      pixelFormat: QOpenGLTexture.PixelFormat,
      pixelType: QOpenGLTexture.PixelType,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLTexturePrivate::allocateStorage(QOpenGLTexture::PixelFormat
    pixelFormat, QOpenGLTexture::PixelType pixelType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#allocateStorage

    Parameters
    ----------

    pixelFormat : QOpenGLTexture.PixelFormat
      Passed on as its number.

    pixelType : QOpenGLTexture.PixelType
      Passed on as its number.
    """
    #  void
    #      QOpenGLTexturePrivate::allocateStorage(QOpenGLTexture::PixelFormat
    #      pixelFormat, QOpenGLTexture::PixelType pixelType)
    self.uglySide.call(
        'ritual_ZN21QOpenGLTexturePrivate15allocateStorageEN14QOpenGLTextur'
        'e11PixelFormatENS0_9PixelTypeE',
        pixelFormat.value, pixelType.value,
    )

  @overload(QOpenGLTexture.PixelFormat, QOpenGLTexture.PixelType)
  def allocateMutableStorage(
      self,
      pixelFormat: QOpenGLTexture.PixelFormat,
      pixelType: QOpenGLTexture.PixelType,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLTexturePrivate::allocateMutableStorage(QOpenGLTexture::PixelFormat
    pixelFormat, QOpenGLTexture::PixelType pixelType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html#allocateMutableStorage

    Parameters
    ----------

    pixelFormat : QOpenGLTexture.PixelFormat
      Passed on as its number.

    pixelType : QOpenGLTexture.PixelType
      Passed on as its number.
    """
    #  void QOpenGLTexturePrivate::allocateMutableStorage(QOpenGLTexture::
    #      PixelFormat pixelFormat, QOpenGLTexture::PixelType pixelType)
    self.uglySide.call(
        'ritual_ZN21QOpenGLTexturePrivate22allocateMutableStorageEN14QOpenG'
        'LTexture11PixelFormatENS0_9PixelTypeE',
        pixelFormat.value, pixelType.value,
    )

  def allocateImmutableStorage(self) -> None:
    """
    Calls Qt's 'void QOpenGLTexturePrivate::allocateImmutableStorage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureprivate.html
    """
    #  void QOpenGLTexturePrivate::allocateImmutableStorage()
    self.uglySide.call(
        'ritual_ZN21QOpenGLTexturePrivate24allocateImmutableStorageEv',
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'bool QOpenGLTexturePrivate::create()': leans on
    'QOpenGLTextureHelper::qt_TextureImage2D(unsigned int, unsigned int,
    unsigned int, int, unsigned int, int, int, int, unsigned int, unsigned
    int, void const*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpenGLTexturePrivate.create' has no cute function yet. Qt's "
        "'bool QOpenGLTexturePrivate::create()': leans on "
        "'QOpenGLTextureHelper::qt_TextureImage2D(unsigned int, unsigned "
        "int, unsigned int, int, unsigned int, int, int, int, unsigned int, "
        "unsigned int, void const*)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def initializeOpenGLFunctions(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTexturePrivate::initializeOpenGLFunctions()': leans on
    'QOpenGLTextureHelper::qt_TextureImage2D(unsigned int, unsigned int,
    unsigned int, int, unsigned int, int, int, int, unsigned int, unsigned
    int, void const*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpenGLTexturePrivate.initializeOpenGLFunctions' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTexturePrivate::initializeOpenGLFunctions()': leans on "
        "'QOpenGLTextureHelper::qt_TextureImage2D(unsigned int, unsigned "
        "int, unsigned int, int, unsigned int, int, int, int, unsigned int, "
        "unsigned int, void const*)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def resetFuncs(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTexturePrivate::resetFuncs(QOpenGLTextureHelper
    *funcs)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QOpenGLTexturePrivate.resetFuncs' has no cute function yet. Qt's "
        "'void QOpenGLTexturePrivate::resetFuncs(QOpenGLTextureHelper "
        "*funcs)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setCompressedData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTexturePrivate::setCompressedData(int mipLevel, int
    layer, int layerCount, QOpenGLTexture::CubeMapFace cubeFace, int
    dataSize, const void *data, const QOpenGLPixelTransferOptions *const
    options)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'isCompressedFormat'.
    """
    raise NotImplementedError(
        "'QOpenGLTexturePrivate.setCompressedData' has no cute function "
        "yet. Qt's 'void QOpenGLTexturePrivate::setCompressedData(int "
        "mipLevel, int layer, int layerCount, QOpenGLTexture::CubeMapFace "
        "cubeFace, int dataSize, const void *data, const "
        "QOpenGLPixelTransferOptions *const options)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'isCompressedFormat'.")

  @staticmethod
  def setData(*__, **_) -> Never:
    """
    - Qt's 'void QOpenGLTexturePrivate::setData(int mipLevel, int layer, int
      layerCount, QOpenGLTexture::CubeMapFace cubeFace,
      QOpenGLTexture::PixelFormat sourceFormat, QOpenGLTexture::PixelType
      sourceType, const void *data, const QOpenGLPixelTransferOptions *const
      options)': names 'void', which has no cute class yet.
    - Qt's 'void QOpenGLTexturePrivate::setData(int xOffset, int yOffset, int
      zOffset, int width, int height, int depth, int mipLevel, int layer, int
      layerCount, QOpenGLTexture::CubeMapFace cubeFace,
      QOpenGLTexture::PixelFormat sourceFormat, QOpenGLTexture::PixelType
      sourceType, const void *data, const QOpenGLPixelTransferOptions *const
      options)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTexturePrivate.setData' has no cute function yet. Qt's "
        "'void QOpenGLTexturePrivate::setData(int mipLevel, int layer, int "
        "layerCount, QOpenGLTexture::CubeMapFace cubeFace, "
        "QOpenGLTexture::PixelFormat sourceFormat, "
        "QOpenGLTexture::PixelType sourceType, const void *data, const "
        "QOpenGLPixelTransferOptions *const options)': names 'void', which "
        "has no cute class yet. Qt's 'void "
        "QOpenGLTexturePrivate::setData(int xOffset, int yOffset, int "
        "zOffset, int width, int height, int depth, int mipLevel, int "
        "layer, int layerCount, QOpenGLTexture::CubeMapFace cubeFace, "
        "QOpenGLTexture::PixelFormat sourceFormat, "
        "QOpenGLTexture::PixelType sourceType, const void *data, const "
        "QOpenGLPixelTransferOptions *const options)': names 'void', which "
        "has no cute class yet.")
