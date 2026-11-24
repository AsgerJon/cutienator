//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlmetatype_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlmetatype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QQmlListMetaTypeInterface::QQmlListMetaTypeInterface(QByteArray name,
//      const QtPrivate::QMetaTypeInterface *valueType)
extern "C" Q_DECL_EXPORT
QQmlListMetaTypeInterface *ritual_ZN25QQmlListMetaTypeInterfaceC1E10QByteArrayPKN9QtPrivate18QMetaTypeInterfaceE(
    const QByteArray *name,
    const QtPrivate::QMetaTypeInterface *valueType) {
  return new QQmlListMetaTypeInterface(*name, valueType);
}
