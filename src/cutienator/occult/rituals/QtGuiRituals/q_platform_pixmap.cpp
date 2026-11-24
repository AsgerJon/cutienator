//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformpixmap.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformpixmap.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpixmap.h>
#include <cstring>

//  A QPlatformPixmap that Python can take functions over in. Every QPlatformPixmap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformPixmapCall0)(const void *, int *);
typedef void (*CuteQPlatformPixmapCall1)(const void *, int, int, int *);
typedef void (*CuteQPlatformPixmapCall2)(const void *, const QImage *, int, int *);
typedef void (*CuteQPlatformPixmapCall3)(const void *, QImageReader *, int, int *);
typedef void (*CuteQPlatformPixmapCall4)(const void *, const QPlatformPixmap *, const QRect *, int *);
typedef bool (*CuteQPlatformPixmapCall5)(const void *, int, int, const QRect *, int *);
typedef int (*CuteQPlatformPixmapCall6)(const void *, int, int *);
typedef void (*CuteQPlatformPixmapCall7)(const void *, const QColor *, int *);
typedef const QBitmap * (*CuteQPlatformPixmapCall8)(const void *, int *);
typedef void (*CuteQPlatformPixmapCall9)(const void *, const QBitmap *, int *);
typedef bool (*CuteQPlatformPixmapCall10)(const void *, int *);
typedef const QPixmap * (*CuteQPlatformPixmapCall11)(const void *, const QTransform *, int, int *);
typedef const QImage * (*CuteQPlatformPixmapCall12)(const void *, int *);
typedef const QImage * (*CuteQPlatformPixmapCall13)(const void *, const QRect *, int *);
typedef void * (*CuteQPlatformPixmapCall14)(const void *, int *);
typedef qreal (*CuteQPlatformPixmapCall15)(const void *, int *);
typedef void (*CuteQPlatformPixmapCall16)(const void *, qreal, int *);
typedef void * (*CuteQPlatformPixmapCall17)(const void *, int *);
class CuteQPlatformPixmap : public QPlatformPixmap {
public:
  using QPlatformPixmap::QPlatformPixmap;
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
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap6metricEN12QPaintDevice17PaintDeviceMetricE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap4fillERK6QColor")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap4maskEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap7setMaskERK7QBitmap")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap15hasAlphaChannelEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap11transformedERK10QTransformN2Qt18TransformationModeE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap7toImageEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap7toImageERK5QRect")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap11paintEngineEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformPixmap16devicePixelRatioEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap19setDevicePixelRatioEd")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformPixmap6bufferEv")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  QPlatformPixmap *QPlatformPixmap::createCompatiblePlatformPixmap()
  //      const
  QPlatformPixmap *createCompatiblePlatformPixmap() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformPixmapCall0 call = reinterpret_cast<CuteQPlatformPixmapCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformPixmap *>(given);
    }
    return QPlatformPixmap::createCompatiblePlatformPixmap();
  }

  //  void QPlatformPixmap::resize(int width, int height)
  void resize(int width, int height) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformPixmapCall1 call = reinterpret_cast<CuteQPlatformPixmapCall1>(taken[1]);
      call(this, width, height, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformPixmap::fromImage(const QImage &image,
  //      Qt::ImageConversionFlags flags)
  void fromImage(
      const QImage &image,
      Qt::ImageConversionFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformPixmapCall2 call = reinterpret_cast<CuteQPlatformPixmapCall2>(taken[2]);
      call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QPlatformPixmap::fromImageReader(QImageReader *imageReader,
  //      Qt::ImageConversionFlags flags)
  void fromImageReader(
      QImageReader *imageReader,
      Qt::ImageConversionFlags flags) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformPixmapCall3 call = reinterpret_cast<CuteQPlatformPixmapCall3>(taken[3]);
      call(this, imageReader, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QPlatformPixmap::fromImageReader(imageReader, flags);
  }

  //  void QPlatformPixmap::copy(const QPlatformPixmap *data, const QRect
  //      &rect)
  void copy(const QPlatformPixmap *data, const QRect &rect) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformPixmapCall4 call = reinterpret_cast<CuteQPlatformPixmapCall4>(taken[4]);
      call(this, data, &rect, &handled);
      if (handled) return;
    }
    QPlatformPixmap::copy(data, rect);
  }

  //  bool QPlatformPixmap::scroll(int dx, int dy, const QRect &rect)
  bool scroll(int dx, int dy, const QRect &rect) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformPixmapCall5 call = reinterpret_cast<CuteQPlatformPixmapCall5>(taken[5]);
      bool given = call(this, dx, dy, &rect, &handled);
      if (handled) return given;
    }
    return QPlatformPixmap::scroll(dx, dy, rect);
  }

  //  int QPlatformPixmap::metric(QPaintDevice::PaintDeviceMetric metric)
  //      const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformPixmapCall6 call = reinterpret_cast<CuteQPlatformPixmapCall6>(taken[6]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPlatformPixmap::fill(const QColor &color)
  void fill(const QColor &color) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformPixmapCall7 call = reinterpret_cast<CuteQPlatformPixmapCall7>(taken[7]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  QBitmap QPlatformPixmap::mask() const
  QBitmap mask() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformPixmapCall8 call = reinterpret_cast<CuteQPlatformPixmapCall8>(taken[8]);
      const QBitmap * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPixmap::mask();
  }

  //  void QPlatformPixmap::setMask(const QBitmap &mask)
  void setMask(const QBitmap &mask) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformPixmapCall9 call = reinterpret_cast<CuteQPlatformPixmapCall9>(taken[9]);
      call(this, &mask, &handled);
      if (handled) return;
    }
    QPlatformPixmap::setMask(mask);
  }

  //  bool QPlatformPixmap::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformPixmapCall10 call = reinterpret_cast<CuteQPlatformPixmapCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QPixmap QPlatformPixmap::transformed(const QTransform &matrix,
  //      Qt::TransformationMode mode) const
  QPixmap transformed(
      const QTransform &matrix,
      Qt::TransformationMode mode) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformPixmapCall11 call = reinterpret_cast<CuteQPlatformPixmapCall11>(taken[11]);
      const QPixmap * given = call(this, &matrix, static_cast<int>(mode), &handled);
      if (handled && given) return *given;
    }
    return QPlatformPixmap::transformed(matrix, mode);
  }

  //  QImage QPlatformPixmap::toImage() const
  QImage toImage() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformPixmapCall12 call = reinterpret_cast<CuteQPlatformPixmapCall12>(taken[12]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QImage QPlatformPixmap::toImage(const QRect &rect) const
  QImage toImage(const QRect &rect) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformPixmapCall13 call = reinterpret_cast<CuteQPlatformPixmapCall13>(taken[13]);
      const QImage * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPixmap::toImage(rect);
  }

  //  QPaintEngine *QPlatformPixmap::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformPixmapCall14 call = reinterpret_cast<CuteQPlatformPixmapCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return {};
  }

  //  qreal QPlatformPixmap::devicePixelRatio() const
  qreal devicePixelRatio() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformPixmapCall15 call = reinterpret_cast<CuteQPlatformPixmapCall15>(taken[15]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
  void setDevicePixelRatio(qreal scaleFactor) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformPixmapCall16 call = reinterpret_cast<CuteQPlatformPixmapCall16>(taken[16]);
      call(this, scaleFactor, &handled);
      if (handled) return;
    }
  }

  //  QImage *QPlatformPixmap::buffer()
  QImage *buffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformPixmapCall17 call = reinterpret_cast<CuteQPlatformPixmapCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QImage *>(given);
    }
    return QPlatformPixmap::buffer();
  }
};

//  QPlatformPixmap::~QPlatformPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmapD1Ev(QPlatformPixmap *self) {
  delete self;
}

//  QPlatformPixmap *QPlatformPixmap::createCompatiblePlatformPixmap() const
extern "C" Q_DECL_EXPORT
QPlatformPixmap *ritual_ZNK15QPlatformPixmap30createCompatiblePlatformPixmapEv(
    const QPlatformPixmap *self) {
  return self->createCompatiblePlatformPixmap();
}

//  void QPlatformPixmap::resize(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap6resizeEii(
    QPlatformPixmap *self,
    int width,
    int height) {
  self->resize(width, height);
}

//  void QPlatformPixmap::fromImage(const QImage &image,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    QPlatformPixmap *self,
    const QImage *image,
    int flags) {
  self->fromImage(*image, QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPlatformPixmap::fromImageReader(QImageReader *imageReader,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap15fromImageReaderEP12QImageReader6QFlagsIN2Qt19ImageConversionFlagEE(
    QPlatformPixmap *self,
    QImageReader *imageReader,
    int flags) {
  self->fromImageReader(
      imageReader,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  bool QPlatformPixmap::fromFile(const QString &filename, const char
//      *format, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformPixmap8fromFileERK7QStringPKc6QFlagsIN2Qt19ImageConversionFlagEE(
    QPlatformPixmap *self,
    const QString *filename,
    const char *format,
    int flags) {
  return self->fromFile(
      *filename,
      format,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPlatformPixmap::copy(const QPlatformPixmap *data, const QRect
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap4copyEPKS_RK5QRect(
    QPlatformPixmap *self,
    const QPlatformPixmap *data,
    const QRect *rect) {
  self->copy(data, *rect);
}

//  bool QPlatformPixmap::scroll(int dx, int dy, const QRect &rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformPixmap6scrollEiiRK5QRect(
    QPlatformPixmap *self,
    int dx,
    int dy,
    const QRect *rect) {
  return self->scroll(dx, dy, *rect);
}

//  int QPlatformPixmap::metric(QPaintDevice::PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPlatformPixmap6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPlatformPixmap *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  void QPlatformPixmap::fill(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap4fillERK6QColor(
    QPlatformPixmap *self,
    const QColor *color) {
  self->fill(*color);
}

//  QBitmap QPlatformPixmap::mask() const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK15QPlatformPixmap4maskEv(const QPlatformPixmap *self) {
  return new QBitmap(self->mask());
}

//  void QPlatformPixmap::setMask(const QBitmap &mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap7setMaskERK7QBitmap(
    QPlatformPixmap *self,
    const QBitmap *mask) {
  self->setMask(*mask);
}

//  bool QPlatformPixmap::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformPixmap15hasAlphaChannelEv(
    const QPlatformPixmap *self) {
  return self->hasAlphaChannel();
}

//  QPixmap QPlatformPixmap::transformed(const QTransform &matrix,
//      Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK15QPlatformPixmap11transformedERK10QTransformN2Qt18TransformationModeE(
    const QPlatformPixmap *self,
    const QTransform *matrix,
    Qt::TransformationMode mode) {
  return new QPixmap(self->transformed(*matrix, mode));
}

//  QImage QPlatformPixmap::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK15QPlatformPixmap7toImageEv(const QPlatformPixmap *self) {
  return new QImage(self->toImage());
}

//  QImage QPlatformPixmap::toImage(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK15QPlatformPixmap7toImageERK5QRect(
    const QPlatformPixmap *self,
    const QRect *rect) {
  return new QImage(self->toImage(*rect));
}

//  QPaintEngine *QPlatformPixmap::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK15QPlatformPixmap11paintEngineEv(
    const QPlatformPixmap *self) {
  return self->paintEngine();
}

//  int QPlatformPixmap::serialNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPlatformPixmap12serialNumberEv(
    const QPlatformPixmap *self) {
  return self->serialNumber();
}

//  PixelType QPlatformPixmap::pixelType() const
extern "C" Q_DECL_EXPORT
QPlatformPixmap::PixelType ritual_ZNK15QPlatformPixmap9pixelTypeEv(
    const QPlatformPixmap *self) {
  return self->pixelType();
}

//  ClassId QPlatformPixmap::classId() const
extern "C" Q_DECL_EXPORT
QPlatformPixmap::ClassId ritual_ZNK15QPlatformPixmap7classIdEv(
    const QPlatformPixmap *self) {
  return self->classId();
}

//  qreal QPlatformPixmap::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QPlatformPixmap16devicePixelRatioEv(
    const QPlatformPixmap *self) {
  return self->devicePixelRatio();
}

//  void QPlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap19setDevicePixelRatioEd(
    QPlatformPixmap *self,
    qreal scaleFactor) {
  self->setDevicePixelRatio(scaleFactor);
}

//  QImage *QPlatformPixmap::buffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN15QPlatformPixmap6bufferEv(QPlatformPixmap *self) {
  return self->buffer();
}

//  int QPlatformPixmap::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPlatformPixmap5widthEv(const QPlatformPixmap *self) {
  return self->width();
}

//  int QPlatformPixmap::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPlatformPixmap6heightEv(const QPlatformPixmap *self) {
  return self->height();
}

//  int QPlatformPixmap::colorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPlatformPixmap10colorCountEv(const QPlatformPixmap *self) {
  return self->colorCount();
}

//  int QPlatformPixmap::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPlatformPixmap5depthEv(const QPlatformPixmap *self) {
  return self->depth();
}

//  bool QPlatformPixmap::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformPixmap6isNullEv(const QPlatformPixmap *self) {
  return self->isNull();
}

//  qint64 QPlatformPixmap::cacheKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QPlatformPixmap8cacheKeyEv(const QPlatformPixmap *self) {
  return self->cacheKey();
}

//  QPlatformPixmap *QPlatformPixmap::create(int w, int h, PixelType type)
extern "C" Q_DECL_EXPORT
QPlatformPixmap *ritual_ZN15QPlatformPixmap6createEiiNS_9PixelTypeE(
    int w,
    int h,
    QPlatformPixmap::PixelType type) {
  return QPlatformPixmap::create(w, h, type);
}

//  void QPlatformPixmap::setSerialNumber(int serNo)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap15setSerialNumberEi(
    QPlatformPixmap *self,
    int serNo) {
  self->setSerialNumber(serNo);
}

//  void QPlatformPixmap::setDetachNumber(int detNo)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap15setDetachNumberEi(
    QPlatformPixmap *self,
    int detNo) {
  self->setDetachNumber(detNo);
}

//  void QPlatformPixmap::callDestructionHooks()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformPixmap20callDestructionHooksEv(
    QPlatformPixmap *self) {
  self->callDestructionHooks();
}

//  a Python function taken by a CuteQPlatformPixmap, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformPixmap(
    QPlatformPixmap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformPixmap *>(self)->take(key, call);
}

//  QPlatformPixmap *QPlatformPixmap::createCompatiblePlatformPixmap() const
extern "C" Q_DECL_EXPORT
QPlatformPixmap *ritual_own_ZNK15QPlatformPixmap30createCompatiblePlatformPixmapEv(
    const QPlatformPixmap *self) {
  return self->QPlatformPixmap::createCompatiblePlatformPixmap();
}

//  void QPlatformPixmap::fromImageReader(QImageReader *imageReader,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformPixmap15fromImageReaderEP12QImageReader6QFlagsIN2Qt19ImageConversionFlagEE(
    QPlatformPixmap *self,
    QImageReader *imageReader,
    int flags) {
  self->QPlatformPixmap::fromImageReader(
      imageReader,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPlatformPixmap::copy(const QPlatformPixmap *data, const QRect
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformPixmap4copyEPKS_RK5QRect(
    QPlatformPixmap *self,
    const QPlatformPixmap *data,
    const QRect *rect) {
  self->QPlatformPixmap::copy(data, *rect);
}

//  bool QPlatformPixmap::scroll(int dx, int dy, const QRect &rect)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPlatformPixmap6scrollEiiRK5QRect(
    QPlatformPixmap *self,
    int dx,
    int dy,
    const QRect *rect) {
  return self->QPlatformPixmap::scroll(dx, dy, *rect);
}

//  QBitmap QPlatformPixmap::mask() const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_own_ZNK15QPlatformPixmap4maskEv(
    const QPlatformPixmap *self) {
  return new QBitmap(self->QPlatformPixmap::mask());
}

//  void QPlatformPixmap::setMask(const QBitmap &mask)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformPixmap7setMaskERK7QBitmap(
    QPlatformPixmap *self,
    const QBitmap *mask) {
  self->QPlatformPixmap::setMask(*mask);
}

//  QPixmap QPlatformPixmap::transformed(const QTransform &matrix,
//      Qt::TransformationMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK15QPlatformPixmap11transformedERK10QTransformN2Qt18TransformationModeE(
    const QPlatformPixmap *self,
    const QTransform *matrix,
    Qt::TransformationMode mode) {
  return new QPixmap(self->QPlatformPixmap::transformed(*matrix, mode));
}

//  QImage QPlatformPixmap::toImage(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK15QPlatformPixmap7toImageERK5QRect(
    const QPlatformPixmap *self,
    const QRect *rect) {
  return new QImage(self->QPlatformPixmap::toImage(*rect));
}

//  QImage *QPlatformPixmap::buffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN15QPlatformPixmap6bufferEv(QPlatformPixmap *self) {
  return self->QPlatformPixmap::buffer();
}
