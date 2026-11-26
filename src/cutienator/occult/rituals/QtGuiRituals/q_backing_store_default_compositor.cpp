//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qbackingstoredefaultcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qbackingstoredefaultcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtGui/qimage.h>
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qbackingstoredefaultcompositor_p.h>
#include <QtGui/qtransform.h>
#include <QtGui/private/qmath_p.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpa/qplatformgraphicsbuffer.h>
#include <QtCore/qfile.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 144, as local:qbackingstoredefaultcompositor.cpp:scaledDirtyRegion
static QRegion scaledDirtyRegion(const QRegion &region, qreal factor, const QPoint &offset)
{
    if (offset.isNull() && factor <= 1)
        return region;

    QTransform xf = QTransform::fromScale(factor, factor);
    xf.translate(offset.x(), offset.y());
    return xf.map(region);
}

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 177, as local:qbackingstoredefaultcompositor.cpp:SourceTransformOrigin
enum class SourceTransformOrigin {
    BottomLeft,
    TopLeft
};

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 258, as local:qbackingstoredefaultcompositor.cpp:updateMatrix3x3
static void updateMatrix3x3(QRhiResourceUpdateBatch *resourceUpdates, QRhiBuffer *ubuf, const QMatrix3x3 &m)
{
    // mat3 is still 4 floats per column in the uniform buffer (but there is no
    // 4th column), so 48 bytes altogether, not 36 or 64.

    float f[12];
    const float *src = static_cast<const float *>(m.constData());
    float *dst = f;
    memcpy(dst, src, 3 * sizeof(float));
    memcpy(dst + 4, src + 3, 3 * sizeof(float));
    memcpy(dst + 8, src + 6, 3 * sizeof(float));

    resourceUpdates->updateDynamicBuffer(ubuf, 64, 48, f);
}

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 273, as local:qbackingstoredefaultcompositor.cpp:PipelineBlend
enum class PipelineBlend {
    None,
    Alpha,
    PremulAlpha
};

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 335, as local:qbackingstoredefaultcompositor.cpp:UBUF_SIZE
static const int UBUF_SIZE = 120;

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 16, as _ZN30QBackingStoreDefaultCompositorD1Ev
inline QBackingStoreDefaultCompositor::~QBackingStoreDefaultCompositor()
{
    reset();
}

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 21, as _ZN30QBackingStoreDefaultCompositor5resetEv
inline void QBackingStoreDefaultCompositor::reset()
{
    m_rhi = nullptr;
    m_psNoBlend.reset();
    m_psBlend.reset();
    m_psPremulBlend.reset();
    m_samplerNearest.reset();
    m_samplerLinear.reset();
    m_vbuf.reset();
    m_texture.reset();
    m_widgetQuadData.reset();
    for (PerQuadData &d : m_textureQuadData)
        d.reset();
}

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 36, as _ZNK30QBackingStoreDefaultCompositor9toTextureEPK21QPlatformBackingStoreP4QRhiP23QRhiResourceUpdateBatchRK7QRegionP6QFlagsINS0_11TextureFlagEE
inline QRhiTexture *QBackingStoreDefaultCompositor::toTexture(const QPlatformBackingStore *backingStore,
                                                       QRhi *rhi,
                                                       QRhiResourceUpdateBatch *resourceUpdates,
                                                       const QRegion &dirtyRegion,
                                                       QPlatformBackingStore::TextureFlags *flags) const
{
    return toTexture(backingStore->toImage(), rhi, resourceUpdates, dirtyRegion, flags);
}

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 45, as _ZNK30QBackingStoreDefaultCompositor9toTextureERK6QImageP4QRhiP23QRhiResourceUpdateBatchRK7QRegionP6QFlagsIN21QPlatformBackingStore11TextureFlagEE
inline QRhiTexture *QBackingStoreDefaultCompositor::toTexture(const QImage &sourceImage,
                                                       QRhi *rhi,
                                                       QRhiResourceUpdateBatch *resourceUpdates,
                                                       const QRegion &dirtyRegion,
                                                       QPlatformBackingStore::TextureFlags *flags) const
{
    Q_ASSERT(rhi);
    Q_ASSERT(resourceUpdates);
    Q_ASSERT(flags);

    if (!m_rhi) {
        m_rhi = rhi;
    } else if (m_rhi != rhi) {
        qWarning("QBackingStoreDefaultCompositor: the QRhi has changed unexpectedly, this should not happen");
        return nullptr;
    }

    QImage image = sourceImage;

    bool needsConversion = false;
    *flags = {};

    switch (image.format()) {
    case QImage::Format_ARGB32_Premultiplied:
        *flags |= QPlatformBackingStore::TexturePremultiplied;
        Q_FALLTHROUGH();
    case QImage::Format_RGB32:
    case QImage::Format_ARGB32:
        *flags |= QPlatformBackingStore::TextureSwizzle;
        break;
    case QImage::Format_RGBA8888_Premultiplied:
        *flags |= QPlatformBackingStore::TexturePremultiplied;
        Q_FALLTHROUGH();
    case QImage::Format_RGBX8888:
    case QImage::Format_RGBA8888:
        break;
    case QImage::Format_BGR30:
    case QImage::Format_A2BGR30_Premultiplied:
        // no fast path atm
        needsConversion = true;
        break;
    case QImage::Format_RGB30:
    case QImage::Format_A2RGB30_Premultiplied:
        // no fast path atm
        needsConversion = true;
        break;
    default:
        needsConversion = true;
        break;
    }

    if (image.size().isEmpty())
        return nullptr;

    const bool resized = !m_texture || m_texture->pixelSize() != image.size();
    if (dirtyRegion.isEmpty() && !resized)
        return m_texture.get();

    if (needsConversion)
        image = image.convertToFormat(QImage::Format_RGBA8888);
    else
        image.detach(); // if it was just wrapping data, that's no good, we need ownership, so detach

    if (resized) {
        if (!m_texture)
            m_texture.reset(rhi->newTexture(QRhiTexture::RGBA8, image.size()));
        else
            m_texture->setPixelSize(image.size());
        if (!m_texture->create()) {
            // Typically a lost device. Make sure to reset the null native resource
            qWarning("QBackingStoreDefaultCompositor: Failed to create backing store texture");
            m_texture.reset();
            return nullptr;
        }
        resourceUpdates->uploadTexture(m_texture.get(), image);
    } else {
        QRect imageRect = image.rect();
        QRect rect = dirtyRegion.boundingRect() & imageRect;
        QRhiTextureSubresourceUploadDescription subresDesc(image);
        subresDesc.setSourceTopLeft(rect.topLeft());
        subresDesc.setSourceSize(rect.size());
        subresDesc.setDestinationTopLeft(rect.topLeft());
        QRhiTextureUploadDescription uploadDesc(QRhiTextureUploadEntry(0, 0, subresDesc));
        resourceUpdates->uploadTexture(m_texture.get(), uploadDesc);
    }

    return m_texture.get();
}

//  from src/gui/painting/qbackingstoredefaultcompositor.cpp, line 413, as _ZN30QBackingStoreDefaultCompositor14updateUniformsEPNS_11PerQuadDataEP23QRhiResourceUpdateBatchRK10QMatrix4x4RK14QGenericMatrixILi3ELi3EfE6QFlagsINS_19UpdateUniformOptionEE
inline void QBackingStoreDefaultCompositor::updateUniforms(PerQuadData *d, QRhiResourceUpdateBatch *resourceUpdates,
                                                    const QMatrix4x4 &target, const QMatrix3x3 &source,
                                                    UpdateUniformOptions options)
{
    resourceUpdates->updateDynamicBuffer(d->ubuf, 0, 64, target.constData());
    updateMatrix3x3(resourceUpdates, d->ubuf, source);
    float opacity = 1.0f;
    resourceUpdates->updateDynamicBuffer(d->ubuf, 112, 4, &opacity);
    qint32 textureSwizzle = options;
    resourceUpdates->updateDynamicBuffer(d->ubuf, 116, 4, &textureSwizzle);
}
//  -----------------------------------------------------------------------

//  QBackingStoreDefaultCompositor::~QBackingStoreDefaultCompositor()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBackingStoreDefaultCompositorD1Ev(
    QBackingStoreDefaultCompositor *self) {
  delete self;
}

//  void QBackingStoreDefaultCompositor::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBackingStoreDefaultCompositor5resetEv(
    QBackingStoreDefaultCompositor *self) {
  self->reset();
}

//  QRhiTexture *QBackingStoreDefaultCompositor::toTexture(const
//      QPlatformBackingStore *backingStore, QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates, const QRegion &dirtyRegion,
//      QPlatformBackingStore::TextureFlags *flags) const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK30QBackingStoreDefaultCompositor9toTextureEPK21QPlatformBackingStoreP4QRhiP23QRhiResourceUpdateBatchRK7QRegionP6QFlagsINS0_11TextureFlagEE(
    const QBackingStoreDefaultCompositor *self,
    const QPlatformBackingStore *backingStore,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates,
    const QRegion *dirtyRegion,
    QPlatformBackingStore::TextureFlags *flags) {
  return self->toTexture(
      backingStore,
      rhi,
      resourceUpdates,
      *dirtyRegion,
      flags);
}

//  QRhiTexture *QBackingStoreDefaultCompositor::toTexture(const QImage
//      &image, QRhi *rhi, QRhiResourceUpdateBatch *resourceUpdates, const
//      QRegion &dirtyRegion, QPlatformBackingStore::TextureFlags *flags)
//      const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK30QBackingStoreDefaultCompositor9toTextureERK6QImageP4QRhiP23QRhiResourceUpdateBatchRK7QRegionP6QFlagsIN21QPlatformBackingStore11TextureFlagEE(
    const QBackingStoreDefaultCompositor *self,
    const QImage *image,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates,
    const QRegion *dirtyRegion,
    QPlatformBackingStore::TextureFlags *flags) {
  return self->toTexture(*image, rhi, resourceUpdates, *dirtyRegion, flags);
}

//  void QBackingStoreDefaultCompositor::updateUniforms(PerQuadData *d,
//      QRhiResourceUpdateBatch *resourceUpdates, const QMatrix4x4 &target,
//      const QMatrix3x3 &source, UpdateUniformOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBackingStoreDefaultCompositor14updateUniformsEPNS_11PerQuadDataEP23QRhiResourceUpdateBatchRK10QMatrix4x4RK14QGenericMatrixILi3ELi3EfE6QFlagsINS_19UpdateUniformOptionEE(
    QBackingStoreDefaultCompositor *self,
    QBackingStoreDefaultCompositor::PerQuadData *d,
    QRhiResourceUpdateBatch *resourceUpdates,
    const QMatrix4x4 *target,
    const QMatrix3x3 *source,
    int options) {
  self->updateUniforms(
      d,
      resourceUpdates,
      *target,
      *source,
      QFlags<QBackingStoreDefaultCompositor::UpdateUniformOption>::fromInt(options));
}

//  a QBackingStoreDefaultCompositor::PerQuadData a ritual of
//      QBackingStoreDefaultCompositor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QBackingStoreDefaultCompositor__QBackingStoreDefaultCompositor_PerQuadData(
    QBackingStoreDefaultCompositor::PerQuadData *self) {
  delete self;
}
