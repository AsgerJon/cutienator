//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterials
//  hadergenerator_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterialshadergenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGMaterialShaderGenerator::~QSSGMaterialShaderGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGMaterialShaderGeneratorD1Ev(
    QSSGMaterialShaderGenerator *self) {
  delete self;
}

//  const char
//      *QSSGMaterialShaderGenerator::getSamplerName(QSSGRenderableImage::Typ
//      e type)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator14getSamplerNameEN19QSSGRenderableImage4TypeE(
    QSSGRenderableImage::Type type) {
  return QSSGMaterialShaderGenerator::getSamplerName(type);
}

//  const char
//      *QSSGMaterialShaderGenerator::directionalLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator37directionalLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::directionalLightProcessorArgumentList();
}

//  const char
//      *QSSGMaterialShaderGenerator::pointLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator31pointLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::pointLightProcessorArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::spotLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator30spotLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::spotLightProcessorArgumentList();
}

//  const char
//      *QSSGMaterialShaderGenerator::ambientLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator33ambientLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::ambientLightProcessorArgumentList();
}

//  const char
//      *QSSGMaterialShaderGenerator::specularLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator34specularLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::specularLightProcessorArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::shadedFragmentMainArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator30shadedFragmentMainArgumentListEv() {
  return QSSGMaterialShaderGenerator::shadedFragmentMainArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::postProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator25postProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::postProcessorArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::iblProbeProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator29iblProbeProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::iblProbeProcessorArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::vertexMainArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator22vertexMainArgumentListEv() {
  return QSSGMaterialShaderGenerator::vertexMainArgumentList();
}

//  const char
//      *QSSGMaterialShaderGenerator::vertexInstancedMainArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator31vertexInstancedMainArgumentListEv() {
  return QSSGMaterialShaderGenerator::vertexInstancedMainArgumentList();
}
