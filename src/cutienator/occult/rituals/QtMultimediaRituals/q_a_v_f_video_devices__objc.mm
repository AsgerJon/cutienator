//  Written by hand on 2026-11-26 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qavfvideodevices_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Objective-C++: the header imports AVFoundation, so only a compiler of
//  Objective-C++ on Apple's systems reads it; 'summon' builds this file
//  there only. Qt's library offers the class, and the rituals call it. The
//  constructor takes a 'std::function': its ritual, 'ritual_callback' and
//  the compiler's name of the constructor, takes a C function of Python's
//  and its context, and hands Qt a 'std::function' calling it with the
//  context first.
#include <QtMultimedia/qtmultimediaglobal.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qavfvideodevices_p.h>
#include <functional>

//  QAVFVideoDevices::QAVFVideoDevices(QPlatformMediaIntegration
//      *integration, std::function<bool(uint32_t)>
//      &&isCvPixelFormatSupportedDelegate)
extern "C" Q_DECL_EXPORT
QAVFVideoDevices *ritual_callback_ZN16QAVFVideoDevicesC1EP25QPlatformMediaIntegrationOSt8functionIFbjEE(
    QPlatformMediaIntegration *integration,
    void *call,
    void *context) {
  auto function = reinterpret_cast<bool (*)(void *, uint32_t)>(call);
  std::function<bool(uint32_t)> delegate;
  if (function)
    delegate = [function, context](uint32_t format) {
      return function(context, format);
    };
  return new QAVFVideoDevices(integration, std::move(delegate));
}

//  QAVFVideoDevices::~QAVFVideoDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAVFVideoDevicesD1Ev(
    QAVFVideoDevices *self) {
  delete self;
}

//  QList<QCameraDevice> QAVFVideoDevices::findVideoInputs() const
extern "C" Q_DECL_EXPORT
QList<QCameraDevice> *ritual_ZNK16QAVFVideoDevices15findVideoInputsEv(
    const QAVFVideoDevices *self) {
  return new QList<QCameraDevice>(self->findVideoInputs());
}

//  void QAVFVideoDevices::onAvCaptureDevicesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAVFVideoDevices25onAvCaptureDevicesChangedEv(
    QAVFVideoDevices *self) {
  self->onAvCaptureDevicesChanged();
}

//  void QAVFVideoDevices::rebuildObserveredAvCaptureDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAVFVideoDevices33rebuildObserveredAvCaptureDevicesEv(
    QAVFVideoDevices *self) {
  self->rebuildObserveredAvCaptureDevices();
}

#endif
