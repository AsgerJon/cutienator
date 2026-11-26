//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qenvironmentlight.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qenvironmentlight.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QEnvironmentLight that Python can take functions over in. Every Qt3DRender::QEnvironmentLight
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QEnvironmentLightCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QEnvironmentLightCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEnvironmentLightCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEnvironmentLightCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEnvironmentLightCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEnvironmentLightCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEnvironmentLightCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QEnvironmentLight : public Qt3DRender::QEnvironmentLight {
public:
  using Qt3DRender::QEnvironmentLight::QEnvironmentLight;
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
      CuteQt3DRender_QEnvironmentLightCall0 call = reinterpret_cast<CuteQt3DRender_QEnvironmentLightCall0>(taken[0]);
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
      CuteQt3DRender_QEnvironmentLightCall1 call = reinterpret_cast<CuteQt3DRender_QEnvironmentLightCall1>(taken[1]);
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
      CuteQt3DRender_QEnvironmentLightCall2 call = reinterpret_cast<CuteQt3DRender_QEnvironmentLightCall2>(taken[2]);
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
      CuteQt3DRender_QEnvironmentLightCall3 call = reinterpret_cast<CuteQt3DRender_QEnvironmentLightCall3>(taken[3]);
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
      CuteQt3DRender_QEnvironmentLightCall4 call = reinterpret_cast<CuteQt3DRender_QEnvironmentLightCall4>(taken[4]);
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
      CuteQt3DRender_QEnvironmentLightCall5 call = reinterpret_cast<CuteQt3DRender_QEnvironmentLightCall5>(taken[5]);
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
      CuteQt3DRender_QEnvironmentLightCall6 call = reinterpret_cast<CuteQt3DRender_QEnvironmentLightCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QEnvironmentLight::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender17QEnvironmentLight10metaObjectEv(
    const Qt3DRender::QEnvironmentLight *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QEnvironmentLight::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender17QEnvironmentLight11qt_metacastEPKc(
    Qt3DRender::QEnvironmentLight *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QEnvironmentLight::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender17QEnvironmentLight11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QEnvironmentLight *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QEnvironmentLight::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender17QEnvironmentLight2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QEnvironmentLight::tr(s, c, n));
}

//  Qt3DRender::QEnvironmentLight::QEnvironmentLight(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QEnvironmentLight *ritual_ZN10Qt3DRender17QEnvironmentLightC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QEnvironmentLight(parent);
}

//  Qt3DRender::QEnvironmentLight::~QEnvironmentLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QEnvironmentLightD1Ev(
    Qt3DRender::QEnvironmentLight *self) {
  delete self;
}

//  Qt3DRender::QAbstractTexture *Qt3DRender::QEnvironmentLight::irradiance()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DRender17QEnvironmentLight10irradianceEv(
    const Qt3DRender::QEnvironmentLight *self) {
  return self->irradiance();
}

//  Qt3DRender::QAbstractTexture *Qt3DRender::QEnvironmentLight::specular()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DRender17QEnvironmentLight8specularEv(
    const Qt3DRender::QEnvironmentLight *self) {
  return self->specular();
}

//  void
//      Qt3DRender::QEnvironmentLight::setIrradiance(Qt3DRender::QAbstractTex
//      ture *irradiance)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QEnvironmentLight13setIrradianceEPNS_16QAbstractTextureE(
    Qt3DRender::QEnvironmentLight *self,
    Qt3DRender::QAbstractTexture *irradiance) {
  self->setIrradiance(irradiance);
}

//  void
//      Qt3DRender::QEnvironmentLight::setSpecular(Qt3DRender::QAbstractTextu
//      re *specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QEnvironmentLight11setSpecularEPNS_16QAbstractTextureE(
    Qt3DRender::QEnvironmentLight *self,
    Qt3DRender::QAbstractTexture *specular) {
  self->setSpecular(specular);
}

//  Qt3DRender::QEnvironmentLight::QEnvironmentLight(QEnvironmentLightPrivate
//      &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QEnvironmentLight *ritual_ZN10Qt3DRender17QEnvironmentLightC1ERNS_24QEnvironmentLightPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QEnvironmentLightPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QEnvironmentLight(*dd, parent);
}

//  void Qt3DRender::QEnvironmentLight::irradianceChanged(Qt3DRender::QAbstra
//      ctTexture *environmentIrradiance)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QEnvironmentLight17irradianceChangedEPNS_16QAbstractTextureE(
    Qt3DRender::QEnvironmentLight *self,
    Qt3DRender::QAbstractTexture *environmentIrradiance) {
  self->irradianceChanged(environmentIrradiance);
}

//  void Qt3DRender::QEnvironmentLight::specularChanged(Qt3DRender::QAbstract
//      Texture *environmentSpecular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QEnvironmentLight15specularChangedEPNS_16QAbstractTextureE(
    Qt3DRender::QEnvironmentLight *self,
    Qt3DRender::QAbstractTexture *environmentSpecular) {
  self->specularChanged(environmentSpecular);
}

//  QEnvironmentLightPrivate *Qt3DRender::QEnvironmentLight::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QEnvironmentLightPrivate *ritual_ZN10Qt3DRender17QEnvironmentLight6d_funcEv(
    Qt3DRender::QEnvironmentLight *self) {
  return self->d_func();
}

//  const QEnvironmentLightPrivate *Qt3DRender::QEnvironmentLight::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QEnvironmentLightPrivate *ritual_ZNK10Qt3DRender17QEnvironmentLight6d_funcEv(
    const Qt3DRender::QEnvironmentLight *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QEnvironmentLight, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QEnvironmentLight(
    Qt3DRender::QEnvironmentLight *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QEnvironmentLight *>(self)->take(key, call);
}
