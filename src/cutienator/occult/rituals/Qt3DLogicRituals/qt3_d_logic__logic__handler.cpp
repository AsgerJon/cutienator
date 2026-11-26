//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DLogic/6.12.0/Qt3DLogic/private/handler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DLogic/Qt3DLogic>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/6.12.0/Qt3DLogic/private/handler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/private/manager_p.h>
#include <Qt3DLogic/qlogicaspect.h>
#include <QtCore/QDebug>
#include <QtCore/QThread>
#include <QtCore/qcoreapplication.h>
#include <Qt3DCore/private/qabstractaspect_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/private/managers_p.h>
#include <Qt3DLogic/private/handler_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DLogic/private/manager_p.h>
#include <Qt3DLogic/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/logic/manager.cpp, line 38, as _ZN9Qt3DLogic5Logic7Manager13appendHandlerEPNS0_7HandlerE
namespace Qt3DLogic::Logic {
inline void Manager::appendHandler(Handler *handler)
{
    HHandler handle = m_logicHandlerManager->lookupHandle(handler->peerId());
    if (!m_logicHandlers.contains(handle)) {
        m_logicHandlers.append(handle);
        m_logicComponentIds.append(handler->peerId());
    }
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/handler.cpp, line 16, as _ZN9Qt3DLogic5Logic7HandlerC1Ev
namespace Qt3DLogic::Logic {
inline Handler::Handler()
    : m_logicManager(nullptr)
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/handler.cpp, line 21, as _ZN9Qt3DLogic5Logic7Handler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DLogic::Logic {
inline void Handler::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    Q_UNUSED(frontEnd);
    if (firstTime)
        m_logicManager->appendHandler(this);
}
}  // namespace Qt3DLogic::Logic
//  -----------------------------------------------------------------------

//  Qt3DLogic::Logic::Handler::Handler()
extern "C" Q_DECL_EXPORT
Qt3DLogic::Logic::Handler *ritual_ZN9Qt3DLogic5Logic7HandlerC1Ev() {
  return new Qt3DLogic::Logic::Handler();
}

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

//  void Qt3DLogic::Logic::Handler::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Handler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DLogic::Logic::Handler *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DLogic::Logic::Handler::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DLogic5Logic7Handler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DLogic::Logic::Handler *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DLogic::Logic::Handler::syncFromFrontEnd(frontEnd, firstTime);
}
