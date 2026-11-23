//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpixmap.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qtransform.h>
#include <QtGui/qimage.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  Only a class built on QPixmap may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPixmap : QPixmap {
  using QPixmap::metric;
};

//  A QPixmap that Python can take functions over in. Every QPixmap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPixmapCall0)(const void *, int *);
typedef void * (*CuteQPixmapCall1)(const void *, int *);
typedef int (*CuteQPixmapCall2)(const void *, int, int *);
typedef void (*CuteQPixmapCall3)(const void *, QPainter *, int *);
typedef void * (*CuteQPixmapCall4)(const void *, QPoint *, int *);
typedef void * (*CuteQPixmapCall5)(const void *, int *);
class CuteQPixmap : public QPixmap {
public:
  using QPixmap::QPixmap;
  CuteQPixmap(const QPixmap &other) : QPixmap(other) {}
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

  //  int QPixmap::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPixmapCall0 call = reinterpret_cast<CuteQPixmapCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPixmap::devType();
  }

  //  QPaintEngine *QPixmap::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPixmapCall1 call = reinterpret_cast<CuteQPixmapCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPixmap::paintEngine();
  }

  //  int QPixmap::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPixmapCall2 call = reinterpret_cast<CuteQPixmapCall2>(taken[2]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QPixmap::metric(a0);
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPixmapCall3 call = reinterpret_cast<CuteQPixmapCall3>(taken[3]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPixmapCall4 call = reinterpret_cast<CuteQPixmapCall4>(taken[4]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPixmapCall5 call = reinterpret_cast<CuteQPixmapCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

//  QPixmap::QPixmap()
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QPixmapC1Ev() {
  return new CuteQPixmap();
}

//  QPixmap::QPixmap(int w, int h)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QPixmapC1Eii(int w, int h) {
  return new CuteQPixmap(w, h);
}

//  QPixmap::QPixmap(const QSize &a0)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QPixmapC1ERK5QSize(const QSize *a0) {
  return new CuteQPixmap(*a0);
}

//  QPixmap::QPixmap(const QString &fileName, const char *format,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QPixmapC1ERK7QStringPKc6QFlagsIN2Qt19ImageConversionFlagEE(
    const QString *fileName,
    const char *format,
    int flags) {
  return new CuteQPixmap(
      *fileName,
      format,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  QPixmap::QPixmap(const QPixmap &a0)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QPixmapC1ERKS_(const QPixmap *a0) {
  return new CuteQPixmap(*a0);
}

//  QPixmap::~QPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPixmapD1Ev(QPixmap *self) {
  delete self;
}

//  QVariant QPixmap::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QPixmapcv8QVariantEv(const QPixmap *self) {
  return new QVariant(self->operator QVariant());
}

//  bool QPixmap::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPixmap6isNullEv(const QPixmap *self) {
  return self->isNull();
}

//  int QPixmap::devType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QPixmap7devTypeEv(const QPixmap *self) {
  return self->devType();
}

//  int QPixmap::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QPixmap5widthEv(const QPixmap *self) {
  return self->width();
}

//  int QPixmap::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QPixmap6heightEv(const QPixmap *self) {
  return self->height();
}

//  QSize QPixmap::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QPixmap4sizeEv(const QPixmap *self) {
  return new QSize(self->size());
}

//  QRect QPixmap::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QPixmap4rectEv(const QPixmap *self) {
  return new QRect(self->rect());
}

//  int QPixmap::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QPixmap5depthEv(const QPixmap *self) {
  return self->depth();
}

//  int QPixmap::defaultDepth()
extern "C" Q_DECL_EXPORT
int ritual_ZN7QPixmap12defaultDepthEv() {
  return QPixmap::defaultDepth();
}

//  void QPixmap::fill(const QColor &fillColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPixmap4fillERK6QColor(
    QPixmap *self,
    const QColor *fillColor) {
  self->fill(*fillColor);
}

//  QBitmap QPixmap::mask() const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK7QPixmap4maskEv(const QPixmap *self) {
  return new QBitmap(self->mask());
}

//  void QPixmap::setMask(const QBitmap &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPixmap7setMaskERK7QBitmap(QPixmap *self, const QBitmap *a0) {
  self->setMask(*a0);
}

//  qreal QPixmap::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QPixmap16devicePixelRatioEv(const QPixmap *self) {
  return self->devicePixelRatio();
}

//  void QPixmap::setDevicePixelRatio(qreal scaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPixmap19setDevicePixelRatioEd(
    QPixmap *self,
    qreal scaleFactor) {
  self->setDevicePixelRatio(scaleFactor);
}

//  QSizeF QPixmap::deviceIndependentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK7QPixmap21deviceIndependentSizeEv(const QPixmap *self) {
  return new QSizeF(self->deviceIndependentSize());
}

//  bool QPixmap::hasAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPixmap8hasAlphaEv(const QPixmap *self) {
  return self->hasAlpha();
}

//  bool QPixmap::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPixmap15hasAlphaChannelEv(const QPixmap *self) {
  return self->hasAlphaChannel();
}

//  QBitmap QPixmap::createHeuristicMask(bool clipTight) const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK7QPixmap19createHeuristicMaskEb(
    const QPixmap *self,
    bool clipTight) {
  return new QBitmap(self->createHeuristicMask(clipTight));
}

//  QBitmap QPixmap::createMaskFromColor(const QColor &maskColor,
//      Qt::MaskMode mode) const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK7QPixmap19createMaskFromColorERK6QColorN2Qt8MaskModeE(
    const QPixmap *self,
    const QColor *maskColor,
    Qt::MaskMode mode) {
  return new QBitmap(self->createMaskFromColor(*maskColor, mode));
}

//  QPixmap QPixmap::scaled(int w, int h, Qt::AspectRatioMode aspectMode,
//      Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QPixmap6scaledEiiN2Qt15AspectRatioModeENS0_18TransformationModeE(
    const QPixmap *self,
    int w,
    int h,
    Qt::AspectRatioMode aspectMode,
    Qt::TransformationMode mode) {
  return new QPixmap(self->scaled(w, h, aspectMode, mode));
}

//  QPixmap QPixmap::scaled(const QSize &s, Qt::AspectRatioMode aspectMode,
//      Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QPixmap6scaledERK5QSizeN2Qt15AspectRatioModeENS3_18TransformationModeE(
    const QPixmap *self,
    const QSize *s,
    Qt::AspectRatioMode aspectMode,
    Qt::TransformationMode mode) {
  return new QPixmap(self->scaled(*s, aspectMode, mode));
}

//  QPixmap QPixmap::scaledToWidth(int w, Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QPixmap13scaledToWidthEiN2Qt18TransformationModeE(
    const QPixmap *self,
    int w,
    Qt::TransformationMode mode) {
  return new QPixmap(self->scaledToWidth(w, mode));
}

//  QPixmap QPixmap::scaledToHeight(int h, Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QPixmap14scaledToHeightEiN2Qt18TransformationModeE(
    const QPixmap *self,
    int h,
    Qt::TransformationMode mode) {
  return new QPixmap(self->scaledToHeight(h, mode));
}

//  QPixmap QPixmap::transformed(const QTransform &a0, Qt::TransformationMode
//      mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QPixmap11transformedERK10QTransformN2Qt18TransformationModeE(
    const QPixmap *self,
    const QTransform *a0,
    Qt::TransformationMode mode) {
  return new QPixmap(self->transformed(*a0, mode));
}

//  QTransform QPixmap::trueMatrix(const QTransform &m, int w, int h)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN7QPixmap10trueMatrixERK10QTransformii(
    const QTransform *m,
    int w,
    int h) {
  return new QTransform(QPixmap::trueMatrix(*m, w, h));
}

//  QImage QPixmap::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK7QPixmap7toImageEv(const QPixmap *self) {
  return new QImage(self->toImage());
}

//  QPixmap QPixmap::fromImage(const QImage &image, Qt::ImageConversionFlags
//      flags)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    const QImage *image,
    int flags) {
  return new QPixmap(
      QPixmap::fromImage(
          *image,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  QPixmap QPixmap::fromImageReader(QImageReader *imageReader,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QPixmap15fromImageReaderEP12QImageReader6QFlagsIN2Qt19ImageConversionFlagEE(
    QImageReader *imageReader,
    int flags) {
  return new QPixmap(
      QPixmap::fromImageReader(
          imageReader,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  bool QPixmap::load(const QString &fileName, const char *format,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QPixmap4loadERK7QStringPKc6QFlagsIN2Qt19ImageConversionFlagEE(
    QPixmap *self,
    const QString *fileName,
    const char *format,
    int flags) {
  return self->load(
      *fileName,
      format,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  bool QPixmap::loadFromData(const QByteArray &data, const char *format,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QPixmap12loadFromDataERK10QByteArrayPKc6QFlagsIN2Qt19ImageConversionFlagEE(
    QPixmap *self,
    const QByteArray *data,
    const char *format,
    int flags) {
  return self->loadFromData(
      *data,
      format,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  bool QPixmap::save(const QString &fileName, const char *format, int
//      quality) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPixmap4saveERK7QStringPKci(
    const QPixmap *self,
    const QString *fileName,
    const char *format,
    int quality) {
  return self->save(*fileName, format, quality);
}

//  bool QPixmap::save(QIODevice *device, const char *format, int quality)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPixmap4saveEP9QIODevicePKci(
    const QPixmap *self,
    QIODevice *device,
    const char *format,
    int quality) {
  return self->save(device, format, quality);
}

//  bool QPixmap::convertFromImage(const QImage &img,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QPixmap16convertFromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    QPixmap *self,
    const QImage *img,
    int flags) {
  return self->convertFromImage(
      *img,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  QPixmap QPixmap::copy(int x, int y, int width, int height) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QPixmap4copyEiiii(
    const QPixmap *self,
    int x,
    int y,
    int width,
    int height) {
  return new QPixmap(self->copy(x, y, width, height));
}

//  QPixmap QPixmap::copy(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QPixmap4copyERK5QRect(
    const QPixmap *self,
    const QRect *rect) {
  return new QPixmap(self->copy(*rect));
}

//  void QPixmap::scroll(int dx, int dy, int x, int y, int width, int height,
//      QRegion *exposed)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPixmap6scrollEiiiiiiP7QRegion(
    QPixmap *self,
    int dx,
    int dy,
    int x,
    int y,
    int width,
    int height,
    QRegion *exposed) {
  self->scroll(dx, dy, x, y, width, height, exposed);
}

//  void QPixmap::scroll(int dx, int dy, const QRect &rect, QRegion *exposed)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPixmap6scrollEiiRK5QRectP7QRegion(
    QPixmap *self,
    int dx,
    int dy,
    const QRect *rect,
    QRegion *exposed) {
  self->scroll(dx, dy, *rect, exposed);
}

//  qint64 QPixmap::cacheKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK7QPixmap8cacheKeyEv(const QPixmap *self) {
  return self->cacheKey();
}

//  bool QPixmap::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPixmap10isDetachedEv(const QPixmap *self) {
  return self->isDetached();
}

//  void QPixmap::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPixmap6detachEv(QPixmap *self) {
  self->detach();
}

//  bool QPixmap::isQBitmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPixmap9isQBitmapEv(const QPixmap *self) {
  return self->isQBitmap();
}

//  QPaintEngine *QPixmap::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK7QPixmap11paintEngineEv(const QPixmap *self) {
  return self->paintEngine();
}

//  bool QPixmap::operator!() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPixmapntEv(const QPixmap *self) {
  return self->operator!();
}

//  int QPixmap::metric(PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QPixmap6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPixmap *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->metric(a0);
}

//  bool QPixmap::doImageIO(QImageWriter *io, int quality) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPixmap9doImageIOEP12QImageWriteri(
    const QPixmap *self,
    QImageWriter *io,
    int quality) {
  return self->doImageIO(io, quality);
}

//  QPixmap::QPixmap(const QSize &s, int type)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QPixmapC1ERK5QSizei(const QSize *s, int type) {
  return new CuteQPixmap(*s, type);
}

//  void QPixmap::doInit(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPixmap6doInitEiii(QPixmap *self, int a0, int a1, int a2) {
  self->doInit(a0, a1, a2);
}

//  a Python function taken by a CuteQPixmap, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPixmap(QPixmap *self, const char *key, void *call) {
  return static_cast<CuteQPixmap *>(self)->take(key, call);
}

//  int QPixmap::devType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QPixmap7devTypeEv(const QPixmap *self) {
  return self->QPixmap::devType();
}

//  QPaintEngine *QPixmap::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK7QPixmap11paintEngineEv(const QPixmap *self) {
  return self->QPixmap::paintEngine();
}

//  int QPixmap::metric(PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QPixmap6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPixmap *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return static_cast<const OwnQPixmap *>(self)->OwnQPixmap::metric(a0);
}
