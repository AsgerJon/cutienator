//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudiobufferinput.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qaudiobufferinput.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qaudiobuffer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAudioBufferInput that Python can take functions over in. Every QAudioBufferInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioBufferInputCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioBufferInputCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioBufferInputCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioBufferInputCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioBufferInputCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioBufferInputCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioBufferInputCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAudioBufferInput : public QAudioBufferInput {
public:
  using QAudioBufferInput::QAudioBufferInput;
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
      CuteQAudioBufferInputCall0 call = reinterpret_cast<CuteQAudioBufferInputCall0>(taken[0]);
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
      CuteQAudioBufferInputCall1 call = reinterpret_cast<CuteQAudioBufferInputCall1>(taken[1]);
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
      CuteQAudioBufferInputCall2 call = reinterpret_cast<CuteQAudioBufferInputCall2>(taken[2]);
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
      CuteQAudioBufferInputCall3 call = reinterpret_cast<CuteQAudioBufferInputCall3>(taken[3]);
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
      CuteQAudioBufferInputCall4 call = reinterpret_cast<CuteQAudioBufferInputCall4>(taken[4]);
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
      CuteQAudioBufferInputCall5 call = reinterpret_cast<CuteQAudioBufferInputCall5>(taken[5]);
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
      CuteQAudioBufferInputCall6 call = reinterpret_cast<CuteQAudioBufferInputCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAudioBufferInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QAudioBufferInput10metaObjectEv(
    const QAudioBufferInput *self) {
  return self->metaObject();
}

//  void *QAudioBufferInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QAudioBufferInput11qt_metacastEPKc(
    QAudioBufferInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAudioBufferInput::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QAudioBufferInput11qt_metacallEN11QMetaObject4CallEiPPv(
    QAudioBufferInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAudioBufferInput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QAudioBufferInput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAudioBufferInput::tr(s, c, n));
}

//  QAudioBufferInput::QAudioBufferInput(QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioBufferInput *ritual_ZN17QAudioBufferInputC1EP7QObject(
    QObject *parent) {
  return new CuteQAudioBufferInput(parent);
}

//  QAudioBufferInput::QAudioBufferInput(const QAudioFormat &format, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QAudioBufferInput *ritual_ZN17QAudioBufferInputC1ERK12QAudioFormatP7QObject(
    const QAudioFormat *format,
    QObject *parent) {
  return new CuteQAudioBufferInput(*format, parent);
}

//  QAudioBufferInput::~QAudioBufferInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAudioBufferInputD1Ev(QAudioBufferInput *self) {
  delete self;
}

//  bool QAudioBufferInput::sendAudioBuffer(const QAudioBuffer &audioBuffer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAudioBufferInput15sendAudioBufferERK12QAudioBuffer(
    QAudioBufferInput *self,
    const QAudioBuffer *audioBuffer) {
  return self->sendAudioBuffer(*audioBuffer);
}

//  QAudioFormat QAudioBufferInput::format() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK17QAudioBufferInput6formatEv(
    const QAudioBufferInput *self) {
  return new QAudioFormat(self->format());
}

//  QMediaCaptureSession *QAudioBufferInput::captureSession() const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK17QAudioBufferInput14captureSessionEv(
    const QAudioBufferInput *self) {
  return self->captureSession();
}

//  void QAudioBufferInput::readyToSendAudioBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAudioBufferInput22readyToSendAudioBufferEv(
    QAudioBufferInput *self) {
  self->readyToSendAudioBuffer();
}

//  void QAudioBufferInput::setCaptureSession(QMediaCaptureSession
//      *captureSession)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAudioBufferInput17setCaptureSessionEP20QMediaCaptureSession(
    QAudioBufferInput *self,
    QMediaCaptureSession *captureSession) {
  self->setCaptureSession(captureSession);
}

//  QPlatformAudioBufferInput *QAudioBufferInput::platformAudioBufferInput()
//      const
extern "C" Q_DECL_EXPORT
QPlatformAudioBufferInput *ritual_ZNK17QAudioBufferInput24platformAudioBufferInputEv(
    const QAudioBufferInput *self) {
  return self->platformAudioBufferInput();
}

//  QAudioBufferInputPrivate *QAudioBufferInput::d_func()
extern "C" Q_DECL_EXPORT
QAudioBufferInputPrivate *ritual_ZN17QAudioBufferInput6d_funcEv(
    QAudioBufferInput *self) {
  return self->d_func();
}

//  const QAudioBufferInputPrivate *QAudioBufferInput::d_func() const
extern "C" Q_DECL_EXPORT
const QAudioBufferInputPrivate *ritual_ZNK17QAudioBufferInput6d_funcEv(
    const QAudioBufferInput *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAudioBufferInput, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioBufferInput(
    QAudioBufferInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAudioBufferInput *>(self)->take(key, call);
}
