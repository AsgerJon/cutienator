//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaformatinfo_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaformatinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qmediaformat.h>

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
