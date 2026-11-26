//  Written by hand on 2026-11-25 from
//  Qt3DRender/6.12.0/Qt3DRender/private/vsyncframeadvanceservice_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  The class is final: there is no Cute class and no 'take', and the
//  virtual functions, final too, are only called through the object.
//  Not written: 'metaObject' and 'tr' (the class has no Q_OBJECT of its
//  own), 'd_func' (its private class is not complete in any header Qt
//  installs).
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/vsyncframeadvanceservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::VSyncFrameAdvanceService::VSyncFrameAdvanceService(bool
//      drivenByRenderThread)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::VSyncFrameAdvanceService *ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceServiceC1Eb(
    bool drivenByRenderThread) {
  return new Qt3DRender::Render::VSyncFrameAdvanceService(drivenByRenderThread);
}

//  Qt3DRender::Render::VSyncFrameAdvanceService::~VSyncFrameAdvanceService()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceServiceD1Ev(
    Qt3DRender::Render::VSyncFrameAdvanceService *self) {
  delete self;
}

//  qint64 Qt3DRender::Render::VSyncFrameAdvanceService::waitForNextFrame()
extern "C" Q_DECL_EXPORT
long long ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceService16waitForNextFrameEv(
    Qt3DRender::Render::VSyncFrameAdvanceService *self) {
  return self->waitForNextFrame();
}

//  void Qt3DRender::Render::VSyncFrameAdvanceService::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceService5startEv(
    Qt3DRender::Render::VSyncFrameAdvanceService *self) {
  self->start();
}

//  void Qt3DRender::Render::VSyncFrameAdvanceService::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceService4stopEv(
    Qt3DRender::Render::VSyncFrameAdvanceService *self) {
  self->stop();
}

//  void Qt3DRender::Render::VSyncFrameAdvanceService::proceedToNextFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render24VSyncFrameAdvanceService18proceedToNextFrameEv(
    Qt3DRender::Render::VSyncFrameAdvanceService *self) {
  self->proceedToNextFrame();
}
