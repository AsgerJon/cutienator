//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaintegration_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudioresampler_p.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qcapturablewindow.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcapturablewindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qvideoframeformat.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QString>
#include <memory>
#include <QtMultimedia/QAudioFormat>
#include <QtMultimedia/QCapturableWindow>

//  Only a class built on QPlatformMediaIntegration may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPlatformMediaIntegration : QPlatformMediaIntegration {
  using QPlatformMediaIntegration::createFormatInfo;
  using QPlatformMediaIntegration::createVideoDevices;
  using QPlatformMediaIntegration::createCapturableWindows;
};

//  A QPlatformMediaIntegration that Python can take functions over in. Every QPlatformMediaIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformMediaIntegrationCall0)(const void *, QScreenCapture *, int *);
typedef void * (*CuteQPlatformMediaIntegrationCall1)(const void *, QWindowCapture *, int *);
typedef bool (*CuteQPlatformMediaIntegrationCall2)(const void *, int *);
typedef void * (*CuteQPlatformMediaIntegrationCall3)(const void *, int *);
typedef void * (*CuteQPlatformMediaIntegrationCall4)(const void *, int *);
typedef void * (*CuteQPlatformMediaIntegrationCall5)(const void *, int *);
typedef void * (*CuteQPlatformMediaIntegrationCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformMediaIntegrationCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformMediaIntegrationCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaIntegrationCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaIntegrationCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaIntegrationCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaIntegrationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaIntegrationCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformMediaIntegration : public QPlatformMediaIntegration {
public:
  using QPlatformMediaIntegration::QPlatformMediaIntegration;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QPlatformMediaIntegration19createScreenCaptureEP14QScreenCapture")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformMediaIntegration19createWindowCaptureEP14QWindowCapture")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QPlatformMediaIntegration41isCameraSwitchingDuringRecordingSupportedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformMediaIntegration18gstreamerInterfaceEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformMediaIntegration16createFormatInfoEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformMediaIntegration18createVideoDevicesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformMediaIntegration23createCapturableWindowsEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QPlatformSurfaceCapture
  //      *QPlatformMediaIntegration::createScreenCapture(QScreenCapture
  //      *a0)
  QPlatformSurfaceCapture *createScreenCapture(QScreenCapture *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall0 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QPlatformSurfaceCapture *>(given);
    }
    return QPlatformMediaIntegration::createScreenCapture(a0);
  }

  //  QPlatformSurfaceCapture
  //      *QPlatformMediaIntegration::createWindowCapture(QWindowCapture
  //      *a0)
  QPlatformSurfaceCapture *createWindowCapture(QWindowCapture *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall1 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall1>(taken[1]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QPlatformSurfaceCapture *>(given);
    }
    return QPlatformMediaIntegration::createWindowCapture(a0);
  }

  //  bool QPlatformMediaIntegration::isCameraSwitchingDuringRecordingSuppo
  //      rted() const
  bool isCameraSwitchingDuringRecordingSupported() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall2 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMediaIntegration::isCameraSwitchingDuringRecordingSupported();
  }

  //  QGStreamerInterface *QPlatformMediaIntegration::gstreamerInterface()
  QGStreamerInterface *gstreamerInterface() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall3 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGStreamerInterface *>(given);
    }
    return QPlatformMediaIntegration::gstreamerInterface();
  }

  //  QPlatformMediaFormatInfo
  //      *QPlatformMediaIntegration::createFormatInfo()
  QPlatformMediaFormatInfo *createFormatInfo() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall4 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMediaFormatInfo *>(given);
    }
    return QPlatformMediaIntegration::createFormatInfo();
  }

  //  QPlatformVideoDevices
  //      *QPlatformMediaIntegration::createVideoDevices()
  QPlatformVideoDevices *createVideoDevices() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall5 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformVideoDevices *>(given);
    }
    return QPlatformMediaIntegration::createVideoDevices();
  }

  //  QPlatformCapturableWindows
  //      *QPlatformMediaIntegration::createCapturableWindows()
  QPlatformCapturableWindows *createCapturableWindows() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall6 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformCapturableWindows *>(given);
    }
    return QPlatformMediaIntegration::createCapturableWindows();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall7 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall8 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall9 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall10 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall11 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall12 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformMediaIntegrationCall13 call = reinterpret_cast<CuteQPlatformMediaIntegrationCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformMediaIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QPlatformMediaIntegration10metaObjectEv(
    const QPlatformMediaIntegration *self) {
  return self->metaObject();
}

//  void *QPlatformMediaIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QPlatformMediaIntegration11qt_metacastEPKc(
    QPlatformMediaIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformMediaIntegration::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QPlatformMediaIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformMediaIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformMediaIntegration::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QPlatformMediaIntegration2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformMediaIntegration::tr(s, c, n));
}

//  QPlatformMediaIntegration *QPlatformMediaIntegration::instance()
extern "C" Q_DECL_EXPORT
QPlatformMediaIntegration *ritual_ZN25QPlatformMediaIntegration8instanceEv() {
  return QPlatformMediaIntegration::instance();
}

//  QPlatformMediaIntegration::QPlatformMediaIntegration(QLatin1String a0)
extern "C" Q_DECL_EXPORT
QPlatformMediaIntegration *ritual_ZN25QPlatformMediaIntegrationC1E13QLatin1String(
    const QLatin1String *a0) {
  return new CuteQPlatformMediaIntegration(*a0);
}

//  QPlatformMediaIntegration::~QPlatformMediaIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformMediaIntegrationD1Ev(
    QPlatformMediaIntegration *self) {
  delete self;
}

//  const QPlatformMediaFormatInfo *QPlatformMediaIntegration::formatInfo()
extern "C" Q_DECL_EXPORT
const QPlatformMediaFormatInfo *ritual_ZN25QPlatformMediaIntegration10formatInfoEv(
    QPlatformMediaIntegration *self) {
  return self->formatInfo();
}

//  q23::expected<QPlatformCamera *, QString>
//      QPlatformMediaIntegration::createCamera(QCamera *a0)
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformCamera *, QString> *ritual_ZN25QPlatformMediaIntegration12createCameraEP7QCamera(
    QPlatformMediaIntegration *self,
    QCamera *a0) {
  return new q23::expected<QPlatformCamera *, QString>(
      self->createCamera(
          a0));
}

//  QPlatformSurfaceCapture
//      *QPlatformMediaIntegration::createScreenCapture(QScreenCapture *a0)
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_ZN25QPlatformMediaIntegration19createScreenCaptureEP14QScreenCapture(
    QPlatformMediaIntegration *self,
    QScreenCapture *a0) {
  return self->createScreenCapture(a0);
}

//  QPlatformSurfaceCapture
//      *QPlatformMediaIntegration::createWindowCapture(QWindowCapture *a0)
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_ZN25QPlatformMediaIntegration19createWindowCaptureEP14QWindowCapture(
    QPlatformMediaIntegration *self,
    QWindowCapture *a0) {
  return self->createWindowCapture(a0);
}

//  q23::expected<QPlatformAudioDecoder *, QString>
//      QPlatformMediaIntegration::createAudioDecoder(QAudioDecoder *a0)
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformAudioDecoder *, QString> *ritual_ZN25QPlatformMediaIntegration18createAudioDecoderEP13QAudioDecoder(
    QPlatformMediaIntegration *self,
    QAudioDecoder *a0) {
  return new q23::expected<QPlatformAudioDecoder *, QString>(
      self->createAudioDecoder(
          a0));
}

//  q23::expected<std::unique_ptr<QPlatformAudioResampler>, QString>
//      QPlatformMediaIntegration::createAudioResampler(const QAudioFormat
//      &a0, const QAudioFormat &a1)
extern "C" Q_DECL_EXPORT
q23::expected<std::unique_ptr<QPlatformAudioResampler>, QString> *ritual_ZN25QPlatformMediaIntegration20createAudioResamplerERK12QAudioFormatS2_(
    QPlatformMediaIntegration *self,
    const QAudioFormat *a0,
    const QAudioFormat *a1) {
  return new q23::expected<std::unique_ptr<QPlatformAudioResampler>, QString>(
      self->createAudioResampler(
          *a0,
          *a1));
}

//  q23::expected<QPlatformMediaCaptureSession *, QString>
//      QPlatformMediaIntegration::createCaptureSession()
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformMediaCaptureSession *, QString> *ritual_ZN25QPlatformMediaIntegration20createCaptureSessionEv(
    QPlatformMediaIntegration *self) {
  return new q23::expected<QPlatformMediaCaptureSession *, QString>(
      self->createCaptureSession());
}

//  q23::expected<QPlatformMediaPlayer *, QString>
//      QPlatformMediaIntegration::createPlayer(QMediaPlayer *a0)
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformMediaPlayer *, QString> *ritual_ZN25QPlatformMediaIntegration12createPlayerEP12QMediaPlayer(
    QPlatformMediaIntegration *self,
    QMediaPlayer *a0) {
  return new q23::expected<QPlatformMediaPlayer *, QString>(
      self->createPlayer(
          a0));
}

//  q23::expected<QPlatformMediaRecorder *, QString>
//      QPlatformMediaIntegration::createRecorder(QMediaRecorder *a0)
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformMediaRecorder *, QString> *ritual_ZN25QPlatformMediaIntegration14createRecorderEP14QMediaRecorder(
    QPlatformMediaIntegration *self,
    QMediaRecorder *a0) {
  return new q23::expected<QPlatformMediaRecorder *, QString>(
      self->createRecorder(
          a0));
}

//  q23::expected<QPlatformImageCapture *, QString>
//      QPlatformMediaIntegration::createImageCapture(QImageCapture *a0)
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformImageCapture *, QString> *ritual_ZN25QPlatformMediaIntegration18createImageCaptureEP13QImageCapture(
    QPlatformMediaIntegration *self,
    QImageCapture *a0) {
  return new q23::expected<QPlatformImageCapture *, QString>(
      self->createImageCapture(
          a0));
}

//  q23::expected<QPlatformAudioInput *, QString>
//      QPlatformMediaIntegration::createAudioInput(QAudioInput *a0)
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformAudioInput *, QString> *ritual_ZN25QPlatformMediaIntegration16createAudioInputEP11QAudioInput(
    QPlatformMediaIntegration *self,
    QAudioInput *a0) {
  return new q23::expected<QPlatformAudioInput *, QString>(
      self->createAudioInput(
          a0));
}

//  q23::expected<QPlatformAudioOutput *, QString>
//      QPlatformMediaIntegration::createAudioOutput(QAudioOutput *a0)
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformAudioOutput *, QString> *ritual_ZN25QPlatformMediaIntegration17createAudioOutputEP12QAudioOutput(
    QPlatformMediaIntegration *self,
    QAudioOutput *a0) {
  return new q23::expected<QPlatformAudioOutput *, QString>(
      self->createAudioOutput(
          a0));
}

//  q23::expected<QPlatformVideoSink *, QString>
//      QPlatformMediaIntegration::createVideoSink(QVideoSink *a0)
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformVideoSink *, QString> *ritual_ZN25QPlatformMediaIntegration15createVideoSinkEP10QVideoSink(
    QPlatformMediaIntegration *self,
    QVideoSink *a0) {
  return new q23::expected<QPlatformVideoSink *, QString>(
      self->createVideoSink(
          a0));
}

//  QList<QCapturableWindow>
//      QPlatformMediaIntegration::capturableWindowsList()
extern "C" Q_DECL_EXPORT
QList<QCapturableWindow> *ritual_ZN25QPlatformMediaIntegration21capturableWindowsListEv(
    QPlatformMediaIntegration *self) {
  return new QList<QCapturableWindow>(self->capturableWindowsList());
}

//  bool QPlatformMediaIntegration::isCapturableWindowValid(const
//      QCapturableWindowPrivate &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QPlatformMediaIntegration23isCapturableWindowValidERK24QCapturableWindowPrivate(
    QPlatformMediaIntegration *self,
    const QCapturableWindowPrivate *a0) {
  return self->isCapturableWindowValid(*a0);
}

//  q23::expected<QCapturableWindow, QString>
//      QPlatformMediaIntegration::capturableWindowFromQWindow(QWindow *a0)
extern "C" Q_DECL_EXPORT
q23::expected<QCapturableWindow, QString> *ritual_ZN25QPlatformMediaIntegration27capturableWindowFromQWindowEP7QWindow(
    QPlatformMediaIntegration *self,
    QWindow *a0) {
  return new q23::expected<QCapturableWindow, QString>(
      self->capturableWindowFromQWindow(
          a0));
}

//  QPlatformVideoDevices *QPlatformMediaIntegration::videoDevices()
extern "C" Q_DECL_EXPORT
QPlatformVideoDevices *ritual_ZN25QPlatformMediaIntegration12videoDevicesEv(
    QPlatformMediaIntegration *self) {
  return self->videoDevices();
}

//  QPlatformCapturableWindows
//      *QPlatformMediaIntegration::capturableWindows()
extern "C" Q_DECL_EXPORT
QPlatformCapturableWindows *ritual_ZN25QPlatformMediaIntegration17capturableWindowsEv(
    QPlatformMediaIntegration *self) {
  return self->capturableWindows();
}

//  QPlatformAudioDevices *QPlatformMediaIntegration::audioDevices()
extern "C" Q_DECL_EXPORT
QPlatformAudioDevices *ritual_ZN25QPlatformMediaIntegration12audioDevicesEv(
    QPlatformMediaIntegration *self) {
  return self->audioDevices();
}

//  QStringList QPlatformMediaIntegration::availableBackends()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN25QPlatformMediaIntegration17availableBackendsEv() {
  return new QList<QString>(QPlatformMediaIntegration::availableBackends());
}

//  QString QPlatformMediaIntegration::defaultBackend()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QPlatformMediaIntegration14defaultBackendEv() {
  return new QString(QPlatformMediaIntegration::defaultBackend());
}

//  void QPlatformMediaIntegration::setBackend(const QString &backend)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformMediaIntegration10setBackendERK7QString(
    const QString *backend) {
  QPlatformMediaIntegration::setBackend(*backend);
}

//  QLatin1String QPlatformMediaIntegration::name()
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZN25QPlatformMediaIntegration4nameEv(
    QPlatformMediaIntegration *self) {
  return new QLatin1String(self->name());
}

//  QVideoFrame QPlatformMediaIntegration::convertVideoFrame(QVideoFrame &a0,
//      const QVideoFrameFormat &a1)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN25QPlatformMediaIntegration17convertVideoFrameER11QVideoFrameRK17QVideoFrameFormat(
    QPlatformMediaIntegration *self,
    QVideoFrame *a0,
    const QVideoFrameFormat *a1) {
  return new QVideoFrame(self->convertVideoFrame(*a0, *a1));
}

//  QLatin1String QPlatformMediaIntegration::audioBackendName()
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZN25QPlatformMediaIntegration16audioBackendNameEv() {
  return new QLatin1String(QPlatformMediaIntegration::audioBackendName());
}

//  bool
//      QPlatformMediaIntegration::isCameraSwitchingDuringRecordingSupported(
//      ) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QPlatformMediaIntegration41isCameraSwitchingDuringRecordingSupportedEv(
    const QPlatformMediaIntegration *self) {
  return self->isCameraSwitchingDuringRecordingSupported();
}

//  q23::expected<QPlatformCamera *, QString> QPlatformMediaIntegration::crea
//      teGStreamerVideoSource(QGStreamerVideoSource *a0, const
//      GstElementOrDescription &a1)
extern "C" Q_DECL_EXPORT
q23::expected<QPlatformCamera *, QString> *ritual_ZN25QPlatformMediaIntegration26createGStreamerVideoSourceEP21QGStreamerVideoSourceRKSt7variantIJ7QStringP11_GstElementEE(
    QPlatformMediaIntegration *self,
    QGStreamerVideoSource *a0,
    const GstElementOrDescription *a1) {
  return new q23::expected<QPlatformCamera *, QString>(
      self->createGStreamerVideoSource(
          a0,
          *a1));
}

//  QGStreamerInterface *QPlatformMediaIntegration::gstreamerInterface()
extern "C" Q_DECL_EXPORT
QGStreamerInterface *ritual_ZN25QPlatformMediaIntegration18gstreamerInterfaceEv(
    QPlatformMediaIntegration *self) {
  return self->gstreamerInterface();
}

//  void QPlatformMediaIntegration::resetInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformMediaIntegration13resetInstanceEv(
    QPlatformMediaIntegration *self) {
  self->resetInstance();
}

//  QPlatformMediaFormatInfo *QPlatformMediaIntegration::createFormatInfo()
extern "C" Q_DECL_EXPORT
QPlatformMediaFormatInfo *ritual_ZN25QPlatformMediaIntegration16createFormatInfoEv(
    QPlatformMediaIntegration *self) {
  return self->createFormatInfo();
}

//  QPlatformVideoDevices *QPlatformMediaIntegration::createVideoDevices()
extern "C" Q_DECL_EXPORT
QPlatformVideoDevices *ritual_ZN25QPlatformMediaIntegration18createVideoDevicesEv(
    QPlatformMediaIntegration *self) {
  return self->createVideoDevices();
}

//  QPlatformCapturableWindows
//      *QPlatformMediaIntegration::createCapturableWindows()
extern "C" Q_DECL_EXPORT
QPlatformCapturableWindows *ritual_ZN25QPlatformMediaIntegration23createCapturableWindowsEv(
    QPlatformMediaIntegration *self) {
  return self->createCapturableWindows();
}

//  a Python function taken by a CuteQPlatformMediaIntegration, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformMediaIntegration(
    QPlatformMediaIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformMediaIntegration *>(self)->take(key, call);
}

//  QPlatformSurfaceCapture
//      *QPlatformMediaIntegration::createScreenCapture(QScreenCapture *a0)
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_own_ZN25QPlatformMediaIntegration19createScreenCaptureEP14QScreenCapture(
    QPlatformMediaIntegration *self,
    QScreenCapture *a0) {
  return self->QPlatformMediaIntegration::createScreenCapture(a0);
}

//  QPlatformSurfaceCapture
//      *QPlatformMediaIntegration::createWindowCapture(QWindowCapture *a0)
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_own_ZN25QPlatformMediaIntegration19createWindowCaptureEP14QWindowCapture(
    QPlatformMediaIntegration *self,
    QWindowCapture *a0) {
  return self->QPlatformMediaIntegration::createWindowCapture(a0);
}

//  bool
//      QPlatformMediaIntegration::isCameraSwitchingDuringRecordingSupported(
//      ) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QPlatformMediaIntegration41isCameraSwitchingDuringRecordingSupportedEv(
    const QPlatformMediaIntegration *self) {
  return self->QPlatformMediaIntegration::isCameraSwitchingDuringRecordingSupported();
}

//  QGStreamerInterface *QPlatformMediaIntegration::gstreamerInterface()
extern "C" Q_DECL_EXPORT
QGStreamerInterface *ritual_own_ZN25QPlatformMediaIntegration18gstreamerInterfaceEv(
    QPlatformMediaIntegration *self) {
  return self->QPlatformMediaIntegration::gstreamerInterface();
}

//  QPlatformMediaFormatInfo *QPlatformMediaIntegration::createFormatInfo()
extern "C" Q_DECL_EXPORT
QPlatformMediaFormatInfo *ritual_own_ZN25QPlatformMediaIntegration16createFormatInfoEv(
    QPlatformMediaIntegration *self) {
  return static_cast<OwnQPlatformMediaIntegration *>(self)->OwnQPlatformMediaIntegration::createFormatInfo();
}

//  QPlatformVideoDevices *QPlatformMediaIntegration::createVideoDevices()
extern "C" Q_DECL_EXPORT
QPlatformVideoDevices *ritual_own_ZN25QPlatformMediaIntegration18createVideoDevicesEv(
    QPlatformMediaIntegration *self) {
  return static_cast<OwnQPlatformMediaIntegration *>(self)->OwnQPlatformMediaIntegration::createVideoDevices();
}

//  QPlatformCapturableWindows
//      *QPlatformMediaIntegration::createCapturableWindows()
extern "C" Q_DECL_EXPORT
QPlatformCapturableWindows *ritual_own_ZN25QPlatformMediaIntegration23createCapturableWindowsEv(
    QPlatformMediaIntegration *self) {
  return static_cast<OwnQPlatformMediaIntegration *>(self)->OwnQPlatformMediaIntegration::createCapturableWindows();
}

//  a q23::expected<QPlatformCamera *, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QPlatformCamera_QString(
    q23::expected<QPlatformCamera *, QString> *self) {
  delete self;
}

//  a q23::expected<QPlatformAudioDecoder *, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QPlatformAudioDecoder_QString(
    q23::expected<QPlatformAudioDecoder *, QString> *self) {
  delete self;
}

//  a q23::expected<std::unique_ptr<QPlatformAudioResampler>, QString> a
//      ritual of QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_std_unique_ptr_QPlatformAudioResampler_QString(
    q23::expected<std::unique_ptr<QPlatformAudioResampler>, QString> *self) {
  delete self;
}

//  a q23::expected<QPlatformMediaCaptureSession *, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QPlatformMediaCaptureSession_QString(
    q23::expected<QPlatformMediaCaptureSession *, QString> *self) {
  delete self;
}

//  a q23::expected<QPlatformMediaPlayer *, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QPlatformMediaPlayer_QString(
    q23::expected<QPlatformMediaPlayer *, QString> *self) {
  delete self;
}

//  a q23::expected<QPlatformMediaRecorder *, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QPlatformMediaRecorder_QString(
    q23::expected<QPlatformMediaRecorder *, QString> *self) {
  delete self;
}

//  a q23::expected<QPlatformImageCapture *, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QPlatformImageCapture_QString(
    q23::expected<QPlatformImageCapture *, QString> *self) {
  delete self;
}

//  a q23::expected<QPlatformAudioInput *, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QPlatformAudioInput_QString(
    q23::expected<QPlatformAudioInput *, QString> *self) {
  delete self;
}

//  a q23::expected<QPlatformAudioOutput *, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QPlatformAudioOutput_QString(
    q23::expected<QPlatformAudioOutput *, QString> *self) {
  delete self;
}

//  a q23::expected<QPlatformVideoSink *, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QPlatformVideoSink_QString(
    q23::expected<QPlatformVideoSink *, QString> *self) {
  delete self;
}

//  a q23::expected<QCapturableWindow, QString> a ritual of
//      QPlatformMediaIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaIntegration__q23_expected_QCapturableWindow_QString(
    q23::expected<QCapturableWindow, QString> *self) {
  delete self;
}
