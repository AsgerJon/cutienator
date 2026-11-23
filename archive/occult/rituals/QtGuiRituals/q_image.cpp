//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qimage.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtGui/qtransform.h>
#include <QtGui/qcolorspace.h>
#include <QtGui/qcolortransform.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qpixelformat.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QImage may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQImage : QImage {
  using QImage::metric;
};

//  A QImage that Python can take functions over in. Every QImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQImageCall0)(const void *, int *);
typedef void * (*CuteQImageCall1)(const void *, int *);
typedef int (*CuteQImageCall2)(const void *, int, int *);
typedef void (*CuteQImageCall3)(const void *, QPainter *, int *);
typedef void * (*CuteQImageCall4)(const void *, QPoint *, int *);
typedef void * (*CuteQImageCall5)(const void *, int *);
class CuteQImage : public QImage {
public:
  using QImage::QImage;
  CuteQImage(const QImage &other) : QImage(other) {}
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  int QImage::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQImageCall0 call = reinterpret_cast<CuteQImageCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QImage::devType();
  }

  //  QPaintEngine *QImage::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQImageCall1 call = reinterpret_cast<CuteQImageCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QImage::paintEngine();
  }

  //  int QImage::metric(PaintDeviceMetric metric) const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQImageCall2 call = reinterpret_cast<CuteQImageCall2>(taken[2]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QImage::metric(metric);
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQImageCall3 call = reinterpret_cast<CuteQImageCall3>(taken[3]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQImageCall4 call = reinterpret_cast<CuteQImageCall4>(taken[4]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQImageCall5 call = reinterpret_cast<CuteQImageCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

//  QImage::QImage()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN6QImageC1Ev() {
  return new CuteQImage();
}

//  QImage::QImage(const QSize &size, Format format)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN6QImageC1ERK5QSizeNS_6FormatE(
    const QSize *size,
    QImage::Format format) {
  return new CuteQImage(*size, format);
}

//  QImage::QImage(int width, int height, Format format)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN6QImageC1EiiNS_6FormatE(
    int width,
    int height,
    QImage::Format format) {
  return new CuteQImage(width, height, format);
}

//  QImage::QImage(const QString &fileName, const char *format)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN6QImageC1ERK7QStringPKc(
    const QString *fileName,
    const char *format) {
  return new CuteQImage(*fileName, format);
}

//  QImage::QImage(const QImage &a0)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN6QImageC1ERKS_(const QImage *a0) {
  return new CuteQImage(*a0);
}

//  QImage::~QImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImageD1Ev(QImage *self) {
  delete self;
}

//  bool QImage::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImage6isNullEv(const QImage *self) {
  return self->isNull();
}

//  int QImage::devType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage7devTypeEv(const QImage *self) {
  return self->devType();
}

//  bool QImage::operator==(const QImage &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImageeqERKS_(const QImage *self, const QImage *a0) {
  return self->operator==(*a0);
}

//  bool QImage::operator!=(const QImage &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImageneERKS_(const QImage *self, const QImage *a0) {
  return self->operator!=(*a0);
}

//  QVariant QImage::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK6QImagecv8QVariantEv(const QImage *self) {
  return new QVariant(self->operator QVariant());
}

//  void QImage::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage6detachEv(QImage *self) {
  self->detach();
}

//  bool QImage::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImage10isDetachedEv(const QImage *self) {
  return self->isDetached();
}

//  QImage QImage::copy(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage4copyERK5QRect(
    const QImage *self,
    const QRect *rect) {
  return new QImage(self->copy(*rect));
}

//  QImage QImage::copy(int x, int y, int w, int h) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage4copyEiiii(
    const QImage *self,
    int x,
    int y,
    int w,
    int h) {
  return new QImage(self->copy(x, y, w, h));
}

//  Format QImage::format() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZNK6QImage6formatEv(const QImage *self) {
  return self->format();
}

//  QImage QImage::convertToFormat(Format f, Qt::ImageConversionFlags flags)
//      const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNKR6QImage15convertToFormatENS_6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    const QImage *self,
    QImage::Format f,
    int flags) {
  return new QImage(
      self->convertToFormat(
          f,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  bool QImage::reinterpretAsFormat(Format f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QImage19reinterpretAsFormatENS_6FormatE(
    QImage *self,
    QImage::Format f) {
  return self->reinterpretAsFormat(f);
}

//  QImage QImage::convertedTo(Format f, Qt::ImageConversionFlags flags)
//      const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNKR6QImage11convertedToENS_6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    const QImage *self,
    QImage::Format f,
    int flags) {
  return new QImage(
      self->convertedTo(
          f,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  void QImage::convertTo(Format f, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage9convertToENS_6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    QImage *self,
    QImage::Format f,
    int flags) {
  self->convertTo(f, QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  int QImage::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage5widthEv(const QImage *self) {
  return self->width();
}

//  int QImage::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage6heightEv(const QImage *self) {
  return self->height();
}

//  QSize QImage::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6QImage4sizeEv(const QImage *self) {
  return new QSize(self->size());
}

//  QRect QImage::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QImage4rectEv(const QImage *self) {
  return new QRect(self->rect());
}

//  int QImage::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage5depthEv(const QImage *self) {
  return self->depth();
}

//  int QImage::colorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage10colorCountEv(const QImage *self) {
  return self->colorCount();
}

//  int QImage::bitPlaneCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage13bitPlaneCountEv(const QImage *self) {
  return self->bitPlaneCount();
}

//  QRgb QImage::color(int i) const
extern "C" Q_DECL_EXPORT
QRgb ritual_ZNK6QImage5colorEi(const QImage *self, int i) {
  return self->color(i);
}

//  void QImage::setColor(int i, QRgb c)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage8setColorEij(QImage *self, int i, QRgb c) {
  self->setColor(i, c);
}

//  void QImage::setColorCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage13setColorCountEi(QImage *self, int a0) {
  self->setColorCount(a0);
}

//  bool QImage::allGray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImage7allGrayEv(const QImage *self) {
  return self->allGray();
}

//  bool QImage::isGrayscale() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImage11isGrayscaleEv(const QImage *self) {
  return self->isGrayscale();
}

//  qsizetype QImage::sizeInBytes() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK6QImage11sizeInBytesEv(const QImage *self) {
  return self->sizeInBytes();
}

//  qsizetype QImage::bytesPerLine() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK6QImage12bytesPerLineEv(const QImage *self) {
  return self->bytesPerLine();
}

//  bool QImage::valid(int x, int y) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImage5validEii(const QImage *self, int x, int y) {
  return self->valid(x, y);
}

//  bool QImage::valid(const QPoint &pt) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImage5validERK6QPoint(
    const QImage *self,
    const QPoint *pt) {
  return self->valid(*pt);
}

//  int QImage::pixelIndex(int x, int y) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage10pixelIndexEii(const QImage *self, int x, int y) {
  return self->pixelIndex(x, y);
}

//  int QImage::pixelIndex(const QPoint &pt) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage10pixelIndexERK6QPoint(
    const QImage *self,
    const QPoint *pt) {
  return self->pixelIndex(*pt);
}

//  QRgb QImage::pixel(int x, int y) const
extern "C" Q_DECL_EXPORT
QRgb ritual_ZNK6QImage5pixelEii(const QImage *self, int x, int y) {
  return self->pixel(x, y);
}

//  QRgb QImage::pixel(const QPoint &pt) const
extern "C" Q_DECL_EXPORT
QRgb ritual_ZNK6QImage5pixelERK6QPoint(
    const QImage *self,
    const QPoint *pt) {
  return self->pixel(*pt);
}

//  void QImage::setPixel(int x, int y, uint index_or_rgb)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage8setPixelEiij(
    QImage *self,
    int x,
    int y,
    uint index_or_rgb) {
  self->setPixel(x, y, index_or_rgb);
}

//  void QImage::setPixel(const QPoint &pt, uint index_or_rgb)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage8setPixelERK6QPointj(
    QImage *self,
    const QPoint *pt,
    uint index_or_rgb) {
  self->setPixel(*pt, index_or_rgb);
}

//  QColor QImage::pixelColor(int x, int y) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QImage10pixelColorEii(const QImage *self, int x, int y) {
  return new QColor(self->pixelColor(x, y));
}

//  QColor QImage::pixelColor(const QPoint &pt) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QImage10pixelColorERK6QPoint(
    const QImage *self,
    const QPoint *pt) {
  return new QColor(self->pixelColor(*pt));
}

//  void QImage::setPixelColor(int x, int y, const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage13setPixelColorEiiRK6QColor(
    QImage *self,
    int x,
    int y,
    const QColor *c) {
  self->setPixelColor(x, y, *c);
}

//  void QImage::setPixelColor(const QPoint &pt, const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage13setPixelColorERK6QPointRK6QColor(
    QImage *self,
    const QPoint *pt,
    const QColor *c) {
  self->setPixelColor(*pt, *c);
}

//  qreal QImage::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QImage16devicePixelRatioEv(const QImage *self) {
  return self->devicePixelRatio();
}

//  void QImage::setDevicePixelRatio(qreal scaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage19setDevicePixelRatioEd(
    QImage *self,
    qreal scaleFactor) {
  self->setDevicePixelRatio(scaleFactor);
}

//  QSizeF QImage::deviceIndependentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK6QImage21deviceIndependentSizeEv(const QImage *self) {
  return new QSizeF(self->deviceIndependentSize());
}

//  void QImage::fill(uint pixel)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage4fillEj(QImage *self, uint pixel) {
  self->fill(pixel);
}

//  void QImage::fill(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage4fillERK6QColor(QImage *self, const QColor *color) {
  self->fill(*color);
}

//  void QImage::fill(Qt::GlobalColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage4fillEN2Qt11GlobalColorE(
    QImage *self,
    Qt::GlobalColor color) {
  self->fill(color);
}

//  bool QImage::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImage15hasAlphaChannelEv(const QImage *self) {
  return self->hasAlphaChannel();
}

//  void QImage::setAlphaChannel(const QImage &alphaChannel)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage15setAlphaChannelERKS_(
    QImage *self,
    const QImage *alphaChannel) {
  self->setAlphaChannel(*alphaChannel);
}

//  QImage QImage::createAlphaMask(Qt::ImageConversionFlags flags) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage15createAlphaMaskE6QFlagsIN2Qt19ImageConversionFlagEE(
    const QImage *self,
    int flags) {
  return new QImage(
      self->createAlphaMask(
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  QImage QImage::createHeuristicMask(bool clipTight) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage19createHeuristicMaskEb(
    const QImage *self,
    bool clipTight) {
  return new QImage(self->createHeuristicMask(clipTight));
}

//  QImage QImage::createMaskFromColor(QRgb color, Qt::MaskMode mode) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage19createMaskFromColorEjN2Qt8MaskModeE(
    const QImage *self,
    QRgb color,
    Qt::MaskMode mode) {
  return new QImage(self->createMaskFromColor(color, mode));
}

//  QImage QImage::scaled(int w, int h, Qt::AspectRatioMode aspectMode,
//      Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage6scaledEiiN2Qt15AspectRatioModeENS0_18TransformationModeE(
    const QImage *self,
    int w,
    int h,
    Qt::AspectRatioMode aspectMode,
    Qt::TransformationMode mode) {
  return new QImage(self->scaled(w, h, aspectMode, mode));
}

//  QImage QImage::scaled(const QSize &s, Qt::AspectRatioMode aspectMode,
//      Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage6scaledERK5QSizeN2Qt15AspectRatioModeENS3_18TransformationModeE(
    const QImage *self,
    const QSize *s,
    Qt::AspectRatioMode aspectMode,
    Qt::TransformationMode mode) {
  return new QImage(self->scaled(*s, aspectMode, mode));
}

//  QImage QImage::scaledToWidth(int w, Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage13scaledToWidthEiN2Qt18TransformationModeE(
    const QImage *self,
    int w,
    Qt::TransformationMode mode) {
  return new QImage(self->scaledToWidth(w, mode));
}

//  QImage QImage::scaledToHeight(int h, Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage14scaledToHeightEiN2Qt18TransformationModeE(
    const QImage *self,
    int h,
    Qt::TransformationMode mode) {
  return new QImage(self->scaledToHeight(h, mode));
}

//  QImage QImage::transformed(const QTransform &matrix,
//      Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage11transformedERK10QTransformN2Qt18TransformationModeE(
    const QImage *self,
    const QTransform *matrix,
    Qt::TransformationMode mode) {
  return new QImage(self->transformed(*matrix, mode));
}

//  QTransform QImage::trueMatrix(const QTransform &a0, int w, int h)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN6QImage10trueMatrixERK10QTransformii(
    const QTransform *a0,
    int w,
    int h) {
  return new QTransform(QImage::trueMatrix(*a0, w, h));
}

//  QImage QImage::mirrored(bool horizontally, bool vertically) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNKR6QImage8mirroredEbb(
    const QImage *self,
    bool horizontally,
    bool vertically) {
  return new QImage(self->mirrored(horizontally, vertically));
}

//  void QImage::mirror(bool horizontally, bool vertically)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage6mirrorEbb(
    QImage *self,
    bool horizontally,
    bool vertically) {
  self->mirror(horizontally, vertically);
}

//  QImage QImage::rgbSwapped() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNKR6QImage10rgbSwappedEv(const QImage *self) {
  return new QImage(self->rgbSwapped());
}

//  QImage QImage::flipped(Qt::Orientations orient) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNKR6QImage7flippedE6QFlagsIN2Qt11OrientationEE(
    const QImage *self,
    int orient) {
  return new QImage(self->flipped(QFlags<Qt::Orientation>::fromInt(orient)));
}

//  void QImage::flip(Qt::Orientations orient)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage4flipE6QFlagsIN2Qt11OrientationEE(
    QImage *self,
    int orient) {
  self->flip(QFlags<Qt::Orientation>::fromInt(orient));
}

//  void QImage::rgbSwap()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage7rgbSwapEv(QImage *self) {
  self->rgbSwap();
}

//  void QImage::invertPixels(InvertMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage12invertPixelsENS_10InvertModeE(
    QImage *self,
    QImage::InvertMode a0) {
  self->invertPixels(a0);
}

//  QColorSpace QImage::colorSpace() const
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZNK6QImage10colorSpaceEv(const QImage *self) {
  return new QColorSpace(self->colorSpace());
}

//  QImage QImage::convertedToColorSpace(const QColorSpace &colorSpace) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage21convertedToColorSpaceERK11QColorSpace(
    const QImage *self,
    const QColorSpace *colorSpace) {
  return new QImage(self->convertedToColorSpace(*colorSpace));
}

//  QImage QImage::convertedToColorSpace(const QColorSpace &colorSpace,
//      QImage::Format format, Qt::ImageConversionFlags flags) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNKR6QImage21convertedToColorSpaceERK11QColorSpaceNS_6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    const QImage *self,
    const QColorSpace *colorSpace,
    QImage::Format format,
    int flags) {
  return new QImage(
      self->convertedToColorSpace(
          *colorSpace,
          format,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  void QImage::convertToColorSpace(const QColorSpace &colorSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage19convertToColorSpaceERK11QColorSpace(
    QImage *self,
    const QColorSpace *colorSpace) {
  self->convertToColorSpace(*colorSpace);
}

//  void QImage::convertToColorSpace(const QColorSpace &colorSpace,
//      QImage::Format format, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage19convertToColorSpaceERK11QColorSpaceNS_6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    QImage *self,
    const QColorSpace *colorSpace,
    QImage::Format format,
    int flags) {
  self->convertToColorSpace(
      *colorSpace,
      format,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QImage::setColorSpace(const QColorSpace &colorSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage13setColorSpaceERK11QColorSpace(
    QImage *self,
    const QColorSpace *colorSpace) {
  self->setColorSpace(*colorSpace);
}

//  QImage QImage::colorTransformed(const QColorTransform &transform) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNKR6QImage16colorTransformedERK15QColorTransform(
    const QImage *self,
    const QColorTransform *transform) {
  return new QImage(self->colorTransformed(*transform));
}

//  QImage QImage::colorTransformed(const QColorTransform &transform,
//      QImage::Format format, Qt::ImageConversionFlags flags) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNKR6QImage16colorTransformedERK15QColorTransformNS_6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    const QImage *self,
    const QColorTransform *transform,
    QImage::Format format,
    int flags) {
  return new QImage(
      self->colorTransformed(
          *transform,
          format,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  void QImage::applyColorTransform(const QColorTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage19applyColorTransformERK15QColorTransform(
    QImage *self,
    const QColorTransform *transform) {
  self->applyColorTransform(*transform);
}

//  void QImage::applyColorTransform(const QColorTransform &transform,
//      QImage::Format format, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage19applyColorTransformERK15QColorTransformNS_6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    QImage *self,
    const QColorTransform *transform,
    QImage::Format format,
    int flags) {
  self->applyColorTransform(
      *transform,
      format,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  bool QImage::load(QIODevice *device, const char *format)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QImage4loadEP9QIODevicePKc(
    QImage *self,
    QIODevice *device,
    const char *format) {
  return self->load(device, format);
}

//  bool QImage::load(const QString &fileName, const char *format)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QImage4loadERK7QStringPKc(
    QImage *self,
    const QString *fileName,
    const char *format) {
  return self->load(*fileName, format);
}

//  bool QImage::loadFromData(QByteArrayView data, const char *format)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QImage12loadFromDataE14QByteArrayViewPKc(
    QImage *self,
    const QByteArrayView *data,
    const char *format) {
  return self->loadFromData(*data, format);
}

//  bool QImage::loadFromData(const QByteArray &data, const char *format)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QImage12loadFromDataERK10QByteArrayPKc(
    QImage *self,
    const QByteArray *data,
    const char *format) {
  return self->loadFromData(*data, format);
}

//  bool QImage::save(const QString &fileName, const char *format, int
//      quality) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImage4saveERK7QStringPKci(
    const QImage *self,
    const QString *fileName,
    const char *format,
    int quality) {
  return self->save(*fileName, format, quality);
}

//  bool QImage::save(QIODevice *device, const char *format, int quality)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QImage4saveEP9QIODevicePKci(
    const QImage *self,
    QIODevice *device,
    const char *format,
    int quality) {
  return self->save(device, format, quality);
}

//  QImage QImage::fromData(QByteArrayView data, const char *format)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN6QImage8fromDataE14QByteArrayViewPKc(
    const QByteArrayView *data,
    const char *format) {
  return new QImage(QImage::fromData(*data, format));
}

//  QImage QImage::fromData(const QByteArray &data, const char *format)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN6QImage8fromDataERK10QByteArrayPKc(
    const QByteArray *data,
    const char *format) {
  return new QImage(QImage::fromData(*data, format));
}

//  qint64 QImage::cacheKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK6QImage8cacheKeyEv(const QImage *self) {
  return self->cacheKey();
}

//  QPaintEngine *QImage::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK6QImage11paintEngineEv(const QImage *self) {
  return self->paintEngine();
}

//  int QImage::dotsPerMeterX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage13dotsPerMeterXEv(const QImage *self) {
  return self->dotsPerMeterX();
}

//  int QImage::dotsPerMeterY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage13dotsPerMeterYEv(const QImage *self) {
  return self->dotsPerMeterY();
}

//  void QImage::setDotsPerMeterX(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage16setDotsPerMeterXEi(QImage *self, int a0) {
  self->setDotsPerMeterX(a0);
}

//  void QImage::setDotsPerMeterY(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage16setDotsPerMeterYEi(QImage *self, int a0) {
  self->setDotsPerMeterY(a0);
}

//  QPoint QImage::offset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK6QImage6offsetEv(const QImage *self) {
  return new QPoint(self->offset());
}

//  void QImage::setOffset(const QPoint &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage9setOffsetERK6QPoint(QImage *self, const QPoint *a0) {
  self->setOffset(*a0);
}

//  QStringList QImage::textKeys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK6QImage8textKeysEv(const QImage *self) {
  return new QList<QString>(self->textKeys());
}

//  QString QImage::text(const QString &key) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QImage4textERK7QString(
    const QImage *self,
    const QString *key) {
  return new QString(self->text(*key));
}

//  void QImage::setText(const QString &key, const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage7setTextERK7QStringS2_(
    QImage *self,
    const QString *key,
    const QString *value) {
  self->setText(*key, *value);
}

//  QPixelFormat QImage::pixelFormat() const
extern "C" Q_DECL_EXPORT
QPixelFormat *ritual_ZNK6QImage11pixelFormatEv(const QImage *self) {
  return new QPixelFormat(self->pixelFormat());
}

//  QPixelFormat QImage::toPixelFormat(QImage::Format format)
extern "C" Q_DECL_EXPORT
QPixelFormat *ritual_ZN6QImage13toPixelFormatENS_6FormatE(
    QImage::Format format) {
  return new QPixelFormat(QImage::toPixelFormat(format));
}

//  QImage::Format QImage::toImageFormat(QPixelFormat format)
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZN6QImage13toImageFormatE12QPixelFormat(
    const QPixelFormat *format) {
  return QImage::toImageFormat(*format);
}

//  int QImage::metric(PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QImage6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QImage *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  QImage QImage::mirrored_helper(bool horizontal, bool vertical) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage15mirrored_helperEbb(
    const QImage *self,
    bool horizontal,
    bool vertical) {
  return new QImage(self->mirrored_helper(horizontal, vertical));
}

//  QImage QImage::rgbSwapped_helper() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage17rgbSwapped_helperEv(const QImage *self) {
  return new QImage(self->rgbSwapped_helper());
}

//  void QImage::mirrored_inplace(bool horizontal, bool vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage16mirrored_inplaceEbb(
    QImage *self,
    bool horizontal,
    bool vertical) {
  self->mirrored_inplace(horizontal, vertical);
}

//  void QImage::rgbSwapped_inplace()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage18rgbSwapped_inplaceEv(QImage *self) {
  self->rgbSwapped_inplace();
}

//  QImage QImage::convertToFormat_helper(Format format,
//      Qt::ImageConversionFlags flags) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage22convertToFormat_helperENS_6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    const QImage *self,
    QImage::Format format,
    int flags) {
  return new QImage(
      self->convertToFormat_helper(
          format,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  bool QImage::convertToFormat_inplace(Format format,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QImage23convertToFormat_inplaceENS_6FormatE6QFlagsIN2Qt19ImageConversionFlagEE(
    QImage *self,
    QImage::Format format,
    int flags) {
  return self->convertToFormat_inplace(
      format,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  QImage QImage::smoothScaled(int w, int h) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QImage12smoothScaledEii(
    const QImage *self,
    int w,
    int h) {
  return new QImage(self->smoothScaled(w, h));
}

//  void QImage::detachMetadata(bool invalidateCache)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QImage14detachMetadataEb(QImage *self, bool invalidateCache) {
  self->detachMetadata(invalidateCache);
}

//  a Python function taken by a CuteQImage, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QImage(QImage *self, const char *key, void *call) {
  return static_cast<CuteQImage *>(self)->take(key, call);
}

//  int QImage::devType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK6QImage7devTypeEv(const QImage *self) {
  return self->QImage::devType();
}

//  QPaintEngine *QImage::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK6QImage11paintEngineEv(const QImage *self) {
  return self->QImage::paintEngine();
}

//  int QImage::metric(PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK6QImage6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QImage *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return static_cast<const OwnQImage *>(self)->OwnQImage::metric(metric);
}
