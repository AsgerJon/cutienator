//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/gattcharacteristic1adaptor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/gattcharacteristic1adaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtDBus/qdbusmessage.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/gattcharacteristic1adaptor_p.h>
#include <QtCore/QMetaObject>
#include <QtCore/QByteArray>
#include <QtCore/QList>
#include <QtCore/QMap>
#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QVariant>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 38, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor5flagsEv
namespace QtBluetoothPrivate {
inline QStringList OrgBluezGattCharacteristic1Adaptor::flags() const
{
    // get the value of property Flags
    return qvariant_cast< QStringList >(parent()->property("Flags"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 44, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor9notifyingEv
namespace QtBluetoothPrivate {
inline bool OrgBluezGattCharacteristic1Adaptor::notifying() const
{
    // get the value of property Notifying
    return qvariant_cast< bool >(parent()->property("Notifying"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 50, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor7serviceEv
namespace QtBluetoothPrivate {
inline QDBusObjectPath OrgBluezGattCharacteristic1Adaptor::service() const
{
    // get the value of property Service
    return qvariant_cast< QDBusObjectPath >(parent()->property("Service"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 56, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor4uUIDEv
namespace QtBluetoothPrivate {
inline QString OrgBluezGattCharacteristic1Adaptor::uUID() const
{
    // get the value of property UUID
    return qvariant_cast< QString >(parent()->property("UUID"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 62, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor5valueEv
namespace QtBluetoothPrivate {
inline QByteArray OrgBluezGattCharacteristic1Adaptor::value() const
{
    // get the value of property Value
    return qvariant_cast< QByteArray >(parent()->property("Value"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 68, as _ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor9ReadValueERK4QMapI7QString8QVariantERK12QDBusMessage
namespace QtBluetoothPrivate {
inline QByteArray OrgBluezGattCharacteristic1Adaptor::ReadValue(const QVariantMap &options,
                                                         const QDBusMessage& msg)
{
    // handle method call org.bluez.GattCharacteristic1.ReadValue
    QByteArray value;
    QString error;
    QMetaObject::invokeMethod(parent(), "ReadValue", Q_RETURN_ARG(QByteArray, value),
                              Q_ARG(QVariantMap, options), Q_ARG(QString&, error));
    if (!error.isEmpty()) {
        // Reply with error if needed
        auto reply = msg.createErrorReply(error, {});
        QDBusConnection::systemBus().send(reply);
    }
    return value;
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor : public QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor {
public:
  using QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::OrgBluezGattCharacteristic1Adaptor;
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::qt_metacast
//      (const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::qt_metacall(Q
//      MetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::~OrgBluezGattChar
//      acteristic1Adaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorD1Ev(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  delete self;
}

//  QStringList
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::flags() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor5flagsEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return new QList<QString>(self->flags());
}

//  bool QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::notifying()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor9notifyingEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return self->notifying();
}

//  QDBusObjectPath
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::service()
//      const
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor7serviceEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return new QDBusObjectPath(self->service());
}

//  QString QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::uUID()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor4uUIDEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return new QString(self->uUID());
}

//  QByteArray
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor5valueEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return new QByteArray(self->value());
}

//  QByteArray
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::ReadValue(con
//      st QVariantMap &options, const QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor9ReadValueERK4QMapI7QString8QVariantERK12QDBusMessage(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    const QMap<QString, QVariant> *options,
    const QDBusMessage *msg) {
  return new QByteArray(self->ReadValue(*options, *msg));
}

//  void
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::StartNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor11StartNotifyEv(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "StartNotify()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "StartNotify()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::StopNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor10StopNotifyEv(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "StopNotify()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "StopNotify()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::WriteValue(co
//      nst QByteArray &value, const QVariantMap &options, const QDBusMessage
//      &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor10WriteValueERK10QByteArrayRK4QMapI7QString8QVariantERK12QDBusMessage(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    const QByteArray *value,
    const QMap<QString, QVariant> *options,
    const QDBusMessage *msg) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "WriteValue(const QByteArray &,const QVariantMap &,const QDBusMessage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "WriteValue(const QByteArray &,const QVariantMap &,const QDBusMessage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(value)),
      const_cast<void *>(static_cast<const void *>(options)),
      const_cast<void *>(static_cast<const void *>(msg)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor *>(self)->take(key, call);
}

#endif  // QT_CONFIG(bluez)
