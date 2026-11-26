//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGApplyBufferValue::QSSGApplyBufferValue(const QByteArray &bufferName,
//      const QByteArray &shaderSampler)
extern "C" Q_DECL_EXPORT
QSSGApplyBufferValue *ritual_ZN20QSSGApplyBufferValueC1ERK10QByteArrayS2_(
    const QByteArray *bufferName,
    const QByteArray *shaderSampler) {
  return new QSSGApplyBufferValue(*bufferName, *shaderSampler);
}

//  void QSSGApplyBufferValue::addDebug(QDebug &stream) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QSSGApplyBufferValue8addDebugER6QDebug(
    const QSSGApplyBufferValue *self,
    QDebug *stream) {
  self->addDebug(*stream);
}

//  QSSGApplyBufferValue::QSSGApplyBufferValue(const QSSGApplyBufferValue
//      &command)
extern "C" Q_DECL_EXPORT
QSSGApplyBufferValue *ritual_ZN20QSSGApplyBufferValueC1ERKS_(
    const QSSGApplyBufferValue *command) {
  return new QSSGApplyBufferValue(*command);
}

//  QSSGApplyBufferValue::~QSSGApplyBufferValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGApplyBufferValueD1Ev(QSSGApplyBufferValue *self) {
  delete self;
}
