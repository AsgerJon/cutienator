//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGRhiGraphicsPipelineStatePrivate::setShaderPipeline(QSSGRhiGraphi
//      csPipelineState &ps, const QSSGRhiShaderPipeline *pipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QSSGRhiGraphicsPipelineStatePrivate17setShaderPipelineER28QSSGRhiGraphicsPipelineStatePK21QSSGRhiShaderPipeline(
    QSSGRhiGraphicsPipelineState *ps,
    const QSSGRhiShaderPipeline *pipeline) {
  QSSGRhiGraphicsPipelineStatePrivate::setShaderPipeline(*ps, pipeline);
}

//  const QSSGRhiShaderPipeline
//      *QSSGRhiGraphicsPipelineStatePrivate::getShaderPipeline(const
//      QSSGRhiGraphicsPipelineState &ps)
extern "C" Q_DECL_EXPORT
const QSSGRhiShaderPipeline *ritual_ZN35QSSGRhiGraphicsPipelineStatePrivate17getShaderPipelineERK28QSSGRhiGraphicsPipelineState(
    const QSSGRhiGraphicsPipelineState *ps) {
  return QSSGRhiGraphicsPipelineStatePrivate::getShaderPipeline(*ps);
}

//  QSSGRhiGraphicsPipelineStatePrivate::~QSSGRhiGraphicsPipelineStatePrivate
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QSSGRhiGraphicsPipelineStatePrivateD1Ev(
    QSSGRhiGraphicsPipelineStatePrivate *self) {
  delete self;
}
