//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/qaudiolistener.h, Qt 6.12.0. Changes made here are lost.
#include <QtSpatialAudio/qaudiolistener.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAudioListener that Python can take functions over in. Every QAudioListener
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioListenerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioListenerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioListenerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioListenerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioListenerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioListenerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioListenerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAudioListener : public QAudioListener {
public:
  using QAudioListener::QAudioListener;
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAudioListenerCall0 call = reinterpret_cast<CuteQAudioListenerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAudioListenerCall1 call = reinterpret_cast<CuteQAudioListenerCall1>(taken[1]);
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
      CuteQAudioListenerCall2 call = reinterpret_cast<CuteQAudioListenerCall2>(taken[2]);
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
      CuteQAudioListenerCall3 call = reinterpret_cast<CuteQAudioListenerCall3>(taken[3]);
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
      CuteQAudioListenerCall4 call = reinterpret_cast<CuteQAudioListenerCall4>(taken[4]);
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
      CuteQAudioListenerCall5 call = reinterpret_cast<CuteQAudioListenerCall5>(taken[5]);
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
      CuteQAudioListenerCall6 call = reinterpret_cast<CuteQAudioListenerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QAudioListener::QAudioListener(QAudioEngine *engine)
extern "C" Q_DECL_EXPORT
QAudioListener *ritual_ZN14QAudioListenerC1EP12QAudioEngine(
    QAudioEngine *engine) {
  return new CuteQAudioListener(engine);
}

//  QAudioListener::~QAudioListener()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAudioListenerD1Ev(QAudioListener *self) {
  delete self;
}

//  void QAudioListener::setPosition(QVector3D pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAudioListener11setPositionE9QVector3D(
    QAudioListener *self,
    const QVector3D *pos) {
  self->setPosition(*pos);
}

//  QVector3D QAudioListener::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK14QAudioListener8positionEv(
    const QAudioListener *self) {
  return new QVector3D(self->position());
}

//  void QAudioListener::setRotation(const QQuaternion &q)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAudioListener11setRotationERK11QQuaternion(
    QAudioListener *self,
    const QQuaternion *q) {
  self->setRotation(*q);
}

//  QQuaternion QAudioListener::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK14QAudioListener8rotationEv(
    const QAudioListener *self) {
  return new QQuaternion(self->rotation());
}

//  QAudioEngine *QAudioListener::engine() const
extern "C" Q_DECL_EXPORT
QAudioEngine *ritual_ZNK14QAudioListener6engineEv(
    const QAudioListener *self) {
  return self->engine();
}

//  QAudioListenerPrivate *QAudioListener::d_func()
extern "C" Q_DECL_EXPORT
QAudioListenerPrivate *ritual_ZN14QAudioListener6d_funcEv(
    QAudioListener *self) {
  return self->d_func();
}

//  const QAudioListenerPrivate *QAudioListener::d_func() const
extern "C" Q_DECL_EXPORT
const QAudioListenerPrivate *ritual_ZNK14QAudioListener6d_funcEv(
    const QAudioListener *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAudioListener, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioListener(
    QAudioListener *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAudioListener *>(self)->take(key, call);
}
