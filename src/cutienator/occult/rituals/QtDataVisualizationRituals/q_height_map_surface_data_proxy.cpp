//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qheightmapsurfacedataproxy.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDataVisualization/qheightmapsurfacedataproxy.h>
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHeightMapSurfaceDataProxy that Python can take functions over in. Every QHeightMapSurfaceDataProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHeightMapSurfaceDataProxyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHeightMapSurfaceDataProxyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightMapSurfaceDataProxyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHeightMapSurfaceDataProxy : public QHeightMapSurfaceDataProxy {
public:
  using QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyCall0 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyCall1 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyCall2 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyCall3 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyCall4 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyCall5 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyCall6 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHeightMapSurfaceDataProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QHeightMapSurfaceDataProxy10metaObjectEv(
    const QHeightMapSurfaceDataProxy *self) {
  return self->metaObject();
}

//  void *QHeightMapSurfaceDataProxy::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QHeightMapSurfaceDataProxy11qt_metacastEPKc(
    QHeightMapSurfaceDataProxy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHeightMapSurfaceDataProxy::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QHeightMapSurfaceDataProxy11qt_metacallEN11QMetaObject4CallEiPPv(
    QHeightMapSurfaceDataProxy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHeightMapSurfaceDataProxy::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QHeightMapSurfaceDataProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHeightMapSurfaceDataProxy::tr(s, c, n));
}

//  QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(QObject *parent)
extern "C" Q_DECL_EXPORT
QHeightMapSurfaceDataProxy *ritual_ZN26QHeightMapSurfaceDataProxyC1EP7QObject(
    QObject *parent) {
  return new CuteQHeightMapSurfaceDataProxy(parent);
}

//  QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(const QImage
//      &image, QObject *parent)
extern "C" Q_DECL_EXPORT
QHeightMapSurfaceDataProxy *ritual_ZN26QHeightMapSurfaceDataProxyC1ERK6QImageP7QObject(
    const QImage *image,
    QObject *parent) {
  return new CuteQHeightMapSurfaceDataProxy(*image, parent);
}

//  QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(const QString
//      &filename, QObject *parent)
extern "C" Q_DECL_EXPORT
QHeightMapSurfaceDataProxy *ritual_ZN26QHeightMapSurfaceDataProxyC1ERK7QStringP7QObject(
    const QString *filename,
    QObject *parent) {
  return new CuteQHeightMapSurfaceDataProxy(*filename, parent);
}

//  QHeightMapSurfaceDataProxy::~QHeightMapSurfaceDataProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxyD1Ev(
    QHeightMapSurfaceDataProxy *self) {
  delete self;
}

//  void QHeightMapSurfaceDataProxy::setHeightMap(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy12setHeightMapERK6QImage(
    QHeightMapSurfaceDataProxy *self,
    const QImage *image) {
  self->setHeightMap(*image);
}

//  QImage QHeightMapSurfaceDataProxy::heightMap() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK26QHeightMapSurfaceDataProxy9heightMapEv(
    const QHeightMapSurfaceDataProxy *self) {
  return new QImage(self->heightMap());
}

//  void QHeightMapSurfaceDataProxy::setHeightMapFile(const QString
//      &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy16setHeightMapFileERK7QString(
    QHeightMapSurfaceDataProxy *self,
    const QString *filename) {
  self->setHeightMapFile(*filename);
}

//  QString QHeightMapSurfaceDataProxy::heightMapFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QHeightMapSurfaceDataProxy13heightMapFileEv(
    const QHeightMapSurfaceDataProxy *self) {
  return new QString(self->heightMapFile());
}

//  void QHeightMapSurfaceDataProxy::setValueRanges(float minX, float maxX,
//      float minZ, float maxZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy14setValueRangesEffff(
    QHeightMapSurfaceDataProxy *self,
    float minX,
    float maxX,
    float minZ,
    float maxZ) {
  self->setValueRanges(minX, maxX, minZ, maxZ);
}

//  void QHeightMapSurfaceDataProxy::setMinXValue(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy12setMinXValueEf(
    QHeightMapSurfaceDataProxy *self,
    float min) {
  self->setMinXValue(min);
}

//  float QHeightMapSurfaceDataProxy::minXValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QHeightMapSurfaceDataProxy9minXValueEv(
    const QHeightMapSurfaceDataProxy *self) {
  return self->minXValue();
}

//  void QHeightMapSurfaceDataProxy::setMaxXValue(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy12setMaxXValueEf(
    QHeightMapSurfaceDataProxy *self,
    float max) {
  self->setMaxXValue(max);
}

//  float QHeightMapSurfaceDataProxy::maxXValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QHeightMapSurfaceDataProxy9maxXValueEv(
    const QHeightMapSurfaceDataProxy *self) {
  return self->maxXValue();
}

//  void QHeightMapSurfaceDataProxy::setMinZValue(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy12setMinZValueEf(
    QHeightMapSurfaceDataProxy *self,
    float min) {
  self->setMinZValue(min);
}

//  float QHeightMapSurfaceDataProxy::minZValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QHeightMapSurfaceDataProxy9minZValueEv(
    const QHeightMapSurfaceDataProxy *self) {
  return self->minZValue();
}

//  void QHeightMapSurfaceDataProxy::setMaxZValue(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy12setMaxZValueEf(
    QHeightMapSurfaceDataProxy *self,
    float max) {
  self->setMaxZValue(max);
}

//  float QHeightMapSurfaceDataProxy::maxZValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QHeightMapSurfaceDataProxy9maxZValueEv(
    const QHeightMapSurfaceDataProxy *self) {
  return self->maxZValue();
}

//  void QHeightMapSurfaceDataProxy::setMinYValue(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy12setMinYValueEf(
    QHeightMapSurfaceDataProxy *self,
    float min) {
  self->setMinYValue(min);
}

//  float QHeightMapSurfaceDataProxy::minYValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QHeightMapSurfaceDataProxy9minYValueEv(
    const QHeightMapSurfaceDataProxy *self) {
  return self->minYValue();
}

//  void QHeightMapSurfaceDataProxy::setMaxYValue(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy12setMaxYValueEf(
    QHeightMapSurfaceDataProxy *self,
    float max) {
  self->setMaxYValue(max);
}

//  float QHeightMapSurfaceDataProxy::maxYValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QHeightMapSurfaceDataProxy9maxYValueEv(
    const QHeightMapSurfaceDataProxy *self) {
  return self->maxYValue();
}

//  void QHeightMapSurfaceDataProxy::setAutoScaleY(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy13setAutoScaleYEb(
    QHeightMapSurfaceDataProxy *self,
    bool enabled) {
  self->setAutoScaleY(enabled);
}

//  bool QHeightMapSurfaceDataProxy::autoScaleY() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QHeightMapSurfaceDataProxy10autoScaleYEv(
    const QHeightMapSurfaceDataProxy *self) {
  return self->autoScaleY();
}

//  void QHeightMapSurfaceDataProxy::heightMapChanged(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy16heightMapChangedERK6QImage(
    QHeightMapSurfaceDataProxy *self,
    const QImage *image) {
  self->heightMapChanged(*image);
}

//  void QHeightMapSurfaceDataProxy::heightMapFileChanged(const QString
//      &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy20heightMapFileChangedERK7QString(
    QHeightMapSurfaceDataProxy *self,
    const QString *filename) {
  self->heightMapFileChanged(*filename);
}

//  void QHeightMapSurfaceDataProxy::minXValueChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy16minXValueChangedEf(
    QHeightMapSurfaceDataProxy *self,
    float value) {
  self->minXValueChanged(value);
}

//  void QHeightMapSurfaceDataProxy::maxXValueChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy16maxXValueChangedEf(
    QHeightMapSurfaceDataProxy *self,
    float value) {
  self->maxXValueChanged(value);
}

//  void QHeightMapSurfaceDataProxy::minZValueChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy16minZValueChangedEf(
    QHeightMapSurfaceDataProxy *self,
    float value) {
  self->minZValueChanged(value);
}

//  void QHeightMapSurfaceDataProxy::maxZValueChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy16maxZValueChangedEf(
    QHeightMapSurfaceDataProxy *self,
    float value) {
  self->maxZValueChanged(value);
}

//  void QHeightMapSurfaceDataProxy::minYValueChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy16minYValueChangedEf(
    QHeightMapSurfaceDataProxy *self,
    float value) {
  self->minYValueChanged(value);
}

//  void QHeightMapSurfaceDataProxy::maxYValueChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy16maxYValueChangedEf(
    QHeightMapSurfaceDataProxy *self,
    float value) {
  self->maxYValueChanged(value);
}

//  void QHeightMapSurfaceDataProxy::autoScaleYChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHeightMapSurfaceDataProxy17autoScaleYChangedEb(
    QHeightMapSurfaceDataProxy *self,
    bool enabled) {
  self->autoScaleYChanged(enabled);
}

//  QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(QHeightMapSurfaceD
//      ataProxyPrivate *d, QObject *parent)
extern "C" Q_DECL_EXPORT
QHeightMapSurfaceDataProxy *ritual_ZN26QHeightMapSurfaceDataProxyC1EP33QHeightMapSurfaceDataProxyPrivateP7QObject(
    QHeightMapSurfaceDataProxyPrivate *d,
    QObject *parent) {
  return new CuteQHeightMapSurfaceDataProxy(d, parent);
}

//  QHeightMapSurfaceDataProxyPrivate *QHeightMapSurfaceDataProxy::dptr()
extern "C" Q_DECL_EXPORT
QHeightMapSurfaceDataProxyPrivate *ritual_ZN26QHeightMapSurfaceDataProxy4dptrEv(
    QHeightMapSurfaceDataProxy *self) {
  return self->dptr();
}

//  const QHeightMapSurfaceDataProxyPrivate
//      *QHeightMapSurfaceDataProxy::dptrc() const
extern "C" Q_DECL_EXPORT
const QHeightMapSurfaceDataProxyPrivate *ritual_ZNK26QHeightMapSurfaceDataProxy5dptrcEv(
    const QHeightMapSurfaceDataProxy *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQHeightMapSurfaceDataProxy, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHeightMapSurfaceDataProxy(
    QHeightMapSurfaceDataProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHeightMapSurfaceDataProxy *>(self)->take(key, call);
}
