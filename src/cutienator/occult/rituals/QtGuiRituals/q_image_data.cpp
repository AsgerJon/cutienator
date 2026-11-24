//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qimage_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>

//  QImageData::QImageData()
extern "C" Q_DECL_EXPORT
QImageData *ritual_ZN10QImageDataC1Ev() {
  return new QImageData();
}

//  QImageData::~QImageData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QImageDataD1Ev(QImageData *self) {
  delete self;
}

//  QImageData *QImageData::create(const QSize &size, QImage::Format format)
extern "C" Q_DECL_EXPORT
QImageData *ritual_ZN10QImageData6createERK5QSizeN6QImage6FormatE(
    const QSize *size,
    QImage::Format format) {
  return QImageData::create(*size, format);
}

//  const QImageData *QImageData::get(const QImage &img)
extern "C" Q_DECL_EXPORT
const QImageData *ritual_ZN10QImageData3getERK6QImage(const QImage *img) {
  return QImageData::get(*img);
}

//  bool QImageData::checkForAlphaPixels() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QImageData19checkForAlphaPixelsEv(const QImageData *self) {
  return self->checkForAlphaPixels();
}

//  bool QImageData::convertInPlace(QImage::Format newFormat,
//      Qt::ImageConversionFlags a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QImageData14convertInPlaceEN6QImage6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    QImageData *self,
    QImage::Format newFormat,
    int a1) {
  return self->convertInPlace(
      newFormat,
      QFlags<Qt::ImageConversionFlag>::fromInt(a1));
}

//  bool QImageData::doImageIO(const QImage *image, QImageWriter *io, int
//      quality) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QImageData9doImageIOEPK6QImageP12QImageWriteri(
    const QImageData *self,
    const QImage *image,
    QImageWriter *io,
    int quality) {
  return self->doImageIO(image, io, quality);
}

//  ImageSizeParameters QImageData::calculateImageParameters(qsizetype width,
//      qsizetype height, qsizetype depth)
extern "C" Q_DECL_EXPORT
QImageData::ImageSizeParameters *ritual_ZN10QImageData24calculateImageParametersExxx(
    qsizetype width,
    qsizetype height,
    qsizetype depth) {
  return new QImageData::ImageSizeParameters(
      QImageData::calculateImageParameters(
          width,
          height,
          depth));
}
