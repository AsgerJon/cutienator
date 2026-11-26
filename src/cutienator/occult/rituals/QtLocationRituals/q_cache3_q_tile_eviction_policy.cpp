//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeofiletilecache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeofiletilecache_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QSharedPointer>

//  void QCache3QTileEvictionPolicy::aboutToBeRemoved(const QGeoTileSpec
//      &key, QSharedPointer<QGeoCachedTileDisk> obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCache3QTileEvictionPolicy16aboutToBeRemovedERK12QGeoTileSpec14QSharedPointerI18QGeoCachedTileDiskE(
    QCache3QTileEvictionPolicy *self,
    const QGeoTileSpec *key,
    const QSharedPointer<QGeoCachedTileDisk> *obj) {
  self->aboutToBeRemoved(*key, *obj);
}

//  void QCache3QTileEvictionPolicy::aboutToBeEvicted(const QGeoTileSpec
//      &key, QSharedPointer<QGeoCachedTileDisk> obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCache3QTileEvictionPolicy16aboutToBeEvictedERK12QGeoTileSpec14QSharedPointerI18QGeoCachedTileDiskE(
    QCache3QTileEvictionPolicy *self,
    const QGeoTileSpec *key,
    const QSharedPointer<QGeoCachedTileDisk> *obj) {
  self->aboutToBeEvicted(*key, *obj);
}

//  QCache3QTileEvictionPolicy::~QCache3QTileEvictionPolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCache3QTileEvictionPolicyD1Ev(
    QCache3QTileEvictionPolicy *self) {
  delete self;
}
