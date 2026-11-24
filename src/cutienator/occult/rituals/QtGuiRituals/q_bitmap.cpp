//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbitmap.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qbitmap.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>
#include <cstring>

//  A QBitmap that Python can take functions over in. Every QBitmap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQBitmapCall0)(const void *, int *);
typedef void * (*CuteQBitmapCall1)(const void *, int *);
typedef int (*CuteQBitmapCall2)(const void *, int, int *);
typedef void (*CuteQBitmapCall3)(const void *, QPainter *, int *);
typedef void * (*CuteQBitmapCall4)(const void *, QPoint *, int *);
typedef void * (*CuteQBitmapCall5)(const void *, int *);
class CuteQBitmap : public QBitmap {
public:
  using QBitmap::QBitmap;
  CuteQBitmap(const QBitmap &other) : QBitmap(other) {}
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
      CuteQBitmapCall0 call = reinterpret_cast<CuteQBitmapCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPixmap::devType();
  }

  //  QPaintEngine *QPixmap::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQBitmapCall1 call = reinterpret_cast<CuteQBitmapCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPixmap::paintEngine();
  }

  //  int QPixmap::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQBitmapCall2 call = reinterpret_cast<CuteQBitmapCall2>(taken[2]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QPixmap::metric(a0);
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQBitmapCall3 call = reinterpret_cast<CuteQBitmapCall3>(taken[3]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQBitmapCall4 call = reinterpret_cast<CuteQBitmapCall4>(taken[4]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQBitmapCall5 call = reinterpret_cast<CuteQBitmapCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

//  QBitmap::QBitmap()
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1Ev() {
  return new CuteQBitmap();
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QBitmap::QBitmap(const QPixmap &a0)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1ERK7QPixmap(const QPixmap *a0) {
  return new CuteQBitmap(*a0);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  QBitmap::QBitmap(int w, int h)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1Eii(int w, int h) {
  return new CuteQBitmap(w, h);
}

//  QBitmap::QBitmap(const QSize &a0)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1ERK5QSize(const QSize *a0) {
  return new CuteQBitmap(*a0);
}

//  QBitmap::QBitmap(const QString &fileName, const char *format)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1ERK7QStringPKc(
    const QString *fileName,
    const char *format) {
  return new CuteQBitmap(*fileName, format);
}

//  QBitmap::~QBitmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBitmapD1Ev(QBitmap *self) {
  delete self;
}

//  QVariant QBitmap::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QBitmapcv8QVariantEv(const QBitmap *self) {
  return new QVariant(self->operator QVariant());
}

//  void QBitmap::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBitmap5clearEv(QBitmap *self) {
  self->clear();
}

//  QBitmap QBitmap::fromImage(const QImage &image, Qt::ImageConversionFlags
//      flags)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    const QImage *image,
    int flags) {
  return new QBitmap(
      QBitmap::fromImage(
          *image,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  QBitmap QBitmap::fromPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmap10fromPixmapERK7QPixmap(const QPixmap *pixmap) {
  return new QBitmap(QBitmap::fromPixmap(*pixmap));
}

//  QBitmap QBitmap::transformed(const QTransform &matrix) const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK7QBitmap11transformedERK10QTransform(
    const QBitmap *self,
    const QTransform *matrix) {
  return new QBitmap(self->transformed(*matrix));
}

//  a Python function taken by a CuteQBitmap, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBitmap(QBitmap *self, const char *key, void *call) {
  return static_cast<CuteQBitmap *>(self)->take(key, call);
}
