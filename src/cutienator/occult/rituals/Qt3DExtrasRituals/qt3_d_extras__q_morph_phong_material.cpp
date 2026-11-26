//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qmorphphongmaterial.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qmorphphongmaterial.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QMorphPhongMaterial that Python can take functions over in. Every Qt3DExtras::QMorphPhongMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QMorphPhongMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QMorphPhongMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMorphPhongMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMorphPhongMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMorphPhongMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMorphPhongMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMorphPhongMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QMorphPhongMaterial : public Qt3DExtras::QMorphPhongMaterial {
public:
  using Qt3DExtras::QMorphPhongMaterial::QMorphPhongMaterial;
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
      CuteQt3DExtras_QMorphPhongMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QMorphPhongMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QMorphPhongMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QMorphPhongMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QMorphPhongMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QMorphPhongMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QMorphPhongMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QMorphPhongMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QMorphPhongMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QMorphPhongMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QMorphPhongMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QMorphPhongMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QMorphPhongMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QMorphPhongMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QMorphPhongMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras19QMorphPhongMaterial10metaObjectEv(
    const Qt3DExtras::QMorphPhongMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QMorphPhongMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras19QMorphPhongMaterial11qt_metacastEPKc(
    Qt3DExtras::QMorphPhongMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QMorphPhongMaterial::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras19QMorphPhongMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QMorphPhongMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QMorphPhongMaterial::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras19QMorphPhongMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QMorphPhongMaterial::tr(s, c, n));
}

//  Qt3DExtras::QMorphPhongMaterial::QMorphPhongMaterial(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QMorphPhongMaterial *ritual_ZN10Qt3DExtras19QMorphPhongMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QMorphPhongMaterial(parent);
}

//  Qt3DExtras::QMorphPhongMaterial::~QMorphPhongMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterialD1Ev(
    Qt3DExtras::QMorphPhongMaterial *self) {
  delete self;
}

//  QColor Qt3DExtras::QMorphPhongMaterial::ambient() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras19QMorphPhongMaterial7ambientEv(
    const Qt3DExtras::QMorphPhongMaterial *self) {
  return new QColor(self->ambient());
}

//  QColor Qt3DExtras::QMorphPhongMaterial::diffuse() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras19QMorphPhongMaterial7diffuseEv(
    const Qt3DExtras::QMorphPhongMaterial *self) {
  return new QColor(self->diffuse());
}

//  QColor Qt3DExtras::QMorphPhongMaterial::specular() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras19QMorphPhongMaterial8specularEv(
    const Qt3DExtras::QMorphPhongMaterial *self) {
  return new QColor(self->specular());
}

//  float Qt3DExtras::QMorphPhongMaterial::shininess() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QMorphPhongMaterial9shininessEv(
    const Qt3DExtras::QMorphPhongMaterial *self) {
  return self->shininess();
}

//  float Qt3DExtras::QMorphPhongMaterial::interpolator() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QMorphPhongMaterial12interpolatorEv(
    const Qt3DExtras::QMorphPhongMaterial *self) {
  return self->interpolator();
}

//  void Qt3DExtras::QMorphPhongMaterial::setAmbient(const QColor &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial10setAmbientERK6QColor(
    Qt3DExtras::QMorphPhongMaterial *self,
    const QColor *ambient) {
  self->setAmbient(*ambient);
}

//  void Qt3DExtras::QMorphPhongMaterial::setDiffuse(const QColor &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial10setDiffuseERK6QColor(
    Qt3DExtras::QMorphPhongMaterial *self,
    const QColor *diffuse) {
  self->setDiffuse(*diffuse);
}

//  void Qt3DExtras::QMorphPhongMaterial::setSpecular(const QColor &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial11setSpecularERK6QColor(
    Qt3DExtras::QMorphPhongMaterial *self,
    const QColor *specular) {
  self->setSpecular(*specular);
}

//  void Qt3DExtras::QMorphPhongMaterial::setShininess(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial12setShininessEf(
    Qt3DExtras::QMorphPhongMaterial *self,
    float shininess) {
  self->setShininess(shininess);
}

//  void Qt3DExtras::QMorphPhongMaterial::setInterpolator(float interpolator)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial15setInterpolatorEf(
    Qt3DExtras::QMorphPhongMaterial *self,
    float interpolator) {
  self->setInterpolator(interpolator);
}

//  void Qt3DExtras::QMorphPhongMaterial::ambientChanged(const QColor
//      &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial14ambientChangedERK6QColor(
    Qt3DExtras::QMorphPhongMaterial *self,
    const QColor *ambient) {
  self->ambientChanged(*ambient);
}

//  void Qt3DExtras::QMorphPhongMaterial::diffuseChanged(const QColor
//      &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial14diffuseChangedERK6QColor(
    Qt3DExtras::QMorphPhongMaterial *self,
    const QColor *diffuse) {
  self->diffuseChanged(*diffuse);
}

//  void Qt3DExtras::QMorphPhongMaterial::specularChanged(const QColor
//      &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial15specularChangedERK6QColor(
    Qt3DExtras::QMorphPhongMaterial *self,
    const QColor *specular) {
  self->specularChanged(*specular);
}

//  void Qt3DExtras::QMorphPhongMaterial::shininessChanged(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial16shininessChangedEf(
    Qt3DExtras::QMorphPhongMaterial *self,
    float shininess) {
  self->shininessChanged(shininess);
}

//  void Qt3DExtras::QMorphPhongMaterial::interpolatorChanged(float
//      interpolator)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMorphPhongMaterial19interpolatorChangedEf(
    Qt3DExtras::QMorphPhongMaterial *self,
    float interpolator) {
  self->interpolatorChanged(interpolator);
}

//  QMorphPhongMaterialPrivate *Qt3DExtras::QMorphPhongMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QMorphPhongMaterialPrivate *ritual_ZN10Qt3DExtras19QMorphPhongMaterial6d_funcEv(
    Qt3DExtras::QMorphPhongMaterial *self) {
  return self->d_func();
}

//  const QMorphPhongMaterialPrivate
//      *Qt3DExtras::QMorphPhongMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QMorphPhongMaterialPrivate *ritual_ZNK10Qt3DExtras19QMorphPhongMaterial6d_funcEv(
    const Qt3DExtras::QMorphPhongMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QMorphPhongMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QMorphPhongMaterial(
    Qt3DExtras::QMorphPhongMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QMorphPhongMaterial *>(self)->take(key, call);
}
