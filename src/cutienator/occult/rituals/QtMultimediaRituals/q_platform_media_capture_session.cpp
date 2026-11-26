//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediacapture_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediacapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <vector>

//  A QPlatformMediaCaptureSession that Python can take functions over in. Every QPlatformMediaCaptureSession
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformMediaCaptureSessionCall0)(const void *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall1)(const void *, QPlatformCamera *, int *);
typedef void * (*CuteQPlatformMediaCaptureSessionCall2)(const void *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall3)(const void *, QPlatformSurfaceCapture *, int *);
typedef void * (*CuteQPlatformMediaCaptureSessionCall4)(const void *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall5)(const void *, QPlatformSurfaceCapture *, int *);
typedef void * (*CuteQPlatformMediaCaptureSessionCall6)(const void *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall7)(const void *, QPlatformVideoFrameInput *, int *);
typedef void * (*CuteQPlatformMediaCaptureSessionCall8)(const void *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall9)(const void *, QPlatformImageCapture *, int *);
typedef void * (*CuteQPlatformMediaCaptureSessionCall10)(const void *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall11)(const void *, QPlatformMediaRecorder *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall12)(const void *, QPlatformAudioInput *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall13)(const void *, QPlatformAudioBufferInput *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall14)(const void *, QVideoSink *, int *);
typedef void (*CuteQPlatformMediaCaptureSessionCall15)(const void *, QPlatformAudioOutput *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformMediaCaptureSessionCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformMediaCaptureSessionCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaCaptureSessionCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaCaptureSessionCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaCaptureSessionCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaCaptureSessionCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaCaptureSessionCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformMediaCaptureSession : public QPlatformMediaCaptureSession {
public:
  using QPlatformMediaCaptureSession::QPlatformMediaCaptureSession;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession6cameraEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession9setCameraEP15QPlatformCamera")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession13screenCaptureEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession16setScreenCaptureEP23QPlatformSurfaceCapture")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession13windowCaptureEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession16setWindowCaptureEP23QPlatformSurfaceCapture")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession15videoFrameInputEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession18setVideoFrameInputEP24QPlatformVideoFrameInput")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession12imageCaptureEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession15setImageCaptureEP21QPlatformImageCapture")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession13mediaRecorderEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession16setMediaRecorderEP22QPlatformMediaRecorder")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession13setAudioInputEP19QPlatformAudioInput")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession19setAudioBufferInputEP25QPlatformAudioBufferInput")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession15setVideoPreviewEP10QVideoSink")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformMediaCaptureSession14setAudioOutputEP20QPlatformAudioOutput")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QPlatformCamera *QPlatformMediaCaptureSession::camera()
  QPlatformCamera *camera() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall0 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformCamera *>(given);
    }
    return {};
  }

  //  void QPlatformMediaCaptureSession::setCamera(QPlatformCamera *a0)
  void setCamera(QPlatformCamera *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall1 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaCaptureSession::setCamera(a0);
  }

  //  QPlatformSurfaceCapture
  //      *QPlatformMediaCaptureSession::screenCapture()
  QPlatformSurfaceCapture *screenCapture() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall2 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurfaceCapture *>(given);
    }
    return QPlatformMediaCaptureSession::screenCapture();
  }

  //  void QPlatformMediaCaptureSession::setScreenCapture(QPlatformSurfaceC
  //      apture *a0)
  void setScreenCapture(QPlatformSurfaceCapture *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall3 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaCaptureSession::setScreenCapture(a0);
  }

  //  QPlatformSurfaceCapture
  //      *QPlatformMediaCaptureSession::windowCapture()
  QPlatformSurfaceCapture *windowCapture() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall4 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurfaceCapture *>(given);
    }
    return QPlatformMediaCaptureSession::windowCapture();
  }

  //  void QPlatformMediaCaptureSession::setWindowCapture(QPlatformSurfaceC
  //      apture *a0)
  void setWindowCapture(QPlatformSurfaceCapture *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall5 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaCaptureSession::setWindowCapture(a0);
  }

  //  QPlatformVideoFrameInput
  //      *QPlatformMediaCaptureSession::videoFrameInput()
  QPlatformVideoFrameInput *videoFrameInput() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall6 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformVideoFrameInput *>(given);
    }
    return QPlatformMediaCaptureSession::videoFrameInput();
  }

  //  void QPlatformMediaCaptureSession::setVideoFrameInput(QPlatformVideoF
  //      rameInput *a0)
  void setVideoFrameInput(QPlatformVideoFrameInput *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall7 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaCaptureSession::setVideoFrameInput(a0);
  }

  //  QPlatformImageCapture *QPlatformMediaCaptureSession::imageCapture()
  QPlatformImageCapture *imageCapture() override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall8 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformImageCapture *>(given);
    }
    return {};
  }

  //  void
  //      QPlatformMediaCaptureSession::setImageCapture(QPlatformImageCaptu
  //      re *a0)
  void setImageCapture(QPlatformImageCapture *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall9 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaCaptureSession::setImageCapture(a0);
  }

  //  QPlatformMediaRecorder *QPlatformMediaCaptureSession::mediaRecorder()
  QPlatformMediaRecorder *mediaRecorder() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall10 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMediaRecorder *>(given);
    }
    return {};
  }

  //  void
  //      QPlatformMediaCaptureSession::setMediaRecorder(QPlatformMediaReco
  //      rder *a0)
  void setMediaRecorder(QPlatformMediaRecorder *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall11 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaCaptureSession::setMediaRecorder(a0);
  }

  //  void QPlatformMediaCaptureSession::setAudioInput(QPlatformAudioInput
  //      *input)
  void setAudioInput(QPlatformAudioInput *input) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall12 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall12>(taken[12]);
      call(this, input, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformMediaCaptureSession::setAudioBufferInput(QPlatformAudio
  //      BufferInput *a0)
  void setAudioBufferInput(QPlatformAudioBufferInput *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall13 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaCaptureSession::setAudioBufferInput(a0);
  }

  //  void QPlatformMediaCaptureSession::setVideoPreview(QVideoSink *a0)
  void setVideoPreview(QVideoSink *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall14 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaCaptureSession::setVideoPreview(a0);
  }

  //  void
  //      QPlatformMediaCaptureSession::setAudioOutput(QPlatformAudioOutput
  //      *a0)
  void setAudioOutput(QPlatformAudioOutput *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall15 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaCaptureSession::setAudioOutput(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall16 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall17 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall18 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall19 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall20 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall21 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPlatformMediaCaptureSessionCall22 call = reinterpret_cast<CuteQPlatformMediaCaptureSessionCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformMediaCaptureSession::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QPlatformMediaCaptureSession10metaObjectEv(
    const QPlatformMediaCaptureSession *self) {
  return self->metaObject();
}

//  void *QPlatformMediaCaptureSession::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QPlatformMediaCaptureSession11qt_metacastEPKc(
    QPlatformMediaCaptureSession *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformMediaCaptureSession::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QPlatformMediaCaptureSession11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformMediaCaptureSession *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformMediaCaptureSession::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QPlatformMediaCaptureSession2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformMediaCaptureSession::tr(s, c, n));
}

//  QPlatformMediaCaptureSession::QPlatformMediaCaptureSession()
extern "C" Q_DECL_EXPORT
QPlatformMediaCaptureSession *ritual_ZN28QPlatformMediaCaptureSessionC1Ev() {
  return new CuteQPlatformMediaCaptureSession();
}

//  QPlatformMediaCaptureSession::~QPlatformMediaCaptureSession()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSessionD1Ev(
    QPlatformMediaCaptureSession *self) {
  delete self;
}

//  void QPlatformMediaCaptureSession::setCaptureSession(QMediaCaptureSession
//      *session)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession17setCaptureSessionEP20QMediaCaptureSession(
    QPlatformMediaCaptureSession *self,
    QMediaCaptureSession *session) {
  self->setCaptureSession(session);
}

//  QMediaCaptureSession *QPlatformMediaCaptureSession::captureSession()
//      const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK28QPlatformMediaCaptureSession14captureSessionEv(
    const QPlatformMediaCaptureSession *self) {
  return self->captureSession();
}

//  QPlatformCamera *QPlatformMediaCaptureSession::camera()
extern "C" Q_DECL_EXPORT
QPlatformCamera *ritual_ZN28QPlatformMediaCaptureSession6cameraEv(
    QPlatformMediaCaptureSession *self) {
  return self->camera();
}

//  void QPlatformMediaCaptureSession::setCamera(QPlatformCamera *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession9setCameraEP15QPlatformCamera(
    QPlatformMediaCaptureSession *self,
    QPlatformCamera *a0) {
  self->setCamera(a0);
}

//  QPlatformSurfaceCapture *QPlatformMediaCaptureSession::screenCapture()
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_ZN28QPlatformMediaCaptureSession13screenCaptureEv(
    QPlatformMediaCaptureSession *self) {
  return self->screenCapture();
}

//  void
//      QPlatformMediaCaptureSession::setScreenCapture(QPlatformSurfaceCaptur
//      e *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession16setScreenCaptureEP23QPlatformSurfaceCapture(
    QPlatformMediaCaptureSession *self,
    QPlatformSurfaceCapture *a0) {
  self->setScreenCapture(a0);
}

//  QPlatformSurfaceCapture *QPlatformMediaCaptureSession::windowCapture()
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_ZN28QPlatformMediaCaptureSession13windowCaptureEv(
    QPlatformMediaCaptureSession *self) {
  return self->windowCapture();
}

//  void
//      QPlatformMediaCaptureSession::setWindowCapture(QPlatformSurfaceCaptur
//      e *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession16setWindowCaptureEP23QPlatformSurfaceCapture(
    QPlatformMediaCaptureSession *self,
    QPlatformSurfaceCapture *a0) {
  self->setWindowCapture(a0);
}

//  QPlatformVideoFrameInput *QPlatformMediaCaptureSession::videoFrameInput()
extern "C" Q_DECL_EXPORT
QPlatformVideoFrameInput *ritual_ZN28QPlatformMediaCaptureSession15videoFrameInputEv(
    QPlatformMediaCaptureSession *self) {
  return self->videoFrameInput();
}

//  void
//      QPlatformMediaCaptureSession::setVideoFrameInput(QPlatformVideoFrameI
//      nput *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession18setVideoFrameInputEP24QPlatformVideoFrameInput(
    QPlatformMediaCaptureSession *self,
    QPlatformVideoFrameInput *a0) {
  self->setVideoFrameInput(a0);
}

//  QPlatformImageCapture *QPlatformMediaCaptureSession::imageCapture()
extern "C" Q_DECL_EXPORT
QPlatformImageCapture *ritual_ZN28QPlatformMediaCaptureSession12imageCaptureEv(
    QPlatformMediaCaptureSession *self) {
  return self->imageCapture();
}

//  void QPlatformMediaCaptureSession::setImageCapture(QPlatformImageCapture
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession15setImageCaptureEP21QPlatformImageCapture(
    QPlatformMediaCaptureSession *self,
    QPlatformImageCapture *a0) {
  self->setImageCapture(a0);
}

//  QPlatformMediaRecorder *QPlatformMediaCaptureSession::mediaRecorder()
extern "C" Q_DECL_EXPORT
QPlatformMediaRecorder *ritual_ZN28QPlatformMediaCaptureSession13mediaRecorderEv(
    QPlatformMediaCaptureSession *self) {
  return self->mediaRecorder();
}

//  void
//      QPlatformMediaCaptureSession::setMediaRecorder(QPlatformMediaRecorder
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession16setMediaRecorderEP22QPlatformMediaRecorder(
    QPlatformMediaCaptureSession *self,
    QPlatformMediaRecorder *a0) {
  self->setMediaRecorder(a0);
}

//  void QPlatformMediaCaptureSession::setAudioInput(QPlatformAudioInput
//      *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession13setAudioInputEP19QPlatformAudioInput(
    QPlatformMediaCaptureSession *self,
    QPlatformAudioInput *input) {
  self->setAudioInput(input);
}

//  void QPlatformMediaCaptureSession::setAudioBufferInput(QPlatformAudioBuff
//      erInput *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession19setAudioBufferInputEP25QPlatformAudioBufferInput(
    QPlatformMediaCaptureSession *self,
    QPlatformAudioBufferInput *a0) {
  self->setAudioBufferInput(a0);
}

//  void QPlatformMediaCaptureSession::setVideoPreview(QVideoSink *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession15setVideoPreviewEP10QVideoSink(
    QPlatformMediaCaptureSession *self,
    QVideoSink *a0) {
  self->setVideoPreview(a0);
}

//  void QPlatformMediaCaptureSession::setAudioOutput(QPlatformAudioOutput
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession14setAudioOutputEP20QPlatformAudioOutput(
    QPlatformMediaCaptureSession *self,
    QPlatformAudioOutput *a0) {
  self->setAudioOutput(a0);
}

//  std::vector<QPlatformVideoSource *>
//      QPlatformMediaCaptureSession::activeVideoSources()
extern "C" Q_DECL_EXPORT
std::vector<QPlatformVideoSource *> *ritual_ZN28QPlatformMediaCaptureSession18activeVideoSourcesEv(
    QPlatformMediaCaptureSession *self) {
  return new std::vector<QPlatformVideoSource *>(self->activeVideoSources());
}

//  void QPlatformMediaCaptureSession::cameraChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession13cameraChangedEv(
    QPlatformMediaCaptureSession *self) {
  self->cameraChanged();
}

//  void QPlatformMediaCaptureSession::screenCaptureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession20screenCaptureChangedEv(
    QPlatformMediaCaptureSession *self) {
  self->screenCaptureChanged();
}

//  void QPlatformMediaCaptureSession::windowCaptureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession20windowCaptureChangedEv(
    QPlatformMediaCaptureSession *self) {
  self->windowCaptureChanged();
}

//  void QPlatformMediaCaptureSession::videoFrameInputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession22videoFrameInputChangedEv(
    QPlatformMediaCaptureSession *self) {
  self->videoFrameInputChanged();
}

//  void QPlatformMediaCaptureSession::imageCaptureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession19imageCaptureChangedEv(
    QPlatformMediaCaptureSession *self) {
  self->imageCaptureChanged();
}

//  void QPlatformMediaCaptureSession::encoderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMediaCaptureSession14encoderChangedEv(
    QPlatformMediaCaptureSession *self) {
  self->encoderChanged();
}

//  a Python function taken by a CuteQPlatformMediaCaptureSession, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformMediaCaptureSession(
    QPlatformMediaCaptureSession *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformMediaCaptureSession *>(self)->take(key, call);
}

//  void QPlatformMediaCaptureSession::setCamera(QPlatformCamera *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QPlatformMediaCaptureSession9setCameraEP15QPlatformCamera(
    QPlatformMediaCaptureSession *self,
    QPlatformCamera *a0) {
  self->QPlatformMediaCaptureSession::setCamera(a0);
}

//  QPlatformSurfaceCapture *QPlatformMediaCaptureSession::screenCapture()
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_own_ZN28QPlatformMediaCaptureSession13screenCaptureEv(
    QPlatformMediaCaptureSession *self) {
  return self->QPlatformMediaCaptureSession::screenCapture();
}

//  void
//      QPlatformMediaCaptureSession::setScreenCapture(QPlatformSurfaceCaptur
//      e *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QPlatformMediaCaptureSession16setScreenCaptureEP23QPlatformSurfaceCapture(
    QPlatformMediaCaptureSession *self,
    QPlatformSurfaceCapture *a0) {
  self->QPlatformMediaCaptureSession::setScreenCapture(a0);
}

//  QPlatformSurfaceCapture *QPlatformMediaCaptureSession::windowCapture()
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_own_ZN28QPlatformMediaCaptureSession13windowCaptureEv(
    QPlatformMediaCaptureSession *self) {
  return self->QPlatformMediaCaptureSession::windowCapture();
}

//  void
//      QPlatformMediaCaptureSession::setWindowCapture(QPlatformSurfaceCaptur
//      e *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QPlatformMediaCaptureSession16setWindowCaptureEP23QPlatformSurfaceCapture(
    QPlatformMediaCaptureSession *self,
    QPlatformSurfaceCapture *a0) {
  self->QPlatformMediaCaptureSession::setWindowCapture(a0);
}

//  QPlatformVideoFrameInput *QPlatformMediaCaptureSession::videoFrameInput()
extern "C" Q_DECL_EXPORT
QPlatformVideoFrameInput *ritual_own_ZN28QPlatformMediaCaptureSession15videoFrameInputEv(
    QPlatformMediaCaptureSession *self) {
  return self->QPlatformMediaCaptureSession::videoFrameInput();
}

//  void
//      QPlatformMediaCaptureSession::setVideoFrameInput(QPlatformVideoFrameI
//      nput *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QPlatformMediaCaptureSession18setVideoFrameInputEP24QPlatformVideoFrameInput(
    QPlatformMediaCaptureSession *self,
    QPlatformVideoFrameInput *a0) {
  self->QPlatformMediaCaptureSession::setVideoFrameInput(a0);
}

//  void QPlatformMediaCaptureSession::setImageCapture(QPlatformImageCapture
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QPlatformMediaCaptureSession15setImageCaptureEP21QPlatformImageCapture(
    QPlatformMediaCaptureSession *self,
    QPlatformImageCapture *a0) {
  self->QPlatformMediaCaptureSession::setImageCapture(a0);
}

//  void
//      QPlatformMediaCaptureSession::setMediaRecorder(QPlatformMediaRecorder
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QPlatformMediaCaptureSession16setMediaRecorderEP22QPlatformMediaRecorder(
    QPlatformMediaCaptureSession *self,
    QPlatformMediaRecorder *a0) {
  self->QPlatformMediaCaptureSession::setMediaRecorder(a0);
}

//  void QPlatformMediaCaptureSession::setAudioBufferInput(QPlatformAudioBuff
//      erInput *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QPlatformMediaCaptureSession19setAudioBufferInputEP25QPlatformAudioBufferInput(
    QPlatformMediaCaptureSession *self,
    QPlatformAudioBufferInput *a0) {
  self->QPlatformMediaCaptureSession::setAudioBufferInput(a0);
}

//  void QPlatformMediaCaptureSession::setVideoPreview(QVideoSink *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QPlatformMediaCaptureSession15setVideoPreviewEP10QVideoSink(
    QPlatformMediaCaptureSession *self,
    QVideoSink *a0) {
  self->QPlatformMediaCaptureSession::setVideoPreview(a0);
}

//  void QPlatformMediaCaptureSession::setAudioOutput(QPlatformAudioOutput
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QPlatformMediaCaptureSession14setAudioOutputEP20QPlatformAudioOutput(
    QPlatformMediaCaptureSession *self,
    QPlatformAudioOutput *a0) {
  self->QPlatformMediaCaptureSession::setAudioOutput(a0);
}

//  a std::vector<QPlatformVideoSource *> a ritual of
//      QPlatformMediaCaptureSession gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaCaptureSession__std_vector_QPlatformVideoSource(
    std::vector<QPlatformVideoSource *> *self) {
  delete self;
}
