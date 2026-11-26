//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qeventdispatcher_glib_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(glib) && defined(Q_OS_UNIX)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qeventdispatcher_glib_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPAEventDispatcherGlib that Python can take functions over in. Every QPAEventDispatcherGlib
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPAEventDispatcherGlibCall0)(const void *, int, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQPAEventDispatcherGlibCall1)(const void *, int, const QDeadlineTimer *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQPAEventDispatcherGlibCall2)(const void *, int *);
typedef void (*CuteQPAEventDispatcherGlibCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPAEventDispatcherGlibCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPAEventDispatcherGlibCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPAEventDispatcherGlibCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPAEventDispatcherGlibCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPAEventDispatcherGlibCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPAEventDispatcherGlibCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPAEventDispatcherGlibCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPAEventDispatcherGlib : public QPAEventDispatcherGlib {
public:
  using QPAEventDispatcherGlib::QPAEventDispatcherGlib;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE")) {
      taken[0] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher10startingUpEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher11closingDownEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool
  //      QPAEventDispatcherGlib::processEvents(QEventLoop::ProcessEventsFl
  //      ags flags)
  bool processEvents(QEventLoop::ProcessEventsFlags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall0 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QPAEventDispatcherGlib::processEvents(flags);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop
  //      ::ProcessEventsFlags flags, QDeadlineTimer deadline)
  bool processEventsWithDeadline(
      QEventLoop::ProcessEventsFlags flags,
      QDeadlineTimer deadline) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall1 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall1>(taken[1]);
      bool given = call(this, static_cast<int>(flags.toInt()), &deadline, &handled);
      if (handled) return given;
    }
    return QAbstractEventDispatcherV2::processEventsWithDeadline(flags, deadline);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QAbstractEventDispatcher::startingUp()
  void startingUp() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall2 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::startingUp();
  }

  //  void QAbstractEventDispatcher::closingDown()
  void closingDown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall3 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::closingDown();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall4 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall5 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall6 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall7 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall8 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall9 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPAEventDispatcherGlibCall10 call = reinterpret_cast<CuteQPAEventDispatcherGlibCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPAEventDispatcherGlib::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QPAEventDispatcherGlib10metaObjectEv(
    const QPAEventDispatcherGlib *self) {
  return self->metaObject();
}

//  void *QPAEventDispatcherGlib::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QPAEventDispatcherGlib11qt_metacastEPKc(
    QPAEventDispatcherGlib *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPAEventDispatcherGlib::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QPAEventDispatcherGlib11qt_metacallEN11QMetaObject4CallEiPPv(
    QPAEventDispatcherGlib *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPAEventDispatcherGlib::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QPAEventDispatcherGlib2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPAEventDispatcherGlib::tr(s, c, n));
}

//  QPAEventDispatcherGlibPrivate *QPAEventDispatcherGlib::d_func()
extern "C" Q_DECL_EXPORT
QPAEventDispatcherGlibPrivate *ritual_ZN22QPAEventDispatcherGlib6d_funcEv(
    QPAEventDispatcherGlib *self) {
  return self->d_func();
}

//  const QPAEventDispatcherGlibPrivate *QPAEventDispatcherGlib::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QPAEventDispatcherGlibPrivate *ritual_ZNK22QPAEventDispatcherGlib6d_funcEv(
    const QPAEventDispatcherGlib *self) {
  return self->d_func();
}

//  QPAEventDispatcherGlib::QPAEventDispatcherGlib(QObject *parent)
extern "C" Q_DECL_EXPORT
QPAEventDispatcherGlib *ritual_ZN22QPAEventDispatcherGlibC1EP7QObject(
    QObject *parent) {
  return new CuteQPAEventDispatcherGlib(parent);
}

//  QPAEventDispatcherGlib::~QPAEventDispatcherGlib()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPAEventDispatcherGlibD1Ev(QPAEventDispatcherGlib *self) {
  delete self;
}

//  bool QPAEventDispatcherGlib::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QPAEventDispatcherGlib13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QPAEventDispatcherGlib *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  a Python function taken by a CuteQPAEventDispatcherGlib, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPAEventDispatcherGlib(
    QPAEventDispatcherGlib *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPAEventDispatcherGlib *>(self)->take(key, call);
}

//  bool QPAEventDispatcherGlib::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QPAEventDispatcherGlib13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QPAEventDispatcherGlib *self,
    int flags) {
  return self->QPAEventDispatcherGlib::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

#endif  // QT_CONFIG(glib) && defined(Q_OS_UNIX)
