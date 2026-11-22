//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpaintdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpaintdevice.h>
#include <cstring>

//  Only a class built on QPaintDevice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPaintDevice : QPaintDevice {
  using QPaintDevice::metric;
  using QPaintDevice::initPainter;
  using QPaintDevice::redirected;
  using QPaintDevice::sharedPainter;
};

//  A QPaintDevice that Python can take functions over in. Every QPaintDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPaintDeviceCall0)(const void *, int *);
typedef void * (*CuteQPaintDeviceCall1)(const void *, int *);
typedef int (*CuteQPaintDeviceCall2)(const void *, int, int *);
typedef void (*CuteQPaintDeviceCall3)(const void *, QPainter *, int *);
typedef void * (*CuteQPaintDeviceCall4)(const void *, QPoint *, int *);
typedef void * (*CuteQPaintDeviceCall5)(const void *, int *);
class CuteQPaintDevice : public QPaintDevice {
public:
  using QPaintDevice::QPaintDevice;
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

  //  int QPaintDevice::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPaintDeviceCall0 call = reinterpret_cast<CuteQPaintDeviceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintDevice::devType();
  }

  //  QPaintEngine *QPaintDevice::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPaintDeviceCall1 call = reinterpret_cast<CuteQPaintDeviceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return {};
  }

  //  int QPaintDevice::metric(PaintDeviceMetric metric) const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPaintDeviceCall2 call = reinterpret_cast<CuteQPaintDeviceCall2>(taken[2]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QPaintDevice::metric(metric);
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPaintDeviceCall3 call = reinterpret_cast<CuteQPaintDeviceCall3>(taken[3]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPaintDeviceCall4 call = reinterpret_cast<CuteQPaintDeviceCall4>(taken[4]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPaintDeviceCall5 call = reinterpret_cast<CuteQPaintDeviceCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

//  QPaintDevice::~QPaintDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintDeviceD1Ev(QPaintDevice *self) {
  delete self;
}

//  int QPaintDevice::devType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice7devTypeEv(const QPaintDevice *self) {
  return self->devType();
}

//  bool QPaintDevice::paintingActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPaintDevice14paintingActiveEv(const QPaintDevice *self) {
  return self->paintingActive();
}

//  QPaintEngine *QPaintDevice::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK12QPaintDevice11paintEngineEv(
    const QPaintDevice *self) {
  return self->paintEngine();
}

//  int QPaintDevice::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice5widthEv(const QPaintDevice *self) {
  return self->width();
}

//  int QPaintDevice::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice6heightEv(const QPaintDevice *self) {
  return self->height();
}

//  int QPaintDevice::widthMM() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice7widthMMEv(const QPaintDevice *self) {
  return self->widthMM();
}

//  int QPaintDevice::heightMM() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice8heightMMEv(const QPaintDevice *self) {
  return self->heightMM();
}

//  int QPaintDevice::logicalDpiX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice11logicalDpiXEv(const QPaintDevice *self) {
  return self->logicalDpiX();
}

//  int QPaintDevice::logicalDpiY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice11logicalDpiYEv(const QPaintDevice *self) {
  return self->logicalDpiY();
}

//  int QPaintDevice::physicalDpiX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice12physicalDpiXEv(const QPaintDevice *self) {
  return self->physicalDpiX();
}

//  int QPaintDevice::physicalDpiY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice12physicalDpiYEv(const QPaintDevice *self) {
  return self->physicalDpiY();
}

//  qreal QPaintDevice::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPaintDevice16devicePixelRatioEv(
    const QPaintDevice *self) {
  return self->devicePixelRatio();
}

//  qreal QPaintDevice::devicePixelRatioF() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPaintDevice17devicePixelRatioFEv(
    const QPaintDevice *self) {
  return self->devicePixelRatioF();
}

//  int QPaintDevice::colorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice10colorCountEv(const QPaintDevice *self) {
  return self->colorCount();
}

//  int QPaintDevice::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice5depthEv(const QPaintDevice *self) {
  return self->depth();
}

//  qreal QPaintDevice::devicePixelRatioFScale()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN12QPaintDevice22devicePixelRatioFScaleEv() {
  return QPaintDevice::devicePixelRatioFScale();
}

//  int QPaintDevice::encodeMetricF(PaintDeviceMetric metric, double value)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QPaintDevice13encodeMetricFENS_17PaintDeviceMetricEd(
    QPaintDevice::PaintDeviceMetric metric,
    double value) {
  return QPaintDevice::encodeMetricF(metric, value);
}

//  a Python function taken by a CuteQPaintDevice, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPaintDevice(
    QPaintDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPaintDevice *>(self)->take(key, call);
}

//  int QPaintDevice::devType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QPaintDevice7devTypeEv(const QPaintDevice *self) {
  return self->QPaintDevice::devType();
}

//  int QPaintDevice::metric(PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE(
    const QPaintDevice *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return static_cast<const OwnQPaintDevice *>(self)->OwnQPaintDevice::metric(
      metric);
}

//  void QPaintDevice::initPainter(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QPaintDevice11initPainterEP8QPainter(
    const QPaintDevice *self,
    QPainter *painter) {
  static_cast<const OwnQPaintDevice *>(self)->OwnQPaintDevice::initPainter(
      painter);
}

//  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_own_ZNK12QPaintDevice10redirectedEP6QPoint(
    const QPaintDevice *self,
    QPoint *offset) {
  return static_cast<const OwnQPaintDevice *>(self)->OwnQPaintDevice::redirected(
      offset);
}

//  QPainter *QPaintDevice::sharedPainter() const
extern "C" Q_DECL_EXPORT
QPainter *ritual_own_ZNK12QPaintDevice13sharedPainterEv(
    const QPaintDevice *self) {
  return static_cast<const OwnQPaintDevice *>(self)->OwnQPaintDevice::sharedPainter();
}
