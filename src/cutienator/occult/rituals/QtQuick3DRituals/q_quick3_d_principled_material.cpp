//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dprincipledmaterial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dprincipledmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DPrincipledMaterial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DPrincipledMaterial : QQuick3DPrincipledMaterial {
  using QQuick3DPrincipledMaterial::updateSpatialNode;
  using QQuick3DPrincipledMaterial::markAllDirty;
  using QQuick3DPrincipledMaterial::itemChange;
};

//  A QQuick3DPrincipledMaterial that Python can take functions over in. Every QQuick3DPrincipledMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DPrincipledMaterialCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DPrincipledMaterialCall1)(const void *, int *);
typedef void (*CuteQQuick3DPrincipledMaterialCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DPrincipledMaterialCall3)(const void *, int *);
typedef void (*CuteQQuick3DPrincipledMaterialCall4)(const void *, int *);
typedef void (*CuteQQuick3DPrincipledMaterialCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DPrincipledMaterialCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DPrincipledMaterialCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPrincipledMaterialCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPrincipledMaterialCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPrincipledMaterialCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPrincipledMaterialCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPrincipledMaterialCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DPrincipledMaterial : public QQuick3DPrincipledMaterial {
public:
  using QQuick3DPrincipledMaterial::QQuick3DPrincipledMaterial;
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
  //      *QQuick3DPrincipledMaterial::updateSpatialNode(QSSGRenderGraphObj
  //      ect *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DPrincipledMaterialCall0 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DPrincipledMaterial::updateSpatialNode(node);
  }

  //  void QQuick3DPrincipledMaterial::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DPrincipledMaterialCall1 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DPrincipledMaterial::markAllDirty();
  }

  //  void QQuick3DPrincipledMaterial::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DPrincipledMaterialCall2 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DPrincipledMaterial::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DPrincipledMaterialCall3 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DPrincipledMaterialCall4 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DPrincipledMaterialCall5 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall5>(taken[5]);
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
      CuteQQuick3DPrincipledMaterialCall6 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall6>(taken[6]);
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
      CuteQQuick3DPrincipledMaterialCall7 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall7>(taken[7]);
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
      CuteQQuick3DPrincipledMaterialCall8 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall8>(taken[8]);
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
      CuteQQuick3DPrincipledMaterialCall9 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall9>(taken[9]);
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
      CuteQQuick3DPrincipledMaterialCall10 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall10>(taken[10]);
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
      CuteQQuick3DPrincipledMaterialCall11 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall11>(taken[11]);
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
      CuteQQuick3DPrincipledMaterialCall12 call = reinterpret_cast<CuteQQuick3DPrincipledMaterialCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DPrincipledMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuick3DPrincipledMaterial10metaObjectEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->metaObject();
}

//  QString QQuick3DPrincipledMaterial::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuick3DPrincipledMaterial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DPrincipledMaterial::tr(s, c, n));
}

//  QQuick3DPrincipledMaterial::QQuick3DPrincipledMaterial(QQuick3DObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DPrincipledMaterial *ritual_ZN26QQuick3DPrincipledMaterialC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DPrincipledMaterial(parent);
}

//  QQuick3DPrincipledMaterial::~QQuick3DPrincipledMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterialD1Ev(
    QQuick3DPrincipledMaterial *self) {
  delete self;
}

//  Lighting QQuick3DPrincipledMaterial::lighting() const
extern "C" Q_DECL_EXPORT
QQuick3DPrincipledMaterial::Lighting ritual_ZNK26QQuick3DPrincipledMaterial8lightingEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->lighting();
}

//  BlendMode QQuick3DPrincipledMaterial::blendMode() const
extern "C" Q_DECL_EXPORT
QQuick3DPrincipledMaterial::BlendMode ritual_ZNK26QQuick3DPrincipledMaterial9blendModeEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->blendMode();
}

//  QColor QQuick3DPrincipledMaterial::baseColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK26QQuick3DPrincipledMaterial9baseColorEv(
    const QQuick3DPrincipledMaterial *self) {
  return new QColor(self->baseColor());
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::baseColorMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial12baseColorMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->baseColorMap();
}

//  bool QQuick3DPrincipledMaterial::baseColorSingleChannelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuick3DPrincipledMaterial29baseColorSingleChannelEnabledEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->baseColorSingleChannelEnabled();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::baseColorChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial16baseColorChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->baseColorChannel();
}

//  bool QQuick3DPrincipledMaterial::specularSingleChannelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuick3DPrincipledMaterial28specularSingleChannelEnabledEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->specularSingleChannelEnabled();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::specularChannel() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial15specularChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->specularChannel();
}

//  bool QQuick3DPrincipledMaterial::emissiveSingleChannelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuick3DPrincipledMaterial28emissiveSingleChannelEnabledEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->emissiveSingleChannelEnabled();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::emissiveChannel() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial15emissiveChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->emissiveChannel();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::emissiveMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial11emissiveMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->emissiveMap();
}

//  QVector3D QQuick3DPrincipledMaterial::emissiveFactor() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK26QQuick3DPrincipledMaterial14emissiveFactorEv(
    const QQuick3DPrincipledMaterial *self) {
  return new QVector3D(self->emissiveFactor());
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::specularReflectionMap()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial21specularReflectionMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->specularReflectionMap();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::specularMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial11specularMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->specularMap();
}

//  float QQuick3DPrincipledMaterial::specularTint() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial12specularTintEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->specularTint();
}

//  float QQuick3DPrincipledMaterial::specularAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial14specularAmountEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->specularAmount();
}

//  float QQuick3DPrincipledMaterial::roughness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial9roughnessEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->roughness();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::roughnessMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial12roughnessMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->roughnessMap();
}

//  bool QQuick3DPrincipledMaterial::invertOpacityMapValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuick3DPrincipledMaterial21invertOpacityMapValueEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->invertOpacityMapValue();
}

//  float QQuick3DPrincipledMaterial::opacity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial7opacityEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->opacity();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::opacityMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial10opacityMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->opacityMap();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::normalMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial9normalMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->normalMap();
}

//  float QQuick3DPrincipledMaterial::metalness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial9metalnessEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->metalness();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::metalnessMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial12metalnessMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->metalnessMap();
}

//  float QQuick3DPrincipledMaterial::normalStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial14normalStrengthEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->normalStrength();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::occlusionMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial12occlusionMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->occlusionMap();
}

//  float QQuick3DPrincipledMaterial::occlusionAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial15occlusionAmountEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->occlusionAmount();
}

//  AlphaMode QQuick3DPrincipledMaterial::alphaMode() const
extern "C" Q_DECL_EXPORT
QQuick3DPrincipledMaterial::AlphaMode ritual_ZNK26QQuick3DPrincipledMaterial9alphaModeEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->alphaMode();
}

//  float QQuick3DPrincipledMaterial::alphaCutoff() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial11alphaCutoffEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->alphaCutoff();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::metalnessChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial16metalnessChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->metalnessChannel();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::roughnessChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial16roughnessChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->roughnessChannel();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::opacityChannel() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial14opacityChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->opacityChannel();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::occlusionChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial16occlusionChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->occlusionChannel();
}

//  float QQuick3DPrincipledMaterial::pointSize() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial9pointSizeEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->pointSize();
}

//  float QQuick3DPrincipledMaterial::lineWidth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial9lineWidthEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->lineWidth();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::heightMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial9heightMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->heightMap();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::heightChannel() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial13heightChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->heightChannel();
}

//  float QQuick3DPrincipledMaterial::heightAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial12heightAmountEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->heightAmount();
}

//  int QQuick3DPrincipledMaterial::minHeightMapSamples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuick3DPrincipledMaterial19minHeightMapSamplesEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->minHeightMapSamples();
}

//  int QQuick3DPrincipledMaterial::maxHeightMapSamples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuick3DPrincipledMaterial19maxHeightMapSamplesEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->maxHeightMapSamples();
}

//  float QQuick3DPrincipledMaterial::clearcoatAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial15clearcoatAmountEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatAmount();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::clearcoatMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial12clearcoatMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatMap();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::clearcoatChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial16clearcoatChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatChannel();
}

//  float QQuick3DPrincipledMaterial::clearcoatRoughnessAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial24clearcoatRoughnessAmountEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatRoughnessAmount();
}

//  TextureChannelMapping
//      QQuick3DPrincipledMaterial::clearcoatRoughnessChannel() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial25clearcoatRoughnessChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatRoughnessChannel();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::clearcoatRoughnessMap()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial21clearcoatRoughnessMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatRoughnessMap();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::clearcoatNormalMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial18clearcoatNormalMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatNormalMap();
}

//  float QQuick3DPrincipledMaterial::clearcoatNormalStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial23clearcoatNormalStrengthEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatNormalStrength();
}

//  float QQuick3DPrincipledMaterial::transmissionFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial18transmissionFactorEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->transmissionFactor();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::transmissionMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial15transmissionMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->transmissionMap();
}

//  TextureChannelMapping QQuick3DPrincipledMaterial::transmissionChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK26QQuick3DPrincipledMaterial19transmissionChannelEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->transmissionChannel();
}

//  float QQuick3DPrincipledMaterial::thicknessFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial15thicknessFactorEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->thicknessFactor();
}

//  QQuick3DTexture *QQuick3DPrincipledMaterial::thicknessMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DPrincipledMaterial12thicknessMapEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->thicknessMap();
}

//  float QQuick3DPrincipledMaterial::attenuationDistance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial19attenuationDistanceEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->attenuationDistance();
}

//  const QColor &QQuick3DPrincipledMaterial::attenuationColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK26QQuick3DPrincipledMaterial16attenuationColorEv(
    const QQuick3DPrincipledMaterial *self) {
  return new QColor(self->attenuationColor());
}

//  float QQuick3DPrincipledMaterial::indexOfRefraction() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial17indexOfRefractionEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->indexOfRefraction();
}

//  bool QQuick3DPrincipledMaterial::fresnelScaleBiasEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuick3DPrincipledMaterial23fresnelScaleBiasEnabledEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->fresnelScaleBiasEnabled();
}

//  float QQuick3DPrincipledMaterial::fresnelScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial12fresnelScaleEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->fresnelScale();
}

//  float QQuick3DPrincipledMaterial::fresnelBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial11fresnelBiasEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->fresnelBias();
}

//  float QQuick3DPrincipledMaterial::fresnelPower() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial12fresnelPowerEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->fresnelPower();
}

//  bool QQuick3DPrincipledMaterial::clearcoatFresnelScaleBiasEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuick3DPrincipledMaterial32clearcoatFresnelScaleBiasEnabledEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatFresnelScaleBiasEnabled();
}

//  float QQuick3DPrincipledMaterial::clearcoatFresnelScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial21clearcoatFresnelScaleEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatFresnelScale();
}

//  float QQuick3DPrincipledMaterial::clearcoatFresnelBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial20clearcoatFresnelBiasEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatFresnelBias();
}

//  float QQuick3DPrincipledMaterial::clearcoatFresnelPower() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DPrincipledMaterial21clearcoatFresnelPowerEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->clearcoatFresnelPower();
}

//  bool QQuick3DPrincipledMaterial::vertexColorsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuick3DPrincipledMaterial19vertexColorsEnabledEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->vertexColorsEnabled();
}

//  bool QQuick3DPrincipledMaterial::vertexColorsMaskEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuick3DPrincipledMaterial23vertexColorsMaskEnabledEv(
    const QQuick3DPrincipledMaterial *self) {
  return self->vertexColorsMaskEnabled();
}

//  VertexColorMaskFlags QQuick3DPrincipledMaterial::vertexColorRedMask()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuick3DPrincipledMaterial18vertexColorRedMaskEv(
    const QQuick3DPrincipledMaterial *self) {
  return static_cast<int>(self->vertexColorRedMask().toInt());
}

//  VertexColorMaskFlags QQuick3DPrincipledMaterial::vertexColorGreenMask()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuick3DPrincipledMaterial20vertexColorGreenMaskEv(
    const QQuick3DPrincipledMaterial *self) {
  return static_cast<int>(self->vertexColorGreenMask().toInt());
}

//  VertexColorMaskFlags QQuick3DPrincipledMaterial::vertexColorBlueMask()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuick3DPrincipledMaterial19vertexColorBlueMaskEv(
    const QQuick3DPrincipledMaterial *self) {
  return static_cast<int>(self->vertexColorBlueMask().toInt());
}

//  VertexColorMaskFlags QQuick3DPrincipledMaterial::vertexColorAlphaMask()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuick3DPrincipledMaterial20vertexColorAlphaMaskEv(
    const QQuick3DPrincipledMaterial *self) {
  return static_cast<int>(self->vertexColorAlphaMask().toInt());
}

//  void QQuick3DPrincipledMaterial::setLighting(QQuick3DPrincipledMaterial::
//      Lighting lighting)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial11setLightingENS_8LightingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DPrincipledMaterial::Lighting lighting) {
  self->setLighting(lighting);
}

//  void QQuick3DPrincipledMaterial::setBlendMode(QQuick3DPrincipledMaterial:
//      :BlendMode blendMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12setBlendModeENS_9BlendModeE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DPrincipledMaterial::BlendMode blendMode) {
  self->setBlendMode(blendMode);
}

//  void QQuick3DPrincipledMaterial::setBaseColor(QColor baseColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12setBaseColorE6QColor(
    QQuick3DPrincipledMaterial *self,
    const QColor *baseColor) {
  self->setBaseColor(*baseColor);
}

//  void QQuick3DPrincipledMaterial::setBaseColorMap(QQuick3DTexture
//      *baseColorMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setBaseColorMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *baseColorMap) {
  self->setBaseColorMap(baseColorMap);
}

//  void QQuick3DPrincipledMaterial::setBaseColorSingleChannelEnabled(bool
//      baseColorSingleChannelEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial32setBaseColorSingleChannelEnabledEb(
    QQuick3DPrincipledMaterial *self,
    bool baseColorSingleChannelEnabled) {
  self->setBaseColorSingleChannelEnabled(baseColorSingleChannelEnabled);
}

//  void QQuick3DPrincipledMaterial::setBaseColorChannel(QQuick3DMaterial::Te
//      xtureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial19setBaseColorChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setBaseColorChannel(channel);
}

//  void QQuick3DPrincipledMaterial::setSpecularSingleChannelEnabled(bool
//      specularSingleChannelEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial31setSpecularSingleChannelEnabledEb(
    QQuick3DPrincipledMaterial *self,
    bool specularSingleChannelEnabled) {
  self->setSpecularSingleChannelEnabled(specularSingleChannelEnabled);
}

//  void QQuick3DPrincipledMaterial::setSpecularChannel(QQuick3DMaterial::Tex
//      tureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial18setSpecularChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setSpecularChannel(channel);
}

//  void QQuick3DPrincipledMaterial::setEmissiveSingleChannelEnabled(bool
//      emissiveSingleChannelEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial31setEmissiveSingleChannelEnabledEb(
    QQuick3DPrincipledMaterial *self,
    bool emissiveSingleChannelEnabled) {
  self->setEmissiveSingleChannelEnabled(emissiveSingleChannelEnabled);
}

//  void QQuick3DPrincipledMaterial::setEmissiveChannel(QQuick3DMaterial::Tex
//      tureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial18setEmissiveChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setEmissiveChannel(channel);
}

//  void QQuick3DPrincipledMaterial::setEmissiveMap(QQuick3DTexture
//      *emissiveMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial14setEmissiveMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *emissiveMap) {
  self->setEmissiveMap(emissiveMap);
}

//  void QQuick3DPrincipledMaterial::setEmissiveFactor(QVector3D
//      emissiveFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial17setEmissiveFactorE9QVector3D(
    QQuick3DPrincipledMaterial *self,
    const QVector3D *emissiveFactor) {
  self->setEmissiveFactor(*emissiveFactor);
}

//  void QQuick3DPrincipledMaterial::setSpecularReflectionMap(QQuick3DTexture
//      *specularReflectionMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial24setSpecularReflectionMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *specularReflectionMap) {
  self->setSpecularReflectionMap(specularReflectionMap);
}

//  void QQuick3DPrincipledMaterial::setSpecularMap(QQuick3DTexture
//      *specularMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial14setSpecularMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *specularMap) {
  self->setSpecularMap(specularMap);
}

//  void QQuick3DPrincipledMaterial::setSpecularTint(float specularTint)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setSpecularTintEf(
    QQuick3DPrincipledMaterial *self,
    float specularTint) {
  self->setSpecularTint(specularTint);
}

//  void QQuick3DPrincipledMaterial::setSpecularAmount(float specularAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial17setSpecularAmountEf(
    QQuick3DPrincipledMaterial *self,
    float specularAmount) {
  self->setSpecularAmount(specularAmount);
}

//  void QQuick3DPrincipledMaterial::setRoughness(float roughness)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12setRoughnessEf(
    QQuick3DPrincipledMaterial *self,
    float roughness) {
  self->setRoughness(roughness);
}

//  void QQuick3DPrincipledMaterial::setRoughnessMap(QQuick3DTexture
//      *roughnessMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setRoughnessMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *roughnessMap) {
  self->setRoughnessMap(roughnessMap);
}

//  void QQuick3DPrincipledMaterial::setInvertOpacityMapValue(bool
//      invertOpacityMapValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial24setInvertOpacityMapValueEb(
    QQuick3DPrincipledMaterial *self,
    bool invertOpacityMapValue) {
  self->setInvertOpacityMapValue(invertOpacityMapValue);
}

//  void QQuick3DPrincipledMaterial::setOpacity(float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial10setOpacityEf(
    QQuick3DPrincipledMaterial *self,
    float opacity) {
  self->setOpacity(opacity);
}

//  void QQuick3DPrincipledMaterial::setOpacityMap(QQuick3DTexture
//      *opacityMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial13setOpacityMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *opacityMap) {
  self->setOpacityMap(opacityMap);
}

//  void QQuick3DPrincipledMaterial::setNormalMap(QQuick3DTexture *normalMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12setNormalMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *normalMap) {
  self->setNormalMap(normalMap);
}

//  void QQuick3DPrincipledMaterial::setMetalness(float metalnessAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12setMetalnessEf(
    QQuick3DPrincipledMaterial *self,
    float metalnessAmount) {
  self->setMetalness(metalnessAmount);
}

//  void QQuick3DPrincipledMaterial::setMetalnessMap(QQuick3DTexture
//      *metalnessMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setMetalnessMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *metalnessMap) {
  self->setMetalnessMap(metalnessMap);
}

//  void QQuick3DPrincipledMaterial::setNormalStrength(float normalStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial17setNormalStrengthEf(
    QQuick3DPrincipledMaterial *self,
    float normalStrength) {
  self->setNormalStrength(normalStrength);
}

//  void QQuick3DPrincipledMaterial::setOcclusionMap(QQuick3DTexture
//      *occlusionMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setOcclusionMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *occlusionMap) {
  self->setOcclusionMap(occlusionMap);
}

//  void QQuick3DPrincipledMaterial::setOcclusionAmount(float
//      occlusionAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial18setOcclusionAmountEf(
    QQuick3DPrincipledMaterial *self,
    float occlusionAmount) {
  self->setOcclusionAmount(occlusionAmount);
}

//  void QQuick3DPrincipledMaterial::setAlphaMode(QQuick3DPrincipledMaterial:
//      :AlphaMode alphaMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12setAlphaModeENS_9AlphaModeE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DPrincipledMaterial::AlphaMode alphaMode) {
  self->setAlphaMode(alphaMode);
}

//  void QQuick3DPrincipledMaterial::setAlphaCutoff(float alphaCutoff)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial14setAlphaCutoffEf(
    QQuick3DPrincipledMaterial *self,
    float alphaCutoff) {
  self->setAlphaCutoff(alphaCutoff);
}

//  void QQuick3DPrincipledMaterial::setMetalnessChannel(QQuick3DMaterial::Te
//      xtureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial19setMetalnessChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setMetalnessChannel(channel);
}

//  void QQuick3DPrincipledMaterial::setRoughnessChannel(QQuick3DMaterial::Te
//      xtureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial19setRoughnessChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setRoughnessChannel(channel);
}

//  void QQuick3DPrincipledMaterial::setOpacityChannel(QQuick3DMaterial::Text
//      ureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial17setOpacityChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setOpacityChannel(channel);
}

//  void QQuick3DPrincipledMaterial::setOcclusionChannel(QQuick3DMaterial::Te
//      xtureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial19setOcclusionChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setOcclusionChannel(channel);
}

//  void QQuick3DPrincipledMaterial::setPointSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12setPointSizeEf(
    QQuick3DPrincipledMaterial *self,
    float size) {
  self->setPointSize(size);
}

//  void QQuick3DPrincipledMaterial::setLineWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12setLineWidthEf(
    QQuick3DPrincipledMaterial *self,
    float width) {
  self->setLineWidth(width);
}

//  void QQuick3DPrincipledMaterial::setHeightMap(QQuick3DTexture *heightMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12setHeightMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *heightMap) {
  self->setHeightMap(heightMap);
}

//  void QQuick3DPrincipledMaterial::setHeightChannel(QQuick3DMaterial::Textu
//      reChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial16setHeightChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setHeightChannel(channel);
}

//  void QQuick3DPrincipledMaterial::setHeightAmount(float heightAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setHeightAmountEf(
    QQuick3DPrincipledMaterial *self,
    float heightAmount) {
  self->setHeightAmount(heightAmount);
}

//  void QQuick3DPrincipledMaterial::setMinHeightMapSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial22setMinHeightMapSamplesEi(
    QQuick3DPrincipledMaterial *self,
    int samples) {
  self->setMinHeightMapSamples(samples);
}

//  void QQuick3DPrincipledMaterial::setMaxHeightMapSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial22setMaxHeightMapSamplesEi(
    QQuick3DPrincipledMaterial *self,
    int samples) {
  self->setMaxHeightMapSamples(samples);
}

//  void QQuick3DPrincipledMaterial::setClearcoatAmount(float
//      newClearcoatAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial18setClearcoatAmountEf(
    QQuick3DPrincipledMaterial *self,
    float newClearcoatAmount) {
  self->setClearcoatAmount(newClearcoatAmount);
}

//  void QQuick3DPrincipledMaterial::setClearcoatMap(QQuick3DTexture
//      *newClearcoatMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setClearcoatMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *newClearcoatMap) {
  self->setClearcoatMap(newClearcoatMap);
}

//  void QQuick3DPrincipledMaterial::setClearcoatChannel(QQuick3DMaterial::Te
//      xtureChannelMapping newClearcoatChannel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial19setClearcoatChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping newClearcoatChannel) {
  self->setClearcoatChannel(newClearcoatChannel);
}

//  void QQuick3DPrincipledMaterial::setClearcoatRoughnessAmount(float
//      newClearcoatRoughnessAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial27setClearcoatRoughnessAmountEf(
    QQuick3DPrincipledMaterial *self,
    float newClearcoatRoughnessAmount) {
  self->setClearcoatRoughnessAmount(newClearcoatRoughnessAmount);
}

//  void QQuick3DPrincipledMaterial::setClearcoatRoughnessChannel(QQuick3DMat
//      erial::TextureChannelMapping newClearcoatRoughnessChannel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial28setClearcoatRoughnessChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping newClearcoatRoughnessChannel) {
  self->setClearcoatRoughnessChannel(newClearcoatRoughnessChannel);
}

//  void QQuick3DPrincipledMaterial::setClearcoatRoughnessMap(QQuick3DTexture
//      *newClearcoatRoughnessMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial24setClearcoatRoughnessMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *newClearcoatRoughnessMap) {
  self->setClearcoatRoughnessMap(newClearcoatRoughnessMap);
}

//  void QQuick3DPrincipledMaterial::setClearcoatNormalMap(QQuick3DTexture
//      *newClearcoatNormalMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial21setClearcoatNormalMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *newClearcoatNormalMap) {
  self->setClearcoatNormalMap(newClearcoatNormalMap);
}

//  void QQuick3DPrincipledMaterial::setClearcoatNormalStrength(float
//      clearcoatNormalStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial26setClearcoatNormalStrengthEf(
    QQuick3DPrincipledMaterial *self,
    float clearcoatNormalStrength) {
  self->setClearcoatNormalStrength(clearcoatNormalStrength);
}

//  void QQuick3DPrincipledMaterial::setTransmissionFactor(float
//      newTransmissionFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial21setTransmissionFactorEf(
    QQuick3DPrincipledMaterial *self,
    float newTransmissionFactor) {
  self->setTransmissionFactor(newTransmissionFactor);
}

//  void QQuick3DPrincipledMaterial::setTransmissionMap(QQuick3DTexture
//      *newTransmissionMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial18setTransmissionMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *newTransmissionMap) {
  self->setTransmissionMap(newTransmissionMap);
}

//  void QQuick3DPrincipledMaterial::setTransmissionChannel(QQuick3DMaterial:
//      :TextureChannelMapping newTransmissionChannel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial22setTransmissionChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DMaterial::TextureChannelMapping newTransmissionChannel) {
  self->setTransmissionChannel(newTransmissionChannel);
}

//  void QQuick3DPrincipledMaterial::setThicknessFactor(float
//      newThicknessFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial18setThicknessFactorEf(
    QQuick3DPrincipledMaterial *self,
    float newThicknessFactor) {
  self->setThicknessFactor(newThicknessFactor);
}

//  void QQuick3DPrincipledMaterial::setThicknessMap(QQuick3DTexture
//      *newThicknessMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setThicknessMapEP15QQuick3DTexture(
    QQuick3DPrincipledMaterial *self,
    QQuick3DTexture *newThicknessMap) {
  self->setThicknessMap(newThicknessMap);
}

//  void QQuick3DPrincipledMaterial::setAttenuationDistance(float
//      newAttenuationDistance)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial22setAttenuationDistanceEf(
    QQuick3DPrincipledMaterial *self,
    float newAttenuationDistance) {
  self->setAttenuationDistance(newAttenuationDistance);
}

//  void QQuick3DPrincipledMaterial::setAttenuationColor(const QColor
//      &newAttenuationColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial19setAttenuationColorERK6QColor(
    QQuick3DPrincipledMaterial *self,
    const QColor *newAttenuationColor) {
  self->setAttenuationColor(*newAttenuationColor);
}

//  void QQuick3DPrincipledMaterial::setIndexOfRefraction(float
//      indexOfRefraction)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial20setIndexOfRefractionEf(
    QQuick3DPrincipledMaterial *self,
    float indexOfRefraction) {
  self->setIndexOfRefraction(indexOfRefraction);
}

//  void QQuick3DPrincipledMaterial::setFresnelScaleBiasEnabled(bool
//      fresnelScaleBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial26setFresnelScaleBiasEnabledEb(
    QQuick3DPrincipledMaterial *self,
    bool fresnelScaleBias) {
  self->setFresnelScaleBiasEnabled(fresnelScaleBias);
}

//  void QQuick3DPrincipledMaterial::setFresnelScale(float fresnelScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setFresnelScaleEf(
    QQuick3DPrincipledMaterial *self,
    float fresnelScale) {
  self->setFresnelScale(fresnelScale);
}

//  void QQuick3DPrincipledMaterial::setFresnelBias(float fresnelBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial14setFresnelBiasEf(
    QQuick3DPrincipledMaterial *self,
    float fresnelBias) {
  self->setFresnelBias(fresnelBias);
}

//  void QQuick3DPrincipledMaterial::setFresnelPower(float fresnelPower)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial15setFresnelPowerEf(
    QQuick3DPrincipledMaterial *self,
    float fresnelPower) {
  self->setFresnelPower(fresnelPower);
}

//  void QQuick3DPrincipledMaterial::setClearcoatFresnelScaleBiasEnabled(bool
//      clearcoatFresnelScaleBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial35setClearcoatFresnelScaleBiasEnabledEb(
    QQuick3DPrincipledMaterial *self,
    bool clearcoatFresnelScaleBias) {
  self->setClearcoatFresnelScaleBiasEnabled(clearcoatFresnelScaleBias);
}

//  void QQuick3DPrincipledMaterial::setClearcoatFresnelScale(float
//      clearcoatFresnelScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial24setClearcoatFresnelScaleEf(
    QQuick3DPrincipledMaterial *self,
    float clearcoatFresnelScale) {
  self->setClearcoatFresnelScale(clearcoatFresnelScale);
}

//  void QQuick3DPrincipledMaterial::setClearcoatFresnelBias(float
//      clearcoatFresnelBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial23setClearcoatFresnelBiasEf(
    QQuick3DPrincipledMaterial *self,
    float clearcoatFresnelBias) {
  self->setClearcoatFresnelBias(clearcoatFresnelBias);
}

//  void QQuick3DPrincipledMaterial::setClearcoatFresnelPower(float
//      clearcoatFresnelPower)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial24setClearcoatFresnelPowerEf(
    QQuick3DPrincipledMaterial *self,
    float clearcoatFresnelPower) {
  self->setClearcoatFresnelPower(clearcoatFresnelPower);
}

//  void QQuick3DPrincipledMaterial::setVertexColorsEnabled(bool
//      vertexColorsEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial22setVertexColorsEnabledEb(
    QQuick3DPrincipledMaterial *self,
    bool vertexColorsEnabled) {
  self->setVertexColorsEnabled(vertexColorsEnabled);
}

//  void QQuick3DPrincipledMaterial::setVertexColorsMaskEnabled(bool
//      vertexColorsMaskEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial26setVertexColorsMaskEnabledEb(
    QQuick3DPrincipledMaterial *self,
    bool vertexColorsMaskEnabled) {
  self->setVertexColorsMaskEnabled(vertexColorsMaskEnabled);
}

//  void
//      QQuick3DPrincipledMaterial::setVertexColorRedMask(VertexColorMaskFlag
//      s vertexColorRedMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial21setVertexColorRedMaskE6QFlagsINS_15VertexColorMaskEE(
    QQuick3DPrincipledMaterial *self,
    int vertexColorRedMask) {
  self->setVertexColorRedMask(
      QFlags<QQuick3DPrincipledMaterial::VertexColorMask>::fromInt(vertexColorRedMask));
}

//  void
//      QQuick3DPrincipledMaterial::setVertexColorGreenMask(VertexColorMaskFl
//      ags vertexColorGreenMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial23setVertexColorGreenMaskE6QFlagsINS_15VertexColorMaskEE(
    QQuick3DPrincipledMaterial *self,
    int vertexColorGreenMask) {
  self->setVertexColorGreenMask(
      QFlags<QQuick3DPrincipledMaterial::VertexColorMask>::fromInt(vertexColorGreenMask));
}

//  void
//      QQuick3DPrincipledMaterial::setVertexColorBlueMask(VertexColorMaskFla
//      gs vertexColorBlueMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial22setVertexColorBlueMaskE6QFlagsINS_15VertexColorMaskEE(
    QQuick3DPrincipledMaterial *self,
    int vertexColorBlueMask) {
  self->setVertexColorBlueMask(
      QFlags<QQuick3DPrincipledMaterial::VertexColorMask>::fromInt(vertexColorBlueMask));
}

//  void
//      QQuick3DPrincipledMaterial::setVertexColorAlphaMask(VertexColorMaskFl
//      ags vertexColorAlphaMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial23setVertexColorAlphaMaskE6QFlagsINS_15VertexColorMaskEE(
    QQuick3DPrincipledMaterial *self,
    int vertexColorAlphaMask) {
  self->setVertexColorAlphaMask(
      QFlags<QQuick3DPrincipledMaterial::VertexColorMask>::fromInt(vertexColorAlphaMask));
}

//  QSSGRenderGraphObject
//      *QQuick3DPrincipledMaterial::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN26QQuick3DPrincipledMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DPrincipledMaterial *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DPrincipledMaterial::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial12markAllDirtyEv(
    QQuick3DPrincipledMaterial *self) {
  self->markAllDirty();
}

//  void QQuick3DPrincipledMaterial::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DPrincipledMaterial::updateSceneManager(QQuick3DSceneManager
//      *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DPrincipledMaterial *self,
    QQuick3DSceneManager *window) {
  self->updateSceneManager(window);
}

//  void QQuick3DPrincipledMaterial::markDirty(DirtyType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DPrincipledMaterial9markDirtyENS_9DirtyTypeE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DPrincipledMaterial::DirtyType type) {
  self->markDirty(type);
}

//  float QQuick3DPrincipledMaterial::ensureNormalized(float val)
extern "C" Q_DECL_EXPORT
float ritual_ZN26QQuick3DPrincipledMaterial16ensureNormalizedEf(float val) {
  return QQuick3DPrincipledMaterial::ensureNormalized(val);
}

//  a Python function taken by a CuteQQuick3DPrincipledMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DPrincipledMaterial(
    QQuick3DPrincipledMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DPrincipledMaterial *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DPrincipledMaterial::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN26QQuick3DPrincipledMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DPrincipledMaterial *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DPrincipledMaterial *>(self)->OwnQQuick3DPrincipledMaterial::updateSpatialNode(
      node);
}

//  void QQuick3DPrincipledMaterial::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuick3DPrincipledMaterial12markAllDirtyEv(
    QQuick3DPrincipledMaterial *self) {
  static_cast<OwnQQuick3DPrincipledMaterial *>(self)->OwnQQuick3DPrincipledMaterial::markAllDirty();
}

//  void QQuick3DPrincipledMaterial::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuick3DPrincipledMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DPrincipledMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DPrincipledMaterial *>(self)->OwnQQuick3DPrincipledMaterial::itemChange(
      a0,
      *a1);
}
