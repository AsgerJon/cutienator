//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpicture.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpicture.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <cstring>

//  Only a class built on QPicture may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPicture : QPicture {
  using QPicture::metric;
};

//  A QPicture that Python can take functions over in. Every QPicture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPictureCall0)(const void *, int *);
typedef void * (*CuteQPictureCall1)(const void *, int *);
typedef int (*CuteQPictureCall2)(const void *, int, int *);
typedef void (*CuteQPictureCall3)(const void *, QPainter *, int *);
typedef void * (*CuteQPictureCall4)(const void *, QPoint *, int *);
typedef void * (*CuteQPictureCall5)(const void *, int *);
class CuteQPicture : public QPicture {
public:
  using QPicture::QPicture;
  CuteQPicture(const QPicture &other) : QPicture(other) {}
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

  //  int QPicture::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPictureCall0 call = reinterpret_cast<CuteQPictureCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPicture::devType();
  }

  //  QPaintEngine *QPicture::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPictureCall1 call = reinterpret_cast<CuteQPictureCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPicture::paintEngine();
  }

  //  int QPicture::metric(PaintDeviceMetric m) const
  int metric(QPaintDevice::PaintDeviceMetric m) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPictureCall2 call = reinterpret_cast<CuteQPictureCall2>(taken[2]);
      int given = call(this, static_cast<int>(m), &handled);
      if (handled) return given;
    }
    return QPicture::metric(m);
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPictureCall3 call = reinterpret_cast<CuteQPictureCall3>(taken[3]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPictureCall4 call = reinterpret_cast<CuteQPictureCall4>(taken[4]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPictureCall5 call = reinterpret_cast<CuteQPictureCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

//  QPicture::QPicture(int formatVersion)
extern "C" Q_DECL_EXPORT
QPicture *ritual_ZN8QPictureC1Ei(int formatVersion) {
  return new CuteQPicture(formatVersion);
}

//  QPicture::QPicture(const QPicture &a0)
extern "C" Q_DECL_EXPORT
QPicture *ritual_ZN8QPictureC1ERKS_(const QPicture *a0) {
  return new CuteQPicture(*a0);
}

//  QPicture::~QPicture()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPictureD1Ev(QPicture *self) {
  delete self;
}

//  bool QPicture::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPicture6isNullEv(const QPicture *self) {
  return self->isNull();
}

//  int QPicture::devType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPicture7devTypeEv(const QPicture *self) {
  return self->devType();
}

//  uint QPicture::size() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK8QPicture4sizeEv(const QPicture *self) {
  return self->size();
}

//  const char *QPicture::data() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK8QPicture4dataEv(const QPicture *self) {
  return self->data();
}

//  void QPicture::setData(const char *data, uint size)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPicture7setDataEPKcj(
    QPicture *self,
    const char *data,
    uint size) {
  self->setData(data, size);
}

//  bool QPicture::play(QPainter *p)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4playEP8QPainter(QPicture *self, QPainter *p) {
  return self->play(p);
}

//  bool QPicture::load(QIODevice *dev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4loadEP9QIODevice(QPicture *self, QIODevice *dev) {
  return self->load(dev);
}

//  bool QPicture::load(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4loadERK7QString(
    QPicture *self,
    const QString *fileName) {
  return self->load(*fileName);
}

//  bool QPicture::save(QIODevice *dev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4saveEP9QIODevice(QPicture *self, QIODevice *dev) {
  return self->save(dev);
}

//  bool QPicture::save(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPicture4saveERK7QString(
    QPicture *self,
    const QString *fileName) {
  return self->save(*fileName);
}

//  QRect QPicture::boundingRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QPicture12boundingRectEv(const QPicture *self) {
  return new QRect(self->boundingRect());
}

//  void QPicture::setBoundingRect(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPicture15setBoundingRectERK5QRect(
    QPicture *self,
    const QRect *r) {
  self->setBoundingRect(*r);
}

//  void QPicture::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPicture6detachEv(QPicture *self) {
  self->detach();
}

//  bool QPicture::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPicture10isDetachedEv(const QPicture *self) {
  return self->isDetached();
}

//  QPaintEngine *QPicture::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK8QPicture11paintEngineEv(const QPicture *self) {
  return self->paintEngine();
}

//  int QPicture::metric(PaintDeviceMetric m) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPicture6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPicture *self,
    QPaintDevice::PaintDeviceMetric m) {
  return self->metric(m);
}

//  a Python function taken by a CuteQPicture, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPicture(QPicture *self, const char *key, void *call) {
  return static_cast<CuteQPicture *>(self)->take(key, call);
}

//  int QPicture::devType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK8QPicture7devTypeEv(const QPicture *self) {
  return self->QPicture::devType();
}

//  QPaintEngine *QPicture::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK8QPicture11paintEngineEv(const QPicture *self) {
  return self->QPicture::paintEngine();
}

//  int QPicture::metric(PaintDeviceMetric m) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK8QPicture6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPicture *self,
    QPaintDevice::PaintDeviceMetric m) {
  return static_cast<const OwnQPicture *>(self)->OwnQPicture::metric(m);
}
