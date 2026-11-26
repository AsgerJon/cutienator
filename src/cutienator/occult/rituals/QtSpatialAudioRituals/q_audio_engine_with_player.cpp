//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_withplayer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qtspatialaudioglobal_p.h>
#include <QtSpatialAudio/QtSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_withplayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/qaudioengine.h>
#include <QtSpatialAudio/private/qaudioengine_p.h>
#include <QtMultimedia/private/qmultimedia_ranges_p.h>
#include <QtSpatialAudio/private/qaudioengine_threaded_p.h>
#include <QtSpatialAudio/private/qaudioengine_withplayer_p.h>
#include <QtCore/qspan.h>
#include <QtMultimedia/qaudiosink.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/private/qaudiosystem_p.h>
#include <QtMultimedia/private/qplatformaudiodevices_p.h>
#include <QtMultimedia/private/qplatformmediaintegration_p.h>
#include <QtCore/q20vector.h>
#include <QtSpatialAudio/private/qaudioengine_withplayer_p.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/private/qmemory_resource_tlsf_p.h>
#include <QtMultimedia/private/qmultimedia_ranges_p.h>
#include <QtMultimedia/private/qrtaudioengine_p.h>
#include <QtMultimedia/private/qtmm_pmr_p.h>
#include <QtSpatialAudio/private/qambisonicdecoder_p.h>
#include <QtSpatialAudio/private/qspatialaudiosound_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudio/qaudioengine.cpp, line 37, as _ZN19QAudioEnginePrivateD2Ev
inline QAudioEnginePrivate::~QAudioEnginePrivate() = default;

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_withplayer.cpp, line 311, as _ZN22QAudioEngineWithPlayer4stopEv
inline void QAudioEngineWithPlayer::stop()
{
    if (!m_engineVoice)
        return;
    m_playbackEngine->stop(m_engineVoice);
    m_engineVoice = {};
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_withplayer.cpp, line 335, as _ZNK22QAudioEngineWithPlayer8isPausedEv
inline bool QAudioEngineWithPlayer::isPaused() const
{
    return m_paused;
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_withplayer.cpp, line 340, as _ZN22QAudioEngineWithPlayer15setOutputDeviceERK12QAudioDevice
inline void QAudioEngineWithPlayer::setOutputDevice(const QAudioDevice &device)
{
    if (m_device == device)
        return;
    if (m_engineVoice) {
        qWarning() << "Changing device on a running engine not implemented";
        return;
    }
    m_device = device;
    Q_Q(QAudioEngine);
    emit q->outputDeviceChanged();
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_withplayer.cpp, line 353, as _ZNK22QAudioEngineWithPlayer12outputDeviceEv
inline QAudioDevice QAudioEngineWithPlayer::outputDevice() const
{
    return m_device;
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_withplayer.cpp, line 421, as _ZN22QAudioEngineWithPlayer17updateRoomEffectsEv
inline void QAudioEngineWithPlayer::updateRoomEffects()
{
    for (auto [sound, key] : playbackStates)
        sound->updateRoomEffects();
}
//  -----------------------------------------------------------------------

//  void QAudioEngineWithPlayer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAudioEngineWithPlayer4stopEv(QAudioEngineWithPlayer *self) {
  self->stop();
}

//  bool QAudioEngineWithPlayer::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QAudioEngineWithPlayer8isPausedEv(
    const QAudioEngineWithPlayer *self) {
  return self->isPaused();
}

//  void QAudioEngineWithPlayer::setOutputDevice(const QAudioDevice &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAudioEngineWithPlayer15setOutputDeviceERK12QAudioDevice(
    QAudioEngineWithPlayer *self,
    const QAudioDevice *device) {
  self->setOutputDevice(*device);
}

//  QAudioDevice QAudioEngineWithPlayer::outputDevice() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK22QAudioEngineWithPlayer12outputDeviceEv(
    const QAudioEngineWithPlayer *self) {
  return new QAudioDevice(self->outputDevice());
}

//  void QAudioEngineWithPlayer::updateRoomEffects()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAudioEngineWithPlayer17updateRoomEffectsEv(
    QAudioEngineWithPlayer *self) {
  self->updateRoomEffects();
}

//  QAudioFormat QAudioEngineWithPlayer::audioFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK22QAudioEngineWithPlayer11audioFormatEv(
    const QAudioEngineWithPlayer *self) {
  return new QAudioFormat(self->audioFormat());
}
