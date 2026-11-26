//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DLogic/6.12.0/Qt3DLogic/private/handler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DLogic/Qt3DLogic>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/6.12.0/Qt3DLogic/private/handler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/private/handler_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DLogic/private/manager_p.h>
#include <Qt3DLogic/private/managers_p.h>
#include <Qt3DLogic/private/manager_p.h>
#include <Qt3DLogic/qlogicaspect.h>
#include <QtCore/QDebug>
#include <QtCore/QThread>
#include <QtCore/qcoreapplication.h>
#include <Qt3DCore/private/qabstractaspect_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/logic/handler.cpp, line 33, as _ZNK9Qt3DLogic5Logic14HandlerFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DLogic::Logic {
inline Qt3DCore::QBackendNode *HandlerFunctor::create(Qt3DCore::QNodeId id) const
{
    Handler *handler = m_manager->logicHandlerManager()->getOrCreateResource(id);
    handler->setManager(m_manager);
    return handler;
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/handler.cpp, line 40, as _ZNK9Qt3DLogic5Logic14HandlerFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DLogic::Logic {
inline Qt3DCore::QBackendNode *HandlerFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_manager->logicHandlerManager()->lookupResource(id);
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/handler.cpp, line 45, as _ZNK9Qt3DLogic5Logic14HandlerFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DLogic::Logic {
inline void HandlerFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_manager->removeHandler(id);
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/handler.cpp, line 16, as _ZN9Qt3DLogic5Logic7HandlerC1Ev
namespace Qt3DLogic::Logic {
inline Handler::Handler()
    : m_logicManager(nullptr)
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 47, as _ZN9Qt3DLogic5Logic7Manager13removeHandlerEN8Qt3DCore7QNodeIdE
namespace Qt3DLogic::Logic {
inline void Manager::removeHandler(Qt3DCore::QNodeId id)
{
    HHandler handle = m_logicHandlerManager->lookupHandle(id);
    m_logicComponentIds.removeAll(id);
    m_logicHandlers.removeAll(handle);
    m_logicHandlerManager->releaseResource(id);
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

//  from ../qt3d/src/logic/handler.cpp, line 28, as _ZN9Qt3DLogic5Logic14HandlerFunctorC1EPNS0_7ManagerE
namespace Qt3DLogic::Logic {
inline HandlerFunctor::HandlerFunctor(Manager *manager)
    : m_manager(manager)
{
}
}  // namespace Qt3DLogic::Logic
//  -----------------------------------------------------------------------

//  Qt3DLogic::Logic::HandlerFunctor::HandlerFunctor(Manager *handler)
extern "C" Q_DECL_EXPORT
Qt3DLogic::Logic::HandlerFunctor *ritual_ZN9Qt3DLogic5Logic14HandlerFunctorC1EPNS0_7ManagerE(
    Qt3DLogic::Logic::Manager *handler) {
  return new Qt3DLogic::Logic::HandlerFunctor(handler);
}

//  Qt3DCore::QBackendNode
//      *Qt3DLogic::Logic::HandlerFunctor::create(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DLogic5Logic14HandlerFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DLogic::Logic::HandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DLogic::Logic::HandlerFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DLogic5Logic14HandlerFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DLogic::Logic::HandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DLogic::Logic::HandlerFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9Qt3DLogic5Logic14HandlerFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DLogic::Logic::HandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DLogic::Logic::HandlerFunctor::~HandlerFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic14HandlerFunctorD1Ev(
    Qt3DLogic::Logic::HandlerFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DLogic::Logic::HandlerFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DLogic5Logic14HandlerFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DLogic::Logic::HandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DLogic::Logic::HandlerFunctor::get(*id);
}

//  void Qt3DLogic::Logic::HandlerFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9Qt3DLogic5Logic14HandlerFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DLogic::Logic::HandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DLogic::Logic::HandlerFunctor::destroy(*id);
}
