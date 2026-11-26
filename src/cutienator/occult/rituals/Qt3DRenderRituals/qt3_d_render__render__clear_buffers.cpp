//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/clearbuffers_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/clearbuffers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>

//  Qt3DRender::Render::ClearBuffers::ClearBuffers()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ClearBuffers *ritual_ZN10Qt3DRender6Render12ClearBuffersC1Ev() {
  return new Qt3DRender::Render::ClearBuffers();
}

//  QClearBuffers::BufferType Qt3DRender::Render::ClearBuffers::type() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QClearBuffers::BufferType ritual_ZNK10Qt3DRender6Render12ClearBuffers4typeEv(
    const Qt3DRender::Render::ClearBuffers *self) {
  return self->type();
}

//  float Qt3DRender::Render::ClearBuffers::clearDepthValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render12ClearBuffers15clearDepthValueEv(
    const Qt3DRender::Render::ClearBuffers *self) {
  return self->clearDepthValue();
}

//  int Qt3DRender::Render::ClearBuffers::clearStencilValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12ClearBuffers17clearStencilValueEv(
    const Qt3DRender::Render::ClearBuffers *self) {
  return self->clearStencilValue();
}

//  Qt3DCore::QNodeId Qt3DRender::Render::ClearBuffers::bufferId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render12ClearBuffers8bufferIdEv(
    const Qt3DRender::Render::ClearBuffers *self) {
  return new Qt3DCore::QNodeId(self->bufferId());
}

//  QVector4D Qt3DRender::Render::ClearBuffers::clearColor() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK10Qt3DRender6Render12ClearBuffers10clearColorEv(
    const Qt3DRender::Render::ClearBuffers *self) {
  return new QVector4D(self->clearColor());
}

//  QColor Qt3DRender::Render::ClearBuffers::clearColorAsColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DRender6Render12ClearBuffers17clearColorAsColorEv(
    const Qt3DRender::Render::ClearBuffers *self) {
  return new QColor(self->clearColorAsColor());
}

//  bool Qt3DRender::Render::ClearBuffers::clearsAllColorBuffers() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12ClearBuffers21clearsAllColorBuffersEv(
    const Qt3DRender::Render::ClearBuffers *self) {
  return self->clearsAllColorBuffers();
}

//  void Qt3DRender::Render::ClearBuffers::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ClearBuffers16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ClearBuffers *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::ClearBuffers::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render12ClearBuffers16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ClearBuffers *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::ClearBuffers::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
