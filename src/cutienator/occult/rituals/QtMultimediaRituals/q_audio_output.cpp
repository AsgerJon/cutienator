//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudiooutput.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand: 'ritual_callback_ZN12QAudioOutput21setDisconnectFunctionES
//  t8functionIFvvEE'. Kept as it is when the generator runs again.
#include <QtMultimedia/qaudiooutput.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <functional>

//  A QAudioOutput that Python can take functions over in. Every QAudioOutput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioOutputCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioOutputCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioOutputCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioOutputCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioOutputCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioOutputCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioOutputCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAudioOutput : public QAudioOutput {
public:
  using QAudioOutput::QAudioOutput;
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
      CuteQAudioOutputCall0 call = reinterpret_cast<CuteQAudioOutputCall0>(taken[0]);
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
      CuteQAudioOutputCall1 call = reinterpret_cast<CuteQAudioOutputCall1>(taken[1]);
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
      CuteQAudioOutputCall2 call = reinterpret_cast<CuteQAudioOutputCall2>(taken[2]);
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
      CuteQAudioOutputCall3 call = reinterpret_cast<CuteQAudioOutputCall3>(taken[3]);
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
      CuteQAudioOutputCall4 call = reinterpret_cast<CuteQAudioOutputCall4>(taken[4]);
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
      CuteQAudioOutputCall5 call = reinterpret_cast<CuteQAudioOutputCall5>(taken[5]);
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
      CuteQAudioOutputCall6 call = reinterpret_cast<CuteQAudioOutputCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAudioOutput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QAudioOutput10metaObjectEv(
    const QAudioOutput *self) {
  return self->metaObject();
}

//  void *QAudioOutput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QAudioOutput11qt_metacastEPKc(
    QAudioOutput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAudioOutput::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QAudioOutput11qt_metacallEN11QMetaObject4CallEiPPv(
    QAudioOutput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAudioOutput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QAudioOutput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAudioOutput::tr(s, c, n));
}

//  QAudioOutput::QAudioOutput(QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioOutput *ritual_ZN12QAudioOutputC1EP7QObject(QObject *parent) {
  return new CuteQAudioOutput(parent);
}

//  QAudioOutput::QAudioOutput(const QAudioDevice &device, QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioOutput *ritual_ZN12QAudioOutputC1ERK12QAudioDeviceP7QObject(
    const QAudioDevice *device,
    QObject *parent) {
  return new CuteQAudioOutput(*device, parent);
}

//  QAudioOutput::~QAudioOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioOutputD1Ev(QAudioOutput *self) {
  delete self;
}

//  QAudioDevice QAudioOutput::device() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK12QAudioOutput6deviceEv(const QAudioOutput *self) {
  return new QAudioDevice(self->device());
}

//  float QAudioOutput::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QAudioOutput6volumeEv(const QAudioOutput *self) {
  return self->volume();
}

//  bool QAudioOutput::isMuted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioOutput7isMutedEv(const QAudioOutput *self) {
  return self->isMuted();
}

//  void QAudioOutput::setDevice(const QAudioDevice &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioOutput9setDeviceERK12QAudioDevice(
    QAudioOutput *self,
    const QAudioDevice *device) {
  self->setDevice(*device);
}

//  void QAudioOutput::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioOutput9setVolumeEf(QAudioOutput *self, float volume) {
  self->setVolume(volume);
}

//  void QAudioOutput::setMuted(bool muted)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioOutput8setMutedEb(QAudioOutput *self, bool muted) {
  self->setMuted(muted);
}

//  void QAudioOutput::deviceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioOutput13deviceChangedEv(QAudioOutput *self) {
  self->deviceChanged();
}

//  void QAudioOutput::volumeChanged(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioOutput13volumeChangedEf(
    QAudioOutput *self,
    float volume) {
  self->volumeChanged(volume);
}

//  void QAudioOutput::mutedChanged(bool muted)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioOutput12mutedChangedEb(
    QAudioOutput *self,
    bool muted) {
  self->mutedChanged(muted);
}

//  QPlatformAudioOutput *QAudioOutput::handle() const
extern "C" Q_DECL_EXPORT
QPlatformAudioOutput *ritual_ZNK12QAudioOutput6handleEv(
    const QAudioOutput *self) {
  return self->handle();
}

//  void QAudioOutput::setDisconnectFunction(std::function<void ()>
//      disconnectFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioOutput21setDisconnectFunctionESt8functionIFvvEE(
    QAudioOutput *self,
    const std::function<void ()> *disconnectFunction) {
  self->setDisconnectFunction(*disconnectFunction);
}

//  a Python function taken by a CuteQAudioOutput, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioOutput(
    QAudioOutput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAudioOutput *>(self)->take(key, call);
}

//  void QAudioOutput::setDisconnectFunction(std::function<void ()>
//      disconnectFunction)
extern "C" Q_DECL_EXPORT
void ritual_callback_ZN12QAudioOutput21setDisconnectFunctionESt8functionIFvvEE(
    QAudioOutput *self,
    void *call,
    void *context) {
  auto function = reinterpret_cast<void (*)(void *)>(call);
  self->setDisconnectFunction([function, context]() {
    function(context);
  });
}
