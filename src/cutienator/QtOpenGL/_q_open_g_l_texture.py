"""
QOpenGLTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopengltexture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor, QImage
  from . import QOpenGLTexturePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']


class QOpenGLTexture(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLTexture: a plain Python object standing in
  front of one C++ QOpenGLTexture.

  What exists
  -----------

  Every function of Qt's QOpenGLTexture that has a ritual and that Python can
  call so far, 66 names in all: 'target', 'create', 'destroy', 'isCreated',
  'textureId', 'bind', 'release', 'isBound', 'boundTextureId', 'setFormat',
  'format', 'setSize', 'width', 'height', 'depth', 'setMipLevels',
  'mipLevels', 'maximumMipLevels', 'setLayers', 'layers', 'faces',
  'setSamples', 'samples', 'setFixedSamplePositions',
  'isFixedSamplePositions', 'allocateStorage', 'isStorageAllocated',
  'createTextureView', 'isTextureView', 'setData', 'hasFeature',
  'setMipBaseLevel', 'mipBaseLevel', 'setMipMaxLevel', 'mipMaxLevel',
  'setMipLevelRange', 'setAutoMipMapGenerationEnabled',
  'isAutoMipMapGenerationEnabled', 'generateMipMaps', 'setSwizzleMask',
  'swizzleMask', 'setDepthStencilMode', 'depthStencilMode',
  'setComparisonFunction', 'comparisonFunction', 'setComparisonMode',
  'comparisonMode', 'setMinificationFilter', 'minificationFilter',
  'setMagnificationFilter', 'magnificationFilter', 'setMinMagFilters',
  'setMaximumAnisotropy', 'maximumAnisotropy', 'setWrapMode', 'wrapMode',
  'setBorderColor', 'borderColor', 'setMinimumLevelOfDetail',
  'minimumLevelOfDetail', 'setMaximumLevelOfDetail', 'maximumLevelOfDetail',
  'setLevelOfDetailRange', 'setLevelofDetailBias', 'levelofDetailBias',
  'd_func'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLTexture::~QOpenGLTexture()': the destructor: Python never
    removes a C++ QOpenGLTexture.
  - Qt's 'void QOpenGLTexture::setData(int mipLevel, int layer, CubeMapFace
    cubeFace, PixelFormat sourceFormat, PixelType sourceType, const void
    *data, const QOpenGLPixelTransferOptions *const options)': names 'void',
    which has no cute class yet.
  - Qt's 'void QOpenGLTexture::setData(int mipLevel, int layer, int
    layerCount, CubeMapFace cubeFace, PixelFormat sourceFormat, PixelType
    sourceType, const void *data, const QOpenGLPixelTransferOptions *const
    options)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLTexture::setData(int mipLevel, int layer, PixelFormat
    sourceFormat, PixelType sourceType, const void *data, const
    QOpenGLPixelTransferOptions *const options)': names 'void', which has no
    cute class yet.
  - Qt's 'void QOpenGLTexture::setData(int mipLevel, PixelFormat
    sourceFormat, PixelType sourceType, const void *data, const
    QOpenGLPixelTransferOptions *const options)': names 'void', which has no
    cute class yet.
  - Qt's 'void QOpenGLTexture::setData(PixelFormat sourceFormat, PixelType
    sourceType, const void *data, const QOpenGLPixelTransferOptions *const
    options)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLTexture::setData(int xOffset, int yOffset, int zOffset,
    int width, int height, int depth, PixelFormat sourceFormat, PixelType
    sourceType, const void *data, const QOpenGLPixelTransferOptions *const
    options)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLTexture::setData(int xOffset, int yOffset, int zOffset,
    int width, int height, int depth, int mipLevel, PixelFormat sourceFormat,
    PixelType sourceType, const void *data, const QOpenGLPixelTransferOptions
    *const options)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLTexture::setData(int xOffset, int yOffset, int zOffset,
    int width, int height, int depth, int mipLevel, int layer, PixelFormat
    sourceFormat, PixelType sourceType, const void *data, const
    QOpenGLPixelTransferOptions *const options)': names 'void', which has no
    cute class yet.
  - Qt's 'void QOpenGLTexture::setData(int xOffset, int yOffset, int zOffset,
    int width, int height, int depth, int mipLevel, int layer, CubeMapFace
    cubeFace, PixelFormat sourceFormat, PixelType sourceType, const void
    *data, const QOpenGLPixelTransferOptions *const options)': names 'void',
    which has no cute class yet.
  - Qt's 'void QOpenGLTexture::setData(int xOffset, int yOffset, int zOffset,
    int width, int height, int depth, int mipLevel, int layer, CubeMapFace
    cubeFace, int layerCount, PixelFormat sourceFormat, PixelType sourceType,
    const void *data, const QOpenGLPixelTransferOptions *const options)':
    names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLTexture::setCompressedData(int mipLevel, int layer,
    CubeMapFace cubeFace, int dataSize, const void *data, const
    QOpenGLPixelTransferOptions *const options)': names 'void', which has no
    cute class yet.
  - Qt's 'void QOpenGLTexture::setCompressedData(int mipLevel, int layer, int
    layerCount, CubeMapFace cubeFace, int dataSize, const void *data, const
    QOpenGLPixelTransferOptions *const options)': names 'void', which has no
    cute class yet.
  - Qt's 'void QOpenGLTexture::setCompressedData(int mipLevel, int layer, int
    dataSize, const void *data, const QOpenGLPixelTransferOptions *const
    options)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLTexture::setCompressedData(int mipLevel, int dataSize,
    const void *data, const QOpenGLPixelTransferOptions *const options)':
    names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLTexture::setCompressedData(int dataSize, const void
    *data, const QOpenGLPixelTransferOptions *const options)': names 'void',
    which has no cute class yet.
  - Qt's 'std::pair<int, int> QOpenGLTexture::mipLevelRange() const': gives a
    type Python has no way to take yet.
  - Qt's 'std::pair<Filter, Filter> QOpenGLTexture::minMagFilters() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QOpenGLTexture::setBorderColor(uint r, uint g, uint b, uint
    a)': takes in Python what 'void QOpenGLTexture::setBorderColor(int r, int
    g, int b, int a)' takes.
  - Qt's 'void QOpenGLTexture::borderColor(float *border) const': takes a
    number to change where it is.
  - Qt's 'void QOpenGLTexture::borderColor(int *border) const': takes a
    number to change where it is.
  - Qt's 'void QOpenGLTexture::borderColor(unsigned int *border) const':
    takes a number to change where it is.
  - Qt's 'std::pair<float, float> QOpenGLTexture::levelOfDetailRange()
    const': gives a type Python has no way to take yet.
  - Qt's 'QDebug operator<<(QDebug dbg, const QOpenGLTexture *t)': an
    operator between other classes, written inside this one.
  - Qt's 'const QOpenGLTexturePrivate *QOpenGLTexture::d_func() const': takes
    in Python what 'QOpenGLTexturePrivate *QOpenGLTexture::d_func()' takes.

  What has no ritual
  ------------------

  5 of the 108 functions Qt declares: 3 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLTexture is created at the first use, not by
    'QOpenGLTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLTexture.
  - Each name of Qt's QOpenGLTexture that has no cute function yet,
    'levelOfDetailRange', 'minMagFilters', 'mipLevelRange',
    'setCompressedData', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QOpenGLTexture, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BindingTarget(CuteNum):
    """
    The enum 'QOpenGLTexture::BindingTarget' of Qt, with the 11 names Qt
    gives in it.
    """

    BindingTarget1D = Kee[int](32872)
    BindingTarget1DArray = Kee[int](35868)
    BindingTarget2D = Kee[int](32873)
    BindingTarget2DArray = Kee[int](35869)
    BindingTarget3D = Kee[int](32874)
    BindingTargetCubeMap = Kee[int](34068)
    BindingTargetCubeMapArray = Kee[int](36874)
    BindingTarget2DMultisample = Kee[int](37124)
    BindingTarget2DMultisampleArray = Kee[int](37125)
    BindingTargetRectangle = Kee[int](34038)
    BindingTargetBuffer = Kee[int](35884)

  class ComparisonFunction(CuteNum):
    """
    The enum 'QOpenGLTexture::ComparisonFunction' of Qt, with the 9 names Qt
    gives in it.
    """

    CompareLessEqual = Kee[int](515)
    CompareGreaterEqual = Kee[int](518)
    CompareLess = Kee[int](513)
    CompareGreater = Kee[int](516)
    CompareEqual = Kee[int](514)
    CompareNotEqual = Kee[int](517)
    CompareAlways = Kee[int](519)
    CompareNever = Kee[int](512)
    CommpareNotEqual = Kee[int](517)

  class ComparisonMode(CuteNum):
    """
    The enum 'QOpenGLTexture::ComparisonMode' of Qt, with the 2 names Qt
    gives in it.
    """

    CompareRefToTexture = Kee[int](34894)
    CompareNone = Kee[int](0)

  class CoordinateDirection(CuteNum):
    """
    The enum 'QOpenGLTexture::CoordinateDirection' of Qt, with the 3 names Qt
    gives in it.
    """

    DirectionS = Kee[int](10242)
    DirectionT = Kee[int](10243)
    DirectionR = Kee[int](32882)

  class CubeMapFace(CuteNum):
    """
    The enum 'QOpenGLTexture::CubeMapFace' of Qt, with the 6 names Qt gives
    in it.
    """

    CubeMapPositiveX = Kee[int](34069)
    CubeMapNegativeX = Kee[int](34070)
    CubeMapPositiveY = Kee[int](34071)
    CubeMapNegativeY = Kee[int](34072)
    CubeMapPositiveZ = Kee[int](34073)
    CubeMapNegativeZ = Kee[int](34074)

  class DepthStencilMode(CuteNum):
    """
    The enum 'QOpenGLTexture::DepthStencilMode' of Qt, with the 2 names Qt
    gives in it.
    """

    DepthMode = Kee[int](6402)
    StencilMode = Kee[int](6401)

  class Feature(CuteFlags):
    """
    The flags enum 'QOpenGLTexture::Feature' of Qt, with the 17 names Qt
    gives in it. Qt names the type of its combinations
    'QOpenGLTexture::Features'.
    """

    ImmutableStorage = 0x1
    ImmutableMultisampleStorage = 0x2
    TextureRectangle = 0x4
    TextureArrays = 0x8
    Texture3D = 0x10
    TextureMultisample = 0x20
    TextureBuffer = 0x40
    TextureCubeMapArrays = 0x80
    Swizzle = 0x100
    StencilTexturing = 0x200
    AnisotropicFiltering = 0x400
    NPOTTextures = 0x800
    NPOTTextureRepeat = 0x1000
    Texture1D = 0x2000
    TextureComparisonOperators = 0x4000
    TextureMipMapLevel = 0x8000
    MaxFeatureFlag = 0x10000

  Features = Feature

  class Filter(CuteNum):
    """
    The enum 'QOpenGLTexture::Filter' of Qt, with the 6 names Qt gives in it.
    """

    Nearest = Kee[int](9728)
    Linear = Kee[int](9729)
    NearestMipMapNearest = Kee[int](9984)
    NearestMipMapLinear = Kee[int](9986)
    LinearMipMapNearest = Kee[int](9985)
    LinearMipMapLinear = Kee[int](9987)

  class MipMapGeneration(CuteNum):
    """
    The enum 'QOpenGLTexture::MipMapGeneration' of Qt, with the 2 names Qt
    gives in it.
    """

    GenerateMipMaps = Kee[int](0)
    DontGenerateMipMaps = Kee[int](1)

  class PixelFormat(CuteNum):
    """
    The enum 'QOpenGLTexture::PixelFormat' of Qt, with the 19 names Qt gives
    in it.
    """

    NoSourceFormat = Kee[int](0)
    Red = Kee[int](6403)
    RG = Kee[int](33319)
    RGB = Kee[int](6407)
    BGR = Kee[int](32992)
    RGBA = Kee[int](6408)
    BGRA = Kee[int](32993)
    Red_Integer = Kee[int](36244)
    RG_Integer = Kee[int](33320)
    RGB_Integer = Kee[int](36248)
    BGR_Integer = Kee[int](36250)
    RGBA_Integer = Kee[int](36249)
    BGRA_Integer = Kee[int](36251)
    Stencil = Kee[int](6401)
    Depth = Kee[int](6402)
    DepthStencil = Kee[int](34041)
    Alpha = Kee[int](6406)
    Luminance = Kee[int](6409)
    LuminanceAlpha = Kee[int](6410)

  class PixelType(CuteNum):
    """
    The enum 'QOpenGLTexture::PixelType' of Qt, with the 26 names Qt gives in
    it.
    """

    NoPixelType = Kee[int](0)
    Int8 = Kee[int](5120)
    UInt8 = Kee[int](5121)
    Int16 = Kee[int](5122)
    UInt16 = Kee[int](5123)
    Int32 = Kee[int](5124)
    UInt32 = Kee[int](5125)
    Float16 = Kee[int](5131)
    Float16OES = Kee[int](36193)
    Float32 = Kee[int](5126)
    UInt32_RGB9_E5 = Kee[int](35902)
    UInt32_RG11B10F = Kee[int](35899)
    UInt8_RG3B2 = Kee[int](32818)
    UInt8_RG3B2_Rev = Kee[int](33634)
    UInt16_RGB5A1 = Kee[int](32820)
    UInt16_RGB5A1_Rev = Kee[int](33638)
    UInt16_R5G6B5 = Kee[int](33635)
    UInt16_R5G6B5_Rev = Kee[int](33636)
    UInt16_RGBA4 = Kee[int](32819)
    UInt16_RGBA4_Rev = Kee[int](33637)
    UInt32_RGBA8 = Kee[int](32821)
    UInt32_RGBA8_Rev = Kee[int](33639)
    UInt32_RGB10A2 = Kee[int](32822)
    UInt32_RGB10A2_Rev = Kee[int](33640)
    UInt32_D24S8 = Kee[int](34042)
    Float32_D32_UInt32_S8_X24 = Kee[int](36269)

  class SwizzleComponent(CuteNum):
    """
    The enum 'QOpenGLTexture::SwizzleComponent' of Qt, with the 4 names Qt
    gives in it.
    """

    SwizzleRed = Kee[int](36418)
    SwizzleGreen = Kee[int](36419)
    SwizzleBlue = Kee[int](36420)
    SwizzleAlpha = Kee[int](36421)

  class SwizzleValue(CuteNum):
    """
    The enum 'QOpenGLTexture::SwizzleValue' of Qt, with the 6 names Qt gives
    in it.
    """

    RedValue = Kee[int](6403)
    GreenValue = Kee[int](6404)
    BlueValue = Kee[int](6405)
    AlphaValue = Kee[int](6406)
    ZeroValue = Kee[int](0)
    OneValue = Kee[int](1)

  class Target(CuteNum):
    """
    The enum 'QOpenGLTexture::Target' of Qt, with the 11 names Qt gives in
    it.
    """

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
    The enum 'QOpenGLTexture::TextureFormat' of Qt, with the 126 names Qt
    gives in it.
    """

    NoFormat = Kee[int](0)
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
    RGB10A2 = Kee[int](36975)
    D16 = Kee[int](33189)
    D24 = Kee[int](33190)
    D24S8 = Kee[int](35056)
    D32 = Kee[int](33191)
    D32F = Kee[int](36012)
    D32FS8X24 = Kee[int](36013)
    S8 = Kee[int](36168)
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
    RGBA_ASTC_4x4 = Kee[int](37808)
    RGBA_ASTC_5x4 = Kee[int](37809)
    RGBA_ASTC_5x5 = Kee[int](37810)
    RGBA_ASTC_6x5 = Kee[int](37811)
    RGBA_ASTC_6x6 = Kee[int](37812)
    RGBA_ASTC_8x5 = Kee[int](37813)
    RGBA_ASTC_8x6 = Kee[int](37814)
    RGBA_ASTC_8x8 = Kee[int](37815)
    RGBA_ASTC_10x5 = Kee[int](37816)
    RGBA_ASTC_10x6 = Kee[int](37817)
    RGBA_ASTC_10x8 = Kee[int](37818)
    RGBA_ASTC_10x10 = Kee[int](37819)
    RGBA_ASTC_12x10 = Kee[int](37820)
    RGBA_ASTC_12x12 = Kee[int](37821)
    SRGB8_Alpha8_ASTC_4x4 = Kee[int](37840)
    SRGB8_Alpha8_ASTC_5x4 = Kee[int](37841)
    SRGB8_Alpha8_ASTC_5x5 = Kee[int](37842)
    SRGB8_Alpha8_ASTC_6x5 = Kee[int](37843)
    SRGB8_Alpha8_ASTC_6x6 = Kee[int](37844)
    SRGB8_Alpha8_ASTC_8x5 = Kee[int](37845)
    SRGB8_Alpha8_ASTC_8x6 = Kee[int](37846)
    SRGB8_Alpha8_ASTC_8x8 = Kee[int](37847)
    SRGB8_Alpha8_ASTC_10x5 = Kee[int](37848)
    SRGB8_Alpha8_ASTC_10x6 = Kee[int](37849)
    SRGB8_Alpha8_ASTC_10x8 = Kee[int](37850)
    SRGB8_Alpha8_ASTC_10x10 = Kee[int](37851)
    SRGB8_Alpha8_ASTC_12x10 = Kee[int](37852)
    SRGB8_Alpha8_ASTC_12x12 = Kee[int](37853)
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

  class TextureFormatClass(CuteNum):
    """
    The enum 'QOpenGLTexture::TextureFormatClass' of Qt, with the 18 names Qt
    gives in it.
    """

    NoFormatClass = Kee[int](0)
    FormatClass_128Bit = Kee[int](1)
    FormatClass_96Bit = Kee[int](2)
    FormatClass_64Bit = Kee[int](3)
    FormatClass_48Bit = Kee[int](4)
    FormatClass_32Bit = Kee[int](5)
    FormatClass_24Bit = Kee[int](6)
    FormatClass_16Bit = Kee[int](7)
    FormatClass_8Bit = Kee[int](8)
    FormatClass_RGTC1_R = Kee[int](9)
    FormatClass_RGTC2_RG = Kee[int](10)
    FormatClass_BPTC_Unorm = Kee[int](11)
    FormatClass_BPTC_Float = Kee[int](12)
    FormatClass_S3TC_DXT1_RGB = Kee[int](13)
    FormatClass_S3TC_DXT1_RGBA = Kee[int](14)
    FormatClass_S3TC_DXT3_RGBA = Kee[int](15)
    FormatClass_S3TC_DXT5_RGBA = Kee[int](16)
    FormatClass_Unique = Kee[int](17)

  class TextureUnitReset(CuteNum):
    """
    The enum 'QOpenGLTexture::TextureUnitReset' of Qt, with the 2 names Qt
    gives in it.
    """

    ResetTextureUnit = Kee[int](0)
    DontResetTextureUnit = Kee[int](1)

  class WrapMode(CuteNum):
    """
    The enum 'QOpenGLTexture::WrapMode' of Qt, with the 4 names Qt gives in
    it.
    """

    Repeat = Kee[int](10497)
    MirroredRepeat = Kee[int](33648)
    ClampToEdge = Kee[int](33071)
    ClampToBorder = Kee[int](33069)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(BindingTarget)
  def boundTextureId(target: BindingTarget) -> int:
    """
    Calls Qt's 'GLuint QOpenGLTexture::boundTextureId(BindingTarget target)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#boundTextureId

    Parameters
    ----------

    target : BindingTarget
      Passed on as its number.
    """
    #  GLuint QOpenGLTexture::boundTextureId(BindingTarget target)
    return Rituals.call(
        'ritual_ZN14QOpenGLTexture14boundTextureIdENS_13BindingTargetE',
        target.value,
    )

  @staticmethod
  @overload(int, BindingTarget)
  def boundTextureId(unit: int, target: BindingTarget) -> int:
    """
    Calls Qt's 'GLuint QOpenGLTexture::boundTextureId(uint unit,
    BindingTarget target)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#boundTextureId

    Parameters
    ----------

    unit : int
      Passed on as it is.

    target : BindingTarget
      Passed on as its number.
    """
    #  GLuint QOpenGLTexture::boundTextureId(uint unit, BindingTarget target)
    return Rituals.call(
        'ritual_ZN14QOpenGLTexture14boundTextureIdEjNS_13BindingTargetE',
        unit, target.value,
    )

  @staticmethod
  @overload(Feature)
  def hasFeature(feature: Feature) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexture::hasFeature(Feature feature)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#hasFeature

    Parameters
    ----------

    feature : Feature
      Passed on as its number.
    """
    #  bool QOpenGLTexture::hasFeature(Feature feature)
    return Rituals.call(
        'ritual_ZN14QOpenGLTexture10hasFeatureENS_7FeatureE', feature.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def target(self) -> Target:
    """
    Calls Qt's 'Target QOpenGLTexture::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#target

    Returns
    -------

    Target
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Target(number)' gives.
    """
    #  Target QOpenGLTexture::target() const
    return QOpenGLTexture.Target(self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture6targetEv',
    ))

  def isCreated(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexture::isCreated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#isCreated
    """
    #  bool QOpenGLTexture::isCreated() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture9isCreatedEv')

  def textureId(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLTexture::textureId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#textureId
    """
    #  GLuint QOpenGLTexture::textureId() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture9textureIdEv')

  @overload()
  def isBound(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexture::isBound() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#isBound
    """
    #  bool QOpenGLTexture::isBound() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture7isBoundEv')

  @overload(int)
  def isBound(self, unit: int) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexture::isBound(uint unit)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#isBound

    Parameters
    ----------

    unit : int
      Passed on as it is.
    """
    #  bool QOpenGLTexture::isBound(uint unit)
    return self.uglySide.call('ritual_ZN14QOpenGLTexture7isBoundEj', unit)

  def format(self) -> TextureFormat:
    """
    Calls Qt's 'TextureFormat QOpenGLTexture::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#format

    Returns
    -------

    TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureFormat(number)'
      gives.
    """
    #  TextureFormat QOpenGLTexture::format() const
    return QOpenGLTexture.TextureFormat(self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture6formatEv',
    ))

  def width(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#width
    """
    #  int QOpenGLTexture::width() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#height
    """
    #  int QOpenGLTexture::height() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture6heightEv')

  def depth(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#depth
    """
    #  int QOpenGLTexture::depth() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture5depthEv')

  def mipLevels(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::mipLevels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#mipLevels
    """
    #  int QOpenGLTexture::mipLevels() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture9mipLevelsEv')

  def maximumMipLevels(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::maximumMipLevels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#maximumMipLevels
    """
    #  int QOpenGLTexture::maximumMipLevels() const
    return self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture16maximumMipLevelsEv',
    )

  def layers(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::layers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#layers
    """
    #  int QOpenGLTexture::layers() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture6layersEv')

  def faces(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::faces() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#faces
    """
    #  int QOpenGLTexture::faces() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture5facesEv')

  def samples(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::samples() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#samples
    """
    #  int QOpenGLTexture::samples() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture7samplesEv')

  def isFixedSamplePositions(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexture::isFixedSamplePositions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#isFixedSamplePositions
    """
    #  bool QOpenGLTexture::isFixedSamplePositions() const
    return self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture22isFixedSamplePositionsEv',
    )

  def isStorageAllocated(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexture::isStorageAllocated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#isStorageAllocated
    """
    #  bool QOpenGLTexture::isStorageAllocated() const
    return self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture18isStorageAllocatedEv',
    )

  @overload(Target, TextureFormat, int, int, int, int)
  def createTextureView(
      self,
      target: Target,
      viewFormat: TextureFormat,
      minimumMipmapLevel: int,
      maximumMipmapLevel: int,
      minimumLayer: int,
      maximumLayer: int,
  ) -> Optional[QOpenGLTexture]:
    """
    Calls Qt's 'QOpenGLTexture *QOpenGLTexture::createTextureView(Target
    target, TextureFormat viewFormat, int minimumMipmapLevel, int
    maximumMipmapLevel, int minimumLayer, int maximumLayer) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#createTextureView

    Parameters
    ----------

    target : Target
      Passed on as its number.

    viewFormat : TextureFormat
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
    #  QOpenGLTexture *QOpenGLTexture::createTextureView(Target target,
    #      TextureFormat viewFormat, int minimumMipmapLevel, int
    #      maximumMipmapLevel, int minimumLayer, int maximumLayer) const
    address = self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture17createTextureViewENS_6TargetENS_13Text'
        'ureFormatEiiii',
        target.value, viewFormat.value, minimumMipmapLevel,
        maximumMipmapLevel, minimumLayer, maximumLayer,
    )
    return QOpenGLTexture._cuteAt(address)

  def isTextureView(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexture::isTextureView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#isTextureView
    """
    #  bool QOpenGLTexture::isTextureView() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture13isTextureViewEv')

  def mipBaseLevel(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::mipBaseLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#mipBaseLevel
    """
    #  int QOpenGLTexture::mipBaseLevel() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture12mipBaseLevelEv')

  def mipMaxLevel(self) -> int:
    """
    Calls Qt's 'int QOpenGLTexture::mipMaxLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#mipMaxLevel
    """
    #  int QOpenGLTexture::mipMaxLevel() const
    return self.uglySide.call('ritual_ZNK14QOpenGLTexture11mipMaxLevelEv')

  def isAutoMipMapGenerationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexture::isAutoMipMapGenerationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#isAutoMipMapGenerationEnabled
    """
    #  bool QOpenGLTexture::isAutoMipMapGenerationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture29isAutoMipMapGenerationEnabledEv',
    )

  @overload(SwizzleComponent)
  def swizzleMask(self, component: SwizzleComponent) -> SwizzleValue:
    """
    Calls Qt's 'SwizzleValue QOpenGLTexture::swizzleMask(SwizzleComponent
    component) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#swizzleMask

    Parameters
    ----------

    component : SwizzleComponent
      Passed on as its number.

    Returns
    -------

    SwizzleValue
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SwizzleValue(number)'
      gives.
    """
    #  SwizzleValue QOpenGLTexture::swizzleMask(SwizzleComponent component)
    #      const
    return QOpenGLTexture.SwizzleValue(self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture11swizzleMaskENS_16SwizzleComponentE',
        component.value,
    ))

  def depthStencilMode(self) -> DepthStencilMode:
    """
    Calls Qt's 'DepthStencilMode QOpenGLTexture::depthStencilMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#depthStencilMode

    Returns
    -------

    DepthStencilMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DepthStencilMode(number)'
      gives.
    """
    #  DepthStencilMode QOpenGLTexture::depthStencilMode() const
    return QOpenGLTexture.DepthStencilMode(self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture16depthStencilModeEv',
    ))

  def comparisonFunction(self) -> ComparisonFunction:
    """
    Calls Qt's 'ComparisonFunction QOpenGLTexture::comparisonFunction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#comparisonFunction

    Returns
    -------

    ComparisonFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ComparisonFunction(number)' gives.
    """
    #  ComparisonFunction QOpenGLTexture::comparisonFunction() const
    return QOpenGLTexture.ComparisonFunction(self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture18comparisonFunctionEv',
    ))

  def comparisonMode(self) -> ComparisonMode:
    """
    Calls Qt's 'ComparisonMode QOpenGLTexture::comparisonMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#comparisonMode

    Returns
    -------

    ComparisonMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ComparisonMode(number)'
      gives.
    """
    #  ComparisonMode QOpenGLTexture::comparisonMode() const
    return QOpenGLTexture.ComparisonMode(self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture14comparisonModeEv',
    ))

  def minificationFilter(self) -> Filter:
    """
    Calls Qt's 'Filter QOpenGLTexture::minificationFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#minificationFilter

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter QOpenGLTexture::minificationFilter() const
    return QOpenGLTexture.Filter(self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture18minificationFilterEv',
    ))

  def magnificationFilter(self) -> Filter:
    """
    Calls Qt's 'Filter QOpenGLTexture::magnificationFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#magnificationFilter

    Returns
    -------

    Filter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Filter(number)' gives.
    """
    #  Filter QOpenGLTexture::magnificationFilter() const
    return QOpenGLTexture.Filter(self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture19magnificationFilterEv',
    ))

  def maximumAnisotropy(self) -> float:
    """
    Calls Qt's 'float QOpenGLTexture::maximumAnisotropy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#maximumAnisotropy
    """
    #  float QOpenGLTexture::maximumAnisotropy() const
    return self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture17maximumAnisotropyEv',
    )

  @overload(CoordinateDirection)
  def wrapMode(self, direction: CoordinateDirection) -> WrapMode:
    """
    Calls Qt's 'WrapMode QOpenGLTexture::wrapMode(CoordinateDirection
    direction) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#wrapMode

    Parameters
    ----------

    direction : CoordinateDirection
      Passed on as its number.

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  WrapMode QOpenGLTexture::wrapMode(CoordinateDirection direction) const
    return QOpenGLTexture.WrapMode(self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture8wrapModeENS_19CoordinateDirectionE',
        direction.value,
    ))

  def borderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QOpenGLTexture::borderColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#borderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QOpenGLTexture::borderColor() const
    address = self.uglySide.call('ritual_ZNK14QOpenGLTexture11borderColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def minimumLevelOfDetail(self) -> float:
    """
    Calls Qt's 'float QOpenGLTexture::minimumLevelOfDetail() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#minimumLevelOfDetail
    """
    #  float QOpenGLTexture::minimumLevelOfDetail() const
    return self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture20minimumLevelOfDetailEv',
    )

  def maximumLevelOfDetail(self) -> float:
    """
    Calls Qt's 'float QOpenGLTexture::maximumLevelOfDetail() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#maximumLevelOfDetail
    """
    #  float QOpenGLTexture::maximumLevelOfDetail() const
    return self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture20maximumLevelOfDetailEv',
    )

  def levelofDetailBias(self) -> float:
    """
    Calls Qt's 'float QOpenGLTexture::levelofDetailBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#levelofDetailBias
    """
    #  float QOpenGLTexture::levelofDetailBias() const
    return self.uglySide.call(
        'ritual_ZNK14QOpenGLTexture17levelofDetailBiasEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TextureFormat)
  def setFormat(self, format: TextureFormat) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setFormat(TextureFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setFormat

    Parameters
    ----------

    format : TextureFormat
      Passed on as its number.
    """
    #  void QOpenGLTexture::setFormat(TextureFormat format)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture9setFormatENS_13TextureFormatE',
        format.value,
    )

  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  def setSize(self, width: int, height: int = 1, depth: int = 1) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setSize(int width, int height, int
    depth)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setSize

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    depth : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QOpenGLTexture::setSize(int width, int height, int depth)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture7setSizeEiii', width, height, depth,
    )

  @overload(int)
  def setMipLevels(self, levels: int) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMipLevels(int levels)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setMipLevels

    Parameters
    ----------

    levels : int
      Passed on as it is.
    """
    #  void QOpenGLTexture::setMipLevels(int levels)
    self.uglySide.call('ritual_ZN14QOpenGLTexture12setMipLevelsEi', levels)

  @overload(int)
  def setLayers(self, layers: int) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setLayers(int layers)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setLayers

    Parameters
    ----------

    layers : int
      Passed on as it is.
    """
    #  void QOpenGLTexture::setLayers(int layers)
    self.uglySide.call('ritual_ZN14QOpenGLTexture9setLayersEi', layers)

  @overload(int)
  def setSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setSamples(int samples)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setSamples

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QOpenGLTexture::setSamples(int samples)
    self.uglySide.call('ritual_ZN14QOpenGLTexture10setSamplesEi', samples)

  @overload(bool)
  def setFixedSamplePositions(self, fixed: bool) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setFixedSamplePositions(bool fixed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setFixedSamplePositions

    Parameters
    ----------

    fixed : bool
      Passed on as it is.
    """
    #  void QOpenGLTexture::setFixedSamplePositions(bool fixed)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture23setFixedSamplePositionsEb', fixed,
    )

  @overload(QImage)
  @overload(QImage, MipMapGeneration)
  def setData(
      self,
      image: QImage,
      genMipMaps: MipMapGeneration = MipMapGeneration.GenerateMipMaps,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setData(const QImage &image,
    MipMapGeneration genMipMaps)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setData

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    genMipMaps : MipMapGeneration
      Passed on as its number. May be left out, as in Qt: it is then
      MipMapGeneration.GenerateMipMaps.
    """
    #  void QOpenGLTexture::setData(const QImage &image, MipMapGeneration
    #      genMipMaps)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture7setDataERK6QImageNS_16MipMapGenerationE',
        self._valueOf(image), genMipMaps.value,
    )

  @overload(int)
  def setMipBaseLevel(self, baseLevel: int) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMipBaseLevel(int baseLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setMipBaseLevel

    Parameters
    ----------

    baseLevel : int
      Passed on as it is.
    """
    #  void QOpenGLTexture::setMipBaseLevel(int baseLevel)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture15setMipBaseLevelEi', baseLevel,
    )

  @overload(int)
  def setMipMaxLevel(self, maxLevel: int) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMipMaxLevel(int maxLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setMipMaxLevel

    Parameters
    ----------

    maxLevel : int
      Passed on as it is.
    """
    #  void QOpenGLTexture::setMipMaxLevel(int maxLevel)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture14setMipMaxLevelEi', maxLevel,
    )

  @overload(int, int)
  def setMipLevelRange(self, baseLevel: int, maxLevel: int) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMipLevelRange(int baseLevel, int
    maxLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setMipLevelRange

    Parameters
    ----------

    baseLevel : int
      Passed on as it is.

    maxLevel : int
      Passed on as it is.
    """
    #  void QOpenGLTexture::setMipLevelRange(int baseLevel, int maxLevel)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture16setMipLevelRangeEii',
        baseLevel, maxLevel,
    )

  @overload(bool)
  def setAutoMipMapGenerationEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setAutoMipMapGenerationEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setAutoMipMapGenerationEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QOpenGLTexture::setAutoMipMapGenerationEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture30setAutoMipMapGenerationEnabledEb',
        enabled,
    )

  @overload(SwizzleComponent, SwizzleValue)
  def setSwizzleMask(
      self,
      component: SwizzleComponent,
      value: SwizzleValue,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setSwizzleMask(SwizzleComponent
    component, SwizzleValue value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setSwizzleMask

    Parameters
    ----------

    component : SwizzleComponent
      Passed on as its number.

    value : SwizzleValue
      Passed on as its number.
    """
    #  void QOpenGLTexture::setSwizzleMask(SwizzleComponent component,
    #      SwizzleValue value)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture14setSwizzleMaskENS_16SwizzleComponentENS'
        '_12SwizzleValueE',
        component.value, value.value,
    )

  @overload(SwizzleValue, SwizzleValue, SwizzleValue, SwizzleValue)
  def setSwizzleMask(
      self,
      r: SwizzleValue,
      g: SwizzleValue,
      b: SwizzleValue,
      a: SwizzleValue,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setSwizzleMask(SwizzleValue r,
    SwizzleValue g, SwizzleValue b, SwizzleValue a)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setSwizzleMask

    Parameters
    ----------

    r : SwizzleValue
      Passed on as its number.

    g : SwizzleValue
      Passed on as its number.

    b : SwizzleValue
      Passed on as its number.

    a : SwizzleValue
      Passed on as its number.
    """
    #  void QOpenGLTexture::setSwizzleMask(SwizzleValue r, SwizzleValue g,
    #      SwizzleValue b, SwizzleValue a)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture14setSwizzleMaskENS_12SwizzleValueES0_S0_'
        'S0_',
        r.value, g.value, b.value, a.value,
    )

  @overload(DepthStencilMode)
  def setDepthStencilMode(self, mode: DepthStencilMode) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setDepthStencilMode(DepthStencilMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setDepthStencilMode

    Parameters
    ----------

    mode : DepthStencilMode
      Passed on as its number.
    """
    #  void QOpenGLTexture::setDepthStencilMode(DepthStencilMode mode)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture19setDepthStencilModeENS_16DepthStencilMo'
        'deE',
        mode.value,
    )

  @overload(ComparisonFunction)
  def setComparisonFunction(self, function: ComparisonFunction) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setComparisonFunction(ComparisonFunction
    function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setComparisonFunction

    Parameters
    ----------

    function : ComparisonFunction
      Passed on as its number.
    """
    #  void QOpenGLTexture::setComparisonFunction(ComparisonFunction
    #      function)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture21setComparisonFunctionENS_18ComparisonFu'
        'nctionE',
        function.value,
    )

  @overload(ComparisonMode)
  def setComparisonMode(self, mode: ComparisonMode) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setComparisonMode(ComparisonMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setComparisonMode

    Parameters
    ----------

    mode : ComparisonMode
      Passed on as its number.
    """
    #  void QOpenGLTexture::setComparisonMode(ComparisonMode mode)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture17setComparisonModeENS_14ComparisonModeE',
        mode.value,
    )

  @overload(Filter)
  def setMinificationFilter(self, filter: Filter) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMinificationFilter(Filter filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setMinificationFilter

    Parameters
    ----------

    filter : Filter
      Passed on as its number.
    """
    #  void QOpenGLTexture::setMinificationFilter(Filter filter)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture21setMinificationFilterENS_6FilterE',
        filter.value,
    )

  @overload(Filter)
  def setMagnificationFilter(self, filter: Filter) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMagnificationFilter(Filter filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setMagnificationFilter

    Parameters
    ----------

    filter : Filter
      Passed on as its number.
    """
    #  void QOpenGLTexture::setMagnificationFilter(Filter filter)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture22setMagnificationFilterENS_6FilterE',
        filter.value,
    )

  @overload(Filter, Filter)
  def setMinMagFilters(
      self,
      minificationFilter: Filter,
      magnificationFilter: Filter,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMinMagFilters(Filter
    minificationFilter, Filter magnificationFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setMinMagFilters

    Parameters
    ----------

    minificationFilter : Filter
      Passed on as its number.

    magnificationFilter : Filter
      Passed on as its number.
    """
    #  void QOpenGLTexture::setMinMagFilters(Filter minificationFilter,
    #      Filter magnificationFilter)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture16setMinMagFiltersENS_6FilterES0_',
        minificationFilter.value, magnificationFilter.value,
    )

  @overload(float)
  def setMaximumAnisotropy(self, anisotropy: float) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMaximumAnisotropy(float anisotropy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setMaximumAnisotropy

    Parameters
    ----------

    anisotropy : float
      Passed on as it is.
    """
    #  void QOpenGLTexture::setMaximumAnisotropy(float anisotropy)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture20setMaximumAnisotropyEf', anisotropy,
    )

  @overload(WrapMode)
  def setWrapMode(self, mode: WrapMode) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setWrapMode(WrapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setWrapMode

    Parameters
    ----------

    mode : WrapMode
      Passed on as its number.
    """
    #  void QOpenGLTexture::setWrapMode(WrapMode mode)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture11setWrapModeENS_8WrapModeE', mode.value,
    )

  @overload(CoordinateDirection, WrapMode)
  def setWrapMode(
      self,
      direction: CoordinateDirection,
      mode: WrapMode,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setWrapMode(CoordinateDirection
    direction, WrapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setWrapMode

    Parameters
    ----------

    direction : CoordinateDirection
      Passed on as its number.

    mode : WrapMode
      Passed on as its number.
    """
    #  void QOpenGLTexture::setWrapMode(CoordinateDirection direction,
    #      WrapMode mode)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture11setWrapModeENS_19CoordinateDirectionENS'
        '_8WrapModeE',
        direction.value, mode.value,
    )

  @overload(QColor)
  def setBorderColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setBorderColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setBorderColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QOpenGLTexture::setBorderColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture14setBorderColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float, float, float, float)
  def setBorderColor(self, r: float, g: float, b: float, a: float) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setBorderColor(float r, float g, float
    b, float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setBorderColor

    Parameters
    ----------

    r : float
      Passed on as it is.

    g : float
      Passed on as it is.

    b : float
      Passed on as it is.

    a : float
      Passed on as it is.
    """
    #  void QOpenGLTexture::setBorderColor(float r, float g, float b, float
    #      a)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture14setBorderColorEffff', r, g, b, a,
    )

  @overload(int, int, int, int)
  def setBorderColor(self, r: int, g: int, b: int, a: int) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setBorderColor(int r, int g, int b, int
    a)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#setBorderColor

    Parameters
    ----------

    r : int
      Passed on as it is.

    g : int
      Passed on as it is.

    b : int
      Passed on as it is.

    a : int
      Passed on as it is.
    """
    #  void QOpenGLTexture::setBorderColor(int r, int g, int b, int a)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture14setBorderColorEiiii', r, g, b, a,
    )

  @overload(float)
  def setMinimumLevelOfDetail(self, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMinimumLevelOfDetail(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setMinimumLevelOfDetail

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QOpenGLTexture::setMinimumLevelOfDetail(float value)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture23setMinimumLevelOfDetailEf', value,
    )

  @overload(float)
  def setMaximumLevelOfDetail(self, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setMaximumLevelOfDetail(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setMaximumLevelOfDetail

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QOpenGLTexture::setMaximumLevelOfDetail(float value)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture23setMaximumLevelOfDetailEf', value,
    )

  @overload(float, float)
  def setLevelOfDetailRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setLevelOfDetailRange(float min, float
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setLevelOfDetailRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QOpenGLTexture::setLevelOfDetailRange(float min, float max)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture21setLevelOfDetailRangeEff', min, max,
    )

  @overload(float)
  def setLevelofDetailBias(self, bias: float) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::setLevelofDetailBias(float bias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#setLevelofDetailBias

    Parameters
    ----------

    bias : float
      Passed on as it is.
    """
    #  void QOpenGLTexture::setLevelofDetailBias(float bias)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture20setLevelofDetailBiasEf', bias,
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

  @overload(Target)
  def __init__(self, target: Target) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLTexture::QOpenGLTexture(Target
    target)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#QOpenGLTexture

    Parameters
    ----------

    target : Target
      Passed on as its number.
    """
    #  QOpenGLTexture::QOpenGLTexture(Target target)
    self._noteCreation(QOpenGLTexture, lambda: Rituals.call(
        'ritual_ZN14QOpenGLTextureC1ENS_6TargetE', target.value,
    ))

  @overload(QImage)
  @overload(QImage, MipMapGeneration)
  def __init__(
      self,
      image: QImage,
      genMipMaps: MipMapGeneration = MipMapGeneration.GenerateMipMaps,
  ) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLTexture::QOpenGLTexture(const
    QImage &image, MipMapGeneration genMipMaps)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#QOpenGLTexture

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    genMipMaps : MipMapGeneration
      Passed on as its number. May be left out, as in Qt: it is then
      MipMapGeneration.GenerateMipMaps.
    """
    #  QOpenGLTexture::QOpenGLTexture(const QImage &image, MipMapGeneration
    #      genMipMaps)
    self._noteCreation(QOpenGLTexture, lambda: Rituals.call(
        'ritual_ZN14QOpenGLTextureC1ERK6QImageNS_16MipMapGenerationE',
        self._valueOf(image), genMipMaps.value,
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTexture::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#create
    """
    #  bool QOpenGLTexture::create()
    return self.uglySide.call('ritual_ZN14QOpenGLTexture6createEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#destroy
    """
    #  void QOpenGLTexture::destroy()
    self.uglySide.call('ritual_ZN14QOpenGLTexture7destroyEv')

  @overload()
  def bind(self) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::bind()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#bind
    """
    #  void QOpenGLTexture::bind()
    self.uglySide.call('ritual_ZN14QOpenGLTexture4bindEv')

  @overload(int)
  @overload(int, TextureUnitReset)
  def bind(
      self,
      unit: int,
      reset: TextureUnitReset = TextureUnitReset.DontResetTextureUnit,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::bind(uint unit, TextureUnitReset
    reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#bind

    Parameters
    ----------

    unit : int
      Passed on as it is.

    reset : TextureUnitReset
      Passed on as its number. May be left out, as in Qt: it is then
      TextureUnitReset.DontResetTextureUnit.
    """
    #  void QOpenGLTexture::bind(uint unit, TextureUnitReset reset)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture4bindEjNS_16TextureUnitResetE',
        unit, reset.value,
    )

  @overload()
  def release(self) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::release()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#release
    """
    #  void QOpenGLTexture::release()
    self.uglySide.call('ritual_ZN14QOpenGLTexture7releaseEv')

  @overload(int)
  @overload(int, TextureUnitReset)
  def release(
      self,
      unit: int,
      reset: TextureUnitReset = TextureUnitReset.DontResetTextureUnit,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::release(uint unit, TextureUnitReset
    reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#release

    Parameters
    ----------

    unit : int
      Passed on as it is.

    reset : TextureUnitReset
      Passed on as its number. May be left out, as in Qt: it is then
      TextureUnitReset.DontResetTextureUnit.
    """
    #  void QOpenGLTexture::release(uint unit, TextureUnitReset reset)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture7releaseEjNS_16TextureUnitResetE',
        unit, reset.value,
    )

  @overload()
  def allocateStorage(self) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::allocateStorage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#allocateStorage
    """
    #  void QOpenGLTexture::allocateStorage()
    self.uglySide.call('ritual_ZN14QOpenGLTexture15allocateStorageEv')

  @overload(PixelFormat, PixelType)
  def allocateStorage(
      self,
      pixelFormat: PixelFormat,
      pixelType: PixelType,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::allocateStorage(PixelFormat pixelFormat,
    PixelType pixelType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#allocateStorage

    Parameters
    ----------

    pixelFormat : PixelFormat
      Passed on as its number.

    pixelType : PixelType
      Passed on as its number.
    """
    #  void QOpenGLTexture::allocateStorage(PixelFormat pixelFormat,
    #      PixelType pixelType)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture15allocateStorageENS_11PixelFormatENS_9Pi'
        'xelTypeE',
        pixelFormat.value, pixelType.value,
    )

  @overload()
  def generateMipMaps(self) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::generateMipMaps()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#generateMipMaps
    """
    #  void QOpenGLTexture::generateMipMaps()
    self.uglySide.call('ritual_ZN14QOpenGLTexture15generateMipMapsEv')

  @overload(int)
  @overload(int, bool)
  def generateMipMaps(
      self,
      baseLevel: int,
      resetBaseLevel: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTexture::generateMipMaps(int baseLevel, bool
    resetBaseLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexture.html#generateMipMaps

    Parameters
    ----------

    baseLevel : int
      Passed on as it is.

    resetBaseLevel : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QOpenGLTexture::generateMipMaps(int baseLevel, bool
    #      resetBaseLevel)
    self.uglySide.call(
        'ritual_ZN14QOpenGLTexture15generateMipMapsEib',
        baseLevel, resetBaseLevel,
    )

  def d_func(self) -> Optional[QOpenGLTexturePrivate]:
    """
    Calls Qt's 'QOpenGLTexturePrivate *QOpenGLTexture::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltexture.html#d_func

    Returns
    -------

    Optional[QOpenGLTexturePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLTexturePrivate *QOpenGLTexture::d_func()
    address = self.uglySide.call('ritual_ZN14QOpenGLTexture6d_funcEv')
    from . import QOpenGLTexturePrivate
    return QOpenGLTexturePrivate._cuteAt(address)

  @staticmethod
  def levelOfDetailRange(*__, **_) -> Never:
    """
    Qt's 'std::pair<float, float> QOpenGLTexture::levelOfDetailRange()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLTexture.levelOfDetailRange' has no cute function yet. Qt's "
        "'std::pair<float, float> QOpenGLTexture::levelOfDetailRange() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def minMagFilters(*__, **_) -> Never:
    """
    Qt's 'std::pair<Filter, Filter> QOpenGLTexture::minMagFilters() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLTexture.minMagFilters' has no cute function yet. Qt's "
        "'std::pair<Filter, Filter> QOpenGLTexture::minMagFilters() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def mipLevelRange(*__, **_) -> Never:
    """
    Qt's 'std::pair<int, int> QOpenGLTexture::mipLevelRange() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLTexture.mipLevelRange' has no cute function yet. Qt's "
        "'std::pair<int, int> QOpenGLTexture::mipLevelRange() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def setCompressedData(*__, **_) -> Never:
    """
    - Qt's 'void QOpenGLTexture::setCompressedData(int mipLevel, int layer,
      CubeMapFace cubeFace, int dataSize, const void *data, const
      QOpenGLPixelTransferOptions *const options)': names 'void', which has
      no cute class yet.
    - Qt's 'void QOpenGLTexture::setCompressedData(int mipLevel, int layer,
      int layerCount, CubeMapFace cubeFace, int dataSize, const void *data,
      const QOpenGLPixelTransferOptions *const options)': names 'void', which
      has no cute class yet.
    - Qt's 'void QOpenGLTexture::setCompressedData(int mipLevel, int layer,
      int dataSize, const void *data, const QOpenGLPixelTransferOptions
      *const options)': names 'void', which has no cute class yet.
    - Qt's 'void QOpenGLTexture::setCompressedData(int mipLevel, int
      dataSize, const void *data, const QOpenGLPixelTransferOptions *const
      options)': names 'void', which has no cute class yet.
    - Qt's 'void QOpenGLTexture::setCompressedData(int dataSize, const void
      *data, const QOpenGLPixelTransferOptions *const options)': names
      'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTexture.setCompressedData' has no cute function yet. Qt's "
        "'void QOpenGLTexture::setCompressedData(int mipLevel, int layer, "
        "CubeMapFace cubeFace, int dataSize, const void *data, const "
        "QOpenGLPixelTransferOptions *const options)': names 'void', which "
        "has no cute class yet. Qt's 'void "
        "QOpenGLTexture::setCompressedData(int mipLevel, int layer, int "
        "layerCount, CubeMapFace cubeFace, int dataSize, const void *data, "
        "const QOpenGLPixelTransferOptions *const options)': names 'void', "
        "which has no cute class yet. Qt's 'void "
        "QOpenGLTexture::setCompressedData(int mipLevel, int layer, int "
        "dataSize, const void *data, const QOpenGLPixelTransferOptions "
        "*const options)': names 'void', which has no cute class yet. Qt's "
        "'void QOpenGLTexture::setCompressedData(int mipLevel, int "
        "dataSize, const void *data, const QOpenGLPixelTransferOptions "
        "*const options)': names 'void', which has no cute class yet. Qt's "
        "'void QOpenGLTexture::setCompressedData(int dataSize, const void "
        "*data, const QOpenGLPixelTransferOptions *const options)': names "
        "'void', which has no cute class yet.")
