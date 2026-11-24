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

//  QDBusMetaObject::~QDBusMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusMetaObjectD1Ev(QDBusMetaObject *self) {
  delete self;
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
