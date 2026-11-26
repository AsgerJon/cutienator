//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/private/qscxmlstatemachine_p.h>
#include <QtScxml/private/qscxmlexecutablecontent_p.h>
#include <QtScxml/private/qscxmlevent_p.h>
#include <QtScxml/qscxmlinvokableservice.h>
#include <QtScxml/private/qscxmldatamodel_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qhash.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimer.h>
#include <QtCore/qthread.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlstatemachine.cpp, line 229, as _ZN14QScxmlInternal13EventLoopHook10timerEventEP11QTimerEvent
namespace QScxmlInternal {
inline void EventLoopHook::timerEvent(QTimerEvent *timerEvent)
{
    const int timerId = timerEvent->timerId();
    for (auto it = smp->m_delayedEvents.begin(), eit = smp->m_delayedEvents.end(); it != eit; ++it) {
        if (it->first == timerId) {
            QScxmlEvent *scxmlEvent = it->second;
            smp->m_delayedEvents.erase(it);
            smp->routeEvent(scxmlEvent);
            killTimer(timerId);
            return;
        }
    }
}
}  // namespace QScxmlInternal

//  from ../qtscxml/src/scxml/qscxmlstatemachine.cpp, line 216, as _ZN14QScxmlInternal13EventLoopHook18queueProcessEventsEv
namespace QScxmlInternal {
inline void EventLoopHook::queueProcessEvents()
{
    if (smp->m_isProcessingEvents)
        return;

    QMetaObject::invokeMethod(this, "doProcessEvents", Qt::QueuedConnection);
}
}  // namespace QScxmlInternal
//  -----------------------------------------------------------------------

//  Only a class built on QScxmlInternal::EventLoopHook may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQScxmlInternal_EventLoopHook : QScxmlInternal::EventLoopHook {
  using QScxmlInternal::EventLoopHook::timerEvent;
};

//  A QScxmlInternal::EventLoopHook that Python can take functions over in. Every QScxmlInternal::EventLoopHook
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_EventLoopHookCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlInternal_EventLoopHookCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlInternal_EventLoopHookCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_EventLoopHookCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_EventLoopHookCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_EventLoopHookCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_EventLoopHookCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlInternal_EventLoopHook : public QScxmlInternal::EventLoopHook {
public:
  using QScxmlInternal::EventLoopHook::EventLoopHook;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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
  //  void QScxmlInternal::EventLoopHook::timerEvent(QTimerEvent
  //      *timerEvent)
  void timerEvent(QTimerEvent *timerEvent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlInternal_EventLoopHookCall0 call = reinterpret_cast<CuteQScxmlInternal_EventLoopHookCall0>(taken[0]);
      call(this, timerEvent, &handled);
      if (handled) return;
    }
    QScxmlInternal::EventLoopHook::timerEvent(timerEvent);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlInternal_EventLoopHookCall1 call = reinterpret_cast<CuteQScxmlInternal_EventLoopHookCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQScxmlInternal_EventLoopHookCall2 call = reinterpret_cast<CuteQScxmlInternal_EventLoopHookCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScxmlInternal_EventLoopHookCall3 call = reinterpret_cast<CuteQScxmlInternal_EventLoopHookCall3>(taken[3]);
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
      CuteQScxmlInternal_EventLoopHookCall4 call = reinterpret_cast<CuteQScxmlInternal_EventLoopHookCall4>(taken[4]);
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
      CuteQScxmlInternal_EventLoopHookCall5 call = reinterpret_cast<CuteQScxmlInternal_EventLoopHookCall5>(taken[5]);
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
      CuteQScxmlInternal_EventLoopHookCall6 call = reinterpret_cast<CuteQScxmlInternal_EventLoopHookCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlInternal::EventLoopHook::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QScxmlInternal13EventLoopHook10metaObjectEv(
    const QScxmlInternal::EventLoopHook *self) {
  return self->metaObject();
}

//  void *QScxmlInternal::EventLoopHook::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QScxmlInternal13EventLoopHook11qt_metacastEPKc(
    QScxmlInternal::EventLoopHook *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlInternal::EventLoopHook::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QScxmlInternal13EventLoopHook11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlInternal::EventLoopHook *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QScxmlInternal::EventLoopHook::queueProcessEvents()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal13EventLoopHook18queueProcessEventsEv(
    QScxmlInternal::EventLoopHook *self) {
  self->queueProcessEvents();
}

//  void QScxmlInternal::EventLoopHook::doProcessEvents()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal13EventLoopHook15doProcessEventsEv(
    QScxmlInternal::EventLoopHook *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QScxmlInternal::EventLoopHook")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "doProcessEvents()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "doProcessEvents()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QScxmlInternal::EventLoopHook::timerEvent(QTimerEvent *timerEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal13EventLoopHook10timerEventEP11QTimerEvent(
    QScxmlInternal::EventLoopHook *self,
    QTimerEvent *timerEvent) {
  self->timerEvent(timerEvent);
}

//  a Python function taken by a CuteQScxmlInternal_EventLoopHook, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlInternal_EventLoopHook(
    QScxmlInternal::EventLoopHook *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlInternal_EventLoopHook *>(self)->take(key, call);
}

//  void QScxmlInternal::EventLoopHook::timerEvent(QTimerEvent *timerEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QScxmlInternal13EventLoopHook10timerEventEP11QTimerEvent(
    QScxmlInternal::EventLoopHook *self,
    QTimerEvent *timerEvent) {
  static_cast<OwnQScxmlInternal_EventLoopHook *>(self)->OwnQScxmlInternal_EventLoopHook::timerEvent(
      timerEvent);
}
