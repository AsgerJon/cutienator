//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dspecularglossymaterial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dspecularglossymaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DSpecularGlossyMaterial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DSpecularGlossyMaterial : QQuick3DSpecularGlossyMaterial {
  using QQuick3DSpecularGlossyMaterial::updateSpatialNode;
  using QQuick3DSpecularGlossyMaterial::markAllDirty;
  using QQuick3DSpecularGlossyMaterial::itemChange;
};

//  A QQuick3DSpecularGlossyMaterial that Python can take functions over in. Every QQuick3DSpecularGlossyMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DSpecularGlossyMaterialCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall1)(const void *, int *);
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall3)(const void *, int *);
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall4)(const void *, int *);
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSpecularGlossyMaterialCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSpecularGlossyMaterialCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpecularGlossyMaterialCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DSpecularGlossyMaterial : public QQuick3DSpecularGlossyMaterial {
public:
  using QQuick3DSpecularGlossyMaterial::QQuick3DSpecularGlossyMaterial;
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

  //  QSSGRenderGraphObject *QQuick3DSpecularGlossyMaterial::updateSpatialN
  //      ode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DSpecularGlossyMaterialCall0 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DSpecularGlossyMaterial::updateSpatialNode(node);
  }

  //  void QQuick3DSpecularGlossyMaterial::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DSpecularGlossyMaterialCall1 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DSpecularGlossyMaterial::markAllDirty();
  }

  //  void QQuick3DSpecularGlossyMaterial::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DSpecularGlossyMaterialCall2 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DSpecularGlossyMaterial::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DSpecularGlossyMaterialCall3 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DSpecularGlossyMaterialCall4 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DSpecularGlossyMaterialCall5 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall5>(taken[5]);
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
      CuteQQuick3DSpecularGlossyMaterialCall6 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall6>(taken[6]);
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
      CuteQQuick3DSpecularGlossyMaterialCall7 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall7>(taken[7]);
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
      CuteQQuick3DSpecularGlossyMaterialCall8 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall8>(taken[8]);
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
      CuteQQuick3DSpecularGlossyMaterialCall9 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall9>(taken[9]);
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
      CuteQQuick3DSpecularGlossyMaterialCall10 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall10>(taken[10]);
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
      CuteQQuick3DSpecularGlossyMaterialCall11 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall11>(taken[11]);
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
      CuteQQuick3DSpecularGlossyMaterialCall12 call = reinterpret_cast<CuteQQuick3DSpecularGlossyMaterialCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DSpecularGlossyMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QQuick3DSpecularGlossyMaterial10metaObjectEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->metaObject();
}

//  void *QQuick3DSpecularGlossyMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QQuick3DSpecularGlossyMaterial11qt_metacastEPKc(
    QQuick3DSpecularGlossyMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DSpecularGlossyMaterial::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QQuick3DSpecularGlossyMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DSpecularGlossyMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DSpecularGlossyMaterial::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQuick3DSpecularGlossyMaterial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DSpecularGlossyMaterial::tr(s, c, n));
}

//  QQuick3DSpecularGlossyMaterial::QQuick3DSpecularGlossyMaterial(QQuick3DOb
//      ject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DSpecularGlossyMaterial *ritual_ZN30QQuick3DSpecularGlossyMaterialC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DSpecularGlossyMaterial(parent);
}

//  QQuick3DSpecularGlossyMaterial::~QQuick3DSpecularGlossyMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterialD1Ev(
    QQuick3DSpecularGlossyMaterial *self) {
  delete self;
}

//  Lighting QQuick3DSpecularGlossyMaterial::lighting() const
extern "C" Q_DECL_EXPORT
QQuick3DSpecularGlossyMaterial::Lighting ritual_ZNK30QQuick3DSpecularGlossyMaterial8lightingEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->lighting();
}

//  BlendMode QQuick3DSpecularGlossyMaterial::blendMode() const
extern "C" Q_DECL_EXPORT
QQuick3DSpecularGlossyMaterial::BlendMode ritual_ZNK30QQuick3DSpecularGlossyMaterial9blendModeEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->blendMode();
}

//  QColor QQuick3DSpecularGlossyMaterial::albedoColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK30QQuick3DSpecularGlossyMaterial11albedoColorEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return new QColor(self->albedoColor());
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::albedoMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial9albedoMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->albedoMap();
}

//  bool QQuick3DSpecularGlossyMaterial::albedoSingleChannelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DSpecularGlossyMaterial26albedoSingleChannelEnabledEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->albedoSingleChannelEnabled();
}

//  TextureChannelMapping QQuick3DSpecularGlossyMaterial::albedoChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial13albedoChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->albedoChannel();
}

//  bool QQuick3DSpecularGlossyMaterial::specularSingleChannelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DSpecularGlossyMaterial28specularSingleChannelEnabledEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->specularSingleChannelEnabled();
}

//  TextureChannelMapping QQuick3DSpecularGlossyMaterial::specularChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial15specularChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->specularChannel();
}

//  bool QQuick3DSpecularGlossyMaterial::emissiveSingleChannelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DSpecularGlossyMaterial28emissiveSingleChannelEnabledEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->emissiveSingleChannelEnabled();
}

//  TextureChannelMapping QQuick3DSpecularGlossyMaterial::emissiveChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial15emissiveChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->emissiveChannel();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::emissiveMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial11emissiveMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->emissiveMap();
}

//  QVector3D QQuick3DSpecularGlossyMaterial::emissiveFactor() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK30QQuick3DSpecularGlossyMaterial14emissiveFactorEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return new QVector3D(self->emissiveFactor());
}

//  float QQuick3DSpecularGlossyMaterial::glossiness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial10glossinessEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->glossiness();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::glossinessMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial13glossinessMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->glossinessMap();
}

//  bool QQuick3DSpecularGlossyMaterial::invertOpacityMapValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DSpecularGlossyMaterial21invertOpacityMapValueEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->invertOpacityMapValue();
}

//  float QQuick3DSpecularGlossyMaterial::opacity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial7opacityEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->opacity();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::opacityMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial10opacityMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->opacityMap();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::normalMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial9normalMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->normalMap();
}

//  QColor QQuick3DSpecularGlossyMaterial::specularColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK30QQuick3DSpecularGlossyMaterial13specularColorEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return new QColor(self->specularColor());
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::specularMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial11specularMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->specularMap();
}

//  float QQuick3DSpecularGlossyMaterial::normalStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial14normalStrengthEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->normalStrength();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::occlusionMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial12occlusionMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->occlusionMap();
}

//  float QQuick3DSpecularGlossyMaterial::occlusionAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial15occlusionAmountEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->occlusionAmount();
}

//  AlphaMode QQuick3DSpecularGlossyMaterial::alphaMode() const
extern "C" Q_DECL_EXPORT
QQuick3DSpecularGlossyMaterial::AlphaMode ritual_ZNK30QQuick3DSpecularGlossyMaterial9alphaModeEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->alphaMode();
}

//  float QQuick3DSpecularGlossyMaterial::alphaCutoff() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial11alphaCutoffEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->alphaCutoff();
}

//  TextureChannelMapping QQuick3DSpecularGlossyMaterial::glossinessChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial17glossinessChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->glossinessChannel();
}

//  TextureChannelMapping QQuick3DSpecularGlossyMaterial::opacityChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial14opacityChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->opacityChannel();
}

//  TextureChannelMapping QQuick3DSpecularGlossyMaterial::occlusionChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial16occlusionChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->occlusionChannel();
}

//  float QQuick3DSpecularGlossyMaterial::pointSize() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial9pointSizeEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->pointSize();
}

//  float QQuick3DSpecularGlossyMaterial::lineWidth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial9lineWidthEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->lineWidth();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::heightMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial9heightMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->heightMap();
}

//  TextureChannelMapping QQuick3DSpecularGlossyMaterial::heightChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial13heightChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->heightChannel();
}

//  float QQuick3DSpecularGlossyMaterial::heightAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial12heightAmountEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->heightAmount();
}

//  int QQuick3DSpecularGlossyMaterial::minHeightMapSamples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DSpecularGlossyMaterial19minHeightMapSamplesEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->minHeightMapSamples();
}

//  int QQuick3DSpecularGlossyMaterial::maxHeightMapSamples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DSpecularGlossyMaterial19maxHeightMapSamplesEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->maxHeightMapSamples();
}

//  float QQuick3DSpecularGlossyMaterial::clearcoatAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial15clearcoatAmountEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatAmount();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::clearcoatMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial12clearcoatMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatMap();
}

//  TextureChannelMapping QQuick3DSpecularGlossyMaterial::clearcoatChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial16clearcoatChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatChannel();
}

//  float QQuick3DSpecularGlossyMaterial::clearcoatRoughnessAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial24clearcoatRoughnessAmountEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatRoughnessAmount();
}

//  TextureChannelMapping
//      QQuick3DSpecularGlossyMaterial::clearcoatRoughnessChannel() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial25clearcoatRoughnessChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatRoughnessChannel();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::clearcoatRoughnessMap()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial21clearcoatRoughnessMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatRoughnessMap();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::clearcoatNormalMap()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial18clearcoatNormalMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatNormalMap();
}

//  float QQuick3DSpecularGlossyMaterial::transmissionFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial18transmissionFactorEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->transmissionFactor();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::transmissionMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial15transmissionMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->transmissionMap();
}

//  TextureChannelMapping
//      QQuick3DSpecularGlossyMaterial::transmissionChannel() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial19transmissionChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->transmissionChannel();
}

//  float QQuick3DSpecularGlossyMaterial::thicknessFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial15thicknessFactorEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->thicknessFactor();
}

//  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::thicknessMap() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DSpecularGlossyMaterial12thicknessMapEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->thicknessMap();
}

//  TextureChannelMapping QQuick3DSpecularGlossyMaterial::thicknessChannel()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial::TextureChannelMapping ritual_ZNK30QQuick3DSpecularGlossyMaterial16thicknessChannelEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->thicknessChannel();
}

//  float QQuick3DSpecularGlossyMaterial::attenuationDistance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial19attenuationDistanceEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->attenuationDistance();
}

//  QColor QQuick3DSpecularGlossyMaterial::attenuationColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK30QQuick3DSpecularGlossyMaterial16attenuationColorEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return new QColor(self->attenuationColor());
}

//  bool QQuick3DSpecularGlossyMaterial::fresnelScaleBiasEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DSpecularGlossyMaterial23fresnelScaleBiasEnabledEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->fresnelScaleBiasEnabled();
}

//  float QQuick3DSpecularGlossyMaterial::fresnelScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial12fresnelScaleEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->fresnelScale();
}

//  float QQuick3DSpecularGlossyMaterial::fresnelBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial11fresnelBiasEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->fresnelBias();
}

//  float QQuick3DSpecularGlossyMaterial::fresnelPower() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial12fresnelPowerEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->fresnelPower();
}

//  bool QQuick3DSpecularGlossyMaterial::clearcoatFresnelScaleBiasEnabled()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DSpecularGlossyMaterial32clearcoatFresnelScaleBiasEnabledEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatFresnelScaleBiasEnabled();
}

//  float QQuick3DSpecularGlossyMaterial::clearcoatFresnelScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial21clearcoatFresnelScaleEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatFresnelScale();
}

//  float QQuick3DSpecularGlossyMaterial::clearcoatFresnelBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial20clearcoatFresnelBiasEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatFresnelBias();
}

//  float QQuick3DSpecularGlossyMaterial::clearcoatFresnelPower() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial21clearcoatFresnelPowerEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatFresnelPower();
}

//  bool QQuick3DSpecularGlossyMaterial::vertexColorsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DSpecularGlossyMaterial19vertexColorsEnabledEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->vertexColorsEnabled();
}

//  float QQuick3DSpecularGlossyMaterial::clearcoatNormalStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DSpecularGlossyMaterial23clearcoatNormalStrengthEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->clearcoatNormalStrength();
}

//  bool QQuick3DSpecularGlossyMaterial::vertexColorsMaskEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DSpecularGlossyMaterial23vertexColorsMaskEnabledEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return self->vertexColorsMaskEnabled();
}

//  VertexColorMaskFlags QQuick3DSpecularGlossyMaterial::vertexColorRedMask()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DSpecularGlossyMaterial18vertexColorRedMaskEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return static_cast<int>(self->vertexColorRedMask().toInt());
}

//  VertexColorMaskFlags
//      QQuick3DSpecularGlossyMaterial::vertexColorGreenMask() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DSpecularGlossyMaterial20vertexColorGreenMaskEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return static_cast<int>(self->vertexColorGreenMask().toInt());
}

//  VertexColorMaskFlags
//      QQuick3DSpecularGlossyMaterial::vertexColorBlueMask() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DSpecularGlossyMaterial19vertexColorBlueMaskEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return static_cast<int>(self->vertexColorBlueMask().toInt());
}

//  VertexColorMaskFlags
//      QQuick3DSpecularGlossyMaterial::vertexColorAlphaMask() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DSpecularGlossyMaterial20vertexColorAlphaMaskEv(
    const QQuick3DSpecularGlossyMaterial *self) {
  return static_cast<int>(self->vertexColorAlphaMask().toInt());
}

//  void QQuick3DSpecularGlossyMaterial::setLighting(QQuick3DSpecularGlossyMa
//      terial::Lighting lighting)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial11setLightingENS_8LightingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DSpecularGlossyMaterial::Lighting lighting) {
  self->setLighting(lighting);
}

//  void QQuick3DSpecularGlossyMaterial::setBlendMode(QQuick3DSpecularGlossyM
//      aterial::BlendMode blendMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial12setBlendModeENS_9BlendModeE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DSpecularGlossyMaterial::BlendMode blendMode) {
  self->setBlendMode(blendMode);
}

//  void QQuick3DSpecularGlossyMaterial::setAlbedoColor(const QColor &albedo)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial14setAlbedoColorERK6QColor(
    QQuick3DSpecularGlossyMaterial *self,
    const QColor *albedo) {
  self->setAlbedoColor(*albedo);
}

//  void QQuick3DSpecularGlossyMaterial::setAlbedoMap(QQuick3DTexture
//      *albedoMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial12setAlbedoMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *albedoMap) {
  self->setAlbedoMap(albedoMap);
}

//  void QQuick3DSpecularGlossyMaterial::setAlbedoSingleChannelEnabled(bool
//      albedoSingleChannelEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial29setAlbedoSingleChannelEnabledEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool albedoSingleChannelEnabled) {
  self->setAlbedoSingleChannelEnabled(albedoSingleChannelEnabled);
}

//  void QQuick3DSpecularGlossyMaterial::setAlbedoChannel(QQuick3DMaterial::T
//      extureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16setAlbedoChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setAlbedoChannel(channel);
}

//  void QQuick3DSpecularGlossyMaterial::setSpecularSingleChannelEnabled(bool
//      specularSingleChannelEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial31setSpecularSingleChannelEnabledEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool specularSingleChannelEnabled) {
  self->setSpecularSingleChannelEnabled(specularSingleChannelEnabled);
}

//  void QQuick3DSpecularGlossyMaterial::setSpecularChannel(QQuick3DMaterial:
//      :TextureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18setSpecularChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setSpecularChannel(channel);
}

//  void QQuick3DSpecularGlossyMaterial::setEmissiveSingleChannelEnabled(bool
//      emissiveSingleChannelEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial31setEmissiveSingleChannelEnabledEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool emissiveSingleChannelEnabled) {
  self->setEmissiveSingleChannelEnabled(emissiveSingleChannelEnabled);
}

//  void QQuick3DSpecularGlossyMaterial::setEmissiveChannel(QQuick3DMaterial:
//      :TextureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18setEmissiveChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setEmissiveChannel(channel);
}

//  void QQuick3DSpecularGlossyMaterial::setEmissiveMap(QQuick3DTexture
//      *emissiveMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial14setEmissiveMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *emissiveMap) {
  self->setEmissiveMap(emissiveMap);
}

//  void QQuick3DSpecularGlossyMaterial::setEmissiveFactor(const QVector3D
//      &emissiveFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial17setEmissiveFactorERK9QVector3D(
    QQuick3DSpecularGlossyMaterial *self,
    const QVector3D *emissiveFactor) {
  self->setEmissiveFactor(*emissiveFactor);
}

//  void QQuick3DSpecularGlossyMaterial::setGlossiness(float glossiness)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial13setGlossinessEf(
    QQuick3DSpecularGlossyMaterial *self,
    float glossiness) {
  self->setGlossiness(glossiness);
}

//  void QQuick3DSpecularGlossyMaterial::setGlossinessMap(QQuick3DTexture
//      *glossinessMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16setGlossinessMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *glossinessMap) {
  self->setGlossinessMap(glossinessMap);
}

//  void QQuick3DSpecularGlossyMaterial::setInvertOpacityMapValue(bool
//      invertOpacityMapValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial24setInvertOpacityMapValueEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool invertOpacityMapValue) {
  self->setInvertOpacityMapValue(invertOpacityMapValue);
}

//  void QQuick3DSpecularGlossyMaterial::setOpacity(float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial10setOpacityEf(
    QQuick3DSpecularGlossyMaterial *self,
    float opacity) {
  self->setOpacity(opacity);
}

//  void QQuick3DSpecularGlossyMaterial::setOpacityMap(QQuick3DTexture
//      *opacityMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial13setOpacityMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *opacityMap) {
  self->setOpacityMap(opacityMap);
}

//  void QQuick3DSpecularGlossyMaterial::setNormalMap(QQuick3DTexture
//      *normalMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial12setNormalMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *normalMap) {
  self->setNormalMap(normalMap);
}

//  void QQuick3DSpecularGlossyMaterial::setSpecularColor(const QColor
//      &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16setSpecularColorERK6QColor(
    QQuick3DSpecularGlossyMaterial *self,
    const QColor *specular) {
  self->setSpecularColor(*specular);
}

//  void QQuick3DSpecularGlossyMaterial::setSpecularMap(QQuick3DTexture
//      *specularMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial14setSpecularMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *specularMap) {
  self->setSpecularMap(specularMap);
}

//  void QQuick3DSpecularGlossyMaterial::setNormalStrength(float
//      normalStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial17setNormalStrengthEf(
    QQuick3DSpecularGlossyMaterial *self,
    float normalStrength) {
  self->setNormalStrength(normalStrength);
}

//  void QQuick3DSpecularGlossyMaterial::setOcclusionMap(QQuick3DTexture
//      *occlusionMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial15setOcclusionMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *occlusionMap) {
  self->setOcclusionMap(occlusionMap);
}

//  void QQuick3DSpecularGlossyMaterial::setOcclusionAmount(float
//      occlusionAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18setOcclusionAmountEf(
    QQuick3DSpecularGlossyMaterial *self,
    float occlusionAmount) {
  self->setOcclusionAmount(occlusionAmount);
}

//  void QQuick3DSpecularGlossyMaterial::setAlphaMode(QQuick3DSpecularGlossyM
//      aterial::AlphaMode alphaMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial12setAlphaModeENS_9AlphaModeE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DSpecularGlossyMaterial::AlphaMode alphaMode) {
  self->setAlphaMode(alphaMode);
}

//  void QQuick3DSpecularGlossyMaterial::setAlphaCutoff(float alphaCutoff)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial14setAlphaCutoffEf(
    QQuick3DSpecularGlossyMaterial *self,
    float alphaCutoff) {
  self->setAlphaCutoff(alphaCutoff);
}

//  void QQuick3DSpecularGlossyMaterial::setGlossinessChannel(QQuick3DMateria
//      l::TextureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial20setGlossinessChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setGlossinessChannel(channel);
}

//  void QQuick3DSpecularGlossyMaterial::setOpacityChannel(QQuick3DMaterial::
//      TextureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial17setOpacityChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setOpacityChannel(channel);
}

//  void QQuick3DSpecularGlossyMaterial::setOcclusionChannel(QQuick3DMaterial
//      ::TextureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19setOcclusionChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setOcclusionChannel(channel);
}

//  void QQuick3DSpecularGlossyMaterial::setPointSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial12setPointSizeEf(
    QQuick3DSpecularGlossyMaterial *self,
    float size) {
  self->setPointSize(size);
}

//  void QQuick3DSpecularGlossyMaterial::setLineWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial12setLineWidthEf(
    QQuick3DSpecularGlossyMaterial *self,
    float width) {
  self->setLineWidth(width);
}

//  void QQuick3DSpecularGlossyMaterial::setHeightMap(QQuick3DTexture
//      *heightMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial12setHeightMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *heightMap) {
  self->setHeightMap(heightMap);
}

//  void QQuick3DSpecularGlossyMaterial::setHeightChannel(QQuick3DMaterial::T
//      extureChannelMapping channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16setHeightChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping channel) {
  self->setHeightChannel(channel);
}

//  void QQuick3DSpecularGlossyMaterial::setHeightAmount(float heightAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial15setHeightAmountEf(
    QQuick3DSpecularGlossyMaterial *self,
    float heightAmount) {
  self->setHeightAmount(heightAmount);
}

//  void QQuick3DSpecularGlossyMaterial::setMinHeightMapSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22setMinHeightMapSamplesEi(
    QQuick3DSpecularGlossyMaterial *self,
    int samples) {
  self->setMinHeightMapSamples(samples);
}

//  void QQuick3DSpecularGlossyMaterial::setMaxHeightMapSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22setMaxHeightMapSamplesEi(
    QQuick3DSpecularGlossyMaterial *self,
    int samples) {
  self->setMaxHeightMapSamples(samples);
}

//  void QQuick3DSpecularGlossyMaterial::setClearcoatAmount(float
//      newClearcoatAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18setClearcoatAmountEf(
    QQuick3DSpecularGlossyMaterial *self,
    float newClearcoatAmount) {
  self->setClearcoatAmount(newClearcoatAmount);
}

//  void QQuick3DSpecularGlossyMaterial::setClearcoatMap(QQuick3DTexture
//      *newClearcoatMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial15setClearcoatMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *newClearcoatMap) {
  self->setClearcoatMap(newClearcoatMap);
}

//  void QQuick3DSpecularGlossyMaterial::setClearcoatChannel(QQuick3DMaterial
//      ::TextureChannelMapping newClearcoatChannel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19setClearcoatChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping newClearcoatChannel) {
  self->setClearcoatChannel(newClearcoatChannel);
}

//  void QQuick3DSpecularGlossyMaterial::setClearcoatRoughnessAmount(float
//      newClearcoatRoughnessAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial27setClearcoatRoughnessAmountEf(
    QQuick3DSpecularGlossyMaterial *self,
    float newClearcoatRoughnessAmount) {
  self->setClearcoatRoughnessAmount(newClearcoatRoughnessAmount);
}

//  void QQuick3DSpecularGlossyMaterial::setClearcoatRoughnessChannel(QQuick3
//      DMaterial::TextureChannelMapping newClearcoatRoughnessChannel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial28setClearcoatRoughnessChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping newClearcoatRoughnessChannel) {
  self->setClearcoatRoughnessChannel(newClearcoatRoughnessChannel);
}

//  void
//      QQuick3DSpecularGlossyMaterial::setClearcoatRoughnessMap(QQuick3DText
//      ure *newClearcoatRoughnessMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial24setClearcoatRoughnessMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *newClearcoatRoughnessMap) {
  self->setClearcoatRoughnessMap(newClearcoatRoughnessMap);
}

//  void
//      QQuick3DSpecularGlossyMaterial::setClearcoatNormalMap(QQuick3DTexture
//      *newClearcoatNormalMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial21setClearcoatNormalMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *newClearcoatNormalMap) {
  self->setClearcoatNormalMap(newClearcoatNormalMap);
}

//  void QQuick3DSpecularGlossyMaterial::setClearcoatNormalStrength(float
//      newClearcoatNormalStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial26setClearcoatNormalStrengthEf(
    QQuick3DSpecularGlossyMaterial *self,
    float newClearcoatNormalStrength) {
  self->setClearcoatNormalStrength(newClearcoatNormalStrength);
}

//  void QQuick3DSpecularGlossyMaterial::setTransmissionFactor(float
//      newTransmissionFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial21setTransmissionFactorEf(
    QQuick3DSpecularGlossyMaterial *self,
    float newTransmissionFactor) {
  self->setTransmissionFactor(newTransmissionFactor);
}

//  void QQuick3DSpecularGlossyMaterial::setTransmissionMap(QQuick3DTexture
//      *newTransmissionMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18setTransmissionMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *newTransmissionMap) {
  self->setTransmissionMap(newTransmissionMap);
}

//  void QQuick3DSpecularGlossyMaterial::setTransmissionChannel(QQuick3DMater
//      ial::TextureChannelMapping newTransmissionChannel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22setTransmissionChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping newTransmissionChannel) {
  self->setTransmissionChannel(newTransmissionChannel);
}

//  void QQuick3DSpecularGlossyMaterial::setThicknessFactor(float
//      newThicknessFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18setThicknessFactorEf(
    QQuick3DSpecularGlossyMaterial *self,
    float newThicknessFactor) {
  self->setThicknessFactor(newThicknessFactor);
}

//  void QQuick3DSpecularGlossyMaterial::setThicknessMap(QQuick3DTexture
//      *newThicknessMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial15setThicknessMapEP15QQuick3DTexture(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DTexture *newThicknessMap) {
  self->setThicknessMap(newThicknessMap);
}

//  void QQuick3DSpecularGlossyMaterial::setThicknessChannel(QQuick3DMaterial
//      ::TextureChannelMapping newThicknessChannel)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19setThicknessChannelEN16QQuick3DMaterial21TextureChannelMappingE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DMaterial::TextureChannelMapping newThicknessChannel) {
  self->setThicknessChannel(newThicknessChannel);
}

//  void QQuick3DSpecularGlossyMaterial::setAttenuationDistance(float
//      newAttenuationDistance)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22setAttenuationDistanceEf(
    QQuick3DSpecularGlossyMaterial *self,
    float newAttenuationDistance) {
  self->setAttenuationDistance(newAttenuationDistance);
}

//  void QQuick3DSpecularGlossyMaterial::setAttenuationColor(const QColor
//      &newAttenuationColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19setAttenuationColorERK6QColor(
    QQuick3DSpecularGlossyMaterial *self,
    const QColor *newAttenuationColor) {
  self->setAttenuationColor(*newAttenuationColor);
}

//  void QQuick3DSpecularGlossyMaterial::setFresnelScaleBiasEnabled(bool
//      fresnelScaleBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial26setFresnelScaleBiasEnabledEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool fresnelScaleBias) {
  self->setFresnelScaleBiasEnabled(fresnelScaleBias);
}

//  void QQuick3DSpecularGlossyMaterial::setFresnelScale(float fresnelScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial15setFresnelScaleEf(
    QQuick3DSpecularGlossyMaterial *self,
    float fresnelScale) {
  self->setFresnelScale(fresnelScale);
}

//  void QQuick3DSpecularGlossyMaterial::setFresnelBias(float fresnelBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial14setFresnelBiasEf(
    QQuick3DSpecularGlossyMaterial *self,
    float fresnelBias) {
  self->setFresnelBias(fresnelBias);
}

//  void QQuick3DSpecularGlossyMaterial::setFresnelPower(float fresnelPower)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial15setFresnelPowerEf(
    QQuick3DSpecularGlossyMaterial *self,
    float fresnelPower) {
  self->setFresnelPower(fresnelPower);
}

//  void
//      QQuick3DSpecularGlossyMaterial::setClearcoatFresnelScaleBiasEnabled(b
//      ool clearcoatFresnelScaleBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial35setClearcoatFresnelScaleBiasEnabledEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool clearcoatFresnelScaleBias) {
  self->setClearcoatFresnelScaleBiasEnabled(clearcoatFresnelScaleBias);
}

//  void QQuick3DSpecularGlossyMaterial::setClearcoatFresnelScale(float
//      clearcoatFresnelScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial24setClearcoatFresnelScaleEf(
    QQuick3DSpecularGlossyMaterial *self,
    float clearcoatFresnelScale) {
  self->setClearcoatFresnelScale(clearcoatFresnelScale);
}

//  void QQuick3DSpecularGlossyMaterial::setClearcoatFresnelBias(float
//      clearcoatFresnelBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial23setClearcoatFresnelBiasEf(
    QQuick3DSpecularGlossyMaterial *self,
    float clearcoatFresnelBias) {
  self->setClearcoatFresnelBias(clearcoatFresnelBias);
}

//  void QQuick3DSpecularGlossyMaterial::setClearcoatFresnelPower(float
//      clearcoatFresnelPower)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial24setClearcoatFresnelPowerEf(
    QQuick3DSpecularGlossyMaterial *self,
    float clearcoatFresnelPower) {
  self->setClearcoatFresnelPower(clearcoatFresnelPower);
}

//  void QQuick3DSpecularGlossyMaterial::setVertexColorsEnabled(bool
//      vertexColorsEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22setVertexColorsEnabledEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool vertexColorsEnabled) {
  self->setVertexColorsEnabled(vertexColorsEnabled);
}

//  void QQuick3DSpecularGlossyMaterial::setVertexColorsMaskEnabled(bool
//      vertexColorsMaskEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial26setVertexColorsMaskEnabledEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool vertexColorsMaskEnabled) {
  self->setVertexColorsMaskEnabled(vertexColorsMaskEnabled);
}

//  void QQuick3DSpecularGlossyMaterial::setVertexColorRedMask(VertexColorMas
//      kFlags vertexColorRedMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial21setVertexColorRedMaskE6QFlagsINS_15VertexColorMaskEE(
    QQuick3DSpecularGlossyMaterial *self,
    int vertexColorRedMask) {
  self->setVertexColorRedMask(
      QFlags<QQuick3DSpecularGlossyMaterial::VertexColorMask>::fromInt(vertexColorRedMask));
}

//  void QQuick3DSpecularGlossyMaterial::setVertexColorGreenMask(VertexColorM
//      askFlags vertexColorGreenMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial23setVertexColorGreenMaskE6QFlagsINS_15VertexColorMaskEE(
    QQuick3DSpecularGlossyMaterial *self,
    int vertexColorGreenMask) {
  self->setVertexColorGreenMask(
      QFlags<QQuick3DSpecularGlossyMaterial::VertexColorMask>::fromInt(vertexColorGreenMask));
}

//  void QQuick3DSpecularGlossyMaterial::setVertexColorBlueMask(VertexColorMa
//      skFlags vertexColorBlueMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22setVertexColorBlueMaskE6QFlagsINS_15VertexColorMaskEE(
    QQuick3DSpecularGlossyMaterial *self,
    int vertexColorBlueMask) {
  self->setVertexColorBlueMask(
      QFlags<QQuick3DSpecularGlossyMaterial::VertexColorMask>::fromInt(vertexColorBlueMask));
}

//  void QQuick3DSpecularGlossyMaterial::setVertexColorAlphaMask(VertexColorM
//      askFlags vertexColorAlphaMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial23setVertexColorAlphaMaskE6QFlagsINS_15VertexColorMaskEE(
    QQuick3DSpecularGlossyMaterial *self,
    int vertexColorAlphaMask) {
  self->setVertexColorAlphaMask(
      QFlags<QQuick3DSpecularGlossyMaterial::VertexColorMask>::fromInt(vertexColorAlphaMask));
}

//  void QQuick3DSpecularGlossyMaterial::lightingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial15lightingChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->lightingChanged();
}

//  void QQuick3DSpecularGlossyMaterial::blendModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16blendModeChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->blendModeChanged();
}

//  void QQuick3DSpecularGlossyMaterial::albedoColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18albedoColorChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->albedoColorChanged();
}

//  void QQuick3DSpecularGlossyMaterial::albedoMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16albedoMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->albedoMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::albedoSingleChannelEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial33albedoSingleChannelEnabledChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->albedoSingleChannelEnabledChanged();
}

//  void QQuick3DSpecularGlossyMaterial::albedoChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial20albedoChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->albedoChannelChanged();
}

//  void
//      QQuick3DSpecularGlossyMaterial::specularSingleChannelEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial35specularSingleChannelEnabledChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->specularSingleChannelEnabledChanged();
}

//  void QQuick3DSpecularGlossyMaterial::specularChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22specularChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->specularChannelChanged();
}

//  void
//      QQuick3DSpecularGlossyMaterial::emissiveSingleChannelEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial35emissiveSingleChannelEnabledChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->emissiveSingleChannelEnabledChanged();
}

//  void QQuick3DSpecularGlossyMaterial::emissiveChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22emissiveChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->emissiveChannelChanged();
}

//  void QQuick3DSpecularGlossyMaterial::emissiveMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18emissiveMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->emissiveMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::emissiveFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial21emissiveFactorChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->emissiveFactorChanged();
}

//  void QQuick3DSpecularGlossyMaterial::glossinessChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial17glossinessChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->glossinessChanged();
}

//  void QQuick3DSpecularGlossyMaterial::glossinessMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial20glossinessMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->glossinessMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::invertOpacityMapValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial28invertOpacityMapValueChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->invertOpacityMapValueChanged();
}

//  void QQuick3DSpecularGlossyMaterial::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial14opacityChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->opacityChanged();
}

//  void QQuick3DSpecularGlossyMaterial::opacityMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial17opacityMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->opacityMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::normalMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16normalMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->normalMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::specularColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial20specularColorChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->specularColorChanged();
}

//  void QQuick3DSpecularGlossyMaterial::specularMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18specularMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->specularMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::normalStrengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial21normalStrengthChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->normalStrengthChanged();
}

//  void QQuick3DSpecularGlossyMaterial::occlusionMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19occlusionMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->occlusionMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::occlusionAmountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22occlusionAmountChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->occlusionAmountChanged();
}

//  void QQuick3DSpecularGlossyMaterial::alphaModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16alphaModeChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->alphaModeChanged();
}

//  void QQuick3DSpecularGlossyMaterial::alphaCutoffChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18alphaCutoffChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->alphaCutoffChanged();
}

//  void QQuick3DSpecularGlossyMaterial::glossinessChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial24glossinessChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->glossinessChannelChanged();
}

//  void QQuick3DSpecularGlossyMaterial::opacityChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial21opacityChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->opacityChannelChanged();
}

//  void QQuick3DSpecularGlossyMaterial::occlusionChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial23occlusionChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->occlusionChannelChanged();
}

//  void QQuick3DSpecularGlossyMaterial::pointSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16pointSizeChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->pointSizeChanged();
}

//  void QQuick3DSpecularGlossyMaterial::lineWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16lineWidthChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->lineWidthChanged();
}

//  void QQuick3DSpecularGlossyMaterial::heightMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial16heightMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->heightMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::heightChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial20heightChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->heightChannelChanged();
}

//  void QQuick3DSpecularGlossyMaterial::heightAmountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19heightAmountChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->heightAmountChanged();
}

//  void QQuick3DSpecularGlossyMaterial::minHeightMapSamplesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial26minHeightMapSamplesChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->minHeightMapSamplesChanged();
}

//  void QQuick3DSpecularGlossyMaterial::maxHeightMapSamplesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial26maxHeightMapSamplesChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->maxHeightMapSamplesChanged();
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatAmountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22clearcoatAmountChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->clearcoatAmountChanged();
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19clearcoatMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->clearcoatMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial23clearcoatChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->clearcoatChannelChanged();
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatRoughnessAmountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial31clearcoatRoughnessAmountChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->clearcoatRoughnessAmountChanged();
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatRoughnessChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial32clearcoatRoughnessChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->clearcoatRoughnessChannelChanged();
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatRoughnessMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial28clearcoatRoughnessMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->clearcoatRoughnessMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatNormalMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial25clearcoatNormalMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->clearcoatNormalMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatNormalStrengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial30clearcoatNormalStrengthChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->clearcoatNormalStrengthChanged();
}

//  void QQuick3DSpecularGlossyMaterial::transmissionFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial25transmissionFactorChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->transmissionFactorChanged();
}

//  void QQuick3DSpecularGlossyMaterial::transmissionMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22transmissionMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->transmissionMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::transmissionChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial26transmissionChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->transmissionChannelChanged();
}

//  void QQuick3DSpecularGlossyMaterial::thicknessFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial22thicknessFactorChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->thicknessFactorChanged();
}

//  void QQuick3DSpecularGlossyMaterial::thicknessMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19thicknessMapChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->thicknessMapChanged();
}

//  void QQuick3DSpecularGlossyMaterial::thicknessChannelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial23thicknessChannelChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->thicknessChannelChanged();
}

//  void QQuick3DSpecularGlossyMaterial::attenuationDistanceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial26attenuationDistanceChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->attenuationDistanceChanged();
}

//  void QQuick3DSpecularGlossyMaterial::attenuationColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial23attenuationColorChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->attenuationColorChanged();
}

//  void QQuick3DSpecularGlossyMaterial::vertexColorsEnabledChanged(bool
//      vertexColorsEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial26vertexColorsEnabledChangedEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool vertexColorsEnabled) {
  self->vertexColorsEnabledChanged(vertexColorsEnabled);
}

//  void QQuick3DSpecularGlossyMaterial::fresnelScaleBiasEnabledChanged(bool
//      fresnelScaleBiasEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial30fresnelScaleBiasEnabledChangedEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool fresnelScaleBiasEnabled) {
  self->fresnelScaleBiasEnabledChanged(fresnelScaleBiasEnabled);
}

//  void QQuick3DSpecularGlossyMaterial::fresnelScaleChanged(float
//      fresnelScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19fresnelScaleChangedEf(
    QQuick3DSpecularGlossyMaterial *self,
    float fresnelScale) {
  self->fresnelScaleChanged(fresnelScale);
}

//  void QQuick3DSpecularGlossyMaterial::fresnelBiasChanged(float
//      fresnelBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18fresnelBiasChangedEf(
    QQuick3DSpecularGlossyMaterial *self,
    float fresnelBias) {
  self->fresnelBiasChanged(fresnelBias);
}

//  void QQuick3DSpecularGlossyMaterial::fresnelPowerChanged(float
//      fresnelPower)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial19fresnelPowerChangedEf(
    QQuick3DSpecularGlossyMaterial *self,
    float fresnelPower) {
  self->fresnelPowerChanged(fresnelPower);
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatFresnelScaleBiasEnabledChan
//      ged(bool clearcoatFresnelScaleBiasEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial39clearcoatFresnelScaleBiasEnabledChangedEb(
    QQuick3DSpecularGlossyMaterial *self,
    bool clearcoatFresnelScaleBiasEnabled) {
  self->clearcoatFresnelScaleBiasEnabledChanged(
      clearcoatFresnelScaleBiasEnabled);
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatFresnelScaleChanged(float
//      clearcoatFresnelScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial28clearcoatFresnelScaleChangedEf(
    QQuick3DSpecularGlossyMaterial *self,
    float clearcoatFresnelScale) {
  self->clearcoatFresnelScaleChanged(clearcoatFresnelScale);
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatFresnelBiasChanged(float
//      clearcoatFresnelBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial27clearcoatFresnelBiasChangedEf(
    QQuick3DSpecularGlossyMaterial *self,
    float clearcoatFresnelBias) {
  self->clearcoatFresnelBiasChanged(clearcoatFresnelBias);
}

//  void QQuick3DSpecularGlossyMaterial::clearcoatFresnelPowerChanged(float
//      clearcoatFresnelPower)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial28clearcoatFresnelPowerChangedEf(
    QQuick3DSpecularGlossyMaterial *self,
    float clearcoatFresnelPower) {
  self->clearcoatFresnelPowerChanged(clearcoatFresnelPower);
}

//  void QQuick3DSpecularGlossyMaterial::vertexColorsMaskEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial30vertexColorsMaskEnabledChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->vertexColorsMaskEnabledChanged();
}

//  void QQuick3DSpecularGlossyMaterial::vertexColorRedMaskChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial25vertexColorRedMaskChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->vertexColorRedMaskChanged();
}

//  void QQuick3DSpecularGlossyMaterial::vertexColorGreenMaskChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial27vertexColorGreenMaskChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->vertexColorGreenMaskChanged();
}

//  void QQuick3DSpecularGlossyMaterial::vertexColorBlueMaskChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial26vertexColorBlueMaskChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->vertexColorBlueMaskChanged();
}

//  void QQuick3DSpecularGlossyMaterial::vertexColorAlphaMaskChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial27vertexColorAlphaMaskChangedEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->vertexColorAlphaMaskChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DSpecularGlossyMaterial::updateSpatialNode(QSSGRenderGraphObj
//      ect *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN30QQuick3DSpecularGlossyMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSpecularGlossyMaterial *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DSpecularGlossyMaterial::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial12markAllDirtyEv(
    QQuick3DSpecularGlossyMaterial *self) {
  self->markAllDirty();
}

//  void QQuick3DSpecularGlossyMaterial::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void
//      QQuick3DSpecularGlossyMaterial::updateSceneManager(QQuick3DSceneManag
//      er *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DSceneManager *window) {
  self->updateSceneManager(window);
}

//  void QQuick3DSpecularGlossyMaterial::markDirty(DirtyType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DSpecularGlossyMaterial9markDirtyENS_9DirtyTypeE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DSpecularGlossyMaterial::DirtyType type) {
  self->markDirty(type);
}

//  float QQuick3DSpecularGlossyMaterial::ensureNormalized(float val)
extern "C" Q_DECL_EXPORT
float ritual_ZN30QQuick3DSpecularGlossyMaterial16ensureNormalizedEf(
    float val) {
  return QQuick3DSpecularGlossyMaterial::ensureNormalized(val);
}

//  a Python function taken by a CuteQQuick3DSpecularGlossyMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DSpecularGlossyMaterial(
    QQuick3DSpecularGlossyMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DSpecularGlossyMaterial *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DSpecularGlossyMaterial::updateSpatialNode(QSSGRenderGraphObj
//      ect *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN30QQuick3DSpecularGlossyMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSpecularGlossyMaterial *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DSpecularGlossyMaterial *>(self)->OwnQQuick3DSpecularGlossyMaterial::updateSpatialNode(
      node);
}

//  void QQuick3DSpecularGlossyMaterial::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DSpecularGlossyMaterial12markAllDirtyEv(
    QQuick3DSpecularGlossyMaterial *self) {
  static_cast<OwnQQuick3DSpecularGlossyMaterial *>(self)->OwnQQuick3DSpecularGlossyMaterial::markAllDirty();
}

//  void QQuick3DSpecularGlossyMaterial::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DSpecularGlossyMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DSpecularGlossyMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DSpecularGlossyMaterial *>(self)->OwnQQuick3DSpecularGlossyMaterial::itemChange(
      a0,
      *a1);
}
