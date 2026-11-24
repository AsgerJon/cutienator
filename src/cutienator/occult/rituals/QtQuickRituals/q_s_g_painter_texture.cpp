//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultpainternode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultpainternode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  QSGPainterTexture::QSGPainterTexture()
extern "C" Q_DECL_EXPORT
QSGPainterTexture *ritual_ZN17QSGPainterTextureC1Ev() {
  return new QSGPainterTexture();
}

//  void QSGPainterTexture::setDirtyRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGPainterTexture12setDirtyRectERK5QRect(
    QSGPainterTexture *self,
    const QRect *rect) {
  self->setDirtyRect(*rect);
}

//  void QSGPainterTexture::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGPainterTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGPainterTexture *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->commitTextureOperations(rhi, resourceUpdates);
}

//  void QSGPainterTexture::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGPainterTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGPainterTexture *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->QSGPainterTexture::commitTextureOperations(rhi, resourceUpdates);
}
