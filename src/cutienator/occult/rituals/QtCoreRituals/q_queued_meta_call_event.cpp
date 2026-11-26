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

//  from src/corelib/kernel/qobject.cpp, line 659, as _ZN20QQueuedMetaCallEvent13copyArgValuesEiPKPKN9QtPrivate18QMetaTypeInterfaceEPKPKv
inline void QQueuedMetaCallEvent::copyArgValues(int argCount, const QtPrivate::QMetaTypeInterface * const *argTypes,
                                                const void * const *argValues)
{
    allocArgs();
    void **args = d.args_;
    QMetaType *types = reinterpret_cast<QMetaType *>(d.args_ + d.nargs_);
    int inplaceIndex = 0;

    if (argCount) {
        types[0] = QMetaType(); // return type
        args[0] = nullptr; // return value pointer
    }
    // no return value

    for (int n = 1; n < argCount; ++n) {
        types[n] = QMetaType(argTypes[n]);
        if (typeFitsInPlace(types[n]) && inplaceIndex < InplaceValuesCapacity) {
            // Copy-construct in place
            void *where = &valuesPrealloc_[inplaceIndex++].storage;
            types[n].construct(where, argValues[n]);
            args[n] = where;
        } else {
            // Allocate and copy-construct
            args[n] = types[n].create(argValues[n]);
        }
    }
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

//  QQueuedMetaCallEvent::QQueuedMetaCallEvent(ushort method_offset, ushort
//      method_relative, QObjectPrivate::StaticMetaCallFunction callFunction,
//      const QObject *sender, int signalId, int argCount, const
//      QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
//      *argValues)
extern "C" Q_DECL_EXPORT
QQueuedMetaCallEvent *ritual_ZN20QQueuedMetaCallEventC1EttPFvP7QObjectN11QMetaObject4CallEiPPvEPKS0_iiPKPKN9QtPrivate18QMetaTypeInterfaceEPKPKv(
    ushort method_offset,
    ushort method_relative,
    void *callFunction,
    const QObject *sender,
    int signalId,
    int argCount,
    const QtPrivate::QMetaTypeInterface *const *argTypes,
    const void *const *argValues) {
  return new CuteQQueuedMetaCallEvent(
      method_offset,
      method_relative,
      reinterpret_cast<QObjectPrivate::StaticMetaCallFunction>(callFunction),
      sender,
      signalId,
      argCount,
      argTypes,
      argValues);
}

//  QQueuedMetaCallEvent::QQueuedMetaCallEvent(QtPrivate::QSlotObjectBase
//      *slotObj, const QObject *sender, int signalId, int argCount, const
//      QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
//      *argValues)
extern "C" Q_DECL_EXPORT
QQueuedMetaCallEvent *ritual_ZN20QQueuedMetaCallEventC1EPN9QtPrivate15QSlotObjectBaseEPK7QObjectiiPKPKNS0_18QMetaTypeInterfaceEPKPKv(
    QtPrivate::QSlotObjectBase *slotObj,
    const QObject *sender,
    int signalId,
    int argCount,
    const QtPrivate::QMetaTypeInterface *const *argTypes,
    const void *const *argValues) {
  return new CuteQQueuedMetaCallEvent(
      slotObj,
      sender,
      signalId,
      argCount,
      argTypes,
      argValues);
}

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

//  void QQueuedMetaCallEvent::copyArgValues(int argCount, const
//      QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
//      *argValues)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQueuedMetaCallEvent13copyArgValuesEiPKPKN9QtPrivate18QMetaTypeInterfaceEPKPKv(
    QQueuedMetaCallEvent *self,
    int argCount,
    const QtPrivate::QMetaTypeInterface *const *argTypes,
    const void *const *argValues) {
  self->copyArgValues(argCount, argTypes, argValues);
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
