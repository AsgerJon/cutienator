//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGShaderKeyDiffuseModel::QSSGShaderKeyDiffuseModel(const char *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyDiffuseModel *ritual_ZN25QSSGShaderKeyDiffuseModelC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyDiffuseModel(inName);
}

//  QSSGShaderKeyDiffuseModel::~QSSGShaderKeyDiffuseModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGShaderKeyDiffuseModelD1Ev(
    QSSGShaderKeyDiffuseModel *self) {
  delete self;
}
