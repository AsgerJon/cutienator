//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGBakedLightingModel::QSSGBakedLightingModel(const QSSGRenderModel
//      *model, const QVector<QSSGRenderableObjectHandle> &renderables)
extern "C" Q_DECL_EXPORT
QSSGBakedLightingModel *ritual_ZN22QSSGBakedLightingModelC1EPK15QSSGRenderModelRK5QListI26QSSGRenderableObjectHandleE(
    const QSSGRenderModel *model,
    const QVector<QSSGRenderableObjectHandle> *renderables) {
  return new QSSGBakedLightingModel(model, *renderables);
}

//  QSSGBakedLightingModel::~QSSGBakedLightingModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGBakedLightingModelD1Ev(QSSGBakedLightingModel *self) {
  delete self;
}
