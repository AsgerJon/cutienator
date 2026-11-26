//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/calcboundingvolumejob_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/calcboundingvolumejob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::CalculateBoundingVolumeJob::CalculateBoundingVolumeJo
//      b()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::CalculateBoundingVolumeJob *ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJobC1Ev() {
  return new Qt3DRender::Render::CalculateBoundingVolumeJob();
}

//  void Qt3DRender::Render::CalculateBoundingVolumeJob::setRoot(Entity
//      *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob7setRootEPNS0_6EntityE(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self,
    Qt3DRender::Render::Entity *node) {
  self->setRoot(node);
}

//  void
//      Qt3DRender::Render::CalculateBoundingVolumeJob::setManagers(NodeManag
//      ers *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob11setManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setManagers(manager);
}

//  void Qt3DRender::Render::CalculateBoundingVolumeJob::setFrontEndNodeManag
//      er(Qt3DCore::QAbstractFrontEndNodeManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob22setFrontEndNodeManagerEPN8Qt3DCore28QAbstractFrontEndNodeManagerE(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self,
    Qt3DCore::QAbstractFrontEndNodeManager *manager) {
  self->setFrontEndNodeManager(manager);
}

//  void Qt3DRender::Render::CalculateBoundingVolumeJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob3runEv(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self) {
  self->run();
}

//  void Qt3DRender::Render::CalculateBoundingVolumeJob::postFrame(Qt3DCore::
//      QAspectEngine *aspectEngine)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob9postFrameEPN8Qt3DCore13QAspectEngineE(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self,
    Qt3DCore::QAspectEngine *aspectEngine) {
  self->postFrame(aspectEngine);
}

//  void Qt3DRender::Render::CalculateBoundingVolumeJob::process(const
//      Qt3DCore::BoundingVolumeComputeResult &result, bool computedResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob7processERKN8Qt3DCore27BoundingVolumeComputeResultEb(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self,
    const Qt3DCore::BoundingVolumeComputeResult *result,
    bool computedResult) {
  self->process(*result, computedResult);
}

//  Qt3DRender::Render::CalculateBoundingVolumeJob as the
//      Qt3DCore::BoundingVolumeJobProcessor it is built on
extern "C" Q_DECL_EXPORT
Qt3DCore::BoundingVolumeJobProcessor *ritual_cast_Qt3DRender_Render_CalculateBoundingVolumeJob_Qt3DCore_BoundingVolumeJobProcessor(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self) {
  return static_cast<Qt3DCore::BoundingVolumeJobProcessor *>(self);
}

//  void Qt3DRender::Render::CalculateBoundingVolumeJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob3runEv(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self) {
  self->Qt3DRender::Render::CalculateBoundingVolumeJob::run();
}

//  void Qt3DRender::Render::CalculateBoundingVolumeJob::postFrame(Qt3DCore::
//      QAspectEngine *aspectEngine)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob9postFrameEPN8Qt3DCore13QAspectEngineE(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self,
    Qt3DCore::QAspectEngine *aspectEngine) {
  self->Qt3DRender::Render::CalculateBoundingVolumeJob::postFrame(
      aspectEngine);
}

//  void Qt3DRender::Render::CalculateBoundingVolumeJob::process(const
//      Qt3DCore::BoundingVolumeComputeResult &result, bool computedResult)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob7processERKN8Qt3DCore27BoundingVolumeComputeResultEb(
    Qt3DRender::Render::CalculateBoundingVolumeJob *self,
    const Qt3DCore::BoundingVolumeComputeResult *result,
    bool computedResult) {
  self->Qt3DRender::Render::CalculateBoundingVolumeJob::process(
      *result,
      computedResult);
}
