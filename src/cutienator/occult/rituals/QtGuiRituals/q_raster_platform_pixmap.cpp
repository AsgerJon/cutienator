//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpixmap_raster_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpixmap_raster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpixmap.h>
#include <cstring>

//  Only a class built on QRasterPlatformPixmap may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRasterPlatformPixmap : QRasterPlatformPixmap {
  using QRasterPlatformPixmap::metric;
};

//  A QRasterPlatformPixmap that Python can take functions over in. Every QRasterPlatformPixmap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQRasterPlatformPixmapCall0)(const void *, int *);
typedef void (*CuteQRasterPlatformPixmapCall1)(const void *, int, int, int *);
typedef void (*CuteQRasterPlatformPixmapCall2)(const void *, const QImage *, int, int *);
typedef void (*CuteQRasterPlatformPixmapCall3)(const void *, QImageReader *, int, int *);
typedef void (*CuteQRasterPlatformPixmapCall4)(const void *, const QPlatformPixmap *, const QRect *, int *);
typedef bool (*CuteQRasterPlatformPixmapCall5)(const void *, int, int, const QRect *, int *);
typedef void (*CuteQRasterPlatformPixmapCall6)(const void *, const QColor *, int *);
typedef bool (*CuteQRasterPlatformPixmapCall7)(const void *, int *);
typedef const QImage * (*CuteQRasterPlatformPixmapCall8)(const void *, int *);
typedef const QImage * (*CuteQRasterPlatformPixmapCall9)(const void *, const QRect *, int *);
typedef void * (*CuteQRasterPlatformPixmapCall10)(const void *, int *);
typedef void * (*CuteQRasterPlatformPixmapCall11)(const void *, int *);
typedef qreal (*CuteQRasterPlatformPixmapCall12)(const void *, int *);
typedef void (*CuteQRasterPlatformPixmapCall13)(const void *, qreal, int *);
typedef int (*CuteQRasterPlatformPixmapCall14)(const void *, int, int *);
typedef const QBitmap * (*CuteQRasterPlatformPixmapCall15)(const void *, int *);
typedef void (*CuteQRasterPlatformPixmapCall16)(const void *, const QBitmap *, int *);
typedef const QPixmap * (*CuteQRasterPlatformPixmapCall17)(const void *, const QTransform *, int, int *);
class CuteQRasterPlatformPixmap : public QRasterPlatformPixmap {
public:
  using QRasterPlatformPixmap::QRasterPlatformPixmap;
  CuteQRasterPlatformPixmap(const QRasterPlatformPixmap &other) : QRasterPlatformPixmap(other) {}
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap30createCompatiblePlatformPixmapEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap6resizeEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap15fromImageReaderEP12QImageReader6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap4copyEPKS_RK5QRect")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap6scrollEiiRK5QRect")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap4fillERK6QColor")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap15hasAlphaChannelEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap7toImageEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap7toImageERK5QRect")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap11paintEngineEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap6bufferEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap16devicePixelRatioEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap19setDevicePixelRatioEd")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap6metricEN12QPaintDevice17PaintDeviceMetricE")) {
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
    return false;
  }

  //  QPlatformPixmap
  //      *QRasterPlatformPixmap::createCompatiblePlatformPixmap() const
  QPlatformPixmap *createCompatiblePlatformPixmap() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall0 call = reinterpret_cast<CuteQRasterPlatformPixmapCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformPixmap *>(given);
    }
    return QRasterPlatformPixmap::createCompatiblePlatformPixmap();
  }

  //  void QRasterPlatformPixmap::resize(int width, int height)
  void resize(int width, int height) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall1 call = reinterpret_cast<CuteQRasterPlatformPixmapCall1>(taken[1]);
      call(this, width, height, &handled);
      if (handled) return;
    }
    QRasterPlatformPixmap::resize(width, height);
  }

  //  void QRasterPlatformPixmap::fromImage(const QImage &image,
  //      Qt::ImageConversionFlags flags)
  void fromImage(
      const QImage &image,
      Qt::ImageConversionFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall2 call = reinterpret_cast<CuteQRasterPlatformPixmapCall2>(taken[2]);
      call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRasterPlatformPixmap::fromImage(image, flags);
  }

  //  void QRasterPlatformPixmap::fromImageReader(QImageReader
  //      *imageReader, Qt::ImageConversionFlags flags)
  void fromImageReader(
      QImageReader *imageReader,
      Qt::ImageConversionFlags flags) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall3 call = reinterpret_cast<CuteQRasterPlatformPixmapCall3>(taken[3]);
      call(this, imageReader, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRasterPlatformPixmap::fromImageReader(imageReader, flags);
  }

  //  void QRasterPlatformPixmap::copy(const QPlatformPixmap *data, const
  //      QRect &rect)
  void copy(const QPlatformPixmap *data, const QRect &rect) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall4 call = reinterpret_cast<CuteQRasterPlatformPixmapCall4>(taken[4]);
      call(this, data, &rect, &handled);
      if (handled) return;
    }
    QRasterPlatformPixmap::copy(data, rect);
  }

  //  bool QRasterPlatformPixmap::scroll(int dx, int dy, const QRect &rect)
  bool scroll(int dx, int dy, const QRect &rect) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall5 call = reinterpret_cast<CuteQRasterPlatformPixmapCall5>(taken[5]);
      bool given = call(this, dx, dy, &rect, &handled);
      if (handled) return given;
    }
    return QRasterPlatformPixmap::scroll(dx, dy, rect);
  }

  //  void QRasterPlatformPixmap::fill(const QColor &color)
  void fill(const QColor &color) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall6 call = reinterpret_cast<CuteQRasterPlatformPixmapCall6>(taken[6]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QRasterPlatformPixmap::fill(color);
  }

  //  bool QRasterPlatformPixmap::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall7 call = reinterpret_cast<CuteQRasterPlatformPixmapCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRasterPlatformPixmap::hasAlphaChannel();
  }

  //  QImage QRasterPlatformPixmap::toImage() const
  QImage toImage() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall8 call = reinterpret_cast<CuteQRasterPlatformPixmapCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRasterPlatformPixmap::toImage();
  }

  //  QImage QRasterPlatformPixmap::toImage(const QRect &rect) const
  QImage toImage(const QRect &rect) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall9 call = reinterpret_cast<CuteQRasterPlatformPixmapCall9>(taken[9]);
      const QImage * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QRasterPlatformPixmap::toImage(rect);
  }

  //  QPaintEngine *QRasterPlatformPixmap::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall10 call = reinterpret_cast<CuteQRasterPlatformPixmapCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QRasterPlatformPixmap::paintEngine();
  }

  //  QImage *QRasterPlatformPixmap::buffer()
  QImage *buffer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall11 call = reinterpret_cast<CuteQRasterPlatformPixmapCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QImage *>(given);
    }
    return QRasterPlatformPixmap::buffer();
  }

  //  qreal QRasterPlatformPixmap::devicePixelRatio() const
  qreal devicePixelRatio() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall12 call = reinterpret_cast<CuteQRasterPlatformPixmapCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QRasterPlatformPixmap::devicePixelRatio();
  }

  //  void QRasterPlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
  void setDevicePixelRatio(qreal scaleFactor) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall13 call = reinterpret_cast<CuteQRasterPlatformPixmapCall13>(taken[13]);
      call(this, scaleFactor, &handled);
      if (handled) return;
    }
    QRasterPlatformPixmap::setDevicePixelRatio(scaleFactor);
  }

  //  int QRasterPlatformPixmap::metric(QPaintDevice::PaintDeviceMetric
  //      metric) const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall14 call = reinterpret_cast<CuteQRasterPlatformPixmapCall14>(taken[14]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QRasterPlatformPixmap::metric(metric);
  }

  //  QBitmap QPlatformPixmap::mask() const
  QBitmap mask() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall15 call = reinterpret_cast<CuteQRasterPlatformPixmapCall15>(taken[15]);
      const QBitmap * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPixmap::mask();
  }

  //  void QPlatformPixmap::setMask(const QBitmap &mask)
  void setMask(const QBitmap &mask) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRasterPlatformPixmapCall16 call = reinterpret_cast<CuteQRasterPlatformPixmapCall16>(taken[16]);
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
      CuteQRasterPlatformPixmapCall17 call = reinterpret_cast<CuteQRasterPlatformPixmapCall17>(taken[17]);
      const QPixmap * given = call(this, &matrix, static_cast<int>(mode), &handled);
      if (handled && given) return *given;
    }
    return QPlatformPixmap::transformed(matrix, mode);
  }
};

//  QRasterPlatformPixmap::QRasterPlatformPixmap(PixelType type)
extern "C" Q_DECL_EXPORT
QRasterPlatformPixmap *ritual_ZN21QRasterPlatformPixmapC1EN15QPlatformPixmap9PixelTypeE(
    QPlatformPixmap::PixelType type) {
  return new CuteQRasterPlatformPixmap(type);
}

//  QRasterPlatformPixmap::~QRasterPlatformPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRasterPlatformPixmapD1Ev(QRasterPlatformPixmap *self) {
  delete self;
}

//  QPlatformPixmap *QRasterPlatformPixmap::createCompatiblePlatformPixmap()
//      const
extern "C" Q_DECL_EXPORT
QPlatformPixmap *ritual_ZNK21QRasterPlatformPixmap30createCompatiblePlatformPixmapEv(
    const QRasterPlatformPixmap *self) {
  return self->createCompatiblePlatformPixmap();
}

//  void QRasterPlatformPixmap::resize(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRasterPlatformPixmap6resizeEii(
    QRasterPlatformPixmap *self,
    int width,
    int height) {
  self->resize(width, height);
}

//  void QRasterPlatformPixmap::fromImage(const QImage &image,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRasterPlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    QRasterPlatformPixmap *self,
    const QImage *image,
    int flags) {
  self->fromImage(*image, QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QRasterPlatformPixmap::fromImageReader(QImageReader *imageReader,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRasterPlatformPixmap15fromImageReaderEP12QImageReader6QFlagsIN2Qt19ImageConversionFlagEE(
    QRasterPlatformPixmap *self,
    QImageReader *imageReader,
    int flags) {
  self->fromImageReader(
      imageReader,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QRasterPlatformPixmap::copy(const QPlatformPixmap *data, const QRect
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRasterPlatformPixmap4copyEPK15QPlatformPixmapRK5QRect(
    QRasterPlatformPixmap *self,
    const QPlatformPixmap *data,
    const QRect *rect) {
  self->copy(data, *rect);
}

//  bool QRasterPlatformPixmap::scroll(int dx, int dy, const QRect &rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QRasterPlatformPixmap6scrollEiiRK5QRect(
    QRasterPlatformPixmap *self,
    int dx,
    int dy,
    const QRect *rect) {
  return self->scroll(dx, dy, *rect);
}

//  void QRasterPlatformPixmap::fill(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRasterPlatformPixmap4fillERK6QColor(
    QRasterPlatformPixmap *self,
    const QColor *color) {
  self->fill(*color);
}

//  bool QRasterPlatformPixmap::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QRasterPlatformPixmap15hasAlphaChannelEv(
    const QRasterPlatformPixmap *self) {
  return self->hasAlphaChannel();
}

//  QImage QRasterPlatformPixmap::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK21QRasterPlatformPixmap7toImageEv(
    const QRasterPlatformPixmap *self) {
  return new QImage(self->toImage());
}

//  QImage QRasterPlatformPixmap::toImage(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK21QRasterPlatformPixmap7toImageERK5QRect(
    const QRasterPlatformPixmap *self,
    const QRect *rect) {
  return new QImage(self->toImage(*rect));
}

//  QPaintEngine *QRasterPlatformPixmap::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK21QRasterPlatformPixmap11paintEngineEv(
    const QRasterPlatformPixmap *self) {
  return self->paintEngine();
}

//  QImage *QRasterPlatformPixmap::buffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN21QRasterPlatformPixmap6bufferEv(
    QRasterPlatformPixmap *self) {
  return self->buffer();
}

//  qreal QRasterPlatformPixmap::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QRasterPlatformPixmap16devicePixelRatioEv(
    const QRasterPlatformPixmap *self) {
  return self->devicePixelRatio();
}

//  void QRasterPlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRasterPlatformPixmap19setDevicePixelRatioEd(
    QRasterPlatformPixmap *self,
    qreal scaleFactor) {
  self->setDevicePixelRatio(scaleFactor);
}

//  int QRasterPlatformPixmap::metric(QPaintDevice::PaintDeviceMetric metric)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QRasterPlatformPixmap6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QRasterPlatformPixmap *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  void QRasterPlatformPixmap::createPixmapForImage(QImage sourceImage,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRasterPlatformPixmap20createPixmapForImageE6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    QRasterPlatformPixmap *self,
    const QImage *sourceImage,
    int flags) {
  self->createPixmapForImage(
      *sourceImage,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  QImage::Format QRasterPlatformPixmap::systemNativeFormat()
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZN21QRasterPlatformPixmap18systemNativeFormatEv() {
  return QRasterPlatformPixmap::systemNativeFormat();
}

//  a Python function taken by a CuteQRasterPlatformPixmap, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRasterPlatformPixmap(
    QRasterPlatformPixmap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRasterPlatformPixmap *>(self)->take(key, call);
}

//  QPlatformPixmap *QRasterPlatformPixmap::createCompatiblePlatformPixmap()
//      const
extern "C" Q_DECL_EXPORT
QPlatformPixmap *ritual_own_ZNK21QRasterPlatformPixmap30createCompatiblePlatformPixmapEv(
    const QRasterPlatformPixmap *self) {
  return self->QRasterPlatformPixmap::createCompatiblePlatformPixmap();
}

//  void QRasterPlatformPixmap::resize(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QRasterPlatformPixmap6resizeEii(
    QRasterPlatformPixmap *self,
    int width,
    int height) {
  self->QRasterPlatformPixmap::resize(width, height);
}

//  void QRasterPlatformPixmap::fromImage(const QImage &image,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QRasterPlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    QRasterPlatformPixmap *self,
    const QImage *image,
    int flags) {
  self->QRasterPlatformPixmap::fromImage(
      *image,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QRasterPlatformPixmap::fromImageReader(QImageReader *imageReader,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QRasterPlatformPixmap15fromImageReaderEP12QImageReader6QFlagsIN2Qt19ImageConversionFlagEE(
    QRasterPlatformPixmap *self,
    QImageReader *imageReader,
    int flags) {
  self->QRasterPlatformPixmap::fromImageReader(
      imageReader,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QRasterPlatformPixmap::copy(const QPlatformPixmap *data, const QRect
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QRasterPlatformPixmap4copyEPK15QPlatformPixmapRK5QRect(
    QRasterPlatformPixmap *self,
    const QPlatformPixmap *data,
    const QRect *rect) {
  self->QRasterPlatformPixmap::copy(data, *rect);
}

//  bool QRasterPlatformPixmap::scroll(int dx, int dy, const QRect &rect)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QRasterPlatformPixmap6scrollEiiRK5QRect(
    QRasterPlatformPixmap *self,
    int dx,
    int dy,
    const QRect *rect) {
  return self->QRasterPlatformPixmap::scroll(dx, dy, *rect);
}

//  void QRasterPlatformPixmap::fill(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QRasterPlatformPixmap4fillERK6QColor(
    QRasterPlatformPixmap *self,
    const QColor *color) {
  self->QRasterPlatformPixmap::fill(*color);
}

//  bool QRasterPlatformPixmap::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QRasterPlatformPixmap15hasAlphaChannelEv(
    const QRasterPlatformPixmap *self) {
  return self->QRasterPlatformPixmap::hasAlphaChannel();
}

//  QImage QRasterPlatformPixmap::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK21QRasterPlatformPixmap7toImageEv(
    const QRasterPlatformPixmap *self) {
  return new QImage(self->QRasterPlatformPixmap::toImage());
}

//  QImage QRasterPlatformPixmap::toImage(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK21QRasterPlatformPixmap7toImageERK5QRect(
    const QRasterPlatformPixmap *self,
    const QRect *rect) {
  return new QImage(self->QRasterPlatformPixmap::toImage(*rect));
}

//  QPaintEngine *QRasterPlatformPixmap::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK21QRasterPlatformPixmap11paintEngineEv(
    const QRasterPlatformPixmap *self) {
  return self->QRasterPlatformPixmap::paintEngine();
}

//  QImage *QRasterPlatformPixmap::buffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN21QRasterPlatformPixmap6bufferEv(
    QRasterPlatformPixmap *self) {
  return self->QRasterPlatformPixmap::buffer();
}

//  qreal QRasterPlatformPixmap::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK21QRasterPlatformPixmap16devicePixelRatioEv(
    const QRasterPlatformPixmap *self) {
  return self->QRasterPlatformPixmap::devicePixelRatio();
}

//  void QRasterPlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QRasterPlatformPixmap19setDevicePixelRatioEd(
    QRasterPlatformPixmap *self,
    qreal scaleFactor) {
  self->QRasterPlatformPixmap::setDevicePixelRatio(scaleFactor);
}

//  int QRasterPlatformPixmap::metric(QPaintDevice::PaintDeviceMetric metric)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QRasterPlatformPixmap6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QRasterPlatformPixmap *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return static_cast<const OwnQRasterPlatformPixmap *>(self)->OwnQRasterPlatformPixmap::metric(
      metric);
}
