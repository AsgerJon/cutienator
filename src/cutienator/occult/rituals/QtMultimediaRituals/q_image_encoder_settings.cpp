//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformimagecapture_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformimagecapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>

//  bool QImageEncoderSettings::operator==(const QImageEncoderSettings
//      &other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QImageEncoderSettingseqERKS_(
    QImageEncoderSettings *self,
    const QImageEncoderSettings *other) {
  return self->operator==(*other);
}

//  bool QImageEncoderSettings::operator!=(const QImageEncoderSettings
//      &other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QImageEncoderSettingsneERKS_(
    QImageEncoderSettings *self,
    const QImageEncoderSettings *other) {
  return self->operator!=(*other);
}

//  QImageCapture::FileFormat QImageEncoderSettings::format() const
extern "C" Q_DECL_EXPORT
QImageCapture::FileFormat ritual_ZNK21QImageEncoderSettings6formatEv(
    const QImageEncoderSettings *self) {
  return self->format();
}

//  void QImageEncoderSettings::setFormat(QImageCapture::FileFormat f)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QImageEncoderSettings9setFormatEN13QImageCapture10FileFormatE(
    QImageEncoderSettings *self,
    QImageCapture::FileFormat f) {
  self->setFormat(f);
}

//  QSize QImageEncoderSettings::resolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QImageEncoderSettings10resolutionEv(
    const QImageEncoderSettings *self) {
  return new QSize(self->resolution());
}

//  void QImageEncoderSettings::setResolution(const QSize &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QImageEncoderSettings13setResolutionERK5QSize(
    QImageEncoderSettings *self,
    const QSize *s) {
  self->setResolution(*s);
}

//  void QImageEncoderSettings::setResolution(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QImageEncoderSettings13setResolutionEii(
    QImageEncoderSettings *self,
    int width,
    int height) {
  self->setResolution(width, height);
}

//  QImageCapture::Quality QImageEncoderSettings::quality() const
extern "C" Q_DECL_EXPORT
QImageCapture::Quality ritual_ZNK21QImageEncoderSettings7qualityEv(
    const QImageEncoderSettings *self) {
  return self->quality();
}

//  void QImageEncoderSettings::setQuality(QImageCapture::Quality quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QImageEncoderSettings10setQualityEN13QImageCapture7QualityE(
    QImageEncoderSettings *self,
    QImageCapture::Quality quality) {
  self->setQuality(quality);
}

//  QImageEncoderSettings::~QImageEncoderSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QImageEncoderSettingsD1Ev(QImageEncoderSettings *self) {
  delete self;
}
