//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsingleshottimer_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QSingleShotTimer' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 5 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsingleshottimer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/private/qsingleshottimer_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/qthread.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtCore__QSingleShotTimer.cpp, line 1, as moc:QSingleShotTimer
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN16QSingleShotTimerE_t {};
} // unnamed namespace

template <> constexpr inline auto QSingleShotTimer::qt_create_metaobjectdata<qt_meta_tag_ZN16QSingleShotTimerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSingleShotTimer",
        "timeout",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'timeout'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QSingleShotTimer, qt_meta_tag_ZN16QSingleShotTimerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSingleShotTimer::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QSingleShotTimerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QSingleShotTimerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN16QSingleShotTimerE_t>.metaTypes,
    nullptr
} };

void QSingleShotTimer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QSingleShotTimer *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->timeout(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QSingleShotTimer::*)()>(_a, &QSingleShotTimer::timeout, 0))
            return;
    }
}

const QMetaObject *QSingleShotTimer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSingleShotTimer::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QSingleShotTimerE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QSingleShotTimer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QSingleShotTimer::timeout()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from src/corelib/kernel/qsingleshottimer.cpp, line 67, as _ZN16QSingleShotTimer10timerEventEP11QTimerEvent
inline void QSingleShotTimer::timerEvent(QTimerEvent *event)
{
    if (event->id() == Qt::TimerId::Invalid) {
        StartTimerEvent *startTimerEvent = static_cast<StartTimerEvent *>(event);
        Q_UNUSED(startTimerEvent->timer.release()); // it's the same as "this"
        const QDeadlineTimer &deadline = startTimerEvent->deadline;
        if (deadline.hasExpired()) {
            timerFinished();
        } else {
            timer.start(deadline.remainingTimeAsDuration(), deadline.timerType(), this);
            // we are now definitely in a thread that has an event dispatcher
            setParent(QThread::currentThread()->eventDispatcher());
        }
    } else {
        // need to kill the timer _before_ we emit timeout() in case the
        // slot connected to timeout calls processEvents()
        timer.stop();

        timerFinished();
    }
}

//  from src/corelib/kernel/qsingleshottimer.cpp, line 35, as _ZN16QSingleShotTimerD0Ev
inline QSingleShotTimer::~QSingleShotTimer() = default;

//  from src/corelib/kernel/qsingleshottimer.cpp, line 15, as _ZN16QSingleShotTimerC1ENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObjectPKc
inline QSingleShotTimer::QSingleShotTimer(Duration interval, Qt::TimerType timerType,
                                   const QObject *r, const char *member)
    : QObject(QAbstractEventDispatcher::instance())
{
    connect(this, SIGNAL(timeout()), r, member);
    startTimerForReceiver(interval, timerType, r);
}

//  from src/corelib/kernel/qsingleshottimer.cpp, line 23, as _ZN16QSingleShotTimerC1ENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObjectPN9QtPrivate15QSlotObjectBaseE
inline QSingleShotTimer::QSingleShotTimer(Duration interval, Qt::TimerType timerType,
                                   const QObject *r, QtPrivate::QSlotObjectBase *slotObj)
    : QObject(QAbstractEventDispatcher::instance())
{
    int signal_index = QMetaObjectPrivate::signalOffset(&staticMetaObject);
    Q_ASSERT(QMetaObjectPrivate::signal(&staticMetaObject, signal_index).name() == "timeout");
    QObjectPrivate::connectImpl(this, signal_index, r ? r : this, nullptr, slotObj,
                                Qt::AutoConnection, nullptr, &staticMetaObject);

    startTimerForReceiver(interval, timerType, r);
}

//  from src/corelib/kernel/qsingleshottimer.cpp, line 42, as _ZN16QSingleShotTimer21startTimerForReceiverENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObject
inline void QSingleShotTimer::startTimerForReceiver(Duration interval, Qt::TimerType timerType,
                                             const QObject *receiver)
{
    if (receiver && receiver->thread() != thread()) {
        QObjectPrivate *d_ptr = QObjectPrivate::get(this);
        d_ptr->sendChildEvents = false;

        setParent(nullptr);
        moveToThread(receiver->thread());

        QCoreApplication::postEvent(this,
                                    new StartTimerEvent(this, QDeadlineTimer(interval, timerType)));
        // the event owns "this" and is handled concurrently, so unsafe to
        // access "this" beyond this point
    } else {
        timer.start(interval, timerType, this);
    }
}

//  from src/corelib/kernel/qsingleshottimer.cpp, line 61, as _ZN16QSingleShotTimer13timerFinishedEv
inline void QSingleShotTimer::timerFinished()
{
    Q_EMIT timeout();
    delete this;
}
//  -----------------------------------------------------------------------

//  A QSingleShotTimer that Python can take functions over in. Every QSingleShotTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSingleShotTimerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSingleShotTimerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSingleShotTimer : public QSingleShotTimer {
public:
  using QSingleShotTimer::QSingleShotTimer;
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
  //  void QSingleShotTimer::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSingleShotTimerCall0 call = reinterpret_cast<CuteQSingleShotTimerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSingleShotTimer::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSingleShotTimerCall1 call = reinterpret_cast<CuteQSingleShotTimerCall1>(taken[1]);
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
      CuteQSingleShotTimerCall2 call = reinterpret_cast<CuteQSingleShotTimerCall2>(taken[2]);
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
      CuteQSingleShotTimerCall3 call = reinterpret_cast<CuteQSingleShotTimerCall3>(taken[3]);
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
      CuteQSingleShotTimerCall4 call = reinterpret_cast<CuteQSingleShotTimerCall4>(taken[4]);
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
      CuteQSingleShotTimerCall5 call = reinterpret_cast<CuteQSingleShotTimerCall5>(taken[5]);
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
      CuteQSingleShotTimerCall6 call = reinterpret_cast<CuteQSingleShotTimerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSingleShotTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QSingleShotTimer10metaObjectEv(
    const QSingleShotTimer *self) {
  return self->metaObject();
}

//  void *QSingleShotTimer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QSingleShotTimer11qt_metacastEPKc(
    QSingleShotTimer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSingleShotTimer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QSingleShotTimer11qt_metacallEN11QMetaObject4CallEiPPv(
    QSingleShotTimer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSingleShotTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QSingleShotTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSingleShotTimer::tr(s, c, n));
}

//  QSingleShotTimer::QSingleShotTimer(Duration interval, Qt::TimerType
//      timerType, const QObject *r, const char *member)
extern "C" Q_DECL_EXPORT
QSingleShotTimer *ritual_ZN16QSingleShotTimerC1ENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObjectPKc(
    long long interval,
    Qt::TimerType timerType,
    const QObject *r,
    const char *member) {
  return new CuteQSingleShotTimer(
      QSingleShotTimer::Duration(interval),
      timerType,
      r,
      member);
}

//  QSingleShotTimer::QSingleShotTimer(Duration interval, Qt::TimerType
//      timerType, const QObject *r, QtPrivate::QSlotObjectBase *slotObj)
extern "C" Q_DECL_EXPORT
QSingleShotTimer *ritual_ZN16QSingleShotTimerC1ENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    long long interval,
    Qt::TimerType timerType,
    const QObject *r,
    QtPrivate::QSlotObjectBase *slotObj) {
  return new CuteQSingleShotTimer(
      QSingleShotTimer::Duration(interval),
      timerType,
      r,
      slotObj);
}

//  QSingleShotTimer::~QSingleShotTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSingleShotTimerD1Ev(QSingleShotTimer *self) {
  delete self;
}

//  void QSingleShotTimer::startTimerForReceiver(Duration interval,
//      Qt::TimerType timerType, const QObject *receiver)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSingleShotTimer21startTimerForReceiverENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObject(
    QSingleShotTimer *self,
    long long interval,
    Qt::TimerType timerType,
    const QObject *receiver) {
  self->startTimerForReceiver(
      QSingleShotTimer::Duration(interval),
      timerType,
      receiver);
}

//  void QSingleShotTimer::timeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSingleShotTimer7timeoutEv(QSingleShotTimer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSingleShotTimer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "timeout()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "timeout()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QSingleShotTimer::timerFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSingleShotTimer13timerFinishedEv(QSingleShotTimer *self) {
  self->timerFinished();
}

//  void QSingleShotTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSingleShotTimer10timerEventEP11QTimerEvent(
    QSingleShotTimer *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  a Python function taken by a CuteQSingleShotTimer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSingleShotTimer(
    QSingleShotTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSingleShotTimer *>(self)->take(key, call);
}

//  void QSingleShotTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSingleShotTimer10timerEventEP11QTimerEvent(
    QSingleShotTimer *self,
    QTimerEvent *a0) {
  self->QSingleShotTimer::timerEvent(a0);
}
