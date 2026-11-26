//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QSharedPointer>

//  QGeoTiledMapScene *QGeoTiledMapScenePrivate::q_func()
extern "C" Q_DECL_EXPORT
QGeoTiledMapScene *ritual_ZN24QGeoTiledMapScenePrivate6q_funcEv(
    QGeoTiledMapScenePrivate *self) {
  return self->q_func();
}

//  const QGeoTiledMapScene *QGeoTiledMapScenePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGeoTiledMapScene *ritual_ZNK24QGeoTiledMapScenePrivate6q_funcEv(
    const QGeoTiledMapScenePrivate *self) {
  return self->q_func();
}

//  QGeoTiledMapScenePrivate::QGeoTiledMapScenePrivate()
extern "C" Q_DECL_EXPORT
QGeoTiledMapScenePrivate *ritual_ZN24QGeoTiledMapScenePrivateC1Ev() {
  return new QGeoTiledMapScenePrivate();
}

//  QGeoTiledMapScenePrivate::~QGeoTiledMapScenePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoTiledMapScenePrivateD1Ev(
    QGeoTiledMapScenePrivate *self) {
  delete self;
}

//  void QGeoTiledMapScenePrivate::addTile(const QGeoTileSpec &spec,
//      QSharedPointer<QGeoTileTexture> texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoTiledMapScenePrivate7addTileERK12QGeoTileSpec14QSharedPointerI15QGeoTileTextureE(
    QGeoTiledMapScenePrivate *self,
    const QGeoTileSpec *spec,
    const QSharedPointer<QGeoTileTexture> *texture) {
  self->addTile(*spec, *texture);
}

//  void QGeoTiledMapScenePrivate::setVisibleTiles(const QSet<QGeoTileSpec>
//      &visibleTiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoTiledMapScenePrivate15setVisibleTilesERK4QSetI12QGeoTileSpecE(
    QGeoTiledMapScenePrivate *self,
    const QSet<QGeoTileSpec> *visibleTiles) {
  self->setVisibleTiles(*visibleTiles);
}

//  void QGeoTiledMapScenePrivate::removeTiles(const QSet<QGeoTileSpec>
//      &oldTiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoTiledMapScenePrivate11removeTilesERK4QSetI12QGeoTileSpecE(
    QGeoTiledMapScenePrivate *self,
    const QSet<QGeoTileSpec> *oldTiles) {
  self->removeTiles(*oldTiles);
}

//  bool QGeoTiledMapScenePrivate::buildGeometry(const QGeoTileSpec &spec,
//      QSGImageNode *imageNode, bool &overzooming)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QGeoTiledMapScenePrivate13buildGeometryERK12QGeoTileSpecP12QSGImageNodeRb(
    QGeoTiledMapScenePrivate *self,
    const QGeoTileSpec *spec,
    QSGImageNode *imageNode,
    bool *overzooming) {
  return self->buildGeometry(*spec, imageNode, *overzooming);
}

//  void QGeoTiledMapScenePrivate::updateTileBounds(const QSet<QGeoTileSpec>
//      &tiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoTiledMapScenePrivate16updateTileBoundsERK4QSetI12QGeoTileSpecE(
    QGeoTiledMapScenePrivate *self,
    const QSet<QGeoTileSpec> *tiles) {
  self->updateTileBounds(*tiles);
}

//  void QGeoTiledMapScenePrivate::setupCamera()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoTiledMapScenePrivate11setupCameraEv(
    QGeoTiledMapScenePrivate *self) {
  self->setupCamera();
}

//  bool QGeoTiledMapScenePrivate::isTiltedOrRotated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QGeoTiledMapScenePrivate17isTiltedOrRotatedEv(
    const QGeoTiledMapScenePrivate *self) {
  return self->isTiltedOrRotated();
}
