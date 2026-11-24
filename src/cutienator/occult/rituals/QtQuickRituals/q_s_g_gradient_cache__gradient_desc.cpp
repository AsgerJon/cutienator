//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QSGGradientCache::GradientDesc::compare(const GradientDesc &other)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSGGradientCache12GradientDesc7compareERKS0_(
    const QSGGradientCache::GradientDesc *self,
    const QSGGradientCache::GradientDesc *other) {
  return self->compare(*other);
}

//  QSGGradientCache::GradientDesc::~GradientDesc()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGGradientCache12GradientDescD1Ev(
    QSGGradientCache::GradientDesc *self) {
  delete self;
}
