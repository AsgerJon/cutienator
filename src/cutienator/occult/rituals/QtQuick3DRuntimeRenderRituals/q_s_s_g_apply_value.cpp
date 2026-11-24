//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGApplyValue::QSSGApplyValue(const QByteArray &inName)
extern "C" Q_DECL_EXPORT
QSSGApplyValue *ritual_ZN14QSSGApplyValueC1ERK10QByteArray(
    const QByteArray *inName) {
  return new QSSGApplyValue(*inName);
}

//  QSSGApplyValue::QSSGApplyValue(const QSSGApplyValue &command)
extern "C" Q_DECL_EXPORT
QSSGApplyValue *ritual_ZN14QSSGApplyValueC1ERKS_(
    const QSSGApplyValue *command) {
  return new QSSGApplyValue(*command);
}

//  QSSGApplyValue::QSSGApplyValue()
extern "C" Q_DECL_EXPORT
QSSGApplyValue *ritual_ZN14QSSGApplyValueC1Ev() {
  return new QSSGApplyValue();
}

//  QSSGApplyValue::~QSSGApplyValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGApplyValueD1Ev(QSSGApplyValue *self) {
  delete self;
}
