//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudioutils_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudioutils_p.h>
#include <audioclient.h>

//  QWindowsAudioUtils::AudioClientCreationResult::~AudioClientCreationResult
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsAudioUtils25AudioClientCreationResultD1Ev(
    QWindowsAudioUtils::AudioClientCreationResult *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
