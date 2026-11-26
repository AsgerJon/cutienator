//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qmediaformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtMultimedia/qmediaformat.h>
#if QT_CONFIG(mimetype)
#include <QtCore/qmimetype.h>
#endif
#include <QtCore/qstring.h>
#include <QtCore/QList>
#include <QtMultimedia/QMediaFormat>

//  QMediaFormat::QMediaFormat(FileFormat format)
extern "C" Q_DECL_EXPORT
QMediaFormat *ritual_ZN12QMediaFormatC1ENS_10FileFormatE(
    QMediaFormat::FileFormat format) {
  return new QMediaFormat(format);
}

//  QMediaFormat::~QMediaFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaFormatD1Ev(QMediaFormat *self) {
  delete self;
}

//  QMediaFormat::QMediaFormat(const QMediaFormat &other)
extern "C" Q_DECL_EXPORT
QMediaFormat *ritual_ZN12QMediaFormatC1ERKS_(const QMediaFormat *other) {
  return new QMediaFormat(*other);
}

//  QMediaFormat &QMediaFormat::operator=(const QMediaFormat &other)
extern "C" Q_DECL_EXPORT
QMediaFormat *ritual_ZN12QMediaFormataSERKS_(
    QMediaFormat *self,
    const QMediaFormat *other) {
  return &(self->operator=(*other));
}

//  QMediaFormat::QMediaFormat(QMediaFormat &&other)
extern "C" Q_DECL_EXPORT
QMediaFormat *ritual_ZN12QMediaFormatC1EOS_(QMediaFormat *other) {
  return new QMediaFormat(std::move(*other));
}

//  QMediaFormat &QMediaFormat::operator=(QMediaFormat &&other)
extern "C" Q_DECL_EXPORT
QMediaFormat *ritual_ZN12QMediaFormataSEOS_(
    QMediaFormat *self,
    QMediaFormat *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QMediaFormat::swap(QMediaFormat &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaFormat4swapERS_(
    QMediaFormat *self,
    QMediaFormat *other) {
  self->swap(*other);
}

//  FileFormat QMediaFormat::fileFormat() const
extern "C" Q_DECL_EXPORT
QMediaFormat::FileFormat ritual_ZNK12QMediaFormat10fileFormatEv(
    const QMediaFormat *self) {
  return self->fileFormat();
}

//  void QMediaFormat::setFileFormat(FileFormat f)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaFormat13setFileFormatENS_10FileFormatE(
    QMediaFormat *self,
    QMediaFormat::FileFormat f) {
  self->setFileFormat(f);
}

//  void QMediaFormat::setVideoCodec(VideoCodec codec)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaFormat13setVideoCodecENS_10VideoCodecE(
    QMediaFormat *self,
    QMediaFormat::VideoCodec codec) {
  self->setVideoCodec(codec);
}

//  VideoCodec QMediaFormat::videoCodec() const
extern "C" Q_DECL_EXPORT
QMediaFormat::VideoCodec ritual_ZNK12QMediaFormat10videoCodecEv(
    const QMediaFormat *self) {
  return self->videoCodec();
}

//  void QMediaFormat::setAudioCodec(AudioCodec codec)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaFormat13setAudioCodecENS_10AudioCodecE(
    QMediaFormat *self,
    QMediaFormat::AudioCodec codec) {
  self->setAudioCodec(codec);
}

//  AudioCodec QMediaFormat::audioCodec() const
extern "C" Q_DECL_EXPORT
QMediaFormat::AudioCodec ritual_ZNK12QMediaFormat10audioCodecEv(
    const QMediaFormat *self) {
  return self->audioCodec();
}

//  bool QMediaFormat::isSupported(ConversionMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMediaFormat11isSupportedENS_14ConversionModeE(
    const QMediaFormat *self,
    QMediaFormat::ConversionMode mode) {
  return self->isSupported(mode);
}

#if QT_CONFIG(mimetype)
//  QMimeType QMediaFormat::mimeType() const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK12QMediaFormat8mimeTypeEv(const QMediaFormat *self) {
  return new QMimeType(self->mimeType());
}
#endif  // QT_CONFIG(mimetype)

//  QList<FileFormat> QMediaFormat::supportedFileFormats(ConversionMode m)
extern "C" Q_DECL_EXPORT
QList<QMediaFormat::FileFormat> *ritual_ZN12QMediaFormat20supportedFileFormatsENS_14ConversionModeE(
    QMediaFormat *self,
    QMediaFormat::ConversionMode m) {
  return new QList<QMediaFormat::FileFormat>(self->supportedFileFormats(m));
}

//  QList<VideoCodec> QMediaFormat::supportedVideoCodecs(ConversionMode m)
extern "C" Q_DECL_EXPORT
QList<QMediaFormat::VideoCodec> *ritual_ZN12QMediaFormat20supportedVideoCodecsENS_14ConversionModeE(
    QMediaFormat *self,
    QMediaFormat::ConversionMode m) {
  return new QList<QMediaFormat::VideoCodec>(self->supportedVideoCodecs(m));
}

//  QList<AudioCodec> QMediaFormat::supportedAudioCodecs(ConversionMode m)
extern "C" Q_DECL_EXPORT
QList<QMediaFormat::AudioCodec> *ritual_ZN12QMediaFormat20supportedAudioCodecsENS_14ConversionModeE(
    QMediaFormat *self,
    QMediaFormat::ConversionMode m) {
  return new QList<QMediaFormat::AudioCodec>(self->supportedAudioCodecs(m));
}

//  QString QMediaFormat::fileFormatName(FileFormat fileFormat)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QMediaFormat14fileFormatNameENS_10FileFormatE(
    QMediaFormat::FileFormat fileFormat) {
  return new QString(QMediaFormat::fileFormatName(fileFormat));
}

//  QString QMediaFormat::audioCodecName(AudioCodec codec)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QMediaFormat14audioCodecNameENS_10AudioCodecE(
    QMediaFormat::AudioCodec codec) {
  return new QString(QMediaFormat::audioCodecName(codec));
}

//  QString QMediaFormat::videoCodecName(VideoCodec codec)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QMediaFormat14videoCodecNameENS_10VideoCodecE(
    QMediaFormat::VideoCodec codec) {
  return new QString(QMediaFormat::videoCodecName(codec));
}

//  QString QMediaFormat::fileFormatDescription(QMediaFormat::FileFormat
//      fileFormat)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QMediaFormat21fileFormatDescriptionENS_10FileFormatE(
    QMediaFormat::FileFormat fileFormat) {
  return new QString(QMediaFormat::fileFormatDescription(fileFormat));
}

//  QString QMediaFormat::audioCodecDescription(QMediaFormat::AudioCodec
//      codec)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QMediaFormat21audioCodecDescriptionENS_10AudioCodecE(
    QMediaFormat::AudioCodec codec) {
  return new QString(QMediaFormat::audioCodecDescription(codec));
}

//  QString QMediaFormat::videoCodecDescription(QMediaFormat::VideoCodec
//      codec)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QMediaFormat21videoCodecDescriptionENS_10VideoCodecE(
    QMediaFormat::VideoCodec codec) {
  return new QString(QMediaFormat::videoCodecDescription(codec));
}

//  bool QMediaFormat::operator==(const QMediaFormat &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMediaFormateqERKS_(
    const QMediaFormat *self,
    const QMediaFormat *other) {
  return self->operator==(*other);
}

//  bool QMediaFormat::operator!=(const QMediaFormat &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMediaFormatneERKS_(
    const QMediaFormat *self,
    const QMediaFormat *other) {
  return self->operator!=(*other);
}

//  void QMediaFormat::resolveForEncoding(ResolveFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMediaFormat18resolveForEncodingENS_12ResolveFlagsE(
    QMediaFormat *self,
    QMediaFormat::ResolveFlags flags) {
  self->resolveForEncoding(flags);
}

//  a QList<QMediaFormat::FileFormat> a ritual of QMediaFormat gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMediaFormat__QList_QMediaFormat_FileFormat(
    QList<QMediaFormat::FileFormat> *self) {
  delete self;
}

//  a QList<QMediaFormat::VideoCodec> a ritual of QMediaFormat gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMediaFormat__QList_QMediaFormat_VideoCodec(
    QList<QMediaFormat::VideoCodec> *self) {
  delete self;
}

//  a QList<QMediaFormat::AudioCodec> a ritual of QMediaFormat gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMediaFormat__QList_QMediaFormat_AudioCodec(
    QList<QMediaFormat::AudioCodec> *self) {
  delete self;
}
