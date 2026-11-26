//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/rendercapture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/rendercapture_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrendercapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>

//  Qt3DRender::Render::RenderCapture::RenderCapture()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderCapture *ritual_ZN10Qt3DRender6Render13RenderCaptureC1Ev() {
  return new Qt3DRender::Render::RenderCapture();
}

//  void Qt3DRender::Render::RenderCapture::requestCapture(const
//      QRenderCaptureRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13RenderCapture14requestCaptureERKNS_21QRenderCaptureRequestE(
    Qt3DRender::Render::RenderCapture *self,
    const Qt3DRender::QRenderCaptureRequest *request) {
  self->requestCapture(*request);
}

//  bool Qt3DRender::Render::RenderCapture::wasCaptureRequested() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render13RenderCapture19wasCaptureRequestedEv(
    const Qt3DRender::Render::RenderCapture *self) {
  return self->wasCaptureRequested();
}

//  QRenderCaptureRequest
//      Qt3DRender::Render::RenderCapture::takeCaptureRequest()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureRequest *ritual_ZN10Qt3DRender6Render13RenderCapture18takeCaptureRequestEv(
    Qt3DRender::Render::RenderCapture *self) {
  return new Qt3DRender::QRenderCaptureRequest(self->takeCaptureRequest());
}

//  void Qt3DRender::Render::RenderCapture::addRenderCapture(int captureId,
//      const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13RenderCapture16addRenderCaptureEiRK6QImage(
    Qt3DRender::Render::RenderCapture *self,
    int captureId,
    const QImage *image) {
  self->addRenderCapture(captureId, *image);
}

//  void Qt3DRender::Render::RenderCapture::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13RenderCapture16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderCapture *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::RenderCapture::syncRenderCapturesToFrontend(Qt3D
//      Core::QAspectManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13RenderCapture28syncRenderCapturesToFrontendEPN8Qt3DCore14QAspectManagerE(
    Qt3DRender::Render::RenderCapture *self,
    Qt3DCore::QAspectManager *manager) {
  self->syncRenderCapturesToFrontend(manager);
}

//  void Qt3DRender::Render::RenderCapture::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render13RenderCapture16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderCapture *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::RenderCapture::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
