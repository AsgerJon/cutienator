//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/QtCore>
#include <QtCore/6.12.0/QtCore/private/qthread_p.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDaemonThread that Python can take functions over in. Every QDaemonThread
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQDaemonThreadCall0)(const void *, QEvent *, int *);
typedef void (*CuteQDaemonThreadCall1)(const void *, int *);
typedef bool (*CuteQDaemonThreadCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQDaemonThreadCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQDaemonThreadCall4)(const void *, QChildEvent *, int *);
typedef void (*CuteQDaemonThreadCall5)(const void *, QEvent *, int *);
typedef void (*CuteQDaemonThreadCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQDaemonThreadCall7)(const void *, const QMetaMethod *, int *);
class CuteQDaemonThread : public QDaemonThread {
public:
  using QDaemonThread::QDaemonThread;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDaemonThreadCall0 call = reinterpret_cast<CuteQDaemonThreadCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QThread::event(event);
  }

  //  void QThread::run()
  void run() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDaemonThreadCall1 call = reinterpret_cast<CuteQDaemonThreadCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QThread::run();
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDaemonThreadCall2 call = reinterpret_cast<CuteQDaemonThreadCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDaemonThreadCall3 call = reinterpret_cast<CuteQDaemonThreadCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDaemonThreadCall4 call = reinterpret_cast<CuteQDaemonThreadCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDaemonThreadCall5 call = reinterpret_cast<CuteQDaemonThreadCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDaemonThreadCall6 call = reinterpret_cast<CuteQDaemonThreadCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDaemonThreadCall7 call = reinterpret_cast<CuteQDaemonThreadCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  QDaemonThread::QDaemonThread(QObject *parent)
extern "C" Q_DECL_EXPORT
QDaemonThread *ritual_ZN13QDaemonThreadC1EP7QObject(QObject *parent) {
  return new CuteQDaemonThread(parent);
}

//  QDaemonThread::~QDaemonThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDaemonThreadD1Ev(QDaemonThread *self) {
  delete self;
}

//  a Python function taken by a CuteQDaemonThread, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDaemonThread(
    QDaemonThread *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDaemonThread *>(self)->take(key, call);
}
