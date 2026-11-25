//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiosource_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its virtual
//  function is called, through the object, and what its header writes out.
//  It is final, so 'self' is taken as a
//  QtMultimediaPrivate::QPlatformAudioSourceStream for that one, and the
//  call stays virtual. Not written: the constructor, the destructor,
//  'start', 'stop', 'suspend', 'resume' and the others its header declares,
//  which Qt's library offers not.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiosource_p.h>

//  void QtWASAPI::QWASAPIAudioSourceStream::updateStreamIdle(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QtWASAPI24QWASAPIAudioSourceStream16updateStreamIdleEb(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self,
    bool a0) {
  self->updateStreamIdle(a0);
}

//  bool QtWASAPI::QWASAPIAudioSourceStream::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QtWASAPI24QWASAPIAudioSourceStream4openEv(
    QtWASAPI::QWASAPIAudioSourceStream *self) {
  return self->open();
}

#endif  // defined(Q_OS_WIN)
