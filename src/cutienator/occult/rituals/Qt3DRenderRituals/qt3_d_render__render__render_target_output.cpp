//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/rendertargetoutput_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/rendertargetoutput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qstring.h>

//  Qt3DRender::Render::RenderTargetOutput::RenderTargetOutput()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderTargetOutput *ritual_ZN10Qt3DRender6Render18RenderTargetOutputC1Ev() {
  return new Qt3DRender::Render::RenderTargetOutput();
}

//  Qt3DCore::QNodeId Qt3DRender::Render::RenderTargetOutput::textureUuid()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render18RenderTargetOutput11textureUuidEv(
    const Qt3DRender::Render::RenderTargetOutput *self) {
  return new Qt3DCore::QNodeId(self->textureUuid());
}

//  int Qt3DRender::Render::RenderTargetOutput::mipLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render18RenderTargetOutput8mipLevelEv(
    const Qt3DRender::Render::RenderTargetOutput *self) {
  return self->mipLevel();
}

//  int Qt3DRender::Render::RenderTargetOutput::layer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render18RenderTargetOutput5layerEv(
    const Qt3DRender::Render::RenderTargetOutput *self) {
  return self->layer();
}

//  QString Qt3DRender::Render::RenderTargetOutput::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender6Render18RenderTargetOutput4nameEv(
    const Qt3DRender::Render::RenderTargetOutput *self) {
  return new QString(self->name());
}

//  QAbstractTexture::CubeMapFace
//      Qt3DRender::Render::RenderTargetOutput::face() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::CubeMapFace ritual_ZNK10Qt3DRender6Render18RenderTargetOutput4faceEv(
    const Qt3DRender::Render::RenderTargetOutput *self) {
  return self->face();
}

//  QRenderTargetOutput::AttachmentPoint
//      Qt3DRender::Render::RenderTargetOutput::point() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput::AttachmentPoint ritual_ZNK10Qt3DRender6Render18RenderTargetOutput5pointEv(
    const Qt3DRender::Render::RenderTargetOutput *self) {
  return self->point();
}

//  void Qt3DRender::Render::RenderTargetOutput::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render18RenderTargetOutput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderTargetOutput *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  Attachment *Qt3DRender::Render::RenderTargetOutput::attachment()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Attachment *ritual_ZN10Qt3DRender6Render18RenderTargetOutput10attachmentEv(
    Qt3DRender::Render::RenderTargetOutput *self) {
  return self->attachment();
}

//  const Attachment *Qt3DRender::Render::RenderTargetOutput::attachment()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::Attachment *ritual_ZNK10Qt3DRender6Render18RenderTargetOutput10attachmentEv(
    const Qt3DRender::Render::RenderTargetOutput *self) {
  return self->attachment();
}

//  void Qt3DRender::Render::RenderTargetOutput::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render18RenderTargetOutput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderTargetOutput *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::RenderTargetOutput::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
