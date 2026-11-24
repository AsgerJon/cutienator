//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>

//  QMatrix4x4 QSSGModelHelpers::getGlobalTransform(const QSSGFrameData
//      &frameData, QSSGNodeId model, QSSGPrepContextId prepId)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN16QSSGModelHelpers18getGlobalTransformERK13QSSGFrameData10QSSGNodeId17QSSGPrepContextId(
    const QSSGFrameData *frameData,
    QSSGNodeId model,
    QSSGPrepContextId prepId) {
  return new QMatrix4x4(
      QSSGModelHelpers::getGlobalTransform(
          *frameData,
          model,
          prepId));
}

//  QMatrix4x4 QSSGModelHelpers::getLocalTransform(const QSSGFrameData
//      &frameData, QSSGNodeId model)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN16QSSGModelHelpers17getLocalTransformERK13QSSGFrameData10QSSGNodeId(
    const QSSGFrameData *frameData,
    QSSGNodeId model) {
  return new QMatrix4x4(
      QSSGModelHelpers::getLocalTransform(
          *frameData,
          model));
}

//  float QSSGModelHelpers::getGlobalOpacity(const QSSGFrameData &frameData,
//      QSSGNodeId model)
extern "C" Q_DECL_EXPORT
float ritual_ZN16QSSGModelHelpers16getGlobalOpacityERK13QSSGFrameData10QSSGNodeId(
    const QSSGFrameData *frameData,
    QSSGNodeId model) {
  return QSSGModelHelpers::getGlobalOpacity(*frameData, model);
}

//  float QSSGModelHelpers::getGlobalOpacity(const QSSGFrameData &frameData,
//      QSSGNodeId model, QSSGPrepContextId prepId)
extern "C" Q_DECL_EXPORT
float ritual_ZN16QSSGModelHelpers16getGlobalOpacityERK13QSSGFrameData10QSSGNodeId17QSSGPrepContextId(
    const QSSGFrameData *frameData,
    QSSGNodeId model,
    QSSGPrepContextId prepId) {
  return QSSGModelHelpers::getGlobalOpacity(*frameData, model, prepId);
}

//  float QSSGModelHelpers::getLocalOpacity(const QSSGFrameData &frameData,
//      QSSGNodeId model)
extern "C" Q_DECL_EXPORT
float ritual_ZN16QSSGModelHelpers15getLocalOpacityERK13QSSGFrameData10QSSGNodeId(
    const QSSGFrameData *frameData,
    QSSGNodeId model) {
  return QSSGModelHelpers::getLocalOpacity(*frameData, model);
}

//  void QSSGModelHelpers::setGlobalTransform(const QSSGFrameData &frameData,
//      QSSGRenderablesId prepId, QSSGNodeId model, const QMatrix4x4
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGModelHelpers18setGlobalTransformERK13QSSGFrameData17QSSGRenderablesId10QSSGNodeIdRK10QMatrix4x4(
    const QSSGFrameData *frameData,
    QSSGRenderablesId prepId,
    QSSGNodeId model,
    const QMatrix4x4 *transform) {
  QSSGModelHelpers::setGlobalTransform(
      *frameData,
      prepId,
      model,
      *transform);
}

//  void QSSGModelHelpers::setGlobalOpacity(const QSSGFrameData &frameData,
//      QSSGRenderablesId renderablesId, QSSGNodeId model, float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGModelHelpers16setGlobalOpacityERK13QSSGFrameData17QSSGRenderablesId10QSSGNodeIdf(
    const QSSGFrameData *frameData,
    QSSGRenderablesId renderablesId,
    QSSGNodeId model,
    float opacity) {
  QSSGModelHelpers::setGlobalOpacity(
      *frameData,
      renderablesId,
      model,
      opacity);
}

//  QSSGModelHelpers::~QSSGModelHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGModelHelpersD1Ev(QSSGModelHelpers *self) {
  delete self;
}
