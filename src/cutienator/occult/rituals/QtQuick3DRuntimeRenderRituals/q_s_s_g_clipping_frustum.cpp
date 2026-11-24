//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderclippingfrustum_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderclippingfrustum_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>

//  QSSGClippingFrustum::QSSGClippingFrustum()
extern "C" Q_DECL_EXPORT
QSSGClippingFrustum *ritual_ZN19QSSGClippingFrustumC1Ev() {
  return new QSSGClippingFrustum();
}

//  QSSGClippingFrustum::QSSGClippingFrustum(const QMatrix4x4
//      &modelviewprojection, const QSSGClipPlane &nearPlane)
extern "C" Q_DECL_EXPORT
QSSGClippingFrustum *ritual_ZN19QSSGClippingFrustumC1ERK10QMatrix4x4RK13QSSGClipPlane(
    const QMatrix4x4 *modelviewprojection,
    const QSSGClipPlane *nearPlane) {
  return new QSSGClippingFrustum(*modelviewprojection, *nearPlane);
}

//  bool QSSGClippingFrustum::intersectsWith(const QSSGBounds3 &bounds) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSSGClippingFrustum14intersectsWithERK11QSSGBounds3(
    const QSSGClippingFrustum *self,
    const QSSGBounds3 *bounds) {
  return self->intersectsWith(*bounds);
}

//  bool QSSGClippingFrustum::intersectsWith(const QVector3D &point, float
//      radius) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSSGClippingFrustum14intersectsWithERK9QVector3Df(
    const QSSGClippingFrustum *self,
    const QVector3D *point,
    float radius) {
  return self->intersectsWith(*point, radius);
}

//  QSSGClippingFrustum::~QSSGClippingFrustum()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGClippingFrustumD1Ev(QSSGClippingFrustum *self) {
  delete self;
}
