//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpnghandler_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the includes of 'png.h' and
//  'pngconf.h', taken with Qt's code from qpnghandler.cpp, stand under
//  '__has_include(<png.h>)', because a Qt that builds its own libpng
//  into QtGui may leave no 'png.h' on the include path (the
//  Apple-silicon Mac had none), and no code here uses libpng. Kept as
//  it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(png)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpnghandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qpnghandler_p.h>
#ifndef QT_NO_IMAGEFORMAT_PNG
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdebug.h>
#include <QtCore/qiodevice.h>
#include <QtGui/qimage.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qvariant.h>
#include <QtGui/private/qimage_p.h> // for qt_getImageText
#include <QtGui/qcolorspace.h>
#include <QtGui/private/qcolorspace_p.h>
#if __has_include(<png.h>)
#include <png.h>
#include <pngconf.h>
#endif  // __has_include(<png.h>)
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/image/qpnghandler.cpp, line 1076, as _ZNK11QPngHandler14supportsOptionEN15QImageIOHandler11ImageOptionE
#if !defined(QT_NO_IMAGEFORMAT_PNG)
inline bool QPngHandler::supportsOption(ImageOption option) const
{
    return option == Gamma
        || option == Description
        || option == ImageFormat
        || option == Quality
        || option == CompressionRatio
        || option == Size;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
//  -----------------------------------------------------------------------

//  A QPngHandler that Python can take functions over in. Every QPngHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_IMAGEFORMAT_PNG)
typedef bool (*CuteQPngHandlerCall0)(const void *, int *);
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
typedef bool (*CuteQPngHandlerCall1)(const void *, QImage *, int *);
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
typedef bool (*CuteQPngHandlerCall2)(const void *, const QImage *, int *);
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
typedef const QVariant * (*CuteQPngHandlerCall3)(const void *, int, int *);
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
typedef void (*CuteQPngHandlerCall4)(const void *, int, const QVariant *, int *);
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
typedef bool (*CuteQPngHandlerCall5)(const void *, int, int *);
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
typedef bool (*CuteQPngHandlerCall6)(const void *, int *);
typedef bool (*CuteQPngHandlerCall7)(const void *, int, int *);
typedef int (*CuteQPngHandlerCall8)(const void *, int *);
typedef int (*CuteQPngHandlerCall9)(const void *, int *);
typedef int (*CuteQPngHandlerCall10)(const void *, int *);
typedef int (*CuteQPngHandlerCall11)(const void *, int *);
typedef const QRect * (*CuteQPngHandlerCall12)(const void *, int *);
class CuteQPngHandler : public QPngHandler {
public:
  using QPngHandler::QPngHandler;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_IMAGEFORMAT_PNG)
    if (!std::strcmp(key, "_ZNK15QImageIOHandler7canReadEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
    if (!std::strcmp(key, "_ZN15QImageIOHandler4readEP6QImage")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
    if (!std::strcmp(key, "_ZN15QImageIOHandler5writeERK6QImage")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
    if (!std::strcmp(key, "_ZNK15QImageIOHandler6optionENS_11ImageOptionE")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
    if (!std::strcmp(key, "_ZN15QImageIOHandler9setOptionENS_11ImageOptionERK8QVariant")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#if !defined(QT_NO_IMAGEFORMAT_PNG)
    if (!std::strcmp(key, "_ZNK15QImageIOHandler14supportsOptionENS_11ImageOptionE")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
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

#if !defined(QT_NO_IMAGEFORMAT_PNG)
  //  bool QPngHandler::canRead() const
  bool canRead() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPngHandlerCall0 call = reinterpret_cast<CuteQPngHandlerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPngHandler::canRead();
  }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)

#if !defined(QT_NO_IMAGEFORMAT_PNG)
  //  bool QPngHandler::read(QImage *image)
  bool read(QImage *image) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPngHandlerCall1 call = reinterpret_cast<CuteQPngHandlerCall1>(taken[1]);
      bool given = call(this, image, &handled);
      if (handled) return given;
    }
    return QPngHandler::read(image);
  }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)

#if !defined(QT_NO_IMAGEFORMAT_PNG)
  //  bool QPngHandler::write(const QImage &image)
  bool write(const QImage &image) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPngHandlerCall2 call = reinterpret_cast<CuteQPngHandlerCall2>(taken[2]);
      bool given = call(this, &image, &handled);
      if (handled) return given;
    }
    return QPngHandler::write(image);
  }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)

#if !defined(QT_NO_IMAGEFORMAT_PNG)
  //  QVariant QPngHandler::option(ImageOption option) const
  QVariant option(QImageIOHandler::ImageOption option) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPngHandlerCall3 call = reinterpret_cast<CuteQPngHandlerCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(option), &handled);
      if (handled && given) return *given;
    }
    return QPngHandler::option(option);
  }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)

#if !defined(QT_NO_IMAGEFORMAT_PNG)
  //  void QPngHandler::setOption(ImageOption option, const QVariant
  //      &value)
  void setOption(
      QImageIOHandler::ImageOption option,
      const QVariant &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPngHandlerCall4 call = reinterpret_cast<CuteQPngHandlerCall4>(taken[4]);
      call(this, static_cast<int>(option), &value, &handled);
      if (handled) return;
    }
    QPngHandler::setOption(option, value);
  }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)

#if !defined(QT_NO_IMAGEFORMAT_PNG)
  //  bool QPngHandler::supportsOption(ImageOption option) const
  bool supportsOption(QImageIOHandler::ImageOption option) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPngHandlerCall5 call = reinterpret_cast<CuteQPngHandlerCall5>(taken[5]);
      bool given = call(this, static_cast<int>(option), &handled);
      if (handled) return given;
    }
    return QPngHandler::supportsOption(option);
  }
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)

  //  bool QImageIOHandler::jumpToNextImage()
  bool jumpToNextImage() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPngHandlerCall6 call = reinterpret_cast<CuteQPngHandlerCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::jumpToNextImage();
  }

  //  bool QImageIOHandler::jumpToImage(int imageNumber)
  bool jumpToImage(int imageNumber) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPngHandlerCall7 call = reinterpret_cast<CuteQPngHandlerCall7>(taken[7]);
      bool given = call(this, imageNumber, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::jumpToImage(imageNumber);
  }

  //  int QImageIOHandler::loopCount() const
  int loopCount() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPngHandlerCall8 call = reinterpret_cast<CuteQPngHandlerCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::loopCount();
  }

  //  int QImageIOHandler::imageCount() const
  int imageCount() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPngHandlerCall9 call = reinterpret_cast<CuteQPngHandlerCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::imageCount();
  }

  //  int QImageIOHandler::nextImageDelay() const
  int nextImageDelay() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPngHandlerCall10 call = reinterpret_cast<CuteQPngHandlerCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::nextImageDelay();
  }

  //  int QImageIOHandler::currentImageNumber() const
  int currentImageNumber() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPngHandlerCall11 call = reinterpret_cast<CuteQPngHandlerCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QImageIOHandler::currentImageNumber();
  }

  //  QRect QImageIOHandler::currentImageRect() const
  QRect currentImageRect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPngHandlerCall12 call = reinterpret_cast<CuteQPngHandlerCall12>(taken[12]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QImageIOHandler::currentImageRect();
  }
};

//  bool QPngHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPngHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QPngHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->supportsOption(option);
}

//  a Python function taken by a CuteQPngHandler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPngHandler(
    QPngHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPngHandler *>(self)->take(key, call);
}

#if !defined(QT_NO_IMAGEFORMAT_PNG)
//  bool QPngHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QPngHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QPngHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->QPngHandler::supportsOption(option);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)

#endif  // !defined(QT_NO_IMAGEFORMAT_PNG)
#endif  // QT_CONFIG(png)
