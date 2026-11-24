//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DLogic/6.12.0/Qt3DLogic/private/manager_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DLogic/Qt3DLogic>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/6.12.0/Qt3DLogic/private/manager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DLogic::Logic::Manager::setLogicAspect(QLogicAspect *logicAspect)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Manager14setLogicAspectEPNS_12QLogicAspectE(
    Qt3DLogic::Logic::Manager *self,
    Qt3DLogic::QLogicAspect *logicAspect) {
  self->setLogicAspect(logicAspect);
}

//  HandlerManager *Qt3DLogic::Logic::Manager::logicHandlerManager() const
extern "C" Q_DECL_EXPORT
Qt3DLogic::Logic::HandlerManager *ritual_ZNK9Qt3DLogic5Logic7Manager19logicHandlerManagerEv(
    const Qt3DLogic::Logic::Manager *self) {
  return self->logicHandlerManager();
}

//  void Qt3DLogic::Logic::Manager::setDeltaTime(float dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Manager12setDeltaTimeEf(
    Qt3DLogic::Logic::Manager *self,
    float dt) {
  self->setDeltaTime(dt);
}
