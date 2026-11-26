//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qimageiohandler.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qimageiohandler.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QImageIOHandler that Python can take functions over in. Every QImageIOHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQImageIOHandlerCall0)(const void *, int *);
typedef bool (*CuteQImageIOHandlerCall1)(const void *, QImage *, int *);
typedef bool (*CuteQImageIOHandlerCall2)(const void *, const QImage *, int *);
typedef const QVariant * (*CuteQImageIOHandlerCall3)(const void *, int, int *);
typedef void (*CuteQImageIOHandlerCall4)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQImageIOHandlerCall5)(const void *, int, int *);
typedef bool (*CuteQImageIOHandlerCall6)(const void *, int *);
typedef bool (*CuteQImageIOHandlerCall7)(const void *, int, int *);
typedef int (*CuteQImageIOHandlerCall8)(const void *, int *);
typedef int (*CuteQImageIOHandlerCall9)(const void *, int *);
typedef int (*CuteQImageIOHandlerCall10)(const void *, int *);
typedef int (*CuteQImageIOHandlerCall11)(const void *, int *);
typedef const QRect * (*CuteQImageIOHandlerCall12)(const void *, int *);
class CuteQImageIOHandler : public QImageIOHandler {
public:
  using QImageIOHandler::QImageIOHandler;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QImageIOHandler7canReadEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QImageIOHandler4readEP6QImage")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QImageIOHandler5writeERK6QImage")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QImageIOHandler6optionENS_11ImageOptionE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QImageIOHandler9setOptionENS_11ImageOptionERK8QVariant")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QImageIOHandler14supportsOptionENS_11ImageOptionE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QImageIOHandler15jumpToNextImageEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QImageIOHandler11jumpToImageEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QImageIOHandler9loopCountEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QImageIOHandler10imageCountEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QImageIOHandler14nextImageDelayEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QImageIOHandler18currentImageNumberEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QImageIOHandler16currentImageRectEv")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  bool QImageIOHandler::canRead() const
  bool canRead() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQImageIOHandlerCall0 call = reinterpret_cast<CuteQImageIOHandlerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QImageIOHandler::read(QImage *image)
  bool read(QImage *image) override {
    if (taken[1]) {
      int handled = 0;
      CuteQImageIOHandlerCall1 call = reinterpret_cast<CuteQImageIOHandlerCall1>(taken[1]);
      bool given = call(this, image, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QImageIOHandler::write(const QImage &image)
  bool write(const QImage &image) override {
    if (taken[2]) {
      int handled = 0;
      CuteQImageIOHandlerCall2 call = reinterpret_cast<CuteQImageIOHandlerCall2>(taken[2]);
      bool given = call(this, &image, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::write(image);
  }

  //  QVariant QImageIOHandler::option(ImageOption option) const
  QVariant option(QImageIOHandler::ImageOption option) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQImageIOHandlerCall3 call = reinterpret_cast<CuteQImageIOHandlerCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(option), &handled);
      if (handled && given) return *given;
    }
    return QImageIOHandler::option(option);
  }

  //  void QImageIOHandler::setOption(ImageOption option, const QVariant
  //      &value)
  void setOption(
      QImageIOHandler::ImageOption option,
      const QVariant &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQImageIOHandlerCall4 call = reinterpret_cast<CuteQImageIOHandlerCall4>(taken[4]);
      call(this, static_cast<int>(option), &value, &handled);
      if (handled) return;
    }
    QImageIOHandler::setOption(option, value);
  }

  //  bool QImageIOHandler::supportsOption(ImageOption option) const
  bool supportsOption(QImageIOHandler::ImageOption option) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQImageIOHandlerCall5 call = reinterpret_cast<CuteQImageIOHandlerCall5>(taken[5]);
      bool given = call(this, static_cast<int>(option), &handled);
      if (handled) return given;
    }
    return QImageIOHandler::supportsOption(option);
  }

  //  bool QImageIOHandler::jumpToNextImage()
  bool jumpToNextImage() override {
    if (taken[6]) {
      int handled = 0;
      CuteQImageIOHandlerCall6 call = reinterpret_cast<CuteQImageIOHandlerCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::jumpToNextImage();
  }

  //  bool QImageIOHandler::jumpToImage(int imageNumber)
  bool jumpToImage(int imageNumber) override {
    if (taken[7]) {
      int handled = 0;
      CuteQImageIOHandlerCall7 call = reinterpret_cast<CuteQImageIOHandlerCall7>(taken[7]);
      bool given = call(this, imageNumber, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::jumpToImage(imageNumber);
  }

  //  int QImageIOHandler::loopCount() const
  int loopCount() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQImageIOHandlerCall8 call = reinterpret_cast<CuteQImageIOHandlerCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::loopCount();
  }

  //  int QImageIOHandler::imageCount() const
  int imageCount() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQImageIOHandlerCall9 call = reinterpret_cast<CuteQImageIOHandlerCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::imageCount();
  }

  //  int QImageIOHandler::nextImageDelay() const
  int nextImageDelay() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQImageIOHandlerCall10 call = reinterpret_cast<CuteQImageIOHandlerCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::nextImageDelay();
  }

  //  int QImageIOHandler::currentImageNumber() const
  int currentImageNumber() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQImageIOHandlerCall11 call = reinterpret_cast<CuteQImageIOHandlerCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::currentImageNumber();
  }

  //  QRect QImageIOHandler::currentImageRect() const
  QRect currentImageRect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQImageIOHandlerCall12 call = reinterpret_cast<CuteQImageIOHandlerCall12>(taken[12]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QImageIOHandler::currentImageRect();
  }
};

//  QImageIOHandlerPrivate *QImageIOHandler::d_func()
extern "C" Q_DECL_EXPORT
QImageIOHandlerPrivate *ritual_ZN15QImageIOHandler6d_funcEv(
    QImageIOHandler *self) {
  return self->d_func();
}

//  const QImageIOHandlerPrivate *QImageIOHandler::d_func() const
extern "C" Q_DECL_EXPORT
const QImageIOHandlerPrivate *ritual_ZNK15QImageIOHandler6d_funcEv(
    const QImageIOHandler *self) {
  return self->d_func();
}

//  QImageIOHandler::QImageIOHandler()
extern "C" Q_DECL_EXPORT
QImageIOHandler *ritual_ZN15QImageIOHandlerC1Ev() {
  return new CuteQImageIOHandler();
}

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

//  QImageIOHandler::QImageIOHandler(QImageIOHandlerPrivate &dd)
extern "C" Q_DECL_EXPORT
QImageIOHandler *ritual_ZN15QImageIOHandlerC1ER22QImageIOHandlerPrivate(
    QImageIOHandlerPrivate *dd) {
  return new CuteQImageIOHandler(*dd);
}

//  a Python function taken by a CuteQImageIOHandler, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QImageIOHandler(
    QImageIOHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQImageIOHandler *>(self)->take(key, call);
}

//  bool QImageIOHandler::write(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QImageIOHandler5writeERK6QImage(
    QImageIOHandler *self,
    const QImage *image) {
  return self->QImageIOHandler::write(*image);
}

//  QVariant QImageIOHandler::option(ImageOption option) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK15QImageIOHandler6optionENS_11ImageOptionE(
    const QImageIOHandler *self,
    QImageIOHandler::ImageOption option) {
  return new QVariant(self->QImageIOHandler::option(option));
}

//  void QImageIOHandler::setOption(ImageOption option, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QImageIOHandler9setOptionENS_11ImageOptionERK8QVariant(
    QImageIOHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->QImageIOHandler::setOption(option, *value);
}

//  bool QImageIOHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QImageIOHandler14supportsOptionENS_11ImageOptionE(
    const QImageIOHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->QImageIOHandler::supportsOption(option);
}

//  bool QImageIOHandler::jumpToNextImage()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QImageIOHandler15jumpToNextImageEv(
    QImageIOHandler *self) {
  return self->QImageIOHandler::jumpToNextImage();
}

//  bool QImageIOHandler::jumpToImage(int imageNumber)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QImageIOHandler11jumpToImageEi(
    QImageIOHandler *self,
    int imageNumber) {
  return self->QImageIOHandler::jumpToImage(imageNumber);
}

//  int QImageIOHandler::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QImageIOHandler9loopCountEv(
    const QImageIOHandler *self) {
  return self->QImageIOHandler::loopCount();
}

//  int QImageIOHandler::imageCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QImageIOHandler10imageCountEv(
    const QImageIOHandler *self) {
  return self->QImageIOHandler::imageCount();
}

//  int QImageIOHandler::nextImageDelay() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QImageIOHandler14nextImageDelayEv(
    const QImageIOHandler *self) {
  return self->QImageIOHandler::nextImageDelay();
}

//  int QImageIOHandler::currentImageNumber() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QImageIOHandler18currentImageNumberEv(
    const QImageIOHandler *self) {
  return self->QImageIOHandler::currentImageNumber();
}

//  QRect QImageIOHandler::currentImageRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK15QImageIOHandler16currentImageRectEv(
    const QImageIOHandler *self) {
  return new QRect(self->QImageIOHandler::currentImageRect());
}
