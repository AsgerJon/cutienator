//  Written by hand on 2026-11-26 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerabase_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Objective-C++: the header imports AVFoundation, so only a compiler of
//  Objective-C++ on Apple's systems reads it; 'summon' builds this file
//  there only. Qt's library offers the class, and the rituals call it. The
//  class is abstract: an object of it is one of a class Qt builds on it.
//  'AVCaptureDevice' crosses as its address.
#include <QtMultimedia/qtmultimediaglobal.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerabase_p.h>

//  bool QAVFCameraBase::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAVFCameraBase8isActiveEv(
    const QAVFCameraBase *self) {
  return self->isActive();
}

//  void QAVFCameraBase::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase9setActiveEb(
    QAVFCameraBase *self,
    bool active) {
  self->setActive(active);
}

//  void QAVFCameraBase::setCamera(const QCameraDevice &camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase9setCameraERK13QCameraDevice(
    QAVFCameraBase *self,
    const QCameraDevice *camera) {
  self->setCamera(*camera);
}

//  bool QAVFCameraBase::setCameraFormat(const QCameraFormat &format)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QAVFCameraBase15setCameraFormatERK13QCameraFormat(
    QAVFCameraBase *self,
    const QCameraFormat *format) {
  return self->setCameraFormat(*format);
}

//  void QAVFCameraBase::setFocusMode(QCamera::FocusMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase12setFocusModeEN7QCamera9FocusModeE(
    QAVFCameraBase *self,
    int mode) {
  self->setFocusMode(static_cast<QCamera::FocusMode>(mode));
}

//  bool QAVFCameraBase::isFocusModeSupported(QCamera::FocusMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAVFCameraBase20isFocusModeSupportedEN7QCamera9FocusModeE(
    const QAVFCameraBase *self,
    int mode) {
  return self->isFocusModeSupported(static_cast<QCamera::FocusMode>(mode));
}

//  void QAVFCameraBase::setCustomFocusPoint(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase19setCustomFocusPointERK7QPointF(
    QAVFCameraBase *self,
    const QPointF *point) {
  self->setCustomFocusPoint(*point);
}

//  void QAVFCameraBase::setFocusDistance(float distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase16setFocusDistanceEf(
    QAVFCameraBase *self,
    float distance) {
  self->setFocusDistance(distance);
}

//  void QAVFCameraBase::zoomTo(float factor, float rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase6zoomToEff(
    QAVFCameraBase *self,
    float factor,
    float rate) {
  self->zoomTo(factor, rate);
}

//  void QAVFCameraBase::setFlashMode(QCamera::FlashMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase12setFlashModeEN7QCamera9FlashModeE(
    QAVFCameraBase *self,
    int mode) {
  self->setFlashMode(static_cast<QCamera::FlashMode>(mode));
}

//  bool QAVFCameraBase::isFlashModeSupported(QCamera::FlashMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAVFCameraBase20isFlashModeSupportedEN7QCamera9FlashModeE(
    const QAVFCameraBase *self,
    int mode) {
  return self->isFlashModeSupported(static_cast<QCamera::FlashMode>(mode));
}

//  bool QAVFCameraBase::isFlashReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAVFCameraBase12isFlashReadyEv(
    const QAVFCameraBase *self) {
  return self->isFlashReady();
}

//  void QAVFCameraBase::setTorchMode(QCamera::TorchMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase12setTorchModeEN7QCamera9TorchModeE(
    QAVFCameraBase *self,
    int mode) {
  self->setTorchMode(static_cast<QCamera::TorchMode>(mode));
}

//  bool QAVFCameraBase::isTorchModeSupported(QCamera::TorchMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAVFCameraBase20isTorchModeSupportedEN7QCamera9TorchModeE(
    const QAVFCameraBase *self,
    int mode) {
  return self->isTorchModeSupported(static_cast<QCamera::TorchMode>(mode));
}

//  void QAVFCameraBase::setExposureMode(QCamera::ExposureMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase15setExposureModeEN7QCamera12ExposureModeE(
    QAVFCameraBase *self,
    int mode) {
  self->setExposureMode(static_cast<QCamera::ExposureMode>(mode));
}

//  bool QAVFCameraBase::isExposureModeSupported(QCamera::ExposureMode mode)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAVFCameraBase23isExposureModeSupportedEN7QCamera12ExposureModeE(
    const QAVFCameraBase *self,
    int mode) {
  return self->isExposureModeSupported(static_cast<QCamera::ExposureMode>(mode));
}

//  void QAVFCameraBase::setExposureCompensation(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase23setExposureCompensationEf(
    QAVFCameraBase *self,
    float bias) {
  self->setExposureCompensation(bias);
}

//  void QAVFCameraBase::setManualIsoSensitivity(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase23setManualIsoSensitivityEi(
    QAVFCameraBase *self,
    int value) {
  self->setManualIsoSensitivity(value);
}

//  int QAVFCameraBase::isoSensitivity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QAVFCameraBase14isoSensitivityEv(
    const QAVFCameraBase *self) {
  return self->isoSensitivity();
}

//  void QAVFCameraBase::setManualExposureTime(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase21setManualExposureTimeEf(
    QAVFCameraBase *self,
    float value) {
  self->setManualExposureTime(value);
}

//  float QAVFCameraBase::exposureTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14QAVFCameraBase12exposureTimeEv(
    const QAVFCameraBase *self) {
  return self->exposureTime();
}

//  bool
//      QAVFCameraBase::isWhiteBalanceModeSupported(QCamera::WhiteBalanceMode
//      mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAVFCameraBase27isWhiteBalanceModeSupportedEN7QCamera16WhiteBalanceModeE(
    const QAVFCameraBase *self,
    int mode) {
  return self->isWhiteBalanceModeSupported(static_cast<QCamera::WhiteBalanceMode>(mode));
}

//  void QAVFCameraBase::setWhiteBalanceMode(QCamera::WhiteBalanceMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase19setWhiteBalanceModeEN7QCamera16WhiteBalanceModeE(
    QAVFCameraBase *self,
    int mode) {
  self->setWhiteBalanceMode(static_cast<QCamera::WhiteBalanceMode>(mode));
}

//  void QAVFCameraBase::setColorTemperature(int temperature)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBase19setColorTemperatureEi(
    QAVFCameraBase *self,
    int temperature) {
  self->setColorTemperature(temperature);
}

//  AVCaptureDevice *QAVFCameraBase::device() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK14QAVFCameraBase6deviceEv(
    const QAVFCameraBase *self) {
  return self->device();
}

//  bool QAVFCameraBase::checkCameraPermission()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QAVFCameraBase21checkCameraPermissionEv(
    QAVFCameraBase *self) {
  return self->checkCameraPermission();
}

//  QAVFCameraBase::~QAVFCameraBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAVFCameraBaseD1Ev(
    QAVFCameraBase *self) {
  delete self;
}

#endif
