//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/profile1context_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/profile1context_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusunixfiledescriptor.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A OrgBluezProfile1ContextInterface that Python can take functions over in. Every OrgBluezProfile1ContextInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteOrgBluezProfile1ContextInterfaceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteOrgBluezProfile1ContextInterfaceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteOrgBluezProfile1ContextInterfaceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteOrgBluezProfile1ContextInterfaceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteOrgBluezProfile1ContextInterfaceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteOrgBluezProfile1ContextInterfaceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteOrgBluezProfile1ContextInterfaceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteOrgBluezProfile1ContextInterface : public OrgBluezProfile1ContextInterface {
public:
  using OrgBluezProfile1ContextInterface::OrgBluezProfile1ContextInterface;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteOrgBluezProfile1ContextInterfaceCall0 call = reinterpret_cast<CuteOrgBluezProfile1ContextInterfaceCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteOrgBluezProfile1ContextInterfaceCall1 call = reinterpret_cast<CuteOrgBluezProfile1ContextInterfaceCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteOrgBluezProfile1ContextInterfaceCall2 call = reinterpret_cast<CuteOrgBluezProfile1ContextInterfaceCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteOrgBluezProfile1ContextInterfaceCall3 call = reinterpret_cast<CuteOrgBluezProfile1ContextInterfaceCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteOrgBluezProfile1ContextInterfaceCall4 call = reinterpret_cast<CuteOrgBluezProfile1ContextInterfaceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteOrgBluezProfile1ContextInterfaceCall5 call = reinterpret_cast<CuteOrgBluezProfile1ContextInterfaceCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteOrgBluezProfile1ContextInterfaceCall6 call = reinterpret_cast<CuteOrgBluezProfile1ContextInterfaceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *OrgBluezProfile1ContextInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32OrgBluezProfile1ContextInterface10metaObjectEv(
    const OrgBluezProfile1ContextInterface *self) {
  return self->metaObject();
}

//  void *OrgBluezProfile1ContextInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32OrgBluezProfile1ContextInterface11qt_metacastEPKc(
    OrgBluezProfile1ContextInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int OrgBluezProfile1ContextInterface::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32OrgBluezProfile1ContextInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    OrgBluezProfile1ContextInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void OrgBluezProfile1ContextInterface::newConnection(const
//      QDBusUnixFileDescriptor &fd)
extern "C" Q_DECL_EXPORT
void ritual_ZN32OrgBluezProfile1ContextInterface13newConnectionERK23QDBusUnixFileDescriptor(
    OrgBluezProfile1ContextInterface *self,
    const QDBusUnixFileDescriptor *fd) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "OrgBluezProfile1ContextInterface")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "newConnection(const QDBusUnixFileDescriptor &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "newConnection(const QDBusUnixFileDescriptor &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(fd)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void OrgBluezProfile1ContextInterface::NewConnection(const
//      QDBusObjectPath &a0, const QDBusUnixFileDescriptor &a1, const
//      QVariantMap &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN32OrgBluezProfile1ContextInterface13NewConnectionERK15QDBusObjectPathRK23QDBusUnixFileDescriptorRK4QMapI7QString8QVariantE(
    OrgBluezProfile1ContextInterface *self,
    const QDBusObjectPath *a0,
    const QDBusUnixFileDescriptor *a1,
    const QMap<QString, QVariant> *a2) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "OrgBluezProfile1ContextInterface")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "NewConnection(const QDBusObjectPath &,const QDBusUnixFileDescriptor &,const QVariantMap &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "NewConnection(const QDBusObjectPath &,const QDBusUnixFileDescriptor &,const QVariantMap &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
      const_cast<void *>(static_cast<const void *>(a1)),
      const_cast<void *>(static_cast<const void *>(a2)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void OrgBluezProfile1ContextInterface::RequestDisconnection(const
//      QDBusObjectPath &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32OrgBluezProfile1ContextInterface20RequestDisconnectionERK15QDBusObjectPath(
    OrgBluezProfile1ContextInterface *self,
    const QDBusObjectPath *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "OrgBluezProfile1ContextInterface")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "RequestDisconnection(const QDBusObjectPath &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "RequestDisconnection(const QDBusObjectPath &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void OrgBluezProfile1ContextInterface::Release()
extern "C" Q_DECL_EXPORT
void ritual_ZN32OrgBluezProfile1ContextInterface7ReleaseEv(
    OrgBluezProfile1ContextInterface *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "OrgBluezProfile1ContextInterface")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "Release()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "Release()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  OrgBluezProfile1ContextInterface as the QDBusContext it is built on
extern "C" Q_DECL_EXPORT
QDBusContext *ritual_cast_OrgBluezProfile1ContextInterface_QDBusContext(
    OrgBluezProfile1ContextInterface *self) {
  return static_cast<QDBusContext *>(self);
}

//  a Python function taken by a CuteOrgBluezProfile1ContextInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_OrgBluezProfile1ContextInterface(
    OrgBluezProfile1ContextInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteOrgBluezProfile1ContextInterface *>(self)->take(key, call);
}

#endif  // QT_CONFIG(bluez)
