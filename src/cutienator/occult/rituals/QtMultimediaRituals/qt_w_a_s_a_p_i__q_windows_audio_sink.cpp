//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiosink_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its destructor,
//  which is virtual, is called, through the object. It is final, so 'self'
//  is taken as a QPlatformAudioSink, and the call stays virtual. Not
//  written: the constructor, which Qt's library offers not.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiosink_p.h>

//  QtWASAPI::QWindowsAudioSink::~QWindowsAudioSink()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QtWASAPI17QWindowsAudioSinkD1Ev(QPlatformAudioSink *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
