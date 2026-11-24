//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qunixeventdispatcher_qpa_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_UNIX) && !defined(Q_OS_WASM)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qunixeventdispatcher_qpa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QUnixEventDispatcherQPA that Python can take functions over in. Every QUnixEventDispatcherQPA
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQUnixEventDispatcherQPACall0)(const void *, int, int *);
typedef void (*CuteQUnixEventDispatcherQPACall1)(const void *, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQUnixEventDispatcherQPACall2)(const void *, int, const QDeadlineTimer *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQUnixEventDispatcherQPACall3)(const void *, int *);
typedef void (*CuteQUnixEventDispatcherQPACall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUnixEventDispatcherQPACall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUnixEventDispatcherQPACall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUnixEventDispatcherQPACall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUnixEventDispatcherQPACall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUnixEventDispatcherQPACall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUnixEventDispatcherQPACall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUnixEventDispatcherQPACall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQUnixEventDispatcherQPA : public QUnixEventDispatcherQPA {
public:
  using QUnixEventDispatcherQPA::QUnixEventDispatcherQPA;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher6wakeUpEv")) {
      taken[1] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher10startingUpEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher11closingDownEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool
  //      QUnixEventDispatcherQPA::processEvents(QEventLoop::ProcessEventsF
  //      lags flags)
  bool processEvents(QEventLoop::ProcessEventsFlags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall0 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QUnixEventDispatcherQPA::processEvents(flags);
  }

  //  void QEventDispatcherUNIX::wakeUp()
  void wakeUp() override {
    if (taken[1]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall1 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherUNIX::wakeUp();
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop
  //      ::ProcessEventsFlags flags, QDeadlineTimer deadline)
  bool processEventsWithDeadline(
      QEventLoop::ProcessEventsFlags flags,
      QDeadlineTimer deadline) override {
    if (taken[2]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall2 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall2>(taken[2]);
      bool given = call(this, static_cast<int>(flags.toInt()), &deadline, &handled);
      if (handled) return given;
    }
    return QAbstractEventDispatcherV2::processEventsWithDeadline(flags, deadline);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QAbstractEventDispatcher::startingUp()
  void startingUp() override {
    if (taken[3]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall3 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::startingUp();
  }

  //  void QAbstractEventDispatcher::closingDown()
  void closingDown() override {
    if (taken[4]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall4 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::closingDown();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall5 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall6 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall7 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall8 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall9 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall10 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQUnixEventDispatcherQPACall11 call = reinterpret_cast<CuteQUnixEventDispatcherQPACall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QUnixEventDispatcherQPA::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QUnixEventDispatcherQPA10metaObjectEv(
    const QUnixEventDispatcherQPA *self) {
  return self->metaObject();
}

//  QString QUnixEventDispatcherQPA::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QUnixEventDispatcherQPA2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUnixEventDispatcherQPA::tr(s, c, n));
}

//  QUnixEventDispatcherQPA::QUnixEventDispatcherQPA(QObject *parent)
extern "C" Q_DECL_EXPORT
QUnixEventDispatcherQPA *ritual_ZN23QUnixEventDispatcherQPAC1EP7QObject(
    QObject *parent) {
  return new CuteQUnixEventDispatcherQPA(parent);
}

//  QUnixEventDispatcherQPA::~QUnixEventDispatcherQPA()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QUnixEventDispatcherQPAD1Ev(QUnixEventDispatcherQPA *self) {
  delete self;
}

//  bool
//      QUnixEventDispatcherQPA::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QUnixEventDispatcherQPA13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QUnixEventDispatcherQPA *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  a Python function taken by a CuteQUnixEventDispatcherQPA, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUnixEventDispatcherQPA(
    QUnixEventDispatcherQPA *self,
    const char *key,
    void *call) {
  return static_cast<CuteQUnixEventDispatcherQPA *>(self)->take(key, call);
}

//  bool
//      QUnixEventDispatcherQPA::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QUnixEventDispatcherQPA13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QUnixEventDispatcherQPA *self,
    int flags) {
  return self->QUnixEventDispatcherQPA::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

#endif  // defined(Q_OS_UNIX) && !defined(Q_OS_WASM)
