//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudioinput.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand: 'ritual_callback_ZN11QAudioInput21setDisconnectFunctionESt
//  8functionIFvvEE'. Kept as it is when the generator runs again.
#include <QtMultimedia/qaudioinput.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <functional>

//  A QAudioInput that Python can take functions over in. Every QAudioInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioInputCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioInputCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioInputCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioInputCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioInputCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioInputCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioInputCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAudioInput : public QAudioInput {
public:
  using QAudioInput::QAudioInput;
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
      CuteQAudioInputCall0 call = reinterpret_cast<CuteQAudioInputCall0>(taken[0]);
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
      CuteQAudioInputCall1 call = reinterpret_cast<CuteQAudioInputCall1>(taken[1]);
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
      CuteQAudioInputCall2 call = reinterpret_cast<CuteQAudioInputCall2>(taken[2]);
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
      CuteQAudioInputCall3 call = reinterpret_cast<CuteQAudioInputCall3>(taken[3]);
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
      CuteQAudioInputCall4 call = reinterpret_cast<CuteQAudioInputCall4>(taken[4]);
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
      CuteQAudioInputCall5 call = reinterpret_cast<CuteQAudioInputCall5>(taken[5]);
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
      CuteQAudioInputCall6 call = reinterpret_cast<CuteQAudioInputCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAudioInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QAudioInput10metaObjectEv(
    const QAudioInput *self) {
  return self->metaObject();
}

//  void *QAudioInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QAudioInput11qt_metacastEPKc(
    QAudioInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAudioInput::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QAudioInput11qt_metacallEN11QMetaObject4CallEiPPv(
    QAudioInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAudioInput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QAudioInput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAudioInput::tr(s, c, n));
}

//  QAudioInput::QAudioInput(QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioInput *ritual_ZN11QAudioInputC1EP7QObject(QObject *parent) {
  return new CuteQAudioInput(parent);
}

//  QAudioInput::QAudioInput(const QAudioDevice &deviceInfo, QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioInput *ritual_ZN11QAudioInputC1ERK12QAudioDeviceP7QObject(
    const QAudioDevice *deviceInfo,
    QObject *parent) {
  return new CuteQAudioInput(*deviceInfo, parent);
}

//  QAudioInput::~QAudioInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAudioInputD1Ev(QAudioInput *self) {
  delete self;
}

//  QAudioDevice QAudioInput::device() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK11QAudioInput6deviceEv(const QAudioInput *self) {
  return new QAudioDevice(self->device());
}

//  float QAudioInput::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QAudioInput6volumeEv(const QAudioInput *self) {
  return self->volume();
}

//  bool QAudioInput::isMuted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QAudioInput7isMutedEv(const QAudioInput *self) {
  return self->isMuted();
}

//  void QAudioInput::setDevice(const QAudioDevice &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAudioInput9setDeviceERK12QAudioDevice(
    QAudioInput *self,
    const QAudioDevice *device) {
  self->setDevice(*device);
}

//  void QAudioInput::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAudioInput9setVolumeEf(QAudioInput *self, float volume) {
  self->setVolume(volume);
}

//  void QAudioInput::setMuted(bool muted)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAudioInput8setMutedEb(QAudioInput *self, bool muted) {
  self->setMuted(muted);
}

//  void QAudioInput::deviceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAudioInput13deviceChangedEv(QAudioInput *self) {
  self->deviceChanged();
}

//  void QAudioInput::volumeChanged(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAudioInput13volumeChangedEf(
    QAudioInput *self,
    float volume) {
  self->volumeChanged(volume);
}

//  void QAudioInput::mutedChanged(bool muted)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAudioInput12mutedChangedEb(QAudioInput *self, bool muted) {
  self->mutedChanged(muted);
}

//  QPlatformAudioInput *QAudioInput::handle() const
extern "C" Q_DECL_EXPORT
QPlatformAudioInput *ritual_ZNK11QAudioInput6handleEv(
    const QAudioInput *self) {
  return self->handle();
}

//  void QAudioInput::setDisconnectFunction(std::function<void ()>
//      disconnectFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAudioInput21setDisconnectFunctionESt8functionIFvvEE(
    QAudioInput *self,
    const std::function<void ()> *disconnectFunction) {
  self->setDisconnectFunction(*disconnectFunction);
}

//  a Python function taken by a CuteQAudioInput, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioInput(
    QAudioInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAudioInput *>(self)->take(key, call);
}

//  void QAudioInput::setDisconnectFunction(std::function<void ()>
//      disconnectFunction)
extern "C" Q_DECL_EXPORT
void ritual_callback_ZN11QAudioInput21setDisconnectFunctionESt8functionIFvvEE(
    QAudioInput *self,
    void *call,
    void *context) {
  auto function = reinterpret_cast<void (*)(void *)>(call);
  self->setDisconnectFunction([function, context]() {
    function(context);
  });
}
