//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGGradientCacheKey::QSGGradientCacheKey(const QGradientStops &stops,
//      QGradient::Spread spread)
extern "C" Q_DECL_EXPORT
QSGGradientCacheKey *ritual_ZN19QSGGradientCacheKeyC1ERK5QListISt4pairId6QColorEEN9QGradient6SpreadE(
    const QGradientStops *stops,
    QGradient::Spread spread) {
  return new QSGGradientCacheKey(*stops, spread);
}

//  bool QSGGradientCacheKey::operator==(const QSGGradientCacheKey &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSGGradientCacheKeyeqERKS_(
    const QSGGradientCacheKey *self,
    const QSGGradientCacheKey *other) {
  return self->operator==(*other);
}

//  QSGGradientCacheKey::~QSGGradientCacheKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGGradientCacheKeyD1Ev(QSGGradientCacheKey *self) {
  delete self;
}
