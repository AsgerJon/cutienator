//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaaudiosink_p.h, Qt 6.12.0,
//  as the Qt of macOS installs it. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its virtual
//  function is called, through the object. It is final, so 'self' is taken
//  as a QtMultimediaPrivate::QPlatformAudioSinkStream, and the call stays
//  virtual. Not written: the constructor, the destructor, 'open', 'start',
//  'stop', 'suspend', 'resume' and the others its header declares, which
//  Qt's library offers not.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcoreaaudiosink_p.h>

//  void QCoreAudioSinkStream::updateStreamIdle(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoreAudioSinkStream16updateStreamIdleEb(
    QtMultimediaPrivate::QPlatformAudioSinkStream *self,
    bool arg) {
  self->updateStreamIdle(arg);
}

#endif  // defined(Q_OS_DARWIN)
