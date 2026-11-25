//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the line pulling in 'qrhivulkan_p.h'
//  stands also under '__has_include(<vulkan/vulkan.h>)', as Qt's
//  'qvulkaninstance.h' does, and the one pulling in 'qrhid3d12_p.h'
//  under '__has_include(<D3D12MemAlloc.h>)', a library Qt keeps in its
//  source and never installs, because neither header compiles without
//  its library and no ritual here needs either. Kept as it is when the
//  generator runs again.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhi_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QLoggingCategory>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtGui/private/qrhinull_p.h>
#ifndef QT_NO_OPENGL
#include <QtGui/private/qrhigles2_p.h>
#endif
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/private/qrhivulkan_p.h>
#endif
#ifdef Q_OS_WIN
#include <QtGui/private/qrhid3d11_p.h>
#if __has_include(<D3D12MemAlloc.h>)
#include <QtGui/private/qrhid3d12_p.h>
#endif
#endif
#if QT_CONFIG(metal)
#include <QtGui/private/qrhimetal_p.h>
#endif
#include <limits>
#include <memory>
#include <QtGui/private/qrhinull_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhi.cpp, line 8782, as _ZNK18QRhiImplementation17textureFormatInfoEN11QRhiTexture6FormatERK5QSizePjS5_S5_
inline bool QRhiImplementation::textureFormatInfo(QRhiTexture::Format format, const QSize &size,
                                           quint32 *bpl, quint32 *byteSize, quint32 *bytesPerPixel) const
{
    if (isCompressedFormat(format))
        return compressedFormatInfo(format, size, bpl, byteSize, nullptr);

    quint32 bpc = 0;
    switch (format) {
    case QRhiTexture::RGBA8:
        bpc = 4;
        break;
    case QRhiTexture::BGRA8:
        bpc = 4;
        break;
    case QRhiTexture::R8:
        bpc = 1;
        break;
    case QRhiTexture::RG8:
        bpc = 2;
        break;
    case QRhiTexture::R16:
        bpc = 2;
        break;
    case QRhiTexture::RG16:
        bpc = 4;
        break;
    case QRhiTexture::RED_OR_ALPHA8:
        bpc = 1;
        break;

    case QRhiTexture::RGBA16F:
        bpc = 8;
        break;
    case QRhiTexture::RGBA32F:
        bpc = 16;
        break;
    case QRhiTexture::R16F:
        bpc = 2;
        break;
    case QRhiTexture::R32F:
        bpc = 4;
        break;

    case QRhiTexture::RGB10A2:
        bpc = 4;
        break;

    case QRhiTexture::D16:
        bpc = 2;
        break;
    case QRhiTexture::D24:
    case QRhiTexture::D24S8:
    case QRhiTexture::D32F:
        bpc = 4;
        break;

    case QRhiTexture::D32FS8:
        bpc = 8;
        break;

    case QRhiTexture::R8SI:
    case QRhiTexture::R8UI:
        bpc = 1;
        break;
    case QRhiTexture::R32SI:
    case QRhiTexture::R32UI:
        bpc = 4;
        break;
    case QRhiTexture::RG32SI:
    case QRhiTexture::RG32UI:
        bpc = 8;
        break;
    case QRhiTexture::RGBA32SI:
    case QRhiTexture::RGBA32UI:
        bpc = 16;
        break;

    default:
        Q_UNREACHABLE();
        break;
    }

    const quint32 width = uint(qMax(0, size.width()));
    const quint32 height = uint(qMax(0, size.height()));

    if (bytesPerPixel)
        *bytesPerPixel = bpc;

    // Compute in 64-bit, as safety for extreme geometry that would not fit.
    const quint64 bytesPerLine = quint64(width) * quint64(bpc);
    const quint64 pixelCount = quint64(width) * quint64(height);
    if (bytesPerLine > std::numeric_limits<quint32>::max()
        || pixelCount > std::numeric_limits<quint32>::max() / bpc)
    {
        qWarning("Texture of size %dx%d with format %d has a byte size "
                 "which is too large to be handled",
                 size.width(), size.height(), int(format));
        if (bpl)
            *bpl = 0;
        if (byteSize)
            *byteSize = 0;
        return false;
    }

    if (bpl)
        *bpl = quint32(bytesPerLine);
    if (byteSize)
        *byteSize = quint32(pixelCount * quint64(bpc));

    return true;
}

//  from src/gui/rhi/qrhi.cpp, line 8635, as _ZNK18QRhiImplementation18isCompressedFormatEN11QRhiTexture6FormatE
inline bool QRhiImplementation::isCompressedFormat(QRhiTexture::Format format) const
{
    return (format >= QRhiTexture::BC1 && format <= QRhiTexture::BC7)
            || (format >= QRhiTexture::ETC2_RGB8 && format <= QRhiTexture::ETC2_RGBA8)
            || (format >= QRhiTexture::ASTC_4x4 && format <= QRhiTexture::ASTC_12x12);
}

//  from src/gui/rhi/qrhi.cpp, line 8642, as _ZNK18QRhiImplementation20compressedFormatInfoEN11QRhiTexture6FormatERK5QSizePjS5_PS2_
inline bool QRhiImplementation::compressedFormatInfo(QRhiTexture::Format format, const QSize &size,
                                              quint32 *bpl, quint32 *byteSize,
                                              QSize *blockDim) const
{
    int xdim = 4;
    int ydim = 4;
    quint32 blockSize = 0;

    switch (format) {
    case QRhiTexture::BC1:
        blockSize = 8;
        break;
    case QRhiTexture::BC2:
        blockSize = 16;
        break;
    case QRhiTexture::BC3:
        blockSize = 16;
        break;
    case QRhiTexture::BC4:
        blockSize = 8;
        break;
    case QRhiTexture::BC5:
        blockSize = 16;
        break;
    case QRhiTexture::BC6H:
        blockSize = 16;
        break;
    case QRhiTexture::BC7:
        blockSize = 16;
        break;

    case QRhiTexture::ETC2_RGB8:
        blockSize = 8;
        break;
    case QRhiTexture::ETC2_RGB8A1:
        blockSize = 8;
        break;
    case QRhiTexture::ETC2_RGBA8:
        blockSize = 16;
        break;

    case QRhiTexture::ASTC_4x4:
        blockSize = 16;
        break;
    case QRhiTexture::ASTC_5x4:
        blockSize = 16;
        xdim = 5;
        break;
    case QRhiTexture::ASTC_5x5:
        blockSize = 16;
        xdim = ydim = 5;
        break;
    case QRhiTexture::ASTC_6x5:
        blockSize = 16;
        xdim = 6;
        ydim = 5;
        break;
    case QRhiTexture::ASTC_6x6:
        blockSize = 16;
        xdim = ydim = 6;
        break;
    case QRhiTexture::ASTC_8x5:
        blockSize = 16;
        xdim = 8;
        ydim = 5;
        break;
    case QRhiTexture::ASTC_8x6:
        blockSize = 16;
        xdim = 8;
        ydim = 6;
        break;
    case QRhiTexture::ASTC_8x8:
        blockSize = 16;
        xdim = ydim = 8;
        break;
    case QRhiTexture::ASTC_10x5:
        blockSize = 16;
        xdim = 10;
        ydim = 5;
        break;
    case QRhiTexture::ASTC_10x6:
        blockSize = 16;
        xdim = 10;
        ydim = 6;
        break;
    case QRhiTexture::ASTC_10x8:
        blockSize = 16;
        xdim = 10;
        ydim = 8;
        break;
    case QRhiTexture::ASTC_10x10:
        blockSize = 16;
        xdim = ydim = 10;
        break;
    case QRhiTexture::ASTC_12x10:
        blockSize = 16;
        xdim = 12;
        ydim = 10;
        break;
    case QRhiTexture::ASTC_12x12:
        blockSize = 16;
        xdim = ydim = 12;
        break;

    default:
        Q_UNREACHABLE();
        break;
    }

    const quint32 wblocks = quint32((qint64(qMax(0, size.width())) + xdim - 1) / xdim);
    const quint32 hblocks = quint32((qint64(qMax(0, size.height())) + ydim - 1) / ydim);

    if (blockDim)
        *blockDim = QSize(xdim, ydim);

    // Compute in 64-bit, as safety for extreme geometry that would not fit.
    // wblocks and hblocks are at most 2^29 and blockSize at most 16.
    const quint64 bytesPerLine = quint64(wblocks) * quint64(blockSize);
    const quint64 totalSize = quint64(wblocks) * quint64(hblocks) * quint64(blockSize);
    if (bytesPerLine > std::numeric_limits<quint32>::max()
        || totalSize > std::numeric_limits<quint32>::max())
    {
        qWarning("Compressed texture of size %dx%d with format %d has a byte size of %llu "
                 "which is too large to be handled",
                 size.width(), size.height(), int(format), totalSize);
        if (bpl)
            *bpl = 0;
        if (byteSize)
            *byteSize = 0;
        return false;
    }

    if (bpl)
        *bpl = quint32(bytesPerLine);
    if (byteSize)
        *byteSize = quint32(totalSize);

    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 706, as _ZN12QNullTextureC1EP18QRhiImplementationN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS2_4FlagEE
inline QNullTexture::QNullTexture(QRhiImplementation *rhi, Format format, const QSize &pixelSize, int depth,
                           int arraySize, int sampleCount, Flags flags)
    : QRhiTexture(rhi, format, pixelSize, depth, arraySize, sampleCount, flags)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 712, as _ZN12QNullTextureD1Ev
inline QNullTexture::~QNullTexture()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 717, as _ZN12QNullTexture7destroyEv
inline void QNullTexture::destroy()
{
    valid = false;

    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 726, as _ZN12QNullTexture6createEv
inline bool QNullTexture::create()
{
    if (valid)
        destroy();

    valid = true;

    QRHI_RES_RHI(QRhiNull);
    const bool isCube = m_flags.testFlag(CubeMap);
    const bool is3D = m_flags.testFlag(ThreeDimensional);
    const bool isArray = m_flags.testFlag(TextureArray);
    const bool hasMipMaps = m_flags.testFlag(MipMapped);
    const bool is1D = m_flags.testFlags(OneDimensional);
    QSize size = is1D ? QSize(qMax(1, m_pixelSize.width()), 1)
                      : (m_pixelSize.isEmpty() ? QSize(1, 1) : m_pixelSize);
    const int mipLevelCount = hasMipMaps ? rhiD->q->mipLevelsForSize(size) : 1;
    const int layerCount = is3D ? qMax(1, m_depth)
                                : (isCube ? 6
                                          : (isArray ? qMax(0, m_arraySize)
                                                     : 1));

    if (!rhiD->textureFormatInfo(m_format, size, nullptr, nullptr, nullptr)) {
        valid = false;
        return false;
    }

    if (m_format == RGBA8) {
        image.resize(layerCount);
        for (int layer = 0; layer < layerCount; ++layer) {
            for (int level = 0; level < mipLevelCount; ++level) {
                image[layer][level] = QImage(rhiD->q->sizeForMipLevel(level, size),
                                             QImage::Format_RGBA8888_Premultiplied);
                image[layer][level].fill(Qt::yellow);
            }
        }
    }

    generation += 1;

    rhiD->registerResource(this);

    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 770, as _ZN12QNullTexture10createFromEN11QRhiTexture13NativeTextureE
inline bool QNullTexture::createFrom(QRhiTexture::NativeTexture src)
{
    Q_UNUSED(src);
    if (valid)
        destroy();

    valid = true;

    generation += 1;

    QRHI_RES_RHI(QRhiNull);
    rhiD->registerResource(this);

    return true;
}
//  -----------------------------------------------------------------------

//  A QNullTexture that Python can take functions over in. Every QNullTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullTextureCall0)(const void *, int *);
typedef bool (*CuteQNullTextureCall1)(const void *, int *);
typedef bool (*CuteQNullTextureCall2)(const void *, const QRhiTexture::NativeTexture *, int *);
typedef int (*CuteQNullTextureCall3)(const void *, int *);
typedef const QRhiTexture::NativeTexture * (*CuteQNullTextureCall4)(const void *, int *);
typedef void (*CuteQNullTextureCall5)(const void *, int, int *);
class CuteQNullTexture : public QNullTexture {
public:
  using QNullTexture::QNullTexture;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture10createFromENS_13NativeTextureE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture13nativeTextureEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture15setNativeLayoutEi")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void QNullTexture::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullTextureCall0 call = reinterpret_cast<CuteQNullTextureCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullTexture::destroy();
  }

  //  bool QNullTexture::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullTextureCall1 call = reinterpret_cast<CuteQNullTextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNullTexture::create();
  }

  //  bool QNullTexture::createFrom(NativeTexture src)
  bool createFrom(QRhiTexture::NativeTexture src) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullTextureCall2 call = reinterpret_cast<CuteQNullTextureCall2>(taken[2]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QNullTexture::createFrom(src);
  }

  //  QRhiResource::Type QRhiTexture::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNullTextureCall3 call = reinterpret_cast<CuteQNullTextureCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTexture::resourceType();
  }

  //  NativeTexture QRhiTexture::nativeTexture()
  QRhiTexture::NativeTexture nativeTexture() override {
    if (taken[4]) {
      int handled = 0;
      CuteQNullTextureCall4 call = reinterpret_cast<CuteQNullTextureCall4>(taken[4]);
      const QRhiTexture::NativeTexture * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiTexture::nativeTexture();
  }

  //  void QRhiTexture::setNativeLayout(int layout)
  void setNativeLayout(int layout) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNullTextureCall5 call = reinterpret_cast<CuteQNullTextureCall5>(taken[5]);
      call(this, layout, &handled);
      if (handled) return;
    }
    QRhiTexture::setNativeLayout(layout);
  }
};

//  QNullTexture::QNullTexture(QRhiImplementation *rhi, Format format, const
//      QSize &pixelSize, int depth, int arraySize, int sampleCount, Flags
//      flags)
extern "C" Q_DECL_EXPORT
QNullTexture *ritual_ZN12QNullTextureC1EP18QRhiImplementationN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS2_4FlagEE(
    QRhiImplementation *rhi,
    QRhiTexture::Format format,
    const QSize *pixelSize,
    int depth,
    int arraySize,
    int sampleCount,
    int flags) {
  return new CuteQNullTexture(
      rhi,
      format,
      *pixelSize,
      depth,
      arraySize,
      sampleCount,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  QNullTexture::~QNullTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNullTextureD1Ev(QNullTexture *self) {
  delete self;
}

//  void QNullTexture::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNullTexture7destroyEv(QNullTexture *self) {
  self->destroy();
}

//  bool QNullTexture::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QNullTexture6createEv(QNullTexture *self) {
  return self->create();
}

//  bool QNullTexture::createFrom(NativeTexture src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QNullTexture10createFromEN11QRhiTexture13NativeTextureE(
    QNullTexture *self,
    const QRhiTexture::NativeTexture *src) {
  return self->createFrom(*src);
}

//  a Python function taken by a CuteQNullTexture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullTexture(
    QNullTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullTexture *>(self)->take(key, call);
}

//  void QNullTexture::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QNullTexture7destroyEv(QNullTexture *self) {
  self->QNullTexture::destroy();
}

//  bool QNullTexture::create()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QNullTexture6createEv(QNullTexture *self) {
  return self->QNullTexture::create();
}

//  bool QNullTexture::createFrom(NativeTexture src)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QNullTexture10createFromEN11QRhiTexture13NativeTextureE(
    QNullTexture *self,
    const QRhiTexture::NativeTexture *src) {
  return self->QNullTexture::createFrom(*src);
}
