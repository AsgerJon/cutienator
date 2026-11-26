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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 24, as _ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateC1E12QAudioBufferbi
namespace QSpatialAudioPrivate {
inline QSpatialAudioPlaybackState::QSpatialAudioPlaybackState(QAudioBuffer buffer, bool playing, int loops)
    : m_playing(playing), m_loops(loops), m_buffer(std::move(buffer))
{
}
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 85, as _ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState8setLoopsEi
namespace QSpatialAudioPrivate {
inline void QSpatialAudioPlaybackState::setLoops(int loops)
{
    m_loops = loops;
}
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 80, as _ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState6resumeEv
namespace QSpatialAudioPrivate {
inline void QSpatialAudioPlaybackState::resume()
{
    m_playing = true;
}
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 95, as _ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState5pauseEv
namespace QSpatialAudioPrivate {
inline void QSpatialAudioPlaybackState::pause()
{
    m_playing = false;
}
}  // namespace QSpatialAudioPrivate

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 209, as _ZN25QSpatialAudioSoundPrivate7loadUrlERK4QUrl
inline void QSpatialAudioSoundPrivate::loadUrl(const QUrl &url)
{
    qCDebug(qLcSpatialAudioEngine) << "Loading sound:" << url;
    m_url = url;

    auto *ep = QAudioEnginePrivate::get(engine);
    if (!ep)
        return;

    m_loadFuture.cancelChain();
    m_sample = {};

    setState(nullptr);

    m_loadFuture = QSampleCache::instance()
                           ->requestSampleFuture(m_sourceResolver->resolve(url), ep->sampleRate())
                           .then(q_ptr, [this](SharedSamplePtr sample) {
        if (!sample) {
            qCWarning(qLcSpatialAudioEngine) << "QAmbientSound: cannot load file";
            return;
        }

        // Build QAudioBuffer with the correct channel layout for this source.
        // QSampleCache resampled to engineRate but preserves native channels.
        // Adapt channel count here: mono<->stereo simple mix.
        const QAudioFormat &srcFmt = sample->format();
        const int srcChannels = srcFmt.channelCount();

        QByteArray pcmData;
        QAudioFormat outFmt = srcFmt;
        outFmt.setChannelCount(nchannels);
        outFmt.setChannelConfig(nchannels == 2 ? QAudioFormat::ChannelConfigStereo
                                               : QAudioFormat::ChannelConfigMono);

        using namespace QAudioHelperInternal;

        if (srcChannels == nchannels) {
            pcmData = sample->data();

            m_sample = std::move(sample); // keep the sample in the QSampleCache as long as we live
        } else if (srcChannels == 1 && nchannels == 2) {
            qWarning() << "QAmbientSound: upmixing mono source to stereo";
            pcmData = upmixMonoToStereo(sample->dataAsFloatSpan(), UpmixScaling::Duplicate);
        } else if (srcChannels == 2 && nchannels == 1) {
            qWarning() << "QAmbientSound: downmixing stereo source to mono";
            pcmData = downmixStereoToMono(sample->dataAsFloatSpan(), DownmixScaling::Average);
        } else {
            qWarning() << "QAmbientSound: unsupported channel count"
                       << srcChannels << "- rejecting file";
            return;
        }

        m_buffer = QAudioBuffer{
            pcmData,
            outFmt,
        };

        qCDebug(qLcSpatialAudioEngine) << "Sound loaded";

        const bool startingPlayback = m_autoPlay || m_state != State::Stopped;
        if (!startingPlayback)
            return;
        const bool startPaused = (m_state == State::Paused) && !m_autoPlay;
        setState(std::make_shared<QSpatialAudioPlaybackState>(*m_buffer, /*playing=*/!startPaused,
                                                              m_loops));

        m_state = startPaused ? State::Paused : State::Playing;
        qCDebug(qLcSpatialAudioEngine)
                << "Sound playback started:" << (startPaused ? "paused" : "playing");
    });
}

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 122, as _ZN25QSpatialAudioSoundPrivate9setVolumeEf
inline void QSpatialAudioSoundPrivate::setVolume(float volume)
{
    m_volume = volume;
    applyVolume();
}

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 128, as _ZN25QSpatialAudioSoundPrivate8setLoopsEi
inline void QSpatialAudioSoundPrivate::setLoops(int loops)
{
    m_loops = loops;
    if (m_playbackState)
        m_playbackState->setLoops(loops);
}

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 135, as _ZN25QSpatialAudioSoundPrivate11setAutoPlayEb
inline void QSpatialAudioSoundPrivate::setAutoPlay(bool enabled)
{
    m_autoPlay = enabled;
}

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 147, as _ZN25QSpatialAudioSoundPrivate4playEv
inline void QSpatialAudioSoundPrivate::play()
{
    qCDebug(qLcSpatialAudioEngine) << "Playing sound";
    switch (m_state) {
    case State::Stopped: {
        m_state = State::Playing;
        if (m_buffer) {
            setState(std::make_shared<QSpatialAudioPlaybackState>(*m_buffer, /*playing=*/true,
                                                                  m_loops));
        }
        return;
    }
    case State::Paused:
    case State::Playing: {
        m_state = State::Playing;
        if (m_playbackState)
            m_playbackState->resume();
        return;
    }
    }
}

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 169, as _ZN25QSpatialAudioSoundPrivate5pauseEv
inline void QSpatialAudioSoundPrivate::pause()
{
    qCDebug(qLcSpatialAudioEngine) << "Pausing sound";
    switch (m_state) {
    case State::Stopped: {
        m_state = State::Paused;
        setState(std::make_shared<QSpatialAudioPlaybackState>(*m_buffer, /*playing=*/false,
                                                              m_loops));
        return;
    }
    case State::Paused: {
        return;
    }
    case State::Playing: {
        m_state = State::Paused;
        setState(nullptr);

        if (m_playbackState)
            m_playbackState->pause();
        return;
    }
    }
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

//  from ../qtmultimedia/src/spatialaudio/qspatialaudiosound.cpp, line 289, as _ZN25QSpatialAudioSoundPrivate8setStateESt10shared_ptrIN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateEE
inline void QSpatialAudioSoundPrivate::setState(SharedPlaybackState state)
{
    auto *ep = QAudioEnginePrivate::get(engine);
    if (ep)
        ep->setSoundPlaybackData(this, state);
    m_playbackState = std::move(state);
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

//  void QSpatialAudioSoundPrivate::loadUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate7loadUrlERK4QUrl(
    QSpatialAudioSoundPrivate *self,
    const QUrl *url) {
  self->loadUrl(*url);
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

//  void QSpatialAudioSoundPrivate::setLoops(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate8setLoopsEi(
    QSpatialAudioSoundPrivate *self,
    int a0) {
  self->setLoops(a0);
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

//  void QSpatialAudioSoundPrivate::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate4playEv(
    QSpatialAudioSoundPrivate *self) {
  self->play();
}

//  void QSpatialAudioSoundPrivate::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate5pauseEv(
    QSpatialAudioSoundPrivate *self) {
  self->pause();
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

//  void QSpatialAudioSoundPrivate::setState(SharedPlaybackState a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSpatialAudioSoundPrivate8setStateESt10shared_ptrIN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateEE(
    QSpatialAudioSoundPrivate *self,
    const QSpatialAudioSoundPrivate::SharedPlaybackState *a0) {
  self->setState(*a0);
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
