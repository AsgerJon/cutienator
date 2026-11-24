//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSSGUserShaderAugmentation::hasUserAugmentation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QSSGUserShaderAugmentation19hasUserAugmentationEv(
    const QSSGUserShaderAugmentation *self) {
  return self->hasUserAugmentation();
}

//  bool QSSGUserShaderAugmentation::hasPropertyUniforms() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QSSGUserShaderAugmentation19hasPropertyUniformsEv(
    const QSSGUserShaderAugmentation *self) {
  return self->hasPropertyUniforms();
}

//  QSSGUserShaderAugmentation::~QSSGUserShaderAugmentation()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGUserShaderAugmentationD1Ev(
    QSSGUserShaderAugmentation *self) {
  delete self;
}
