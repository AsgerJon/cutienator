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
#include "qdbusintegrator_p.h"
#include <qcoreapplication.h>
#include <qelapsedtimer.h>
#include <private/qlatch_p.h>
#include <qloggingcategory.h>
#include <qmetaobject.h>
#include <qobject.h>
#include <qsocketnotifier.h>
#include <qstringlist.h>
#include <qthread.h>
#include <private/qlocking_p.h>
#include <QtCore/qset.h>
#include "qdbusargument.h"
#include "qdbusconnection_p.h"
#include "qdbusconnectionmanager_p.h"
#include "qdbusinterface_p.h"
#include "qdbusmessage.h"
#include "qdbusmetatype.h"
#include "qdbusmetatype_p.h"
#include "qdbusabstractadaptor.h"
#include "qdbusabstractadaptor_p.h"
#include "qdbusserver.h"
#include "qdbusutil_p.h"
#include "qdbusvirtualobject.h"
#include "qdbusmessage_p.h"
#include "qdbuscontext_p.h"
#include "qdbuspendingcall_p.h"
#include "qdbusthreaddebug_p.h"
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusintegrator.cpp, line 1601, as _ZN24QDBusActivateObjectEventD1Ev
#if !defined(QT_NO_DBUS)
inline QDBusActivateObjectEvent::~QDBusActivateObjectEvent()
{
    if (!handled) {
        // we're being destroyed without delivering
        // it means the object was deleted between posting and delivering
        QDBusConnectionPrivate *that = QDBusConnectionPrivate::d(connection);
        that->sendError(message, QDBusError::UnknownObject);
    }

    // semaphore releasing happens in ~QMetaCallEvent
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 1613, as _ZN24QDBusActivateObjectEvent13placeMetaCallEP7QObject
#if !defined(QT_NO_DBUS)
inline void QDBusActivateObjectEvent::placeMetaCall(QObject *)
{
    QDBusConnectionPrivate *that = QDBusConnectionPrivate::d(connection);

    QDBusLockerBase::reportThreadAction(HandleObjectCallPostEventAction,
                                        QDBusLockerBase::BeforeDeliver, that);
    that->activateObject(node, message, pathStartPos);
    QDBusLockerBase::reportThreadAction(HandleObjectCallPostEventAction,
                                        QDBusLockerBase::AfterDeliver, that);

    handled = true;
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  A QDBusActivateObjectEvent that Python can take functions over in. Every QDBusActivateObjectEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusActivateObjectEventCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_DBUS)
typedef void (*CuteQDBusActivateObjectEventCall1)(const void *, bool, int *);
typedef void * (*CuteQDBusActivateObjectEventCall2)(const void *, int *);
class CuteQDBusActivateObjectEvent : public QDBusActivateObjectEvent {
public:
  using QDBusActivateObjectEvent::QDBusActivateObjectEvent;
  CuteQDBusActivateObjectEvent(const QDBusActivateObjectEvent &other) : QDBusActivateObjectEvent(other) {}
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
  //  void QDBusActivateObjectEvent::placeMetaCall(QObject *a0)
  void placeMetaCall(QObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusActivateObjectEventCall0 call = reinterpret_cast<CuteQDBusActivateObjectEventCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDBusActivateObjectEvent::placeMetaCall(a0);
  }
#endif  // !defined(QT_NO_DBUS)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusActivateObjectEventCall1 call = reinterpret_cast<CuteQDBusActivateObjectEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusActivateObjectEventCall2 call = reinterpret_cast<CuteQDBusActivateObjectEventCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QDBusActivateObjectEvent::~QDBusActivateObjectEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusActivateObjectEventD1Ev(
    QDBusActivateObjectEvent *self) {
  delete self;
}

//  void QDBusActivateObjectEvent::placeMetaCall(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusActivateObjectEvent13placeMetaCallEP7QObject(
    QDBusActivateObjectEvent *self,
    QObject *a0) {
  self->placeMetaCall(a0);
}

//  a Python function taken by a CuteQDBusActivateObjectEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusActivateObjectEvent(
    QDBusActivateObjectEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusActivateObjectEvent *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
