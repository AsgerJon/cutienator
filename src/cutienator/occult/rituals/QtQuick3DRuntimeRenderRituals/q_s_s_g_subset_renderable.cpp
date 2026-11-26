//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QVector3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhicustommaterialsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlight_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterialshadergenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderableobjects.cpp, line 31, as _ZN20QSSGSubsetRenderableC1EN20QSSGRenderableObject4TypeE25QSSGRenderableObjectFlagsRK9QVector3DP12QSSGRendererRK16QSSGRenderSubsetRK16QSSGModelContextfjRK21QSSGRenderGraphObjectP19QSSGRenderableImage25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EERK12QSSGDataViewI15QSSGShaderLightEb
inline QSSGSubsetRenderable::QSSGSubsetRenderable(Type type,
                                           QSSGRenderableObjectFlags inFlags,
                                           const QVector3D &inWorldCenterPt,
                                           QSSGRenderer *rendr,
                                           const QSSGRenderSubset &inSubset,
                                           const QSSGModelContext &inModelContext,
                                           float inOpacity,
                                           quint32 inSubsetLevelOfDetail,
                                           const QSSGRenderGraphObject &mat,
                                           QSSGRenderableImage *inFirstImage,
                                           QSSGShaderDefaultMaterialKey inShaderKey,
                                           const QSSGShaderLightListView &inLights,
                                           bool anyLightHasShadows)
    : QSSGRenderableObject(type,
                           inFlags,
                           inWorldCenterPt,
                           inSubset.bounds,
                           inModelContext.model.m_depthBiasSq,
                           inModelContext.model.instancingLodMin,
                           inModelContext.model.instancingLodMax)
    , subsetLevelOfDetail(inSubsetLevelOfDetail)
    , renderer(rendr)
    , modelContext(inModelContext)
    , subset(inSubset)
    , opacity(inOpacity)
    , material(mat)
    , firstImage(inFirstImage)
    , shaderDescription(inShaderKey)
    , lights(inLights)
{
    if (mat.type == QSSGRenderGraphObject::Type::CustomMaterial)
        depthWriteMode = static_cast<const QSSGRenderCustomMaterial *>(&mat)->m_depthDrawMode;
    else
        depthWriteMode = static_cast<const QSSGRenderDefaultMaterial *>(&mat)->depthDrawMode;

    const bool modelBlendParticle = (inModelContext.model.particleBuffer != nullptr
                                     && inModelContext.model.particleBuffer->particleCount());
    if (modelBlendParticle)
        globalBounds = inModelContext.model.particleBuffer->bounds();
    else
        globalBounds.transform(inModelContext.globalTransform);

    // Do we need instanced bounds
    const QSSGRenderInstanceTable *instanceTable = inModelContext.model.instanceTable;
    isInstanced = instanceTable != nullptr;
    if (!instanceTable || !anyLightHasShadows || !(inFlags.castsShadows() || inFlags.receivesShadows()))
        return;

    // Check for specified instancing shadow bounds
    QSSGBounds3 bounds = QSSGBounds3(instanceTable->getShadowBoundsMinimum(), instanceTable->getShadowBoundsMaximum());
    if (!bounds.isEmpty() && bounds.isFinite()) {
        globalBoundsInstancing = bounds;
        return;
    }

    // Calculate instancing shadow bounds
    const auto points = globalBounds.toQSSGBoxPointsNoEmptyCheck();
    for (int i = 0; i < instanceTable->count(); ++i) {
        const QMatrix4x4 transform = instanceTable->getTransform(i);
        for (const QVector3D &point : points) {
            globalBoundsInstancing.include(transform.map(point));
        }
    }
}
//  -----------------------------------------------------------------------

//  QSSGSubsetRenderable::QSSGSubsetRenderable(Type type,
//      QSSGRenderableObjectFlags inFlags, const QVector3D &inWorldCenterPt,
//      QSSGRenderer *rendr, const QSSGRenderSubset &inSubset, const
//      QSSGModelContext &inModelContext, float inOpacity, quint32
//      inSubsetLevelOfDetail, const QSSGRenderGraphObject &mat,
//      QSSGRenderableImage *inFirstImage, QSSGShaderDefaultMaterialKey
//      inShaderKey, const QSSGShaderLightListView &inLights, bool
//      anyLightHasShadows)
extern "C" Q_DECL_EXPORT
QSSGSubsetRenderable *ritual_ZN20QSSGSubsetRenderableC1EN20QSSGRenderableObject4TypeE25QSSGRenderableObjectFlagsRK9QVector3DP12QSSGRendererRK16QSSGRenderSubsetRK16QSSGModelContextfjRK21QSSGRenderGraphObjectP19QSSGRenderableImage25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EERK12QSSGDataViewI15QSSGShaderLightEb(
    QSSGRenderableObject::Type type,
    const QSSGRenderableObjectFlags *inFlags,
    const QVector3D *inWorldCenterPt,
    QSSGRenderer *rendr,
    const QSSGRenderSubset *inSubset,
    const QSSGModelContext *inModelContext,
    float inOpacity,
    quint32 inSubsetLevelOfDetail,
    const QSSGRenderGraphObject *mat,
    QSSGRenderableImage *inFirstImage,
    const QSSGShaderDefaultMaterialKey *inShaderKey,
    const QSSGShaderLightListView *inLights,
    bool anyLightHasShadows) {
  return new QSSGSubsetRenderable(
      type,
      *inFlags,
      *inWorldCenterPt,
      rendr,
      *inSubset,
      *inModelContext,
      inOpacity,
      inSubsetLevelOfDetail,
      *mat,
      inFirstImage,
      *inShaderKey,
      *inLights,
      anyLightHasShadows);
}

//  const QSSGRenderGraphObject &QSSGSubsetRenderable::getMaterial() const
extern "C" Q_DECL_EXPORT
const QSSGRenderGraphObject *ritual_ZNK20QSSGSubsetRenderable11getMaterialEv(
    const QSSGSubsetRenderable *self) {
  return &(self->getMaterial());
}
