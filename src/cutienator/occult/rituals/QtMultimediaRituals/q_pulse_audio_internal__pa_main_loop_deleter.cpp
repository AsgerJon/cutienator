//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qpulsehelpers_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands also under
//  '__has_include(<pulse/pulseaudio.h>)', because Qt's header it needs
//  includes the header of PulseAudio, which a machine with Qt's kit but
//  without the development headers of PulseAudio lacks. Kept as it is when
//  the generator runs again.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(pulseaudio) && __has_include(<pulse/pulseaudio.h>)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qpulsehelpers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPulseAudioInternal::PaMainLoopDeleter::~PaMainLoopDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPulseAudioInternal17PaMainLoopDeleterD1Ev(
    QPulseAudioInternal::PaMainLoopDeleter *self) {
  delete self;
}

#endif  // QT_CONFIG(pulseaudio) && __has_include(<pulse/pulseaudio.h>)
