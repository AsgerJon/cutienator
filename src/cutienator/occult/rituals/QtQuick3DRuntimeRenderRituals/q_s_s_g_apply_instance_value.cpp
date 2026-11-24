//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGApplyInstanceValue::QSSGApplyInstanceValue(const QByteArray &inName,
//      QSSGRenderShaderValue::Type inValueType, quint32 inValueOffset)
extern "C" Q_DECL_EXPORT
QSSGApplyInstanceValue *ritual_ZN22QSSGApplyInstanceValueC1ERK10QByteArrayN21QSSGRenderShaderValue4TypeEj(
    const QByteArray *inName,
    QSSGRenderShaderValue::Type inValueType,
    quint32 inValueOffset) {
  return new QSSGApplyInstanceValue(*inName, inValueType, inValueOffset);
}

//  QSSGApplyInstanceValue::QSSGApplyInstanceValue()
extern "C" Q_DECL_EXPORT
QSSGApplyInstanceValue *ritual_ZN22QSSGApplyInstanceValueC1Ev() {
  return new QSSGApplyInstanceValue();
}

//  QSSGApplyInstanceValue::QSSGApplyInstanceValue(const
//      QSSGApplyInstanceValue &command)
extern "C" Q_DECL_EXPORT
QSSGApplyInstanceValue *ritual_ZN22QSSGApplyInstanceValueC1ERKS_(
    const QSSGApplyInstanceValue *command) {
  return new QSSGApplyInstanceValue(*command);
}

//  QSSGApplyInstanceValue::~QSSGApplyInstanceValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGApplyInstanceValueD1Ev(QSSGApplyInstanceValue *self) {
  delete self;
}
