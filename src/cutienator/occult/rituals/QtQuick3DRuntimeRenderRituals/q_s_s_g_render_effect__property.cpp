//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendereffect_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendereffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>

//  QSSGRenderEffect::Property::Property()
extern "C" Q_DECL_EXPORT
QSSGRenderEffect::Property *ritual_ZN16QSSGRenderEffect8PropertyC1Ev() {
  return new QSSGRenderEffect::Property();
}

//  QSSGRenderEffect::Property::Property(const QByteArray &name, const
//      QByteArray &typeName, const QVariant &value,
//      QSSGRenderShaderValue::Type shaderDataType, int pid)
extern "C" Q_DECL_EXPORT
QSSGRenderEffect::Property *ritual_ZN16QSSGRenderEffect8PropertyC1ERK10QByteArrayS3_RK8QVariantN21QSSGRenderShaderValue4TypeEi(
    const QByteArray *name,
    const QByteArray *typeName,
    const QVariant *value,
    QSSGRenderShaderValue::Type shaderDataType,
    int pid) {
  return new QSSGRenderEffect::Property(
      *name,
      *typeName,
      *value,
      shaderDataType,
      pid);
}

//  QSSGRenderEffect::Property::~Property()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderEffect8PropertyD1Ev(
    QSSGRenderEffect::Property *self) {
  delete self;
}
