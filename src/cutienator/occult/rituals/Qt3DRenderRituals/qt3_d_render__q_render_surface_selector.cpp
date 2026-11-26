//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendersurfaceselector.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DRender/qrendersurfaceselector.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QRenderSurfaceSelector that Python can take functions over in. Every Qt3DRender::QRenderSurfaceSelector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderSurfaceSelectorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderSurfaceSelectorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSurfaceSelectorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSurfaceSelectorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSurfaceSelectorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSurfaceSelectorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSurfaceSelectorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRenderSurfaceSelector : public Qt3DRender::QRenderSurfaceSelector {
public:
  using Qt3DRender::QRenderSurfaceSelector::QRenderSurfaceSelector;
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
      CuteQt3DRender_QRenderSurfaceSelectorCall0 call = reinterpret_cast<CuteQt3DRender_QRenderSurfaceSelectorCall0>(taken[0]);
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
      CuteQt3DRender_QRenderSurfaceSelectorCall1 call = reinterpret_cast<CuteQt3DRender_QRenderSurfaceSelectorCall1>(taken[1]);
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
      CuteQt3DRender_QRenderSurfaceSelectorCall2 call = reinterpret_cast<CuteQt3DRender_QRenderSurfaceSelectorCall2>(taken[2]);
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
      CuteQt3DRender_QRenderSurfaceSelectorCall3 call = reinterpret_cast<CuteQt3DRender_QRenderSurfaceSelectorCall3>(taken[3]);
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
      CuteQt3DRender_QRenderSurfaceSelectorCall4 call = reinterpret_cast<CuteQt3DRender_QRenderSurfaceSelectorCall4>(taken[4]);
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
      CuteQt3DRender_QRenderSurfaceSelectorCall5 call = reinterpret_cast<CuteQt3DRender_QRenderSurfaceSelectorCall5>(taken[5]);
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
      CuteQt3DRender_QRenderSurfaceSelectorCall6 call = reinterpret_cast<CuteQt3DRender_QRenderSurfaceSelectorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRenderSurfaceSelector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender22QRenderSurfaceSelector10metaObjectEv(
    const Qt3DRender::QRenderSurfaceSelector *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRenderSurfaceSelector::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender22QRenderSurfaceSelector11qt_metacastEPKc(
    Qt3DRender::QRenderSurfaceSelector *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRenderSurfaceSelector::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender22QRenderSurfaceSelector11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRenderSurfaceSelector *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QRenderSurfaceSelector::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender22QRenderSurfaceSelector2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderSurfaceSelector::tr(s, c, n));
}

//  Qt3DRender::QRenderSurfaceSelector::QRenderSurfaceSelector(Qt3DCore::QNod
//      e *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSurfaceSelector *ritual_ZN10Qt3DRender22QRenderSurfaceSelectorC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderSurfaceSelector(parent);
}

//  Qt3DRender::QRenderSurfaceSelector::~QRenderSurfaceSelector()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSurfaceSelectorD1Ev(
    Qt3DRender::QRenderSurfaceSelector *self) {
  delete self;
}

//  QObject *Qt3DRender::QRenderSurfaceSelector::surface() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK10Qt3DRender22QRenderSurfaceSelector7surfaceEv(
    const Qt3DRender::QRenderSurfaceSelector *self) {
  return self->surface();
}

//  QSize Qt3DRender::QRenderSurfaceSelector::externalRenderTargetSize()
//      const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DRender22QRenderSurfaceSelector24externalRenderTargetSizeEv(
    const Qt3DRender::QRenderSurfaceSelector *self) {
  return new QSize(self->externalRenderTargetSize());
}

//  float Qt3DRender::QRenderSurfaceSelector::surfacePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender22QRenderSurfaceSelector17surfacePixelRatioEv(
    const Qt3DRender::QRenderSurfaceSelector *self) {
  return self->surfacePixelRatio();
}

//  void Qt3DRender::QRenderSurfaceSelector::setSurface(QObject
//      *surfaceObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSurfaceSelector10setSurfaceEP7QObject(
    Qt3DRender::QRenderSurfaceSelector *self,
    QObject *surfaceObject) {
  self->setSurface(surfaceObject);
}

//  void Qt3DRender::QRenderSurfaceSelector::setSurfacePixelRatio(float
//      ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSurfaceSelector20setSurfacePixelRatioEf(
    Qt3DRender::QRenderSurfaceSelector *self,
    float ratio) {
  self->setSurfacePixelRatio(ratio);
}

//  void
//      Qt3DRender::QRenderSurfaceSelector::setExternalRenderTargetSize(const
//      QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSurfaceSelector27setExternalRenderTargetSizeERK5QSize(
    Qt3DRender::QRenderSurfaceSelector *self,
    const QSize *size) {
  self->setExternalRenderTargetSize(*size);
}

//  void Qt3DRender::QRenderSurfaceSelector::surfaceChanged(QObject *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSurfaceSelector14surfaceChangedEP7QObject(
    Qt3DRender::QRenderSurfaceSelector *self,
    QObject *surface) {
  self->surfaceChanged(surface);
}

//  void
//      Qt3DRender::QRenderSurfaceSelector::externalRenderTargetSizeChanged(c
//      onst QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSurfaceSelector31externalRenderTargetSizeChangedERK5QSize(
    Qt3DRender::QRenderSurfaceSelector *self,
    const QSize *size) {
  self->externalRenderTargetSizeChanged(*size);
}

//  void Qt3DRender::QRenderSurfaceSelector::surfacePixelRatioChanged(float
//      ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSurfaceSelector24surfacePixelRatioChangedEf(
    Qt3DRender::QRenderSurfaceSelector *self,
    float ratio) {
  self->surfacePixelRatioChanged(ratio);
}

//  QRenderSurfaceSelectorPrivate
//      *Qt3DRender::QRenderSurfaceSelector::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSurfaceSelectorPrivate *ritual_ZN10Qt3DRender22QRenderSurfaceSelector6d_funcEv(
    Qt3DRender::QRenderSurfaceSelector *self) {
  return self->d_func();
}

//  const QRenderSurfaceSelectorPrivate
//      *Qt3DRender::QRenderSurfaceSelector::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderSurfaceSelectorPrivate *ritual_ZNK10Qt3DRender22QRenderSurfaceSelector6d_funcEv(
    const Qt3DRender::QRenderSurfaceSelector *self) {
  return self->d_func();
}

//  Qt3DRender::QRenderSurfaceSelector::QRenderSurfaceSelector(QRenderSurface
//      SelectorPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSurfaceSelector *ritual_ZN10Qt3DRender22QRenderSurfaceSelectorC1ERNS_29QRenderSurfaceSelectorPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QRenderSurfaceSelectorPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderSurfaceSelector(*dd, parent);
}

//  a Python function taken by a CuteQt3DRender_QRenderSurfaceSelector, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderSurfaceSelector(
    Qt3DRender::QRenderSurfaceSelector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderSurfaceSelector *>(self)->take(key, call);
}
