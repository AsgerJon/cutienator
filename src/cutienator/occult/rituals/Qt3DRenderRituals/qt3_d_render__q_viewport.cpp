//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qviewport.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qviewport.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QViewport that Python can take functions over in. Every Qt3DRender::QViewport
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QViewportCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QViewportCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QViewportCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QViewportCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QViewportCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QViewportCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QViewportCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QViewport : public Qt3DRender::QViewport {
public:
  using Qt3DRender::QViewport::QViewport;
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
      CuteQt3DRender_QViewportCall0 call = reinterpret_cast<CuteQt3DRender_QViewportCall0>(taken[0]);
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
      CuteQt3DRender_QViewportCall1 call = reinterpret_cast<CuteQt3DRender_QViewportCall1>(taken[1]);
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
      CuteQt3DRender_QViewportCall2 call = reinterpret_cast<CuteQt3DRender_QViewportCall2>(taken[2]);
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
      CuteQt3DRender_QViewportCall3 call = reinterpret_cast<CuteQt3DRender_QViewportCall3>(taken[3]);
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
      CuteQt3DRender_QViewportCall4 call = reinterpret_cast<CuteQt3DRender_QViewportCall4>(taken[4]);
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
      CuteQt3DRender_QViewportCall5 call = reinterpret_cast<CuteQt3DRender_QViewportCall5>(taken[5]);
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
      CuteQt3DRender_QViewportCall6 call = reinterpret_cast<CuteQt3DRender_QViewportCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QViewport::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender9QViewport10metaObjectEv(
    const Qt3DRender::QViewport *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QViewport::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender9QViewport11qt_metacastEPKc(
    Qt3DRender::QViewport *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QViewport::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender9QViewport11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QViewport *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QViewport::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender9QViewport2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QViewport::tr(s, c, n));
}

//  Qt3DRender::QViewport::QViewport(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QViewport *ritual_ZN10Qt3DRender9QViewportC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QViewport(parent);
}

//  Qt3DRender::QViewport::~QViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QViewportD1Ev(Qt3DRender::QViewport *self) {
  delete self;
}

//  QRectF Qt3DRender::QViewport::normalizedRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10Qt3DRender9QViewport14normalizedRectEv(
    const Qt3DRender::QViewport *self) {
  return new QRectF(self->normalizedRect());
}

//  float Qt3DRender::QViewport::gamma() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender9QViewport5gammaEv(
    const Qt3DRender::QViewport *self) {
  return self->gamma();
}

//  void Qt3DRender::QViewport::setNormalizedRect(const QRectF
//      &normalizedRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QViewport17setNormalizedRectERK6QRectF(
    Qt3DRender::QViewport *self,
    const QRectF *normalizedRect) {
  self->setNormalizedRect(*normalizedRect);
}

//  void Qt3DRender::QViewport::setGamma(float gamma)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QViewport8setGammaEf(
    Qt3DRender::QViewport *self,
    float gamma) {
  self->setGamma(gamma);
}

//  void Qt3DRender::QViewport::normalizedRectChanged(const QRectF
//      &normalizedRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QViewport21normalizedRectChangedERK6QRectF(
    Qt3DRender::QViewport *self,
    const QRectF *normalizedRect) {
  self->normalizedRectChanged(*normalizedRect);
}

//  void Qt3DRender::QViewport::gammaChanged(float gamma)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QViewport12gammaChangedEf(
    Qt3DRender::QViewport *self,
    float gamma) {
  self->gammaChanged(gamma);
}

//  Qt3DRender::QViewport::QViewport(QViewportPrivate &dd, Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QViewport *ritual_ZN10Qt3DRender9QViewportC1ERNS_16QViewportPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QViewportPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QViewport(*dd, parent);
}

//  QViewportPrivate *Qt3DRender::QViewport::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QViewportPrivate *ritual_ZN10Qt3DRender9QViewport6d_funcEv(
    Qt3DRender::QViewport *self) {
  return self->d_func();
}

//  const QViewportPrivate *Qt3DRender::QViewport::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QViewportPrivate *ritual_ZNK10Qt3DRender9QViewport6d_funcEv(
    const Qt3DRender::QViewport *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QViewport, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QViewport(
    Qt3DRender::QViewport *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QViewport *>(self)->take(key, call);
}
