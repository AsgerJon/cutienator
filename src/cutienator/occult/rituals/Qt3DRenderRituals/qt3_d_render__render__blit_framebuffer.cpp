//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/blitframebuffer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/blitframebuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qrect.h>

//  Qt3DRender::Render::BlitFramebuffer::BlitFramebuffer()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::BlitFramebuffer *ritual_ZN10Qt3DRender6Render15BlitFramebufferC1Ev() {
  return new Qt3DRender::Render::BlitFramebuffer();
}

//  void Qt3DRender::Render::BlitFramebuffer::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15BlitFramebuffer16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::BlitFramebuffer *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  Qt3DCore::QNodeId
//      Qt3DRender::Render::BlitFramebuffer::sourceRenderTargetId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render15BlitFramebuffer20sourceRenderTargetIdEv(
    const Qt3DRender::Render::BlitFramebuffer *self) {
  return new Qt3DCore::QNodeId(self->sourceRenderTargetId());
}

//  Qt3DCore::QNodeId
//      Qt3DRender::Render::BlitFramebuffer::destinationRenderTargetId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render15BlitFramebuffer25destinationRenderTargetIdEv(
    const Qt3DRender::Render::BlitFramebuffer *self) {
  return new Qt3DCore::QNodeId(self->destinationRenderTargetId());
}

//  QRect Qt3DRender::Render::BlitFramebuffer::sourceRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK10Qt3DRender6Render15BlitFramebuffer10sourceRectEv(
    const Qt3DRender::Render::BlitFramebuffer *self) {
  return new QRect(self->sourceRect());
}

//  QRect Qt3DRender::Render::BlitFramebuffer::destinationRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK10Qt3DRender6Render15BlitFramebuffer15destinationRectEv(
    const Qt3DRender::Render::BlitFramebuffer *self) {
  return new QRect(self->destinationRect());
}

//  Qt3DRender::QRenderTargetOutput::AttachmentPoint
//      Qt3DRender::Render::BlitFramebuffer::sourceAttachmentPoint() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput::AttachmentPoint ritual_ZNK10Qt3DRender6Render15BlitFramebuffer21sourceAttachmentPointEv(
    const Qt3DRender::Render::BlitFramebuffer *self) {
  return self->sourceAttachmentPoint();
}

//  Qt3DRender::QRenderTargetOutput::AttachmentPoint
//      Qt3DRender::Render::BlitFramebuffer::destinationAttachmentPoint()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput::AttachmentPoint ritual_ZNK10Qt3DRender6Render15BlitFramebuffer26destinationAttachmentPointEv(
    const Qt3DRender::Render::BlitFramebuffer *self) {
  return self->destinationAttachmentPoint();
}

//  QBlitFramebuffer::InterpolationMethod
//      Qt3DRender::Render::BlitFramebuffer::interpolationMethod() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlitFramebuffer::InterpolationMethod ritual_ZNK10Qt3DRender6Render15BlitFramebuffer19interpolationMethodEv(
    const Qt3DRender::Render::BlitFramebuffer *self) {
  return self->interpolationMethod();
}

//  void Qt3DRender::Render::BlitFramebuffer::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render15BlitFramebuffer16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::BlitFramebuffer *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::BlitFramebuffer::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
