//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusmetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QDBusMetaObject *QDBusMetaObject::createMetaObject(const QString
//      &interface, const QString &xml, QHash<QString, QDBusMetaObject *>
//      &map, QDBusError &error)
extern "C" Q_DECL_EXPORT
QDBusMetaObject *ritual_ZN15QDBusMetaObject16createMetaObjectERK7QStringS2_R5QHashIS0_PS_ER10QDBusError(
    const QString *interface,
    const QString *xml,
    QHash<QString, QDBusMetaObject *> *map,
    QDBusError *error) {
  return QDBusMetaObject::createMetaObject(*interface, *xml, *map, *error);
}

//  QDBusMetaObject::~QDBusMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusMetaObjectD1Ev(QDBusMetaObject *self) {
  delete self;
}

//  const int *QDBusMetaObject::inputTypesForMethod(int id) const
extern "C" Q_DECL_EXPORT
const int *ritual_ZNK15QDBusMetaObject19inputTypesForMethodEi(
    const QDBusMetaObject *self,
    int id) {
  return self->inputTypesForMethod(id);
}

//  const int *QDBusMetaObject::outputTypesForMethod(int id) const
extern "C" Q_DECL_EXPORT
const int *ritual_ZNK15QDBusMetaObject20outputTypesForMethodEi(
    const QDBusMetaObject *self,
    int id) {
  return self->outputTypesForMethod(id);
}

//  int QDBusMetaObject::propertyMetaType(int id) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDBusMetaObject16propertyMetaTypeEi(
    const QDBusMetaObject *self,
    int id) {
  return self->propertyMetaType(id);
}

//  QDBusMetaObject::QDBusMetaObject()
extern "C" Q_DECL_EXPORT
QDBusMetaObject *ritual_ZN15QDBusMetaObjectC1Ev() {
  return new QDBusMetaObject();
}

#endif  // !defined(QT_NO_DBUS)
