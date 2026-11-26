//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusabstractadaptor_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusabstractadaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qobjectdefs.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusabstractadaptor.h>
#include <QtDBus/private/qdbusabstractadaptor_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qset.h>
#include <QtCore/qthread.h>
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/private/qdbusconnection_p.h>  // for qDBusParametersForMethod
#include <QtDBus/private/qdbusmetatype_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusabstractadaptor.cpp, line 173, as _ZN21QDBusAdaptorConnectorD1Ev
#if !defined(QT_NO_DBUS)
inline QDBusAdaptorConnector::~QDBusAdaptorConnector()
{
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  A QDBusAdaptorConnector that Python can take functions over in. Every QDBusAdaptorConnector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusAdaptorConnectorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusAdaptorConnectorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAdaptorConnectorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAdaptorConnectorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAdaptorConnectorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAdaptorConnectorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAdaptorConnectorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusAdaptorConnector : public QDBusAdaptorConnector {
public:
  using QDBusAdaptorConnector::QDBusAdaptorConnector;
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
      CuteQDBusAdaptorConnectorCall0 call = reinterpret_cast<CuteQDBusAdaptorConnectorCall0>(taken[0]);
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
      CuteQDBusAdaptorConnectorCall1 call = reinterpret_cast<CuteQDBusAdaptorConnectorCall1>(taken[1]);
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
      CuteQDBusAdaptorConnectorCall2 call = reinterpret_cast<CuteQDBusAdaptorConnectorCall2>(taken[2]);
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
      CuteQDBusAdaptorConnectorCall3 call = reinterpret_cast<CuteQDBusAdaptorConnectorCall3>(taken[3]);
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
      CuteQDBusAdaptorConnectorCall4 call = reinterpret_cast<CuteQDBusAdaptorConnectorCall4>(taken[4]);
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
      CuteQDBusAdaptorConnectorCall5 call = reinterpret_cast<CuteQDBusAdaptorConnectorCall5>(taken[5]);
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
      CuteQDBusAdaptorConnectorCall6 call = reinterpret_cast<CuteQDBusAdaptorConnectorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusAdaptorConnector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QDBusAdaptorConnector10metaObjectEv(
    const QDBusAdaptorConnector *self) {
  return self->metaObject();
}

//  void *QDBusAdaptorConnector::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QDBusAdaptorConnector11qt_metacastEPKc(
    QDBusAdaptorConnector *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusAdaptorConnector::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QDBusAdaptorConnector11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusAdaptorConnector *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QDBusAdaptorConnector::~QDBusAdaptorConnector()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusAdaptorConnectorD1Ev(QDBusAdaptorConnector *self) {
  delete self;
}

//  void QDBusAdaptorConnector::relaySlot(QMethodRawArguments a)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusAdaptorConnector9relaySlotE19QMethodRawArguments(
    QDBusAdaptorConnector *self,
    const QMethodRawArguments *a) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusAdaptorConnector")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "relaySlot(QMethodRawArguments)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "relaySlot(QMethodRawArguments)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusAdaptorConnector::polish()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusAdaptorConnector6polishEv(QDBusAdaptorConnector *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusAdaptorConnector")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "polish()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "polish()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusAdaptorConnector::relaySignal(QObject *obj, const QMetaObject
//      *metaObject, int sid, const QVariantList &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusAdaptorConnector11relaySignalEP7QObjectPK11QMetaObjectiRK5QListI8QVariantE(
    QDBusAdaptorConnector *self,
    QObject *obj,
    const QMetaObject *metaObject,
    int sid,
    const QList<QVariant> *args) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusAdaptorConnector")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "relaySignal(QObject *,const QMetaObject *,int,const QVariantList &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "relaySignal(QObject *,const QMetaObject *,int,const QVariantList &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&obj)),
      const_cast<void *>(static_cast<const void *>(&metaObject)),
      const_cast<void *>(static_cast<const void *>(&sid)),
      const_cast<void *>(static_cast<const void *>(args)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQDBusAdaptorConnector, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusAdaptorConnector(
    QDBusAdaptorConnector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusAdaptorConnector *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
