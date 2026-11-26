//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfuturewatcher_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qfuturewatcher.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfuturewatcher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qfuturewatcher.h>
#include <QtCore/private/qfuturewatcher_p.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qthread.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/thread/qfuturewatcher.cpp, line 470, as _ZN25QFutureWatcherBasePrivate16postCallOutEventERK19QFutureCallOutEvent
inline void QFutureWatcherBasePrivate::postCallOutEvent(const QFutureCallOutEvent &callOutEvent)
{
    Q_Q(QFutureWatcherBase);

    if (callOutEvent.callOutType == QFutureCallOutEvent::ResultsReady) {
        if (pendingResultsReady.fetchAndAddRelaxed(1) >= maximumPendingResultsReady)
            q->futureInterface().d->internal_setThrottled(true);
    }

    QCoreApplication::postEvent(q, callOutEvent.clone());
}

//  from src/corelib/thread/qfuturewatcher.cpp, line 482, as _ZN25QFutureWatcherBasePrivate28callOutInterfaceDisconnectedEv
inline void QFutureWatcherBasePrivate::callOutInterfaceDisconnected()
{
    QCoreApplication::removePostedEvents(q_func(), QEvent::FutureCallOut);
}

//  from src/corelib/thread/qfuturewatcher.cpp, line 487, as _ZN25QFutureWatcherBasePrivate16sendCallOutEventEP19QFutureCallOutEvent
inline void QFutureWatcherBasePrivate::sendCallOutEvent(QFutureCallOutEvent *event)
{
    Q_Q(QFutureWatcherBase);

    switch (event->callOutType) {
        case QFutureCallOutEvent::Started:
            emit q->started();
        break;
        case QFutureCallOutEvent::Finished:
            emit q->finished();
        break;
        case QFutureCallOutEvent::Canceled:
            pendingResultsReady.storeRelaxed(0);
            emit q->canceled();
        break;
        case QFutureCallOutEvent::Suspending:
            if (q->futureInterface().isCanceled())
                break;
            emit q->suspending();
#if QT_DEPRECATED_SINCE(6, 0)
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
            emit q->paused();
QT_WARNING_POP
#endif
        break;
        case QFutureCallOutEvent::Suspended:
            if (q->futureInterface().isCanceled())
                break;
            emit q->suspended();
        break;
        case QFutureCallOutEvent::Resumed:
            if (q->futureInterface().isCanceled())
                break;
            emit q->resumed();
        break;
        case QFutureCallOutEvent::ResultsReady: {
            if (q->futureInterface().isCanceled())
                break;

            if (pendingResultsReady.fetchAndAddRelaxed(-1) <= maximumPendingResultsReady)
                q->futureInterface().setThrottled(false);

            const int beginIndex = event->index1;
            const int endIndex = event->index2;

            emit q->resultsReadyAt(beginIndex, endIndex);

            if (resultAtConnected.loadRelaxed() <= 0)
                break;

            for (int i = beginIndex; i < endIndex; ++i)
                emit q->resultReadyAt(i);

        } break;
        case QFutureCallOutEvent::Progress:
            if (q->futureInterface().isCanceled())
                break;

            emit q->progressValueChanged(event->index1);
            if (!event->text.isNull()) // ###
                emit q->progressTextChanged(event->text);
        break;
        case QFutureCallOutEvent::ProgressRange:
            emit q->progressRangeChanged(event->index1, event->index2);
        break;
        default: break;
    }
}
//  -----------------------------------------------------------------------

//  A QFutureWatcherBasePrivate that Python can take functions over in. Every QFutureWatcherBasePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(future)
typedef void (*CuteQFutureWatcherBasePrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(future)
class CuteQFutureWatcherBasePrivate : public QFutureWatcherBasePrivate {
public:
  using QFutureWatcherBasePrivate::QFutureWatcherBasePrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(future)
    if (!std::strcmp(key, "_ZN23QFutureCallOutInterface28callOutInterfaceDisconnectedEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(future)
    return false;
  }

#if QT_CONFIG(future)
  //  void QFutureWatcherBasePrivate::callOutInterfaceDisconnected()
  void callOutInterfaceDisconnected() override {
    if (taken[0]) {
      int handled = 0;
      CuteQFutureWatcherBasePrivateCall0 call = reinterpret_cast<CuteQFutureWatcherBasePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QFutureWatcherBasePrivate::callOutInterfaceDisconnected();
  }
#endif  // QT_CONFIG(future)
};

//  QFutureWatcherBase *QFutureWatcherBasePrivate::q_func()
extern "C" Q_DECL_EXPORT
QFutureWatcherBase *ritual_ZN25QFutureWatcherBasePrivate6q_funcEv(
    QFutureWatcherBasePrivate *self) {
  return self->q_func();
}

//  const QFutureWatcherBase *QFutureWatcherBasePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFutureWatcherBase *ritual_ZNK25QFutureWatcherBasePrivate6q_funcEv(
    const QFutureWatcherBasePrivate *self) {
  return self->q_func();
}

//  void QFutureWatcherBasePrivate::postCallOutEvent(const
//      QFutureCallOutEvent &callOutEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QFutureWatcherBasePrivate16postCallOutEventERK19QFutureCallOutEvent(
    QFutureWatcherBasePrivate *self,
    const QFutureCallOutEvent *callOutEvent) {
  self->postCallOutEvent(*callOutEvent);
}

//  void QFutureWatcherBasePrivate::callOutInterfaceDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QFutureWatcherBasePrivate28callOutInterfaceDisconnectedEv(
    QFutureWatcherBasePrivate *self) {
  self->callOutInterfaceDisconnected();
}

//  void QFutureWatcherBasePrivate::sendCallOutEvent(QFutureCallOutEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QFutureWatcherBasePrivate16sendCallOutEventEP19QFutureCallOutEvent(
    QFutureWatcherBasePrivate *self,
    QFutureCallOutEvent *event) {
  self->sendCallOutEvent(event);
}

//  QFutureWatcherBasePrivate as the QFutureCallOutInterface it is built on
extern "C" Q_DECL_EXPORT
QFutureCallOutInterface *ritual_cast_QFutureWatcherBasePrivate_QFutureCallOutInterface(
    QFutureWatcherBasePrivate *self) {
  return static_cast<QFutureCallOutInterface *>(self);
}

//  a Python function taken by a CuteQFutureWatcherBasePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFutureWatcherBasePrivate(
    QFutureWatcherBasePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFutureWatcherBasePrivate *>(self)->take(key, call);
}

//  void QFutureWatcherBasePrivate::callOutInterfaceDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QFutureWatcherBasePrivate28callOutInterfaceDisconnectedEv(
    QFutureWatcherBasePrivate *self) {
  self->QFutureWatcherBasePrivate::callOutInterfaceDisconnected();
}

#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
