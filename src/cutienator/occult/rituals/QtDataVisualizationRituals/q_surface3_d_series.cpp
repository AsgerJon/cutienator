//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qsurface3dseries.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qsurface3dseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSurface3DSeries that Python can take functions over in. Every QSurface3DSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurface3DSeriesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurface3DSeriesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSurface3DSeries : public QSurface3DSeries {
public:
  using QSurface3DSeries::QSurface3DSeries;
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
      CuteQSurface3DSeriesCall0 call = reinterpret_cast<CuteQSurface3DSeriesCall0>(taken[0]);
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
      CuteQSurface3DSeriesCall1 call = reinterpret_cast<CuteQSurface3DSeriesCall1>(taken[1]);
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
      CuteQSurface3DSeriesCall2 call = reinterpret_cast<CuteQSurface3DSeriesCall2>(taken[2]);
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
      CuteQSurface3DSeriesCall3 call = reinterpret_cast<CuteQSurface3DSeriesCall3>(taken[3]);
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
      CuteQSurface3DSeriesCall4 call = reinterpret_cast<CuteQSurface3DSeriesCall4>(taken[4]);
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
      CuteQSurface3DSeriesCall5 call = reinterpret_cast<CuteQSurface3DSeriesCall5>(taken[5]);
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
      CuteQSurface3DSeriesCall6 call = reinterpret_cast<CuteQSurface3DSeriesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSurface3DSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QSurface3DSeries10metaObjectEv(
    const QSurface3DSeries *self) {
  return self->metaObject();
}

//  void *QSurface3DSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QSurface3DSeries11qt_metacastEPKc(
    QSurface3DSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSurface3DSeries::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QSurface3DSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QSurface3DSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSurface3DSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QSurface3DSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSurface3DSeries::tr(s, c, n));
}

//  QSurface3DSeries::QSurface3DSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZN16QSurface3DSeriesC1EP7QObject(QObject *parent) {
  return new CuteQSurface3DSeries(parent);
}

//  QSurface3DSeries::QSurface3DSeries(QSurfaceDataProxy *dataProxy, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZN16QSurface3DSeriesC1EP17QSurfaceDataProxyP7QObject(
    QSurfaceDataProxy *dataProxy,
    QObject *parent) {
  return new CuteQSurface3DSeries(dataProxy, parent);
}

//  QSurface3DSeries::~QSurface3DSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeriesD1Ev(QSurface3DSeries *self) {
  delete self;
}

//  void QSurface3DSeries::setDataProxy(QSurfaceDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries12setDataProxyEP17QSurfaceDataProxy(
    QSurface3DSeries *self,
    QSurfaceDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  QSurfaceDataProxy *QSurface3DSeries::dataProxy() const
extern "C" Q_DECL_EXPORT
QSurfaceDataProxy *ritual_ZNK16QSurface3DSeries9dataProxyEv(
    const QSurface3DSeries *self) {
  return self->dataProxy();
}

//  void QSurface3DSeries::setSelectedPoint(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries16setSelectedPointERK6QPoint(
    QSurface3DSeries *self,
    const QPoint *position) {
  self->setSelectedPoint(*position);
}

//  QPoint QSurface3DSeries::selectedPoint() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK16QSurface3DSeries13selectedPointEv(
    const QSurface3DSeries *self) {
  return new QPoint(self->selectedPoint());
}

//  QPoint QSurface3DSeries::invalidSelectionPosition()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN16QSurface3DSeries24invalidSelectionPositionEv() {
  return new QPoint(QSurface3DSeries::invalidSelectionPosition());
}

//  void QSurface3DSeries::setFlatShadingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries21setFlatShadingEnabledEb(
    QSurface3DSeries *self,
    bool enabled) {
  self->setFlatShadingEnabled(enabled);
}

//  bool QSurface3DSeries::isFlatShadingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSurface3DSeries20isFlatShadingEnabledEv(
    const QSurface3DSeries *self) {
  return self->isFlatShadingEnabled();
}

//  void QSurface3DSeries::setDrawMode(DrawFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries11setDrawModeE6QFlagsINS_8DrawFlagEE(
    QSurface3DSeries *self,
    int mode) {
  self->setDrawMode(QFlags<QSurface3DSeries::DrawFlag>::fromInt(mode));
}

//  QSurface3DSeries::DrawFlags QSurface3DSeries::drawMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSurface3DSeries8drawModeEv(const QSurface3DSeries *self) {
  return static_cast<int>(self->drawMode().toInt());
}

//  bool QSurface3DSeries::isFlatShadingSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSurface3DSeries22isFlatShadingSupportedEv(
    const QSurface3DSeries *self) {
  return self->isFlatShadingSupported();
}

//  void QSurface3DSeries::setTexture(const QImage &texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries10setTextureERK6QImage(
    QSurface3DSeries *self,
    const QImage *texture) {
  self->setTexture(*texture);
}

//  QImage QSurface3DSeries::texture() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK16QSurface3DSeries7textureEv(
    const QSurface3DSeries *self) {
  return new QImage(self->texture());
}

//  void QSurface3DSeries::setTextureFile(const QString &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries14setTextureFileERK7QString(
    QSurface3DSeries *self,
    const QString *filename) {
  self->setTextureFile(*filename);
}

//  QString QSurface3DSeries::textureFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QSurface3DSeries11textureFileEv(
    const QSurface3DSeries *self) {
  return new QString(self->textureFile());
}

//  void QSurface3DSeries::setWireframeColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries17setWireframeColorERK6QColor(
    QSurface3DSeries *self,
    const QColor *color) {
  self->setWireframeColor(*color);
}

//  QColor QSurface3DSeries::wireframeColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QSurface3DSeries14wireframeColorEv(
    const QSurface3DSeries *self) {
  return new QColor(self->wireframeColor());
}

//  void QSurface3DSeries::dataProxyChanged(QSurfaceDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries16dataProxyChangedEP17QSurfaceDataProxy(
    QSurface3DSeries *self,
    QSurfaceDataProxy *proxy) {
  self->dataProxyChanged(proxy);
}

//  void QSurface3DSeries::selectedPointChanged(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries20selectedPointChangedERK6QPoint(
    QSurface3DSeries *self,
    const QPoint *position) {
  self->selectedPointChanged(*position);
}

//  void QSurface3DSeries::flatShadingEnabledChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries25flatShadingEnabledChangedEb(
    QSurface3DSeries *self,
    bool enable) {
  self->flatShadingEnabledChanged(enable);
}

//  void QSurface3DSeries::flatShadingSupportedChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries27flatShadingSupportedChangedEb(
    QSurface3DSeries *self,
    bool enable) {
  self->flatShadingSupportedChanged(enable);
}

//  void QSurface3DSeries::drawModeChanged(QSurface3DSeries::DrawFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries15drawModeChangedE6QFlagsINS_8DrawFlagEE(
    QSurface3DSeries *self,
    int mode) {
  self->drawModeChanged(QFlags<QSurface3DSeries::DrawFlag>::fromInt(mode));
}

//  void QSurface3DSeries::textureChanged(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries14textureChangedERK6QImage(
    QSurface3DSeries *self,
    const QImage *image) {
  self->textureChanged(*image);
}

//  void QSurface3DSeries::textureFileChanged(const QString &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries18textureFileChangedERK7QString(
    QSurface3DSeries *self,
    const QString *filename) {
  self->textureFileChanged(*filename);
}

//  void QSurface3DSeries::wireframeColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurface3DSeries21wireframeColorChangedERK6QColor(
    QSurface3DSeries *self,
    const QColor *color) {
  self->wireframeColorChanged(*color);
}

//  QSurface3DSeries::QSurface3DSeries(QSurface3DSeriesPrivate *d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZN16QSurface3DSeriesC1EP23QSurface3DSeriesPrivateP7QObject(
    QSurface3DSeriesPrivate *d,
    QObject *parent) {
  return new CuteQSurface3DSeries(d, parent);
}

//  QSurface3DSeriesPrivate *QSurface3DSeries::dptr()
extern "C" Q_DECL_EXPORT
QSurface3DSeriesPrivate *ritual_ZN16QSurface3DSeries4dptrEv(
    QSurface3DSeries *self) {
  return self->dptr();
}

//  const QSurface3DSeriesPrivate *QSurface3DSeries::dptrc() const
extern "C" Q_DECL_EXPORT
const QSurface3DSeriesPrivate *ritual_ZNK16QSurface3DSeries5dptrcEv(
    const QSurface3DSeries *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQSurface3DSeries, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSurface3DSeries(
    QSurface3DSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSurface3DSeries *>(self)->take(key, call);
}

//  QList<QSurface3DSeries *>::QList()
extern "C" Q_DECL_EXPORT
QList<QSurface3DSeries *> *ritual_list_make_QSurface3DSeries_ptr() {
  return new QList<QSurface3DSeries *>();
}

//  void QList<QSurface3DSeries *>::append(const QSurface3DSeries * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSurface3DSeries_ptr(
    QList<QSurface3DSeries *> *self,
    QSurface3DSeries *element) {
  self->append(element);
}

//  qsizetype QList<QSurface3DSeries *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSurface3DSeries_ptr(
    const QList<QSurface3DSeries *> *self) {
  return self->size();
}

//  const QSurface3DSeries * &QList<QSurface3DSeries *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_list_at_QSurface3DSeries_ptr(
    const QList<QSurface3DSeries *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QSurface3DSeries *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSurface3DSeries_ptr(QList<QSurface3DSeries *> *self) {
  delete self;
}
