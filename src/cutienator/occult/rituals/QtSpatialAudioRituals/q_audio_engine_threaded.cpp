//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_threaded_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qtspatialaudioglobal_p.h>
#include <QtSpatialAudio/QtSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_threaded_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qaudioengine_threaded_p.h"
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/qaudiosink.h>
#include <QtMultimedia/private/qaudio_qspan_support_p.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#ifdef Q_OS_WIN
#  include <QtMultimedia/private/qwindows_wasapi_warmup_client_p.h>
#endif
#include <QtSpatialAudio/qambientsound.h>
#include <QtSpatialAudio/qaudiolistener.h>
#include <QtSpatialAudio/private/qambisonicdecoder_p.h>
#include <QtSpatialAudio/private/qspatialaudiosound_p.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qdebug.h>
#include <QtCore/qelapsedtimer.h>
#include <memory>
#include <q20vector.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 271, as _ZNK20QAudioEngineThreaded8isPausedEv
inline bool QAudioEngineThreaded::isPaused() const
{
    return m_paused.loadRelaxed();
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 276, as _ZN20QAudioEngineThreaded15setOutputDeviceERK12QAudioDevice
inline void QAudioEngineThreaded::setOutputDevice(const QAudioDevice &device)
{
    if (m_device == device)
        return;
    if (outputStream) {
        qWarning() << "Changing device on a running engine not implemented";
        return;
    }
    m_device = device;
    Q_Q(QAudioEngine);
    emit q->outputDeviceChanged();
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 289, as _ZN20QAudioEngineThreaded8addSoundEP25QSpatialAudioSoundPrivate
inline void QAudioEngineThreaded::addSound(QSpatialAudioSoundPrivate *sound)
{
    std::lock_guard l(mutex);
    playbackStates.emplace(sound, nullptr);
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 295, as _ZN20QAudioEngineThreaded11removeSoundEP25QSpatialAudioSoundPrivate
inline void QAudioEngineThreaded::removeSound(QSpatialAudioSoundPrivate *sound)
{
    std::lock_guard l(mutex);
    playbackStates.erase(sound);
}

//  from ../qtmultimedia/src/spatialaudio/qaudioengine_threaded.cpp, line 308, as _ZN20QAudioEngineThreaded17updateRoomEffectsEv
inline void QAudioEngineThreaded::updateRoomEffects()
{
    std::lock_guard l(mutex);
    for (auto [sound, key] : playbackStates)
        sound->updateRoomEffects();
}
//  -----------------------------------------------------------------------

//  bool QAudioEngineThreaded::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAudioEngineThreaded8isPausedEv(
    const QAudioEngineThreaded *self) {
  return self->isPaused();
}

//  void QAudioEngineThreaded::setOutputDevice(const QAudioDevice &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioEngineThreaded15setOutputDeviceERK12QAudioDevice(
    QAudioEngineThreaded *self,
    const QAudioDevice *device) {
  self->setOutputDevice(*device);
}

//  QAudioDevice QAudioEngineThreaded::outputDevice() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK20QAudioEngineThreaded12outputDeviceEv(
    const QAudioEngineThreaded *self) {
  return new QAudioDevice(self->outputDevice());
}

//  void QAudioEngineThreaded::addSound(QSpatialAudioSoundPrivate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioEngineThreaded8addSoundEP25QSpatialAudioSoundPrivate(
    QAudioEngineThreaded *self,
    QSpatialAudioSoundPrivate *a0) {
  self->addSound(a0);
}

//  void QAudioEngineThreaded::removeSound(QSpatialAudioSoundPrivate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioEngineThreaded11removeSoundEP25QSpatialAudioSoundPrivate(
    QAudioEngineThreaded *self,
    QSpatialAudioSoundPrivate *a0) {
  self->removeSound(a0);
}

//  void QAudioEngineThreaded::updateRoomEffects()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioEngineThreaded17updateRoomEffectsEv(
    QAudioEngineThreaded *self) {
  self->updateRoomEffects();
}
