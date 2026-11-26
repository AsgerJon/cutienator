//  Written by hand on 2026-11-26 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerautility_p.h, Qt
//  6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  Objective-C++: the header imports AVFoundation, so only a compiler of
//  Objective-C++ on Apple's systems reads it; 'summon' builds this file
//  there only. Each function is Qt's code in the header.
#include <QtMultimedia/qtmultimediaglobal.h>
#if __has_include(<QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerautility_p.h>)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerautility_p.h>

//  AVFConfigurationLock::AVFConfigurationLock(AVCaptureDevice *captureDevice)
extern "C" Q_DECL_EXPORT
AVFConfigurationLock *ritual_ZN20AVFConfigurationLockC1EP15AVCaptureDevice(
    AVCaptureDevice *a0) {
  return new AVFConfigurationLock(a0);
}

//  AVFConfigurationLock::~AVFConfigurationLock()
extern "C" Q_DECL_EXPORT
void ritual_ZN20AVFConfigurationLockD1Ev(AVFConfigurationLock *self) {
  delete self;
}

//  AVFConfigurationLock::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20AVFConfigurationLockcvbEv(const AVFConfigurationLock *self) {
  return self->operator bool();
}

#endif  // __has_include(<QtMultimedia/6.12.0/QtMultimedia/private/qavfcamerautility_p.h>)
