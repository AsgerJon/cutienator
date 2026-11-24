//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGFrameData::scheduleRenderResults(RenderResults results) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QSSGFrameData21scheduleRenderResultsE6QFlagsINS_12RenderResultEE(
    const QSSGFrameData *self,
    int results) {
  self->scheduleRenderResults(
      QFlags<QSSGFrameData::RenderResult>::fromInt(results));
}

//  Result QSSGFrameData::getRenderResult(RenderResult id) const
extern "C" Q_DECL_EXPORT
QSSGFrameData::Result *ritual_ZNK13QSSGFrameData15getRenderResultENS_12RenderResultE(
    const QSSGFrameData *self,
    QSSGFrameData::RenderResult id) {
  return new QSSGFrameData::Result(self->getRenderResult(id));
}

//  Result QSSGFrameData::getRenderResult(QSSGResourceId userPassId,
//      AttachmentSelector attachment) const
extern "C" Q_DECL_EXPORT
QSSGFrameData::Result *ritual_ZNK13QSSGFrameData15getRenderResultE14QSSGResourceIdNS_18AttachmentSelectorE(
    const QSSGFrameData *self,
    QSSGResourceId userPassId,
    QSSGFrameData::AttachmentSelector attachment) {
  return new QSSGFrameData::Result(
      self->getRenderResult(
          userPassId,
          attachment));
}

//  qsizetype QSSGFrameData::getAttachmentCount(QSSGResourceId userPassId)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QSSGFrameData18getAttachmentCountE14QSSGResourceId(
    const QSSGFrameData *self,
    QSSGResourceId userPassId) {
  return self->getAttachmentCount(userPassId);
}

//  QSSGRhiGraphicsPipelineState QSSGFrameData::getPipelineState() const
extern "C" Q_DECL_EXPORT
QSSGRhiGraphicsPipelineState *ritual_ZNK13QSSGFrameData16getPipelineStateEv(
    const QSSGFrameData *self) {
  return new QSSGRhiGraphicsPipelineState(self->getPipelineState());
}

//  QSSGCameraId QSSGFrameData::activeCamera() const
extern "C" Q_DECL_EXPORT
QSSGCameraId ritual_ZNK13QSSGFrameData12activeCameraEv(
    const QSSGFrameData *self) {
  return self->activeCamera();
}

//  QSSGRenderContextInterface *QSSGFrameData::contextInterface() const
extern "C" Q_DECL_EXPORT
QSSGRenderContextInterface *ritual_ZNK13QSSGFrameData16contextInterfaceEv(
    const QSSGFrameData *self) {
  return self->contextInterface();
}

//  void QSSGFrameData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGFrameData5clearEv(QSSGFrameData *self) {
  self->clear();
}

//  QSSGLayerRenderData *QSSGFrameData::getCurrent() const
extern "C" Q_DECL_EXPORT
QSSGLayerRenderData *ritual_ZNK13QSSGFrameData10getCurrentEv(
    const QSSGFrameData *self) {
  return self->getCurrent();
}

//  void QSSGFrameData::scheduleRenderResults(QSSGResourceId userPassId)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QSSGFrameData21scheduleRenderResultsE14QSSGResourceId(
    const QSSGFrameData *self,
    QSSGResourceId userPassId) {
  self->scheduleRenderResults(userPassId);
}

//  QSSGFrameData::QSSGFrameData()
extern "C" Q_DECL_EXPORT
QSSGFrameData *ritual_ZN13QSSGFrameDataC1Ev() {
  return new QSSGFrameData();
}

//  QSSGFrameData::QSSGFrameData(QSSGRenderContextInterface *ctx)
extern "C" Q_DECL_EXPORT
QSSGFrameData *ritual_ZN13QSSGFrameDataC1EP26QSSGRenderContextInterface(
    QSSGRenderContextInterface *ctx) {
  return new QSSGFrameData(ctx);
}

//  QSSGFrameData::~QSSGFrameData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGFrameDataD1Ev(QSSGFrameData *self) {
  delete self;
}
