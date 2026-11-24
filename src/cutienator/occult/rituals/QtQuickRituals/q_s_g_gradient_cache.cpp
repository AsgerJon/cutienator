//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGGradientCache::QSGGradientCache()
extern "C" Q_DECL_EXPORT
QSGGradientCache *ritual_ZN16QSGGradientCacheC1Ev() {
  return new QSGGradientCache();
}

//  QSGGradientCache::~QSGGradientCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGGradientCacheD1Ev(QSGGradientCache *self) {
  delete self;
}

//  QSGGradientCache *QSGGradientCache::cacheForRhi(QRhi *rhi)
extern "C" Q_DECL_EXPORT
QSGGradientCache *ritual_ZN16QSGGradientCache11cacheForRhiEP4QRhi(
    QRhi *rhi) {
  return QSGGradientCache::cacheForRhi(rhi);
}

//  QSGTexture *QSGGradientCache::get(const QSGGradientCacheKey &grad)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN16QSGGradientCache3getERK19QSGGradientCacheKey(
    QSGGradientCache *self,
    const QSGGradientCacheKey *grad) {
  return self->get(*grad);
}

//  void QSGGradientCache::setTextureData(QSGPlainTexture *tx, const
//      QSGGradientCacheKey &grad)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGGradientCache14setTextureDataEP15QSGPlainTextureRK19QSGGradientCacheKey(
    QSGGradientCache *self,
    QSGPlainTexture *tx,
    const QSGGradientCacheKey *grad) {
  self->setTextureData(tx, *grad);
}
