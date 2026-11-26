//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qmediaplayer.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qmediaplayer.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qmediametadata.h>
#include <QtCore/qurl.h>
#include <QtMultimedia/qmediatimerange.h>
#include <QtMultimedia/qplaybackoptions.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QMediaPlayer that Python can take functions over in. Every QMediaPlayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMediaPlayerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMediaPlayerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaPlayerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaPlayerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaPlayerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaPlayerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMediaPlayerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMediaPlayer : public QMediaPlayer {
public:
  using QMediaPlayer::QMediaPlayer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMediaPlayerCall0 call = reinterpret_cast<CuteQMediaPlayerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMediaPlayerCall1 call = reinterpret_cast<CuteQMediaPlayerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMediaPlayerCall2 call = reinterpret_cast<CuteQMediaPlayerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMediaPlayerCall3 call = reinterpret_cast<CuteQMediaPlayerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMediaPlayerCall4 call = reinterpret_cast<CuteQMediaPlayerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMediaPlayerCall5 call = reinterpret_cast<CuteQMediaPlayerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMediaPlayerCall6 call = reinterpret_cast<CuteQMediaPlayerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMediaPlayer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QMediaPlayer10metaObjectEv(
    const QMediaPlayer *self) {
  return self->metaObject();
}

//  void *QMediaPlayer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QMediaPlayer11qt_metacastEPKc(
    QMediaPlayer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QMediaPlayer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QMediaPlayer11qt_metacallEN11QMetaObject4CallEiPPv(
    QMediaPlayer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QMediaPlayer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QMediaPlayer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMediaPlayer::tr(s, c, n));
}

//  QMediaPlayer::QMediaPlayer(QObject *parent)
extern "C" Q_DECL_EXPORT
QMediaPlayer *ritual_ZN12QMediaPlayerC1EP7QObject(QObject *parent) {
  return new CuteQMediaPlayer(parent);
}

//  QMediaPlayer::~QMediaPlayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayerD1Ev(QMediaPlayer *self) {
  delete self;
}

//  QList<QMediaMetaData> QMediaPlayer::audioTracks() const
extern "C" Q_DECL_EXPORT
QList<QMediaMetaData> *ritual_ZNK12QMediaPlayer11audioTracksEv(
    const QMediaPlayer *self) {
  return new QList<QMediaMetaData>(self->audioTracks());
}

//  QList<QMediaMetaData> QMediaPlayer::videoTracks() const
extern "C" Q_DECL_EXPORT
QList<QMediaMetaData> *ritual_ZNK12QMediaPlayer11videoTracksEv(
    const QMediaPlayer *self) {
  return new QList<QMediaMetaData>(self->videoTracks());
}

//  QList<QMediaMetaData> QMediaPlayer::subtitleTracks() const
extern "C" Q_DECL_EXPORT
QList<QMediaMetaData> *ritual_ZNK12QMediaPlayer14subtitleTracksEv(
    const QMediaPlayer *self) {
  return new QList<QMediaMetaData>(self->subtitleTracks());
}

//  int QMediaPlayer::activeAudioTrack() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QMediaPlayer16activeAudioTrackEv(const QMediaPlayer *self) {
  return self->activeAudioTrack();
}

//  int QMediaPlayer::activeVideoTrack() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QMediaPlayer16activeVideoTrackEv(const QMediaPlayer *self) {
  return self->activeVideoTrack();
}

//  int QMediaPlayer::activeSubtitleTrack() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QMediaPlayer19activeSubtitleTrackEv(
    const QMediaPlayer *self) {
  return self->activeSubtitleTrack();
}

//  void QMediaPlayer::setActiveAudioTrack(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer19setActiveAudioTrackEi(
    QMediaPlayer *self,
    int index) {
  self->setActiveAudioTrack(index);
}

//  void QMediaPlayer::setActiveVideoTrack(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer19setActiveVideoTrackEi(
    QMediaPlayer *self,
    int index) {
  self->setActiveVideoTrack(index);
}

//  void QMediaPlayer::setActiveSubtitleTrack(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer22setActiveSubtitleTrackEi(
    QMediaPlayer *self,
    int index) {
  self->setActiveSubtitleTrack(index);
}

//  void QMediaPlayer::setAudioBufferOutput(QAudioBufferOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer20setAudioBufferOutputEP18QAudioBufferOutput(
    QMediaPlayer *self,
    QAudioBufferOutput *output) {
  self->setAudioBufferOutput(output);
}

//  QAudioBufferOutput *QMediaPlayer::audioBufferOutput() const
extern "C" Q_DECL_EXPORT
QAudioBufferOutput *ritual_ZNK12QMediaPlayer17audioBufferOutputEv(
    const QMediaPlayer *self) {
  return self->audioBufferOutput();
}

//  void QMediaPlayer::setAudioOutput(QAudioOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer14setAudioOutputEP12QAudioOutput(
    QMediaPlayer *self,
    QAudioOutput *output) {
  self->setAudioOutput(output);
}

//  QAudioOutput *QMediaPlayer::audioOutput() const
extern "C" Q_DECL_EXPORT
QAudioOutput *ritual_ZNK12QMediaPlayer11audioOutputEv(
    const QMediaPlayer *self) {
  return self->audioOutput();
}

//  void QMediaPlayer::setVideoOutput(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer14setVideoOutputEP7QObject(
    QMediaPlayer *self,
    QObject *a0) {
  self->setVideoOutput(a0);
}

//  QObject *QMediaPlayer::videoOutput() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK12QMediaPlayer11videoOutputEv(const QMediaPlayer *self) {
  return self->videoOutput();
}

//  void QMediaPlayer::setVideoSink(QVideoSink *sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer12setVideoSinkEP10QVideoSink(
    QMediaPlayer *self,
    QVideoSink *sink) {
  self->setVideoSink(sink);
}

//  QVideoSink *QMediaPlayer::videoSink() const
extern "C" Q_DECL_EXPORT
QVideoSink *ritual_ZNK12QMediaPlayer9videoSinkEv(const QMediaPlayer *self) {
  return self->videoSink();
}

//  QUrl QMediaPlayer::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QMediaPlayer6sourceEv(const QMediaPlayer *self) {
  return new QUrl(self->source());
}

//  const QIODevice *QMediaPlayer::sourceDevice() const
extern "C" Q_DECL_EXPORT
const QIODevice *ritual_ZNK12QMediaPlayer12sourceDeviceEv(
    const QMediaPlayer *self) {
  return self->sourceDevice();
}

//  PlaybackState QMediaPlayer::playbackState() const
extern "C" Q_DECL_EXPORT
QMediaPlayer::PlaybackState ritual_ZNK12QMediaPlayer13playbackStateEv(
    const QMediaPlayer *self) {
  return self->playbackState();
}

//  MediaStatus QMediaPlayer::mediaStatus() const
extern "C" Q_DECL_EXPORT
QMediaPlayer::MediaStatus ritual_ZNK12QMediaPlayer11mediaStatusEv(
    const QMediaPlayer *self) {
  return self->mediaStatus();
}

//  qint64 QMediaPlayer::duration() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QMediaPlayer8durationEv(const QMediaPlayer *self) {
  return self->duration();
}

//  qint64 QMediaPlayer::position() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QMediaPlayer8positionEv(const QMediaPlayer *self) {
  return self->position();
}

//  bool QMediaPlayer::hasAudio() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMediaPlayer8hasAudioEv(const QMediaPlayer *self) {
  return self->hasAudio();
}

//  bool QMediaPlayer::hasVideo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMediaPlayer8hasVideoEv(const QMediaPlayer *self) {
  return self->hasVideo();
}

//  float QMediaPlayer::bufferProgress() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QMediaPlayer14bufferProgressEv(const QMediaPlayer *self) {
  return self->bufferProgress();
}

//  QMediaTimeRange QMediaPlayer::bufferedTimeRange() const
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZNK12QMediaPlayer17bufferedTimeRangeEv(
    const QMediaPlayer *self) {
  return new QMediaTimeRange(self->bufferedTimeRange());
}

//  bool QMediaPlayer::isSeekable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMediaPlayer10isSeekableEv(const QMediaPlayer *self) {
  return self->isSeekable();
}

//  qreal QMediaPlayer::playbackRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QMediaPlayer12playbackRateEv(const QMediaPlayer *self) {
  return self->playbackRate();
}

//  bool QMediaPlayer::isPlaying() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMediaPlayer9isPlayingEv(const QMediaPlayer *self) {
  return self->isPlaying();
}

//  int QMediaPlayer::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QMediaPlayer5loopsEv(const QMediaPlayer *self) {
  return self->loops();
}

//  void QMediaPlayer::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer8setLoopsEi(QMediaPlayer *self, int loops) {
  self->setLoops(loops);
}

//  Error QMediaPlayer::error() const
extern "C" Q_DECL_EXPORT
QMediaPlayer::Error ritual_ZNK12QMediaPlayer5errorEv(
    const QMediaPlayer *self) {
  return self->error();
}

//  QString QMediaPlayer::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QMediaPlayer11errorStringEv(const QMediaPlayer *self) {
  return new QString(self->errorString());
}

//  bool QMediaPlayer::isAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMediaPlayer11isAvailableEv(const QMediaPlayer *self) {
  return self->isAvailable();
}

//  QMediaMetaData QMediaPlayer::metaData() const
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_ZNK12QMediaPlayer8metaDataEv(
    const QMediaPlayer *self) {
  return new QMediaMetaData(self->metaData());
}

//  PitchCompensationAvailability
//      QMediaPlayer::pitchCompensationAvailability() const
extern "C" Q_DECL_EXPORT
QMediaPlayer::PitchCompensationAvailability ritual_ZNK12QMediaPlayer29pitchCompensationAvailabilityEv(
    const QMediaPlayer *self) {
  return self->pitchCompensationAvailability();
}

//  bool QMediaPlayer::pitchCompensation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMediaPlayer17pitchCompensationEv(
    const QMediaPlayer *self) {
  return self->pitchCompensation();
}

//  QPlaybackOptions QMediaPlayer::playbackOptions() const
extern "C" Q_DECL_EXPORT
QPlaybackOptions *ritual_ZNK12QMediaPlayer15playbackOptionsEv(
    const QMediaPlayer *self) {
  return new QPlaybackOptions(self->playbackOptions());
}

//  void QMediaPlayer::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer4playEv(QMediaPlayer *self) {
  self->play();
}

//  void QMediaPlayer::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer5pauseEv(QMediaPlayer *self) {
  self->pause();
}

//  void QMediaPlayer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer4stopEv(QMediaPlayer *self) {
  self->stop();
}

//  void QMediaPlayer::setPosition(qint64 position)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer11setPositionEx(
    QMediaPlayer *self,
    qint64 position) {
  self->setPosition(position);
}

//  void QMediaPlayer::setPlaybackRate(qreal rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer15setPlaybackRateEd(
    QMediaPlayer *self,
    qreal rate) {
  self->setPlaybackRate(rate);
}

//  void QMediaPlayer::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer9setSourceERK4QUrl(
    QMediaPlayer *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void QMediaPlayer::setSourceDevice(QIODevice *device, const QUrl
//      &sourceUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer15setSourceDeviceEP9QIODeviceRK4QUrl(
    QMediaPlayer *self,
    QIODevice *device,
    const QUrl *sourceUrl) {
  self->setSourceDevice(device, *sourceUrl);
}

//  void QMediaPlayer::setPitchCompensation(bool a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QMediaPlayer20setPitchCompensationEb(
    const QMediaPlayer *self,
    bool a0) {
  self->setPitchCompensation(a0);
}

//  void QMediaPlayer::setPlaybackOptions(const QPlaybackOptions &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer18setPlaybackOptionsERK16QPlaybackOptions(
    QMediaPlayer *self,
    const QPlaybackOptions *options) {
  self->setPlaybackOptions(*options);
}

//  void QMediaPlayer::resetPlaybackOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer20resetPlaybackOptionsEv(QMediaPlayer *self) {
  self->resetPlaybackOptions();
}

//  void QMediaPlayer::sourceChanged(const QUrl &media)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer13sourceChangedERK4QUrl(
    QMediaPlayer *self,
    const QUrl *media) {
  self->sourceChanged(*media);
}

//  void QMediaPlayer::playbackStateChanged(QMediaPlayer::PlaybackState
//      newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer20playbackStateChangedENS_13PlaybackStateE(
    QMediaPlayer *self,
    QMediaPlayer::PlaybackState newState) {
  self->playbackStateChanged(newState);
}

//  void QMediaPlayer::mediaStatusChanged(QMediaPlayer::MediaStatus status)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer18mediaStatusChangedENS_11MediaStatusE(
    QMediaPlayer *self,
    QMediaPlayer::MediaStatus status) {
  self->mediaStatusChanged(status);
}

//  void QMediaPlayer::durationChanged(qint64 duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer15durationChangedEx(
    QMediaPlayer *self,
    qint64 duration) {
  self->durationChanged(duration);
}

//  void QMediaPlayer::positionChanged(qint64 position)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer15positionChangedEx(
    QMediaPlayer *self,
    qint64 position) {
  self->positionChanged(position);
}

//  void QMediaPlayer::hasAudioChanged(bool available)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer15hasAudioChangedEb(
    QMediaPlayer *self,
    bool available) {
  self->hasAudioChanged(available);
}

//  void QMediaPlayer::hasVideoChanged(bool videoAvailable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer15hasVideoChangedEb(
    QMediaPlayer *self,
    bool videoAvailable) {
  self->hasVideoChanged(videoAvailable);
}

//  void QMediaPlayer::bufferProgressChanged(float progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer21bufferProgressChangedEf(
    QMediaPlayer *self,
    float progress) {
  self->bufferProgressChanged(progress);
}

//  void QMediaPlayer::seekableChanged(bool seekable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer15seekableChangedEb(
    QMediaPlayer *self,
    bool seekable) {
  self->seekableChanged(seekable);
}

//  void QMediaPlayer::playingChanged(bool playing)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer14playingChangedEb(
    QMediaPlayer *self,
    bool playing) {
  self->playingChanged(playing);
}

//  void QMediaPlayer::playbackRateChanged(qreal rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer19playbackRateChangedEd(
    QMediaPlayer *self,
    qreal rate) {
  self->playbackRateChanged(rate);
}

//  void QMediaPlayer::loopsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer12loopsChangedEv(QMediaPlayer *self) {
  self->loopsChanged();
}

//  void QMediaPlayer::metaDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer15metaDataChangedEv(QMediaPlayer *self) {
  self->metaDataChanged();
}

//  void QMediaPlayer::videoOutputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer18videoOutputChangedEv(QMediaPlayer *self) {
  self->videoOutputChanged();
}

//  void QMediaPlayer::audioOutputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer18audioOutputChangedEv(QMediaPlayer *self) {
  self->audioOutputChanged();
}

//  void QMediaPlayer::audioBufferOutputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer24audioBufferOutputChangedEv(
    QMediaPlayer *self) {
  self->audioBufferOutputChanged();
}

//  void QMediaPlayer::tracksChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer13tracksChangedEv(QMediaPlayer *self) {
  self->tracksChanged();
}

//  void QMediaPlayer::activeTracksChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer19activeTracksChangedEv(QMediaPlayer *self) {
  self->activeTracksChanged();
}

//  void QMediaPlayer::errorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer12errorChangedEv(QMediaPlayer *self) {
  self->errorChanged();
}

//  void QMediaPlayer::errorOccurred(QMediaPlayer::Error error, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer13errorOccurredENS_5ErrorERK7QString(
    QMediaPlayer *self,
    QMediaPlayer::Error error,
    const QString *errorString) {
  self->errorOccurred(error, *errorString);
}

//  void QMediaPlayer::pitchCompensationChanged(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer24pitchCompensationChangedEb(
    QMediaPlayer *self,
    bool a0) {
  self->pitchCompensationChanged(a0);
}

//  void QMediaPlayer::playbackOptionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaPlayer22playbackOptionsChangedEv(QMediaPlayer *self) {
  self->playbackOptionsChanged();
}

//  QMediaPlayerPrivate *QMediaPlayer::d_func()
extern "C" Q_DECL_EXPORT
QMediaPlayerPrivate *ritual_ZN12QMediaPlayer6d_funcEv(QMediaPlayer *self) {
  return self->d_func();
}

//  const QMediaPlayerPrivate *QMediaPlayer::d_func() const
extern "C" Q_DECL_EXPORT
const QMediaPlayerPrivate *ritual_ZNK12QMediaPlayer6d_funcEv(
    const QMediaPlayer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQMediaPlayer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMediaPlayer(
    QMediaPlayer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMediaPlayer *>(self)->take(key, call);
}
