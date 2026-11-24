//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qvideoframeformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qvideoframeformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtGui/qmatrix4x4.h>

//  QVideoFrameFormat::QVideoFrameFormat()
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZN17QVideoFrameFormatC1Ev() {
  return new QVideoFrameFormat();
}

//  QVideoFrameFormat::QVideoFrameFormat(const QSize &size, PixelFormat
//      pixelFormat)
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZN17QVideoFrameFormatC1ERK5QSizeNS_11PixelFormatE(
    const QSize *size,
    QVideoFrameFormat::PixelFormat pixelFormat) {
  return new QVideoFrameFormat(*size, pixelFormat);
}

//  QVideoFrameFormat::QVideoFrameFormat(const QVideoFrameFormat &format)
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZN17QVideoFrameFormatC1ERKS_(
    const QVideoFrameFormat *format) {
  return new QVideoFrameFormat(*format);
}

//  QVideoFrameFormat::~QVideoFrameFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormatD1Ev(QVideoFrameFormat *self) {
  delete self;
}

//  void QVideoFrameFormat::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat6detachEv(QVideoFrameFormat *self) {
  self->detach();
}

//  bool QVideoFrameFormat::operator==(const QVideoFrameFormat &format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QVideoFrameFormateqERKS_(
    const QVideoFrameFormat *self,
    const QVideoFrameFormat *format) {
  return self->operator==(*format);
}

//  bool QVideoFrameFormat::operator!=(const QVideoFrameFormat &format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QVideoFrameFormatneERKS_(
    const QVideoFrameFormat *self,
    const QVideoFrameFormat *format) {
  return self->operator!=(*format);
}

//  bool QVideoFrameFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QVideoFrameFormat7isValidEv(const QVideoFrameFormat *self) {
  return self->isValid();
}

//  QVideoFrameFormat::PixelFormat QVideoFrameFormat::pixelFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::PixelFormat ritual_ZNK17QVideoFrameFormat11pixelFormatEv(
    const QVideoFrameFormat *self) {
  return self->pixelFormat();
}

//  QSize QVideoFrameFormat::frameSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QVideoFrameFormat9frameSizeEv(
    const QVideoFrameFormat *self) {
  return new QSize(self->frameSize());
}

//  void QVideoFrameFormat::setFrameSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat12setFrameSizeERK5QSize(
    QVideoFrameFormat *self,
    const QSize *size) {
  self->setFrameSize(*size);
}

//  void QVideoFrameFormat::setFrameSize(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat12setFrameSizeEii(
    QVideoFrameFormat *self,
    int width,
    int height) {
  self->setFrameSize(width, height);
}

//  int QVideoFrameFormat::frameWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QVideoFrameFormat10frameWidthEv(
    const QVideoFrameFormat *self) {
  return self->frameWidth();
}

//  int QVideoFrameFormat::frameHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QVideoFrameFormat11frameHeightEv(
    const QVideoFrameFormat *self) {
  return self->frameHeight();
}

//  int QVideoFrameFormat::planeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QVideoFrameFormat10planeCountEv(
    const QVideoFrameFormat *self) {
  return self->planeCount();
}

//  QRect QVideoFrameFormat::viewport() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QVideoFrameFormat8viewportEv(
    const QVideoFrameFormat *self) {
  return new QRect(self->viewport());
}

//  void QVideoFrameFormat::setViewport(const QRect &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat11setViewportERK5QRect(
    QVideoFrameFormat *self,
    const QRect *viewport) {
  self->setViewport(*viewport);
}

//  Direction QVideoFrameFormat::scanLineDirection() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::Direction ritual_ZNK17QVideoFrameFormat17scanLineDirectionEv(
    const QVideoFrameFormat *self) {
  return self->scanLineDirection();
}

//  void QVideoFrameFormat::setScanLineDirection(Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat20setScanLineDirectionENS_9DirectionE(
    QVideoFrameFormat *self,
    QVideoFrameFormat::Direction direction) {
  self->setScanLineDirection(direction);
}

#if QT_DEPRECATED_SINCE(6, 8)
//  qreal QVideoFrameFormat::frameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QVideoFrameFormat9frameRateEv(
    const QVideoFrameFormat *self) {
  return self->frameRate();
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

#if QT_DEPRECATED_SINCE(6, 8)
//  void QVideoFrameFormat::setFrameRate(qreal rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat12setFrameRateEd(
    QVideoFrameFormat *self,
    qreal rate) {
  self->setFrameRate(rate);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  qreal QVideoFrameFormat::streamFrameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QVideoFrameFormat15streamFrameRateEv(
    const QVideoFrameFormat *self) {
  return self->streamFrameRate();
}

//  void QVideoFrameFormat::setStreamFrameRate(qreal rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat18setStreamFrameRateEd(
    QVideoFrameFormat *self,
    qreal rate) {
  self->setStreamFrameRate(rate);
}

#if QT_DEPRECATED_SINCE(6, 4)
//  YCbCrColorSpace QVideoFrameFormat::yCbCrColorSpace() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::YCbCrColorSpace ritual_ZNK17QVideoFrameFormat15yCbCrColorSpaceEv(
    const QVideoFrameFormat *self) {
  return self->yCbCrColorSpace();
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  void QVideoFrameFormat::setYCbCrColorSpace(YCbCrColorSpace colorSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat18setYCbCrColorSpaceENS_15YCbCrColorSpaceE(
    QVideoFrameFormat *self,
    QVideoFrameFormat::YCbCrColorSpace colorSpace) {
  self->setYCbCrColorSpace(colorSpace);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  ColorSpace QVideoFrameFormat::colorSpace() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::ColorSpace ritual_ZNK17QVideoFrameFormat10colorSpaceEv(
    const QVideoFrameFormat *self) {
  return self->colorSpace();
}

//  void QVideoFrameFormat::setColorSpace(ColorSpace colorSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat13setColorSpaceENS_10ColorSpaceE(
    QVideoFrameFormat *self,
    QVideoFrameFormat::ColorSpace colorSpace) {
  self->setColorSpace(colorSpace);
}

//  ColorTransfer QVideoFrameFormat::colorTransfer() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::ColorTransfer ritual_ZNK17QVideoFrameFormat13colorTransferEv(
    const QVideoFrameFormat *self) {
  return self->colorTransfer();
}

//  void QVideoFrameFormat::setColorTransfer(ColorTransfer colorTransfer)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat16setColorTransferENS_13ColorTransferE(
    QVideoFrameFormat *self,
    QVideoFrameFormat::ColorTransfer colorTransfer) {
  self->setColorTransfer(colorTransfer);
}

//  ColorRange QVideoFrameFormat::colorRange() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::ColorRange ritual_ZNK17QVideoFrameFormat10colorRangeEv(
    const QVideoFrameFormat *self) {
  return self->colorRange();
}

//  void QVideoFrameFormat::setColorRange(ColorRange range)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat13setColorRangeENS_10ColorRangeE(
    QVideoFrameFormat *self,
    QVideoFrameFormat::ColorRange range) {
  self->setColorRange(range);
}

//  bool QVideoFrameFormat::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QVideoFrameFormat10isMirroredEv(
    const QVideoFrameFormat *self) {
  return self->isMirrored();
}

//  void QVideoFrameFormat::setMirrored(bool mirrored)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat11setMirroredEb(
    QVideoFrameFormat *self,
    bool mirrored) {
  self->setMirrored(mirrored);
}

//  QtVideo::Rotation QVideoFrameFormat::rotation() const
extern "C" Q_DECL_EXPORT
QtVideo::Rotation ritual_ZNK17QVideoFrameFormat8rotationEv(
    const QVideoFrameFormat *self) {
  return self->rotation();
}

//  void QVideoFrameFormat::setRotation(QtVideo::Rotation rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat11setRotationEN7QtVideo8RotationE(
    QVideoFrameFormat *self,
    QtVideo::Rotation rotation) {
  self->setRotation(rotation);
}

//  QString QVideoFrameFormat::vertexShaderFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QVideoFrameFormat20vertexShaderFileNameEv(
    const QVideoFrameFormat *self) {
  return new QString(self->vertexShaderFileName());
}

//  QString QVideoFrameFormat::fragmentShaderFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QVideoFrameFormat22fragmentShaderFileNameEv(
    const QVideoFrameFormat *self) {
  return new QString(self->fragmentShaderFileName());
}

//  void QVideoFrameFormat::updateUniformData(QByteArray *dst, const
//      QVideoFrame &frame, const QMatrix4x4 &transform, float opacity) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QVideoFrameFormat17updateUniformDataEP10QByteArrayRK11QVideoFrameRK10QMatrix4x4f(
    const QVideoFrameFormat *self,
    QByteArray *dst,
    const QVideoFrame *frame,
    const QMatrix4x4 *transform,
    float opacity) {
  self->updateUniformData(dst, *frame, *transform, opacity);
}

//  float QVideoFrameFormat::maxLuminance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QVideoFrameFormat12maxLuminanceEv(
    const QVideoFrameFormat *self) {
  return self->maxLuminance();
}

//  void QVideoFrameFormat::setMaxLuminance(float lum)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVideoFrameFormat15setMaxLuminanceEf(
    QVideoFrameFormat *self,
    float lum) {
  self->setMaxLuminance(lum);
}

//  PixelFormat QVideoFrameFormat::pixelFormatFromImageFormat(QImage::Format
//      format)
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::PixelFormat ritual_ZN17QVideoFrameFormat26pixelFormatFromImageFormatEN6QImage6FormatE(
    QImage::Format format) {
  return QVideoFrameFormat::pixelFormatFromImageFormat(format);
}

//  QImage::Format QVideoFrameFormat::imageFormatFromPixelFormat(PixelFormat
//      format)
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZN17QVideoFrameFormat26imageFormatFromPixelFormatENS_11PixelFormatE(
    QVideoFrameFormat::PixelFormat format) {
  return QVideoFrameFormat::imageFormatFromPixelFormat(format);
}

//  QString
//      QVideoFrameFormat::pixelFormatToString(QVideoFrameFormat::PixelFormat
//      pixelFormat)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QVideoFrameFormat19pixelFormatToStringENS_11PixelFormatE(
    QVideoFrameFormat::PixelFormat pixelFormat) {
  return new QString(QVideoFrameFormat::pixelFormatToString(pixelFormat));
}
