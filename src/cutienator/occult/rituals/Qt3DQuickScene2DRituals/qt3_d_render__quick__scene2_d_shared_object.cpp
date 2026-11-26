//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2dsharedobject_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2d_global_p.h>
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2dsharedobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Quick::Scene2DSharedObject::Scene2DSharedObject(Scene2DManage
//      r *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Quick::Scene2DSharedObject *ritual_ZN10Qt3DRender5Quick19Scene2DSharedObjectC1EPNS0_14Scene2DManagerE(
    Qt3DRender::Quick::Scene2DManager *manager) {
  return new Qt3DRender::Quick::Scene2DSharedObject(manager);
}

//  Qt3DRender::Quick::Scene2DSharedObject::~Scene2DSharedObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObjectD1Ev(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  delete self;
}

//  bool Qt3DRender::Quick::Scene2DSharedObject::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject13isInitializedEv(
    const Qt3DRender::Quick::Scene2DSharedObject *self) {
  return self->isInitialized();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::setInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject14setInitializedEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->setInitialized();
}

//  bool Qt3DRender::Quick::Scene2DSharedObject::isQuitting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject10isQuittingEv(
    const Qt3DRender::Quick::Scene2DSharedObject *self) {
  return self->isQuitting();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::setQuitting()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject11setQuittingEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->setQuitting();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::requestQuit()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject11requestQuitEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->requestQuit();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::requestInvalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject17requestInvalidateEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->requestInvalidate();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::requestRender(bool sync)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject13requestRenderEb(
    Qt3DRender::Quick::Scene2DSharedObject *self,
    bool sync) {
  self->requestRender(sync);
}

//  bool Qt3DRender::Quick::Scene2DSharedObject::isSyncRequested() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject15isSyncRequestedEv(
    const Qt3DRender::Quick::Scene2DSharedObject *self) {
  return self->isSyncRequested();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::clearSyncRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject16clearSyncRequestEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->clearSyncRequest();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::wait()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject4waitEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->wait();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::wake()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject4wakeEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->wake();
}

//  bool Qt3DRender::Quick::Scene2DSharedObject::isPrepared() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject10isPreparedEv(
    const Qt3DRender::Quick::Scene2DSharedObject *self) {
  return self->isPrepared();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::setPrepared()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject11setPreparedEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->setPrepared();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::disallowRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject14disallowRenderEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->disallowRender();
}

//  bool Qt3DRender::Quick::Scene2DSharedObject::canRender() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject9canRenderEv(
    const Qt3DRender::Quick::Scene2DSharedObject *self) {
  return self->canRender();
}

//  void Qt3DRender::Quick::Scene2DSharedObject::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject7cleanupEv(
    Qt3DRender::Quick::Scene2DSharedObject *self) {
  self->cleanup();
}
