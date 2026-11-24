//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusconnectioninterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusconnectioninterface.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qmetaobject.h>

//  Only a class built on QDBusConnectionInterface may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDBusConnectionInterface : QDBusConnectionInterface {
  using QDBusConnectionInterface::connectNotify;
  using QDBusConnectionInterface::disconnectNotify;
};

//  const QMetaObject *QDBusConnectionInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QDBusConnectionInterface10metaObjectEv(
    const QDBusConnectionInterface *self) {
  return self->metaObject();
}

//  QString QDBusConnectionInterface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QDBusConnectionInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusConnectionInterface::tr(s, c, n));
}

//  QDBusConnectionInterface::QDBusConnectionInterface(const QDBusConnection
//      &connection, QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusConnectionInterface *ritual_ZN24QDBusConnectionInterfaceC1ERK15QDBusConnectionP7QObject(
    const QDBusConnection *connection,
    QObject *parent) {
  return new QDBusConnectionInterface(*connection, parent);
}

//  QDBusConnectionInterface::~QDBusConnectionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterfaceD1Ev(
    QDBusConnectionInterface *self) {
  delete self;
}

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::connectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface13connectNotifyERK11QMetaMethod(
    QDBusConnectionInterface *self,
    const QMetaMethod *a0) {
  self->connectNotify(*a0);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::disconnectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface16disconnectNotifyERK11QMetaMethod(
    QDBusConnectionInterface *self,
    const QMetaMethod *a0) {
  self->disconnectNotify(*a0);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::connectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QDBusConnectionInterface13connectNotifyERK11QMetaMethod(
    QDBusConnectionInterface *self,
    const QMetaMethod *a0) {
  static_cast<OwnQDBusConnectionInterface *>(self)->OwnQDBusConnectionInterface::connectNotify(
      *a0);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::disconnectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QDBusConnectionInterface16disconnectNotifyERK11QMetaMethod(
    QDBusConnectionInterface *self,
    const QMetaMethod *a0) {
  static_cast<OwnQDBusConnectionInterface *>(self)->OwnQDBusConnectionInterface::disconnectNotify(
      *a0);
}
#endif  // !defined(Q_QDOC)

#endif  // !defined(QT_NO_DBUS)
