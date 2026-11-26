//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrastermode.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrastermode.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QRasterMode that Python can take functions over in. Every Qt3DRender::QRasterMode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRasterModeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRasterModeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRasterModeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRasterModeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRasterModeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRasterModeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRasterModeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRasterMode : public Qt3DRender::QRasterMode {
public:
  using Qt3DRender::QRasterMode::QRasterMode;
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
      CuteQt3DRender_QRasterModeCall0 call = reinterpret_cast<CuteQt3DRender_QRasterModeCall0>(taken[0]);
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
      CuteQt3DRender_QRasterModeCall1 call = reinterpret_cast<CuteQt3DRender_QRasterModeCall1>(taken[1]);
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
      CuteQt3DRender_QRasterModeCall2 call = reinterpret_cast<CuteQt3DRender_QRasterModeCall2>(taken[2]);
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
      CuteQt3DRender_QRasterModeCall3 call = reinterpret_cast<CuteQt3DRender_QRasterModeCall3>(taken[3]);
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
      CuteQt3DRender_QRasterModeCall4 call = reinterpret_cast<CuteQt3DRender_QRasterModeCall4>(taken[4]);
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
      CuteQt3DRender_QRasterModeCall5 call = reinterpret_cast<CuteQt3DRender_QRasterModeCall5>(taken[5]);
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
      CuteQt3DRender_QRasterModeCall6 call = reinterpret_cast<CuteQt3DRender_QRasterModeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRasterMode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender11QRasterMode10metaObjectEv(
    const Qt3DRender::QRasterMode *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRasterMode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender11QRasterMode11qt_metacastEPKc(
    Qt3DRender::QRasterMode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRasterMode::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender11QRasterMode11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRasterMode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QRasterMode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender11QRasterMode2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRasterMode::tr(s, c, n));
}

//  Qt3DRender::QRasterMode::QRasterMode(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRasterMode *ritual_ZN10Qt3DRender11QRasterModeC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRasterMode(parent);
}

//  Qt3DRender::QRasterMode::~QRasterMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRasterModeD1Ev(Qt3DRender::QRasterMode *self) {
  delete self;
}

//  RasterMode Qt3DRender::QRasterMode::rasterMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRasterMode::RasterMode ritual_ZNK10Qt3DRender11QRasterMode10rasterModeEv(
    const Qt3DRender::QRasterMode *self) {
  return self->rasterMode();
}

//  FaceMode Qt3DRender::QRasterMode::faceMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRasterMode::FaceMode ritual_ZNK10Qt3DRender11QRasterMode8faceModeEv(
    const Qt3DRender::QRasterMode *self) {
  return self->faceMode();
}

//  void Qt3DRender::QRasterMode::setRasterMode(RasterMode rasterMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRasterMode13setRasterModeENS0_10RasterModeE(
    Qt3DRender::QRasterMode *self,
    Qt3DRender::QRasterMode::RasterMode rasterMode) {
  self->setRasterMode(rasterMode);
}

//  void Qt3DRender::QRasterMode::setFaceMode(FaceMode faceMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRasterMode11setFaceModeENS0_8FaceModeE(
    Qt3DRender::QRasterMode *self,
    Qt3DRender::QRasterMode::FaceMode faceMode) {
  self->setFaceMode(faceMode);
}

//  void Qt3DRender::QRasterMode::rasterModeChanged(RasterMode rasterMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRasterMode17rasterModeChangedENS0_10RasterModeE(
    Qt3DRender::QRasterMode *self,
    Qt3DRender::QRasterMode::RasterMode rasterMode) {
  self->rasterModeChanged(rasterMode);
}

//  void Qt3DRender::QRasterMode::faceModeChanged(FaceMode faceMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRasterMode15faceModeChangedENS0_8FaceModeE(
    Qt3DRender::QRasterMode *self,
    Qt3DRender::QRasterMode::FaceMode faceMode) {
  self->faceModeChanged(faceMode);
}

//  QRasterModePrivate *Qt3DRender::QRasterMode::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRasterModePrivate *ritual_ZN10Qt3DRender11QRasterMode6d_funcEv(
    Qt3DRender::QRasterMode *self) {
  return self->d_func();
}

//  const QRasterModePrivate *Qt3DRender::QRasterMode::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRasterModePrivate *ritual_ZNK10Qt3DRender11QRasterMode6d_funcEv(
    const Qt3DRender::QRasterMode *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QRasterMode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRasterMode(
    Qt3DRender::QRasterMode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRasterMode *>(self)->take(key, call);
}
