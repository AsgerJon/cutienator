//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qspotlight.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qspotlight.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QSpotLight that Python can take functions over in. Every Qt3DRender::QSpotLight
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QSpotLightCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QSpotLightCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSpotLightCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSpotLightCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSpotLightCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSpotLightCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSpotLightCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QSpotLight : public Qt3DRender::QSpotLight {
public:
  using Qt3DRender::QSpotLight::QSpotLight;
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
      CuteQt3DRender_QSpotLightCall0 call = reinterpret_cast<CuteQt3DRender_QSpotLightCall0>(taken[0]);
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
      CuteQt3DRender_QSpotLightCall1 call = reinterpret_cast<CuteQt3DRender_QSpotLightCall1>(taken[1]);
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
      CuteQt3DRender_QSpotLightCall2 call = reinterpret_cast<CuteQt3DRender_QSpotLightCall2>(taken[2]);
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
      CuteQt3DRender_QSpotLightCall3 call = reinterpret_cast<CuteQt3DRender_QSpotLightCall3>(taken[3]);
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
      CuteQt3DRender_QSpotLightCall4 call = reinterpret_cast<CuteQt3DRender_QSpotLightCall4>(taken[4]);
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
      CuteQt3DRender_QSpotLightCall5 call = reinterpret_cast<CuteQt3DRender_QSpotLightCall5>(taken[5]);
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
      CuteQt3DRender_QSpotLightCall6 call = reinterpret_cast<CuteQt3DRender_QSpotLightCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QSpotLight::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QSpotLight10metaObjectEv(
    const Qt3DRender::QSpotLight *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QSpotLight::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QSpotLight11qt_metacastEPKc(
    Qt3DRender::QSpotLight *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QSpotLight::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QSpotLight11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QSpotLight *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QSpotLight::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QSpotLight2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QSpotLight::tr(s, c, n));
}

//  Qt3DRender::QSpotLight::QSpotLight(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QSpotLight *ritual_ZN10Qt3DRender10QSpotLightC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QSpotLight(parent);
}

//  Qt3DRender::QSpotLight::~QSpotLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLightD1Ev(Qt3DRender::QSpotLight *self) {
  delete self;
}

//  QVector3D Qt3DRender::QSpotLight::localDirection() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10QSpotLight14localDirectionEv(
    const Qt3DRender::QSpotLight *self) {
  return new QVector3D(self->localDirection());
}

//  float Qt3DRender::QSpotLight::cutOffAngle() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10QSpotLight11cutOffAngleEv(
    const Qt3DRender::QSpotLight *self) {
  return self->cutOffAngle();
}

//  float Qt3DRender::QSpotLight::constantAttenuation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10QSpotLight19constantAttenuationEv(
    const Qt3DRender::QSpotLight *self) {
  return self->constantAttenuation();
}

//  float Qt3DRender::QSpotLight::linearAttenuation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10QSpotLight17linearAttenuationEv(
    const Qt3DRender::QSpotLight *self) {
  return self->linearAttenuation();
}

//  float Qt3DRender::QSpotLight::quadraticAttenuation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10QSpotLight20quadraticAttenuationEv(
    const Qt3DRender::QSpotLight *self) {
  return self->quadraticAttenuation();
}

//  void Qt3DRender::QSpotLight::setConstantAttenuation(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight22setConstantAttenuationEf(
    Qt3DRender::QSpotLight *self,
    float value) {
  self->setConstantAttenuation(value);
}

//  void Qt3DRender::QSpotLight::setLinearAttenuation(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight20setLinearAttenuationEf(
    Qt3DRender::QSpotLight *self,
    float value) {
  self->setLinearAttenuation(value);
}

//  void Qt3DRender::QSpotLight::setQuadraticAttenuation(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight23setQuadraticAttenuationEf(
    Qt3DRender::QSpotLight *self,
    float value) {
  self->setQuadraticAttenuation(value);
}

//  void Qt3DRender::QSpotLight::setLocalDirection(const QVector3D
//      &localDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight17setLocalDirectionERK9QVector3D(
    Qt3DRender::QSpotLight *self,
    const QVector3D *localDirection) {
  self->setLocalDirection(*localDirection);
}

//  void Qt3DRender::QSpotLight::setCutOffAngle(float cutOffAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight14setCutOffAngleEf(
    Qt3DRender::QSpotLight *self,
    float cutOffAngle) {
  self->setCutOffAngle(cutOffAngle);
}

//  void Qt3DRender::QSpotLight::constantAttenuationChanged(float
//      constantAttenuation)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight26constantAttenuationChangedEf(
    Qt3DRender::QSpotLight *self,
    float constantAttenuation) {
  self->constantAttenuationChanged(constantAttenuation);
}

//  void Qt3DRender::QSpotLight::linearAttenuationChanged(float
//      linearAttenuation)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight24linearAttenuationChangedEf(
    Qt3DRender::QSpotLight *self,
    float linearAttenuation) {
  self->linearAttenuationChanged(linearAttenuation);
}

//  void Qt3DRender::QSpotLight::quadraticAttenuationChanged(float
//      quadraticAttenuation)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight27quadraticAttenuationChangedEf(
    Qt3DRender::QSpotLight *self,
    float quadraticAttenuation) {
  self->quadraticAttenuationChanged(quadraticAttenuation);
}

//  void Qt3DRender::QSpotLight::localDirectionChanged(const QVector3D
//      &localDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight21localDirectionChangedERK9QVector3D(
    Qt3DRender::QSpotLight *self,
    const QVector3D *localDirection) {
  self->localDirectionChanged(*localDirection);
}

//  void Qt3DRender::QSpotLight::cutOffAngleChanged(float cutOffAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QSpotLight18cutOffAngleChangedEf(
    Qt3DRender::QSpotLight *self,
    float cutOffAngle) {
  self->cutOffAngleChanged(cutOffAngle);
}

//  Qt3DRender::QSpotLight::QSpotLight(QSpotLightPrivate &dd, Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QSpotLight *ritual_ZN10Qt3DRender10QSpotLightC1ERNS_17QSpotLightPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QSpotLightPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QSpotLight(*dd, parent);
}

//  QSpotLightPrivate *Qt3DRender::QSpotLight::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QSpotLightPrivate *ritual_ZN10Qt3DRender10QSpotLight6d_funcEv(
    Qt3DRender::QSpotLight *self) {
  return self->d_func();
}

//  const QSpotLightPrivate *Qt3DRender::QSpotLight::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QSpotLightPrivate *ritual_ZNK10Qt3DRender10QSpotLight6d_funcEv(
    const Qt3DRender::QSpotLight *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QSpotLight, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QSpotLight(
    Qt3DRender::QSpotLight *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QSpotLight *>(self)->take(key, call);
}
