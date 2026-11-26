//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectwithplayer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectwithplayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qurl.h>
#include <memory>
#include <QtMultimedia/QAudioDevice>
#include <QtMultimedia/QAudioFormat>
#include <optional>

//  std::shared_ptr<QRtAudioEngine>
//      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::getEngineFor(cons
//      t QAudioDevice &a0, const QAudioFormat &a1)
extern "C" Q_DECL_EXPORT
std::shared_ptr<QtMultimediaPrivate::QRtAudioEngine> *ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer12getEngineForERK12QAudioDeviceRK12QAudioFormat(
    const QAudioDevice *a0,
    const QAudioFormat *a1) {
  return new std::shared_ptr<QtMultimediaPrivate::QRtAudioEngine>(
      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::getEngineFor(
          *a0,
          *a1));
}

//  QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::QSoundEffectPrivateWi
//      thPlayer(QSoundEffect *q, QAudioDevice audioDevice)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayerC1EP12QSoundEffect12QAudioDevice(
    QSoundEffect *q,
    const QAudioDevice *audioDevice) {
  return new QtMultimediaPrivate::QSoundEffectPrivateWithPlayer(
      q,
      *audioDevice);
}

//  QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::~QSoundEffectPrivateW
//      ithPlayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayerD1Ev(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  delete self;
}

//  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setAudioDevice(Q
//      AudioDevice device)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer14setAudioDeviceE12QAudioDevice(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    const QAudioDevice *device) {
  return self->setAudioDevice(*device);
}

//  QAudioDevice
//      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::audioDevice()
//      const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer11audioDeviceEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return new QAudioDevice(self->audioDevice());
}

//  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setSource(QUrl
//      a0, QSampleCache &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer9setSourceE4QUrlR12QSampleCache(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    const QUrl *a0,
    QSampleCache *a1) {
  self->setSource(*a0, *a1);
}

//  QSoundEffect::Status
//      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::status() const
extern "C" Q_DECL_EXPORT
QSoundEffect::Status ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer6statusEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return self->status();
}

//  int QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer9loopCountEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return self->loopCount();
}

//  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setLoopCount(int
//      a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer12setLoopCountEi(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    int a0) {
  return self->setLoopCount(a0);
}

//  int QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::loopsRemaining()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer14loopsRemainingEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return self->loopsRemaining();
}

//  float QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer6volumeEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return self->volume();
}

//  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setVolume(float
//      a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer9setVolumeEf(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    float a0) {
  return self->setVolume(a0);
}

//  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::muted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer5mutedEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return self->muted();
}

//  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setMuted(bool
//      a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer8setMutedEb(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    bool a0) {
  return self->setMuted(a0);
}

//  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer4playEv(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  self->play();
}

//  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer4stopEv(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  self->stop();
}

//  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::playing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer7playingEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return self->playing();
}

//  const std::shared_ptr<QRtAudioEngine>
//      &QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::player() const
extern "C" Q_DECL_EXPORT
const std::shared_ptr<QtMultimediaPrivate::QRtAudioEngine> *ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer6playerEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return &(self->player());
}

//  const std::set<std::shared_ptr<QSoundEffectVoice>,
//      QRtAudioEngineVoiceCompare>
//      &QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::voices() const
extern "C" Q_DECL_EXPORT
const std::set<std::shared_ptr<QtMultimediaPrivate::QSoundEffectVoice>, QtMultimediaPrivate::QRtAudioEngineVoiceCompare> *ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer6voicesEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return &(self->voices());
}

//  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::play(std::shared
//      _ptr<QSoundEffectVoice> a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer4playESt10shared_ptrINS_17QSoundEffectVoiceEE(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    const std::shared_ptr<QtMultimediaPrivate::QSoundEffectVoice> *a0) {
  self->play(*a0);
}

//  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setStatus(QSound
//      Effect::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer9setStatusEN12QSoundEffect6StatusE(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    QSoundEffect::Status status) {
  self->setStatus(status);
}

//  bool
//      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::updatePlayer(cons
//      t SharedSamplePtr &sample)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer12updatePlayerERKSt10shared_ptrI7QSampleE(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    const SharedSamplePtr *sample) {
  return self->updatePlayer(*sample);
}

//  std::optional<VoiceId>
//      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::activeVoice()
//      const
extern "C" Q_DECL_EXPORT
std::optional<QtMultimediaPrivate::VoiceId> *ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer11activeVoiceEv(
    const QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return new std::optional<QtMultimediaPrivate::VoiceId>(
      self->activeVoice());
}

//  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::formatIsSupporte
//      d(const QAudioFormat &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer17formatIsSupportedERK12QAudioFormat(
    const QAudioFormat *a0) {
  return QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::formatIsSupported(
      *a0);
}

//  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setResolvedAudio
//      Device(QAudioDevice device)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer22setResolvedAudioDeviceE12QAudioDevice(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    const QAudioDevice *device) {
  self->setResolvedAudioDevice(*device);
}

//  void
//      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::resolveAudioDevic
//      e()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer18resolveAudioDeviceEv(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  self->resolveAudioDevice();
}

//  void
//      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setLoopsRemaining
//      (int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer17setLoopsRemainingEi(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self,
    int a0) {
  self->setLoopsRemaining(a0);
}

//  QtMultimediaPrivate::QSoundEffectPrivateWithPlayer as the
//      QSoundEffectPrivate it is built on
extern "C" Q_DECL_EXPORT
QSoundEffectPrivate *ritual_cast_QtMultimediaPrivate_QSoundEffectPrivateWithPlayer_QSoundEffectPrivate(
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer *self) {
  return static_cast<QSoundEffectPrivate *>(self);
}

//  a std::shared_ptr<QtMultimediaPrivate::QRtAudioEngine> a ritual of
//      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMultimediaPrivate_QSoundEffectPrivateWithPlayer__std_shared_ptr_QtMultimediaPrivate_QRtAudioEngine(
    std::shared_ptr<QtMultimediaPrivate::QRtAudioEngine> *self) {
  delete self;
}

//  a std::optional<QtMultimediaPrivate::VoiceId> a ritual of
//      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMultimediaPrivate_QSoundEffectPrivateWithPlayer__std_optional_QtMultimediaPrivate_VoiceId(
    std::optional<QtMultimediaPrivate::VoiceId> *self) {
  delete self;
}
