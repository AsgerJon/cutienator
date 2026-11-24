//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsggeometry_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsggeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGGeometryData::~QSGGeometryData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGGeometryDataD1Ev(QSGGeometryData *self) {
  delete self;
}

//  QSGGeometryData *QSGGeometryData::data(const QSGGeometry *g)
extern "C" Q_DECL_EXPORT
QSGGeometryData *ritual_ZN15QSGGeometryData4dataEPK11QSGGeometry(
    const QSGGeometry *g) {
  return QSGGeometryData::data(g);
}

//  void QSGGeometryData::install(const QSGGeometry *g, QSGGeometryData
//      *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGGeometryData7installEPK11QSGGeometryPS_(
    const QSGGeometry *g,
    QSGGeometryData *data) {
  QSGGeometryData::install(g, data);
}

//  bool QSGGeometryData::hasDirtyVertexData(const QSGGeometry *g)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSGGeometryData18hasDirtyVertexDataEPK11QSGGeometry(
    const QSGGeometry *g) {
  return QSGGeometryData::hasDirtyVertexData(g);
}

//  void QSGGeometryData::clearDirtyVertexData(const QSGGeometry *g)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGGeometryData20clearDirtyVertexDataEPK11QSGGeometry(
    const QSGGeometry *g) {
  QSGGeometryData::clearDirtyVertexData(g);
}

//  bool QSGGeometryData::hasDirtyIndexData(const QSGGeometry *g)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSGGeometryData17hasDirtyIndexDataEPK11QSGGeometry(
    const QSGGeometry *g) {
  return QSGGeometryData::hasDirtyIndexData(g);
}

//  void QSGGeometryData::clearDirtyIndexData(const QSGGeometry *g)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGGeometryData19clearDirtyIndexDataEPK11QSGGeometry(
    const QSGGeometry *g) {
  QSGGeometryData::clearDirtyIndexData(g);
}
