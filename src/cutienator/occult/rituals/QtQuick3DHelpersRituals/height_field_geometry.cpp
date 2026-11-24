//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/heightfieldgeometry_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/heightfieldgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qvectornd.h>

//  const QMetaObject *HeightFieldGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19HeightFieldGeometry10metaObjectEv(
    const HeightFieldGeometry *self) {
  return self->metaObject();
}

//  QString HeightFieldGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19HeightFieldGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(HeightFieldGeometry::tr(s, c, n));
}

//  HeightFieldGeometry::HeightFieldGeometry()
extern "C" Q_DECL_EXPORT
HeightFieldGeometry *ritual_ZN19HeightFieldGeometryC1Ev() {
  return new HeightFieldGeometry();
}

//  const QUrl &HeightFieldGeometry::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19HeightFieldGeometry6sourceEv(
    const HeightFieldGeometry *self) {
  return new QUrl(self->source());
}

//  void HeightFieldGeometry::setSource(const QUrl &newSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN19HeightFieldGeometry9setSourceERK4QUrl(
    HeightFieldGeometry *self,
    const QUrl *newSource) {
  self->setSource(*newSource);
}

//  bool HeightFieldGeometry::smoothShading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19HeightFieldGeometry13smoothShadingEv(
    const HeightFieldGeometry *self) {
  return self->smoothShading();
}

//  void HeightFieldGeometry::setSmoothShading(bool smooth)
extern "C" Q_DECL_EXPORT
void ritual_ZN19HeightFieldGeometry16setSmoothShadingEb(
    HeightFieldGeometry *self,
    bool smooth) {
  self->setSmoothShading(smooth);
}

//  const QVector3D &HeightFieldGeometry::extents() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK19HeightFieldGeometry7extentsEv(
    const HeightFieldGeometry *self) {
  return new QVector3D(self->extents());
}

//  void HeightFieldGeometry::setExtents(const QVector3D &newExtents)
extern "C" Q_DECL_EXPORT
void ritual_ZN19HeightFieldGeometry10setExtentsERK9QVector3D(
    HeightFieldGeometry *self,
    const QVector3D *newExtents) {
  self->setExtents(*newExtents);
}

//  void HeightFieldGeometry::updateData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19HeightFieldGeometry10updateDataEv(
    HeightFieldGeometry *self) {
  self->updateData();
}
