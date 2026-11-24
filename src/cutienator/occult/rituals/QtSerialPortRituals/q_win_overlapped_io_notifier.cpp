//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialPort/6.12.0/QtSerialPort/private/qwinoverlappedionotifier_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSerialPort/qserialportglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialPort/QtSerialPort>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialPort/6.12.0/QtSerialPort/private/qwinoverlappedionotifier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qwinoverlappedionotifier_p.h"
#include <qdebug.h>
#include <qatomic.h>
#include <qelapsedtimer.h>
#include <qmutex.h>
#include <qpointer.h>
#include <qqueue.h>
#include <qset.h>
#include <qthread.h>
#include <qt_windows.h>
#include <private/qobject_p.h>
#include <private/qiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialport/src/serialport/qwinoverlappedionotifier.cpp, line 224, as _ZN24QWinOverlappedIoNotifierC1EP7QObject
inline QWinOverlappedIoNotifier::QWinOverlappedIoNotifier(QObject *parent)
    : QObject(*new QWinOverlappedIoNotifierPrivate, parent)
{
    Q_D(QWinOverlappedIoNotifier);
    WaitForSingleObject(d->iocpInstanceLock, INFINITE);
    if (!d->iocp)
        d->iocp = new QWinIoCompletionPort;
    d->iocpInstanceRefCount++;
    ReleaseMutex(d->iocpInstanceLock);

    d->hSemaphore = CreateSemaphore(NULL, 0, 255, NULL);
    d->hResultsMutex = CreateMutex(NULL, FALSE, NULL);
    connect(this, SIGNAL(_q_notify()), this, SLOT(_q_notified()), Qt::QueuedConnection);
}

//  from ../qtserialport/src/serialport/qwinoverlappedionotifier.cpp, line 239, as _ZN24QWinOverlappedIoNotifierD1Ev
inline QWinOverlappedIoNotifier::~QWinOverlappedIoNotifier()
{
    Q_D(QWinOverlappedIoNotifier);
    setEnabled(false);
    CloseHandle(d->hResultsMutex);
    CloseHandle(d->hSemaphore);

    WaitForSingleObject(d->iocpInstanceLock, INFINITE);
    if (!--d->iocpInstanceRefCount) {
        delete d->iocp;
        d->iocp = 0;
    }
    ReleaseMutex(d->iocpInstanceLock);
}

//  from ../qtserialport/src/serialport/qwinoverlappedionotifier.cpp, line 266, as _ZN24QWinOverlappedIoNotifier10setEnabledEb
inline void QWinOverlappedIoNotifier::setEnabled(bool enabled)
{
    Q_D(QWinOverlappedIoNotifier);
    if (enabled)
        d->iocp->registerNotifier(d);
    else
        d->iocp->unregisterNotifier(d);
}
//  -----------------------------------------------------------------------

//  A QWinOverlappedIoNotifier that Python can take functions over in. Every QWinOverlappedIoNotifier
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWinOverlappedIoNotifierCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWinOverlappedIoNotifierCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWinOverlappedIoNotifierCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWinOverlappedIoNotifierCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWinOverlappedIoNotifierCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWinOverlappedIoNotifierCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWinOverlappedIoNotifierCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWinOverlappedIoNotifier : public QWinOverlappedIoNotifier {
public:
  using QWinOverlappedIoNotifier::QWinOverlappedIoNotifier;
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
      CuteQWinOverlappedIoNotifierCall0 call = reinterpret_cast<CuteQWinOverlappedIoNotifierCall0>(taken[0]);
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
      CuteQWinOverlappedIoNotifierCall1 call = reinterpret_cast<CuteQWinOverlappedIoNotifierCall1>(taken[1]);
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
      CuteQWinOverlappedIoNotifierCall2 call = reinterpret_cast<CuteQWinOverlappedIoNotifierCall2>(taken[2]);
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
      CuteQWinOverlappedIoNotifierCall3 call = reinterpret_cast<CuteQWinOverlappedIoNotifierCall3>(taken[3]);
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
      CuteQWinOverlappedIoNotifierCall4 call = reinterpret_cast<CuteQWinOverlappedIoNotifierCall4>(taken[4]);
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
      CuteQWinOverlappedIoNotifierCall5 call = reinterpret_cast<CuteQWinOverlappedIoNotifierCall5>(taken[5]);
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
      CuteQWinOverlappedIoNotifierCall6 call = reinterpret_cast<CuteQWinOverlappedIoNotifierCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWinOverlappedIoNotifier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QWinOverlappedIoNotifier10metaObjectEv(
    const QWinOverlappedIoNotifier *self) {
  return self->metaObject();
}

//  QString QWinOverlappedIoNotifier::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QWinOverlappedIoNotifier2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWinOverlappedIoNotifier::tr(s, c, n));
}

//  QWinOverlappedIoNotifier::QWinOverlappedIoNotifier(QObject *parent)
extern "C" Q_DECL_EXPORT
QWinOverlappedIoNotifier *ritual_ZN24QWinOverlappedIoNotifierC1EP7QObject(
    QObject *parent) {
  return new CuteQWinOverlappedIoNotifier(parent);
}

//  QWinOverlappedIoNotifier::~QWinOverlappedIoNotifier()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWinOverlappedIoNotifierD1Ev(
    QWinOverlappedIoNotifier *self) {
  delete self;
}

//  void QWinOverlappedIoNotifier::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWinOverlappedIoNotifier10setEnabledEb(
    QWinOverlappedIoNotifier *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  a Python function taken by a CuteQWinOverlappedIoNotifier, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWinOverlappedIoNotifier(
    QWinOverlappedIoNotifier *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWinOverlappedIoNotifier *>(self)->take(key, call);
}

#endif  // defined(Q_OS_WIN)
