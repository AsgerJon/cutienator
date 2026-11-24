//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>

//  const QMetaObject *QDeclarativeGeoMapPainterPath::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QDeclarativeGeoMapPainterPath10metaObjectEv(
    const QDeclarativeGeoMapPainterPath *self) {
  return self->metaObject();
}

//  QPainterPath QDeclarativeGeoMapPainterPath::path() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK29QDeclarativeGeoMapPainterPath4pathEv(
    const QDeclarativeGeoMapPainterPath *self) {
  return new QPainterPath(self->path());
}

//  void QDeclarativeGeoMapPainterPath::setPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeGeoMapPainterPath7setPathERK12QPainterPath(
    QDeclarativeGeoMapPainterPath *self,
    const QPainterPath *path) {
  self->setPath(*path);
}
