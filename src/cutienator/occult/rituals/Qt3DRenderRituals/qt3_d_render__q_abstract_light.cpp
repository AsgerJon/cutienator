//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qabstractlight.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qabstractlight.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QAbstractLight that Python can take functions over in. Every Qt3DRender::QAbstractLight
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAbstractLightCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAbstractLightCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractLightCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractLightCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractLightCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractLightCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractLightCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QAbstractLight : public Qt3DRender::QAbstractLight {
public:
  using Qt3DRender::QAbstractLight::QAbstractLight;
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
      CuteQt3DRender_QAbstractLightCall0 call = reinterpret_cast<CuteQt3DRender_QAbstractLightCall0>(taken[0]);
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
      CuteQt3DRender_QAbstractLightCall1 call = reinterpret_cast<CuteQt3DRender_QAbstractLightCall1>(taken[1]);
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
      CuteQt3DRender_QAbstractLightCall2 call = reinterpret_cast<CuteQt3DRender_QAbstractLightCall2>(taken[2]);
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
      CuteQt3DRender_QAbstractLightCall3 call = reinterpret_cast<CuteQt3DRender_QAbstractLightCall3>(taken[3]);
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
      CuteQt3DRender_QAbstractLightCall4 call = reinterpret_cast<CuteQt3DRender_QAbstractLightCall4>(taken[4]);
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
      CuteQt3DRender_QAbstractLightCall5 call = reinterpret_cast<CuteQt3DRender_QAbstractLightCall5>(taken[5]);
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
      CuteQt3DRender_QAbstractLightCall6 call = reinterpret_cast<CuteQt3DRender_QAbstractLightCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QAbstractLight::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender14QAbstractLight10metaObjectEv(
    const Qt3DRender::QAbstractLight *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QAbstractLight::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender14QAbstractLight11qt_metacastEPKc(
    Qt3DRender::QAbstractLight *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QAbstractLight::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender14QAbstractLight11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QAbstractLight *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QAbstractLight::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender14QAbstractLight2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QAbstractLight::tr(s, c, n));
}

//  Qt3DRender::QAbstractLight::~QAbstractLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QAbstractLightD1Ev(
    Qt3DRender::QAbstractLight *self) {
  delete self;
}

//  Type Qt3DRender::QAbstractLight::type() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractLight::Type ritual_ZNK10Qt3DRender14QAbstractLight4typeEv(
    const Qt3DRender::QAbstractLight *self) {
  return self->type();
}

//  QColor Qt3DRender::QAbstractLight::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DRender14QAbstractLight5colorEv(
    const Qt3DRender::QAbstractLight *self) {
  return new QColor(self->color());
}

//  float Qt3DRender::QAbstractLight::intensity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender14QAbstractLight9intensityEv(
    const Qt3DRender::QAbstractLight *self) {
  return self->intensity();
}

//  void Qt3DRender::QAbstractLight::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QAbstractLight8setColorERK6QColor(
    Qt3DRender::QAbstractLight *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void Qt3DRender::QAbstractLight::setIntensity(float intensity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QAbstractLight12setIntensityEf(
    Qt3DRender::QAbstractLight *self,
    float intensity) {
  self->setIntensity(intensity);
}

//  Qt3DRender::QAbstractLight::QAbstractLight(QAbstractLightPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractLight *ritual_ZN10Qt3DRender14QAbstractLightC1ERNS_21QAbstractLightPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QAbstractLightPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QAbstractLight(*dd, parent);
}

//  void Qt3DRender::QAbstractLight::colorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QAbstractLight12colorChangedERK6QColor(
    Qt3DRender::QAbstractLight *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void Qt3DRender::QAbstractLight::intensityChanged(float intensity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QAbstractLight16intensityChangedEf(
    Qt3DRender::QAbstractLight *self,
    float intensity) {
  self->intensityChanged(intensity);
}

//  QAbstractLightPrivate *Qt3DRender::QAbstractLight::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractLightPrivate *ritual_ZN10Qt3DRender14QAbstractLight6d_funcEv(
    Qt3DRender::QAbstractLight *self) {
  return self->d_func();
}

//  const QAbstractLightPrivate *Qt3DRender::QAbstractLight::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QAbstractLightPrivate *ritual_ZNK10Qt3DRender14QAbstractLight6d_funcEv(
    const Qt3DRender::QAbstractLight *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QAbstractLight, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QAbstractLight(
    Qt3DRender::QAbstractLight *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QAbstractLight *>(self)->take(key, call);
}
