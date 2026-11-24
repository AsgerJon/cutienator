//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercustommaterial_p
//  .h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercustommaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>

//  QSSGRenderCustomMaterial::Property::Property()
extern "C" Q_DECL_EXPORT
QSSGRenderCustomMaterial::Property *ritual_ZN24QSSGRenderCustomMaterial8PropertyC1Ev() {
  return new QSSGRenderCustomMaterial::Property();
}

//  QSSGRenderCustomMaterial::Property::Property(const QByteArray &name,
//      const QVariant &value, QSSGRenderShaderValue::Type shaderDataType,
//      int pid)
extern "C" Q_DECL_EXPORT
QSSGRenderCustomMaterial::Property *ritual_ZN24QSSGRenderCustomMaterial8PropertyC1ERK10QByteArrayRK8QVariantN21QSSGRenderShaderValue4TypeEi(
    const QByteArray *name,
    const QVariant *value,
    QSSGRenderShaderValue::Type shaderDataType,
    int pid) {
  return new QSSGRenderCustomMaterial::Property(
      *name,
      *value,
      shaderDataType,
      pid);
}

//  QSSGRenderCustomMaterial::Property::~Property()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGRenderCustomMaterial8PropertyD1Ev(
    QSSGRenderCustomMaterial::Property *self) {
  delete self;
}
