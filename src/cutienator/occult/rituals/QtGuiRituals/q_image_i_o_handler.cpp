//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qimageiohandler.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qimageiohandler.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

//  QImageIOHandler::~QImageIOHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QImageIOHandlerD1Ev(QImageIOHandler *self) {
  delete self;
}

//  void QImageIOHandler::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QImageIOHandler9setDeviceEP9QIODevice(
    QImageIOHandler *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QImageIOHandler::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK15QImageIOHandler6deviceEv(
    const QImageIOHandler *self) {
  return self->device();
}

//  void QImageIOHandler::setFormat(const QByteArray &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QImageIOHandler9setFormatERK10QByteArray(
    QImageIOHandler *self,
    const QByteArray *format) {
  self->setFormat(*format);
}

//  void QImageIOHandler::setFormat(const QByteArray &format) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QImageIOHandler9setFormatERK10QByteArray(
    const QImageIOHandler *self,
    const QByteArray *format) {
  self->setFormat(*format);
}

//  QByteArray QImageIOHandler::format() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QImageIOHandler6formatEv(
    const QImageIOHandler *self) {
  return new QByteArray(self->format());
}

//  bool QImageIOHandler::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QImageIOHandler7canReadEv(const QImageIOHandler *self) {
  return self->canRead();
}

//  bool QImageIOHandler::read(QImage *image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QImageIOHandler4readEP6QImage(
    QImageIOHandler *self,
    QImage *image) {
  return self->read(image);
}

//  bool QImageIOHandler::write(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QImageIOHandler5writeERK6QImage(
    QImageIOHandler *self,
    const QImage *image) {
  return self->write(*image);
}

//  QVariant QImageIOHandler::option(ImageOption option) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QImageIOHandler6optionENS_11ImageOptionE(
    const QImageIOHandler *self,
    QImageIOHandler::ImageOption option) {
  return new QVariant(self->option(option));
}

//  void QImageIOHandler::setOption(ImageOption option, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QImageIOHandler9setOptionENS_11ImageOptionERK8QVariant(
    QImageIOHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->setOption(option, *value);
}

//  bool QImageIOHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QImageIOHandler14supportsOptionENS_11ImageOptionE(
    const QImageIOHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->supportsOption(option);
}

//  bool QImageIOHandler::jumpToNextImage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QImageIOHandler15jumpToNextImageEv(QImageIOHandler *self) {
  return self->jumpToNextImage();
}

//  bool QImageIOHandler::jumpToImage(int imageNumber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QImageIOHandler11jumpToImageEi(
    QImageIOHandler *self,
    int imageNumber) {
  return self->jumpToImage(imageNumber);
}

//  int QImageIOHandler::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QImageIOHandler9loopCountEv(const QImageIOHandler *self) {
  return self->loopCount();
}

//  int QImageIOHandler::imageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QImageIOHandler10imageCountEv(const QImageIOHandler *self) {
  return self->imageCount();
}

//  int QImageIOHandler::nextImageDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QImageIOHandler14nextImageDelayEv(
    const QImageIOHandler *self) {
  return self->nextImageDelay();
}

//  int QImageIOHandler::currentImageNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QImageIOHandler18currentImageNumberEv(
    const QImageIOHandler *self) {
  return self->currentImageNumber();
}

//  QRect QImageIOHandler::currentImageRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QImageIOHandler16currentImageRectEv(
    const QImageIOHandler *self) {
  return new QRect(self->currentImageRect());
}

//  bool QImageIOHandler::allocateImage(QSize size, QImage::Format format,
//      QImage *image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QImageIOHandler13allocateImageE5QSizeN6QImage6FormatEPS1_(
    const QSize *size,
    QImage::Format format,
    QImage *image) {
  return QImageIOHandler::allocateImage(*size, format, image);
}
