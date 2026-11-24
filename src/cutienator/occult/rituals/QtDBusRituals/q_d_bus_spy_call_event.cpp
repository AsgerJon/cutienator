//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/private/qdbusintegrator_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/private/qlatch_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qobject.h>
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qset.h>
#include <QtDBus/qdbusargument.h>
#include <QtDBus/private/qdbusconnection_p.h>
#include <QtDBus/private/qdbusconnectionmanager_p.h>
#include <QtDBus/private/qdbusinterface_p.h>
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/qdbusmetatype.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#include <QtDBus/qdbusabstractadaptor.h>
#include <QtDBus/private/qdbusabstractadaptor_p.h>
#include <QtDBus/qdbusserver.h>
#include <QtDBus/private/qdbusutil_p.h>
#include <QtDBus/qdbusvirtualobject.h>
#include <QtDBus/private/qdbusmessage_p.h>
#include <QtDBus/private/qdbuscontext_p.h>
#include <QtDBus/private/qdbuspendingcall_p.h>
#include <QtDBus/private/qdbusthreaddebug_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusintegrator.cpp, line 506, as _ZN17QDBusSpyCallEvent13placeMetaCallEP7QObject
#if !defined(QT_NO_DBUS)
inline void QDBusSpyCallEvent::placeMetaCall(QObject *)
{
    invokeSpyHooks(msg);
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  A QDBusSpyCallEvent that Python can take functions over in. Every QDBusSpyCallEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusSpyCallEventCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_DBUS)
typedef void (*CuteQDBusSpyCallEventCall1)(const void *, bool, int *);
typedef void * (*CuteQDBusSpyCallEventCall2)(const void *, int *);
class CuteQDBusSpyCallEvent : public QDBusSpyCallEvent {
public:
  using QDBusSpyCallEvent::QDBusSpyCallEvent;
  CuteQDBusSpyCallEvent(const QDBusSpyCallEvent &other) : QDBusSpyCallEvent(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN22QAbstractMetaCallEvent13placeMetaCallEP7QObject")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_DBUS)
  //  void QDBusSpyCallEvent::placeMetaCall(QObject *a0)
  void placeMetaCall(QObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusSpyCallEventCall0 call = reinterpret_cast<CuteQDBusSpyCallEventCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDBusSpyCallEvent::placeMetaCall(a0);
  }
#endif  // !defined(QT_NO_DBUS)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusSpyCallEventCall1 call = reinterpret_cast<CuteQDBusSpyCallEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusSpyCallEventCall2 call = reinterpret_cast<CuteQDBusSpyCallEventCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  void QDBusSpyCallEvent::placeMetaCall(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusSpyCallEvent13placeMetaCallEP7QObject(
    QDBusSpyCallEvent *self,
    QObject *a0) {
  self->placeMetaCall(a0);
}

//  a Python function taken by a CuteQDBusSpyCallEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusSpyCallEvent(
    QDBusSpyCallEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusSpyCallEvent *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
