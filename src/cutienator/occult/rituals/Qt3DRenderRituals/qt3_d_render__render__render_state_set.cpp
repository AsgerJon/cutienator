//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/renderstateset_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 5. Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/renderstateset_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/statevariant_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::RenderStateSet::RenderStateSet()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderStateSet *ritual_ZN10Qt3DRender6Render14RenderStateSetC1Ev() {
  return new Qt3DRender::Render::RenderStateSet();
}

//  Qt3DRender::Render::RenderStateSet::~RenderStateSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14RenderStateSetD1Ev(
    Qt3DRender::Render::RenderStateSet *self) {
  delete self;
}

//  int Qt3DRender::Render::RenderStateSet::changeCost(RenderStateSet
//      *previousState)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render14RenderStateSet10changeCostEPS1_(
    Qt3DRender::Render::RenderStateSet *self,
    Qt3DRender::Render::RenderStateSet *previousState) {
  return self->changeCost(previousState);
}

//  StateMaskSet Qt3DRender::Render::RenderStateSet::stateMask() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateMaskSet ritual_ZNK10Qt3DRender6Render14RenderStateSet9stateMaskEv(
    const Qt3DRender::Render::RenderStateSet *self) {
  return self->stateMask();
}

//  void Qt3DRender::Render::RenderStateSet::merge(const RenderStateSet
//      *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14RenderStateSet5mergeEPKS1_(
    Qt3DRender::Render::RenderStateSet *self,
    const Qt3DRender::Render::RenderStateSet *other) {
  self->merge(other);
}

//  const std::vector<StateVariant>
//      &Qt3DRender::Render::RenderStateSet::states() const
extern "C" Q_DECL_EXPORT
const std::vector<Qt3DRender::Render::StateVariant> *ritual_ZNK10Qt3DRender6Render14RenderStateSet6statesEv(
    const Qt3DRender::Render::RenderStateSet *self) {
  return &(self->states());
}

//  std::vector<StateVariant> &Qt3DRender::Render::RenderStateSet::states()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DRender::Render::StateVariant> *ritual_ZN10Qt3DRender6Render14RenderStateSet6statesEv(
    Qt3DRender::Render::RenderStateSet *self) {
  return &(self->states());
}

//  bool Qt3DRender::Render::RenderStateSet::canAddStateOfType(StateMask
//      type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render14RenderStateSet17canAddStateOfTypeENS0_9StateMaskE(
    const Qt3DRender::Render::RenderStateSet *self,
    Qt3DRender::Render::StateMask type) {
  return self->canAddStateOfType(type);
}

//  bool Qt3DRender::Render::RenderStateSet::contains(const StateVariant &ds)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render14RenderStateSet8containsERKNS0_12StateVariantE(
    const Qt3DRender::Render::RenderStateSet *self,
    const Qt3DRender::Render::StateVariant *ds) {
  return self->contains(*ds);
}

//  bool Qt3DRender::Render::RenderStateSet::hasStateOfType(StateMask type)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render14RenderStateSet14hasStateOfTypeENS0_9StateMaskE(
    const Qt3DRender::Render::RenderStateSet *self,
    Qt3DRender::Render::StateMask type) {
  return self->hasStateOfType(type);
}

//  bool
//      Qt3DRender::Render::RenderStateSet::allowMultipleStatesOfType(StateMa
//      sk type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render14RenderStateSet25allowMultipleStatesOfTypeENS0_9StateMaskE(
    const Qt3DRender::Render::RenderStateSet *self,
    Qt3DRender::Render::StateMask type) {
  return self->allowMultipleStatesOfType(type);
}

//  void
//      Qt3DRender::Render::RenderStateSet::addState<Qt3DRender::Render::DepthTest>(const
//      Qt3DRender::Render::DepthTest &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14RenderStateSet8addStateINS0_9DepthTestEEEvRKT_(
    Qt3DRender::Render::RenderStateSet *self,
    const Qt3DRender::Render::DepthTest *state) {
  self->addState<Qt3DRender::Render::DepthTest>(*state);
}

//  void
//      Qt3DRender::Render::RenderStateSet::addState<Qt3DRender::Render::CullFace>(const
//      Qt3DRender::Render::CullFace &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14RenderStateSet8addStateINS0_8CullFaceEEEvRKT_(
    Qt3DRender::Render::RenderStateSet *self,
    const Qt3DRender::Render::CullFace *state) {
  self->addState<Qt3DRender::Render::CullFace>(*state);
}

//  void
//      Qt3DRender::Render::RenderStateSet::addState<Qt3DRender::Render::BlendEquation>(const
//      Qt3DRender::Render::BlendEquation &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14RenderStateSet8addStateINS0_13BlendEquationEEEvRKT_(
    Qt3DRender::Render::RenderStateSet *self,
    const Qt3DRender::Render::BlendEquation *state) {
  self->addState<Qt3DRender::Render::BlendEquation>(*state);
}

//  void
//      Qt3DRender::Render::RenderStateSet::addState<Qt3DRender::Render::Dithering>(const
//      Qt3DRender::Render::Dithering &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14RenderStateSet8addStateINS0_9DitheringEEEvRKT_(
    Qt3DRender::Render::RenderStateSet *self,
    const Qt3DRender::Render::Dithering *state) {
  self->addState<Qt3DRender::Render::Dithering>(*state);
}

//  void
//      Qt3DRender::Render::RenderStateSet::addState<Qt3DRender::Render::LineWidth>(const
//      Qt3DRender::Render::LineWidth &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14RenderStateSet8addStateINS0_9LineWidthEEEvRKT_(
    Qt3DRender::Render::RenderStateSet *self,
    const Qt3DRender::Render::LineWidth *state) {
  self->addState<Qt3DRender::Render::LineWidth>(*state);
}
