//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaaudiosink_p.h, Qt 6.12.0,
//  as the Qt of macOS installs it. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its virtual
//  functions are called, through the object, and what its header writes out.
//  It is final, so 'self' is taken as a QPlatformAudioSink for those, and
//  the calls stay virtual. Not written: the constructor and
//  'resumeStreamIfNecessary', which Qt's library offers not.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcoreaaudiosink_p.h>

//  QCoreAudioSink::~QCoreAudioSink()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCoreAudioSinkD1Ev(QPlatformAudioSink *self) {
  delete self;
}

#if !defined(Q_OS_MACOS)
//  void QCoreAudioSink::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCoreAudioSink6resumeEv(QPlatformAudioSink *self) {
  self->resume();
}
#endif  // !defined(Q_OS_MACOS)

#if !defined(Q_OS_MACOS)
//  QCoreAudioSinkStream *QCoreAudioSink::currentStream() const
extern "C" Q_DECL_EXPORT
QCoreAudioSinkStream *ritual_ZNK14QCoreAudioSink13currentStreamEv(
    const QCoreAudioSink *self) {
  return self->currentStream();
}
#endif  // !defined(Q_OS_MACOS)

#if !defined(Q_OS_MACOS)
//  void QCoreAudioSink::notifyStreamStopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCoreAudioSink19notifyStreamStoppedEv(QCoreAudioSink *self) {
  self->notifyStreamStopped();
}
#endif  // !defined(Q_OS_MACOS)

#endif  // defined(Q_OS_DARWIN)
