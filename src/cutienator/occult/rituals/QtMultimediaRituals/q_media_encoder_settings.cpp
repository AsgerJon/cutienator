//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediarecorder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediarecorder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qmediaformat.h>
#include <QtCore/qmimetype.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  QMediaFormat QMediaEncoderSettings::mediaFormat() const
extern "C" Q_DECL_EXPORT
QMediaFormat *ritual_ZNK21QMediaEncoderSettings11mediaFormatEv(
    const QMediaEncoderSettings *self) {
  return new QMediaFormat(self->mediaFormat());
}

//  void QMediaEncoderSettings::setMediaFormat(const QMediaFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings14setMediaFormatERK12QMediaFormat(
    QMediaEncoderSettings *self,
    const QMediaFormat *format) {
  self->setMediaFormat(*format);
}

//  void QMediaEncoderSettings::resolveFormat(QMediaFormat::ResolveFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings13resolveFormatEN12QMediaFormat12ResolveFlagsE(
    QMediaEncoderSettings *self,
    QMediaFormat::ResolveFlags flags) {
  self->resolveFormat(flags);
}

//  QMediaFormat::FileFormat QMediaEncoderSettings::fileFormat() const
extern "C" Q_DECL_EXPORT
QMediaFormat::FileFormat ritual_ZNK21QMediaEncoderSettings10fileFormatEv(
    const QMediaEncoderSettings *self) {
  return self->fileFormat();
}

//  QMediaFormat::VideoCodec QMediaEncoderSettings::videoCodec() const
extern "C" Q_DECL_EXPORT
QMediaFormat::VideoCodec ritual_ZNK21QMediaEncoderSettings10videoCodecEv(
    const QMediaEncoderSettings *self) {
  return self->videoCodec();
}

//  QMediaFormat::AudioCodec QMediaEncoderSettings::audioCodec() const
extern "C" Q_DECL_EXPORT
QMediaFormat::AudioCodec ritual_ZNK21QMediaEncoderSettings10audioCodecEv(
    const QMediaEncoderSettings *self) {
  return self->audioCodec();
}

#if QT_CONFIG(mimetype)
//  QMimeType QMediaEncoderSettings::mimeType() const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK21QMediaEncoderSettings8mimeTypeEv(
    const QMediaEncoderSettings *self) {
  return new QMimeType(self->mimeType());
}
#endif  // QT_CONFIG(mimetype)

//  QString QMediaEncoderSettings::preferredSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QMediaEncoderSettings15preferredSuffixEv(
    const QMediaEncoderSettings *self) {
  return new QString(self->preferredSuffix());
}

//  QMediaRecorder::EncodingMode QMediaEncoderSettings::encodingMode() const
extern "C" Q_DECL_EXPORT
QMediaRecorder::EncodingMode ritual_ZNK21QMediaEncoderSettings12encodingModeEv(
    const QMediaEncoderSettings *self) {
  return self->encodingMode();
}

//  void QMediaEncoderSettings::setEncodingMode(QMediaRecorder::EncodingMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings15setEncodingModeEN14QMediaRecorder12EncodingModeE(
    QMediaEncoderSettings *self,
    QMediaRecorder::EncodingMode mode) {
  self->setEncodingMode(mode);
}

//  QMediaRecorder::Quality QMediaEncoderSettings::quality() const
extern "C" Q_DECL_EXPORT
QMediaRecorder::Quality ritual_ZNK21QMediaEncoderSettings7qualityEv(
    const QMediaEncoderSettings *self) {
  return self->quality();
}

//  void QMediaEncoderSettings::setQuality(QMediaRecorder::Quality quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings10setQualityEN14QMediaRecorder7QualityE(
    QMediaEncoderSettings *self,
    QMediaRecorder::Quality quality) {
  self->setQuality(quality);
}

//  QSize QMediaEncoderSettings::videoResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QMediaEncoderSettings15videoResolutionEv(
    const QMediaEncoderSettings *self) {
  return new QSize(self->videoResolution());
}

//  void QMediaEncoderSettings::setVideoResolution(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings18setVideoResolutionERK5QSize(
    QMediaEncoderSettings *self,
    const QSize *size) {
  self->setVideoResolution(*size);
}

//  qreal QMediaEncoderSettings::videoFrameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QMediaEncoderSettings14videoFrameRateEv(
    const QMediaEncoderSettings *self) {
  return self->videoFrameRate();
}

//  void QMediaEncoderSettings::setVideoFrameRate(qreal rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings17setVideoFrameRateEd(
    QMediaEncoderSettings *self,
    qreal rate) {
  self->setVideoFrameRate(rate);
}

//  int QMediaEncoderSettings::videoBitRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QMediaEncoderSettings12videoBitRateEv(
    const QMediaEncoderSettings *self) {
  return self->videoBitRate();
}

//  void QMediaEncoderSettings::setVideoBitRate(int bitrate)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings15setVideoBitRateEi(
    QMediaEncoderSettings *self,
    int bitrate) {
  self->setVideoBitRate(bitrate);
}

//  int QMediaEncoderSettings::audioBitRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QMediaEncoderSettings12audioBitRateEv(
    const QMediaEncoderSettings *self) {
  return self->audioBitRate();
}

//  void QMediaEncoderSettings::setAudioBitRate(int bitrate)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings15setAudioBitRateEi(
    QMediaEncoderSettings *self,
    int bitrate) {
  self->setAudioBitRate(bitrate);
}

//  int QMediaEncoderSettings::audioChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QMediaEncoderSettings17audioChannelCountEv(
    const QMediaEncoderSettings *self) {
  return self->audioChannelCount();
}

//  void QMediaEncoderSettings::setAudioChannelCount(int channels)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings20setAudioChannelCountEi(
    QMediaEncoderSettings *self,
    int channels) {
  self->setAudioChannelCount(channels);
}

//  int QMediaEncoderSettings::audioSampleRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QMediaEncoderSettings15audioSampleRateEv(
    const QMediaEncoderSettings *self) {
  return self->audioSampleRate();
}

//  void QMediaEncoderSettings::setAudioSampleRate(int rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettings18setAudioSampleRateEi(
    QMediaEncoderSettings *self,
    int rate) {
  self->setAudioSampleRate(rate);
}

//  bool QMediaEncoderSettings::operator==(const QMediaEncoderSettings
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QMediaEncoderSettingseqERKS_(
    const QMediaEncoderSettings *self,
    const QMediaEncoderSettings *other) {
  return self->operator==(*other);
}

//  bool QMediaEncoderSettings::operator!=(const QMediaEncoderSettings
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QMediaEncoderSettingsneERKS_(
    const QMediaEncoderSettings *self,
    const QMediaEncoderSettings *other) {
  return self->operator!=(*other);
}

//  QMediaEncoderSettings::~QMediaEncoderSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMediaEncoderSettingsD1Ev(QMediaEncoderSettings *self) {
  delete self;
}
