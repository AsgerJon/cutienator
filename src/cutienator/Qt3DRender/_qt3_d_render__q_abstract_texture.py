"""
Qt3DRender::QAbstractTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qabstracttexture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractTexture(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QAbstractTexture: a plain Python object
  standing in front of one C++ Qt3DRender::QAbstractTexture.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DRender::QAbstractTexture is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QAbstractTexture that has a ritual and
  that Python can call so far, 57 names in all: 'metaObject', 'tr', 'target',
  'format', 'generateMipMaps', 'status', 'addTextureImage',
  'removeTextureImage', 'wrapMode', 'setSize', 'minificationFilter',
  'magnificationFilter', 'maximumAnisotropy', 'comparisonFunction',
  'comparisonMode', 'width', 'height', 'depth', 'layers', 'samples',
  'mipLevels', 'handleType', 'handle', 'updateData', 'setFormat',
  'setGenerateMipMaps', 'setWidth', 'setHeight', 'setDepth',
  'setMinificationFilter', 'setMagnificationFilter', 'setMaximumAnisotropy',
  'setComparisonFunction', 'setComparisonMode', 'setLayers', 'setSamples',
  'setMipLevels', 'formatChanged', 'statusChanged', 'generateMipMapsChanged',
  'widthChanged', 'heightChanged', 'depthChanged',
  'magnificationFilterChanged', 'minificationFilterChanged',
  'maximumAnisotropyChanged', 'comparisonFunctionChanged',
  'comparisonModeChanged', 'layersChanged', 'samplesChanged',
  'handleTypeChanged', 'handleChanged', 'mipLevelsChanged', 'setStatus',
  'setHandle', 'setHandleType', 'd_func'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QAbstractTexture::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QAbstractTexture::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QAbstractTexture::~QAbstractTexture()': the destructor:
    Python never removes a C++ Qt3DRender::QAbstractTexture.
  - Qt's 'QList<QAbstractTextureImage *>
    Qt3DRender::QAbstractTexture::textureImages() const': gives a type Python
    has no way to take yet.
  - Qt's 'void Qt3DRender::QAbstractTexture::setWrapMode(const
    QTextureWrapMode &wrapMode)': takes a type Python has no way to hand over
    yet.
  - Qt's
    'Qt3DRender::QAbstractTexture::QAbstractTexture(QAbstractTexturePrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QAbstractTexturePrivate
    *Qt3DRender::QAbstractTexture::d_func() const': takes in Python what
    'QAbstractTexturePrivate *Qt3DRender::QAbstractTexture::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 68 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QAbstractTexture is created at the first use, not by
    'Qt3DRender::QAbstractTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QAbstractTexture.
  - Qt tells when it has removed the C++ Qt3DRender::QAbstractTexture. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QAbstractTexture that has no cute function
    yet, 'setWrapMode', 'textureImages', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::QAbstractTexture, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ComparisonFunction(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractTexture::ComparisonFunction' of Qt, with
    the 8 names Qt gives in it.
    """

    CompareLessEqual = Kee[int](515)
    CompareGreaterEqual = Kee[int](518)
    CompareLess = Kee[int](513)
    CompareGreater = Kee[int](516)
    CompareEqual = Kee[int](514)
    CommpareNotEqual = Kee[int](517)
    CompareAlways = Kee[int](519)
    CompareNever = Kee[int](512)

  class ComparisonMode(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractTexture::ComparisonMode' of Qt, with the 2
    names Qt gives in it.
    """

    CompareRefToTexture = Kee[int](34894)
    CompareNone = Kee[int](0)

  class CubeMapFace(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractTexture::CubeMapFace' of Qt, with the 7
    names Qt gives in it.
    """

    CubeMapPositiveX = Kee[int](34069)
    CubeMapNegativeX = Kee[int](34070)
    CubeMapPositiveY = Kee[int](34071)
    CubeMapNegativeY = Kee[int](34072)
    CubeMapPositiveZ = Kee[int](34073)
    CubeMapNegativeZ = Kee[int](34074)
    AllFaces = Kee[int](34075)

  class Filter(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractTexture::Filter' of Qt, with the 6 names
    Qt gives in it.
    """

    Nearest = Kee[int](9728)
    Linear = Kee[int](9729)
    NearestMipMapNearest = Kee[int](9984)
    NearestMipMapLinear = Kee[int](9986)
    LinearMipMapNearest = Kee[int](9985)
    LinearMipMapLinear = Kee[int](9987)

  class HandleType(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractTexture::HandleType' of Qt, with the 3
    names Qt gives in it.
    """

    NoHandle = Kee[int](0)
    OpenGLTextureId = Kee[int](1)
    RHITextureId = Kee[int](2)

  class Status(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractTexture::Status' of Qt, with the 4 names
    Qt gives in it.
    """

    NULL = Kee[int](0)
    Loading = Kee[int](1)
    Ready = Kee[int](2)
    Error = Kee[int](3)

  class Target(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractTexture::Target' of Qt, with the 12 names
    Qt gives in it.
    """

    TargetAutomatic = Kee[int](0)
    Target1D = Kee[int](3552)
    Target1DArray = Kee[int](35864)
    Target2D = Kee[int](3553)
    Target2DArray = Kee[int](35866)
    Target3D = Kee[int](32879)
    TargetCubeMap = Kee[int](34067)
    TargetCubeMapArray = Kee[int](36873)
    Target2DMultisample = Kee[int](37120)
    Target2DMultisampleArray = Kee[int](37122)
    TargetRectangle = Kee[int](34037)
    TargetBuffer = Kee[int](35882)

  class TextureFormat(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractTexture::TextureFormat' of Qt, with the 99
    names Qt gives in it.
    """

    NoFormat = Kee[int](0)
    Automatic = Kee[int](1)
    R8_UNorm = Kee[int](33321)
    RG8_UNorm = Kee[int](33323)
    RGB8_UNorm = Kee[int](32849)
    RGBA8_UNorm = Kee[int](32856)
    R16_UNorm = Kee[int](33322)
    RG16_UNorm = Kee[int](33324)
    RGB16_UNorm = Kee[int](32852)
    RGBA16_UNorm = Kee[int](32859)
    R8_SNorm = Kee[int](36756)
    RG8_SNorm = Kee[int](36757)
    RGB8_SNorm = Kee[int](36758)
    RGBA8_SNorm = Kee[int](36759)
    R16_SNorm = Kee[int](36760)
    RG16_SNorm = Kee[int](36761)
    RGB16_SNorm = Kee[int](36762)
    RGBA16_SNorm = Kee[int](36763)
    R8U = Kee[int](33330)
    RG8U = Kee[int](33336)
    RGB8U = Kee[int](36221)
    RGBA8U = Kee[int](36220)
    R16U = Kee[int](33332)
    RG16U = Kee[int](33338)
    RGB16U = Kee[int](36215)
    RGBA16U = Kee[int](36214)
    R32U = Kee[int](33334)
    RG32U = Kee[int](33340)
    RGB32U = Kee[int](36209)
    RGBA32U = Kee[int](36208)
    R8I = Kee[int](33329)
    RG8I = Kee[int](33335)
    RGB8I = Kee[int](36239)
    RGBA8I = Kee[int](36238)
    R16I = Kee[int](33331)
    RG16I = Kee[int](33337)
    RGB16I = Kee[int](36233)
    RGBA16I = Kee[int](36232)
    R32I = Kee[int](33333)
    RG32I = Kee[int](33339)
    RGB32I = Kee[int](36227)
    RGBA32I = Kee[int](36226)
    R16F = Kee[int](33325)
    RG16F = Kee[int](33327)
    RGB16F = Kee[int](34843)
    RGBA16F = Kee[int](34842)
    R32F = Kee[int](33326)
    RG32F = Kee[int](33328)
    RGB32F = Kee[int](34837)
    RGBA32F = Kee[int](34836)
    RGB9E5 = Kee[int](35901)
    RG11B10F = Kee[int](35898)
    RG3B2 = Kee[int](10768)
    R5G6B5 = Kee[int](36194)
    RGB5A1 = Kee[int](32855)
    RGBA4 = Kee[int](32854)
    RGB10A2 = Kee[int](32857)
    RGB10A2U = Kee[int](36975)
    D16 = Kee[int](33189)
    D24 = Kee[int](33190)
    D24S8 = Kee[int](35056)
    D32 = Kee[int](33191)
    D32F = Kee[int](36012)
    D32FS8X24 = Kee[int](36013)
    RGB_DXT1 = Kee[int](33776)
    RGBA_DXT1 = Kee[int](33777)
    RGBA_DXT3 = Kee[int](33778)
    RGBA_DXT5 = Kee[int](33779)
    R_ATI1N_UNorm = Kee[int](36283)
    R_ATI1N_SNorm = Kee[int](36284)
    RG_ATI2N_UNorm = Kee[int](36285)
    RG_ATI2N_SNorm = Kee[int](36286)
    RGB_BP_UNSIGNED_FLOAT = Kee[int](36495)
    RGB_BP_SIGNED_FLOAT = Kee[int](36494)
    RGB_BP_UNorm = Kee[int](36492)
    R11_EAC_UNorm = Kee[int](37488)
    R11_EAC_SNorm = Kee[int](37489)
    RG11_EAC_UNorm = Kee[int](37490)
    RG11_EAC_SNorm = Kee[int](37491)
    RGB8_ETC2 = Kee[int](37492)
    SRGB8_ETC2 = Kee[int](37493)
    RGB8_PunchThrough_Alpha1_ETC2 = Kee[int](37494)
    SRGB8_PunchThrough_Alpha1_ETC2 = Kee[int](37495)
    RGBA8_ETC2_EAC = Kee[int](37496)
    SRGB8_Alpha8_ETC2_EAC = Kee[int](37497)
    RGB8_ETC1 = Kee[int](36196)
    SRGB8 = Kee[int](35905)
    SRGB8_Alpha8 = Kee[int](35907)
    SRGB_DXT1 = Kee[int](35916)
    SRGB_Alpha_DXT1 = Kee[int](35917)
    SRGB_Alpha_DXT3 = Kee[int](35918)
    SRGB_Alpha_DXT5 = Kee[int](35919)
    SRGB_BP_UNorm = Kee[int](36493)
    DepthFormat = Kee[int](6402)
    AlphaFormat = Kee[int](6406)
    RGBFormat = Kee[int](6407)
    RGBAFormat = Kee[int](6408)
    LuminanceFormat = Kee[int](6409)
    LuminanceAlphaFormat = Kee[int](6410)

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
    Calls Qt's 'QString Qt3DRender::QAbstractTexture::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#tr

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
    #  QString Qt3DRender::QAbstractTexture::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QAbstractTexture'

  #  A C++ Qt3DRender::QAbstractTexture Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QAbstractTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QAbstractTexture::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QAbstractTexture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Target:
    """
    Calls Qt's 'Target Qt3DRender::QAbstractTexture::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#target

    Returns
    -------

    Target
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Target(number)' gives.
    """
    #  Target Qt3DRender::QAbstractTexture::target() const
    return QAbstractTexture.Target(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture6targetEv',
    ))

  def format(self) -> TextureFormat:
    """
    Calls Qt's 'TextureFormat Qt3DRender::QAbstractTexture::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#format

    Returns
    -------

    TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureFormat(number)'
      gives.
    """
    #  TextureFormat Qt3DRender::QAbstractTexture::format() const
    return QAbstractTexture.TextureFormat(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture6formatEv',
    ))

  def generateMipMaps(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QAbstractTexture::generateMipMaps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#generateMipMaps
    """
    #  bool Qt3DRender::QAbstractTexture::generateMipMaps() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture15generateMipMapsEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status Qt3DRender::QAbstractTexture::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status Qt3DRender::QAbstractTexture::status() const
    return QAbstractTexture.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture6statusEv',
    ))

  def minificationFilter(self) -> Filter:
    """
    Calls Qt's 'Filter Qt3DRender::QAbstractTexture::minificationFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter Qt3DRender::QAbstractTexture::minificationFilter() const
    return QAbstractTexture.Filter(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture18minificationFilterEv',
    ))

  def magnificationFilter(self) -> Filter:
    """
    Calls Qt's 'Filter Qt3DRender::QAbstractTexture::magnificationFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter Qt3DRender::QAbstractTexture::magnificationFilter() const
    return QAbstractTexture.Filter(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture19magnificationFilterEv',
    ))

  def maximumAnisotropy(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QAbstractTexture::maximumAnisotropy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#maximumAnisotropy
    """
    #  float Qt3DRender::QAbstractTexture::maximumAnisotropy() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture17maximumAnisotropyEv',
    )

  def comparisonFunction(self) -> ComparisonFunction:
    """
    Calls Qt's 'ComparisonFunction
    Qt3DRender::QAbstractTexture::comparisonFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Returns
    -------

    ComparisonFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ComparisonFunction(number)' gives.
    """
    #  ComparisonFunction Qt3DRender::QAbstractTexture::comparisonFunction()
    #      const
    return QAbstractTexture.ComparisonFunction(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture18comparisonFunctionEv',
    ))

  def comparisonMode(self) -> ComparisonMode:
    """
    Calls Qt's 'ComparisonMode Qt3DRender::QAbstractTexture::comparisonMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#comparisonMode

    Returns
    -------

    ComparisonMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ComparisonMode(number)'
      gives.
    """
    #  ComparisonMode Qt3DRender::QAbstractTexture::comparisonMode() const
    return QAbstractTexture.ComparisonMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture14comparisonModeEv',
    ))

  def width(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QAbstractTexture::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#width
    """
    #  int Qt3DRender::QAbstractTexture::width() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture5widthEv',
    )

  def height(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QAbstractTexture::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#height
    """
    #  int Qt3DRender::QAbstractTexture::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture6heightEv',
    )

  def depth(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QAbstractTexture::depth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#depth
    """
    #  int Qt3DRender::QAbstractTexture::depth() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture5depthEv',
    )

  def layers(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QAbstractTexture::layers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#layers
    """
    #  int Qt3DRender::QAbstractTexture::layers() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture6layersEv',
    )

  def samples(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QAbstractTexture::samples() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#samples
    """
    #  int Qt3DRender::QAbstractTexture::samples() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture7samplesEv',
    )

  def mipLevels(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QAbstractTexture::mipLevels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#mipLevels
    """
    #  int Qt3DRender::QAbstractTexture::mipLevels() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture9mipLevelsEv',
    )

  def handleType(self) -> HandleType:
    """
    Calls Qt's 'HandleType Qt3DRender::QAbstractTexture::handleType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#handleType

    Returns
    -------

    HandleType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HandleType(number)'
      gives.
    """
    #  HandleType Qt3DRender::QAbstractTexture::handleType() const
    return QAbstractTexture.HandleType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture10handleTypeEv',
    ))

  def handle(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DRender::QAbstractTexture::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#handle

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DRender::QAbstractTexture::handle() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QAbstractTexture6handleEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  def setSize(self, width: int, height: int = 1, depth: int = 1) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setSize(int width, int
    height, int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setSize

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    depth : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void Qt3DRender::QAbstractTexture::setSize(int width, int height, int
    #      depth)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture7setSizeEiii',
        width, height, depth,
    )

  @overload(TextureFormat)
  def setFormat(self, format: TextureFormat) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setFormat(TextureFormat
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setFormat

    Parameters
    ----------

    format : TextureFormat
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::setFormat(TextureFormat format)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture9setFormatENS0_13TextureFor'
        'matE',
        format.value,
    )

  @overload(bool)
  def setGenerateMipMaps(self, gen: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setGenerateMipMaps(bool
    gen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    gen : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::setGenerateMipMaps(bool gen)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture18setGenerateMipMapsEb', gen,
    )

  @overload(int)
  def setWidth(self, width: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::setWidth(int width)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture8setWidthEi', width,
    )

  @overload(int)
  def setHeight(self, height: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setHeight(int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setHeight

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::setHeight(int height)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture9setHeightEi', height,
    )

  @overload(int)
  def setDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setDepth(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::setDepth(int depth)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture8setDepthEi', depth,
    )

  @overload(Filter)
  def setMinificationFilter(self, f: Filter) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::setMinificationFilter(Filter f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    f : Filter
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::setMinificationFilter(Filter f)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture21setMinificationFilterENS0'
        '_6FilterE',
        f.value,
    )

  @overload(Filter)
  def setMagnificationFilter(self, f: Filter) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::setMagnificationFilter(Filter f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    f : Filter
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::setMagnificationFilter(Filter f)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture22setMagnificationFilterENS'
        '0_6FilterE',
        f.value,
    )

  @overload(float)
  def setMaximumAnisotropy(self, anisotropy: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setMaximumAnisotropy(float
    anisotropy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    anisotropy : float
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::setMaximumAnisotropy(float
    #      anisotropy)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture20setMaximumAnisotropyEf',
        anisotropy,
    )

  @overload(ComparisonFunction)
  def setComparisonFunction(self, function: ComparisonFunction) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::setComparisonFunction(ComparisonFunction
    function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    function : ComparisonFunction
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::setComparisonFunction(
    #      ComparisonFunction function)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture21setComparisonFunctionENS0'
        '_18ComparisonFunctionE',
        function.value,
    )

  @overload(ComparisonMode)
  def setComparisonMode(self, mode: ComparisonMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::setComparisonMode(ComparisonMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setComparisonMode

    Parameters
    ----------

    mode : ComparisonMode
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::setComparisonMode(ComparisonMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture17setComparisonModeENS0_14C'
        'omparisonModeE',
        mode.value,
    )

  @overload(int)
  def setLayers(self, layers: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setLayers(int layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setLayers

    Parameters
    ----------

    layers : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::setLayers(int layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture9setLayersEi', layers,
    )

  @overload(int)
  def setSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setSamples(int samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setSamples

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::setSamples(int samples)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture10setSamplesEi', samples,
    )

  @overload(int)
  def setMipLevels(self, mipLevels: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setMipLevels(int
    mipLevels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setMipLevels

    Parameters
    ----------

    mipLevels : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::setMipLevels(int mipLevels)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture12setMipLevelsEi', mipLevels,
    )

  @overload(Status)
  def setStatus(self, status: Status) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setStatus(Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::setStatus(Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture9setStatusENS0_6StatusE',
        status.value,
    )

  @overload(QVariant)
  def setHandle(self, handle: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setHandle(const QVariant
    &handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setHandle

    Parameters
    ----------

    handle : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QAbstractTexture::setHandle(const QVariant &handle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture9setHandleERK8QVariant',
        self._valueOf(handle),
    )

  @overload(HandleType)
  def setHandleType(self, type: HandleType) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::setHandleType(HandleType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#setHandleType

    Parameters
    ----------

    type : HandleType
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::setHandleType(HandleType type)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture13setHandleTypeENS0_10Handl'
        'eTypeE',
        type.value,
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
    'Qt3DRender::QAbstractTexture::QAbstractTexture(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#QAbstractTexture

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QAbstractTexture::QAbstractTexture(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QAbstractTexture, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender16QAbstractTextureC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
    ))

  @overload(Target)
  @overload(Target, Qt3DCore.QNode)
  @overload(Target, NoneType)
  def __init__(
      self,
      target: Target,
      parent: Optional[Qt3DCore.QNode] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QAbstractTexture::QAbstractTexture(Target target,
    Qt3DCore::QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#QAbstractTexture

    Parameters
    ----------

    target : Target
      Passed on as its number.

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QAbstractTexture::QAbstractTexture(Target target,
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QAbstractTexture, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender16QAbstractTextureC1ENS0_6TargetEPN8Qt3DCore5'
        'QNodeE',
        target.value, self._addressOf(parent),
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

  @overload(WAIT['Qt3DRender.QAbstractTextureImage'])
  @overload(NoneType)
  def addTextureImage(
      self,
      textureImage: Optional[Qt3DRender.QAbstractTextureImage],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::addTextureImage(QAbstractTextureImage
    *textureImage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#addTextureImage

    Parameters
    ----------

    textureImage : Optional[Qt3DRender.QAbstractTextureImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QAbstractTexture::addTextureImage(
    #      QAbstractTextureImage *textureImage)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture15addTextureImageEPNS_21QAb'
        'stractTextureImageE',
        self._addressOf(textureImage),
    )

  @overload(WAIT['Qt3DRender.QAbstractTextureImage'])
  @overload(NoneType)
  def removeTextureImage(
      self,
      textureImage: Optional[Qt3DRender.QAbstractTextureImage],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::removeTextureImage(QAbstractTextureImage
    *textureImage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    textureImage : Optional[Qt3DRender.QAbstractTextureImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QAbstractTexture::removeTextureImage(
    #      QAbstractTextureImage *textureImage)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture18removeTextureImageEPNS_21'
        'QAbstractTextureImageE',
        self._addressOf(textureImage),
    )

  def wrapMode(self) -> Optional[Qt3DRender.QTextureWrapMode]:
    """
    Calls Qt's 'QTextureWrapMode *Qt3DRender::QAbstractTexture::wrapMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#wrapMode

    Returns
    -------

    Optional[Qt3DRender.QTextureWrapMode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureWrapMode *Qt3DRender::QAbstractTexture::wrapMode()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture8wrapModeEv',
    )
    return Qt3DRender.QTextureWrapMode._cuteAt(address)

  @overload(WAIT['Qt3DRender.QTextureDataUpdate'])
  def updateData(self, update: Qt3DRender.QTextureDataUpdate) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::updateData(const
    QTextureDataUpdate &update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#updateData

    Parameters
    ----------

    update : Qt3DRender.QTextureDataUpdate
      Passed on as a value: Qt reads the C++ Qt3DRender::QTextureDataUpdate,
      which stays Python's own.
    """
    #  void Qt3DRender::QAbstractTexture::updateData(const QTextureDataUpdate
    #      &update)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture10updateDataERKNS_18QTextur'
        'eDataUpdateE',
        self._valueOf(update),
    )

  @overload(TextureFormat)
  def formatChanged(self, format: TextureFormat) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::formatChanged(TextureFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#formatChanged

    Parameters
    ----------

    format : TextureFormat
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::formatChanged(TextureFormat format)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture13formatChangedENS0_13Textu'
        'reFormatE',
        format.value,
    )

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::statusChanged(Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#statusChanged

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::statusChanged(Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture13statusChangedENS0_6Status'
        'E',
        status.value,
    )

  @overload(bool)
  def generateMipMapsChanged(self, generateMipMaps: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::generateMipMapsChanged(bool
    generateMipMaps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    generateMipMaps : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::generateMipMapsChanged(bool
    #      generateMipMaps)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture22generateMipMapsChangedEb',
        generateMipMaps,
    )

  @overload(int)
  def widthChanged(self, width: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::widthChanged(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#widthChanged

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::widthChanged(int width)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture12widthChangedEi', width,
    )

  @overload(int)
  def heightChanged(self, height: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::heightChanged(int
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#heightChanged

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::heightChanged(int height)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture13heightChangedEi', height,
    )

  @overload(int)
  def depthChanged(self, depth: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::depthChanged(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#depthChanged

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::depthChanged(int depth)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture12depthChangedEi', depth,
    )

  @overload(Filter)
  def magnificationFilterChanged(self, magnificationFilter: Filter) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::magnificationFilterChanged(Filter
    magnificationFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    magnificationFilter : Filter
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::magnificationFilterChanged(Filter
    #      magnificationFilter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture26magnificationFilterChange'
        'dENS0_6FilterE',
        magnificationFilter.value,
    )

  @overload(Filter)
  def minificationFilterChanged(self, minificationFilter: Filter) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::minificationFilterChanged(Filter
    minificationFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    minificationFilter : Filter
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::minificationFilterChanged(Filter
    #      minificationFilter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture25minificationFilterChanged'
        'ENS0_6FilterE',
        minificationFilter.value,
    )

  @overload(float)
  def maximumAnisotropyChanged(self, maximumAnisotropy: float) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::maximumAnisotropyChanged(float
    maximumAnisotropy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    maximumAnisotropy : float
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::maximumAnisotropyChanged(float
    #      maximumAnisotropy)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture24maximumAnisotropyChangedE'
        'f',
        maximumAnisotropy,
    )

  @overload(ComparisonFunction)
  def comparisonFunctionChanged(
      self,
      comparisonFunction: ComparisonFunction,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::comparisonFunctionChanged(
    ComparisonFunction comparisonFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    comparisonFunction : ComparisonFunction
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::comparisonFunctionChanged(
    #      ComparisonFunction comparisonFunction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture25comparisonFunctionChanged'
        'ENS0_18ComparisonFunctionE',
        comparisonFunction.value,
    )

  @overload(ComparisonMode)
  def comparisonModeChanged(self, comparisonMode: ComparisonMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::comparisonModeChanged(ComparisonMode
    comparisonMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html

    Parameters
    ----------

    comparisonMode : ComparisonMode
      Passed on as its number.
    """
    #  void
    #      Qt3DRender::QAbstractTexture::comparisonModeChanged(ComparisonMode
    #      comparisonMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture21comparisonModeChangedENS0'
        '_14ComparisonModeE',
        comparisonMode.value,
    )

  @overload(int)
  def layersChanged(self, layers: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::layersChanged(int
    layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#layersChanged

    Parameters
    ----------

    layers : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::layersChanged(int layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture13layersChangedEi', layers,
    )

  @overload(int)
  def samplesChanged(self, samples: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::samplesChanged(int
    samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#samplesChanged

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::samplesChanged(int samples)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture14samplesChangedEi', samples,
    )

  @overload(HandleType)
  def handleTypeChanged(self, handleType: HandleType) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTexture::handleTypeChanged(HandleType handleType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#handleTypeChanged

    Parameters
    ----------

    handleType : HandleType
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTexture::handleTypeChanged(HandleType
    #      handleType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture17handleTypeChangedENS0_10H'
        'andleTypeE',
        handleType.value,
    )

  @overload(QVariant)
  def handleChanged(self, handle: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::handleChanged(QVariant
    handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#handleChanged

    Parameters
    ----------

    handle : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QAbstractTexture::handleChanged(QVariant handle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture13handleChangedE8QVariant',
        self._valueOf(handle),
    )

  @overload(int)
  def mipLevelsChanged(self, mipLevels: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTexture::mipLevelsChanged(int
    mipLevels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#mipLevelsChanged

    Parameters
    ----------

    mipLevels : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTexture::mipLevelsChanged(int mipLevels)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture16mipLevelsChangedEi',
        mipLevels,
    )

  def d_func(self) -> Optional[Qt3DRender.QAbstractTexturePrivate]:
    """
    Calls Qt's 'QAbstractTexturePrivate
    *Qt3DRender::QAbstractTexture::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttexture.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexturePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTexturePrivate *Qt3DRender::QAbstractTexture::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender16QAbstractTexture6d_funcEv',
    )
    return Qt3DRender.QAbstractTexturePrivate._cuteAt(address)

  @staticmethod
  def setWrapMode(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QAbstractTexture::setWrapMode(const
    QTextureWrapMode &wrapMode)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractTexture.setWrapMode' has no cute function "
        "yet. Qt's 'void Qt3DRender::QAbstractTexture::setWrapMode(const "
        "QTextureWrapMode &wrapMode)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def textureImages(*__, **_) -> Never:
    """
    Qt's 'QList<QAbstractTextureImage *>
    Qt3DRender::QAbstractTexture::textureImages() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractTexture.textureImages' has no cute function "
        "yet. Qt's 'QList<QAbstractTextureImage *> "
        "Qt3DRender::QAbstractTexture::textureImages() const': gives a type "
        "Python has no way to take yet.")
