//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSSGShaderLight::operator<(const QSSGShaderLight &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGShaderLightltERKS_(
    const QSSGShaderLight *self,
    const QSSGShaderLight *o) {
  return self->operator<(*o);
}

//  QSSGShaderLight::~QSSGShaderLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGShaderLightD1Ev(QSSGShaderLight *self) {
  delete self;
}
