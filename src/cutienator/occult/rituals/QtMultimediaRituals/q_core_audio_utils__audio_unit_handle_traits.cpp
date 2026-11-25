//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudioutils_p.h, Qt 6.12.0,
//  as the Qt of macOS installs it. Kept as it is when the generator runs
//  again.
//  An 'AudioUnit' is passed as an address. Not written: 'close', which calls
//  AudioToolbox, a library outside Qt.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudioutils_p.h>

//  Type QCoreAudioUtils::AudioUnitHandleTraits::invalidValue()
extern "C" Q_DECL_EXPORT
AudioUnit ritual_ZN15QCoreAudioUtils21AudioUnitHandleTraits12invalidValueEv() {
  return QCoreAudioUtils::AudioUnitHandleTraits::invalidValue();
}

//  QCoreAudioUtils::AudioUnitHandleTraits::~AudioUnitHandleTraits()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoreAudioUtils21AudioUnitHandleTraitsD1Ev(
    QCoreAudioUtils::AudioUnitHandleTraits *self) {
  delete self;
}

#endif  // defined(Q_OS_DARWIN)
