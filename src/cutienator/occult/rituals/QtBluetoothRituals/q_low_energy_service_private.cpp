//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergyserviceprivate_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qlowenergyserviceprivate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qlowenergycharacteristic.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qlowenergydescriptor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/qlowenergyserviceprivate_p.h>
#include <QtBluetooth/private/qlowenergycontrollerbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qlowenergyserviceprivate.cpp, line 15, as _ZN24QLowEnergyServicePrivateD1Ev
inline QLowEnergyServicePrivate::~QLowEnergyServicePrivate()
{
}
//  -----------------------------------------------------------------------

//  A QLowEnergyServicePrivate that Python can take functions over in. Every QLowEnergyServicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyServicePrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyServicePrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLowEnergyServicePrivate : public QLowEnergyServicePrivate {
public:
  using QLowEnergyServicePrivate::QLowEnergyServicePrivate;
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
      CuteQLowEnergyServicePrivateCall0 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall0>(taken[0]);
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
      CuteQLowEnergyServicePrivateCall1 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall1>(taken[1]);
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
      CuteQLowEnergyServicePrivateCall2 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall2>(taken[2]);
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
      CuteQLowEnergyServicePrivateCall3 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall3>(taken[3]);
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
      CuteQLowEnergyServicePrivateCall4 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall4>(taken[4]);
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
      CuteQLowEnergyServicePrivateCall5 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall5>(taken[5]);
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
      CuteQLowEnergyServicePrivateCall6 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLowEnergyServicePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QLowEnergyServicePrivate10metaObjectEv(
    const QLowEnergyServicePrivate *self) {
  return self->metaObject();
}

//  void *QLowEnergyServicePrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QLowEnergyServicePrivate11qt_metacastEPKc(
    QLowEnergyServicePrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLowEnergyServicePrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QLowEnergyServicePrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QLowEnergyServicePrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QLowEnergyServicePrivate::~QLowEnergyServicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivateD1Ev(
    QLowEnergyServicePrivate *self) {
  delete self;
}

//  void
//      QLowEnergyServicePrivate::stateChanged(QLowEnergyService::ServiceStat
//      e newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate12stateChangedEN17QLowEnergyService12ServiceStateE(
    QLowEnergyServicePrivate *self,
    QLowEnergyService::ServiceState newState) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "stateChanged(QLowEnergyService::ServiceState)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "stateChanged(QLowEnergyService::ServiceState)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&newState)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QLowEnergyServicePrivate::errorOccurred(QLowEnergyService::ServiceErr
//      or error)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate13errorOccurredEN17QLowEnergyService12ServiceErrorE(
    QLowEnergyServicePrivate *self,
    QLowEnergyService::ServiceError error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "errorOccurred(QLowEnergyService::ServiceError)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "errorOccurred(QLowEnergyService::ServiceError)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::characteristicChanged(const
//      QLowEnergyCharacteristic &characteristic, const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate21characteristicChangedERK24QLowEnergyCharacteristicRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyCharacteristic *characteristic,
    const QByteArray *newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicChanged(const QLowEnergyCharacteristic &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicChanged(const QLowEnergyCharacteristic &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(characteristic)),
      const_cast<void *>(static_cast<const void *>(newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::characteristicRead(const
//      QLowEnergyCharacteristic &info, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate18characteristicReadERK24QLowEnergyCharacteristicRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyCharacteristic *info,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicRead(const QLowEnergyCharacteristic &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicRead(const QLowEnergyCharacteristic &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(info)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::characteristicWritten(const
//      QLowEnergyCharacteristic &characteristic, const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate21characteristicWrittenERK24QLowEnergyCharacteristicRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyCharacteristic *characteristic,
    const QByteArray *newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicWritten(const QLowEnergyCharacteristic &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicWritten(const QLowEnergyCharacteristic &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(characteristic)),
      const_cast<void *>(static_cast<const void *>(newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::descriptorRead(const QLowEnergyDescriptor
//      &info, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate14descriptorReadERK20QLowEnergyDescriptorRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyDescriptor *info,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "descriptorRead(const QLowEnergyDescriptor &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "descriptorRead(const QLowEnergyDescriptor &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(info)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::descriptorWritten(const
//      QLowEnergyDescriptor &descriptor, const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate17descriptorWrittenERK20QLowEnergyDescriptorRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyDescriptor *descriptor,
    const QByteArray *newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "descriptorWritten(const QLowEnergyDescriptor &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "descriptorWritten(const QLowEnergyDescriptor &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(descriptor)),
      const_cast<void *>(static_cast<const void *>(newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQLowEnergyServicePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLowEnergyServicePrivate(
    QLowEnergyServicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLowEnergyServicePrivate *>(self)->take(key, call);
}
