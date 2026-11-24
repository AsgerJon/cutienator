//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/statevariant_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/statevariant_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::StateVariant::u_Data::u_Data()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateVariant::u_Data *ritual_ZN10Qt3DRender6Render12StateVariant6u_DataC1Ev() {
  return new Qt3DRender::Render::StateVariant::u_Data();
}

//  Qt3DRender::Render::StateVariant::u_Data::u_Data(const u_Data &other)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateVariant::u_Data *ritual_ZN10Qt3DRender6Render12StateVariant6u_DataC1ERKS2_(
    const Qt3DRender::Render::StateVariant::u_Data *other) {
  return new Qt3DRender::Render::StateVariant::u_Data(*other);
}

//  Qt3DRender::Render::StateVariant::u_Data::~u_Data()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12StateVariant6u_DataD1Ev(
    Qt3DRender::Render::StateVariant::u_Data *self) {
  delete self;
}
