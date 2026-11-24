//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGAddShaderDefine::QSSGAddShaderDefine()
extern "C" Q_DECL_EXPORT
QSSGAddShaderDefine *ritual_ZN19QSSGAddShaderDefineC1Ev() {
  return new QSSGAddShaderDefine();
}

//  QSSGAddShaderDefine::QSSGAddShaderDefine(const QByteArray &name, int
//      value)
extern "C" Q_DECL_EXPORT
QSSGAddShaderDefine *ritual_ZN19QSSGAddShaderDefineC1ERK10QByteArrayi(
    const QByteArray *name,
    int value) {
  return new QSSGAddShaderDefine(*name, value);
}

//  QSSGAddShaderDefine::~QSSGAddShaderDefine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGAddShaderDefineD1Ev(QSSGAddShaderDefine *self) {
  delete self;
}
