//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiodevices_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(qnx_io_snd)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiodevices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>

//  QLatin1String QQnxSndAudioDevices::backendName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK19QQnxSndAudioDevices11backendNameEv(
    const QQnxSndAudioDevices *self) {
  return new QLatin1String(self->backendName());
}

//  bool QQnxSndAudioDevices::hasCallbackApi() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQnxSndAudioDevices14hasCallbackApiEv(
    const QQnxSndAudioDevices *self) {
  return self->hasCallbackApi();
}

#endif  // QT_CONFIG(qnx_io_snd)
