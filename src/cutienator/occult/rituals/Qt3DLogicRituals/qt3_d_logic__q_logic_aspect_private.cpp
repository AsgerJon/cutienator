//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DLogic/6.12.0/Qt3DLogic/private/qlogicaspect_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DLogic/Qt3DLogic>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/6.12.0/Qt3DLogic/private/qlogicaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/private/callbackjob_p.h>
#include <Qt3DLogic/private/job_common_p.h>
#include <Qt3DLogic/private/manager_p.h>
#include <Qt3DLogic/private/manager_p.h>
#include <Qt3DLogic/qlogicaspect.h>
#include <QtCore/QDebug>
#include <QtCore/QThread>
#include <QtCore/qcoreapplication.h>
#include <Qt3DCore/private/qabstractaspect_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/private/managers_p.h>
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/qframeaction.h>
#include <Qt3DCore/qnode.h>
#include <QtCore/qsemaphore.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DLogic/qlogicaspect.h>
#include <Qt3DLogic/private/qlogicaspect_p.h>
#include <Qt3DLogic/qframeaction.h>
#include <Qt3DCore/qnode.h>
#include <QtCore/QThread>
#include <QtGui/QWindow>
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/private/handler_p.h>
#include <Qt3DLogic/private/manager_p.h>
#include <Qt3DCore/private/qchangearbiter_p.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/private/qservicelocator_p.h>
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

//  from ../qt3d/src/logic/callbackjob.cpp, line 21, as _ZN9Qt3DLogic5Logic11CallbackJob10setManagerEPNS0_7ManagerE
namespace Qt3DLogic::Logic {
inline void CallbackJob::setManager(Manager *manager)
{
    m_logicManager = manager;
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/callbackjob.cpp, line 14, as _ZN9Qt3DLogic5Logic11CallbackJobC1Ev
namespace Qt3DLogic::Logic {
inline CallbackJob::CallbackJob()
    : QAspectJob()
    , m_logicManager(nullptr)
{
    SET_JOB_RUN_STAT_TYPE(this, JobTypes::Callback, 0)
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 33, as _ZN9Qt3DLogic5Logic7Manager11setExecutorEPNS0_8ExecutorE
namespace Qt3DLogic::Logic {
inline void Manager::setExecutor(Executor *executor)
{
    m_executor = executor;
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 21, as _ZN9Qt3DLogic5Logic7ManagerC1Ev
namespace Qt3DLogic::Logic {
inline Manager::Manager()
    : m_logicHandlerManager(new HandlerManager)
    , m_logicAspect(nullptr)
    , m_executor(nullptr)
    , m_dt(0.0f)
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 29, as _ZN9Qt3DLogic5Logic7ManagerD1Ev
namespace Qt3DLogic::Logic {
inline Manager::~Manager()
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/executor.cpp, line 20, as _ZN9Qt3DLogic5Logic8ExecutorC1EP7QObject
namespace Qt3DLogic::Logic {
using namespace Qt3DCore;
inline Executor::Executor(QObject *parent)
    : QObject(parent)
    , m_scene(nullptr)
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/qlogicaspect.cpp, line 46, as _ZN9Qt3DLogic19QLogicAspectPrivate23onEngineAboutToShutdownEv
namespace Qt3DLogic {
using namespace Qt3DCore;
inline void QLogicAspectPrivate::onEngineAboutToShutdown()
{
    m_executor->setScene(nullptr);
}
}  // namespace Qt3DLogic

//  from ../qt3d/src/logic/handler.cpp, line 28, as _ZN9Qt3DLogic5Logic14HandlerFunctorC1EPNS0_7ManagerE
namespace Qt3DLogic::Logic {
inline HandlerFunctor::HandlerFunctor(Manager *manager)
    : m_manager(manager)
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/callbackjob.cpp, line 26, as _ZN9Qt3DLogic5Logic11CallbackJob3runEv
namespace Qt3DLogic::Logic {
inline void CallbackJob::run()
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/callbackjob.cpp, line 30, as _ZN9Qt3DLogic5Logic11CallbackJob10isRequiredEv
namespace Qt3DLogic::Logic {
inline bool CallbackJob::isRequired()
{
    return false;
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/callbackjob.cpp, line 35, as _ZN9Qt3DLogic5Logic11CallbackJob9postFrameEPN8Qt3DCore13QAspectEngineE
namespace Qt3DLogic::Logic {
inline void CallbackJob::postFrame(Qt3DCore::QAspectEngine *aspectEngine)
{
    Q_UNUSED(aspectEngine);
    Q_ASSERT(m_logicManager);
    m_logicManager->triggerLogicFrameUpdates();
}
}  // namespace Qt3DLogic::Logic

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

//  from ../qt3d/src/logic/qlogicaspect.cpp, line 51, as _ZN9Qt3DLogic19QLogicAspectPrivate20registerBackendTypesEv
namespace Qt3DLogic {
using namespace Qt3DCore;
inline void QLogicAspectPrivate::registerBackendTypes()
{
    Q_Q(QLogicAspect);
    q->registerBackendType<QFrameAction>(QBackendNodeMapperPtr(new Logic::HandlerFunctor(m_manager.data())));
}
}  // namespace Qt3DLogic
//  -----------------------------------------------------------------------

//  QLogicAspect *Qt3DLogic::QLogicAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DLogic::QLogicAspect *ritual_ZN9Qt3DLogic19QLogicAspectPrivate6q_funcEv(
    Qt3DLogic::QLogicAspectPrivate *self) {
  return self->q_func();
}

//  const QLogicAspect *Qt3DLogic::QLogicAspectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DLogic::QLogicAspect *ritual_ZNK9Qt3DLogic19QLogicAspectPrivate6q_funcEv(
    const Qt3DLogic::QLogicAspectPrivate *self) {
  return self->q_func();
}

//  void Qt3DLogic::QLogicAspectPrivate::onEngineAboutToShutdown()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic19QLogicAspectPrivate23onEngineAboutToShutdownEv(
    Qt3DLogic::QLogicAspectPrivate *self) {
  self->onEngineAboutToShutdown();
}

//  void Qt3DLogic::QLogicAspectPrivate::registerBackendTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic19QLogicAspectPrivate20registerBackendTypesEv(
    Qt3DLogic::QLogicAspectPrivate *self) {
  self->registerBackendTypes();
}

//  void Qt3DLogic::QLogicAspectPrivate::onEngineAboutToShutdown()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DLogic19QLogicAspectPrivate23onEngineAboutToShutdownEv(
    Qt3DLogic::QLogicAspectPrivate *self) {
  self->Qt3DLogic::QLogicAspectPrivate::onEngineAboutToShutdown();
}
