//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qeventloop.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qeventloop.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QEventLoop that Python can take functions over in. Every QEventLoop
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventLoopCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventLoopCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventLoopCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventLoopCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventLoopCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventLoopCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventLoopCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQEventLoop : public QEventLoop {
public:
  using QEventLoop::QEventLoop;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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
  //  bool QEventLoop::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQEventLoopCall0 call = reinterpret_cast<CuteQEventLoopCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QEventLoop::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQEventLoopCall1 call = reinterpret_cast<CuteQEventLoopCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQEventLoopCall2 call = reinterpret_cast<CuteQEventLoopCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQEventLoopCall3 call = reinterpret_cast<CuteQEventLoopCall3>(taken[3]);
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
      CuteQEventLoopCall4 call = reinterpret_cast<CuteQEventLoopCall4>(taken[4]);
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
      CuteQEventLoopCall5 call = reinterpret_cast<CuteQEventLoopCall5>(taken[5]);
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
      CuteQEventLoopCall6 call = reinterpret_cast<CuteQEventLoopCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QEventLoop::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QEventLoop10metaObjectEv(
    const QEventLoop *self) {
  return self->metaObject();
}

//  QString QEventLoop::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QEventLoop2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QEventLoop::tr(s, c, n));
}

//  QEventLoopPrivate *QEventLoop::d_func()
extern "C" Q_DECL_EXPORT
QEventLoopPrivate *ritual_ZN10QEventLoop6d_funcEv(QEventLoop *self) {
  return self->d_func();
}

//  const QEventLoopPrivate *QEventLoop::d_func() const
extern "C" Q_DECL_EXPORT
const QEventLoopPrivate *ritual_ZNK10QEventLoop6d_funcEv(
    const QEventLoop *self) {
  return self->d_func();
}

//  QEventLoop::QEventLoop(QObject *parent)
extern "C" Q_DECL_EXPORT
QEventLoop *ritual_ZN10QEventLoopC1EP7QObject(QObject *parent) {
  return new CuteQEventLoop(parent);
}

//  QEventLoop::~QEventLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoopD1Ev(QEventLoop *self) {
  delete self;
}

//  bool QEventLoop::processEvents(ProcessEventsFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QEventLoop13processEventsE6QFlagsINS_17ProcessEventsFlagEE(
    QEventLoop *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QEventLoop::processEvents(ProcessEventsFlags flags, int maximumTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop13processEventsE6QFlagsINS_17ProcessEventsFlagEEi(
    QEventLoop *self,
    int flags,
    int maximumTime) {
  self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      maximumTime);
}

//  void QEventLoop::processEvents(ProcessEventsFlags flags, QDeadlineTimer
//      deadline)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop13processEventsE6QFlagsINS_17ProcessEventsFlagEE14QDeadlineTimer(
    QEventLoop *self,
    int flags,
    const QDeadlineTimer *deadline) {
  self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      *deadline);
}

//  int QEventLoop::exec(ProcessEventsFlags flags)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QEventLoop4execE6QFlagsINS_17ProcessEventsFlagEE(
    QEventLoop *self,
    int flags) {
  return self->exec(QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  bool QEventLoop::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QEventLoop9isRunningEv(const QEventLoop *self) {
  return self->isRunning();
}

//  void QEventLoop::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop6wakeUpEv(QEventLoop *self) {
  self->wakeUp();
}

//  bool QEventLoop::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QEventLoop5eventEP6QEvent(QEventLoop *self, QEvent *event) {
  return self->event(event);
}

//  void QEventLoop::exit(int returnCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop4exitEi(QEventLoop *self, int returnCode) {
  self->exit(returnCode);
}

//  void QEventLoop::quit()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QEventLoop4quitEv(QEventLoop *self) {
  self->quit();
}

//  a Python function taken by a CuteQEventLoop, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEventLoop(QEventLoop *self, const char *key, void *call) {
  return static_cast<CuteQEventLoop *>(self)->take(key, call);
}

//  bool QEventLoop::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QEventLoop5eventEP6QEvent(
    QEventLoop *self,
    QEvent *event) {
  return self->QEventLoop::event(event);
}
