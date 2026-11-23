//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qimagereader.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qimagereader.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>

//  QString QImageReader::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QImageReader2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QImageReader::tr(sourceText, disambiguation, n));
}

//  QImageReader::QImageReader()
extern "C" Q_DECL_EXPORT
QImageReader *ritual_ZN12QImageReaderC1Ev() {
  return new QImageReader();
}

//  QImageReader::QImageReader(QIODevice *device, const QByteArray &format)
extern "C" Q_DECL_EXPORT
QImageReader *ritual_ZN12QImageReaderC1EP9QIODeviceRK10QByteArray(
    QIODevice *device,
    const QByteArray *format) {
  return new QImageReader(device, *format);
}

//  QImageReader::QImageReader(const QString &fileName, const QByteArray
//      &format)
extern "C" Q_DECL_EXPORT
QImageReader *ritual_ZN12QImageReaderC1ERK7QStringRK10QByteArray(
    const QString *fileName,
    const QByteArray *format) {
  return new QImageReader(*fileName, *format);
}

//  QImageReader::~QImageReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReaderD1Ev(QImageReader *self) {
  delete self;
}

//  void QImageReader::setFormat(const QByteArray &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader9setFormatERK10QByteArray(
    QImageReader *self,
    const QByteArray *format) {
  self->setFormat(*format);
}

//  QByteArray QImageReader::format() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QImageReader6formatEv(const QImageReader *self) {
  return new QByteArray(self->format());
}

//  void QImageReader::setAutoDetectImageFormat(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader24setAutoDetectImageFormatEb(
    QImageReader *self,
    bool enabled) {
  self->setAutoDetectImageFormat(enabled);
}

//  bool QImageReader::autoDetectImageFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageReader21autoDetectImageFormatEv(
    const QImageReader *self) {
  return self->autoDetectImageFormat();
}

//  void QImageReader::setDecideFormatFromContent(bool ignored)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader26setDecideFormatFromContentEb(
    QImageReader *self,
    bool ignored) {
  self->setDecideFormatFromContent(ignored);
}

//  bool QImageReader::decideFormatFromContent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageReader23decideFormatFromContentEv(
    const QImageReader *self) {
  return self->decideFormatFromContent();
}

//  void QImageReader::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader9setDeviceEP9QIODevice(
    QImageReader *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QImageReader::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK12QImageReader6deviceEv(const QImageReader *self) {
  return self->device();
}

//  void QImageReader::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader11setFileNameERK7QString(
    QImageReader *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QString QImageReader::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QImageReader8fileNameEv(const QImageReader *self) {
  return new QString(self->fileName());
}

//  QSize QImageReader::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QImageReader4sizeEv(const QImageReader *self) {
  return new QSize(self->size());
}

//  QSize QImageReader::effectiveSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QImageReader13effectiveSizeEv(const QImageReader *self) {
  return new QSize(self->effectiveSize());
}

//  QImage::Format QImageReader::imageFormat() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZNK12QImageReader11imageFormatEv(
    const QImageReader *self) {
  return self->imageFormat();
}

//  QStringList QImageReader::textKeys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QImageReader8textKeysEv(
    const QImageReader *self) {
  return new QList<QString>(self->textKeys());
}

//  QString QImageReader::text(const QString &key) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QImageReader4textERK7QString(
    const QImageReader *self,
    const QString *key) {
  return new QString(self->text(*key));
}

//  void QImageReader::setClipRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader11setClipRectERK5QRect(
    QImageReader *self,
    const QRect *rect) {
  self->setClipRect(*rect);
}

//  QRect QImageReader::clipRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QImageReader8clipRectEv(const QImageReader *self) {
  return new QRect(self->clipRect());
}

//  void QImageReader::setScaledSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader13setScaledSizeERK5QSize(
    QImageReader *self,
    const QSize *size) {
  self->setScaledSize(*size);
}

//  QSize QImageReader::scaledSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QImageReader10scaledSizeEv(const QImageReader *self) {
  return new QSize(self->scaledSize());
}

//  void QImageReader::setQuality(int quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader10setQualityEi(QImageReader *self, int quality) {
  self->setQuality(quality);
}

//  int QImageReader::quality() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QImageReader7qualityEv(const QImageReader *self) {
  return self->quality();
}

//  void QImageReader::setScaledClipRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader17setScaledClipRectERK5QRect(
    QImageReader *self,
    const QRect *rect) {
  self->setScaledClipRect(*rect);
}

//  QRect QImageReader::scaledClipRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QImageReader14scaledClipRectEv(const QImageReader *self) {
  return new QRect(self->scaledClipRect());
}

//  void QImageReader::setBackgroundColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader18setBackgroundColorERK6QColor(
    QImageReader *self,
    const QColor *color) {
  self->setBackgroundColor(*color);
}

//  QColor QImageReader::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QImageReader15backgroundColorEv(
    const QImageReader *self) {
  return new QColor(self->backgroundColor());
}

//  bool QImageReader::supportsAnimation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageReader17supportsAnimationEv(
    const QImageReader *self) {
  return self->supportsAnimation();
}

//  QImageIOHandler::Transformations QImageReader::transformation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QImageReader14transformationEv(const QImageReader *self) {
  return static_cast<int>(self->transformation().toInt());
}

//  void QImageReader::setAutoTransform(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader16setAutoTransformEb(
    QImageReader *self,
    bool enabled) {
  self->setAutoTransform(enabled);
}

//  bool QImageReader::autoTransform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageReader13autoTransformEv(const QImageReader *self) {
  return self->autoTransform();
}

//  QByteArray QImageReader::subType() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QImageReader7subTypeEv(const QImageReader *self) {
  return new QByteArray(self->subType());
}

//  QList<QByteArray> QImageReader::supportedSubTypes() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK12QImageReader17supportedSubTypesEv(
    const QImageReader *self) {
  return new QList<QByteArray>(self->supportedSubTypes());
}

//  bool QImageReader::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageReader7canReadEv(const QImageReader *self) {
  return self->canRead();
}

//  QImage QImageReader::read()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN12QImageReader4readEv(QImageReader *self) {
  return new QImage(self->read());
}

//  bool QImageReader::read(QImage *image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QImageReader4readEP6QImage(
    QImageReader *self,
    QImage *image) {
  return self->read(image);
}

//  bool QImageReader::jumpToNextImage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QImageReader15jumpToNextImageEv(QImageReader *self) {
  return self->jumpToNextImage();
}

//  bool QImageReader::jumpToImage(int imageNumber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QImageReader11jumpToImageEi(
    QImageReader *self,
    int imageNumber) {
  return self->jumpToImage(imageNumber);
}

//  int QImageReader::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QImageReader9loopCountEv(const QImageReader *self) {
  return self->loopCount();
}

//  int QImageReader::imageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QImageReader10imageCountEv(const QImageReader *self) {
  return self->imageCount();
}

//  int QImageReader::nextImageDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QImageReader14nextImageDelayEv(const QImageReader *self) {
  return self->nextImageDelay();
}

//  int QImageReader::currentImageNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QImageReader18currentImageNumberEv(
    const QImageReader *self) {
  return self->currentImageNumber();
}

//  QRect QImageReader::currentImageRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QImageReader16currentImageRectEv(
    const QImageReader *self) {
  return new QRect(self->currentImageRect());
}

//  ImageReaderError QImageReader::error() const
extern "C" Q_DECL_EXPORT
QImageReader::ImageReaderError ritual_ZNK12QImageReader5errorEv(
    const QImageReader *self) {
  return self->error();
}

//  QString QImageReader::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QImageReader11errorStringEv(const QImageReader *self) {
  return new QString(self->errorString());
}

//  bool QImageReader::supportsOption(QImageIOHandler::ImageOption option)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QImageReader14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QImageReader *self,
    QImageIOHandler::ImageOption option) {
  return self->supportsOption(option);
}

//  QByteArray QImageReader::imageFormat(const QString &fileName)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN12QImageReader11imageFormatERK7QString(
    const QString *fileName) {
  return new QByteArray(QImageReader::imageFormat(*fileName));
}

//  QByteArray QImageReader::imageFormat(QIODevice *device)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN12QImageReader11imageFormatEP9QIODevice(
    QIODevice *device) {
  return new QByteArray(QImageReader::imageFormat(device));
}

//  QList<QByteArray> QImageReader::supportedImageFormats()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN12QImageReader21supportedImageFormatsEv() {
  return new QList<QByteArray>(QImageReader::supportedImageFormats());
}

//  QList<QByteArray> QImageReader::supportedMimeTypes()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN12QImageReader18supportedMimeTypesEv() {
  return new QList<QByteArray>(QImageReader::supportedMimeTypes());
}

//  QList<QByteArray> QImageReader::imageFormatsForMimeType(const QByteArray
//      &mimeType)
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN12QImageReader23imageFormatsForMimeTypeERK10QByteArray(
    const QByteArray *mimeType) {
  return new QList<QByteArray>(
      QImageReader::imageFormatsForMimeType(
          *mimeType));
}

//  int QImageReader::allocationLimit()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QImageReader15allocationLimitEv() {
  return QImageReader::allocationLimit();
}

//  void QImageReader::setAllocationLimit(int mbLimit)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QImageReader18setAllocationLimitEi(int mbLimit) {
  QImageReader::setAllocationLimit(mbLimit);
}
