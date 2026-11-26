//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, rituals for functions the
//  generator leaves out: 4. Kept as it is when the generator runs again.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/QAudioDevice>
#include <QtMultimedia/QAudioFormat>
#include <optional>

//  const QMetaObject *QtMultimediaPrivate::QRtAudioEngine::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QtMultimediaPrivate14QRtAudioEngine10metaObjectEv(
    const QtMultimediaPrivate::QRtAudioEngine *self) {
  return self->metaObject();
}

//  void *QtMultimediaPrivate::QRtAudioEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QtMultimediaPrivate14QRtAudioEngine11qt_metacastEPKc(
    QtMultimediaPrivate::QRtAudioEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtMultimediaPrivate::QRtAudioEngine::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QtMultimediaPrivate14QRtAudioEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QtMultimediaPrivate::QRtAudioEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtMultimediaPrivate::QRtAudioEngine::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QtMultimediaPrivate14QRtAudioEngine2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtMultimediaPrivate::QRtAudioEngine::tr(s, c, n));
}

//  QtMultimediaPrivate::QRtAudioEngine::QRtAudioEngine(const QAudioDevice
//      &a0, const QAudioFormat &a1, std::optional<AudioEndpointRole> a2,
//      std::optional<NativePeriodFrames> nativePeriodFrames)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QRtAudioEngine *ritual_ZN19QtMultimediaPrivate14QRtAudioEngineC1ERK12QAudioDeviceRK12QAudioFormatSt8optionalINS_17AudioEndpointRoleEES7_INS_18NativePeriodFramesEE(
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    const std::optional<QtMultimediaPrivate::AudioEndpointRole> *a2,
    const std::optional<QtMultimediaPrivate::NativePeriodFrames> *nativePeriodFrames) {
  return new QtMultimediaPrivate::QRtAudioEngine(
      *a0,
      *a1,
      *a2,
      *nativePeriodFrames);
}

//  QtMultimediaPrivate::QRtAudioEngine::~QRtAudioEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngineD1Ev(
    QtMultimediaPrivate::QRtAudioEngine *self) {
  delete self;
}

//  void QtMultimediaPrivate::QRtAudioEngine::play(SharedVoice a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine4playESt10shared_ptrINS_19QRtAudioEngineVoiceEE(
    QtMultimediaPrivate::QRtAudioEngine *self,
    const QtMultimediaPrivate::QRtAudioEngine::SharedVoice *a0) {
  self->play(*a0);
}

//  void QtMultimediaPrivate::QRtAudioEngine::stop(const SharedVoice &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine4stopERKSt10shared_ptrINS_19QRtAudioEngineVoiceEE(
    QtMultimediaPrivate::QRtAudioEngine *self,
    const QtMultimediaPrivate::QRtAudioEngine::SharedVoice *a0) {
  self->stop(*a0);
}

//  std::unique_ptr<pmr::memory_resource>
//      &QtMultimediaPrivate::QRtAudioEngine::rtMemoryResource()
extern "C" Q_DECL_EXPORT
std::unique_ptr<QtMultimediaPrivate::pmr::memory_resource> *ritual_ZN19QtMultimediaPrivate14QRtAudioEngine16rtMemoryResourceEv(
    QtMultimediaPrivate::QRtAudioEngine *self) {
  return &(self->rtMemoryResource());
}

//  QAudioSink &QtMultimediaPrivate::QRtAudioEngine::audioSink()
extern "C" Q_DECL_EXPORT
QAudioSink *ritual_ZN19QtMultimediaPrivate14QRtAudioEngine9audioSinkEv(
    QtMultimediaPrivate::QRtAudioEngine *self) {
  return &(self->audioSink());
}

//  const std::set<SharedVoice, QRtAudioEngineVoiceCompare>
//      &QtMultimediaPrivate::QRtAudioEngine::voices() const
extern "C" Q_DECL_EXPORT
const std::set<QtMultimediaPrivate::QRtAudioEngine::SharedVoice, QtMultimediaPrivate::QRtAudioEngineVoiceCompare> *ritual_ZNK19QtMultimediaPrivate14QRtAudioEngine6voicesEv(
    const QtMultimediaPrivate::QRtAudioEngine *self) {
  return &(self->voices());
}

//  QtAudio::State QtMultimediaPrivate::QRtAudioEngine::audioState() const
extern "C" Q_DECL_EXPORT
QtAudio::State ritual_ZNK19QtMultimediaPrivate14QRtAudioEngine10audioStateEv(
    const QtMultimediaPrivate::QRtAudioEngine *self) {
  return self->audioState();
}

//  void QtMultimediaPrivate::QRtAudioEngine::stateChanged(QtAudio::State a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine12stateChangedEN6QAudio5StateE(
    QtMultimediaPrivate::QRtAudioEngine *self,
    QtAudio::State a0) {
  self->stateChanged(a0);
}

//  void QtMultimediaPrivate::QRtAudioEngine::runNonRtNotifications()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine21runNonRtNotificationsEv(
    QtMultimediaPrivate::QRtAudioEngine *self) {
  self->runNonRtNotifications();
}

//  void QtMultimediaPrivate::QRtAudioEngine::runNonRtNotification(StopNotifi
//      cation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine20runNonRtNotificationENS0_16StopNotificationE(
    QtMultimediaPrivate::QRtAudioEngine *self,
    const QtMultimediaPrivate::QRtAudioEngine::StopNotification *a0) {
  self->runNonRtNotification(*a0);
}

//  void QtMultimediaPrivate::QRtAudioEngine::runNonRtNotification(VisitReply
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine20runNonRtNotificationENS0_10VisitReplyE(
    QtMultimediaPrivate::QRtAudioEngine *self,
    const QtMultimediaPrivate::QRtAudioEngine::VisitReply *a0) {
  self->runNonRtNotification(*a0);
}

//  void QtMultimediaPrivate::QRtAudioEngine::sendAppToRtCommand(RtCommand
//      cmd)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine18sendAppToRtCommandESt7variantIJNS0_11PlayCommandENS0_11StopCommandENS0_12VisitCommandENS0_19VisitCommandTrivialEEE(
    QtMultimediaPrivate::QRtAudioEngine *self,
    const QtMultimediaPrivate::QRtAudioEngine::RtCommand *cmd) {
  self->sendAppToRtCommand(*cmd);
}

//  bool
//      QtMultimediaPrivate::QRtAudioEngine::sendRtToAppNotification(Notifica
//      tion cmd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtMultimediaPrivate14QRtAudioEngine23sendRtToAppNotificationESt7variantIJNS0_16StopNotificationENS0_10VisitReplyEEE(
    QtMultimediaPrivate::QRtAudioEngine *self,
    const QtMultimediaPrivate::QRtAudioEngine::Notification *cmd) {
  return self->sendRtToAppNotification(*cmd);
}

//  void QtMultimediaPrivate::QRtAudioEngine::sendPendingRtCommands()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine21sendPendingRtCommandsEv(
    QtMultimediaPrivate::QRtAudioEngine *self) {
  self->sendPendingRtCommands();
}

//  bool QtMultimediaPrivate::QRtAudioEngine::sendPendingAppNotifications()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtMultimediaPrivate14QRtAudioEngine27sendPendingAppNotificationsEv(
    QtMultimediaPrivate::QRtAudioEngine *self) {
  return self->sendPendingAppNotifications();
}

//  void QtMultimediaPrivate::QRtAudioEngine::stop(VoiceId a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine4stopENS_7VoiceIdE(
    QtMultimediaPrivate::QRtAudioEngine *self,
    unsigned long long a0) {
  self->stop(static_cast<QtMultimediaPrivate::VoiceId>(a0));
}

//  static VoiceId QtMultimediaPrivate::QRtAudioEngine::allocateVoiceId()
extern "C" Q_DECL_EXPORT
unsigned long long ritual_ZN19QtMultimediaPrivate14QRtAudioEngine15allocateVoiceIdEv() {
  return static_cast<unsigned long long>(
      QtMultimediaPrivate::QRtAudioEngine::allocateVoiceId());
}

//  void QtMultimediaPrivate::QRtAudioEngine::voiceFinished(VoiceId a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate14QRtAudioEngine13voiceFinishedENS_7VoiceIdE(
    QtMultimediaPrivate::QRtAudioEngine *self,
    unsigned long long a0) {
  self->voiceFinished(static_cast<QtMultimediaPrivate::VoiceId>(a0));
}

//  void QtMultimediaPrivate::QRtAudioEngine::visitVoiceRt(VoiceId a0,
//      RtVoiceVisitor a1, bool visitorIsTrivial)
extern "C" Q_DECL_EXPORT
void ritual_callback_ZN19QtMultimediaPrivate14QRtAudioEngine12visitVoiceRtENS_7VoiceIdESt8functionIFvRNS_19QRtAudioEngineVoiceEEEb(
    QtMultimediaPrivate::QRtAudioEngine *self,
    unsigned long long a0,
    void *call,
    void *context,
    bool visitorIsTrivial) {
  using Voice = QtMultimediaPrivate::QRtAudioEngineVoice;
  auto function = reinterpret_cast<void (*)(void *, Voice *)>(call);
  auto visitor = [function, context](Voice &voice) {
    function(context, &voice);
  };
  self->visitVoiceRt(
      static_cast<QtMultimediaPrivate::VoiceId>(a0),
      QtMultimediaPrivate::QRtAudioEngine::RtVoiceVisitor(visitor),
      visitorIsTrivial);
}
