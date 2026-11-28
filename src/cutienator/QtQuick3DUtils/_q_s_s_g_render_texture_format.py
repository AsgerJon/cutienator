"""
QSSGRenderTextureFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderTextureFormat to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QSSGRenderTextureFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderTextureFormat: a plain Python object
  standing in front of one C++ QSSGRenderTextureFormat.

  C++ hands a QSSGRenderTextureFormat around as a copy, so every C++
  QSSGRenderTextureFormat behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderTextureFormat that has a ritual and that
  Python can call so far, 8 names in all: 'isCompressedTextureFormat',
  'isUncompressedTextureFormat', 'isDepthTextureFormat', 'toString',
  'getSizeofFormat', 'getNumberOfComponent', '__eq__', '__ne__'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGRenderTextureFormat::decodeToFloat(void *inPtr, qint32
    byteOfs, float *outPtr) const': names 'void', which has no cute class
    yet.
  - Qt's 'void QSSGRenderTextureFormat::encodeToPixel(float *inPtr, void
    *outPtr, qint32 byteOfs) const': takes a number to change where it is.
  - Qt's 'QSSGRenderTextureFormat::~QSSGRenderTextureFormat()': the
    destructor: Python removes its C++ QSSGRenderTextureFormat by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderTextureFormat is created at the first use, not by
    'QSSGRenderTextureFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderTextureFormat back gives a copy the ritual
    made for Python, in a new cute QSSGRenderTextureFormat.
  - Each name of Qt's QSSGRenderTextureFormat that has no cute function yet,
    'decodeToFloat', 'encodeToPixel', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderTextureFormat, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Format(CuteNum):
    """
    The enum 'QSSGRenderTextureFormat::Format' of Qt, with the 93 names Qt
    gives in it.
    """

    Unknown = Kee[int](0)
    R8 = Kee[int](1)
    R16 = Kee[int](2)
    R16F = Kee[int](3)
    R32I = Kee[int](4)
    R32UI = Kee[int](5)
    R32F = Kee[int](6)
    RG8 = Kee[int](7)
    RGBA8 = Kee[int](8)
    RGB8 = Kee[int](9)
    SRGB8 = Kee[int](10)
    SRGB8A8 = Kee[int](11)
    RGB565 = Kee[int](12)
    RGBA5551 = Kee[int](13)
    Alpha8 = Kee[int](14)
    Luminance8 = Kee[int](15)
    Luminance16 = Kee[int](16)
    LuminanceAlpha8 = Kee[int](17)
    RGBA16F = Kee[int](18)
    RG16F = Kee[int](19)
    RG32F = Kee[int](20)
    RGB32F = Kee[int](21)
    RGBA32F = Kee[int](22)
    R11G11B10 = Kee[int](23)
    RGB9E5 = Kee[int](24)
    RGB10_A2 = Kee[int](25)
    RGB16F = Kee[int](26)
    RGBA32UI = Kee[int](27)
    RGB32UI = Kee[int](28)
    RGBA16UI = Kee[int](29)
    RGB16UI = Kee[int](30)
    RGBA8UI = Kee[int](31)
    RGB8UI = Kee[int](32)
    RGBA32I = Kee[int](33)
    RGB32I = Kee[int](34)
    RGBA16I = Kee[int](35)
    RGB16I = Kee[int](36)
    RGBA8I = Kee[int](37)
    RGB8I = Kee[int](38)
    RGBE8 = Kee[int](39)
    Depth16 = Kee[int](65)
    Depth24 = Kee[int](66)
    Depth32 = Kee[int](67)
    Depth24Stencil8 = Kee[int](68)
    RGBA_DXT1 = Kee[int](129)
    RGB_DXT1 = Kee[int](130)
    RGBA_DXT3 = Kee[int](131)
    RGBA_DXT5 = Kee[int](132)
    R11_EAC_UNorm = Kee[int](133)
    R11_EAC_SNorm = Kee[int](134)
    RG11_EAC_UNorm = Kee[int](135)
    RG11_EAC_SNorm = Kee[int](136)
    RGB8_ETC2 = Kee[int](137)
    SRGB8_ETC2 = Kee[int](138)
    RGB8_PunchThrough_Alpha1_ETC2 = Kee[int](139)
    SRGB8_PunchThrough_Alpha1_ETC2 = Kee[int](140)
    RGBA8_ETC2_EAC = Kee[int](141)
    SRGB8_Alpha8_ETC2_EAC = Kee[int](142)
    RGBA_ASTC_4x4 = Kee[int](143)
    RGBA_ASTC_5x4 = Kee[int](144)
    RGBA_ASTC_5x5 = Kee[int](145)
    RGBA_ASTC_6x5 = Kee[int](146)
    RGBA_ASTC_6x6 = Kee[int](147)
    RGBA_ASTC_8x5 = Kee[int](148)
    RGBA_ASTC_8x6 = Kee[int](149)
    RGBA_ASTC_8x8 = Kee[int](150)
    RGBA_ASTC_10x5 = Kee[int](151)
    RGBA_ASTC_10x6 = Kee[int](152)
    RGBA_ASTC_10x8 = Kee[int](153)
    RGBA_ASTC_10x10 = Kee[int](154)
    RGBA_ASTC_12x10 = Kee[int](155)
    RGBA_ASTC_12x12 = Kee[int](156)
    SRGB8_Alpha8_ASTC_4x4 = Kee[int](157)
    SRGB8_Alpha8_ASTC_5x4 = Kee[int](158)
    SRGB8_Alpha8_ASTC_5x5 = Kee[int](159)
    SRGB8_Alpha8_ASTC_6x5 = Kee[int](160)
    SRGB8_Alpha8_ASTC_6x6 = Kee[int](161)
    SRGB8_Alpha8_ASTC_8x5 = Kee[int](162)
    SRGB8_Alpha8_ASTC_8x6 = Kee[int](163)
    SRGB8_Alpha8_ASTC_8x8 = Kee[int](164)
    SRGB8_Alpha8_ASTC_10x5 = Kee[int](165)
    SRGB8_Alpha8_ASTC_10x6 = Kee[int](166)
    SRGB8_Alpha8_ASTC_10x8 = Kee[int](167)
    SRGB8_Alpha8_ASTC_10x10 = Kee[int](168)
    SRGB8_Alpha8_ASTC_12x10 = Kee[int](169)
    SRGB8_Alpha8_ASTC_12x12 = Kee[int](170)
    BC1 = Kee[int](171)
    BC2 = Kee[int](172)
    BC3 = Kee[int](173)
    BC4 = Kee[int](174)
    BC5 = Kee[int](175)
    BC6H = Kee[int](176)
    BC7 = Kee[int](177)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderTextureFormat'

  #  Qt's '~QSSGRenderTextureFormat()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRenderTextureFormat behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QSSGRenderTextureFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isCompressedTextureFormat(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderTextureFormat::isCompressedTextureFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureformat.html
    """
    #  bool QSSGRenderTextureFormat::isCompressedTextureFormat() const
    return self.uglySide.call(
        'ritual_ZNK23QSSGRenderTextureFormat25isCompressedTextureFormatEv',
    )

  def isUncompressedTextureFormat(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderTextureFormat::isUncompressedTextureFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureformat.html
    """
    #  bool QSSGRenderTextureFormat::isUncompressedTextureFormat() const
    return self.uglySide.call(
        'ritual_ZNK23QSSGRenderTextureFormat27isUncompressedTextureFormatEv',
    )

  def isDepthTextureFormat(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderTextureFormat::isDepthTextureFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureformat.html#isDepthTextureFormat
    """
    #  bool QSSGRenderTextureFormat::isDepthTextureFormat() const
    return self.uglySide.call(
        'ritual_ZNK23QSSGRenderTextureFormat20isDepthTextureFormatEv',
    )

  def toString(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGRenderTextureFormat::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureformat.html#toString

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGRenderTextureFormat::toString() const
    chars = self.uglySide.call(
        'ritual_ZNK23QSSGRenderTextureFormat8toStringEv',
    )
    return None if chars is None else chars.decode()

  def getSizeofFormat(self) -> int:
    """
    Calls Qt's 'qint32 QSSGRenderTextureFormat::getSizeofFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureformat.html#getSizeofFormat
    """
    #  qint32 QSSGRenderTextureFormat::getSizeofFormat() const
    return self.uglySide.call(
        'ritual_ZNK23QSSGRenderTextureFormat15getSizeofFormatEv',
    )

  def getNumberOfComponent(self) -> int:
    """
    Calls Qt's 'qint32 QSSGRenderTextureFormat::getNumberOfComponent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureformat.html#getNumberOfComponent
    """
    #  qint32 QSSGRenderTextureFormat::getNumberOfComponent() const
    return self.uglySide.call(
        'ritual_ZNK23QSSGRenderTextureFormat20getNumberOfComponentEv',
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

  @overload(THIS)
  def __eq__(self, other: QSSGRenderTextureFormat) -> bool:
    """
    Calls Qt's 'bool QSSGRenderTextureFormat::operator==(const
    QSSGRenderTextureFormat &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureformat.html#operator==

    Parameters
    ----------

    other : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.
    """
    #  bool QSSGRenderTextureFormat::operator==(const QSSGRenderTextureFormat
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK23QSSGRenderTextureFormateqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QSSGRenderTextureFormat) -> bool:
    """
    Calls Qt's 'bool QSSGRenderTextureFormat::operator!=(const
    QSSGRenderTextureFormat &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureformat.html#operator!=

    Parameters
    ----------

    other : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.
    """
    #  bool QSSGRenderTextureFormat::operator!=(const QSSGRenderTextureFormat
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK23QSSGRenderTextureFormatneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Format)
  def __init__(self, f: Format) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderTextureFormat::QSSGRenderTextureFormat(Format f)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertextureformat.html

    Parameters
    ----------

    f : Format
      Passed on as its number.
    """
    #  QSSGRenderTextureFormat::QSSGRenderTextureFormat(Format f)
    self._noteCreation(QSSGRenderTextureFormat, lambda: Rituals.call(
        'ritual_ZN23QSSGRenderTextureFormatC1ENS_6FormatE', f.value,
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

  @staticmethod
  def decodeToFloat(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderTextureFormat::decodeToFloat(void *inPtr, qint32
    byteOfs, float *outPtr) const': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QSSGRenderTextureFormat.decodeToFloat' has no cute function yet. "
        "Qt's 'void QSSGRenderTextureFormat::decodeToFloat(void *inPtr, "
        "qint32 byteOfs, float *outPtr) const': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def encodeToPixel(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderTextureFormat::encodeToPixel(float *inPtr, void
    *outPtr, qint32 byteOfs) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QSSGRenderTextureFormat.encodeToPixel' has no cute function yet. "
        "Qt's 'void QSSGRenderTextureFormat::encodeToPixel(float *inPtr, "
        "void *outPtr, qint32 byteOfs) const': takes a number to change "
        "where it is.")
