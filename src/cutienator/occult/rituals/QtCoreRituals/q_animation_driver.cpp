//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAnimationDriver may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAnimationDriver : QAnimationDriver {
  using QAnimationDriver::start;
  using QAnimationDriver::stop;
};

//  A QAnimationDriver that Python can take functions over in. Every QAnimationDriver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAnimationDriverCall0)(const void *, int *);
typedef qint64 (*CuteQAnimationDriverCall1)(const void *, int *);
typedef void (*CuteQAnimationDriverCall2)(const void *, int *);
typedef void (*CuteQAnimationDriverCall3)(const void *, int *);
typedef bool (*CuteQAnimationDriverCall4)(const void *, QEvent *, int *);
typedef bool (*CuteQAnimationDriverCall5)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAnimationDriverCall6)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAnimationDriverCall7)(const void *, QChildEvent *, int *);
typedef void (*CuteQAnimationDriverCall8)(const void *, QEvent *, int *);
typedef void (*CuteQAnimationDriverCall9)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAnimationDriverCall10)(const void *, const QMetaMethod *, int *);
class CuteQAnimationDriver : public QAnimationDriver {
public:
  using QAnimationDriver::QAnimationDriver;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QAnimationDriver7advanceEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QAnimationDriver7elapsedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QAnimationDriver5startEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QAnimationDriver4stopEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void QAnimationDriver::advance()
  void advance() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAnimationDriverCall0 call = reinterpret_cast<CuteQAnimationDriverCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationDriver::advance();
  }

  //  qint64 QAnimationDriver::elapsed() const
  qint64 elapsed() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAnimationDriverCall1 call = reinterpret_cast<CuteQAnimationDriverCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAnimationDriver::elapsed();
  }

  //  void QAnimationDriver::start()
  void start() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAnimationDriverCall2 call = reinterpret_cast<CuteQAnimationDriverCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationDriver::start();
  }

  //  void QAnimationDriver::stop()
  void stop() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAnimationDriverCall3 call = reinterpret_cast<CuteQAnimationDriverCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationDriver::stop();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAnimationDriverCall4 call = reinterpret_cast<CuteQAnimationDriverCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAnimationDriverCall5 call = reinterpret_cast<CuteQAnimationDriverCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAnimationDriverCall6 call = reinterpret_cast<CuteQAnimationDriverCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAnimationDriverCall7 call = reinterpret_cast<CuteQAnimationDriverCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAnimationDriverCall8 call = reinterpret_cast<CuteQAnimationDriverCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAnimationDriverCall9 call = reinterpret_cast<CuteQAnimationDriverCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAnimationDriverCall10 call = reinterpret_cast<CuteQAnimationDriverCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QAnimationDriver::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAnimationDriver10metaObjectEv(
    const QAnimationDriver *self) {
  return self->metaObject();
}

//  QString QAnimationDriver::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QAnimationDriver2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAnimationDriver::tr(s, c, n));
}

//  QAnimationDriver::QAnimationDriver(QObject *parent)
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_ZN16QAnimationDriverC1EP7QObject(QObject *parent) {
  return new CuteQAnimationDriver(parent);
}

//  QAnimationDriver::~QAnimationDriver()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAnimationDriverD1Ev(QAnimationDriver *self) {
  delete self;
}

//  void QAnimationDriver::advance()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAnimationDriver7advanceEv(QAnimationDriver *self) {
  self->advance();
}

//  void QAnimationDriver::install()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAnimationDriver7installEv(QAnimationDriver *self) {
  self->install();
}

//  void QAnimationDriver::uninstall()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAnimationDriver9uninstallEv(QAnimationDriver *self) {
  self->uninstall();
}

//  bool QAnimationDriver::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAnimationDriver9isRunningEv(const QAnimationDriver *self) {
  return self->isRunning();
}

//  qint64 QAnimationDriver::elapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QAnimationDriver7elapsedEv(const QAnimationDriver *self) {
  return self->elapsed();
}

//  a Python function taken by a CuteQAnimationDriver, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAnimationDriver(
    QAnimationDriver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAnimationDriver *>(self)->take(key, call);
}

//  void QAnimationDriver::advance()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAnimationDriver7advanceEv(QAnimationDriver *self) {
  self->QAnimationDriver::advance();
}

//  qint64 QAnimationDriver::elapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK16QAnimationDriver7elapsedEv(
    const QAnimationDriver *self) {
  return self->QAnimationDriver::elapsed();
}

//  void QAnimationDriver::start()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAnimationDriver5startEv(QAnimationDriver *self) {
  static_cast<OwnQAnimationDriver *>(self)->OwnQAnimationDriver::start();
}

//  void QAnimationDriver::stop()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAnimationDriver4stopEv(QAnimationDriver *self) {
  static_cast<OwnQAnimationDriver *>(self)->OwnQAnimationDriver::stop();
}
