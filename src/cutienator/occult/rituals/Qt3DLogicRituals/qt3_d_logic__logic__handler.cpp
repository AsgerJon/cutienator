//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DLogic/6.12.0/Qt3DLogic/private/handler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DLogic/Qt3DLogic>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/6.12.0/Qt3DLogic/private/handler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DLogic::Logic::Handler::setManager(Manager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Handler10setManagerEPNS0_7ManagerE(
    Qt3DLogic::Logic::Handler *self,
    Qt3DLogic::Logic::Manager *manager) {
  self->setManager(manager);
}

//  Manager *Qt3DLogic::Logic::Handler::logicManager() const
extern "C" Q_DECL_EXPORT
Qt3DLogic::Logic::Manager *ritual_ZNK9Qt3DLogic5Logic7Handler12logicManagerEv(
    const Qt3DLogic::Logic::Handler *self) {
  return self->logicManager();
}
