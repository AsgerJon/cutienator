//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qmetalroughmaterial.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qmetalroughmaterial.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QMetalRoughMaterial that Python can take functions over in. Every Qt3DExtras::QMetalRoughMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QMetalRoughMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QMetalRoughMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMetalRoughMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMetalRoughMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMetalRoughMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMetalRoughMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QMetalRoughMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QMetalRoughMaterial : public Qt3DExtras::QMetalRoughMaterial {
public:
  using Qt3DExtras::QMetalRoughMaterial::QMetalRoughMaterial;
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
      CuteQt3DExtras_QMetalRoughMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QMetalRoughMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QMetalRoughMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QMetalRoughMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QMetalRoughMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QMetalRoughMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QMetalRoughMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QMetalRoughMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QMetalRoughMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QMetalRoughMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QMetalRoughMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QMetalRoughMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QMetalRoughMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QMetalRoughMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QMetalRoughMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras19QMetalRoughMaterial10metaObjectEv(
    const Qt3DExtras::QMetalRoughMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QMetalRoughMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras19QMetalRoughMaterial11qt_metacastEPKc(
    Qt3DExtras::QMetalRoughMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QMetalRoughMaterial::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras19QMetalRoughMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QMetalRoughMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QMetalRoughMaterial::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras19QMetalRoughMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QMetalRoughMaterial::tr(s, c, n));
}

//  Qt3DExtras::QMetalRoughMaterial::QMetalRoughMaterial(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QMetalRoughMaterial *ritual_ZN10Qt3DExtras19QMetalRoughMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QMetalRoughMaterial(parent);
}

//  Qt3DExtras::QMetalRoughMaterial::~QMetalRoughMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterialD1Ev(
    Qt3DExtras::QMetalRoughMaterial *self) {
  delete self;
}

//  QVariant Qt3DExtras::QMetalRoughMaterial::baseColor() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DExtras19QMetalRoughMaterial9baseColorEv(
    const Qt3DExtras::QMetalRoughMaterial *self) {
  return new QVariant(self->baseColor());
}

//  QVariant Qt3DExtras::QMetalRoughMaterial::metalness() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DExtras19QMetalRoughMaterial9metalnessEv(
    const Qt3DExtras::QMetalRoughMaterial *self) {
  return new QVariant(self->metalness());
}

//  QVariant Qt3DExtras::QMetalRoughMaterial::roughness() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DExtras19QMetalRoughMaterial9roughnessEv(
    const Qt3DExtras::QMetalRoughMaterial *self) {
  return new QVariant(self->roughness());
}

//  QVariant Qt3DExtras::QMetalRoughMaterial::ambientOcclusion() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DExtras19QMetalRoughMaterial16ambientOcclusionEv(
    const Qt3DExtras::QMetalRoughMaterial *self) {
  return new QVariant(self->ambientOcclusion());
}

//  QVariant Qt3DExtras::QMetalRoughMaterial::normal() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DExtras19QMetalRoughMaterial6normalEv(
    const Qt3DExtras::QMetalRoughMaterial *self) {
  return new QVariant(self->normal());
}

//  float Qt3DExtras::QMetalRoughMaterial::textureScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QMetalRoughMaterial12textureScaleEv(
    const Qt3DExtras::QMetalRoughMaterial *self) {
  return self->textureScale();
}

//  void Qt3DExtras::QMetalRoughMaterial::setBaseColor(const QVariant
//      &baseColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial12setBaseColorERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *baseColor) {
  self->setBaseColor(*baseColor);
}

//  void Qt3DExtras::QMetalRoughMaterial::setMetalness(const QVariant
//      &metalness)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial12setMetalnessERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *metalness) {
  self->setMetalness(*metalness);
}

//  void Qt3DExtras::QMetalRoughMaterial::setRoughness(const QVariant
//      &roughness)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial12setRoughnessERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *roughness) {
  self->setRoughness(*roughness);
}

//  void Qt3DExtras::QMetalRoughMaterial::setAmbientOcclusion(const QVariant
//      &ambientOcclusion)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial19setAmbientOcclusionERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *ambientOcclusion) {
  self->setAmbientOcclusion(*ambientOcclusion);
}

//  void Qt3DExtras::QMetalRoughMaterial::setNormal(const QVariant &normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial9setNormalERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *normal) {
  self->setNormal(*normal);
}

//  void Qt3DExtras::QMetalRoughMaterial::setTextureScale(float textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial15setTextureScaleEf(
    Qt3DExtras::QMetalRoughMaterial *self,
    float textureScale) {
  self->setTextureScale(textureScale);
}

//  void Qt3DExtras::QMetalRoughMaterial::baseColorChanged(const QVariant
//      &baseColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial16baseColorChangedERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *baseColor) {
  self->baseColorChanged(*baseColor);
}

//  void Qt3DExtras::QMetalRoughMaterial::metalnessChanged(const QVariant
//      &metalness)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial16metalnessChangedERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *metalness) {
  self->metalnessChanged(*metalness);
}

//  void Qt3DExtras::QMetalRoughMaterial::roughnessChanged(const QVariant
//      &roughness)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial16roughnessChangedERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *roughness) {
  self->roughnessChanged(*roughness);
}

//  void Qt3DExtras::QMetalRoughMaterial::ambientOcclusionChanged(const
//      QVariant &ambientOcclusion)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial23ambientOcclusionChangedERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *ambientOcclusion) {
  self->ambientOcclusionChanged(*ambientOcclusion);
}

//  void Qt3DExtras::QMetalRoughMaterial::normalChanged(const QVariant
//      &normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial13normalChangedERK8QVariant(
    Qt3DExtras::QMetalRoughMaterial *self,
    const QVariant *normal) {
  self->normalChanged(*normal);
}

//  void Qt3DExtras::QMetalRoughMaterial::textureScaleChanged(float
//      textureScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QMetalRoughMaterial19textureScaleChangedEf(
    Qt3DExtras::QMetalRoughMaterial *self,
    float textureScale) {
  self->textureScaleChanged(textureScale);
}

//  Qt3DExtras::QMetalRoughMaterial::QMetalRoughMaterial(QMetalRoughMaterialP
//      rivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QMetalRoughMaterial *ritual_ZN10Qt3DExtras19QMetalRoughMaterialC1ERNS_26QMetalRoughMaterialPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QMetalRoughMaterialPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QMetalRoughMaterial(*dd, parent);
}

//  QMetalRoughMaterialPrivate *Qt3DExtras::QMetalRoughMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QMetalRoughMaterialPrivate *ritual_ZN10Qt3DExtras19QMetalRoughMaterial6d_funcEv(
    Qt3DExtras::QMetalRoughMaterial *self) {
  return self->d_func();
}

//  const QMetalRoughMaterialPrivate
//      *Qt3DExtras::QMetalRoughMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QMetalRoughMaterialPrivate *ritual_ZNK10Qt3DExtras19QMetalRoughMaterial6d_funcEv(
    const Qt3DExtras::QMetalRoughMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QMetalRoughMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QMetalRoughMaterial(
    Qt3DExtras::QMetalRoughMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QMetalRoughMaterial *>(self)->take(key, call);
}
