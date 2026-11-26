//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaformatinfo_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaformatinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qmediaformat.h>
#include <QtCore/QList>
#include <QtMultimedia/QMediaFormat>

//  QPlatformMediaFormatInfo::QPlatformMediaFormatInfo()
extern "C" Q_DECL_EXPORT
QPlatformMediaFormatInfo *ritual_ZN24QPlatformMediaFormatInfoC1Ev() {
  return new QPlatformMediaFormatInfo();
}

//  QPlatformMediaFormatInfo::~QPlatformMediaFormatInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlatformMediaFormatInfoD1Ev(
    QPlatformMediaFormatInfo *self) {
  delete self;
}

//  QList<QMediaFormat::FileFormat>
//      QPlatformMediaFormatInfo::supportedFileFormats(const QMediaFormat
//      &constraints, QMediaFormat::ConversionMode m) const
extern "C" Q_DECL_EXPORT
QList<QMediaFormat::FileFormat> *ritual_ZNK24QPlatformMediaFormatInfo20supportedFileFormatsERK12QMediaFormatNS0_14ConversionModeE(
    const QPlatformMediaFormatInfo *self,
    const QMediaFormat *constraints,
    QMediaFormat::ConversionMode m) {
  return new QList<QMediaFormat::FileFormat>(
      self->supportedFileFormats(
          *constraints,
          m));
}

//  QList<QMediaFormat::AudioCodec>
//      QPlatformMediaFormatInfo::supportedAudioCodecs(const QMediaFormat
//      &constraints, QMediaFormat::ConversionMode m) const
extern "C" Q_DECL_EXPORT
QList<QMediaFormat::AudioCodec> *ritual_ZNK24QPlatformMediaFormatInfo20supportedAudioCodecsERK12QMediaFormatNS0_14ConversionModeE(
    const QPlatformMediaFormatInfo *self,
    const QMediaFormat *constraints,
    QMediaFormat::ConversionMode m) {
  return new QList<QMediaFormat::AudioCodec>(
      self->supportedAudioCodecs(
          *constraints,
          m));
}

//  QList<QMediaFormat::VideoCodec>
//      QPlatformMediaFormatInfo::supportedVideoCodecs(const QMediaFormat
//      &constraints, QMediaFormat::ConversionMode m) const
extern "C" Q_DECL_EXPORT
QList<QMediaFormat::VideoCodec> *ritual_ZNK24QPlatformMediaFormatInfo20supportedVideoCodecsERK12QMediaFormatNS0_14ConversionModeE(
    const QPlatformMediaFormatInfo *self,
    const QMediaFormat *constraints,
    QMediaFormat::ConversionMode m) {
  return new QList<QMediaFormat::VideoCodec>(
      self->supportedVideoCodecs(
          *constraints,
          m));
}

//  bool QPlatformMediaFormatInfo::isSupported(const QMediaFormat &format,
//      QMediaFormat::ConversionMode m) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QPlatformMediaFormatInfo11isSupportedERK12QMediaFormatNS0_14ConversionModeE(
    const QPlatformMediaFormatInfo *self,
    const QMediaFormat *format,
    QMediaFormat::ConversionMode m) {
  return self->isSupported(*format, m);
}

//  void QPlatformMediaFormatInfo::fixupCodecMaps()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlatformMediaFormatInfo14fixupCodecMapsEv(
    QPlatformMediaFormatInfo *self) {
  self->fixupCodecMaps();
}

//  a QList<QMediaFormat::FileFormat> a ritual of QPlatformMediaFormatInfo
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaFormatInfo__QList_QMediaFormat_FileFormat(
    QList<QMediaFormat::FileFormat> *self) {
  delete self;
}

//  a QList<QMediaFormat::AudioCodec> a ritual of QPlatformMediaFormatInfo
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaFormatInfo__QList_QMediaFormat_AudioCodec(
    QList<QMediaFormat::AudioCodec> *self) {
  delete self;
}

//  a QList<QMediaFormat::VideoCodec> a ritual of QPlatformMediaFormatInfo
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformMediaFormatInfo__QList_QMediaFormat_VideoCodec(
    QList<QMediaFormat::VideoCodec> *self) {
  delete self;
}
