//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderablesId QSSGRenderHelpers::createRenderables(const
//      QSSGFrameData &frameData, QSSGPrepContextId prepId, const
//      QSSGNodeIdList &nodes, CreateFlags flags)
extern "C" Q_DECL_EXPORT
QSSGRenderablesId ritual_ZN17QSSGRenderHelpers17createRenderablesERK13QSSGFrameData17QSSGPrepContextIdRK5QListI10QSSGNodeIdE6QFlagsINS_10CreateFlagEE(
    const QSSGFrameData *frameData,
    QSSGPrepContextId prepId,
    const QSSGNodeIdList *nodes,
    int flags) {
  return QSSGRenderHelpers::createRenderables(
      *frameData,
      prepId,
      *nodes,
      QFlags<QSSGRenderHelpers::CreateFlag>::fromInt(flags));
}

//  QSSGPrepContextId QSSGRenderHelpers::prepareForRender(const QSSGFrameData
//      &frameData, const QSSGRenderExtension &ext, QSSGCameraId cameraId,
//      quint32 slot)
extern "C" Q_DECL_EXPORT
QSSGPrepContextId ritual_ZN17QSSGRenderHelpers16prepareForRenderERK13QSSGFrameDataRK19QSSGRenderExtension12QSSGCameraIdj(
    const QSSGFrameData *frameData,
    const QSSGRenderExtension *ext,
    QSSGCameraId cameraId,
    quint32 slot) {
  return QSSGRenderHelpers::prepareForRender(
      *frameData,
      *ext,
      cameraId,
      slot);
}

//  QSSGPrepResultId QSSGRenderHelpers::commit(const QSSGFrameData
//      &frameData, QSSGPrepContextId prepId, QSSGRenderablesId
//      renderablesId, float lodThreshold)
extern "C" Q_DECL_EXPORT
QSSGPrepResultId ritual_ZN17QSSGRenderHelpers6commitERK13QSSGFrameData17QSSGPrepContextId17QSSGRenderablesIdf(
    const QSSGFrameData *frameData,
    QSSGPrepContextId prepId,
    QSSGRenderablesId renderablesId,
    float lodThreshold) {
  return QSSGRenderHelpers::commit(
      *frameData,
      prepId,
      renderablesId,
      lodThreshold);
}

//  void QSSGRenderHelpers::prepareRenderables(const QSSGFrameData
//      &frameData, QSSGPrepResultId prepId, QRhiRenderPassDescriptor
//      *renderPassDescriptor, QSSGRhiGraphicsPipelineState &ps,
//      QSSGRenderablesFilters filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGRenderHelpers18prepareRenderablesERK13QSSGFrameData16QSSGPrepResultIdP24QRhiRenderPassDescriptorR28QSSGRhiGraphicsPipelineState6QFlagsI21QSSGRenderablesFilterE(
    const QSSGFrameData *frameData,
    QSSGPrepResultId prepId,
    QRhiRenderPassDescriptor *renderPassDescriptor,
    QSSGRhiGraphicsPipelineState *ps,
    int filter) {
  QSSGRenderHelpers::prepareRenderables(
      *frameData,
      prepId,
      renderPassDescriptor,
      *ps,
      QFlags<QSSGRenderablesFilter>::fromInt(filter));
}

//  void QSSGRenderHelpers::renderRenderables(const QSSGFrameData &frameData,
//      QSSGPrepResultId prepId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGRenderHelpers17renderRenderablesERK13QSSGFrameData16QSSGPrepResultId(
    const QSSGFrameData *frameData,
    QSSGPrepResultId prepId) {
  QSSGRenderHelpers::renderRenderables(*frameData, prepId);
}

//  QSSGRenderHelpers::QSSGRenderHelpers()
extern "C" Q_DECL_EXPORT
QSSGRenderHelpers *ritual_ZN17QSSGRenderHelpersC1Ev() {
  return new QSSGRenderHelpers();
}

//  QSSGRenderHelpers::~QSSGRenderHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGRenderHelpersD1Ev(QSSGRenderHelpers *self) {
  delete self;
}
