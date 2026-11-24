//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>

//  QSSGBaseTypeProperty::QSSGBaseTypeProperty()
extern "C" Q_DECL_EXPORT
QSSGBaseTypeProperty *ritual_ZN20QSSGBaseTypePropertyC1Ev() {
  return new QSSGBaseTypeProperty();
}

//  QSSGBaseTypeProperty::QSSGBaseTypeProperty(const QByteArray &name, const
//      QByteArray &typeName, const QVariant &value,
//      QSSGRenderShaderValue::Type shaderDataType, int pid)
extern "C" Q_DECL_EXPORT
QSSGBaseTypeProperty *ritual_ZN20QSSGBaseTypePropertyC1ERK10QByteArrayS2_RK8QVariantN21QSSGRenderShaderValue4TypeEi(
    const QByteArray *name,
    const QByteArray *typeName,
    const QVariant *value,
    QSSGRenderShaderValue::Type shaderDataType,
    int pid) {
  return new QSSGBaseTypeProperty(
      *name,
      *typeName,
      *value,
      shaderDataType,
      pid);
}

//  QSSGBaseTypeProperty::~QSSGBaseTypeProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGBaseTypePropertyD1Ev(QSSGBaseTypeProperty *self) {
  delete self;
}
