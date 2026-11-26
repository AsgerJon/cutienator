//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/btnotifier_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btnotifier_p.h>)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/btnotifier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QSharedPointer>

//  A DarwinBluetooth::LECBManagerNotifier that Python can take functions over in. Every DarwinBluetooth::LECBManagerNotifier
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDarwinBluetooth_LECBManagerNotifierCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDarwinBluetooth_LECBManagerNotifierCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDarwinBluetooth_LECBManagerNotifier : public DarwinBluetooth::LECBManagerNotifier {
public:
  using DarwinBluetooth::LECBManagerNotifier::LECBManagerNotifier;
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
      CuteDarwinBluetooth_LECBManagerNotifierCall0 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall0>(taken[0]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall1 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall1>(taken[1]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall2 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall2>(taken[2]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall3 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall3>(taken[3]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall4 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall4>(taken[4]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall5 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall5>(taken[5]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall6 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DarwinBluetooth::LECBManagerNotifier::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15DarwinBluetooth19LECBManagerNotifier10metaObjectEv(
    const DarwinBluetooth::LECBManagerNotifier *self) {
  return self->metaObject();
}

//  void *DarwinBluetooth::LECBManagerNotifier::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15DarwinBluetooth19LECBManagerNotifier11qt_metacastEPKc(
    DarwinBluetooth::LECBManagerNotifier *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DarwinBluetooth::LECBManagerNotifier::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15DarwinBluetooth19LECBManagerNotifier11qt_metacallEN11QMetaObject4CallEiPPv(
    DarwinBluetooth::LECBManagerNotifier *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void DarwinBluetooth::LECBManagerNotifier::deviceDiscovered(QBluetoothDev
//      iceInfo deviceInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier16deviceDiscoveredE20QBluetoothDeviceInfo(
    DarwinBluetooth::LECBManagerNotifier *self,
    const QBluetoothDeviceInfo *deviceInfo) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "deviceDiscovered(QBluetoothDeviceInfo)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "deviceDiscovered(QBluetoothDeviceInfo)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(deviceInfo)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::discoveryFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier17discoveryFinishedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "discoveryFinished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "discoveryFinished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::connected()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier9connectedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "connected()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "connected()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier12disconnectedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "disconnected()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "disconnected()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::mtuChanged(int newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier10mtuChangedEi(
    DarwinBluetooth::LECBManagerNotifier *self,
    int newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "mtuChanged(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "mtuChanged(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::serviceDiscoveryFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier24serviceDiscoveryFinishedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "serviceDiscoveryFinished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "serviceDiscoveryFinished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::serviceDetailsDiscoveryFinishe
//      d(QSharedPointer<QLowEnergyServicePrivate> service)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier31serviceDetailsDiscoveryFinishedE14QSharedPointerI24QLowEnergyServicePrivateE(
    DarwinBluetooth::LECBManagerNotifier *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "serviceDetailsDiscoveryFinished(QSharedPointer<QLowEnergyServicePrivate>)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "serviceDetailsDiscoveryFinished(QSharedPointer<QLowEnergyServicePrivate>)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(service)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      DarwinBluetooth::LECBManagerNotifier::characteristicRead(QLowEnergyHa
//      ndle charHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier18characteristicReadEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle charHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicRead(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicRead(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&charHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::characteristicWritten(QLowEner
//      gyHandle charHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier21characteristicWrittenEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle charHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicWritten(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicWritten(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&charHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::characteristicUpdated(QLowEner
//      gyHandle charHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier21characteristicUpdatedEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle charHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicUpdated(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicUpdated(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&charHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      DarwinBluetooth::LECBManagerNotifier::descriptorRead(QLowEnergyHandle
//      descHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14descriptorReadEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle descHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "descriptorRead(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "descriptorRead(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&descHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      DarwinBluetooth::LECBManagerNotifier::descriptorWritten(QLowEnergyHan
//      dle descHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier17descriptorWrittenEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle descHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "descriptorWritten(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "descriptorWritten(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&descHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::notificationEnabled(QLowEnergy
//      Handle charHandle, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier19notificationEnabledEtb(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle charHandle,
    bool enabled) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "notificationEnabled(QLowEnergyHandle,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "notificationEnabled(QLowEnergyHandle,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&charHandle)),
      const_cast<void *>(static_cast<const void *>(&enabled)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::servicesWereModified()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier20servicesWereModifiedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "servicesWereModified()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "servicesWereModified()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::rssiUpdated(qint16 newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier11rssiUpdatedEs(
    DarwinBluetooth::LECBManagerNotifier *self,
    qint16 newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rssiUpdated(qint16)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rssiUpdated(qint16)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::LEnotSupported()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14LEnotSupportedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "LEnotSupported()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "LEnotSupported()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(QBluetoothDevic
//      eDiscoveryAgent::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorEN30QBluetoothDeviceDiscoveryAgent5ErrorE(
    DarwinBluetooth::LECBManagerNotifier *self,
    QBluetoothDeviceDiscoveryAgent::Error error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "CBManagerError(QBluetoothDeviceDiscoveryAgent::Error)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "CBManagerError(QBluetoothDeviceDiscoveryAgent::Error)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(QLowEnergyContr
//      oller::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorEN20QLowEnergyController5ErrorE(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyController::Error error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "CBManagerError(QLowEnergyController::Error)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "CBManagerError(QLowEnergyController::Error)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(const
//      QBluetoothUuid &serviceUuid, QLowEnergyController::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorERK14QBluetoothUuidN20QLowEnergyController5ErrorE(
    DarwinBluetooth::LECBManagerNotifier *self,
    const QBluetoothUuid *serviceUuid,
    QLowEnergyController::Error error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "CBManagerError(const QBluetoothUuid &,QLowEnergyController::Error)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "CBManagerError(const QBluetoothUuid &,QLowEnergyController::Error)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(serviceUuid)),
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(const
//      QBluetoothUuid &serviceUuid, QLowEnergyService::ServiceError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorERK14QBluetoothUuidN17QLowEnergyService12ServiceErrorE(
    DarwinBluetooth::LECBManagerNotifier *self,
    const QBluetoothUuid *serviceUuid,
    QLowEnergyService::ServiceError error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "CBManagerError(const QBluetoothUuid &,QLowEnergyService::ServiceError)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "CBManagerError(const QBluetoothUuid &,QLowEnergyService::ServiceError)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(serviceUuid)),
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteDarwinBluetooth_LECBManagerNotifier, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DarwinBluetooth_LECBManagerNotifier(
    DarwinBluetooth::LECBManagerNotifier *self,
    const char *key,
    void *call) {
  return static_cast<CuteDarwinBluetooth_LECBManagerNotifier *>(self)->take(key, call);
}

#endif  // __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btnotifier_p.h>)
