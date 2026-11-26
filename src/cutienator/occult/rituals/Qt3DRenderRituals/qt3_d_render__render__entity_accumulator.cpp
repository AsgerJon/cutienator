//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/entityaccumulator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/entityaccumulator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <functional>
#include <QtCore/QList>

//  Qt3DRender::Render::EntityAccumulator::EntityAccumulator(NodeManagers
//      *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EntityAccumulator *ritual_ZN10Qt3DRender6Render17EntityAccumulatorC1EPNS0_12NodeManagersE(
    Qt3DRender::Render::NodeManagers *manager) {
  return new Qt3DRender::Render::EntityAccumulator(manager);
}

//  Qt3DRender::Render::EntityAccumulator::EntityAccumulator(std::function<bo
//      ol (Entity *)> predicate, NodeManagers *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EntityAccumulator *ritual_ZN10Qt3DRender6Render17EntityAccumulatorC1ESt8functionIFbPNS0_6EntityEEEPNS0_12NodeManagersE(
    const std::function<bool (Qt3DRender::Render::Entity *)> *predicate,
    Qt3DRender::Render::NodeManagers *manager) {
  return new Qt3DRender::Render::EntityAccumulator(*predicate, manager);
}

//  QList<Entity *> Qt3DRender::Render::EntityAccumulator::apply(Entity
//      *root) const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::Render::Entity *> *ritual_ZNK10Qt3DRender6Render17EntityAccumulator5applyEPNS0_6EntityE(
    const Qt3DRender::Render::EntityAccumulator *self,
    Qt3DRender::Render::Entity *root) {
  return new QList<Qt3DRender::Render::Entity *>(self->apply(root));
}

//  Qt3DRender::Render::EntityAccumulator::~EntityAccumulator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17EntityAccumulatorD1Ev(
    Qt3DRender::Render::EntityAccumulator *self) {
  delete self;
}

//  a QList<Qt3DRender::Render::Entity *> a ritual of
//      Qt3DRender::Render::EntityAccumulator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_EntityAccumulator__QList_Qt3DRender_Render_Entity(
    QList<Qt3DRender::Render::Entity *> *self) {
  delete self;
}
