//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudioformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qaudioformat.h>

//  bool QAudioFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioFormat7isValidEv(const QAudioFormat *self) {
  return self->isValid();
}

//  void QAudioFormat::setSampleRate(int sampleRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioFormat13setSampleRateEi(
    QAudioFormat *self,
    int sampleRate) {
  self->setSampleRate(sampleRate);
}

//  int QAudioFormat::sampleRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioFormat10sampleRateEv(const QAudioFormat *self) {
  return self->sampleRate();
}

//  void QAudioFormat::setChannelConfig(ChannelConfig config)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioFormat16setChannelConfigENS_13ChannelConfigE(
    QAudioFormat *self,
    QAudioFormat::ChannelConfig config) {
  self->setChannelConfig(config);
}

//  ChannelConfig QAudioFormat::channelConfig() const
extern "C" Q_DECL_EXPORT
QAudioFormat::ChannelConfig ritual_ZNK12QAudioFormat13channelConfigEv(
    const QAudioFormat *self) {
  return self->channelConfig();
}

//  void QAudioFormat::setChannelCount(int channelCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioFormat15setChannelCountEi(
    QAudioFormat *self,
    int channelCount) {
  self->setChannelCount(channelCount);
}

//  int QAudioFormat::channelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioFormat12channelCountEv(const QAudioFormat *self) {
  return self->channelCount();
}

//  int QAudioFormat::channelOffset(AudioChannelPosition channel) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioFormat13channelOffsetENS_20AudioChannelPositionE(
    const QAudioFormat *self,
    QAudioFormat::AudioChannelPosition channel) {
  return self->channelOffset(channel);
}

//  void QAudioFormat::setSampleFormat(SampleFormat f)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioFormat15setSampleFormatENS_12SampleFormatE(
    QAudioFormat *self,
    QAudioFormat::SampleFormat f) {
  self->setSampleFormat(f);
}

//  SampleFormat QAudioFormat::sampleFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat::SampleFormat ritual_ZNK12QAudioFormat12sampleFormatEv(
    const QAudioFormat *self) {
  return self->sampleFormat();
}

//  qint32 QAudioFormat::bytesForDuration(qint64 microseconds) const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK12QAudioFormat16bytesForDurationEx(
    const QAudioFormat *self,
    qint64 microseconds) {
  return self->bytesForDuration(microseconds);
}

//  qint64 QAudioFormat::durationForBytes(qint32 byteCount) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QAudioFormat16durationForBytesEi(
    const QAudioFormat *self,
    qint32 byteCount) {
  return self->durationForBytes(byteCount);
}

//  qint32 QAudioFormat::bytesForFrames(qint32 frameCount) const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK12QAudioFormat14bytesForFramesEi(
    const QAudioFormat *self,
    qint32 frameCount) {
  return self->bytesForFrames(frameCount);
}

//  qint32 QAudioFormat::framesForBytes(qint32 byteCount) const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK12QAudioFormat14framesForBytesEi(
    const QAudioFormat *self,
    qint32 byteCount) {
  return self->framesForBytes(byteCount);
}

//  qint32 QAudioFormat::framesForDuration(qint64 microseconds) const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK12QAudioFormat17framesForDurationEx(
    const QAudioFormat *self,
    qint64 microseconds) {
  return self->framesForDuration(microseconds);
}

//  qint64 QAudioFormat::durationForFrames(qint32 frameCount) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QAudioFormat17durationForFramesEi(
    const QAudioFormat *self,
    qint32 frameCount) {
  return self->durationForFrames(frameCount);
}

//  int QAudioFormat::bytesPerFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioFormat13bytesPerFrameEv(const QAudioFormat *self) {
  return self->bytesPerFrame();
}

//  int QAudioFormat::bytesPerSample() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioFormat14bytesPerSampleEv(const QAudioFormat *self) {
  return self->bytesPerSample();
}

//  float QAudioFormat::normalizedSampleValue(const void *sample) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QAudioFormat21normalizedSampleValueEPKv(
    const QAudioFormat *self,
    const void *sample) {
  return self->normalizedSampleValue(sample);
}

//  bool operator==(const QAudioFormat &a, const QAudioFormat &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QAudioFormatS1_(
    const QAudioFormat *a,
    const QAudioFormat *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QAudioFormat &a, const QAudioFormat &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QAudioFormatS1_(
    const QAudioFormat *a,
    const QAudioFormat *b) {
  return operator!=(*a, *b);
}

//  ChannelConfig QAudioFormat::defaultChannelConfigForChannelCount(int
//      channelCount)
extern "C" Q_DECL_EXPORT
QAudioFormat::ChannelConfig ritual_ZN12QAudioFormat35defaultChannelConfigForChannelCountEi(
    int channelCount) {
  return QAudioFormat::defaultChannelConfigForChannelCount(channelCount);
}

//  QAudioFormat::~QAudioFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioFormatD1Ev(QAudioFormat *self) {
  delete self;
}
