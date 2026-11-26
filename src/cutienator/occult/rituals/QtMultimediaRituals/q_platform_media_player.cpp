//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaplayer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaplayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qmediatimerange.h>
#include <QtCore/qurl.h>
#include <QtMultimedia/qmediametadata.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qplaybackoptions.h>
#include <cstring>

//  A QPlatformMediaPlayer that Python can take functions over in. Every QPlatformMediaPlayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQPlatformMediaPlayerCall0)(const void *, int *);
typedef qint64 (*CuteQPlatformMediaPlayerCall1)(const void *, int *);
typedef void (*CuteQPlatformMediaPlayerCall2)(const void *, qint64, int *);
typedef float (*CuteQPlatformMediaPlayerCall3)(const void *, int *);
typedef bool (*CuteQPlatformMediaPlayerCall4)(const void *, int *);
typedef bool (*CuteQPlatformMediaPlayerCall5)(const void *, int *);
typedef bool (*CuteQPlatformMediaPlayerCall6)(const void *, int *);
typedef const QMediaTimeRange * (*CuteQPlatformMediaPlayerCall7)(const void *, int *);
typedef qreal (*CuteQPlatformMediaPlayerCall8)(const void *, int *);
typedef void (*CuteQPlatformMediaPlayerCall9)(const void *, qreal, int *);
typedef const QUrl * (*CuteQPlatformMediaPlayerCall10)(const void *, int *);
typedef void * (*CuteQPlatformMediaPlayerCall11)(const void *, int *);
typedef void (*CuteQPlatformMediaPlayerCall12)(const void *, const QUrl *, QIODevice *, int *);
typedef void (*CuteQPlatformMediaPlayerCall13)(const void *, int *);
typedef void (*CuteQPlatformMediaPlayerCall14)(const void *, int *);
typedef void (*CuteQPlatformMediaPlayerCall15)(const void *, int *);
typedef bool (*CuteQPlatformMediaPlayerCall16)(const void *, int *);
typedef void (*CuteQPlatformMediaPlayerCall17)(const void *, QPlatformAudioOutput *, int *);
typedef void (*CuteQPlatformMediaPlayerCall18)(const void *, QAudioBufferOutput *, int *);
typedef const QMediaMetaData * (*CuteQPlatformMediaPlayerCall19)(const void *, int *);
typedef void (*CuteQPlatformMediaPlayerCall20)(const void *, QVideoSink *, int *);
typedef bool (*CuteQPlatformMediaPlayerCall21)(const void *, int *);
typedef int (*CuteQPlatformMediaPlayerCall22)(const void *, int, int *);
typedef const QMediaMetaData * (*CuteQPlatformMediaPlayerCall23)(const void *, int, int, int *);
typedef int (*CuteQPlatformMediaPlayerCall24)(const void *, int, int *);
typedef void (*CuteQPlatformMediaPlayerCall25)(const void *, int, int, int *);
typedef void (*CuteQPlatformMediaPlayerCall26)(const void *, int, int *);
typedef int (*CuteQPlatformMediaPlayerCall27)(const void *, int *);
typedef void (*CuteQPlatformMediaPlayerCall28)(const void *, bool, int *);
typedef bool (*CuteQPlatformMediaPlayerCall29)(const void *, int *);
class CuteQPlatformMediaPlayer : public QPlatformMediaPlayer {
public:
  using QPlatformMediaPlayer::QPlatformMediaPlayer;
  void *taken[30] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer8durationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer8positionEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer11setPositionEx")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer14bufferProgressEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer16isAudioAvailableEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer16isVideoAvailableEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer10isSeekableEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer23availablePlaybackRangesEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer12playbackRateEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer15setPlaybackRateEd")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer5mediaEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer11mediaStreamEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer8setMediaERK4QUrlP9QIODevice")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer4playEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer5pauseEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer4stopEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer23streamPlaybackSupportedEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer14setAudioOutputEP20QPlatformAudioOutput")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer20setAudioBufferOutputEP18QAudioBufferOutput")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer8metaDataEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer12setVideoSinkEP10QVideoSink")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer10canPlayQrcEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer10trackCountENS_9TrackTypeE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer13trackMetaDataENS_9TrackTypeEi")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer11activeTrackENS_9TrackTypeE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer14setActiveTrackENS_9TrackTypeEi")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer8setLoopsEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer29pitchCompensationAvailabilityEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlayer20setPitchCompensationEb")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformMediaPlayer17pitchCompensationEv")) {
      taken[29] = call;
      return true;
    }
    return false;
  }

  //  qint64 QPlatformMediaPlayer::duration() const
  qint64 duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall0 call = reinterpret_cast<CuteQPlatformMediaPlayerCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QPlatformMediaPlayer::position() const
  qint64 position() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall1 call = reinterpret_cast<CuteQPlatformMediaPlayerCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMediaPlayer::position();
  }

  //  void QPlatformMediaPlayer::setPosition(qint64 position)
  void setPosition(qint64 position) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall2 call = reinterpret_cast<CuteQPlatformMediaPlayerCall2>(taken[2]);
      call(this, position, &handled);
      if (handled) return;
    }
  }

  //  float QPlatformMediaPlayer::bufferProgress() const
  float bufferProgress() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall3 call = reinterpret_cast<CuteQPlatformMediaPlayerCall3>(taken[3]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QPlatformMediaPlayer::isAudioAvailable() const
  bool isAudioAvailable() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall4 call = reinterpret_cast<CuteQPlatformMediaPlayerCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMediaPlayer::isAudioAvailable();
  }

  //  bool QPlatformMediaPlayer::isVideoAvailable() const
  bool isVideoAvailable() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall5 call = reinterpret_cast<CuteQPlatformMediaPlayerCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMediaPlayer::isVideoAvailable();
  }

  //  bool QPlatformMediaPlayer::isSeekable() const
  bool isSeekable() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall6 call = reinterpret_cast<CuteQPlatformMediaPlayerCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMediaPlayer::isSeekable();
  }

  //  QMediaTimeRange QPlatformMediaPlayer::availablePlaybackRanges() const
  QMediaTimeRange availablePlaybackRanges() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall7 call = reinterpret_cast<CuteQPlatformMediaPlayerCall7>(taken[7]);
      const QMediaTimeRange * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  qreal QPlatformMediaPlayer::playbackRate() const
  qreal playbackRate() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall8 call = reinterpret_cast<CuteQPlatformMediaPlayerCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPlatformMediaPlayer::setPlaybackRate(qreal rate)
  void setPlaybackRate(qreal rate) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall9 call = reinterpret_cast<CuteQPlatformMediaPlayerCall9>(taken[9]);
      call(this, rate, &handled);
      if (handled) return;
    }
  }

  //  QUrl QPlatformMediaPlayer::media() const
  QUrl media() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall10 call = reinterpret_cast<CuteQPlatformMediaPlayerCall10>(taken[10]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  const QIODevice *QPlatformMediaPlayer::mediaStream() const
  const QIODevice *mediaStream() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall11 call = reinterpret_cast<CuteQPlatformMediaPlayerCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QIODevice *>(given);
    }
    return {};
  }

  //  void QPlatformMediaPlayer::setMedia(const QUrl &media, QIODevice
  //      *stream)
  void setMedia(const QUrl &media, QIODevice *stream) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall12 call = reinterpret_cast<CuteQPlatformMediaPlayerCall12>(taken[12]);
      call(this, &media, stream, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformMediaPlayer::play()
  void play() override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall13 call = reinterpret_cast<CuteQPlatformMediaPlayerCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformMediaPlayer::pause()
  void pause() override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall14 call = reinterpret_cast<CuteQPlatformMediaPlayerCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformMediaPlayer::stop()
  void stop() override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall15 call = reinterpret_cast<CuteQPlatformMediaPlayerCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QPlatformMediaPlayer::streamPlaybackSupported() const
  bool streamPlaybackSupported() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall16 call = reinterpret_cast<CuteQPlatformMediaPlayerCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMediaPlayer::streamPlaybackSupported();
  }

  //  void QPlatformMediaPlayer::setAudioOutput(QPlatformAudioOutput *a0)
  void setAudioOutput(QPlatformAudioOutput *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall17 call = reinterpret_cast<CuteQPlatformMediaPlayerCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaPlayer::setAudioOutput(a0);
  }

  //  void QPlatformMediaPlayer::setAudioBufferOutput(QAudioBufferOutput
  //      *a0)
  void setAudioBufferOutput(QAudioBufferOutput *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall18 call = reinterpret_cast<CuteQPlatformMediaPlayerCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformMediaPlayer::setAudioBufferOutput(a0);
  }

  //  QMediaMetaData QPlatformMediaPlayer::metaData() const
  QMediaMetaData metaData() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall19 call = reinterpret_cast<CuteQPlatformMediaPlayerCall19>(taken[19]);
      const QMediaMetaData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformMediaPlayer::metaData();
  }

  //  void QPlatformMediaPlayer::setVideoSink(QVideoSink *a0)
  void setVideoSink(QVideoSink *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall20 call = reinterpret_cast<CuteQPlatformMediaPlayerCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QPlatformMediaPlayer::canPlayQrc() const
  bool canPlayQrc() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall21 call = reinterpret_cast<CuteQPlatformMediaPlayerCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMediaPlayer::canPlayQrc();
  }

  //  int QPlatformMediaPlayer::trackCount(TrackType a0)
  int trackCount(QPlatformMediaPlayer::TrackType a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall22 call = reinterpret_cast<CuteQPlatformMediaPlayerCall22>(taken[22]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QPlatformMediaPlayer::trackCount(a0);
  }

  //  QMediaMetaData QPlatformMediaPlayer::trackMetaData(TrackType a0, int
  //      a1)
  QMediaMetaData trackMetaData(
      QPlatformMediaPlayer::TrackType a0,
      int a1) override {
    if (taken[23]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall23 call = reinterpret_cast<CuteQPlatformMediaPlayerCall23>(taken[23]);
      const QMediaMetaData * given = call(this, static_cast<int>(a0), a1, &handled);
      if (handled && given) return *given;
    }
    return QPlatformMediaPlayer::trackMetaData(a0, a1);
  }

  //  int QPlatformMediaPlayer::activeTrack(TrackType a0)
  int activeTrack(QPlatformMediaPlayer::TrackType a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall24 call = reinterpret_cast<CuteQPlatformMediaPlayerCall24>(taken[24]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QPlatformMediaPlayer::activeTrack(a0);
  }

  //  void QPlatformMediaPlayer::setActiveTrack(TrackType a0, int a1)
  void setActiveTrack(QPlatformMediaPlayer::TrackType a0, int a1) override {
    if (taken[25]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall25 call = reinterpret_cast<CuteQPlatformMediaPlayerCall25>(taken[25]);
      call(this, static_cast<int>(a0), a1, &handled);
      if (handled) return;
    }
    QPlatformMediaPlayer::setActiveTrack(a0, a1);
  }

  //  void QPlatformMediaPlayer::setLoops(int loops)
  void setLoops(int loops) override {
    if (taken[26]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall26 call = reinterpret_cast<CuteQPlatformMediaPlayerCall26>(taken[26]);
      call(this, loops, &handled);
      if (handled) return;
    }
    QPlatformMediaPlayer::setLoops(loops);
  }

  //  PitchCompensationAvailability
  //      QPlatformMediaPlayer::pitchCompensationAvailability() const
  QPlatformMediaPlayer::PitchCompensationAvailability pitchCompensationAvailability() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall27 call = reinterpret_cast<CuteQPlatformMediaPlayerCall27>(taken[27]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlatformMediaPlayer::PitchCompensationAvailability>(given);
    }
    return QPlatformMediaPlayer::pitchCompensationAvailability();
  }

  //  void QPlatformMediaPlayer::setPitchCompensation(bool enabled)
  void setPitchCompensation(bool enabled) override {
    if (taken[28]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall28 call = reinterpret_cast<CuteQPlatformMediaPlayerCall28>(taken[28]);
      call(this, enabled, &handled);
      if (handled) return;
    }
    QPlatformMediaPlayer::setPitchCompensation(enabled);
  }

  //  bool QPlatformMediaPlayer::pitchCompensation() const
  bool pitchCompensation() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQPlatformMediaPlayerCall29 call = reinterpret_cast<CuteQPlatformMediaPlayerCall29>(taken[29]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMediaPlayer::pitchCompensation();
  }
};

//  QPlatformMediaPlayer::~QPlatformMediaPlayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayerD1Ev(QPlatformMediaPlayer *self) {
  delete self;
}

//  QMediaPlayer::PlaybackState QPlatformMediaPlayer::state() const
extern "C" Q_DECL_EXPORT
QMediaPlayer::PlaybackState ritual_ZNK20QPlatformMediaPlayer5stateEv(
    const QPlatformMediaPlayer *self) {
  return self->state();
}

//  QMediaPlayer::MediaStatus QPlatformMediaPlayer::mediaStatus() const
extern "C" Q_DECL_EXPORT
QMediaPlayer::MediaStatus ritual_ZNK20QPlatformMediaPlayer11mediaStatusEv(
    const QPlatformMediaPlayer *self) {
  return self->mediaStatus();
}

//  qint64 QPlatformMediaPlayer::duration() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QPlatformMediaPlayer8durationEv(
    const QPlatformMediaPlayer *self) {
  return self->duration();
}

//  qint64 QPlatformMediaPlayer::position() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QPlatformMediaPlayer8positionEv(
    const QPlatformMediaPlayer *self) {
  return self->position();
}

//  void QPlatformMediaPlayer::setPosition(qint64 position)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer11setPositionEx(
    QPlatformMediaPlayer *self,
    qint64 position) {
  self->setPosition(position);
}

//  float QPlatformMediaPlayer::bufferProgress() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QPlatformMediaPlayer14bufferProgressEv(
    const QPlatformMediaPlayer *self) {
  return self->bufferProgress();
}

//  bool QPlatformMediaPlayer::isAudioAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformMediaPlayer16isAudioAvailableEv(
    const QPlatformMediaPlayer *self) {
  return self->isAudioAvailable();
}

//  bool QPlatformMediaPlayer::isVideoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformMediaPlayer16isVideoAvailableEv(
    const QPlatformMediaPlayer *self) {
  return self->isVideoAvailable();
}

//  bool QPlatformMediaPlayer::isSeekable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformMediaPlayer10isSeekableEv(
    const QPlatformMediaPlayer *self) {
  return self->isSeekable();
}

//  QMediaTimeRange QPlatformMediaPlayer::availablePlaybackRanges() const
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZNK20QPlatformMediaPlayer23availablePlaybackRangesEv(
    const QPlatformMediaPlayer *self) {
  return new QMediaTimeRange(self->availablePlaybackRanges());
}

//  qreal QPlatformMediaPlayer::playbackRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QPlatformMediaPlayer12playbackRateEv(
    const QPlatformMediaPlayer *self) {
  return self->playbackRate();
}

//  void QPlatformMediaPlayer::setPlaybackRate(qreal rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer15setPlaybackRateEd(
    QPlatformMediaPlayer *self,
    qreal rate) {
  self->setPlaybackRate(rate);
}

//  QUrl QPlatformMediaPlayer::media() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QPlatformMediaPlayer5mediaEv(
    const QPlatformMediaPlayer *self) {
  return new QUrl(self->media());
}

//  const QIODevice *QPlatformMediaPlayer::mediaStream() const
extern "C" Q_DECL_EXPORT
const QIODevice *ritual_ZNK20QPlatformMediaPlayer11mediaStreamEv(
    const QPlatformMediaPlayer *self) {
  return self->mediaStream();
}

//  void QPlatformMediaPlayer::setMedia(const QUrl &media, QIODevice *stream)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer8setMediaERK4QUrlP9QIODevice(
    QPlatformMediaPlayer *self,
    const QUrl *media,
    QIODevice *stream) {
  self->setMedia(*media, stream);
}

//  void QPlatformMediaPlayer::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer4playEv(QPlatformMediaPlayer *self) {
  self->play();
}

//  void QPlatformMediaPlayer::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer5pauseEv(QPlatformMediaPlayer *self) {
  self->pause();
}

//  void QPlatformMediaPlayer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer4stopEv(QPlatformMediaPlayer *self) {
  self->stop();
}

//  bool QPlatformMediaPlayer::streamPlaybackSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformMediaPlayer23streamPlaybackSupportedEv(
    const QPlatformMediaPlayer *self) {
  return self->streamPlaybackSupported();
}

//  void QPlatformMediaPlayer::setAudioOutput(QPlatformAudioOutput *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer14setAudioOutputEP20QPlatformAudioOutput(
    QPlatformMediaPlayer *self,
    QPlatformAudioOutput *a0) {
  self->setAudioOutput(a0);
}

//  void QPlatformMediaPlayer::setAudioBufferOutput(QAudioBufferOutput *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer20setAudioBufferOutputEP18QAudioBufferOutput(
    QPlatformMediaPlayer *self,
    QAudioBufferOutput *a0) {
  self->setAudioBufferOutput(a0);
}

//  QMediaMetaData QPlatformMediaPlayer::metaData() const
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_ZNK20QPlatformMediaPlayer8metaDataEv(
    const QPlatformMediaPlayer *self) {
  return new QMediaMetaData(self->metaData());
}

//  void QPlatformMediaPlayer::setVideoSink(QVideoSink *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer12setVideoSinkEP10QVideoSink(
    QPlatformMediaPlayer *self,
    QVideoSink *a0) {
  self->setVideoSink(a0);
}

//  bool QPlatformMediaPlayer::canPlayQrc() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformMediaPlayer10canPlayQrcEv(
    const QPlatformMediaPlayer *self) {
  return self->canPlayQrc();
}

//  int QPlatformMediaPlayer::trackCount(TrackType a0)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QPlatformMediaPlayer10trackCountENS_9TrackTypeE(
    QPlatformMediaPlayer *self,
    QPlatformMediaPlayer::TrackType a0) {
  return self->trackCount(a0);
}

//  QMediaMetaData QPlatformMediaPlayer::trackMetaData(TrackType a0, int a1)
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_ZN20QPlatformMediaPlayer13trackMetaDataENS_9TrackTypeEi(
    QPlatformMediaPlayer *self,
    QPlatformMediaPlayer::TrackType a0,
    int a1) {
  return new QMediaMetaData(self->trackMetaData(a0, a1));
}

//  int QPlatformMediaPlayer::activeTrack(TrackType a0)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QPlatformMediaPlayer11activeTrackENS_9TrackTypeE(
    QPlatformMediaPlayer *self,
    QPlatformMediaPlayer::TrackType a0) {
  return self->activeTrack(a0);
}

//  void QPlatformMediaPlayer::setActiveTrack(TrackType a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer14setActiveTrackENS_9TrackTypeEi(
    QPlatformMediaPlayer *self,
    QPlatformMediaPlayer::TrackType a0,
    int a1) {
  self->setActiveTrack(a0, a1);
}

//  void QPlatformMediaPlayer::durationChanged(std::chrono::milliseconds ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer15durationChangedENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QPlatformMediaPlayer *self,
    long long ms) {
  self->durationChanged(std::chrono::milliseconds(ms));
}

//  void QPlatformMediaPlayer::durationChanged(qint64 duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer15durationChangedEx(
    QPlatformMediaPlayer *self,
    qint64 duration) {
  self->durationChanged(duration);
}

//  void QPlatformMediaPlayer::positionChanged(std::chrono::milliseconds ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer15positionChangedENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QPlatformMediaPlayer *self,
    long long ms) {
  self->positionChanged(std::chrono::milliseconds(ms));
}

//  void QPlatformMediaPlayer::positionChanged(qint64 position)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer15positionChangedEx(
    QPlatformMediaPlayer *self,
    qint64 position) {
  self->positionChanged(position);
}

//  void QPlatformMediaPlayer::audioAvailableChanged(bool audioAvailable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer21audioAvailableChangedEb(
    QPlatformMediaPlayer *self,
    bool audioAvailable) {
  self->audioAvailableChanged(audioAvailable);
}

//  void QPlatformMediaPlayer::videoAvailableChanged(bool videoAvailable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer21videoAvailableChangedEb(
    QPlatformMediaPlayer *self,
    bool videoAvailable) {
  self->videoAvailableChanged(videoAvailable);
}

//  void QPlatformMediaPlayer::seekableChanged(bool seekable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer15seekableChangedEb(
    QPlatformMediaPlayer *self,
    bool seekable) {
  self->seekableChanged(seekable);
}

//  void QPlatformMediaPlayer::playbackRateChanged(qreal rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer19playbackRateChangedEd(
    QPlatformMediaPlayer *self,
    qreal rate) {
  self->playbackRateChanged(rate);
}

//  void QPlatformMediaPlayer::bufferProgressChanged(float progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer21bufferProgressChangedEf(
    QPlatformMediaPlayer *self,
    float progress) {
  self->bufferProgressChanged(progress);
}

//  void QPlatformMediaPlayer::metaDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer15metaDataChangedEv(
    QPlatformMediaPlayer *self) {
  self->metaDataChanged();
}

//  void QPlatformMediaPlayer::tracksChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer13tracksChangedEv(
    QPlatformMediaPlayer *self) {
  self->tracksChanged();
}

//  void QPlatformMediaPlayer::activeTracksChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer19activeTracksChangedEv(
    QPlatformMediaPlayer *self) {
  self->activeTracksChanged();
}

//  void QPlatformMediaPlayer::stateChanged(QMediaPlayer::PlaybackState
//      newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer12stateChangedEN12QMediaPlayer13PlaybackStateE(
    QPlatformMediaPlayer *self,
    QMediaPlayer::PlaybackState newState) {
  self->stateChanged(newState);
}

//  void QPlatformMediaPlayer::mediaStatusChanged(QMediaPlayer::MediaStatus
//      status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer18mediaStatusChangedEN12QMediaPlayer11MediaStatusE(
    QPlatformMediaPlayer *self,
    QMediaPlayer::MediaStatus status) {
  self->mediaStatusChanged(status);
}

//  void QPlatformMediaPlayer::error(QMediaPlayer::Error a0, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer5errorEN12QMediaPlayer5ErrorERK7QString(
    QPlatformMediaPlayer *self,
    QMediaPlayer::Error a0,
    const QString *errorString) {
  self->error(a0, *errorString);
}

//  void QPlatformMediaPlayer::setInvalidMediaWithError(QMediaPlayer::Error
//      a0, const QString &errString)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer24setInvalidMediaWithErrorEN12QMediaPlayer5ErrorERK7QString(
    QPlatformMediaPlayer *self,
    QMediaPlayer::Error a0,
    const QString *errString) {
  self->setInvalidMediaWithError(a0, *errString);
}

//  void QPlatformMediaPlayer::resetCurrentLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer16resetCurrentLoopEv(
    QPlatformMediaPlayer *self) {
  self->resetCurrentLoop();
}

//  bool QPlatformMediaPlayer::doLoop()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QPlatformMediaPlayer6doLoopEv(QPlatformMediaPlayer *self) {
  return self->doLoop();
}

//  int QPlatformMediaPlayer::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QPlatformMediaPlayer5loopsEv(
    const QPlatformMediaPlayer *self) {
  return self->loops();
}

//  void QPlatformMediaPlayer::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer8setLoopsEi(
    QPlatformMediaPlayer *self,
    int loops) {
  self->setLoops(loops);
}

//  PitchCompensationAvailability
//      QPlatformMediaPlayer::pitchCompensationAvailability() const
extern "C" Q_DECL_EXPORT
QPlatformMediaPlayer::PitchCompensationAvailability ritual_ZNK20QPlatformMediaPlayer29pitchCompensationAvailabilityEv(
    const QPlatformMediaPlayer *self) {
  return self->pitchCompensationAvailability();
}

//  void QPlatformMediaPlayer::setPitchCompensation(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPlayer20setPitchCompensationEb(
    QPlatformMediaPlayer *self,
    bool enabled) {
  self->setPitchCompensation(enabled);
}

//  bool QPlatformMediaPlayer::pitchCompensation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformMediaPlayer17pitchCompensationEv(
    const QPlatformMediaPlayer *self) {
  return self->pitchCompensation();
}

//  void QPlatformMediaPlayer::pitchCompensationChanged(bool enabled) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformMediaPlayer24pitchCompensationChangedEb(
    const QPlatformMediaPlayer *self,
    bool enabled) {
  self->pitchCompensationChanged(enabled);
}

//  QPlaybackOptions QPlatformMediaPlayer::playbackOptions() const
extern "C" Q_DECL_EXPORT
QPlaybackOptions *ritual_ZNK20QPlatformMediaPlayer15playbackOptionsEv(
    const QPlatformMediaPlayer *self) {
  return new QPlaybackOptions(self->playbackOptions());
}

//  QPlatformMediaPlayer::QPlatformMediaPlayer(QMediaPlayer *parent)
extern "C" Q_DECL_EXPORT
QPlatformMediaPlayer *ritual_ZN20QPlatformMediaPlayerC1EP12QMediaPlayer(
    QMediaPlayer *parent) {
  return new CuteQPlatformMediaPlayer(parent);
}

//  a Python function taken by a CuteQPlatformMediaPlayer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformMediaPlayer(
    QPlatformMediaPlayer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformMediaPlayer *>(self)->take(key, call);
}

//  qint64 QPlatformMediaPlayer::position() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK20QPlatformMediaPlayer8positionEv(
    const QPlatformMediaPlayer *self) {
  return self->QPlatformMediaPlayer::position();
}

//  bool QPlatformMediaPlayer::isAudioAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformMediaPlayer16isAudioAvailableEv(
    const QPlatformMediaPlayer *self) {
  return self->QPlatformMediaPlayer::isAudioAvailable();
}

//  bool QPlatformMediaPlayer::isVideoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformMediaPlayer16isVideoAvailableEv(
    const QPlatformMediaPlayer *self) {
  return self->QPlatformMediaPlayer::isVideoAvailable();
}

//  bool QPlatformMediaPlayer::isSeekable() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformMediaPlayer10isSeekableEv(
    const QPlatformMediaPlayer *self) {
  return self->QPlatformMediaPlayer::isSeekable();
}

//  bool QPlatformMediaPlayer::streamPlaybackSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformMediaPlayer23streamPlaybackSupportedEv(
    const QPlatformMediaPlayer *self) {
  return self->QPlatformMediaPlayer::streamPlaybackSupported();
}

//  void QPlatformMediaPlayer::setAudioOutput(QPlatformAudioOutput *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformMediaPlayer14setAudioOutputEP20QPlatformAudioOutput(
    QPlatformMediaPlayer *self,
    QPlatformAudioOutput *a0) {
  self->QPlatformMediaPlayer::setAudioOutput(a0);
}

//  void QPlatformMediaPlayer::setAudioBufferOutput(QAudioBufferOutput *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformMediaPlayer20setAudioBufferOutputEP18QAudioBufferOutput(
    QPlatformMediaPlayer *self,
    QAudioBufferOutput *a0) {
  self->QPlatformMediaPlayer::setAudioBufferOutput(a0);
}

//  QMediaMetaData QPlatformMediaPlayer::metaData() const
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_own_ZNK20QPlatformMediaPlayer8metaDataEv(
    const QPlatformMediaPlayer *self) {
  return new QMediaMetaData(self->QPlatformMediaPlayer::metaData());
}

//  bool QPlatformMediaPlayer::canPlayQrc() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformMediaPlayer10canPlayQrcEv(
    const QPlatformMediaPlayer *self) {
  return self->QPlatformMediaPlayer::canPlayQrc();
}

//  int QPlatformMediaPlayer::trackCount(TrackType a0)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN20QPlatformMediaPlayer10trackCountENS_9TrackTypeE(
    QPlatformMediaPlayer *self,
    QPlatformMediaPlayer::TrackType a0) {
  return self->QPlatformMediaPlayer::trackCount(a0);
}

//  QMediaMetaData QPlatformMediaPlayer::trackMetaData(TrackType a0, int a1)
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_own_ZN20QPlatformMediaPlayer13trackMetaDataENS_9TrackTypeEi(
    QPlatformMediaPlayer *self,
    QPlatformMediaPlayer::TrackType a0,
    int a1) {
  return new QMediaMetaData(
      self->QPlatformMediaPlayer::trackMetaData(
          a0,
          a1));
}

//  int QPlatformMediaPlayer::activeTrack(TrackType a0)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN20QPlatformMediaPlayer11activeTrackENS_9TrackTypeE(
    QPlatformMediaPlayer *self,
    QPlatformMediaPlayer::TrackType a0) {
  return self->QPlatformMediaPlayer::activeTrack(a0);
}

//  void QPlatformMediaPlayer::setActiveTrack(TrackType a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformMediaPlayer14setActiveTrackENS_9TrackTypeEi(
    QPlatformMediaPlayer *self,
    QPlatformMediaPlayer::TrackType a0,
    int a1) {
  self->QPlatformMediaPlayer::setActiveTrack(a0, a1);
}

//  void QPlatformMediaPlayer::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformMediaPlayer8setLoopsEi(
    QPlatformMediaPlayer *self,
    int loops) {
  self->QPlatformMediaPlayer::setLoops(loops);
}

//  PitchCompensationAvailability
//      QPlatformMediaPlayer::pitchCompensationAvailability() const
extern "C" Q_DECL_EXPORT
QPlatformMediaPlayer::PitchCompensationAvailability ritual_own_ZNK20QPlatformMediaPlayer29pitchCompensationAvailabilityEv(
    const QPlatformMediaPlayer *self) {
  return self->QPlatformMediaPlayer::pitchCompensationAvailability();
}

//  void QPlatformMediaPlayer::setPitchCompensation(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformMediaPlayer20setPitchCompensationEb(
    QPlatformMediaPlayer *self,
    bool enabled) {
  self->QPlatformMediaPlayer::setPitchCompensation(enabled);
}

//  bool QPlatformMediaPlayer::pitchCompensation() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformMediaPlayer17pitchCompensationEv(
    const QPlatformMediaPlayer *self) {
  return self->QPlatformMediaPlayer::pitchCompensation();
}
