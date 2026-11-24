//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderclippingfrustum_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderclippingfrustum_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  float QSSGClipPlane::distance(const QVector3D &pt) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QSSGClipPlane8distanceERK9QVector3D(
    const QSSGClipPlane *self,
    const QVector3D *pt) {
  return self->distance(*pt);
}

//  QVector3D QSSGClipPlane::intersectWithLine(const QVector3D &p0, const
//      QVector3D &p1) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK13QSSGClipPlane17intersectWithLineERK9QVector3DS2_(
    const QSSGClipPlane *self,
    const QVector3D *p0,
    const QVector3D *p1) {
  return new QVector3D(self->intersectWithLine(*p0, *p1));
}

//  QVector3D QSSGClipPlane::corner(const QSSGBounds3 &bounds, BoxEdgeFlag
//      edge)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN13QSSGClipPlane6cornerERK11QSSGBounds3h(
    const QSSGBounds3 *bounds,
    QSSGClipPlane::BoxEdgeFlag edge) {
  return new QVector3D(QSSGClipPlane::corner(*bounds, edge));
}

//  int QSSGClipPlane::intersect(const QSSGBounds3 &bounds) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QSSGClipPlane9intersectERK11QSSGBounds3(
    const QSSGClipPlane *self,
    const QSSGBounds3 *bounds) {
  return self->intersect(*bounds);
}

//  bool QSSGClipPlane::intersectSimple(const QSSGBounds3 &bounds) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSSGClipPlane15intersectSimpleERK11QSSGBounds3(
    const QSSGClipPlane *self,
    const QSSGBounds3 *bounds) {
  return self->intersectSimple(*bounds);
}

//  void QSSGClipPlane::calculateBBoxEdges()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGClipPlane18calculateBBoxEdgesEv(QSSGClipPlane *self) {
  self->calculateBBoxEdges();
}

//  QSSGClipPlane::~QSSGClipPlane()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGClipPlaneD1Ev(QSSGClipPlane *self) {
  delete self;
}
