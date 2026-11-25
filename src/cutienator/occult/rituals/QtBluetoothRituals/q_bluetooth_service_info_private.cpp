//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothserviceinfo_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '!defined(Q_OS_MACOS)': on macOS Qt's header includes
//  'darwin/btraii_p.h', a path of Qt's source tree that no installed Qt has,
//  so the header is broken on Qt's side there. Kept as it is when the
//  generator runs again.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if !defined(Q_OS_MACOS)
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothserviceinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtBluetooth/private/qbluetoothserviceinfo_p.h>
#include <QtCore/QUrl>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qbluetoothserviceinfo.cpp, line 621, as _ZNK28QBluetoothServiceInfoPrivate18protocolDescriptorEN14QBluetoothUuid12ProtocolUuidE
inline QBluetoothServiceInfo::Sequence QBluetoothServiceInfoPrivate::protocolDescriptor(QBluetoothUuid::ProtocolUuid protocol) const
{
    if (!attributes.contains(QBluetoothServiceInfo::ProtocolDescriptorList))
        return QBluetoothServiceInfo::Sequence();

    const QBluetoothServiceInfo::Sequence sequence
            = attributes.value(QBluetoothServiceInfo::ProtocolDescriptorList).value<QBluetoothServiceInfo::Sequence>();
    for (const QVariant &v : sequence) {
        QBluetoothServiceInfo::Sequence parameters = v.value<QBluetoothServiceInfo::Sequence>();
        if (parameters.empty())
            continue;
        if (parameters.at(0).userType() == qMetaTypeId<QBluetoothUuid>()) {
            if (parameters.at(0).value<QBluetoothUuid>() == protocol)
                return parameters;
        }
    }

    return QBluetoothServiceInfo::Sequence();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothserviceinfo.cpp, line 641, as _ZNK28QBluetoothServiceInfoPrivate13serverChannelEv
inline int QBluetoothServiceInfoPrivate::serverChannel() const
{
    QBluetoothServiceInfo::Sequence parameters = protocolDescriptor(QBluetoothUuid::ProtocolUuid::Rfcomm);

    if (parameters.isEmpty())
        return -1;
    else if (parameters.size() == 1)
        return 0;
    else
        return parameters.at(1).toUInt();
}
//  -----------------------------------------------------------------------

//  A QBluetoothServiceInfoPrivate that Python can take functions over in. Every QBluetoothServiceInfoPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothServiceInfoPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothServiceInfoPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceInfoPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceInfoPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceInfoPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceInfoPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceInfoPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBluetoothServiceInfoPrivate : public QBluetoothServiceInfoPrivate {
public:
  using QBluetoothServiceInfoPrivate::QBluetoothServiceInfoPrivate;
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
      CuteQBluetoothServiceInfoPrivateCall0 call = reinterpret_cast<CuteQBluetoothServiceInfoPrivateCall0>(taken[0]);
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
      CuteQBluetoothServiceInfoPrivateCall1 call = reinterpret_cast<CuteQBluetoothServiceInfoPrivateCall1>(taken[1]);
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
      CuteQBluetoothServiceInfoPrivateCall2 call = reinterpret_cast<CuteQBluetoothServiceInfoPrivateCall2>(taken[2]);
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
      CuteQBluetoothServiceInfoPrivateCall3 call = reinterpret_cast<CuteQBluetoothServiceInfoPrivateCall3>(taken[3]);
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
      CuteQBluetoothServiceInfoPrivateCall4 call = reinterpret_cast<CuteQBluetoothServiceInfoPrivateCall4>(taken[4]);
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
      CuteQBluetoothServiceInfoPrivateCall5 call = reinterpret_cast<CuteQBluetoothServiceInfoPrivateCall5>(taken[5]);
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
      CuteQBluetoothServiceInfoPrivateCall6 call = reinterpret_cast<CuteQBluetoothServiceInfoPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBluetoothServiceInfoPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QBluetoothServiceInfoPrivate10metaObjectEv(
    const QBluetoothServiceInfoPrivate *self) {
  return self->metaObject();
}

//  QBluetoothServiceInfo::Sequence QBluetoothServiceInfoPrivate::protocolDes
//      criptor(QBluetoothUuid::ProtocolUuid protocol) const
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo::Sequence *ritual_ZNK28QBluetoothServiceInfoPrivate18protocolDescriptorEN14QBluetoothUuid12ProtocolUuidE(
    const QBluetoothServiceInfoPrivate *self,
    QBluetoothUuid::ProtocolUuid protocol) {
  return new QBluetoothServiceInfo::Sequence(
      self->protocolDescriptor(
          protocol));
}

//  int QBluetoothServiceInfoPrivate::serverChannel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QBluetoothServiceInfoPrivate13serverChannelEv(
    const QBluetoothServiceInfoPrivate *self) {
  return self->serverChannel();
}

//  a Python function taken by a CuteQBluetoothServiceInfoPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBluetoothServiceInfoPrivate(
    QBluetoothServiceInfoPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBluetoothServiceInfoPrivate *>(self)->take(key, call);
}

#endif  // !defined(Q_OS_MACOS)
