//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtGui/qimage.h>

//  QRhiResourceUpdateBatch::~QRhiResourceUpdateBatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatchD1Ev(QRhiResourceUpdateBatch *self) {
  delete self;
}

//  void QRhiResourceUpdateBatch::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch7releaseEv(
    QRhiResourceUpdateBatch *self) {
  self->release();
}

//  void QRhiResourceUpdateBatch::merge(QRhiResourceUpdateBatch *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch5mergeEPS_(
    QRhiResourceUpdateBatch *self,
    QRhiResourceUpdateBatch *other) {
  self->merge(other);
}

//  bool QRhiResourceUpdateBatch::hasOptimalCapacity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRhiResourceUpdateBatch18hasOptimalCapacityEv(
    const QRhiResourceUpdateBatch *self) {
  return self->hasOptimalCapacity();
}

//  void QRhiResourceUpdateBatch::updateDynamicBuffer(QRhiBuffer *buf,
//      quint32 offset, QByteArray data)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch19updateDynamicBufferEP10QRhiBufferj10QByteArray(
    QRhiResourceUpdateBatch *self,
    QRhiBuffer *buf,
    quint32 offset,
    const QByteArray *data) {
  self->updateDynamicBuffer(buf, offset, *data);
}

//  void QRhiResourceUpdateBatch::uploadStaticBuffer(QRhiBuffer *buf, quint32
//      offset, QByteArray data)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch18uploadStaticBufferEP10QRhiBufferj10QByteArray(
    QRhiResourceUpdateBatch *self,
    QRhiBuffer *buf,
    quint32 offset,
    const QByteArray *data) {
  self->uploadStaticBuffer(buf, offset, *data);
}

//  void QRhiResourceUpdateBatch::uploadStaticBuffer(QRhiBuffer *buf,
//      QByteArray data)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch18uploadStaticBufferEP10QRhiBuffer10QByteArray(
    QRhiResourceUpdateBatch *self,
    QRhiBuffer *buf,
    const QByteArray *data) {
  self->uploadStaticBuffer(buf, *data);
}

//  void QRhiResourceUpdateBatch::readBackBuffer(QRhiBuffer *buf, quint32
//      offset, quint32 size, QRhiReadbackResult *result)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch14readBackBufferEP10QRhiBufferjjP18QRhiReadbackResult(
    QRhiResourceUpdateBatch *self,
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size,
    QRhiReadbackResult *result) {
  self->readBackBuffer(buf, offset, size, result);
}

//  void QRhiResourceUpdateBatch::uploadTexture(QRhiTexture *tex, const
//      QRhiTextureUploadDescription &desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch13uploadTextureEP11QRhiTextureRK28QRhiTextureUploadDescription(
    QRhiResourceUpdateBatch *self,
    QRhiTexture *tex,
    const QRhiTextureUploadDescription *desc) {
  self->uploadTexture(tex, *desc);
}

//  void QRhiResourceUpdateBatch::uploadTexture(QRhiTexture *tex, const
//      QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch13uploadTextureEP11QRhiTextureRK6QImage(
    QRhiResourceUpdateBatch *self,
    QRhiTexture *tex,
    const QImage *image) {
  self->uploadTexture(tex, *image);
}

//  void QRhiResourceUpdateBatch::copyTexture(QRhiTexture *dst, QRhiTexture
//      *src, const QRhiTextureCopyDescription &desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch11copyTextureEP11QRhiTextureS1_RK26QRhiTextureCopyDescription(
    QRhiResourceUpdateBatch *self,
    QRhiTexture *dst,
    QRhiTexture *src,
    const QRhiTextureCopyDescription *desc) {
  self->copyTexture(dst, src, *desc);
}

//  void QRhiResourceUpdateBatch::readBackTexture(const
//      QRhiReadbackDescription &rb, QRhiReadbackResult *result)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch15readBackTextureERK23QRhiReadbackDescriptionP18QRhiReadbackResult(
    QRhiResourceUpdateBatch *self,
    const QRhiReadbackDescription *rb,
    QRhiReadbackResult *result) {
  self->readBackTexture(*rb, result);
}

//  void QRhiResourceUpdateBatch::generateMips(QRhiTexture *tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiResourceUpdateBatch12generateMipsEP11QRhiTexture(
    QRhiResourceUpdateBatch *self,
    QRhiTexture *tex) {
  self->generateMips(tex);
}

//  QRhiResourceUpdateBatch::QRhiResourceUpdateBatch(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatch *ritual_ZN23QRhiResourceUpdateBatchC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new QRhiResourceUpdateBatch(rhi);
}
