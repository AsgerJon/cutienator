//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qwasmanimationdriver_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WASM)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qwasmanimationdriver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWasmAnimationDriver may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWasmAnimationDriver : QWasmAnimationDriver {
  using QWasmAnimationDriver::start;
  using QWasmAnimationDriver::stop;
};

//  A QWasmAnimationDriver that Python can take functions over in. Every QWasmAnimationDriver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef qint64 (*CuteQWasmAnimationDriverCall0)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQWasmAnimationDriverCall1)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQWasmAnimationDriverCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQWasmAnimationDriverCall3)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWasmAnimationDriverCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWasmAnimationDriverCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWasmAnimationDriverCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWasmAnimationDriverCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWasmAnimationDriverCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWasmAnimationDriverCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWasmAnimationDriverCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWasmAnimationDriver : public QWasmAnimationDriver {
public:
  using QWasmAnimationDriver::QWasmAnimationDriver;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK16QAnimationDriver7elapsedEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN16QAnimationDriver5startEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN16QAnimationDriver4stopEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN16QAnimationDriver7advanceEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
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

#if QT_CONFIG(animation)
  //  qint64 QWasmAnimationDriver::elapsed() const
  qint64 elapsed() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWasmAnimationDriverCall0 call = reinterpret_cast<CuteQWasmAnimationDriverCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QWasmAnimationDriver::elapsed();
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QWasmAnimationDriver::start()
  void start() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWasmAnimationDriverCall1 call = reinterpret_cast<CuteQWasmAnimationDriverCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QWasmAnimationDriver::start();
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QWasmAnimationDriver::stop()
  void stop() override {
    if (taken[2]) {
      int handled = 0;
      CuteQWasmAnimationDriverCall2 call = reinterpret_cast<CuteQWasmAnimationDriverCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWasmAnimationDriver::stop();
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAnimationDriver::advance()
  void advance() override {
    if (taken[3]) {
      int handled = 0;
      CuteQWasmAnimationDriverCall3 call = reinterpret_cast<CuteQWasmAnimationDriverCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationDriver::advance();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWasmAnimationDriverCall4 call = reinterpret_cast<CuteQWasmAnimationDriverCall4>(taken[4]);
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
      CuteQWasmAnimationDriverCall5 call = reinterpret_cast<CuteQWasmAnimationDriverCall5>(taken[5]);
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
      CuteQWasmAnimationDriverCall6 call = reinterpret_cast<CuteQWasmAnimationDriverCall6>(taken[6]);
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
      CuteQWasmAnimationDriverCall7 call = reinterpret_cast<CuteQWasmAnimationDriverCall7>(taken[7]);
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
      CuteQWasmAnimationDriverCall8 call = reinterpret_cast<CuteQWasmAnimationDriverCall8>(taken[8]);
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
      CuteQWasmAnimationDriverCall9 call = reinterpret_cast<CuteQWasmAnimationDriverCall9>(taken[9]);
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
      CuteQWasmAnimationDriverCall10 call = reinterpret_cast<CuteQWasmAnimationDriverCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWasmAnimationDriver::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QWasmAnimationDriver10metaObjectEv(
    const QWasmAnimationDriver *self) {
  return self->metaObject();
}

//  QString QWasmAnimationDriver::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QWasmAnimationDriver2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWasmAnimationDriver::tr(s, c, n));
}

//  QWasmAnimationDriver::QWasmAnimationDriver(QUnifiedTimer *unifiedTimer)
extern "C" Q_DECL_EXPORT
QWasmAnimationDriver *ritual_ZN20QWasmAnimationDriverC1EP13QUnifiedTimer(
    QUnifiedTimer *unifiedTimer) {
  return new CuteQWasmAnimationDriver(unifiedTimer);
}

//  QWasmAnimationDriver::~QWasmAnimationDriver()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWasmAnimationDriverD1Ev(QWasmAnimationDriver *self) {
  delete self;
}

//  qint64 QWasmAnimationDriver::elapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QWasmAnimationDriver7elapsedEv(
    const QWasmAnimationDriver *self) {
  return self->elapsed();
}

//  void QWasmAnimationDriver::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWasmAnimationDriver5startEv(QWasmAnimationDriver *self) {
  self->start();
}

//  void QWasmAnimationDriver::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWasmAnimationDriver4stopEv(QWasmAnimationDriver *self) {
  self->stop();
}

//  void QWasmAnimationDriver::handleAnimationFrame(double timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWasmAnimationDriver20handleAnimationFrameEd(
    QWasmAnimationDriver *self,
    double timestamp) {
  self->handleAnimationFrame(timestamp);
}

//  void QWasmAnimationDriver::handleFallbackTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWasmAnimationDriver21handleFallbackTimeoutEv(
    QWasmAnimationDriver *self) {
  self->handleFallbackTimeout();
}

//  double QWasmAnimationDriver::getCurrentTimeFromTimeline() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QWasmAnimationDriver26getCurrentTimeFromTimelineEv(
    const QWasmAnimationDriver *self) {
  return self->getCurrentTimeFromTimeline();
}

//  a Python function taken by a CuteQWasmAnimationDriver, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWasmAnimationDriver(
    QWasmAnimationDriver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWasmAnimationDriver *>(self)->take(key, call);
}

//  qint64 QWasmAnimationDriver::elapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK20QWasmAnimationDriver7elapsedEv(
    const QWasmAnimationDriver *self) {
  return self->QWasmAnimationDriver::elapsed();
}

//  void QWasmAnimationDriver::start()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QWasmAnimationDriver5startEv(
    QWasmAnimationDriver *self) {
  static_cast<OwnQWasmAnimationDriver *>(self)->OwnQWasmAnimationDriver::start();
}

//  void QWasmAnimationDriver::stop()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QWasmAnimationDriver4stopEv(QWasmAnimationDriver *self) {
  static_cast<OwnQWasmAnimationDriver *>(self)->OwnQWasmAnimationDriver::stop();
}

#endif  // defined(Q_OS_WASM)
