//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/attachmentpack_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/attachmentpack_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::AttachmentPack::AttachmentPack()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::AttachmentPack *ritual_ZN10Qt3DRender6Render14AttachmentPackC1Ev() {
  return new Qt3DRender::Render::AttachmentPack();
}

//  Qt3DRender::Render::AttachmentPack::AttachmentPack(const RenderTarget
//      *target, AttachmentManager *attachmentManager, const
//      QList<QRenderTargetOutput::AttachmentPoint> &drawBuffers)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::AttachmentPack *ritual_ZN10Qt3DRender6Render14AttachmentPackC1EPKNS0_12RenderTargetEPNS0_17AttachmentManagerERK5QListINS_19QRenderTargetOutput15AttachmentPointEE(
    const Qt3DRender::Render::RenderTarget *target,
    Qt3DRender::Render::AttachmentManager *attachmentManager,
    const QList<Qt3DRender::QRenderTargetOutput::AttachmentPoint> *drawBuffers) {
  return new Qt3DRender::Render::AttachmentPack(
      target,
      attachmentManager,
      *drawBuffers);
}

//  const std::vector<Attachment>
//      &Qt3DRender::Render::AttachmentPack::attachments() const
extern "C" Q_DECL_EXPORT
const std::vector<Qt3DRender::Render::Attachment> *ritual_ZNK10Qt3DRender6Render14AttachmentPack11attachmentsEv(
    const Qt3DRender::Render::AttachmentPack *self) {
  return &(self->attachments());
}

//  const std::vector<QRenderTargetOutput::AttachmentPoint>
//      &Qt3DRender::Render::AttachmentPack::getDrawBuffers() const
extern "C" Q_DECL_EXPORT
const std::vector<Qt3DRender::QRenderTargetOutput::AttachmentPoint> *ritual_ZNK10Qt3DRender6Render14AttachmentPack14getDrawBuffersEv(
    const Qt3DRender::Render::AttachmentPack *self) {
  return &(self->getDrawBuffers());
}

//  int Qt3DRender::Render::AttachmentPack::getDrawBufferIndex(QRenderTargetO
//      utput::AttachmentPoint attachmentPoint) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render14AttachmentPack18getDrawBufferIndexENS_19QRenderTargetOutput15AttachmentPointE(
    const Qt3DRender::Render::AttachmentPack *self,
    Qt3DRender::QRenderTargetOutput::AttachmentPoint attachmentPoint) {
  return self->getDrawBufferIndex(attachmentPoint);
}

//  Qt3DRender::Render::AttachmentPack::~AttachmentPack()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14AttachmentPackD1Ev(
    Qt3DRender::Render::AttachmentPack *self) {
  delete self;
}
