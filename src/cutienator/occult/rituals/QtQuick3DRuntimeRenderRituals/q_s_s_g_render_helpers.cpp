//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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
