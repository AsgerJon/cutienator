//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderParticles::QSSGRenderParticles()
extern "C" Q_DECL_EXPORT
QSSGRenderParticles *ritual_ZN19QSSGRenderParticlesC1Ev() {
  return new QSSGRenderParticles();
}

//  QSSGRenderParticles::~QSSGRenderParticles()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRenderParticlesD1Ev(QSSGRenderParticles *self) {
  delete self;
}
