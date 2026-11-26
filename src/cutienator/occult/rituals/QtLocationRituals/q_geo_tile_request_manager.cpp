//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotilerequestmanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilerequestmanager_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/QMap>
#include <QtCore/QSharedPointer>

//  QGeoTileRequestManager::QGeoTileRequestManager(QGeoTiledMap *map,
//      QGeoTiledMappingManagerEngine *engine)
extern "C" Q_DECL_EXPORT
QGeoTileRequestManager *ritual_ZN22QGeoTileRequestManagerC1EP12QGeoTiledMapP29QGeoTiledMappingManagerEngine(
    QGeoTiledMap *map,
    QGeoTiledMappingManagerEngine *engine) {
  return new QGeoTileRequestManager(map, engine);
}

//  QGeoTileRequestManager::~QGeoTileRequestManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoTileRequestManagerD1Ev(QGeoTileRequestManager *self) {
  delete self;
}

//  QMap<QGeoTileSpec, QSharedPointer<QGeoTileTexture>>
//      QGeoTileRequestManager::requestTiles(const QSet<QGeoTileSpec> &tiles)
extern "C" Q_DECL_EXPORT
QMap<QGeoTileSpec, QSharedPointer<QGeoTileTexture>> *ritual_ZN22QGeoTileRequestManager12requestTilesERK4QSetI12QGeoTileSpecE(
    QGeoTileRequestManager *self,
    const QSet<QGeoTileSpec> *tiles) {
  return new QMap<QGeoTileSpec, QSharedPointer<QGeoTileTexture>>(
      self->requestTiles(
          *tiles));
}

//  void QGeoTileRequestManager::tileError(const QGeoTileSpec &tile, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoTileRequestManager9tileErrorERK12QGeoTileSpecRK7QString(
    QGeoTileRequestManager *self,
    const QGeoTileSpec *tile,
    const QString *errorString) {
  self->tileError(*tile, *errorString);
}

//  void QGeoTileRequestManager::tileFetched(const QGeoTileSpec &spec)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoTileRequestManager11tileFetchedERK12QGeoTileSpec(
    QGeoTileRequestManager *self,
    const QGeoTileSpec *spec) {
  self->tileFetched(*spec);
}

//  QSharedPointer<QGeoTileTexture> QGeoTileRequestManager::tileTexture(const
//      QGeoTileSpec &spec)
extern "C" Q_DECL_EXPORT
QSharedPointer<QGeoTileTexture> *ritual_ZN22QGeoTileRequestManager11tileTextureERK12QGeoTileSpec(
    QGeoTileRequestManager *self,
    const QGeoTileSpec *spec) {
  return new QSharedPointer<QGeoTileTexture>(self->tileTexture(*spec));
}

//  a QMap<QGeoTileSpec, QSharedPointer<QGeoTileTexture>> a ritual of
//      QGeoTileRequestManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGeoTileRequestManager__QMap_QGeoTileSpec_QSharedPointer_QGeoTileTexture(
    QMap<QGeoTileSpec, QSharedPointer<QGeoTileTexture>> *self) {
  delete self;
}

//  a QSharedPointer<QGeoTileTexture> a ritual of QGeoTileRequestManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGeoTileRequestManager__QSharedPointer_QGeoTileTexture(
    QSharedPointer<QGeoTileTexture> *self) {
  delete self;
}
