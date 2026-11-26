//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/propertiesadaptor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/propertiesadaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/propertiesadaptor_p.h>
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

//  from ../qtconnectivity/src/bluetooth/bluez/propertiesadaptor.cpp, line 38, as _ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor3GetERK7QStringS3_
namespace QtBluetoothPrivate {
inline QDBusVariant OrgFreedesktopDBusPropertiesAdaptor::Get(const QString &interface, const QString &name)
{
    // handle method call org.freedesktop.DBus.Properties.Get
    QDBusVariant value;
    QMetaObject::invokeMethod(parent(), "Get", Q_RETURN_ARG(QDBusVariant, value), Q_ARG(QString, interface), Q_ARG(QString, name));
    return value;
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/propertiesadaptor.cpp, line 46, as _ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor6GetAllERK7QString
namespace QtBluetoothPrivate {
inline QVariantMap OrgFreedesktopDBusPropertiesAdaptor::GetAll(const QString &interface)
{
    // handle method call org.freedesktop.DBus.Properties.GetAll
    QVariantMap properties;
    QMetaObject::invokeMethod(parent(), "GetAll", Q_RETURN_ARG(QVariantMap, properties), Q_ARG(QString, interface));
    return properties;
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor that Python can take functions over in. Every QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor : public QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor {
public:
  using QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::OrgFreedesktopDBusPropertiesAdaptor;
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::metaObject(
//      ) const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor10metaObjectEv(
    const QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metacas
//      t(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor11qt_metacastEPKc(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metacall(
//      QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::~OrgFreedesktopD
//      BusPropertiesAdaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorD1Ev(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self) {
  delete self;
}

//  QDBusVariant
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::Get(const
//      QString &interface, const QString &name)
extern "C" Q_DECL_EXPORT
QDBusVariant *ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor3GetERK7QStringS3_(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const QString *interface,
    const QString *name) {
  return new QDBusVariant(self->Get(*interface, *name));
}

//  QVariantMap
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::GetAll(const
//      QString &interface)
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor6GetAllERK7QString(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const QString *interface) {
  return new QMap<QString, QVariant>(self->GetAll(*interface));
}

//  void QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::Set(const
//      QString &interface, const QString &name, const QDBusVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor3SetERK7QStringS3_RK12QDBusVariant(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const QString *interface,
    const QString *name,
    const QDBusVariant *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "Set(const QString &,const QString &,const QDBusVariant &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "Set(const QString &,const QString &,const QDBusVariant &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(interface)),
      const_cast<void *>(static_cast<const void *>(name)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::PropertiesC
//      hanged(const QString &interface, const QVariantMap
//      &changed_properties, const QStringList &invalidated_properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor17PropertiesChangedERK7QStringRK4QMapIS1_8QVariantERK5QListIS1_E(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const QString *interface,
    const QMap<QString, QVariant> *changed_properties,
    const QList<QString> *invalidated_properties) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "PropertiesChanged(const QString &,const QVariantMap &,const QStringList &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "PropertiesChanged(const QString &,const QVariantMap &,const QStringList &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(interface)),
      const_cast<void *>(static_cast<const void *>(changed_properties)),
      const_cast<void *>(static_cast<const void *>(invalidated_properties)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor *>(self)->take(key, call);
}

#endif  // QT_CONFIG(bluez)
