//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qvideoframeinput.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qvideoframeinput.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qvideoframeformat.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QVideoFrameInput that Python can take functions over in. Every QVideoFrameInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVideoFrameInputCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVideoFrameInputCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoFrameInputCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoFrameInputCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoFrameInputCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoFrameInputCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoFrameInputCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVideoFrameInput : public QVideoFrameInput {
public:
  using QVideoFrameInput::QVideoFrameInput;
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
      CuteQVideoFrameInputCall0 call = reinterpret_cast<CuteQVideoFrameInputCall0>(taken[0]);
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
      CuteQVideoFrameInputCall1 call = reinterpret_cast<CuteQVideoFrameInputCall1>(taken[1]);
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
      CuteQVideoFrameInputCall2 call = reinterpret_cast<CuteQVideoFrameInputCall2>(taken[2]);
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
      CuteQVideoFrameInputCall3 call = reinterpret_cast<CuteQVideoFrameInputCall3>(taken[3]);
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
      CuteQVideoFrameInputCall4 call = reinterpret_cast<CuteQVideoFrameInputCall4>(taken[4]);
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
      CuteQVideoFrameInputCall5 call = reinterpret_cast<CuteQVideoFrameInputCall5>(taken[5]);
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
      CuteQVideoFrameInputCall6 call = reinterpret_cast<CuteQVideoFrameInputCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVideoFrameInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QVideoFrameInput10metaObjectEv(
    const QVideoFrameInput *self) {
  return self->metaObject();
}

//  QString QVideoFrameInput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QVideoFrameInput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVideoFrameInput::tr(s, c, n));
}

//  QVideoFrameInput::QVideoFrameInput(QObject *parent)
extern "C" Q_DECL_EXPORT
QVideoFrameInput *ritual_ZN16QVideoFrameInputC1EP7QObject(QObject *parent) {
  return new CuteQVideoFrameInput(parent);
}

//  QVideoFrameInput::QVideoFrameInput(const QVideoFrameFormat &format,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QVideoFrameInput *ritual_ZN16QVideoFrameInputC1ERK17QVideoFrameFormatP7QObject(
    const QVideoFrameFormat *format,
    QObject *parent) {
  return new CuteQVideoFrameInput(*format, parent);
}

//  QVideoFrameInput::~QVideoFrameInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVideoFrameInputD1Ev(QVideoFrameInput *self) {
  delete self;
}

//  bool QVideoFrameInput::sendVideoFrame(const QVideoFrame &frame)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QVideoFrameInput14sendVideoFrameERK11QVideoFrame(
    QVideoFrameInput *self,
    const QVideoFrame *frame) {
  return self->sendVideoFrame(*frame);
}

//  QVideoFrameFormat QVideoFrameInput::format() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZNK16QVideoFrameInput6formatEv(
    const QVideoFrameInput *self) {
  return new QVideoFrameFormat(self->format());
}

//  QMediaCaptureSession *QVideoFrameInput::captureSession() const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK16QVideoFrameInput14captureSessionEv(
    const QVideoFrameInput *self) {
  return self->captureSession();
}

//  void QVideoFrameInput::setCaptureSession(QMediaCaptureSession
//      *captureSession)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVideoFrameInput17setCaptureSessionEP20QMediaCaptureSession(
    QVideoFrameInput *self,
    QMediaCaptureSession *captureSession) {
  self->setCaptureSession(captureSession);
}

//  QPlatformVideoFrameInput *QVideoFrameInput::platformVideoFrameInput()
//      const
extern "C" Q_DECL_EXPORT
QPlatformVideoFrameInput *ritual_ZNK16QVideoFrameInput23platformVideoFrameInputEv(
    const QVideoFrameInput *self) {
  return self->platformVideoFrameInput();
}

//  a Python function taken by a CuteQVideoFrameInput, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVideoFrameInput(
    QVideoFrameInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVideoFrameInput *>(self)->take(key, call);
}
