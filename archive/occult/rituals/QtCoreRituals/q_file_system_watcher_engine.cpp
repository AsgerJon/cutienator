//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/QtCore>
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_p.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QFileSystemWatcherEngine that Python can take functions over in. Every QFileSystemWatcherEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQFileSystemWatcherEngineCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQFileSystemWatcherEngineCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQFileSystemWatcherEngineCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQFileSystemWatcherEngineCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQFileSystemWatcherEngineCall4)(const void *, QEvent *, int *);
typedef void (*CuteQFileSystemWatcherEngineCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQFileSystemWatcherEngineCall6)(const void *, const QMetaMethod *, int *);
class CuteQFileSystemWatcherEngine : public QFileSystemWatcherEngine {
public:
  using QFileSystemWatcherEngine::QFileSystemWatcherEngine;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileSystemWatcherEngineCall0 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileSystemWatcherEngineCall1 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFileSystemWatcherEngineCall2 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFileSystemWatcherEngineCall3 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFileSystemWatcherEngineCall4 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFileSystemWatcherEngineCall5 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQFileSystemWatcherEngineCall6 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QFileSystemWatcherEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QFileSystemWatcherEngine10metaObjectEv(
    const QFileSystemWatcherEngine *self) {
  return self->metaObject();
}

//  a Python function taken by a CuteQFileSystemWatcherEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileSystemWatcherEngine(
    QFileSystemWatcherEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileSystemWatcherEngine *>(self)->take(key, call);
}
