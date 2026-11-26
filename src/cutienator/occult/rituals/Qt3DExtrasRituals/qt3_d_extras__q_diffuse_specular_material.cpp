//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qdiffusespecularmaterial.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DExtras/qdiffusespecularmaterial.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QDiffuseSpecularMaterial that Python can take functions over in. Every Qt3DExtras::QDiffuseSpecularMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QDiffuseSpecularMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QDiffuseSpecularMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QDiffuseSpecularMaterial : public Qt3DExtras::QDiffuseSpecularMaterial {
public:
  using Qt3DExtras::QDiffuseSpecularMaterial::QDiffuseSpecularMaterial;
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
      CuteQt3DExtras_QDiffuseSpecularMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QDiffuseSpecularMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QDiffuseSpecularMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QDiffuseSpecularMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QDiffuseSpecularMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QDiffuseSpecularMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QDiffuseSpecularMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QDiffuseSpecularMaterial::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial10metaObjectEv(
    const Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QDiffuseSpecularMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial11qt_metacastEPKc(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QDiffuseSpecularMaterial::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QDiffuseSpecularMaterial::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QDiffuseSpecularMaterial::tr(s, c, n));
}

//  Qt3DExtras::QDiffuseSpecularMaterial::QDiffuseSpecularMaterial(Qt3DCore::
//      QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseSpecularMaterial *ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QDiffuseSpecularMaterial(parent);
}

//  Qt3DExtras::QDiffuseSpecularMaterial::~QDiffuseSpecularMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterialD1Ev(
    Qt3DExtras::QDiffuseSpecularMaterial *self) {
  delete self;
}

//  QColor Qt3DExtras::QDiffuseSpecularMaterial::ambient() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial7ambientEv(
    const Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return new QColor(self->ambient());
}

//  QVariant Qt3DExtras::QDiffuseSpecularMaterial::diffuse() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial7diffuseEv(
    const Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return new QVariant(self->diffuse());
}

//  QVariant Qt3DExtras::QDiffuseSpecularMaterial::specular() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial8specularEv(
    const Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return new QVariant(self->specular());
}

//  float Qt3DExtras::QDiffuseSpecularMaterial::shininess() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial9shininessEv(
    const Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return self->shininess();
}

//  QVariant Qt3DExtras::QDiffuseSpecularMaterial::normal() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial6normalEv(
    const Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return new QVariant(self->normal());
}

//  float Qt3DExtras::QDiffuseSpecularMaterial::textureScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial12textureScaleEv(
    const Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return self->textureScale();
}

//  bool Qt3DExtras::QDiffuseSpecularMaterial::isAlphaBlendingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial22isAlphaBlendingEnabledEv(
    const Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return self->isAlphaBlendingEnabled();
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::setAmbient(const QColor
//      &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial10setAmbientERK6QColor(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const QColor *ambient) {
  self->setAmbient(*ambient);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::setDiffuse(const QVariant
//      &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial10setDiffuseERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const QVariant *diffuse) {
  self->setDiffuse(*diffuse);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::setSpecular(const QVariant
//      &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial11setSpecularERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const QVariant *specular) {
  self->setSpecular(*specular);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::setShininess(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial12setShininessEf(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    float shininess) {
  self->setShininess(shininess);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::setNormal(const QVariant
//      &normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial9setNormalERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const QVariant *normal) {
  self->setNormal(*normal);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::setTextureScale(float
//      textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial15setTextureScaleEf(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    float textureScale) {
  self->setTextureScale(textureScale);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::setAlphaBlendingEnabled(bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial23setAlphaBlendingEnabledEb(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    bool enabled) {
  self->setAlphaBlendingEnabled(enabled);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::ambientChanged(const QColor
//      &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial14ambientChangedERK6QColor(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const QColor *ambient) {
  self->ambientChanged(*ambient);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::diffuseChanged(const QVariant
//      &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial14diffuseChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const QVariant *diffuse) {
  self->diffuseChanged(*diffuse);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::specularChanged(const QVariant
//      &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial15specularChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const QVariant *specular) {
  self->specularChanged(*specular);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::shininessChanged(float
//      shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial16shininessChangedEf(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    float shininess) {
  self->shininessChanged(shininess);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::normalChanged(const QVariant
//      &normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial13normalChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const QVariant *normal) {
  self->normalChanged(*normal);
}

//  void Qt3DExtras::QDiffuseSpecularMaterial::textureScaleChanged(float
//      textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial19textureScaleChangedEf(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    float textureScale) {
  self->textureScaleChanged(textureScale);
}

//  void
//      Qt3DExtras::QDiffuseSpecularMaterial::alphaBlendingEnabledChanged(boo
//      l enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial27alphaBlendingEnabledChangedEb(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    bool enabled) {
  self->alphaBlendingEnabledChanged(enabled);
}

//  QDiffuseSpecularMaterialPrivate
//      *Qt3DExtras::QDiffuseSpecularMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseSpecularMaterialPrivate *ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial6d_funcEv(
    Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return self->d_func();
}

//  const QDiffuseSpecularMaterialPrivate
//      *Qt3DExtras::QDiffuseSpecularMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QDiffuseSpecularMaterialPrivate *ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial6d_funcEv(
    const Qt3DExtras::QDiffuseSpecularMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QDiffuseSpecularMaterial, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QDiffuseSpecularMaterial(
    Qt3DExtras::QDiffuseSpecularMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QDiffuseSpecularMaterial *>(self)->take(key, call);
}
