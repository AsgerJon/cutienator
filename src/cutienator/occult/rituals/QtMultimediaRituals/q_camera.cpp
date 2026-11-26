//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qcamera.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qcamera.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qcameradevice.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCamera that Python can take functions over in. Every QCamera
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCameraCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCameraCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCameraCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCameraCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCameraCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCameraCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCameraCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCamera : public QCamera {
public:
  using QCamera::QCamera;
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
      CuteQCameraCall0 call = reinterpret_cast<CuteQCameraCall0>(taken[0]);
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
      CuteQCameraCall1 call = reinterpret_cast<CuteQCameraCall1>(taken[1]);
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
      CuteQCameraCall2 call = reinterpret_cast<CuteQCameraCall2>(taken[2]);
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
      CuteQCameraCall3 call = reinterpret_cast<CuteQCameraCall3>(taken[3]);
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
      CuteQCameraCall4 call = reinterpret_cast<CuteQCameraCall4>(taken[4]);
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
      CuteQCameraCall5 call = reinterpret_cast<CuteQCameraCall5>(taken[5]);
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
      CuteQCameraCall6 call = reinterpret_cast<CuteQCameraCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QCamera10metaObjectEv(const QCamera *self) {
  return self->metaObject();
}

//  void *QCamera::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN7QCamera11qt_metacastEPKc(QCamera *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCamera::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QCamera11qt_metacallEN11QMetaObject4CallEiPPv(
    QCamera *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCamera::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QCamera2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QCamera::tr(s, c, n));
}

//  QCamera::QCamera(QObject *parent)
extern "C" Q_DECL_EXPORT
QCamera *ritual_ZN7QCameraC1EP7QObject(QObject *parent) {
  return new CuteQCamera(parent);
}

//  QCamera::QCamera(const QCameraDevice &cameraDevice, QObject *parent)
extern "C" Q_DECL_EXPORT
QCamera *ritual_ZN7QCameraC1ERK13QCameraDeviceP7QObject(
    const QCameraDevice *cameraDevice,
    QObject *parent) {
  return new CuteQCamera(*cameraDevice, parent);
}

//  QCamera::QCamera(QCameraDevice::Position position, QObject *parent)
extern "C" Q_DECL_EXPORT
QCamera *ritual_ZN7QCameraC1EN13QCameraDevice8PositionEP7QObject(
    QCameraDevice::Position position,
    QObject *parent) {
  return new CuteQCamera(position, parent);
}

//  QCamera::~QCamera()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCameraD1Ev(QCamera *self) {
  delete self;
}

//  bool QCamera::isAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QCamera11isAvailableEv(const QCamera *self) {
  return self->isAvailable();
}

//  bool QCamera::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QCamera8isActiveEv(const QCamera *self) {
  return self->isActive();
}

//  QMediaCaptureSession *QCamera::captureSession() const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK7QCamera14captureSessionEv(
    const QCamera *self) {
  return self->captureSession();
}

//  QCameraDevice QCamera::cameraDevice() const
extern "C" Q_DECL_EXPORT
QCameraDevice *ritual_ZNK7QCamera12cameraDeviceEv(const QCamera *self) {
  return new QCameraDevice(self->cameraDevice());
}

//  void QCamera::setCameraDevice(const QCameraDevice &cameraDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera15setCameraDeviceERK13QCameraDevice(
    QCamera *self,
    const QCameraDevice *cameraDevice) {
  self->setCameraDevice(*cameraDevice);
}

//  QCameraFormat QCamera::cameraFormat() const
extern "C" Q_DECL_EXPORT
QCameraFormat *ritual_ZNK7QCamera12cameraFormatEv(const QCamera *self) {
  return new QCameraFormat(self->cameraFormat());
}

//  void QCamera::setCameraFormat(const QCameraFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera15setCameraFormatERK13QCameraFormat(
    QCamera *self,
    const QCameraFormat *format) {
  self->setCameraFormat(*format);
}

//  Error QCamera::error() const
extern "C" Q_DECL_EXPORT
QCamera::Error ritual_ZNK7QCamera5errorEv(const QCamera *self) {
  return self->error();
}

//  QString QCamera::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QCamera11errorStringEv(const QCamera *self) {
  return new QString(self->errorString());
}

//  Features QCamera::supportedFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCamera17supportedFeaturesEv(const QCamera *self) {
  return static_cast<int>(self->supportedFeatures().toInt());
}

//  FocusMode QCamera::focusMode() const
extern "C" Q_DECL_EXPORT
QCamera::FocusMode ritual_ZNK7QCamera9focusModeEv(const QCamera *self) {
  return self->focusMode();
}

//  void QCamera::setFocusMode(FocusMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera12setFocusModeENS_9FocusModeE(
    QCamera *self,
    QCamera::FocusMode mode) {
  self->setFocusMode(mode);
}

//  bool QCamera::isFocusModeSupported(FocusMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QCamera20isFocusModeSupportedENS_9FocusModeE(
    const QCamera *self,
    QCamera::FocusMode mode) {
  return self->isFocusModeSupported(mode);
}

//  QPointF QCamera::focusPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QCamera10focusPointEv(const QCamera *self) {
  return new QPointF(self->focusPoint());
}

//  QPointF QCamera::customFocusPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QCamera16customFocusPointEv(const QCamera *self) {
  return new QPointF(self->customFocusPoint());
}

//  void QCamera::setCustomFocusPoint(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera19setCustomFocusPointERK7QPointF(
    QCamera *self,
    const QPointF *point) {
  self->setCustomFocusPoint(*point);
}

//  void QCamera::setFocusDistance(float d)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera16setFocusDistanceEf(QCamera *self, float d) {
  self->setFocusDistance(d);
}

//  float QCamera::focusDistance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QCamera13focusDistanceEv(const QCamera *self) {
  return self->focusDistance();
}

//  float QCamera::minimumZoomFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QCamera17minimumZoomFactorEv(const QCamera *self) {
  return self->minimumZoomFactor();
}

//  float QCamera::maximumZoomFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QCamera17maximumZoomFactorEv(const QCamera *self) {
  return self->maximumZoomFactor();
}

//  float QCamera::zoomFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QCamera10zoomFactorEv(const QCamera *self) {
  return self->zoomFactor();
}

//  void QCamera::setZoomFactor(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera13setZoomFactorEf(QCamera *self, float factor) {
  self->setZoomFactor(factor);
}

//  FlashMode QCamera::flashMode() const
extern "C" Q_DECL_EXPORT
QCamera::FlashMode ritual_ZNK7QCamera9flashModeEv(const QCamera *self) {
  return self->flashMode();
}

//  bool QCamera::isFlashModeSupported(FlashMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QCamera20isFlashModeSupportedENS_9FlashModeE(
    const QCamera *self,
    QCamera::FlashMode mode) {
  return self->isFlashModeSupported(mode);
}

//  bool QCamera::isFlashReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QCamera12isFlashReadyEv(const QCamera *self) {
  return self->isFlashReady();
}

//  TorchMode QCamera::torchMode() const
extern "C" Q_DECL_EXPORT
QCamera::TorchMode ritual_ZNK7QCamera9torchModeEv(const QCamera *self) {
  return self->torchMode();
}

//  bool QCamera::isTorchModeSupported(TorchMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QCamera20isTorchModeSupportedENS_9TorchModeE(
    const QCamera *self,
    QCamera::TorchMode mode) {
  return self->isTorchModeSupported(mode);
}

//  ExposureMode QCamera::exposureMode() const
extern "C" Q_DECL_EXPORT
QCamera::ExposureMode ritual_ZNK7QCamera12exposureModeEv(
    const QCamera *self) {
  return self->exposureMode();
}

//  bool QCamera::isExposureModeSupported(ExposureMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QCamera23isExposureModeSupportedENS_12ExposureModeE(
    const QCamera *self,
    QCamera::ExposureMode mode) {
  return self->isExposureModeSupported(mode);
}

//  float QCamera::exposureCompensation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QCamera20exposureCompensationEv(const QCamera *self) {
  return self->exposureCompensation();
}

//  int QCamera::isoSensitivity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCamera14isoSensitivityEv(const QCamera *self) {
  return self->isoSensitivity();
}

//  int QCamera::manualIsoSensitivity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCamera20manualIsoSensitivityEv(const QCamera *self) {
  return self->manualIsoSensitivity();
}

//  float QCamera::exposureTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QCamera12exposureTimeEv(const QCamera *self) {
  return self->exposureTime();
}

//  float QCamera::manualExposureTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QCamera18manualExposureTimeEv(const QCamera *self) {
  return self->manualExposureTime();
}

//  int QCamera::minimumIsoSensitivity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCamera21minimumIsoSensitivityEv(const QCamera *self) {
  return self->minimumIsoSensitivity();
}

//  int QCamera::maximumIsoSensitivity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCamera21maximumIsoSensitivityEv(const QCamera *self) {
  return self->maximumIsoSensitivity();
}

//  float QCamera::minimumExposureTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QCamera19minimumExposureTimeEv(const QCamera *self) {
  return self->minimumExposureTime();
}

//  float QCamera::maximumExposureTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QCamera19maximumExposureTimeEv(const QCamera *self) {
  return self->maximumExposureTime();
}

//  WhiteBalanceMode QCamera::whiteBalanceMode() const
extern "C" Q_DECL_EXPORT
QCamera::WhiteBalanceMode ritual_ZNK7QCamera16whiteBalanceModeEv(
    const QCamera *self) {
  return self->whiteBalanceMode();
}

//  bool QCamera::isWhiteBalanceModeSupported(WhiteBalanceMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QCamera27isWhiteBalanceModeSupportedENS_16WhiteBalanceModeE(
    const QCamera *self,
    QCamera::WhiteBalanceMode mode) {
  return self->isWhiteBalanceModeSupported(mode);
}

//  int QCamera::colorTemperature() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCamera16colorTemperatureEv(const QCamera *self) {
  return self->colorTemperature();
}

//  void QCamera::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera9setActiveEb(QCamera *self, bool active) {
  self->setActive(active);
}

//  void QCamera::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera5startEv(QCamera *self) {
  self->start();
}

//  void QCamera::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera4stopEv(QCamera *self) {
  self->stop();
}

//  void QCamera::zoomTo(float zoom, float rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera6zoomToEff(QCamera *self, float zoom, float rate) {
  self->zoomTo(zoom, rate);
}

//  void QCamera::setFlashMode(FlashMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera12setFlashModeENS_9FlashModeE(
    QCamera *self,
    QCamera::FlashMode mode) {
  self->setFlashMode(mode);
}

//  void QCamera::setTorchMode(TorchMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera12setTorchModeENS_9TorchModeE(
    QCamera *self,
    QCamera::TorchMode mode) {
  self->setTorchMode(mode);
}

//  void QCamera::setExposureMode(ExposureMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera15setExposureModeENS_12ExposureModeE(
    QCamera *self,
    QCamera::ExposureMode mode) {
  self->setExposureMode(mode);
}

//  void QCamera::setExposureCompensation(float ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera23setExposureCompensationEf(QCamera *self, float ev) {
  self->setExposureCompensation(ev);
}

//  void QCamera::setManualIsoSensitivity(int iso)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera23setManualIsoSensitivityEi(QCamera *self, int iso) {
  self->setManualIsoSensitivity(iso);
}

//  void QCamera::setAutoIsoSensitivity()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera21setAutoIsoSensitivityEv(QCamera *self) {
  self->setAutoIsoSensitivity();
}

//  void QCamera::setManualExposureTime(float seconds)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera21setManualExposureTimeEf(
    QCamera *self,
    float seconds) {
  self->setManualExposureTime(seconds);
}

//  void QCamera::setAutoExposureTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera19setAutoExposureTimeEv(QCamera *self) {
  self->setAutoExposureTime();
}

//  void QCamera::setWhiteBalanceMode(WhiteBalanceMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera19setWhiteBalanceModeENS_16WhiteBalanceModeE(
    QCamera *self,
    QCamera::WhiteBalanceMode mode) {
  self->setWhiteBalanceMode(mode);
}

//  void QCamera::setColorTemperature(int colorTemperature)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera19setColorTemperatureEi(
    QCamera *self,
    int colorTemperature) {
  self->setColorTemperature(colorTemperature);
}

//  void QCamera::activeChanged(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera13activeChangedEb(QCamera *self, bool a0) {
  self->activeChanged(a0);
}

//  void QCamera::errorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera12errorChangedEv(QCamera *self) {
  self->errorChanged();
}

//  void QCamera::errorOccurred(QCamera::Error error, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera13errorOccurredENS_5ErrorERK7QString(
    QCamera *self,
    QCamera::Error error,
    const QString *errorString) {
  self->errorOccurred(error, *errorString);
}

//  void QCamera::cameraDeviceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera19cameraDeviceChangedEv(QCamera *self) {
  self->cameraDeviceChanged();
}

//  void QCamera::cameraFormatChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera19cameraFormatChangedEv(QCamera *self) {
  self->cameraFormatChanged();
}

//  void QCamera::supportedFeaturesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera24supportedFeaturesChangedEv(QCamera *self) {
  self->supportedFeaturesChanged();
}

//  void QCamera::focusModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera16focusModeChangedEv(QCamera *self) {
  self->focusModeChanged();
}

//  void QCamera::zoomFactorChanged(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera17zoomFactorChangedEf(QCamera *self, float a0) {
  self->zoomFactorChanged(a0);
}

//  void QCamera::minimumZoomFactorChanged(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera24minimumZoomFactorChangedEf(QCamera *self, float a0) {
  self->minimumZoomFactorChanged(a0);
}

//  void QCamera::maximumZoomFactorChanged(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera24maximumZoomFactorChangedEf(QCamera *self, float a0) {
  self->maximumZoomFactorChanged(a0);
}

//  void QCamera::focusDistanceChanged(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera20focusDistanceChangedEf(QCamera *self, float a0) {
  self->focusDistanceChanged(a0);
}

//  void QCamera::focusPointChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera17focusPointChangedEv(QCamera *self) {
  self->focusPointChanged();
}

//  void QCamera::customFocusPointChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera23customFocusPointChangedEv(QCamera *self) {
  self->customFocusPointChanged();
}

//  void QCamera::flashReady(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera10flashReadyEb(QCamera *self, bool a0) {
  self->flashReady(a0);
}

//  void QCamera::flashModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera16flashModeChangedEv(QCamera *self) {
  self->flashModeChanged();
}

//  void QCamera::torchModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera16torchModeChangedEv(QCamera *self) {
  self->torchModeChanged();
}

//  void QCamera::exposureTimeChanged(float speed)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera19exposureTimeChangedEf(QCamera *self, float speed) {
  self->exposureTimeChanged(speed);
}

//  void QCamera::manualExposureTimeChanged(float speed)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera25manualExposureTimeChangedEf(
    QCamera *self,
    float speed) {
  self->manualExposureTimeChanged(speed);
}

//  void QCamera::isoSensitivityChanged(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera21isoSensitivityChangedEi(QCamera *self, int a0) {
  self->isoSensitivityChanged(a0);
}

//  void QCamera::manualIsoSensitivityChanged(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera27manualIsoSensitivityChangedEi(
    QCamera *self,
    int a0) {
  self->manualIsoSensitivityChanged(a0);
}

//  void QCamera::exposureCompensationChanged(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera27exposureCompensationChangedEf(
    QCamera *self,
    float a0) {
  self->exposureCompensationChanged(a0);
}

//  void QCamera::exposureModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera19exposureModeChangedEv(QCamera *self) {
  self->exposureModeChanged();
}

//  void QCamera::whiteBalanceModeChanged() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QCamera23whiteBalanceModeChangedEv(const QCamera *self) {
  self->whiteBalanceModeChanged();
}

//  void QCamera::colorTemperatureChanged() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QCamera23colorTemperatureChangedEv(const QCamera *self) {
  self->colorTemperatureChanged();
}

//  void QCamera::brightnessChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera17brightnessChangedEv(QCamera *self) {
  self->brightnessChanged();
}

//  void QCamera::contrastChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera15contrastChangedEv(QCamera *self) {
  self->contrastChanged();
}

//  void QCamera::saturationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera17saturationChangedEv(QCamera *self) {
  self->saturationChanged();
}

//  void QCamera::hueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera10hueChangedEv(QCamera *self) {
  self->hueChanged();
}

//  class QPlatformCamera *QCamera::platformCamera()
extern "C" Q_DECL_EXPORT
class QPlatformCamera *ritual_ZN7QCamera14platformCameraEv(QCamera *self) {
  return self->platformCamera();
}

//  void QCamera::setCaptureSession(QMediaCaptureSession *session)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCamera17setCaptureSessionEP20QMediaCaptureSession(
    QCamera *self,
    QMediaCaptureSession *session) {
  self->setCaptureSession(session);
}

//  QCameraPrivate *QCamera::d_func()
extern "C" Q_DECL_EXPORT
QCameraPrivate *ritual_ZN7QCamera6d_funcEv(QCamera *self) {
  return self->d_func();
}

//  const QCameraPrivate *QCamera::d_func() const
extern "C" Q_DECL_EXPORT
const QCameraPrivate *ritual_ZNK7QCamera6d_funcEv(const QCamera *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCamera, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCamera(QCamera *self, const char *key, void *call) {
  return static_cast<CuteQCamera *>(self)->take(key, call);
}
