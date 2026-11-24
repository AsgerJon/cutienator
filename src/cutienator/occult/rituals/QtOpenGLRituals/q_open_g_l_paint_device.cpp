//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglpaintdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopenglpaintdevice.h>
#include <QtCore/qsize.h>
#include <cstring>

//  Only a class built on QOpenGLPaintDevice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQOpenGLPaintDevice : QOpenGLPaintDevice {
  using QOpenGLPaintDevice::metric;
};

//  A QOpenGLPaintDevice that Python can take functions over in. Every QOpenGLPaintDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef int (*CuteQOpenGLPaintDeviceCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void * (*CuteQOpenGLPaintDeviceCall1)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLPaintDeviceCall2)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef int (*CuteQOpenGLPaintDeviceCall3)(const void *, int, int *);
#endif  // !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLPaintDeviceCall4)(const void *, QPainter *, int *);
typedef void * (*CuteQOpenGLPaintDeviceCall5)(const void *, QPoint *, int *);
typedef void * (*CuteQOpenGLPaintDeviceCall6)(const void *, int *);
class CuteQOpenGLPaintDevice : public QOpenGLPaintDevice {
public:
  using QOpenGLPaintDevice::QOpenGLPaintDevice;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN18QOpenGLPaintDevice18ensureActiveTargetEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_OPENGL)
  //  int QOpenGLPaintDevice::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLPaintDeviceCall0 call = reinterpret_cast<CuteQOpenGLPaintDeviceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLPaintDevice::devType();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  QPaintEngine *QOpenGLPaintDevice::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLPaintDeviceCall1 call = reinterpret_cast<CuteQOpenGLPaintDeviceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QOpenGLPaintDevice::paintEngine();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLPaintDevice::ensureActiveTarget()
  void ensureActiveTarget() override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLPaintDeviceCall2 call = reinterpret_cast<CuteQOpenGLPaintDeviceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLPaintDevice::ensureActiveTarget();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  int QOpenGLPaintDevice::metric(QPaintDevice::PaintDeviceMetric
  //      metric) const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLPaintDeviceCall3 call = reinterpret_cast<CuteQOpenGLPaintDeviceCall3>(taken[3]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QOpenGLPaintDevice::metric(metric);
  }
#endif  // !defined(QT_NO_OPENGL)

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLPaintDeviceCall4 call = reinterpret_cast<CuteQOpenGLPaintDeviceCall4>(taken[4]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLPaintDeviceCall5 call = reinterpret_cast<CuteQOpenGLPaintDeviceCall5>(taken[5]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGLPaintDeviceCall6 call = reinterpret_cast<CuteQOpenGLPaintDeviceCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

//  QOpenGLPaintDevicePrivate *QOpenGLPaintDevice::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLPaintDevicePrivate *ritual_ZN18QOpenGLPaintDevice6d_funcEv(
    QOpenGLPaintDevice *self) {
  return self->d_func();
}

//  const QOpenGLPaintDevicePrivate *QOpenGLPaintDevice::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLPaintDevicePrivate *ritual_ZNK18QOpenGLPaintDevice6d_funcEv(
    const QOpenGLPaintDevice *self) {
  return self->d_func();
}

//  QOpenGLPaintDevice::QOpenGLPaintDevice()
extern "C" Q_DECL_EXPORT
QOpenGLPaintDevice *ritual_ZN18QOpenGLPaintDeviceC1Ev() {
  return new CuteQOpenGLPaintDevice();
}

//  QOpenGLPaintDevice::QOpenGLPaintDevice(const QSize &size)
extern "C" Q_DECL_EXPORT
QOpenGLPaintDevice *ritual_ZN18QOpenGLPaintDeviceC1ERK5QSize(
    const QSize *size) {
  return new CuteQOpenGLPaintDevice(*size);
}

//  QOpenGLPaintDevice::QOpenGLPaintDevice(int width, int height)
extern "C" Q_DECL_EXPORT
QOpenGLPaintDevice *ritual_ZN18QOpenGLPaintDeviceC1Eii(
    int width,
    int height) {
  return new CuteQOpenGLPaintDevice(width, height);
}

//  QOpenGLPaintDevice::~QOpenGLPaintDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLPaintDeviceD1Ev(QOpenGLPaintDevice *self) {
  delete self;
}

//  int QOpenGLPaintDevice::devType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QOpenGLPaintDevice7devTypeEv(
    const QOpenGLPaintDevice *self) {
  return self->devType();
}

//  QPaintEngine *QOpenGLPaintDevice::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK18QOpenGLPaintDevice11paintEngineEv(
    const QOpenGLPaintDevice *self) {
  return self->paintEngine();
}

//  QOpenGLContext *QOpenGLPaintDevice::context() const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK18QOpenGLPaintDevice7contextEv(
    const QOpenGLPaintDevice *self) {
  return self->context();
}

//  QSize QOpenGLPaintDevice::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QOpenGLPaintDevice4sizeEv(
    const QOpenGLPaintDevice *self) {
  return new QSize(self->size());
}

//  void QOpenGLPaintDevice::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLPaintDevice7setSizeERK5QSize(
    QOpenGLPaintDevice *self,
    const QSize *size) {
  self->setSize(*size);
}

//  void QOpenGLPaintDevice::setDevicePixelRatio(qreal devicePixelRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLPaintDevice19setDevicePixelRatioEd(
    QOpenGLPaintDevice *self,
    qreal devicePixelRatio) {
  self->setDevicePixelRatio(devicePixelRatio);
}

//  qreal QOpenGLPaintDevice::dotsPerMeterX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QOpenGLPaintDevice13dotsPerMeterXEv(
    const QOpenGLPaintDevice *self) {
  return self->dotsPerMeterX();
}

//  qreal QOpenGLPaintDevice::dotsPerMeterY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QOpenGLPaintDevice13dotsPerMeterYEv(
    const QOpenGLPaintDevice *self) {
  return self->dotsPerMeterY();
}

//  void QOpenGLPaintDevice::setDotsPerMeterX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLPaintDevice16setDotsPerMeterXEd(
    QOpenGLPaintDevice *self,
    qreal a0) {
  self->setDotsPerMeterX(a0);
}

//  void QOpenGLPaintDevice::setDotsPerMeterY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLPaintDevice16setDotsPerMeterYEd(
    QOpenGLPaintDevice *self,
    qreal a0) {
  self->setDotsPerMeterY(a0);
}

//  void QOpenGLPaintDevice::setPaintFlipped(bool flipped)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLPaintDevice15setPaintFlippedEb(
    QOpenGLPaintDevice *self,
    bool flipped) {
  self->setPaintFlipped(flipped);
}

//  bool QOpenGLPaintDevice::paintFlipped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QOpenGLPaintDevice12paintFlippedEv(
    const QOpenGLPaintDevice *self) {
  return self->paintFlipped();
}

//  void QOpenGLPaintDevice::ensureActiveTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLPaintDevice18ensureActiveTargetEv(
    QOpenGLPaintDevice *self) {
  self->ensureActiveTarget();
}

//  int QOpenGLPaintDevice::metric(QPaintDevice::PaintDeviceMetric metric)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QOpenGLPaintDevice6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QOpenGLPaintDevice *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  a Python function taken by a CuteQOpenGLPaintDevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLPaintDevice(
    QOpenGLPaintDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLPaintDevice *>(self)->take(key, call);
}

//  int QOpenGLPaintDevice::devType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QOpenGLPaintDevice7devTypeEv(
    const QOpenGLPaintDevice *self) {
  return self->QOpenGLPaintDevice::devType();
}

//  QPaintEngine *QOpenGLPaintDevice::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK18QOpenGLPaintDevice11paintEngineEv(
    const QOpenGLPaintDevice *self) {
  return self->QOpenGLPaintDevice::paintEngine();
}

//  void QOpenGLPaintDevice::ensureActiveTarget()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QOpenGLPaintDevice18ensureActiveTargetEv(
    QOpenGLPaintDevice *self) {
  self->QOpenGLPaintDevice::ensureActiveTarget();
}

//  int QOpenGLPaintDevice::metric(QPaintDevice::PaintDeviceMetric metric)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QOpenGLPaintDevice6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QOpenGLPaintDevice *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return static_cast<const OwnQOpenGLPaintDevice *>(self)->OwnQOpenGLPaintDevice::metric(
      metric);
}

#endif  // !defined(QT_NO_OPENGL)
