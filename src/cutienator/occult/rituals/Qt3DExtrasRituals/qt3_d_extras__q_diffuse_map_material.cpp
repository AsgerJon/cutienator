//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qdiffusemapmaterial.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qdiffusemapmaterial.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QDiffuseMapMaterial that Python can take functions over in. Every Qt3DExtras::QDiffuseMapMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QDiffuseMapMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QDiffuseMapMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseMapMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseMapMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseMapMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseMapMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseMapMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QDiffuseMapMaterial : public Qt3DExtras::QDiffuseMapMaterial {
public:
  using Qt3DExtras::QDiffuseMapMaterial::QDiffuseMapMaterial;
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
      CuteQt3DExtras_QDiffuseMapMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QDiffuseMapMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QDiffuseMapMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QDiffuseMapMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QDiffuseMapMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QDiffuseMapMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QDiffuseMapMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QDiffuseMapMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras19QDiffuseMapMaterial10metaObjectEv(
    const Qt3DExtras::QDiffuseMapMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QDiffuseMapMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras19QDiffuseMapMaterial11qt_metacastEPKc(
    Qt3DExtras::QDiffuseMapMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QDiffuseMapMaterial::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras19QDiffuseMapMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QDiffuseMapMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QDiffuseMapMaterial::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras19QDiffuseMapMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QDiffuseMapMaterial::tr(s, c, n));
}

//  Qt3DExtras::QDiffuseMapMaterial::QDiffuseMapMaterial(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseMapMaterial *ritual_ZN10Qt3DExtras19QDiffuseMapMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QDiffuseMapMaterial(parent);
}

//  Qt3DExtras::QDiffuseMapMaterial::~QDiffuseMapMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterialD1Ev(
    Qt3DExtras::QDiffuseMapMaterial *self) {
  delete self;
}

//  QColor Qt3DExtras::QDiffuseMapMaterial::ambient() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras19QDiffuseMapMaterial7ambientEv(
    const Qt3DExtras::QDiffuseMapMaterial *self) {
  return new QColor(self->ambient());
}

//  QColor Qt3DExtras::QDiffuseMapMaterial::specular() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras19QDiffuseMapMaterial8specularEv(
    const Qt3DExtras::QDiffuseMapMaterial *self) {
  return new QColor(self->specular());
}

//  float Qt3DExtras::QDiffuseMapMaterial::shininess() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QDiffuseMapMaterial9shininessEv(
    const Qt3DExtras::QDiffuseMapMaterial *self) {
  return self->shininess();
}

//  Qt3DRender::QAbstractTexture *Qt3DExtras::QDiffuseMapMaterial::diffuse()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DExtras19QDiffuseMapMaterial7diffuseEv(
    const Qt3DExtras::QDiffuseMapMaterial *self) {
  return self->diffuse();
}

//  float Qt3DExtras::QDiffuseMapMaterial::textureScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QDiffuseMapMaterial12textureScaleEv(
    const Qt3DExtras::QDiffuseMapMaterial *self) {
  return self->textureScale();
}

//  void Qt3DExtras::QDiffuseMapMaterial::setAmbient(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial10setAmbientERK6QColor(
    Qt3DExtras::QDiffuseMapMaterial *self,
    const QColor *color) {
  self->setAmbient(*color);
}

//  void Qt3DExtras::QDiffuseMapMaterial::setSpecular(const QColor &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial11setSpecularERK6QColor(
    Qt3DExtras::QDiffuseMapMaterial *self,
    const QColor *specular) {
  self->setSpecular(*specular);
}

//  void Qt3DExtras::QDiffuseMapMaterial::setShininess(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial12setShininessEf(
    Qt3DExtras::QDiffuseMapMaterial *self,
    float shininess) {
  self->setShininess(shininess);
}

//  void
//      Qt3DExtras::QDiffuseMapMaterial::setDiffuse(Qt3DRender::QAbstractText
//      ure *diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial10setDiffuseEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QDiffuseMapMaterial *self,
    Qt3DRender::QAbstractTexture *diffuse) {
  self->setDiffuse(diffuse);
}

//  void Qt3DExtras::QDiffuseMapMaterial::setTextureScale(float textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial15setTextureScaleEf(
    Qt3DExtras::QDiffuseMapMaterial *self,
    float textureScale) {
  self->setTextureScale(textureScale);
}

//  void Qt3DExtras::QDiffuseMapMaterial::ambientChanged(const QColor
//      &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial14ambientChangedERK6QColor(
    Qt3DExtras::QDiffuseMapMaterial *self,
    const QColor *ambient) {
  self->ambientChanged(*ambient);
}

//  void Qt3DExtras::QDiffuseMapMaterial::diffuseChanged(Qt3DRender::QAbstrac
//      tTexture *diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial14diffuseChangedEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QDiffuseMapMaterial *self,
    Qt3DRender::QAbstractTexture *diffuse) {
  self->diffuseChanged(diffuse);
}

//  void Qt3DExtras::QDiffuseMapMaterial::specularChanged(const QColor
//      &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial15specularChangedERK6QColor(
    Qt3DExtras::QDiffuseMapMaterial *self,
    const QColor *specular) {
  self->specularChanged(*specular);
}

//  void Qt3DExtras::QDiffuseMapMaterial::shininessChanged(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial16shininessChangedEf(
    Qt3DExtras::QDiffuseMapMaterial *self,
    float shininess) {
  self->shininessChanged(shininess);
}

//  void Qt3DExtras::QDiffuseMapMaterial::textureScaleChanged(float
//      textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QDiffuseMapMaterial19textureScaleChangedEf(
    Qt3DExtras::QDiffuseMapMaterial *self,
    float textureScale) {
  self->textureScaleChanged(textureScale);
}

//  QDiffuseMapMaterialPrivate *Qt3DExtras::QDiffuseMapMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseMapMaterialPrivate *ritual_ZN10Qt3DExtras19QDiffuseMapMaterial6d_funcEv(
    Qt3DExtras::QDiffuseMapMaterial *self) {
  return self->d_func();
}

//  const QDiffuseMapMaterialPrivate
//      *Qt3DExtras::QDiffuseMapMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QDiffuseMapMaterialPrivate *ritual_ZNK10Qt3DExtras19QDiffuseMapMaterial6d_funcEv(
    const Qt3DExtras::QDiffuseMapMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QDiffuseMapMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QDiffuseMapMaterial(
    Qt3DExtras::QDiffuseMapMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QDiffuseMapMaterial *>(self)->take(key, call);
}
