//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3ddefaultmaterial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3ddefaultmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DDefaultMaterial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DDefaultMaterial : QQuick3DDefaultMaterial {
  using QQuick3DDefaultMaterial::updateSpatialNode;
  using QQuick3DDefaultMaterial::markAllDirty;
  using QQuick3DDefaultMaterial::itemChange;
};

//  A QQuick3DDefaultMaterial that Python can take functions over in. Every QQuick3DDefaultMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DDefaultMaterialCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DDefaultMaterialCall1)(const void *, int *);
typedef void (*CuteQQuick3DDefaultMaterialCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DDefaultMaterialCall3)(const void *, int *);
typedef void (*CuteQQuick3DDefaultMaterialCall4)(const void *, int *);
typedef void (*CuteQQuick3DDefaultMaterialCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DDefaultMaterialCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DDefaultMaterialCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDefaultMaterialCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDefaultMaterialCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDefaultMaterialCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDefaultMaterialCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDefaultMaterialCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DDefaultMaterial : public QQuick3DDefaultMaterial {
public:
  using QQuick3DDefaultMaterial::QQuick3DDefaultMaterial;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DDefaultMaterial::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall0 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DDefaultMaterial::updateSpatialNode(node);
  }

  //  void QQuick3DDefaultMaterial::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall1 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DDefaultMaterial::markAllDirty();
  }

  //  void QQuick3DDefaultMaterial::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall2 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DDefaultMaterial::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall3 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall4 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall5 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall6 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall7 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall8 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall9 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall10 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall11 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DDefaultMaterialCall12 call = reinterpret_cast<CuteQQuick3DDefaultMaterialCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DDefaultMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DDefaultMaterial10metaObjectEv(
    const QQuick3DDefaultMaterial *self) {
  return self->metaObject();
}

//  void *QQuick3DDefaultMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuick3DDefaultMaterial11qt_metacastEPKc(
    QQuick3DDefaultMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DDefaultMaterial::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuick3DDefaultMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DDefaultMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DDefaultMaterial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuick3DDefaultMaterial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DDefaultMaterial::tr(s, c, n));
}

//  QQuick3DDefaultMaterial::QQuick3DDefaultMaterial(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DDefaultMaterial *ritual_ZN23QQuick3DDefaultMaterialC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DDefaultMaterial(parent);
}

//  QQuick3DDefaultMaterial::~QQuick3DDefaultMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterialD1Ev(QQuick3DDefaultMaterial *self) {
  delete self;
}

//  Lighting QQuick3DDefaultMaterial::lighting() const
extern "C" Q_DECL_EXPORT
QQuick3DDefaultMaterial::Lighting ritual_ZNK23QQuick3DDefaultMaterial8lightingEv(
    const QQuick3DDefaultMaterial *self) {
  return self->lighting();
}

//  BlendMode QQuick3DDefaultMaterial::blendMode() const
extern "C" Q_DECL_EXPORT
QQuick3DDefaultMaterial::BlendMode ritual_ZNK23QQuick3DDefaultMaterial9blendModeEv(
    const QQuick3DDefaultMaterial *self) {
  return self->blendMode();
}

//  QColor QQuick3DDefaultMaterial::diffuseColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK23QQuick3DDefaultMaterial12diffuseColorEv(
    const QQuick3DDefaultMaterial *self) {
  return new QColor(self->diffuseColor());
}

//  QQuick3DTexture *QQuick3DDefaultMaterial::diffuseMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK23QQuick3DDefaultMaterial10diffuseMapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->diffuseMap();
}

//  QVector3D QQuick3DDefaultMaterial::emissiveFactor() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DDefaultMaterial14emissiveFactorEv(
    const QQuick3DDefaultMaterial *self) {
  return new QVector3D(self->emissiveFactor());
}

//  QQuick3DTexture *QQuick3DDefaultMaterial::emissiveMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK23QQuick3DDefaultMaterial11emissiveMapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->emissiveMap();
}

//  QQuick3DTexture *QQuick3DDefaultMaterial::specularReflectionMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK23QQuick3DDefaultMaterial21specularReflectionMapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->specularReflectionMap();
}

//  QQuick3DTexture *QQuick3DDefaultMaterial::specularMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK23QQuick3DDefaultMaterial11specularMapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->specularMap();
}

//  SpecularModel QQuick3DDefaultMaterial::specularModel() const
extern "C" Q_DECL_EXPORT
QQuick3DDefaultMaterial::SpecularModel ritual_ZNK23QQuick3DDefaultMaterial13specularModelEv(
    const QQuick3DDefaultMaterial *self) {
  return self->specularModel();
}

//  QColor QQuick3DDefaultMaterial::specularTint() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK23QQuick3DDefaultMaterial12specularTintEv(
    const QQuick3DDefaultMaterial *self) {
  return new QColor(self->specularTint());
}

//  float QQuick3DDefaultMaterial::indexOfRefraction() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial17indexOfRefractionEv(
    const QQuick3DDefaultMaterial *self) {
  return self->indexOfRefraction();
}

//  float QQuick3DDefaultMaterial::fresnelPower() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial12fresnelPowerEv(
    const QQuick3DDefaultMaterial *self) {
  return self->fresnelPower();
}

//  float QQuick3DDefaultMaterial::specularAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial14specularAmountEv(
    const QQuick3DDefaultMaterial *self) {
  return self->specularAmount();
}

//  float QQuick3DDefaultMaterial::specularRoughness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial17specularRoughnessEv(
    const QQuick3DDefaultMaterial *self) {
  return self->specularRoughness();
}

//  QQuick3DTexture *QQuick3DDefaultMaterial::roughnessMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK23QQuick3DDefaultMaterial12roughnessMapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->roughnessMap();
}

//  float QQuick3DDefaultMaterial::opacity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial7opacityEv(
    const QQuick3DDefaultMaterial *self) {
  return self->opacity();
}

//  QQuick3DTexture *QQuick3DDefaultMaterial::opacityMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK23QQuick3DDefaultMaterial10opacityMapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->opacityMap();
}

//  QQuick3DTexture *QQuick3DDefaultMaterial::bumpMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK23QQuick3DDefaultMaterial7bumpMapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->bumpMap();
}

//  float QQuick3DDefaultMaterial::bumpAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial10bumpAmountEv(
    const QQuick3DDefaultMaterial *self) {
  return self->bumpAmount();
}

//  QQuick3DTexture *QQuick3DDefaultMaterial::normalMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK23QQuick3DDefaultMaterial9normalMapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->normalMap();
}

//  QQuick3DTexture *QQuick3DDefaultMaterial::translucencyMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK23QQuick3DDefaultMaterial15translucencyMapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->translucencyMap();
}

//  float QQuick3DDefaultMaterial::translucentFalloff() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial18translucentFalloffEv(
    const QQuick3DDefaultMaterial *self) {
  return self->translucentFalloff();
}

//  float QQuick3DDefaultMaterial::diffuseLightWrap() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial16diffuseLightWrapEv(
    const QQuick3DDefaultMaterial *self) {
  return self->diffuseLightWrap();
}

//  bool QQuick3DDefaultMaterial::vertexColorsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuick3DDefaultMaterial19vertexColorsEnabledEv(
    const QQuick3DDefaultMaterial *self) {
  return self->vertexColorsEnabled();
}

//  TextureChannelMapping QQuick3DDefaultMaterial::roughnessChannel() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK23QQuick3DDefaultMaterial16roughnessChannelEv(
    const QQuick3DDefaultMaterial *self) {
  return self->roughnessChannel();
}

//  TextureChannelMapping QQuick3DDefaultMaterial::opacityChannel() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK23QQuick3DDefaultMaterial14opacityChannelEv(
    const QQuick3DDefaultMaterial *self) {
  return self->opacityChannel();
}

//  TextureChannelMapping QQuick3DDefaultMaterial::translucencyChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK23QQuick3DDefaultMaterial19translucencyChannelEv(
    const QQuick3DDefaultMaterial *self) {
  return self->translucencyChannel();
}

//  float QQuick3DDefaultMaterial::pointSize() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial9pointSizeEv(
    const QQuick3DDefaultMaterial *self) {
  return self->pointSize();
}

//  float QQuick3DDefaultMaterial::lineWidth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DDefaultMaterial9lineWidthEv(
    const QQuick3DDefaultMaterial *self) {
  return self->lineWidth();
}

//  void
//      QQuick3DDefaultMaterial::setLighting(QQuick3DDefaultMaterial::Lightin
//      g lighting)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial11setLightingENS_8LightingE(
    QQuick3DDefaultMaterial *self,
    QQuick3DDefaultMaterial::Lighting lighting) {
  self->setLighting(lighting);
}

//  void
//      QQuick3DDefaultMaterial::setBlendMode(QQuick3DDefaultMaterial::BlendM
//      ode blendMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial12setBlendModeENS_9BlendModeE(
    QQuick3DDefaultMaterial *self,
    QQuick3DDefaultMaterial::BlendMode blendMode) {
  self->setBlendMode(blendMode);
}

//  void QQuick3DDefaultMaterial::setDiffuseColor(QColor diffuseColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial15setDiffuseColorE6QColor(
    QQuick3DDefaultMaterial *self,
    const QColor *diffuseColor) {
  self->setDiffuseColor(*diffuseColor);
}

//  void QQuick3DDefaultMaterial::setDiffuseMap(QQuick3DTexture *diffuseMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial13setDiffuseMapEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *diffuseMap) {
  self->setDiffuseMap(diffuseMap);
}

//  void QQuick3DDefaultMaterial::setEmissiveFactor(QVector3D emissiveFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial17setEmissiveFactorE9QVector3D(
    QQuick3DDefaultMaterial *self,
    const QVector3D *emissiveFactor) {
  self->setEmissiveFactor(*emissiveFactor);
}

//  void QQuick3DDefaultMaterial::setEmissiveMap(QQuick3DTexture
//      *emissiveMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial14setEmissiveMapEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *emissiveMap) {
  self->setEmissiveMap(emissiveMap);
}

//  void QQuick3DDefaultMaterial::setSpecularReflectionMap(QQuick3DTexture
//      *specularReflectionMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial24setSpecularReflectionMapEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *specularReflectionMap) {
  self->setSpecularReflectionMap(specularReflectionMap);
}

//  void QQuick3DDefaultMaterial::setSpecularMap(QQuick3DTexture
//      *specularMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial14setSpecularMapEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *specularMap) {
  self->setSpecularMap(specularMap);
}

//  void QQuick3DDefaultMaterial::setSpecularModel(QQuick3DDefaultMaterial::S
//      pecularModel specularModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial16setSpecularModelENS_13SpecularModelE(
    QQuick3DDefaultMaterial *self,
    QQuick3DDefaultMaterial::SpecularModel specularModel) {
  self->setSpecularModel(specularModel);
}

//  void QQuick3DDefaultMaterial::setSpecularTint(QColor specularTint)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial15setSpecularTintE6QColor(
    QQuick3DDefaultMaterial *self,
    const QColor *specularTint) {
  self->setSpecularTint(*specularTint);
}

//  void QQuick3DDefaultMaterial::setIndexOfRefraction(float
//      indexOfRefraction)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial20setIndexOfRefractionEf(
    QQuick3DDefaultMaterial *self,
    float indexOfRefraction) {
  self->setIndexOfRefraction(indexOfRefraction);
}

//  void QQuick3DDefaultMaterial::setFresnelPower(float fresnelPower)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial15setFresnelPowerEf(
    QQuick3DDefaultMaterial *self,
    float fresnelPower) {
  self->setFresnelPower(fresnelPower);
}

//  void QQuick3DDefaultMaterial::setSpecularAmount(float specularAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial17setSpecularAmountEf(
    QQuick3DDefaultMaterial *self,
    float specularAmount) {
  self->setSpecularAmount(specularAmount);
}

//  void QQuick3DDefaultMaterial::setSpecularRoughness(float
//      specularRoughness)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial20setSpecularRoughnessEf(
    QQuick3DDefaultMaterial *self,
    float specularRoughness) {
  self->setSpecularRoughness(specularRoughness);
}

//  void QQuick3DDefaultMaterial::setRoughnessMap(QQuick3DTexture
//      *roughnessMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial15setRoughnessMapEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *roughnessMap) {
  self->setRoughnessMap(roughnessMap);
}

//  void QQuick3DDefaultMaterial::setOpacity(float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial10setOpacityEf(
    QQuick3DDefaultMaterial *self,
    float opacity) {
  self->setOpacity(opacity);
}

//  void QQuick3DDefaultMaterial::setOpacityMap(QQuick3DTexture *opacityMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial13setOpacityMapEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *opacityMap) {
  self->setOpacityMap(opacityMap);
}

//  void QQuick3DDefaultMaterial::setBumpMap(QQuick3DTexture *bumpMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial10setBumpMapEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *bumpMap) {
  self->setBumpMap(bumpMap);
}

//  void QQuick3DDefaultMaterial::setBumpAmount(float bumpAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial13setBumpAmountEf(
    QQuick3DDefaultMaterial *self,
    float bumpAmount) {
  self->setBumpAmount(bumpAmount);
}

//  void QQuick3DDefaultMaterial::setNormalMap(QQuick3DTexture *normalMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial12setNormalMapEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *normalMap) {
  self->setNormalMap(normalMap);
}

//  void QQuick3DDefaultMaterial::setTranslucencyMap(QQuick3DTexture
//      *translucencyMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial18setTranslucencyMapEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *translucencyMap) {
  self->setTranslucencyMap(translucencyMap);
}

//  void QQuick3DDefaultMaterial::setTranslucentFalloff(float
//      translucentFalloff)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial21setTranslucentFalloffEf(
    QQuick3DDefaultMaterial *self,
    float translucentFalloff) {
  self->setTranslucentFalloff(translucentFalloff);
}

//  void QQuick3DDefaultMaterial::setDiffuseLightWrap(float diffuseLightWrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial19setDiffuseLightWrapEf(
    QQuick3DDefaultMaterial *self,
    float diffuseLightWrap) {
  self->setDiffuseLightWrap(diffuseLightWrap);
}

//  void QQuick3DDefaultMaterial::setVertexColorsEnabled(bool
//      vertexColorsEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial22setVertexColorsEnabledEb(
    QQuick3DDefaultMaterial *self,
    bool vertexColorsEnabled) {
  self->setVertexColorsEnabled(vertexColorsEnabled);
}

//  void QQuick3DDefaultMaterial::setRoughnessChannel(QQuick3DMaterial::Textu
//      reChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial19setRoughnessChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DDefaultMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setRoughnessChannel(channel);
}

//  void QQuick3DDefaultMaterial::setOpacityChannel(QQuick3DMaterial::Texture
//      ChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial17setOpacityChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DDefaultMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setOpacityChannel(channel);
}

//  void QQuick3DDefaultMaterial::setTranslucencyChannel(QQuick3DMaterial::Te
//      xtureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial22setTranslucencyChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DDefaultMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setTranslucencyChannel(channel);
}

//  void QQuick3DDefaultMaterial::setPointSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial12setPointSizeEf(
    QQuick3DDefaultMaterial *self,
    float size) {
  self->setPointSize(size);
}

//  void QQuick3DDefaultMaterial::setLineWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial12setLineWidthEf(
    QQuick3DDefaultMaterial *self,
    float width) {
  self->setLineWidth(width);
}

//  void QQuick3DDefaultMaterial::lightingChanged(QQuick3DDefaultMaterial::Li
//      ghting lighting)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial15lightingChangedENS_8LightingE(
    QQuick3DDefaultMaterial *self,
    QQuick3DDefaultMaterial::Lighting lighting) {
  self->lightingChanged(lighting);
}

//  void QQuick3DDefaultMaterial::blendModeChanged(QQuick3DDefaultMaterial::B
//      lendMode blendMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial16blendModeChangedENS_9BlendModeE(
    QQuick3DDefaultMaterial *self,
    QQuick3DDefaultMaterial::BlendMode blendMode) {
  self->blendModeChanged(blendMode);
}

//  void QQuick3DDefaultMaterial::diffuseColorChanged(QColor diffuseColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial19diffuseColorChangedE6QColor(
    QQuick3DDefaultMaterial *self,
    const QColor *diffuseColor) {
  self->diffuseColorChanged(*diffuseColor);
}

//  void QQuick3DDefaultMaterial::diffuseMapChanged(QQuick3DTexture
//      *diffuseMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial17diffuseMapChangedEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *diffuseMap) {
  self->diffuseMapChanged(diffuseMap);
}

//  void QQuick3DDefaultMaterial::emissiveFactorChanged(QVector3D
//      emissiveFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial21emissiveFactorChangedE9QVector3D(
    QQuick3DDefaultMaterial *self,
    const QVector3D *emissiveFactor) {
  self->emissiveFactorChanged(*emissiveFactor);
}

//  void QQuick3DDefaultMaterial::emissiveMapChanged(QQuick3DTexture
//      *emissiveMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial18emissiveMapChangedEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *emissiveMap) {
  self->emissiveMapChanged(emissiveMap);
}

//  void
//      QQuick3DDefaultMaterial::specularReflectionMapChanged(QQuick3DTexture
//      *specularReflectionMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial28specularReflectionMapChangedEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *specularReflectionMap) {
  self->specularReflectionMapChanged(specularReflectionMap);
}

//  void QQuick3DDefaultMaterial::specularMapChanged(QQuick3DTexture
//      *specularMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial18specularMapChangedEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *specularMap) {
  self->specularMapChanged(specularMap);
}

//  void QQuick3DDefaultMaterial::specularModelChanged(QQuick3DDefaultMateria
//      l::SpecularModel specularModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial20specularModelChangedENS_13SpecularModelE(
    QQuick3DDefaultMaterial *self,
    QQuick3DDefaultMaterial::SpecularModel specularModel) {
  self->specularModelChanged(specularModel);
}

//  void QQuick3DDefaultMaterial::specularTintChanged(QColor specularTint)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial19specularTintChangedE6QColor(
    QQuick3DDefaultMaterial *self,
    const QColor *specularTint) {
  self->specularTintChanged(*specularTint);
}

//  void QQuick3DDefaultMaterial::indexOfRefractionChanged(float
//      indexOfRefraction)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial24indexOfRefractionChangedEf(
    QQuick3DDefaultMaterial *self,
    float indexOfRefraction) {
  self->indexOfRefractionChanged(indexOfRefraction);
}

//  void QQuick3DDefaultMaterial::fresnelPowerChanged(float fresnelPower)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial19fresnelPowerChangedEf(
    QQuick3DDefaultMaterial *self,
    float fresnelPower) {
  self->fresnelPowerChanged(fresnelPower);
}

//  void QQuick3DDefaultMaterial::specularAmountChanged(float specularAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial21specularAmountChangedEf(
    QQuick3DDefaultMaterial *self,
    float specularAmount) {
  self->specularAmountChanged(specularAmount);
}

//  void QQuick3DDefaultMaterial::specularRoughnessChanged(float
//      specularRoughness)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial24specularRoughnessChangedEf(
    QQuick3DDefaultMaterial *self,
    float specularRoughness) {
  self->specularRoughnessChanged(specularRoughness);
}

//  void QQuick3DDefaultMaterial::roughnessMapChanged(QQuick3DTexture
//      *roughnessMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial19roughnessMapChangedEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *roughnessMap) {
  self->roughnessMapChanged(roughnessMap);
}

//  void QQuick3DDefaultMaterial::opacityChanged(float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial14opacityChangedEf(
    QQuick3DDefaultMaterial *self,
    float opacity) {
  self->opacityChanged(opacity);
}

//  void QQuick3DDefaultMaterial::opacityMapChanged(QQuick3DTexture
//      *opacityMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial17opacityMapChangedEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *opacityMap) {
  self->opacityMapChanged(opacityMap);
}

//  void QQuick3DDefaultMaterial::bumpMapChanged(QQuick3DTexture *bumpMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial14bumpMapChangedEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *bumpMap) {
  self->bumpMapChanged(bumpMap);
}

//  void QQuick3DDefaultMaterial::bumpAmountChanged(float bumpAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial17bumpAmountChangedEf(
    QQuick3DDefaultMaterial *self,
    float bumpAmount) {
  self->bumpAmountChanged(bumpAmount);
}

//  void QQuick3DDefaultMaterial::normalMapChanged(QQuick3DTexture
//      *normalMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial16normalMapChangedEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *normalMap) {
  self->normalMapChanged(normalMap);
}

//  void QQuick3DDefaultMaterial::translucencyMapChanged(QQuick3DTexture
//      *translucencyMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial22translucencyMapChangedEP15QQuick3DTexture(
    QQuick3DDefaultMaterial *self,
    QQuick3DTexture *translucencyMap) {
  self->translucencyMapChanged(translucencyMap);
}

//  void QQuick3DDefaultMaterial::translucentFalloffChanged(float
//      translucentFalloff)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial25translucentFalloffChangedEf(
    QQuick3DDefaultMaterial *self,
    float translucentFalloff) {
  self->translucentFalloffChanged(translucentFalloff);
}

//  void QQuick3DDefaultMaterial::diffuseLightWrapChanged(float
//      diffuseLightWrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial23diffuseLightWrapChangedEf(
    QQuick3DDefaultMaterial *self,
    float diffuseLightWrap) {
  self->diffuseLightWrapChanged(diffuseLightWrap);
}

//  void QQuick3DDefaultMaterial::vertexColorsEnabledChanged(bool
//      vertexColorsEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial26vertexColorsEnabledChangedEb(
    QQuick3DDefaultMaterial *self,
    bool vertexColorsEnabled) {
  self->vertexColorsEnabledChanged(vertexColorsEnabled);
}

//  void QQuick3DDefaultMaterial::roughnessChannelChanged(QQuick3DMaterial::T
//      extureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial23roughnessChannelChangedEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DDefaultMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->roughnessChannelChanged(channel);
}

//  void QQuick3DDefaultMaterial::opacityChannelChanged(QQuick3DMaterial::Tex
//      tureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial21opacityChannelChangedEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DDefaultMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->opacityChannelChanged(channel);
}

//  void QQuick3DDefaultMaterial::translucencyChannelChanged(QQuick3DMaterial
//      ::TextureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial26translucencyChannelChangedEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DDefaultMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->translucencyChannelChanged(channel);
}

//  void QQuick3DDefaultMaterial::pointSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial16pointSizeChangedEv(
    QQuick3DDefaultMaterial *self) {
  self->pointSizeChanged();
}

//  void QQuick3DDefaultMaterial::lineWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial16lineWidthChangedEv(
    QQuick3DDefaultMaterial *self) {
  self->lineWidthChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DDefaultMaterial::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN23QQuick3DDefaultMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DDefaultMaterial *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DDefaultMaterial::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial12markAllDirtyEv(
    QQuick3DDefaultMaterial *self) {
  self->markAllDirty();
}

//  void QQuick3DDefaultMaterial::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DDefaultMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DDefaultMaterial::updateSceneManager(QQuick3DSceneManager
//      *sceneManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DDefaultMaterial *self,
    QQuick3DSceneManager *sceneManager) {
  self->updateSceneManager(sceneManager);
}

//  void QQuick3DDefaultMaterial::markDirty(DirtyType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DDefaultMaterial9markDirtyENS_9DirtyTypeE(
    QQuick3DDefaultMaterial *self,
    QQuick3DDefaultMaterial::DirtyType type) {
  self->markDirty(type);
}

//  a Python function taken by a CuteQQuick3DDefaultMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DDefaultMaterial(
    QQuick3DDefaultMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DDefaultMaterial *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DDefaultMaterial::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN23QQuick3DDefaultMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DDefaultMaterial *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DDefaultMaterial *>(self)->OwnQQuick3DDefaultMaterial::updateSpatialNode(
      node);
}

//  void QQuick3DDefaultMaterial::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DDefaultMaterial12markAllDirtyEv(
    QQuick3DDefaultMaterial *self) {
  static_cast<OwnQQuick3DDefaultMaterial *>(self)->OwnQQuick3DDefaultMaterial::markAllDirty();
}

//  void QQuick3DDefaultMaterial::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DDefaultMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DDefaultMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DDefaultMaterial *>(self)->OwnQQuick3DDefaultMaterial::itemChange(
      a0,
      *a1);
}
