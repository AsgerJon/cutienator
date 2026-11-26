//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/statevariant_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: added by hand, instances of templates of the
//  class: 5. Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/statevariant_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  RenderStateImpl *Qt3DRender::Render::StateVariant::state()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderStateImpl *ritual_ZN10Qt3DRender6Render12StateVariant5stateEv(
    Qt3DRender::Render::StateVariant *self) {
  return self->state();
}

//  const RenderStateImpl *Qt3DRender::Render::StateVariant::constState()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::RenderStateImpl *ritual_ZNK10Qt3DRender6Render12StateVariant10constStateEv(
    const Qt3DRender::Render::StateVariant *self) {
  return self->constState();
}

//  bool Qt3DRender::Render::StateVariant::operator==(const StateVariant
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12StateVarianteqERKS1_(
    const Qt3DRender::Render::StateVariant *self,
    const Qt3DRender::Render::StateVariant *other) {
  return self->operator==(*other);
}

//  bool Qt3DRender::Render::StateVariant::operator!=(const StateVariant
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12StateVariantneERKS1_(
    const Qt3DRender::Render::StateVariant *self,
    const Qt3DRender::Render::StateVariant *other) {
  return self->operator!=(*other);
}

//  Qt3DRender::Render::StateVariant::~StateVariant()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12StateVariantD1Ev(
    Qt3DRender::Render::StateVariant *self) {
  delete self;
}

//  Qt3DRender::Render::StateVariant
//      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::DepthTest>(const
//      Qt3DRender::Render::DepthTest &state)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateVariant * ritual_ZN10Qt3DRender6Render12StateVariant9fromValueINS0_9DepthTestEEES1_RKT_(
    const Qt3DRender::Render::DepthTest *state) {
  return new Qt3DRender::Render::StateVariant(
      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::DepthTest>(*state));
}

//  Qt3DRender::Render::StateVariant
//      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::CullFace>(const
//      Qt3DRender::Render::CullFace &state)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateVariant * ritual_ZN10Qt3DRender6Render12StateVariant9fromValueINS0_8CullFaceEEES1_RKT_(
    const Qt3DRender::Render::CullFace *state) {
  return new Qt3DRender::Render::StateVariant(
      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::CullFace>(*state));
}

//  Qt3DRender::Render::StateVariant
//      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::BlendEquation>(const
//      Qt3DRender::Render::BlendEquation &state)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateVariant * ritual_ZN10Qt3DRender6Render12StateVariant9fromValueINS0_13BlendEquationEEES1_RKT_(
    const Qt3DRender::Render::BlendEquation *state) {
  return new Qt3DRender::Render::StateVariant(
      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::BlendEquation>(*state));
}

//  Qt3DRender::Render::StateVariant
//      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::Dithering>(const
//      Qt3DRender::Render::Dithering &state)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateVariant * ritual_ZN10Qt3DRender6Render12StateVariant9fromValueINS0_9DitheringEEES1_RKT_(
    const Qt3DRender::Render::Dithering *state) {
  return new Qt3DRender::Render::StateVariant(
      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::Dithering>(*state));
}

//  Qt3DRender::Render::StateVariant
//      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::LineWidth>(const
//      Qt3DRender::Render::LineWidth &state)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateVariant * ritual_ZN10Qt3DRender6Render12StateVariant9fromValueINS0_9LineWidthEEES1_RKT_(
    const Qt3DRender::Render::LineWidth *state) {
  return new Qt3DRender::Render::StateVariant(
      Qt3DRender::Render::StateVariant::fromValue<Qt3DRender::Render::LineWidth>(*state));
}
