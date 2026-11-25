//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaaudiosource_p.h, Qt
//  6.12.0, as the Qt of macOS installs it. Kept as it is when the generator
//  runs again.
//  Qt's library offers nothing of this class by name: only its virtual
//  functions are called, through the object, and what its header writes out.
//  It is final, so 'self' is taken as a QPlatformAudioSource for those, and
//  the calls stay virtual. Not written: the constructor and
//  'resumeStreamIfNecessary', which Qt's library offers not.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcoreaaudiosource_p.h>

//  QCoreAudioSource::~QCoreAudioSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreAudioSourceD1Ev(QPlatformAudioSource *self) {
  delete self;
}

#if !defined(Q_OS_MACOS)
//  void QCoreAudioSource::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreAudioSource6resumeEv(QPlatformAudioSource *self) {
  self->resume();
}
#endif  // !defined(Q_OS_MACOS)

#if !defined(Q_OS_MACOS)
//  QCoreAudioSourceStream *QCoreAudioSource::currentStream() const
extern "C" Q_DECL_EXPORT
QCoreAudioSourceStream *ritual_ZNK16QCoreAudioSource13currentStreamEv(
    const QCoreAudioSource *self) {
  return self->currentStream();
}
#endif  // !defined(Q_OS_MACOS)

#if !defined(Q_OS_MACOS)
//  void QCoreAudioSource::notifyStreamStopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCoreAudioSource19notifyStreamStoppedEv(
    QCoreAudioSource *self) {
  self->notifyStreamStopped();
}
#endif  // !defined(Q_OS_MACOS)

#endif  // defined(Q_OS_DARWIN)
