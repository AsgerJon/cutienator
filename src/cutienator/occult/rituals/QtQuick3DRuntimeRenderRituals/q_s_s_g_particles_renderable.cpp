//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/QVector3D>
#include <QtGui/QMatrix4x4>

//  QSSGParticlesRenderable::QSSGParticlesRenderable(QSSGRenderableObjectFlag
//      s inFlags, const QVector3D &inWorldCenterPt, QSSGRenderer *rendr,
//      const QMatrix4x4 &inGlobalTransform, const QSSGRenderParticles
//      &inParticles, QSSGRenderableImage *inFirstImage, QSSGRenderableImage
//      *inColorTable, const QSSGShaderLightListView &inLights, float
//      inOpacity, QSSGShaderParticleMaterialKey inShaderKey)
extern "C" Q_DECL_EXPORT
QSSGParticlesRenderable *ritual_ZN23QSSGParticlesRenderableC1E25QSSGRenderableObjectFlagsRK9QVector3DP12QSSGRendererRK10QMatrix4x4RK19QSSGRenderParticlesP19QSSGRenderableImageSD_RK12QSSGDataViewI15QSSGShaderLightEf25QSSGShaderBaseMaterialKeyI39QSSGShaderParticleMaterialKeyPropertiesLm1EE(
    const QSSGRenderableObjectFlags *inFlags,
    const QVector3D *inWorldCenterPt,
    QSSGRenderer *rendr,
    const QMatrix4x4 *inGlobalTransform,
    const QSSGRenderParticles *inParticles,
    QSSGRenderableImage *inFirstImage,
    QSSGRenderableImage *inColorTable,
    const QSSGShaderLightListView *inLights,
    float inOpacity,
    const QSSGShaderParticleMaterialKey *inShaderKey) {
  return new QSSGParticlesRenderable(
      *inFlags,
      *inWorldCenterPt,
      rendr,
      *inGlobalTransform,
      *inParticles,
      inFirstImage,
      inColorTable,
      *inLights,
      inOpacity,
      *inShaderKey);
}
