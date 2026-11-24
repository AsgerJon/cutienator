//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderableObject::QSSGRenderableObject(Type ty,
//      QSSGRenderableObjectFlags inFlags, const QVector3D &inWorldCenterPt,
//      const QSSGBounds3 &inBounds, float inDepthBias, float inMinThreshold,
//      float inMaxThreshold)
extern "C" Q_DECL_EXPORT
QSSGRenderableObject *ritual_ZN20QSSGRenderableObjectC1ENS_4TypeE25QSSGRenderableObjectFlagsRK9QVector3DRK11QSSGBounds3fff(
    QSSGRenderableObject::Type ty,
    const QSSGRenderableObjectFlags *inFlags,
    const QVector3D *inWorldCenterPt,
    const QSSGBounds3 *inBounds,
    float inDepthBias,
    float inMinThreshold,
    float inMaxThreshold) {
  return new QSSGRenderableObject(
      ty,
      *inFlags,
      *inWorldCenterPt,
      *inBounds,
      inDepthBias,
      inMinThreshold,
      inMaxThreshold);
}
