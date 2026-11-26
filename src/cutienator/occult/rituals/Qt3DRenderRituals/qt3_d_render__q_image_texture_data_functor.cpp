//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qtextureimage_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qtextureimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qtextureimage.h>
#include <Qt3DRender/qabstracttextureimage.h>
#include <Qt3DRender/private/qtextureimage_p.h>
#include <Qt3DRender/private/qtextureimagedata_p.h>
#include <Qt3DRender/qtexturedata.h>
#include <Qt3DRender/qtexture.h>
#include <Qt3DRender/private/qtexture_p.h>
#include <QtCore/QFileInfo>
#if QT_CONFIG(mimetype)
#include <QtCore/QMimeDatabase>
#include <QtCore/QMimeType>
#endif
#include <QtCore/QBuffer>
#include <QtCore/qendian.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/qaspectengine.h>
#include <Qt3DCore/private/qdownloadhelperservice_p.h>
#include <Qt3DCore/private/qurlhelper_p.h>
#include <Qt3DRender/private/qrenderaspect_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/texture_p.h>
#include <QtCore/qmath.h>
#include <Qt3DRender/qtextureimage.h>
#include <Qt3DRender/private/qtextureimage_p.h>
#include <Qt3DRender/private/qtexture_p.h>
#include <Qt3DRender/private/qabstracttextureimage_p.h>
#include <QtCore/QFileInfo>
#include <QtCore/QDateTime>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/texture/qtexture.cpp, line 34, as local:qtexture.cpp:DdsPixelFormat
namespace Qt3DRender {
namespace {
struct DdsPixelFormat
{
    quint32 size;
    quint32 flags;
    quint32 fourCC;
    quint32 rgbBitCount;
    quint32 redMask;
    quint32 greenMask;
    quint32 blueMask;
    quint32 alphaMask;
};
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 46, as local:qtexture.cpp:DdsHeader
namespace Qt3DRender {
namespace {
struct DdsHeader
{
    char magic[4];
    quint32 size;
    quint32 flags;
    quint32 height;
    quint32 width;
    quint32 pitchOrLinearSize;
    quint32 depth;
    quint32 mipmapCount;
    quint32 reserved[11];
    DdsPixelFormat pixelFormat;
    quint32 caps;
    quint32 caps2;
    quint32 caps3;
    quint32 caps4;
    quint32 reserved2;
};
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 65, as local:qtexture.cpp:DdsDX10Header
namespace Qt3DRender {
namespace {
struct DdsDX10Header
{
    quint32 format;
    quint32 dimension;
    quint32 miscFlag;
    quint32 arraySize;
    quint32 miscFlags2;
};
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 79, as local:qtexture.cpp:FourCCFlag
namespace Qt3DRender {
namespace {
enum PixelFormatFlag
{
    AlphaFlag                   = 0x1,
    FourCCFlag                  = 0x4,
    RGBFlag                     = 0x40,
    RGBAFlag                    = RGBFlag | AlphaFlag,
    YUVFlag                     = 0x200,
    LuminanceFlag               = 0x20000
};
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 107, as local:qtexture.cpp:DXGIFormat
namespace Qt3DRender {
namespace {
enum DXGIFormat
{
    DXGI_FORMAT_UNKNOWN                     = 0,
    DXGI_FORMAT_R32G32B32A32_TYPELESS       = 1,
    DXGI_FORMAT_R32G32B32A32_FLOAT          = 2,
    DXGI_FORMAT_R32G32B32A32_UINT           = 3,
    DXGI_FORMAT_R32G32B32A32_SINT           = 4,
    DXGI_FORMAT_R32G32B32_TYPELESS          = 5,
    DXGI_FORMAT_R32G32B32_FLOAT             = 6,
    DXGI_FORMAT_R32G32B32_UINT              = 7,
    DXGI_FORMAT_R32G32B32_SINT              = 8,
    DXGI_FORMAT_R16G16B16A16_TYPELESS       = 9,
    DXGI_FORMAT_R16G16B16A16_FLOAT          = 10,
    DXGI_FORMAT_R16G16B16A16_UNORM          = 11,
    DXGI_FORMAT_R16G16B16A16_UINT           = 12,
    DXGI_FORMAT_R16G16B16A16_SNORM          = 13,
    DXGI_FORMAT_R16G16B16A16_SINT           = 14,
    DXGI_FORMAT_R32G32_TYPELESS             = 15,
    DXGI_FORMAT_R32G32_FLOAT                = 16,
    DXGI_FORMAT_R32G32_UINT                 = 17,
    DXGI_FORMAT_R32G32_SINT                 = 18,
    DXGI_FORMAT_R32G8X24_TYPELESS           = 19,
    DXGI_FORMAT_D32_FLOAT_S8X24_UINT        = 20,
    DXGI_FORMAT_R32_FLOAT_X8X24_TYPELESS    = 21,
    DXGI_FORMAT_X32_TYPELESS_G8X24_UINT     = 22,
    DXGI_FORMAT_R10G10B10A2_TYPELESS        = 23,
    DXGI_FORMAT_R10G10B10A2_UNORM           = 24,
    DXGI_FORMAT_R10G10B10A2_UINT            = 25,
    DXGI_FORMAT_R11G11B10_FLOAT             = 26,
    DXGI_FORMAT_R8G8B8A8_TYPELESS           = 27,
    DXGI_FORMAT_R8G8B8A8_UNORM              = 28,
    DXGI_FORMAT_R8G8B8A8_UNORM_SRGB         = 29,
    DXGI_FORMAT_R8G8B8A8_UINT               = 30,
    DXGI_FORMAT_R8G8B8A8_SNORM              = 31,
    DXGI_FORMAT_R8G8B8A8_SINT               = 32,
    DXGI_FORMAT_R16G16_TYPELESS             = 33,
    DXGI_FORMAT_R16G16_FLOAT                = 34,
    DXGI_FORMAT_R16G16_UNORM                = 35,
    DXGI_FORMAT_R16G16_UINT                 = 36,
    DXGI_FORMAT_R16G16_SNORM                = 37,
    DXGI_FORMAT_R16G16_SINT                 = 38,
    DXGI_FORMAT_R32_TYPELESS                = 39,
    DXGI_FORMAT_D32_FLOAT                   = 40,
    DXGI_FORMAT_R32_FLOAT                   = 41,
    DXGI_FORMAT_R32_UINT                    = 42,
    DXGI_FORMAT_R32_SINT                    = 43,
    DXGI_FORMAT_R24G8_TYPELESS              = 44,
    DXGI_FORMAT_D24_UNORM_S8_UINT           = 45,
    DXGI_FORMAT_R24_UNORM_X8_TYPELESS       = 46,
    DXGI_FORMAT_X24_TYPELESS_G8_UINT        = 47,
    DXGI_FORMAT_R8G8_TYPELESS               = 48,
    DXGI_FORMAT_R8G8_UNORM                  = 49,
    DXGI_FORMAT_R8G8_UINT                   = 50,
    DXGI_FORMAT_R8G8_SNORM                  = 51,
    DXGI_FORMAT_R8G8_SINT                   = 52,
    DXGI_FORMAT_R16_TYPELESS                = 53,
    DXGI_FORMAT_R16_FLOAT                   = 54,
    DXGI_FORMAT_D16_UNORM                   = 55,
    DXGI_FORMAT_R16_UNORM                   = 56,
    DXGI_FORMAT_R16_UINT                    = 57,
    DXGI_FORMAT_R16_SNORM                   = 58,
    DXGI_FORMAT_R16_SINT                    = 59,
    DXGI_FORMAT_R8_TYPELESS                 = 60,
    DXGI_FORMAT_R8_UNORM                    = 61,
    DXGI_FORMAT_R8_UINT                     = 62,
    DXGI_FORMAT_R8_SNORM                    = 63,
    DXGI_FORMAT_R8_SINT                     = 64,
    DXGI_FORMAT_A8_UNORM                    = 65,
    DXGI_FORMAT_R1_UNORM                    = 66,
    DXGI_FORMAT_R9G9B9E5_SHAREDEXP          = 67,
    DXGI_FORMAT_R8G8_B8G8_UNORM             = 68,
    DXGI_FORMAT_G8R8_G8B8_UNORM             = 69,
    DXGI_FORMAT_BC1_TYPELESS                = 70,
    DXGI_FORMAT_BC1_UNORM                   = 71,
    DXGI_FORMAT_BC1_UNORM_SRGB              = 72,
    DXGI_FORMAT_BC2_TYPELESS                = 73,
    DXGI_FORMAT_BC2_UNORM                   = 74,
    DXGI_FORMAT_BC2_UNORM_SRGB              = 75,
    DXGI_FORMAT_BC3_TYPELESS                = 76,
    DXGI_FORMAT_BC3_UNORM                   = 77,
    DXGI_FORMAT_BC3_UNORM_SRGB              = 78,
    DXGI_FORMAT_BC4_TYPELESS                = 79,
    DXGI_FORMAT_BC4_UNORM                   = 80,
    DXGI_FORMAT_BC4_SNORM                   = 81,
    DXGI_FORMAT_BC5_TYPELESS                = 82,
    DXGI_FORMAT_BC5_UNORM                   = 83,
    DXGI_FORMAT_BC5_SNORM                   = 84,
    DXGI_FORMAT_B5G6R5_UNORM                = 85,
    DXGI_FORMAT_B5G5R5A1_UNORM              = 86,
    DXGI_FORMAT_B8G8R8A8_UNORM              = 87,
    DXGI_FORMAT_B8G8R8X8_UNORM              = 88,
    DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM  = 89,
    DXGI_FORMAT_B8G8R8A8_TYPELESS           = 90,
    DXGI_FORMAT_B8G8R8A8_UNORM_SRGB         = 91,
    DXGI_FORMAT_B8G8R8X8_TYPELESS           = 92,
    DXGI_FORMAT_B8G8R8X8_UNORM_SRGB         = 93,
    DXGI_FORMAT_BC6H_TYPELESS               = 94,
    DXGI_FORMAT_BC6H_UF16                   = 95,
    DXGI_FORMAT_BC6H_SF16                   = 96,
    DXGI_FORMAT_BC7_TYPELESS                = 97,
    DXGI_FORMAT_BC7_UNORM                   = 98,
    DXGI_FORMAT_BC7_UNORM_SRGB              = 99,
    DXGI_FORMAT_AYUV                        = 100,
    DXGI_FORMAT_Y410                        = 101,
    DXGI_FORMAT_Y416                        = 102,
    DXGI_FORMAT_NV12                        = 103,
    DXGI_FORMAT_P010                        = 104,
    DXGI_FORMAT_P016                        = 105,
    DXGI_FORMAT_420_OPAQUE                  = 106,
    DXGI_FORMAT_YUY2                        = 107,
    DXGI_FORMAT_Y210                        = 108,
    DXGI_FORMAT_Y216                        = 109,
    DXGI_FORMAT_NV11                        = 110,
    DXGI_FORMAT_AI44                        = 111,
    DXGI_FORMAT_IA44                        = 112,
    DXGI_FORMAT_P8                          = 113,
    DXGI_FORMAT_A8P8                        = 114,
    DXGI_FORMAT_B4G4R4A4_UNORM              = 115,
    DXGI_FORMAT_P208                        = 130,
    DXGI_FORMAT_V208                        = 131,
    DXGI_FORMAT_V408                        = 132,
};
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 230, as local:qtexture.cpp:DdsFourCC
namespace Qt3DRender {
namespace {
template <int a, int b, int c, int d>
struct DdsFourCC
{
    static const quint32 value = a | (b << 8) | (c << 16) | (d << 24);
};
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 236, as local:qtexture.cpp:FormatInfo
namespace Qt3DRender {
namespace {
struct FormatInfo
{
    QOpenGLTexture::PixelFormat pixelFormat;
    QOpenGLTexture::TextureFormat textureFormat;
    QOpenGLTexture::PixelType pixelType;
    int components;
    bool compressed;
};
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 406, as local:qtexture.cpp:PkmHeader
namespace Qt3DRender {
namespace {
struct PkmHeader
{
    char magic[4];
    char version[2];
    quint16 textureType;
    quint16 paddedWidth;
    quint16 paddedHeight;
    quint16 width;
    quint16 height;
};
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 417, as local:qtexture.cpp:ImageFormat
namespace Qt3DRender {
namespace {
enum ImageFormat {
    GenericImageFormat = 0,
    DDS,
    PKM,
    HDR,
    KTX
};
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 425, as local:qtexture.cpp:imageFormatFromSuffix
namespace Qt3DRender {
namespace {
inline ImageFormat imageFormatFromSuffix(const QString &suffix)
{
    if (suffix == QStringLiteral("pkm"))
        return PKM;
    if (suffix == QStringLiteral("dds"))
        return DDS;
    if (suffix == QStringLiteral("hdr"))
        return HDR;
    if (suffix == QStringLiteral("ktx"))
        return KTX;
    return GenericImageFormat;
}
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 440, as local:qtexture.cpp:blockSizeForTextureFormat
namespace Qt3DRender {
namespace {
inline quint32 blockSizeForTextureFormat(QOpenGLTexture::TextureFormat format)
{
    switch (format) {
    case QOpenGLTexture::RGB8_ETC1:
    case QOpenGLTexture::RGB8_ETC2:
    case QOpenGLTexture::SRGB8_ETC2:
    case QOpenGLTexture::RGB8_PunchThrough_Alpha1_ETC2:
    case QOpenGLTexture::SRGB8_PunchThrough_Alpha1_ETC2:
    case QOpenGLTexture::R11_EAC_UNorm:
    case QOpenGLTexture::R11_EAC_SNorm:
    case QOpenGLTexture::RGB_DXT1:
        return 8;

    default:
        return 16;
    }
}
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 458, as local:qtexture.cpp:setKtxFile
namespace Qt3DRender {
namespace {
inline QTextureImageDataPtr setKtxFile(QIODevice *source)
{
    static const int KTX_IDENTIFIER_LENGTH = 12;
    static const char ktxIdentifier[KTX_IDENTIFIER_LENGTH] = { '\xAB', 'K', 'T', 'X', ' ', '1', '1', '\xBB', '\r', '\n', '\x1A', '\n' };
    static const quint32 platformEndianIdentifier = 0x04030201;
    static const quint32 inversePlatformEndianIdentifier = 0x01020304;

    struct KTXHeader {
        quint8 identifier[KTX_IDENTIFIER_LENGTH];
        quint32 endianness;
        quint32 glType;
        quint32 glTypeSize;
        quint32 glFormat;
        quint32 glInternalFormat;
        quint32 glBaseInternalFormat;
        quint32 pixelWidth;
        quint32 pixelHeight;
        quint32 pixelDepth;
        quint32 numberOfArrayElements;
        quint32 numberOfFaces;
        quint32 numberOfMipmapLevels;
        quint32 bytesOfKeyValueData;
    };

    KTXHeader header;
    QTextureImageDataPtr imageData;
    if (source->read(reinterpret_cast<char *>(&header), sizeof(header)) != sizeof(header)
            || qstrncmp(reinterpret_cast<char *>(header.identifier), ktxIdentifier, KTX_IDENTIFIER_LENGTH) != 0
            || (header.endianness != platformEndianIdentifier && header.endianness != inversePlatformEndianIdentifier))
    {
        return imageData;
    }

    const bool isInverseEndian = (header.endianness == inversePlatformEndianIdentifier);
    auto decode = [isInverseEndian](quint32 val) {
        return isInverseEndian ? qbswap<quint32>(val) : val;
    };

    const bool isCompressed = decode(header.glType) == 0 && decode(header.glFormat) == 0 && decode(header.glTypeSize) == 1;
    if (!isCompressed) {
        qWarning("Uncompressed ktx texture data is not supported");
        return imageData;
    }

    if (decode(header.numberOfArrayElements) != 0) {
        qWarning("Array ktx textures not supported");
        return imageData;
    }

    if (decode(header.pixelDepth) != 0) {
        qWarning("Only 2D and cube ktx textures are supported");
        return imageData;
    }

    const int bytesToSkip = decode(header.bytesOfKeyValueData);
    if (source->read(bytesToSkip).size() != bytesToSkip) {
        qWarning("Unexpected end of ktx data");
        return imageData;
    }

    const int level0Width = decode(header.pixelWidth);
    const int level0Height = decode(header.pixelHeight);
    const int faceCount = decode(header.numberOfFaces);
    const int mipMapLevels = decode(header.numberOfMipmapLevels);
    const QOpenGLTexture::TextureFormat format = QOpenGLTexture::TextureFormat(decode(header.glInternalFormat));
    const int blockSize = blockSizeForTextureFormat(format);

    // now for each mipmap level we have (arrays and 3d textures not supported here)
    // uint32 imageSize
    // for each array element
    //   for each face
    //     for each z slice
    //       compressed data
    //     padding so that each face data starts at an offset that is a multiple of 4
    // padding so that each imageSize starts at an offset that is a multiple of 4

    // assumes no depth or uncompressed textures (per above)
    auto computeMipMapLevelSize = [&] (int level) {
        const int w = qMax(level0Width >> level, 1);
        const int h = qMax(level0Height >> level, 1);
        return ((w + 3) / 4) * ((h + 3) / 4) * blockSize;
    };

    int dataSize = 0;
    for (auto i = 0; i < mipMapLevels; ++i)
        dataSize += computeMipMapLevelSize(i) * faceCount + 4; // assumes a single layer (per above)

    const QByteArray rawData = source->read(dataSize);
    if (rawData.size() < dataSize) {
        qWarning() << "Unexpected end of data in" << source;
        return imageData;
    }

    if (!source->atEnd())
        qWarning() << "Unrecognized data in" << source;

    imageData = QTextureImageDataPtr::create();
    imageData->setTarget(faceCount == 6 ? QOpenGLTexture::TargetCubeMap : QOpenGLTexture::Target2D);
    imageData->setFormat(format);
    imageData->setWidth(level0Width);
    imageData->setHeight(level0Height);
    imageData->setLayers(1);
    imageData->setDepth(1);
    imageData->setFaces(faceCount);
    imageData->setMipLevels(mipMapLevels);
    imageData->setPixelFormat(QOpenGLTexture::NoSourceFormat);
    imageData->setPixelType(QOpenGLTexture::NoPixelType);
    imageData->setData(rawData, blockSize, true);
    QTextureImageDataPrivate::get(imageData.data())->m_isKtx = true; // see note in QTextureImageDataPrivate

    return imageData;
}
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 571, as local:qtexture.cpp:setPkmFile
namespace Qt3DRender {
namespace {
inline QTextureImageDataPtr setPkmFile(QIODevice *source)
{
    QTextureImageDataPtr imageData;

    PkmHeader header;
    if ((source->read(reinterpret_cast<char *>(&header), sizeof header) != sizeof header)
            || (qstrncmp(header.magic, "PKM ", 4) != 0))
        return imageData;

    QOpenGLTexture::TextureFormat format = QOpenGLTexture::NoFormat;
    int blockSize = 0;

    if (header.version[0] == '2' && header.version[1] == '0') {
        switch (qFromBigEndian(header.textureType)) {
        case 0:
            format = QOpenGLTexture::RGB8_ETC1;
            blockSize = 8;
            break;

        case 1:
            format = QOpenGLTexture::RGB8_ETC2;
            blockSize = 8;
            break;

        case 3:
            format = QOpenGLTexture::RGBA8_ETC2_EAC;
            blockSize = 16;
            break;

        case 4:
            format = QOpenGLTexture::RGB8_PunchThrough_Alpha1_ETC2;
            blockSize = 8;
            break;

        case 5:
            format = QOpenGLTexture::R11_EAC_UNorm;
            blockSize = 8;
            break;

        case 6:
            format = QOpenGLTexture::RG11_EAC_UNorm;
            blockSize = 16;
            break;

        case 7:
            format = QOpenGLTexture::R11_EAC_SNorm;
            blockSize = 8;
            break;

        case 8:
            format = QOpenGLTexture::RG11_EAC_SNorm;
            blockSize = 16;
            break;
        }
    } else {
        format = QOpenGLTexture::RGB8_ETC1;
        blockSize = 8;
    }

    if (format == QOpenGLTexture::NoFormat) {
        qWarning() << "Unrecognized compression format in" << source;
        return imageData;
    }

    // get the extended (multiple of 4) width and height
    const int width = qFromBigEndian(header.paddedWidth);
    const int height = qFromBigEndian(header.paddedHeight);

    const QByteArray data = source->readAll();
    if (data.size() != (width / 4) * (height / 4) * blockSize) {
        qWarning() << "Unexpected data size in" << source;
        return imageData;
    }

    imageData = QTextureImageDataPtr::create();
    imageData->setTarget(QOpenGLTexture::Target2D);
    imageData->setFormat(format);
    imageData->setWidth(width);
    imageData->setHeight(height);
    imageData->setLayers(1);
    imageData->setDepth(1);
    imageData->setFaces(1);
    imageData->setMipLevels(1);
    imageData->setPixelFormat(QOpenGLTexture::NoSourceFormat);
    imageData->setPixelType(QOpenGLTexture::NoPixelType);
    imageData->setData(data, blockSize, true);

    return imageData;
}
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 806, as local:qtexture.cpp:setHdrFile
namespace Qt3DRender {
namespace {
inline QTextureImageDataPtr setHdrFile(QIODevice *source)
{
    QTextureImageDataPtr imageData;
    char sig[256];
    source->read(sig, 11);
    if (strncmp(sig, "#?RADIANCE\n", 11))
        return imageData;

    QByteArray buf = source->readAll();
    const char *p = buf.constData();
    const char *pEnd = p + buf.size();

    // Process lines until the empty one.
    QByteArray line;
    while (p < pEnd) {
        char c = *p++;
        if (c == '\n') {
            if (line.isEmpty())
                break;
            if (line.startsWith(QByteArrayLiteral("FORMAT="))) {
                const QByteArray format = line.mid(7).trimmed();
                if (format != QByteArrayLiteral("32-bit_rle_rgbe")) {
                    qWarning("HDR format '%s' is not supported", format.constData());
                    return imageData;
                }
            }
            line.clear();
        } else {
            line.append(c);
        }
    }
    if (p == pEnd) {
        qWarning("Malformed HDR image data at property strings");
        return imageData;
    }

    // Get the resolution string.
    while (p < pEnd) {
        char c = *p++;
        if (c == '\n')
            break;
        line.append(c);
    }
    if (p == pEnd) {
        qWarning("Malformed HDR image data at resolution string");
        return imageData;
    }

    int w = 0, h = 0;
    // We only care about the standard orientation.
    if (!sscanf(line.constData(), "-Y %d +X %d", &h, &w)) {
        qWarning("Unsupported HDR resolution string '%s'", line.constData());
        return imageData;
    }
    if (w <= 0 || h <= 0) {
        qWarning("Invalid HDR resolution");
        return imageData;
    }

    const QOpenGLTexture::TextureFormat textureFormat = QOpenGLTexture::RGBA32F;
    const QOpenGLTexture::PixelFormat pixelFormat = QOpenGLTexture::RGBA;
    const QOpenGLTexture::PixelType pixelType = QOpenGLTexture::Float32;
    const int blockSize = 4 * sizeof(float);
    QByteArray data;
    data.resize(w * h * blockSize);

    typedef unsigned char RGBE[4];
    RGBE *scanline = new RGBE[w];

    for (int y = 0; y < h; ++y) {
        if (pEnd - p < 4) {
            qWarning("Unexpected end of HDR data");
            delete[] scanline;
            return imageData;
        }

        scanline[0][0] = *p++;
        scanline[0][1] = *p++;
        scanline[0][2] = *p++;
        scanline[0][3] = *p++;

        if (scanline[0][0] == 2 && scanline[0][1] == 2 && scanline[0][2] < 128) {
            // new rle, the first pixel was a dummy
            for (int channel = 0; channel < 4; ++channel) {
                for (int x = 0; x < w && p < pEnd; ) {
                    unsigned char c = *p++;
                    if (c > 128) { // run
                        if (p < pEnd) {
                            int repCount = c & 127;
                            c = *p++;
                            while (repCount--)
                                scanline[x++][channel] = c;
                        }
                    } else { // not a run
                        while (c-- && p < pEnd)
                            scanline[x++][channel] = *p++;
                    }
                }
            }
        } else {
            // old rle
            scanline[0][0] = 2;
            int bitshift = 0;
            int x = 1;
            while (x < w && pEnd - p >= 4) {
                scanline[x][0] = *p++;
                scanline[x][1] = *p++;
                scanline[x][2] = *p++;
                scanline[x][3] = *p++;

                if (scanline[x][0] == 1 && scanline[x][1] == 1 && scanline[x][2] == 1) { // run
                    int repCount = scanline[x][3] << bitshift;
                    while (repCount--) {
                        memcpy(scanline[x], scanline[x - 1], 4);
                        ++x;
                    }
                    bitshift += 8;
                } else { // not a run
                    ++x;
                    bitshift = 0;
                }
            }
        }

        // adjust for -Y orientation
        float *fp = reinterpret_cast<float *>(data.data() + (h - 1 - y) * blockSize * w);
        for (int x = 0; x < w; ++x) {
            float d = qPow(2.0f, float(scanline[x][3]) - 128.0f);
            // r, g, b, a
            *fp++ = scanline[x][0] / 256.0f * d;
            *fp++ = scanline[x][1] / 256.0f * d;
            *fp++ = scanline[x][2] / 256.0f * d;
            *fp++ = 1.0f;
        }
    }

    delete[] scanline;

    imageData = QTextureImageDataPtr::create();
    imageData->setTarget(QOpenGLTexture::Target2D);
    imageData->setFormat(textureFormat);
    imageData->setWidth(w);
    imageData->setHeight(h);
    imageData->setLayers(1);
    imageData->setDepth(1);
    imageData->setFaces(1);
    imageData->setMipLevels(1);
    imageData->setPixelFormat(pixelFormat);
    imageData->setPixelType(pixelType);
    imageData->setData(data, blockSize, false);

    return imageData;
}
}  // namespace
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtexture.cpp, line 962, as _ZN10Qt3DRender20TextureLoadingHelper15loadTextureDataERK4QUrlbb
#if defined(Q_OS_LINUX)
namespace Qt3DRender {
inline QTextureImageDataPtr TextureLoadingHelper::loadTextureData(const QUrl &url, bool allow3D, bool mirrored)
{
    QTextureImageDataPtr textureData;
    if (url.isLocalFile() || url.scheme() == QLatin1String("qrc")
#ifdef Q_OS_ANDROID
            || url.scheme() == QLatin1String("assets")
#endif
            ) {
        const QString source = Qt3DCore::QUrlHelper::urlToLocalFileOrQrc(url);
        QFile f(source);
        if (!f.open(QIODevice::ReadOnly))
            qWarning() << "Failed to open" << source;
        else
            textureData = loadTextureData(&f, QFileInfo(source).suffix().toLower(), allow3D, mirrored);
    }
    return textureData;
}
}  // namespace Qt3DRender
#endif  // defined(Q_OS_LINUX)

//  from ../qt3d/src/render/texture/qtextureimage.cpp, line 261, as _ZNK10Qt3DRender24QImageTextureDataFunctoreqERKNS_26QTextureImageDataGeneratorE
namespace Qt3DRender {
inline bool QImageTextureDataFunctor::operator ==(const QTextureImageDataGenerator &other) const
{
    const QImageTextureDataFunctor *otherFunctor = functor_cast<QImageTextureDataFunctor>(&other);

    // if its the same URL, but different modification times, its not the same image.
    return (otherFunctor != nullptr &&
            otherFunctor->m_url == m_url &&
            otherFunctor->m_lastModified == m_lastModified &&
            otherFunctor->m_mirrored == m_mirrored);
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtextureimage.cpp, line 272, as _ZNK10Qt3DRender24QImageTextureDataFunctor3urlEv
namespace Qt3DRender {
inline QUrl QImageTextureDataFunctor::url() const
{
    return m_url;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/texture/qtextureimage.cpp, line 277, as _ZNK10Qt3DRender24QImageTextureDataFunctor10isMirroredEv
namespace Qt3DRender {
inline bool QImageTextureDataFunctor::isMirrored() const
{
    return m_mirrored;
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  bool Qt3DRender::QImageTextureDataFunctor::operator==(const
//      QTextureImageDataGenerator &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender24QImageTextureDataFunctoreqERKNS_26QTextureImageDataGeneratorE(
    const Qt3DRender::QImageTextureDataFunctor *self,
    const Qt3DRender::QTextureImageDataGenerator *other) {
  return self->operator==(*other);
}

//  QTextureImage::Status Qt3DRender::QImageTextureDataFunctor::status()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImage::Status ritual_ZNK10Qt3DRender24QImageTextureDataFunctor6statusEv(
    const Qt3DRender::QImageTextureDataFunctor *self) {
  return self->status();
}

//  qintptr Qt3DRender::QImageTextureDataFunctor::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK10Qt3DRender24QImageTextureDataFunctor2idEv(
    const Qt3DRender::QImageTextureDataFunctor *self) {
  return self->id();
}

//  QUrl Qt3DRender::QImageTextureDataFunctor::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender24QImageTextureDataFunctor3urlEv(
    const Qt3DRender::QImageTextureDataFunctor *self) {
  return new QUrl(self->url());
}

//  bool Qt3DRender::QImageTextureDataFunctor::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender24QImageTextureDataFunctor10isMirroredEv(
    const Qt3DRender::QImageTextureDataFunctor *self) {
  return self->isMirrored();
}

//  qintptr Qt3DRender::QImageTextureDataFunctor::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK10Qt3DRender24QImageTextureDataFunctor2idEv(
    const Qt3DRender::QImageTextureDataFunctor *self) {
  return self->Qt3DRender::QImageTextureDataFunctor::id();
}

//  a Qt3DRender::QTextureImageDataPtr a ritual of
//      Qt3DRender::QImageTextureDataFunctor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QImageTextureDataFunctor__Qt3DRender_QTextureImageDataPtr(
    Qt3DRender::QTextureImageDataPtr *self) {
  delete self;
}
