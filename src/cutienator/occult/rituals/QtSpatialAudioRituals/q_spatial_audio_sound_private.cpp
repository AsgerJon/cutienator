//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qspatialaudiosound_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qtspatialaudioglobal_p.h>
#include <QtSpatialAudio/QtSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/6.12.0/QtSpatialAudio/private/qspatialaudiosound_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSpatialAudio/private/qspatialaudiosound_p.h>
#include <QtMultimedia/qaudiosink.h>
#include <QtMultimedia/private/qaudio_qspan_support_p.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#include <QtMultimedia/private/qmultimediautils_p.h>
#include <QtMultimedia/private/qmultimedia_ranges_p.h>
#include <QtSpatialAudio/private/qaudioengine_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qurl.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 289, as _ZN25QSpatialAudioSoundPrivate8setStateESt10shared_ptrIN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateEE
inline void QSpatialAudioSoundPrivate::setState(SharedPlaybackState state)
{
    auto *ep = QAudioEnginePrivate::get(engine);
    if (ep)
        ep->setSoundPlaybackData(this, state);
    m_playbackState = std::move(state);
}

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 122, as _ZN25QSpatialAudioSoundPrivate9setVolumeEf
inline void QSpatialAudioSoundPrivate::setVolume(float volume)
{
    m_volume = volume;
    applyVolume();
}

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 135, as _ZN25QSpatialAudioSoundPrivate11setAutoPlayEb
inline void QSpatialAudioSoundPrivate::setAutoPlay(bool enabled)
{
    m_autoPlay = enabled;
}

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 193, as _ZN25QSpatialAudioSoundPrivate4stopEv
inline void QSpatialAudioSoundPrivate::stop()
{
    qCDebug(qLcSpatialAudioEngine) << "Stopping sound";
    switch (m_state) {
    case State::Stopped: {
        return;
    }
    case State::Paused:
    case State::Playing: {
        m_state = State::Stopped;
        setState({});
        return;
    }
    }
}
//  -----------------------------------------------------------------------

//  A QSpatialAudioSoundPrivate that Python can take functions over in. Every QSpatialAudioSoundPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSpatialAudioSoundPrivateCall0)(const void *, int *);
typedef void (*CuteQSpatialAudioSoundPrivateCall1)(const void *, int *);
class CuteQSpatialAudioSoundPrivate : public QSpatialAudioSoundPrivate {
public:
  using QSpatialAudioSoundPrivate::QSpatialAudioSoundPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QSpatialAudioSoundPrivate17updateRoomEffectsEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSpatialAudioSoundPrivate11applyVolumeEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QSpatialAudioSoundPrivate::updateRoomEffects()
  void updateRoomEffects() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSpatialAudioSoundPrivateCall0 call = reinterpret_cast<CuteQSpatialAudioSoundPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSpatialAudioSoundPrivate::updateRoomEffects();
  }

  //  void QSpatialAudioSoundPrivate::applyVolume()
  void applyVolume() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSpatialAudioSoundPrivateCall1 call = reinterpret_cast<CuteQSpatialAudioSoundPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSpatialAudioSoundPrivate::applyVolume();
  }
};

//  QUrl QSpatialAudioSoundPrivate::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK25QSpatialAudioSoundPrivate3urlEv(
    const QSpatialAudioSoundPrivate *self) {
  return new QUrl(self->url());
}

//  void QSpatialAudioSoundPrivate::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate9setVolumeEf(
    QSpatialAudioSoundPrivate *self,
    float volume) {
  self->setVolume(volume);
}

//  float QSpatialAudioSoundPrivate::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK25QSpatialAudioSoundPrivate6volumeEv(
    const QSpatialAudioSoundPrivate *self) {
  return self->volume();
}

//  int QSpatialAudioSoundPrivate::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QSpatialAudioSoundPrivate5loopsEv(
    const QSpatialAudioSoundPrivate *self) {
  return self->loops();
}

//  bool QSpatialAudioSoundPrivate::autoPlay() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSpatialAudioSoundPrivate8autoPlayEv(
    const QSpatialAudioSoundPrivate *self) {
  return self->autoPlay();
}

//  void QSpatialAudioSoundPrivate::setAutoPlay(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate11setAutoPlayEb(
    QSpatialAudioSoundPrivate *self,
    bool a0) {
  self->setAutoPlay(a0);
}

//  void QSpatialAudioSoundPrivate::updateRoomEffects()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate17updateRoomEffectsEv(
    QSpatialAudioSoundPrivate *self) {
  self->updateRoomEffects();
}

//  void QSpatialAudioSoundPrivate::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate4stopEv(
    QSpatialAudioSoundPrivate *self) {
  self->stop();
}

//  State QSpatialAudioSoundPrivate::state() const
extern "C" Q_DECL_EXPORT
QSpatialAudioSoundPrivate::State ritual_ZNK25QSpatialAudioSoundPrivate5stateEv(
    const QSpatialAudioSoundPrivate *self) {
  return self->state();
}

//  void QSpatialAudioSoundPrivate::applyVolume()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate11applyVolumeEv(
    QSpatialAudioSoundPrivate *self) {
  self->applyVolume();
}

//  a Python function taken by a CuteQSpatialAudioSoundPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpatialAudioSoundPrivate(
    QSpatialAudioSoundPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSpatialAudioSoundPrivate *>(self)->take(key, call);
}

//  void QSpatialAudioSoundPrivate::updateRoomEffects()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSpatialAudioSoundPrivate17updateRoomEffectsEv(
    QSpatialAudioSoundPrivate *self) {
  self->QSpatialAudioSoundPrivate::updateRoomEffects();
}
