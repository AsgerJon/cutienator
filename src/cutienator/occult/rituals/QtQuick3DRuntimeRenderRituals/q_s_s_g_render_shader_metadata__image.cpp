//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadermetadata_p
//  .h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadermetadata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderShaderMetadata::Image::Image()
extern "C" Q_DECL_EXPORT
QSSGRenderShaderMetadata::Image *ritual_ZN24QSSGRenderShaderMetadata5ImageC1Ev() {
  return new QSSGRenderShaderMetadata::Image();
}

//  QSSGRenderShaderMetadata::Image::Image(const Uniform &u)
extern "C" Q_DECL_EXPORT
QSSGRenderShaderMetadata::Image *ritual_ZN24QSSGRenderShaderMetadata5ImageC1ERKNS_7UniformE(
    const QSSGRenderShaderMetadata::Uniform *u) {
  return new QSSGRenderShaderMetadata::Image(*u);
}

//  QSSGRenderShaderMetadata::Image::~Image()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGRenderShaderMetadata5ImageD1Ev(
    QSSGRenderShaderMetadata::Image *self) {
  delete self;
}
