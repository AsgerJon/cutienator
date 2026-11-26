//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtconfigmacros.h>
#include <QtCore/qobject.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/private/qobject_p_p.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/private/qtclasshelper_p.h>
#include <QtCore/qspan.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/private/qabstracteventdispatcher_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/private/qcoreevent_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#if QT_CONFIG(regularexpression)
#  include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qset.h>
#if QT_CONFIG(thread)
#include <QtCore/private/qlatch_p.h>
#endif
#include <QtCore/private/qorderedmutexlocker_p.h>
#include <QtCore/private/qhooks_p.h>
#include <new>
#include <mutex>
#include <memory>
#include <optional>
#include <iterator>
#include <ctype.h>
#include <limits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qobject.cpp, line 544, as _ZN14QMetaCallEventC1EPK7QObjectiONS_4DataE
inline QMetaCallEvent::QMetaCallEvent(const QObject *sender, int signalId, Data &&data)
    : QAbstractMetaCallEvent(sender, signalId),
      d(std::move(data))
{
}
//  -----------------------------------------------------------------------

//  A QMetaCallEvent that Python can take functions over in. Every QMetaCallEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetaCallEventCall0)(const void *, QObject *, int *);
typedef void (*CuteQMetaCallEventCall1)(const void *, bool, int *);
typedef void * (*CuteQMetaCallEventCall2)(const void *, int *);
class CuteQMetaCallEvent : public QMetaCallEvent {
public:
  using QMetaCallEvent::QMetaCallEvent;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QAbstractMetaCallEvent13placeMetaCallEP7QObject")) {
      taken[0] = call;
      return true;
    }
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

  //  void QMetaCallEvent::placeMetaCall(QObject *object)
  void placeMetaCall(QObject *object) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetaCallEventCall0 call = reinterpret_cast<CuteQMetaCallEventCall0>(taken[0]);
      call(this, object, &handled);
      if (handled) return;
    }
    QMetaCallEvent::placeMetaCall(object);
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetaCallEventCall1 call = reinterpret_cast<CuteQMetaCallEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetaCallEventCall2 call = reinterpret_cast<CuteQMetaCallEventCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QMetaCallEvent::QMetaCallEvent(ushort method_offset, ushort
//      method_relative, QObjectPrivate::StaticMetaCallFunction callFunction,
//      const QObject *sender, int signalId, void **args, QLatch *latch)
extern "C" Q_DECL_EXPORT
QMetaCallEvent *ritual_ZN14QMetaCallEventC1EttPFvP7QObjectN11QMetaObject4CallEiPPvEPKS0_iS5_P6QLatch(
    ushort method_offset,
    ushort method_relative,
    void *callFunction,
    const QObject *sender,
    int signalId,
    void **args,
    QLatch *latch) {
  return new CuteQMetaCallEvent(
      method_offset,
      method_relative,
      reinterpret_cast<QObjectPrivate::StaticMetaCallFunction>(callFunction),
      sender,
      signalId,
      args,
      latch);
}

//  QMetaCallEvent::QMetaCallEvent(QtPrivate::QSlotObjectBase *slotObj, const
//      QObject *sender, int signalId, void **args, QLatch *latch)
extern "C" Q_DECL_EXPORT
QMetaCallEvent *ritual_ZN14QMetaCallEventC1EPN9QtPrivate15QSlotObjectBaseEPK7QObjectiPPvP6QLatch(
    QtPrivate::QSlotObjectBase *slotObj,
    const QObject *sender,
    int signalId,
    void **args,
    QLatch *latch) {
  return new CuteQMetaCallEvent(slotObj, sender, signalId, args, latch);
}

//  void QMetaCallEvent::placeMetaCall(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMetaCallEvent13placeMetaCallEP7QObject(
    QMetaCallEvent *self,
    QObject *object) {
  self->placeMetaCall(object);
}

//  int QMetaCallEvent::id() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QMetaCallEvent2idEv(const QMetaCallEvent *self) {
  return self->id();
}

//  QMetaCallEvent::QMetaCallEvent(const QObject *sender, int signalId, Data
//      &&data)
extern "C" Q_DECL_EXPORT
QMetaCallEvent *ritual_ZN14QMetaCallEventC1EPK7QObjectiONS_4DataE(
    const QObject *sender,
    int signalId,
    QMetaCallEvent::Data *data) {
  return new CuteQMetaCallEvent(sender, signalId, std::move(*data));
}

//  a Python function taken by a CuteQMetaCallEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetaCallEvent(
    QMetaCallEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetaCallEvent *>(self)->take(key, call);
}

//  void QMetaCallEvent::placeMetaCall(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QMetaCallEvent13placeMetaCallEP7QObject(
    QMetaCallEvent *self,
    QObject *object) {
  self->QMetaCallEvent::placeMetaCall(object);
}
