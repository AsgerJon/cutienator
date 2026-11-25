//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiodevice_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its destructor,
//  which is virtual, is called, through the object. It is final, so 'self'
//  is taken as a QAudioDevicePrivate, and the call stays virtual. Not
//  written: the constructors, 'clone' and 'open', which Qt's library offers
//  not.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiodevice_p.h>

//  QWindowsAudioDevice::~QWindowsAudioDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWindowsAudioDeviceD1Ev(QAudioDevicePrivate *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
