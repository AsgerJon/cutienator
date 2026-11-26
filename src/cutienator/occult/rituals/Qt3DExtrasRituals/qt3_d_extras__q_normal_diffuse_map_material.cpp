//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qnormaldiffusemapmaterial.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DExtras/qnormaldiffusemapmaterial.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QNormalDiffuseMapMaterial that Python can take functions over in. Every Qt3DExtras::QNormalDiffuseMapMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QNormalDiffuseMapMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QNormalDiffuseMapMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QNormalDiffuseMapMaterial : public Qt3DExtras::QNormalDiffuseMapMaterial {
public:
  using Qt3DExtras::QNormalDiffuseMapMaterial::QNormalDiffuseMapMaterial;
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
      CuteQt3DExtras_QNormalDiffuseMapMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QNormalDiffuseMapMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QNormalDiffuseMapMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QNormalDiffuseMapMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QNormalDiffuseMapMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QNormalDiffuseMapMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QNormalDiffuseMapMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QNormalDiffuseMapMaterial::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial10metaObjectEv(
    const Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QNormalDiffuseMapMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial11qt_metacastEPKc(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QNormalDiffuseMapMaterial::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QNormalDiffuseMapMaterial::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QNormalDiffuseMapMaterial::tr(s, c, n));
}

//  Qt3DExtras::QNormalDiffuseMapMaterial::QNormalDiffuseMapMaterial(Qt3DCore
//      ::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseMapMaterial *ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QNormalDiffuseMapMaterial(parent);
}

//  Qt3DExtras::QNormalDiffuseMapMaterial::~QNormalDiffuseMapMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterialD1Ev(
    Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  delete self;
}

//  QColor Qt3DExtras::QNormalDiffuseMapMaterial::ambient() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial7ambientEv(
    const Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  return new QColor(self->ambient());
}

//  QColor Qt3DExtras::QNormalDiffuseMapMaterial::specular() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial8specularEv(
    const Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  return new QColor(self->specular());
}

//  Qt3DRender::QAbstractTexture
//      *Qt3DExtras::QNormalDiffuseMapMaterial::diffuse() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial7diffuseEv(
    const Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  return self->diffuse();
}

//  Qt3DRender::QAbstractTexture
//      *Qt3DExtras::QNormalDiffuseMapMaterial::normal() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial6normalEv(
    const Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  return self->normal();
}

//  float Qt3DExtras::QNormalDiffuseMapMaterial::shininess() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial9shininessEv(
    const Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  return self->shininess();
}

//  float Qt3DExtras::QNormalDiffuseMapMaterial::textureScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial12textureScaleEv(
    const Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  return self->textureScale();
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::setAmbient(const QColor
//      &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial10setAmbientERK6QColor(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    const QColor *ambient) {
  self->setAmbient(*ambient);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::setSpecular(const QColor
//      &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial11setSpecularERK6QColor(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    const QColor *specular) {
  self->setSpecular(*specular);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::setDiffuse(Qt3DRender::QAbstr
//      actTexture *diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial10setDiffuseEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    Qt3DRender::QAbstractTexture *diffuse) {
  self->setDiffuse(diffuse);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::setNormal(Qt3DRender::QAbstra
//      ctTexture *normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial9setNormalEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    Qt3DRender::QAbstractTexture *normal) {
  self->setNormal(normal);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::setShininess(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial12setShininessEf(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    float shininess) {
  self->setShininess(shininess);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::setTextureScale(float
//      textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial15setTextureScaleEf(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    float textureScale) {
  self->setTextureScale(textureScale);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::ambientChanged(const QColor
//      &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial14ambientChangedERK6QColor(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    const QColor *ambient) {
  self->ambientChanged(*ambient);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::diffuseChanged(Qt3DRender::QA
//      bstractTexture *diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial14diffuseChangedEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    Qt3DRender::QAbstractTexture *diffuse) {
  self->diffuseChanged(diffuse);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::normalChanged(Qt3DRender::QAb
//      stractTexture *normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial13normalChangedEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    Qt3DRender::QAbstractTexture *normal) {
  self->normalChanged(normal);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::specularChanged(const QColor
//      &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial15specularChangedERK6QColor(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    const QColor *specular) {
  self->specularChanged(*specular);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::shininessChanged(float
//      shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial16shininessChangedEf(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    float shininess) {
  self->shininessChanged(shininess);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterial::textureScaleChanged(float
//      textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial19textureScaleChangedEf(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    float textureScale) {
  self->textureScaleChanged(textureScale);
}

//  Qt3DExtras::QNormalDiffuseMapMaterial::QNormalDiffuseMapMaterial(QNormalD
//      iffuseMapMaterialPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseMapMaterial *ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterialC1ERNS_32QNormalDiffuseMapMaterialPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QNormalDiffuseMapMaterial(*dd, parent);
}

//  QNormalDiffuseMapMaterialPrivate
//      *Qt3DExtras::QNormalDiffuseMapMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseMapMaterialPrivate *ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial6d_funcEv(
    Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  return self->d_func();
}

//  const QNormalDiffuseMapMaterialPrivate
//      *Qt3DExtras::QNormalDiffuseMapMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QNormalDiffuseMapMaterialPrivate *ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial6d_funcEv(
    const Qt3DExtras::QNormalDiffuseMapMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QNormalDiffuseMapMaterial,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QNormalDiffuseMapMaterial(
    Qt3DExtras::QNormalDiffuseMapMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QNormalDiffuseMapMaterial *>(self)->take(key, call);
}
