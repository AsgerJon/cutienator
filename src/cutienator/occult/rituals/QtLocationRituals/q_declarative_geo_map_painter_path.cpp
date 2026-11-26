//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QDeclarativeGeoMapPainterPath::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QDeclarativeGeoMapPainterPath10metaObjectEv(
    const QDeclarativeGeoMapPainterPath *self) {
  return self->metaObject();
}

//  void *QDeclarativeGeoMapPainterPath::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QDeclarativeGeoMapPainterPath11qt_metacastEPKc(
    QDeclarativeGeoMapPainterPath *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeGeoMapPainterPath::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QDeclarativeGeoMapPainterPath11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeGeoMapPainterPath *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QDeclarativeGeoMapPainterPath::addToPath(QPainterPath &path, const
//      QQuickPathData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeGeoMapPainterPath9addToPathER12QPainterPathRK14QQuickPathData(
    QDeclarativeGeoMapPainterPath *self,
    QPainterPath *path,
    const QQuickPathData *a1) {
  self->addToPath(*path, *a1);
}
