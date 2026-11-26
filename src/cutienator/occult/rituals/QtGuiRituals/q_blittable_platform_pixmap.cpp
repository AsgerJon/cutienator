//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpixmap_blitter_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_BLITTABLE)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpixmap_blitter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpaintengine.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpixmap.h>
#include <cstring>

//  A QBlittablePlatformPixmap that Python can take functions over in. Every QBlittablePlatformPixmap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_BLITTABLE)
typedef void * (*CuteQBlittablePlatformPixmapCall0)(const void *, const QSize *, bool, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlittablePlatformPixmapCall1)(const void *, int, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef int (*CuteQBlittablePlatformPixmapCall2)(const void *, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlittablePlatformPixmapCall3)(const void *, const QColor *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void * (*CuteQBlittablePlatformPixmapCall4)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef const QImage * (*CuteQBlittablePlatformPixmapCall5)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef bool (*CuteQBlittablePlatformPixmapCall6)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlittablePlatformPixmapCall7)(const void *, const QImage *, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef qreal (*CuteQBlittablePlatformPixmapCall8)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlittablePlatformPixmapCall9)(const void *, qreal, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void * (*CuteQBlittablePlatformPixmapCall10)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
typedef void * (*CuteQBlittablePlatformPixmapCall11)(const void *, int *);
typedef void (*CuteQBlittablePlatformPixmapCall12)(const void *, QImageReader *, int, int *);
typedef void (*CuteQBlittablePlatformPixmapCall13)(const void *, const QPlatformPixmap *, const QRect *, int *);
typedef bool (*CuteQBlittablePlatformPixmapCall14)(const void *, int, int, const QRect *, int *);
typedef const QBitmap * (*CuteQBlittablePlatformPixmapCall15)(const void *, int *);
typedef void (*CuteQBlittablePlatformPixmapCall16)(const void *, const QBitmap *, int *);
typedef const QPixmap * (*CuteQBlittablePlatformPixmapCall17)(const void *, const QTransform *, int, int *);
typedef const QImage * (*CuteQBlittablePlatformPixmapCall18)(const void *, const QRect *, int *);
class CuteQBlittablePlatformPixmap : public QBlittablePlatformPixmap {
public:
  using QBlittablePlatformPixmap::QBlittablePlatformPixmap;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZNK24QBlittablePlatformPixmap15createBlittableERK5QSizeb")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN15QPlatformPixmap6resizeEii")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap6metricEN12QPaintDevice17PaintDeviceMetricE")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN15QPlatformPixmap4fillERK6QColor")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN15QPlatformPixmap6bufferEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap7toImageEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap15hasAlphaChannelEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN15QPlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap16devicePixelRatioEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN15QPlatformPixmap19setDevicePixelRatioEd")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap11paintEngineEv")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap30createCompatiblePlatformPixmapEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap15fromImageReaderEP12QImageReader6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap4copyEPKS_RK5QRect")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap6scrollEiiRK5QRect")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap4maskEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap7setMaskERK7QBitmap")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap11transformedERK10QTransformN2Qt18TransformationModeE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap7toImageERK5QRect")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_BLITTABLE)
  //  QBlittable *QBlittablePlatformPixmap::createBlittable(const QSize
  //      &size, bool alpha) const
  QBlittable *createBlittable(const QSize &size, bool alpha) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall0 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall0>(taken[0]);
      void * given = call(this, &size, alpha, &handled);
      if (handled) return static_cast<QBlittable *>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlittablePlatformPixmap::resize(int width, int height)
  void resize(int width, int height) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall1 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall1>(taken[1]);
      call(this, width, height, &handled);
      if (handled) return;
    }
    QBlittablePlatformPixmap::resize(width, height);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  int QBlittablePlatformPixmap::metric(QPaintDevice::PaintDeviceMetric
  //      metric) const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall2 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall2>(taken[2]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QBlittablePlatformPixmap::metric(metric);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlittablePlatformPixmap::fill(const QColor &color)
  void fill(const QColor &color) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall3 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall3>(taken[3]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QBlittablePlatformPixmap::fill(color);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  QImage *QBlittablePlatformPixmap::buffer()
  QImage *buffer() override {
    if (taken[4]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall4 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QImage *>(given);
    }
    return QBlittablePlatformPixmap::buffer();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  QImage QBlittablePlatformPixmap::toImage() const
  QImage toImage() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall5 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall5>(taken[5]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBlittablePlatformPixmap::toImage();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  bool QBlittablePlatformPixmap::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall6 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBlittablePlatformPixmap::hasAlphaChannel();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlittablePlatformPixmap::fromImage(const QImage &image,
  //      Qt::ImageConversionFlags flags)
  void fromImage(
      const QImage &image,
      Qt::ImageConversionFlags flags) override {
    if (taken[7]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall7 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall7>(taken[7]);
      call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QBlittablePlatformPixmap::fromImage(image, flags);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  qreal QBlittablePlatformPixmap::devicePixelRatio() const
  qreal devicePixelRatio() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall8 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QBlittablePlatformPixmap::devicePixelRatio();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlittablePlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
  void setDevicePixelRatio(qreal scaleFactor) override {
    if (taken[9]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall9 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall9>(taken[9]);
      call(this, scaleFactor, &handled);
      if (handled) return;
    }
    QBlittablePlatformPixmap::setDevicePixelRatio(scaleFactor);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  QPaintEngine *QBlittablePlatformPixmap::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall10 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QBlittablePlatformPixmap::paintEngine();
  }
#endif  // !defined(QT_NO_BLITTABLE)

  //  QPlatformPixmap *QPlatformPixmap::createCompatiblePlatformPixmap()
  //      const
  QPlatformPixmap *createCompatiblePlatformPixmap() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall11 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformPixmap *>(given);
    }
    return QPlatformPixmap::createCompatiblePlatformPixmap();
  }

  //  void QPlatformPixmap::fromImageReader(QImageReader *imageReader,
  //      Qt::ImageConversionFlags flags)
  void fromImageReader(
      QImageReader *imageReader,
      Qt::ImageConversionFlags flags) override {
    if (taken[12]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall12 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall12>(taken[12]);
      call(this, imageReader, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QPlatformPixmap::fromImageReader(imageReader, flags);
  }

  //  void QPlatformPixmap::copy(const QPlatformPixmap *data, const QRect
  //      &rect)
  void copy(const QPlatformPixmap *data, const QRect &rect) override {
    if (taken[13]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall13 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall13>(taken[13]);
      call(this, data, &rect, &handled);
      if (handled) return;
    }
    QPlatformPixmap::copy(data, rect);
  }

  //  bool QPlatformPixmap::scroll(int dx, int dy, const QRect &rect)
  bool scroll(int dx, int dy, const QRect &rect) override {
    if (taken[14]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall14 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall14>(taken[14]);
      bool given = call(this, dx, dy, &rect, &handled);
      if (handled) return given;
    }
    return QPlatformPixmap::scroll(dx, dy, rect);
  }

  //  QBitmap QPlatformPixmap::mask() const
  QBitmap mask() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall15 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall15>(taken[15]);
      const QBitmap * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPixmap::mask();
  }

  //  void QPlatformPixmap::setMask(const QBitmap &mask)
  void setMask(const QBitmap &mask) override {
    if (taken[16]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall16 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall16>(taken[16]);
      call(this, &mask, &handled);
      if (handled) return;
    }
    QPlatformPixmap::setMask(mask);
  }

  //  QPixmap QPlatformPixmap::transformed(const QTransform &matrix,
  //      Qt::TransformationMode mode) const
  QPixmap transformed(
      const QTransform &matrix,
      Qt::TransformationMode mode) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall17 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall17>(taken[17]);
      const QPixmap * given = call(this, &matrix, static_cast<int>(mode), &handled);
      if (handled && given) return *given;
    }
    return QPlatformPixmap::transformed(matrix, mode);
  }

  //  QImage QPlatformPixmap::toImage(const QRect &rect) const
  QImage toImage(const QRect &rect) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQBlittablePlatformPixmapCall18 call = reinterpret_cast<CuteQBlittablePlatformPixmapCall18>(taken[18]);
      const QImage * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPixmap::toImage(rect);
  }
};

//  QBlittablePlatformPixmap::QBlittablePlatformPixmap()
extern "C" Q_DECL_EXPORT
QBlittablePlatformPixmap *ritual_ZN24QBlittablePlatformPixmapC1Ev() {
  return new CuteQBlittablePlatformPixmap();
}

//  QBlittablePlatformPixmap::~QBlittablePlatformPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmapD1Ev(
    QBlittablePlatformPixmap *self) {
  delete self;
}

//  QBlittable *QBlittablePlatformPixmap::createBlittable(const QSize &size,
//      bool alpha) const
extern "C" Q_DECL_EXPORT
QBlittable *ritual_ZNK24QBlittablePlatformPixmap15createBlittableERK5QSizeb(
    const QBlittablePlatformPixmap *self,
    const QSize *size,
    bool alpha) {
  return self->createBlittable(*size, alpha);
}

//  QBlittable *QBlittablePlatformPixmap::blittable() const
extern "C" Q_DECL_EXPORT
QBlittable *ritual_ZNK24QBlittablePlatformPixmap9blittableEv(
    const QBlittablePlatformPixmap *self) {
  return self->blittable();
}

//  void QBlittablePlatformPixmap::setBlittable(QBlittable *blittable)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap12setBlittableEP10QBlittable(
    QBlittablePlatformPixmap *self,
    QBlittable *blittable) {
  self->setBlittable(blittable);
}

//  void QBlittablePlatformPixmap::resize(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap6resizeEii(
    QBlittablePlatformPixmap *self,
    int width,
    int height) {
  self->resize(width, height);
}

//  int QBlittablePlatformPixmap::metric(QPaintDevice::PaintDeviceMetric
//      metric) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QBlittablePlatformPixmap6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QBlittablePlatformPixmap *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  void QBlittablePlatformPixmap::fill(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap4fillERK6QColor(
    QBlittablePlatformPixmap *self,
    const QColor *color) {
  self->fill(*color);
}

//  QImage *QBlittablePlatformPixmap::buffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN24QBlittablePlatformPixmap6bufferEv(
    QBlittablePlatformPixmap *self) {
  return self->buffer();
}

//  QImage QBlittablePlatformPixmap::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK24QBlittablePlatformPixmap7toImageEv(
    const QBlittablePlatformPixmap *self) {
  return new QImage(self->toImage());
}

//  bool QBlittablePlatformPixmap::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QBlittablePlatformPixmap15hasAlphaChannelEv(
    const QBlittablePlatformPixmap *self) {
  return self->hasAlphaChannel();
}

//  void QBlittablePlatformPixmap::fromImage(const QImage &image,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    QBlittablePlatformPixmap *self,
    const QImage *image,
    int flags) {
  self->fromImage(*image, QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  qreal QBlittablePlatformPixmap::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QBlittablePlatformPixmap16devicePixelRatioEv(
    const QBlittablePlatformPixmap *self) {
  return self->devicePixelRatio();
}

//  void QBlittablePlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap19setDevicePixelRatioEd(
    QBlittablePlatformPixmap *self,
    qreal scaleFactor) {
  self->setDevicePixelRatio(scaleFactor);
}

//  QPaintEngine *QBlittablePlatformPixmap::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK24QBlittablePlatformPixmap11paintEngineEv(
    const QBlittablePlatformPixmap *self) {
  return self->paintEngine();
}

//  void QBlittablePlatformPixmap::markRasterOverlay(const QRectF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayERK6QRectF(
    QBlittablePlatformPixmap *self,
    const QRectF *a0) {
  self->markRasterOverlay(*a0);
}

//  void QBlittablePlatformPixmap::markRasterOverlay(const QPointF &a0, const
//      QTextItem &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayERK7QPointFRK9QTextItem(
    QBlittablePlatformPixmap *self,
    const QPointF *a0,
    const QTextItem *a1) {
  self->markRasterOverlay(*a0, *a1);
}

//  void QBlittablePlatformPixmap::markRasterOverlay(const QVectorPath &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayERK11QVectorPath(
    QBlittablePlatformPixmap *self,
    const QVectorPath *a0) {
  self->markRasterOverlay(*a0);
}

//  void QBlittablePlatformPixmap::markRasterOverlay(const QPainterPath &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayERK12QPainterPath(
    QBlittablePlatformPixmap *self,
    const QPainterPath *a0) {
  self->markRasterOverlay(*a0);
}

//  void QBlittablePlatformPixmap::markRasterOverlay(const QRect *rects, int
//      rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayEPK5QRecti(
    QBlittablePlatformPixmap *self,
    const QRect *rects,
    int rectCount) {
  self->markRasterOverlay(rects, rectCount);
}

//  void QBlittablePlatformPixmap::markRasterOverlay(const QRectF *rects, int
//      rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayEPK6QRectFi(
    QBlittablePlatformPixmap *self,
    const QRectF *rects,
    int rectCount) {
  self->markRasterOverlay(rects, rectCount);
}

//  void QBlittablePlatformPixmap::markRasterOverlay(const QPointF *points,
//      int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayEPK7QPointFi(
    QBlittablePlatformPixmap *self,
    const QPointF *points,
    int pointCount) {
  self->markRasterOverlay(points, pointCount);
}

//  void QBlittablePlatformPixmap::markRasterOverlay(const QPoint *points,
//      int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayEPK6QPointi(
    QBlittablePlatformPixmap *self,
    const QPoint *points,
    int pointCount) {
  self->markRasterOverlay(points, pointCount);
}

//  void QBlittablePlatformPixmap::unmarkRasterOverlay(const QRectF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBlittablePlatformPixmap19unmarkRasterOverlayERK6QRectF(
    QBlittablePlatformPixmap *self,
    const QRectF *a0) {
  self->unmarkRasterOverlay(*a0);
}

//  a Python function taken by a CuteQBlittablePlatformPixmap, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBlittablePlatformPixmap(
    QBlittablePlatformPixmap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBlittablePlatformPixmap *>(self)->take(key, call);
}

//  void QBlittablePlatformPixmap::resize(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QBlittablePlatformPixmap6resizeEii(
    QBlittablePlatformPixmap *self,
    int width,
    int height) {
  self->QBlittablePlatformPixmap::resize(width, height);
}

//  int QBlittablePlatformPixmap::metric(QPaintDevice::PaintDeviceMetric
//      metric) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QBlittablePlatformPixmap6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QBlittablePlatformPixmap *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->QBlittablePlatformPixmap::metric(metric);
}

//  void QBlittablePlatformPixmap::fill(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QBlittablePlatformPixmap4fillERK6QColor(
    QBlittablePlatformPixmap *self,
    const QColor *color) {
  self->QBlittablePlatformPixmap::fill(*color);
}

//  QImage *QBlittablePlatformPixmap::buffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN24QBlittablePlatformPixmap6bufferEv(
    QBlittablePlatformPixmap *self) {
  return self->QBlittablePlatformPixmap::buffer();
}

//  QImage QBlittablePlatformPixmap::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK24QBlittablePlatformPixmap7toImageEv(
    const QBlittablePlatformPixmap *self) {
  return new QImage(self->QBlittablePlatformPixmap::toImage());
}

//  bool QBlittablePlatformPixmap::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QBlittablePlatformPixmap15hasAlphaChannelEv(
    const QBlittablePlatformPixmap *self) {
  return self->QBlittablePlatformPixmap::hasAlphaChannel();
}

//  void QBlittablePlatformPixmap::fromImage(const QImage &image,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QBlittablePlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    QBlittablePlatformPixmap *self,
    const QImage *image,
    int flags) {
  self->QBlittablePlatformPixmap::fromImage(
      *image,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  qreal QBlittablePlatformPixmap::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK24QBlittablePlatformPixmap16devicePixelRatioEv(
    const QBlittablePlatformPixmap *self) {
  return self->QBlittablePlatformPixmap::devicePixelRatio();
}

//  void QBlittablePlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QBlittablePlatformPixmap19setDevicePixelRatioEd(
    QBlittablePlatformPixmap *self,
    qreal scaleFactor) {
  self->QBlittablePlatformPixmap::setDevicePixelRatio(scaleFactor);
}

//  QPaintEngine *QBlittablePlatformPixmap::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK24QBlittablePlatformPixmap11paintEngineEv(
    const QBlittablePlatformPixmap *self) {
  return self->QBlittablePlatformPixmap::paintEngine();
}

#endif  // !defined(QT_NO_BLITTABLE)
