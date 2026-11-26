//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGeoCameraTiles::QGeoCameraTiles()
extern "C" Q_DECL_EXPORT
QGeoCameraTiles *ritual_ZN15QGeoCameraTilesC1Ev() {
  return new QGeoCameraTiles();
}

//  QGeoCameraTiles::~QGeoCameraTiles()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoCameraTilesD1Ev(QGeoCameraTiles *self) {
  delete self;
}

//  void QGeoCameraTiles::setCameraData(const QGeoCameraData &camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoCameraTiles13setCameraDataERK14QGeoCameraData(
    QGeoCameraTiles *self,
    const QGeoCameraData *camera) {
  self->setCameraData(*camera);
}

//  QGeoCameraData QGeoCameraTiles::cameraData() const
extern "C" Q_DECL_EXPORT
QGeoCameraData *ritual_ZNK15QGeoCameraTiles10cameraDataEv(
    const QGeoCameraTiles *self) {
  return new QGeoCameraData(self->cameraData());
}

//  void QGeoCameraTiles::setVisibleArea(const QRectF &visibleArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoCameraTiles14setVisibleAreaERK6QRectF(
    QGeoCameraTiles *self,
    const QRectF *visibleArea) {
  self->setVisibleArea(*visibleArea);
}

//  void QGeoCameraTiles::setScreenSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoCameraTiles13setScreenSizeERK5QSize(
    QGeoCameraTiles *self,
    const QSize *size) {
  self->setScreenSize(*size);
}

//  void QGeoCameraTiles::setTileSize(int tileSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoCameraTiles11setTileSizeEi(
    QGeoCameraTiles *self,
    int tileSize) {
  self->setTileSize(tileSize);
}

//  int QGeoCameraTiles::tileSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGeoCameraTiles8tileSizeEv(const QGeoCameraTiles *self) {
  return self->tileSize();
}

//  void QGeoCameraTiles::setViewExpansion(double viewExpansion)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoCameraTiles16setViewExpansionEd(
    QGeoCameraTiles *self,
    double viewExpansion) {
  self->setViewExpansion(viewExpansion);
}

//  void QGeoCameraTiles::setPluginString(const QString &pluginString)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoCameraTiles15setPluginStringERK7QString(
    QGeoCameraTiles *self,
    const QString *pluginString) {
  self->setPluginString(*pluginString);
}

//  void QGeoCameraTiles::setMapType(const QGeoMapType &mapType)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoCameraTiles10setMapTypeERK11QGeoMapType(
    QGeoCameraTiles *self,
    const QGeoMapType *mapType) {
  self->setMapType(*mapType);
}

//  QGeoMapType QGeoCameraTiles::activeMapType() const
extern "C" Q_DECL_EXPORT
QGeoMapType *ritual_ZNK15QGeoCameraTiles13activeMapTypeEv(
    const QGeoCameraTiles *self) {
  return new QGeoMapType(self->activeMapType());
}

//  void QGeoCameraTiles::setMapVersion(int mapVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoCameraTiles13setMapVersionEi(
    QGeoCameraTiles *self,
    int mapVersion) {
  self->setMapVersion(mapVersion);
}

//  const QSet<QGeoTileSpec> &QGeoCameraTiles::createTiles()
extern "C" Q_DECL_EXPORT
const QSet<QGeoTileSpec> *ritual_ZN15QGeoCameraTiles11createTilesEv(
    QGeoCameraTiles *self) {
  return &(self->createTiles());
}
