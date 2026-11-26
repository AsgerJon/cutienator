//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const InputAssemblerState &QSSGRhiInputAssemblerStatePrivate::get(const
//      QSSGRhiGraphicsPipelineState &ps)
extern "C" Q_DECL_EXPORT
const QSSGRhiInputAssemblerStatePrivate::InputAssemblerState *ritual_ZN33QSSGRhiInputAssemblerStatePrivate3getERK28QSSGRhiGraphicsPipelineState(
    const QSSGRhiGraphicsPipelineState *ps) {
  return &(QSSGRhiInputAssemblerStatePrivate::get(*ps));
}

//  InputAssemblerState
//      &QSSGRhiInputAssemblerStatePrivate::get(QSSGRhiGraphicsPipelineState
//      &ps)
extern "C" Q_DECL_EXPORT
QSSGRhiInputAssemblerStatePrivate::InputAssemblerState *ritual_ZN33QSSGRhiInputAssemblerStatePrivate3getER28QSSGRhiGraphicsPipelineState(
    QSSGRhiGraphicsPipelineState *ps) {
  return &(QSSGRhiInputAssemblerStatePrivate::get(*ps));
}

//  QSSGRhiInputAssemblerStatePrivate::~QSSGRhiInputAssemblerStatePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QSSGRhiInputAssemblerStatePrivateD1Ev(
    QSSGRhiInputAssemblerStatePrivate *self) {
  delete self;
}
