//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>

//  QSSGRenderRay::IntersectionResult::IntersectionResult()
extern "C" Q_DECL_EXPORT
QSSGRenderRay::IntersectionResult *ritual_ZN13QSSGRenderRay18IntersectionResultC1Ev() {
  return new QSSGRenderRay::IntersectionResult();
}

//  QSSGRenderRay::IntersectionResult::IntersectionResult(float rl, const
//      QVector2D &relxy, const QVector3D &scenePosition, const QVector3D
//      &localPosition, const QVector3D &normal, const QVector3D
//      &sceneNormal)
extern "C" Q_DECL_EXPORT
QSSGRenderRay::IntersectionResult *ritual_ZN13QSSGRenderRay18IntersectionResultC1EfRK9QVector2DRK9QVector3DS6_S6_S6_(
    float rl,
    const QVector2D *relxy,
    const QVector3D *scenePosition,
    const QVector3D *localPosition,
    const QVector3D *normal,
    const QVector3D *sceneNormal) {
  return new QSSGRenderRay::IntersectionResult(
      rl,
      *relxy,
      *scenePosition,
      *localPosition,
      *normal,
      *sceneNormal);
}

//  QSSGRenderRay::IntersectionResult::~IntersectionResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGRenderRay18IntersectionResultD1Ev(
    QSSGRenderRay::IntersectionResult *self) {
  delete self;
}
