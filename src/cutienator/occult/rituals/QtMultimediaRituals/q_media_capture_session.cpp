//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qmediacapturesession.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtMultimedia/qmediacapturesession.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QMediaCaptureSession that Python can take functions over in. Every QMediaCaptureSession
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMediaCaptureSessionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMediaCaptureSessionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaCaptureSessionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaCaptureSessionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaCaptureSessionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaCaptureSessionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaCaptureSessionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMediaCaptureSession : public QMediaCaptureSession {
public:
  using QMediaCaptureSession::QMediaCaptureSession;
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
      CuteQMediaCaptureSessionCall0 call = reinterpret_cast<CuteQMediaCaptureSessionCall0>(taken[0]);
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
      CuteQMediaCaptureSessionCall1 call = reinterpret_cast<CuteQMediaCaptureSessionCall1>(taken[1]);
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
      CuteQMediaCaptureSessionCall2 call = reinterpret_cast<CuteQMediaCaptureSessionCall2>(taken[2]);
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
      CuteQMediaCaptureSessionCall3 call = reinterpret_cast<CuteQMediaCaptureSessionCall3>(taken[3]);
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
      CuteQMediaCaptureSessionCall4 call = reinterpret_cast<CuteQMediaCaptureSessionCall4>(taken[4]);
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
      CuteQMediaCaptureSessionCall5 call = reinterpret_cast<CuteQMediaCaptureSessionCall5>(taken[5]);
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
      CuteQMediaCaptureSessionCall6 call = reinterpret_cast<CuteQMediaCaptureSessionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMediaCaptureSession::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QMediaCaptureSession10metaObjectEv(
    const QMediaCaptureSession *self) {
  return self->metaObject();
}

//  void *QMediaCaptureSession::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QMediaCaptureSession11qt_metacastEPKc(
    QMediaCaptureSession *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QMediaCaptureSession::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QMediaCaptureSession11qt_metacallEN11QMetaObject4CallEiPPv(
    QMediaCaptureSession *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QMediaCaptureSession::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QMediaCaptureSession2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMediaCaptureSession::tr(s, c, n));
}

//  QMediaCaptureSession::QMediaCaptureSession(QObject *parent)
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZN20QMediaCaptureSessionC1EP7QObject(
    QObject *parent) {
  return new CuteQMediaCaptureSession(parent);
}

//  QMediaCaptureSession::~QMediaCaptureSession()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSessionD1Ev(QMediaCaptureSession *self) {
  delete self;
}

//  QAudioInput *QMediaCaptureSession::audioInput() const
extern "C" Q_DECL_EXPORT
QAudioInput *ritual_ZNK20QMediaCaptureSession10audioInputEv(
    const QMediaCaptureSession *self) {
  return self->audioInput();
}

//  void QMediaCaptureSession::setAudioInput(QAudioInput *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession13setAudioInputEP11QAudioInput(
    QMediaCaptureSession *self,
    QAudioInput *input) {
  self->setAudioInput(input);
}

//  QAudioBufferInput *QMediaCaptureSession::audioBufferInput() const
extern "C" Q_DECL_EXPORT
QAudioBufferInput *ritual_ZNK20QMediaCaptureSession16audioBufferInputEv(
    const QMediaCaptureSession *self) {
  return self->audioBufferInput();
}

//  void QMediaCaptureSession::setAudioBufferInput(QAudioBufferInput *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession19setAudioBufferInputEP17QAudioBufferInput(
    QMediaCaptureSession *self,
    QAudioBufferInput *input) {
  self->setAudioBufferInput(input);
}

//  QCamera *QMediaCaptureSession::camera() const
extern "C" Q_DECL_EXPORT
QCamera *ritual_ZNK20QMediaCaptureSession6cameraEv(
    const QMediaCaptureSession *self) {
  return self->camera();
}

//  void QMediaCaptureSession::setCamera(QCamera *camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession9setCameraEP7QCamera(
    QMediaCaptureSession *self,
    QCamera *camera) {
  self->setCamera(camera);
}

//  QObject *QMediaCaptureSession::nativeVideoSource() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QMediaCaptureSession17nativeVideoSourceEv(
    const QMediaCaptureSession *self) {
  return self->nativeVideoSource();
}

//  void QMediaCaptureSession::setNativeVideoSource(QObject *videoSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession20setNativeVideoSourceEP7QObject(
    QMediaCaptureSession *self,
    QObject *videoSource) {
  self->setNativeVideoSource(videoSource);
}

//  QImageCapture *QMediaCaptureSession::imageCapture()
extern "C" Q_DECL_EXPORT
QImageCapture *ritual_ZN20QMediaCaptureSession12imageCaptureEv(
    QMediaCaptureSession *self) {
  return self->imageCapture();
}

//  void QMediaCaptureSession::setImageCapture(QImageCapture *imageCapture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession15setImageCaptureEP13QImageCapture(
    QMediaCaptureSession *self,
    QImageCapture *imageCapture) {
  self->setImageCapture(imageCapture);
}

//  QScreenCapture *QMediaCaptureSession::screenCapture()
extern "C" Q_DECL_EXPORT
QScreenCapture *ritual_ZN20QMediaCaptureSession13screenCaptureEv(
    QMediaCaptureSession *self) {
  return self->screenCapture();
}

//  void QMediaCaptureSession::setScreenCapture(QScreenCapture
//      *screenCapture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession16setScreenCaptureEP14QScreenCapture(
    QMediaCaptureSession *self,
    QScreenCapture *screenCapture) {
  self->setScreenCapture(screenCapture);
}

//  QWindowCapture *QMediaCaptureSession::windowCapture()
extern "C" Q_DECL_EXPORT
QWindowCapture *ritual_ZN20QMediaCaptureSession13windowCaptureEv(
    QMediaCaptureSession *self) {
  return self->windowCapture();
}

//  void QMediaCaptureSession::setWindowCapture(QWindowCapture
//      *windowCapture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession16setWindowCaptureEP14QWindowCapture(
    QMediaCaptureSession *self,
    QWindowCapture *windowCapture) {
  self->setWindowCapture(windowCapture);
}

//  QVideoFrameInput *QMediaCaptureSession::videoFrameInput() const
extern "C" Q_DECL_EXPORT
QVideoFrameInput *ritual_ZNK20QMediaCaptureSession15videoFrameInputEv(
    const QMediaCaptureSession *self) {
  return self->videoFrameInput();
}

//  void QMediaCaptureSession::setVideoFrameInput(QVideoFrameInput *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession18setVideoFrameInputEP16QVideoFrameInput(
    QMediaCaptureSession *self,
    QVideoFrameInput *input) {
  self->setVideoFrameInput(input);
}

//  QMediaRecorder *QMediaCaptureSession::recorder()
extern "C" Q_DECL_EXPORT
QMediaRecorder *ritual_ZN20QMediaCaptureSession8recorderEv(
    QMediaCaptureSession *self) {
  return self->recorder();
}

//  void QMediaCaptureSession::setRecorder(QMediaRecorder *recorder)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession11setRecorderEP14QMediaRecorder(
    QMediaCaptureSession *self,
    QMediaRecorder *recorder) {
  self->setRecorder(recorder);
}

//  void QMediaCaptureSession::setVideoOutput(QObject *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession14setVideoOutputEP7QObject(
    QMediaCaptureSession *self,
    QObject *output) {
  self->setVideoOutput(output);
}

//  QObject *QMediaCaptureSession::videoOutput() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QMediaCaptureSession11videoOutputEv(
    const QMediaCaptureSession *self) {
  return self->videoOutput();
}

//  void QMediaCaptureSession::setVideoSink(QVideoSink *sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession12setVideoSinkEP10QVideoSink(
    QMediaCaptureSession *self,
    QVideoSink *sink) {
  self->setVideoSink(sink);
}

//  QVideoSink *QMediaCaptureSession::videoSink() const
extern "C" Q_DECL_EXPORT
QVideoSink *ritual_ZNK20QMediaCaptureSession9videoSinkEv(
    const QMediaCaptureSession *self) {
  return self->videoSink();
}

//  void QMediaCaptureSession::setAudioOutput(QAudioOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession14setAudioOutputEP12QAudioOutput(
    QMediaCaptureSession *self,
    QAudioOutput *output) {
  self->setAudioOutput(output);
}

//  QAudioOutput *QMediaCaptureSession::audioOutput() const
extern "C" Q_DECL_EXPORT
QAudioOutput *ritual_ZNK20QMediaCaptureSession11audioOutputEv(
    const QMediaCaptureSession *self) {
  return self->audioOutput();
}

//  QPlatformMediaCaptureSession *QMediaCaptureSession::platformSession()
//      const
extern "C" Q_DECL_EXPORT
QPlatformMediaCaptureSession *ritual_ZNK20QMediaCaptureSession15platformSessionEv(
    const QMediaCaptureSession *self) {
  return self->platformSession();
}

//  void QMediaCaptureSession::audioInputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession17audioInputChangedEv(
    QMediaCaptureSession *self) {
  self->audioInputChanged();
}

//  void QMediaCaptureSession::audioBufferInputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession23audioBufferInputChangedEv(
    QMediaCaptureSession *self) {
  self->audioBufferInputChanged();
}

//  void QMediaCaptureSession::cameraChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession13cameraChangedEv(
    QMediaCaptureSession *self) {
  self->cameraChanged();
}

//  void QMediaCaptureSession::nativeVideoSourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession24nativeVideoSourceChangedEv(
    QMediaCaptureSession *self) {
  self->nativeVideoSourceChanged();
}

//  void QMediaCaptureSession::screenCaptureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession20screenCaptureChangedEv(
    QMediaCaptureSession *self) {
  self->screenCaptureChanged();
}

//  void QMediaCaptureSession::windowCaptureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession20windowCaptureChangedEv(
    QMediaCaptureSession *self) {
  self->windowCaptureChanged();
}

//  void QMediaCaptureSession::videoFrameInputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession22videoFrameInputChangedEv(
    QMediaCaptureSession *self) {
  self->videoFrameInputChanged();
}

//  void QMediaCaptureSession::imageCaptureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession19imageCaptureChangedEv(
    QMediaCaptureSession *self) {
  self->imageCaptureChanged();
}

//  void QMediaCaptureSession::recorderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession15recorderChangedEv(
    QMediaCaptureSession *self) {
  self->recorderChanged();
}

//  void QMediaCaptureSession::videoOutputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession18videoOutputChangedEv(
    QMediaCaptureSession *self) {
  self->videoOutputChanged();
}

//  void QMediaCaptureSession::audioOutputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMediaCaptureSession18audioOutputChangedEv(
    QMediaCaptureSession *self) {
  self->audioOutputChanged();
}

//  QMediaCaptureSessionPrivate *QMediaCaptureSession::d_func()
extern "C" Q_DECL_EXPORT
QMediaCaptureSessionPrivate *ritual_ZN20QMediaCaptureSession6d_funcEv(
    QMediaCaptureSession *self) {
  return self->d_func();
}

//  const QMediaCaptureSessionPrivate *QMediaCaptureSession::d_func() const
extern "C" Q_DECL_EXPORT
const QMediaCaptureSessionPrivate *ritual_ZNK20QMediaCaptureSession6d_funcEv(
    const QMediaCaptureSession *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQMediaCaptureSession, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMediaCaptureSession(
    QMediaCaptureSession *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMediaCaptureSession *>(self)->take(key, call);
}
