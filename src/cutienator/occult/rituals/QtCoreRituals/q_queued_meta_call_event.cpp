//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtconfigmacros.h>
#include "qobject.h"
#include "qobject_p.h"
#include "qobject_p_p.h"
#include "qmetaobject_p.h"
#include <QtCore/private/qtclasshelper_p.h>
#include <QtCore/qspan.h>
#include "qabstracteventdispatcher.h"
#include "qabstracteventdispatcher_p.h"
#include "qcoreapplication.h"
#include "qcoreapplication_p.h"
#include "qcoreevent_p.h"
#include "qloggingcategory.h"
#include "qvariant.h"
#include "qmetaobject.h"
#if QT_CONFIG(regularexpression)
#  include <qregularexpression.h>
#endif
#include <qthread.h>
#include <private/qthread_p.h>
#include <qdebug.h>
#include <qvarlengtharray.h>
#include <qscopeguard.h>
#include <qset.h>
#if QT_CONFIG(thread)
#include <private/qlatch_p.h>
#endif
#include <private/qorderedmutexlocker_p.h>
#include <private/qhooks_p.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qobject.cpp, line 644, as _ZN20QQueuedMetaCallEvent9allocArgsEv
inline void QQueuedMetaCallEvent::allocArgs()
{
    if (!d.nargs_)
        return;

    void *const memory = d.nargs_ * PtrAndTypeSize > sizeof(prealloc_) ?
        calloc(d.nargs_, PtrAndTypeSize) : prealloc_;

    Q_CHECK_PTR(memory);
    d.args_ = static_cast<void **>(memory);
}

//  from src/corelib/kernel/qobject.cpp, line 690, as _ZN20QQueuedMetaCallEvent15typeFitsInPlaceE9QMetaType
inline bool QQueuedMetaCallEvent::typeFitsInPlace(const QMetaType type)
{
    return (q20::cmp_less_equal(type.sizeOf(), sizeof(ArgValueStorage)) &&
            q20::cmp_less_equal(type.alignOf(), alignof(ArgValueStorage)));
}
//  -----------------------------------------------------------------------

//  A QQueuedMetaCallEvent that Python can take functions over in. Every QQueuedMetaCallEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQueuedMetaCallEventCall0)(const void *, QObject *, int *);
typedef void (*CuteQQueuedMetaCallEventCall1)(const void *, bool, int *);
typedef void * (*CuteQQueuedMetaCallEventCall2)(const void *, int *);
class CuteQQueuedMetaCallEvent : public QQueuedMetaCallEvent {
public:
  using QQueuedMetaCallEvent::QQueuedMetaCallEvent;
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
      CuteQQueuedMetaCallEventCall0 call = reinterpret_cast<CuteQQueuedMetaCallEventCall0>(taken[0]);
      call(this, object, &handled);
      if (handled) return;
    }
    QMetaCallEvent::placeMetaCall(object);
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQueuedMetaCallEventCall1 call = reinterpret_cast<CuteQQueuedMetaCallEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQueuedMetaCallEventCall2 call = reinterpret_cast<CuteQQueuedMetaCallEventCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QQueuedMetaCallEvent::~QQueuedMetaCallEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQueuedMetaCallEventD1Ev(QQueuedMetaCallEvent *self) {
  delete self;
}

//  void QQueuedMetaCallEvent::allocArgs()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQueuedMetaCallEvent9allocArgsEv(
    QQueuedMetaCallEvent *self) {
  self->allocArgs();
}

//  bool QQueuedMetaCallEvent::typeFitsInPlace(const QMetaType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQueuedMetaCallEvent15typeFitsInPlaceE9QMetaType(
    const QMetaType *type) {
  return QQueuedMetaCallEvent::typeFitsInPlace(*type);
}

//  a Python function taken by a CuteQQueuedMetaCallEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQueuedMetaCallEvent(
    QQueuedMetaCallEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQueuedMetaCallEvent *>(self)->take(key, call);
}
