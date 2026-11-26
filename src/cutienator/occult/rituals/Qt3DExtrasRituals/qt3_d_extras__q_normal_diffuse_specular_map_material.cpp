//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qnormaldiffusespecularmapmaterial.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DExtras/qnormaldiffusespecularmapmaterial.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QNormalDiffuseSpecularMapMaterial that Python can take functions over in. Every Qt3DExtras::QNormalDiffuseSpecularMapMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QNormalDiffuseSpecularMapMaterial : public Qt3DExtras::QNormalDiffuseSpecularMapMaterial {
public:
  using Qt3DExtras::QNormalDiffuseSpecularMapMaterial::QNormalDiffuseSpecularMapMaterial;
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
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial10metaObjectEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial11qt_metacastEPKc(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QNormalDiffuseSpecularMapMaterial::qt_metacall(QMetaObjec
//      t::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QNormalDiffuseSpecularMapMaterial::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DExtras::QNormalDiffuseSpecularMapMaterial::tr(
          s,
          c,
          n));
}

//  Qt3DExtras::QNormalDiffuseSpecularMapMaterial::QNormalDiffuseSpecularMapM
//      aterial(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseSpecularMapMaterial *ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QNormalDiffuseSpecularMapMaterial(parent);
}

//  Qt3DExtras::QNormalDiffuseSpecularMapMaterial::~QNormalDiffuseSpecularMap
//      Material()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterialD1Ev(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  delete self;
}

//  QColor Qt3DExtras::QNormalDiffuseSpecularMapMaterial::ambient() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial7ambientEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  return new QColor(self->ambient());
}

//  Qt3DRender::QAbstractTexture
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::diffuse() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial7diffuseEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  return self->diffuse();
}

//  Qt3DRender::QAbstractTexture
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::normal() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial6normalEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  return self->normal();
}

//  Qt3DRender::QAbstractTexture
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::specular() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial8specularEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  return self->specular();
}

//  float Qt3DExtras::QNormalDiffuseSpecularMapMaterial::shininess() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial9shininessEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  return self->shininess();
}

//  float Qt3DExtras::QNormalDiffuseSpecularMapMaterial::textureScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial12textureScaleEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  return self->textureScale();
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setAmbient(const
//      QColor &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial10setAmbientERK6QColor(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    const QColor *ambient) {
  self->setAmbient(*ambient);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setDiffuse(Qt3DRender
//      ::QAbstractTexture *diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial10setDiffuseEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    Qt3DRender::QAbstractTexture *diffuse) {
  self->setDiffuse(diffuse);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setNormal(Qt3DRender:
//      :QAbstractTexture *normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial9setNormalEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    Qt3DRender::QAbstractTexture *normal) {
  self->setNormal(normal);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setSpecular(Qt3DRende
//      r::QAbstractTexture *specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial11setSpecularEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    Qt3DRender::QAbstractTexture *specular) {
  self->setSpecular(specular);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setShininess(float
//      shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial12setShininessEf(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    float shininess) {
  self->setShininess(shininess);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setTextureScale(float
//      textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial15setTextureScaleEf(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    float textureScale) {
  self->setTextureScale(textureScale);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::ambientChanged(const
//      QColor &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial14ambientChangedERK6QColor(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    const QColor *ambient) {
  self->ambientChanged(*ambient);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::diffuseChanged(Qt3DRe
//      nder::QAbstractTexture *diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial14diffuseChangedEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    Qt3DRender::QAbstractTexture *diffuse) {
  self->diffuseChanged(diffuse);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::normalChanged(Qt3DRen
//      der::QAbstractTexture *normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial13normalChangedEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    Qt3DRender::QAbstractTexture *normal) {
  self->normalChanged(normal);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::specularChanged(Qt3DR
//      ender::QAbstractTexture *specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial15specularChangedEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    Qt3DRender::QAbstractTexture *specular) {
  self->specularChanged(specular);
}

//  void
//      Qt3DExtras::QNormalDiffuseSpecularMapMaterial::shininessChanged(float
//      shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial16shininessChangedEf(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    float shininess) {
  self->shininessChanged(shininess);
}

//  void
//      Qt3DExtras::QNormalDiffuseSpecularMapMaterial::textureScaleChanged(fl
//      oat textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial19textureScaleChangedEf(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    float textureScale) {
  self->textureScaleChanged(textureScale);
}

//  Qt3DExtras::QNormalDiffuseSpecularMapMaterial::QNormalDiffuseSpecularMapM
//      aterial(QNormalDiffuseSpecularMapMaterialPrivate &dd, Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseSpecularMapMaterial *ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterialC1ERNS_40QNormalDiffuseSpecularMapMaterialPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QNormalDiffuseSpecularMapMaterial(*dd, parent);
}

//  QNormalDiffuseSpecularMapMaterialPrivate
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial6d_funcEv(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  return self->d_func();
}

//  const QNormalDiffuseSpecularMapMaterialPrivate
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial6d_funcEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QNormalDiffuseSpecularMapMaterial(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterial *>(self)->take(key, call);
}
