//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dabstractlight_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dabstractlight_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  Only a class built on QQuick3DAbstractLight may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DAbstractLight : QQuick3DAbstractLight {
  using QQuick3DAbstractLight::updateSpatialNode;
  using QQuick3DAbstractLight::markAllDirty;
};

//  A QQuick3DAbstractLight that Python can take functions over in. Every QQuick3DAbstractLight
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DAbstractLightCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DAbstractLightCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAbstractLightCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAbstractLightCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAbstractLightCall4)(const void *, int *);
typedef void (*CuteQQuick3DAbstractLightCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DAbstractLightCall6)(const void *, int *);
typedef void (*CuteQQuick3DAbstractLightCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DAbstractLightCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DAbstractLightCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAbstractLightCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAbstractLightCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAbstractLightCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DAbstractLight : public QQuick3DAbstractLight {
public:
  using QQuick3DAbstractLight::QQuick3DAbstractLight;
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DAbstractLight::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall0 call = reinterpret_cast<CuteQQuick3DAbstractLightCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DAbstractLight::updateSpatialNode(node);
  }

  //  void QQuick3DAbstractLight::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall1 call = reinterpret_cast<CuteQQuick3DAbstractLightCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DAbstractLight::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall2 call = reinterpret_cast<CuteQQuick3DAbstractLightCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall3 call = reinterpret_cast<CuteQQuick3DAbstractLightCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall4 call = reinterpret_cast<CuteQQuick3DAbstractLightCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall5 call = reinterpret_cast<CuteQQuick3DAbstractLightCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall6 call = reinterpret_cast<CuteQQuick3DAbstractLightCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall7 call = reinterpret_cast<CuteQQuick3DAbstractLightCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall8 call = reinterpret_cast<CuteQQuick3DAbstractLightCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall9 call = reinterpret_cast<CuteQQuick3DAbstractLightCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall10 call = reinterpret_cast<CuteQQuick3DAbstractLightCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall11 call = reinterpret_cast<CuteQQuick3DAbstractLightCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DAbstractLightCall12 call = reinterpret_cast<CuteQQuick3DAbstractLightCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DAbstractLight::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DAbstractLight10metaObjectEv(
    const QQuick3DAbstractLight *self) {
  return self->metaObject();
}

//  QString QQuick3DAbstractLight::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuick3DAbstractLight2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DAbstractLight::tr(s, c, n));
}

//  void QQuick3DAbstractLight::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight24qt_qmlMarker_uncreatableEv(
    QQuick3DAbstractLight *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DAbstractLight::~QQuick3DAbstractLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLightD1Ev(QQuick3DAbstractLight *self) {
  delete self;
}

//  QColor QQuick3DAbstractLight::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK21QQuick3DAbstractLight5colorEv(
    const QQuick3DAbstractLight *self) {
  return new QColor(self->color());
}

//  QColor QQuick3DAbstractLight::ambientColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK21QQuick3DAbstractLight12ambientColorEv(
    const QQuick3DAbstractLight *self) {
  return new QColor(self->ambientColor());
}

//  float QQuick3DAbstractLight::brightness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DAbstractLight10brightnessEv(
    const QQuick3DAbstractLight *self) {
  return self->brightness();
}

//  QQuick3DNode *QQuick3DAbstractLight::scope() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK21QQuick3DAbstractLight5scopeEv(
    const QQuick3DAbstractLight *self) {
  return self->scope();
}

//  bool QQuick3DAbstractLight::castsShadow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DAbstractLight11castsShadowEv(
    const QQuick3DAbstractLight *self) {
  return self->castsShadow();
}

//  float QQuick3DAbstractLight::shadowBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DAbstractLight10shadowBiasEv(
    const QQuick3DAbstractLight *self) {
  return self->shadowBias();
}

//  float QQuick3DAbstractLight::shadowFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DAbstractLight12shadowFactorEv(
    const QQuick3DAbstractLight *self) {
  return self->shadowFactor();
}

//  QSSGShadowMapQuality QQuick3DAbstractLight::shadowMapQuality() const
extern "C" Q_DECL_EXPORT
QQuick3DAbstractLight::QSSGShadowMapQuality ritual_ZNK21QQuick3DAbstractLight16shadowMapQualityEv(
    const QQuick3DAbstractLight *self) {
  return self->shadowMapQuality();
}

//  float QQuick3DAbstractLight::shadowMapFar() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DAbstractLight12shadowMapFarEv(
    const QQuick3DAbstractLight *self) {
  return self->shadowMapFar();
}

//  float QQuick3DAbstractLight::shadowFilter() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DAbstractLight12shadowFilterEv(
    const QQuick3DAbstractLight *self) {
  return self->shadowFilter();
}

//  QSSGBakeMode QQuick3DAbstractLight::bakeMode() const
extern "C" Q_DECL_EXPORT
QQuick3DAbstractLight::QSSGBakeMode ritual_ZNK21QQuick3DAbstractLight8bakeModeEv(
    const QQuick3DAbstractLight *self) {
  return self->bakeMode();
}

//  QSSGSoftShadowQuality QQuick3DAbstractLight::softShadowQuality() const
extern "C" Q_DECL_EXPORT
QQuick3DAbstractLight::QSSGSoftShadowQuality ritual_ZNK21QQuick3DAbstractLight17softShadowQualityEv(
    const QQuick3DAbstractLight *self) {
  return self->softShadowQuality();
}

//  float QQuick3DAbstractLight::pcfFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DAbstractLight9pcfFactorEv(
    const QQuick3DAbstractLight *self) {
  return self->pcfFactor();
}

//  bool QQuick3DAbstractLight::use32BitShadowmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DAbstractLight17use32BitShadowmapEv(
    const QQuick3DAbstractLight *self) {
  return self->use32BitShadowmap();
}

//  void QQuick3DAbstractLight::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight8setColorERK6QColor(
    QQuick3DAbstractLight *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuick3DAbstractLight::setAmbientColor(const QColor &ambientColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight15setAmbientColorERK6QColor(
    QQuick3DAbstractLight *self,
    const QColor *ambientColor) {
  self->setAmbientColor(*ambientColor);
}

//  void QQuick3DAbstractLight::setBrightness(float brightness)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight13setBrightnessEf(
    QQuick3DAbstractLight *self,
    float brightness) {
  self->setBrightness(brightness);
}

//  void QQuick3DAbstractLight::setScope(QQuick3DNode *scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight8setScopeEP12QQuick3DNode(
    QQuick3DAbstractLight *self,
    QQuick3DNode *scope) {
  self->setScope(scope);
}

//  void QQuick3DAbstractLight::setCastsShadow(bool castsShadow)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight14setCastsShadowEb(
    QQuick3DAbstractLight *self,
    bool castsShadow) {
  self->setCastsShadow(castsShadow);
}

//  void QQuick3DAbstractLight::setShadowBias(float shadowBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight13setShadowBiasEf(
    QQuick3DAbstractLight *self,
    float shadowBias) {
  self->setShadowBias(shadowBias);
}

//  void QQuick3DAbstractLight::setShadowFactor(float shadowFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight15setShadowFactorEf(
    QQuick3DAbstractLight *self,
    float shadowFactor) {
  self->setShadowFactor(shadowFactor);
}

//  void QQuick3DAbstractLight::setShadowMapQuality(QQuick3DAbstractLight::QS
//      SGShadowMapQuality shadowMapQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight19setShadowMapQualityENS_20QSSGShadowMapQualityE(
    QQuick3DAbstractLight *self,
    QQuick3DAbstractLight::QSSGShadowMapQuality shadowMapQuality) {
  self->setShadowMapQuality(shadowMapQuality);
}

//  void QQuick3DAbstractLight::setShadowMapFar(float shadowMapFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight15setShadowMapFarEf(
    QQuick3DAbstractLight *self,
    float shadowMapFar) {
  self->setShadowMapFar(shadowMapFar);
}

//  void QQuick3DAbstractLight::setShadowFilter(float shadowFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight15setShadowFilterEf(
    QQuick3DAbstractLight *self,
    float shadowFilter) {
  self->setShadowFilter(shadowFilter);
}

//  void
//      QQuick3DAbstractLight::setBakeMode(QQuick3DAbstractLight::QSSGBakeMod
//      e bakeMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight11setBakeModeENS_12QSSGBakeModeE(
    QQuick3DAbstractLight *self,
    QQuick3DAbstractLight::QSSGBakeMode bakeMode) {
  self->setBakeMode(bakeMode);
}

//  void QQuick3DAbstractLight::setSoftShadowQuality(QQuick3DAbstractLight::Q
//      SSGSoftShadowQuality softShadowQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight20setSoftShadowQualityENS_21QSSGSoftShadowQualityE(
    QQuick3DAbstractLight *self,
    QQuick3DAbstractLight::QSSGSoftShadowQuality softShadowQuality) {
  self->setSoftShadowQuality(softShadowQuality);
}

//  void QQuick3DAbstractLight::setPcfFactor(float pcfFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight12setPcfFactorEf(
    QQuick3DAbstractLight *self,
    float pcfFactor) {
  self->setPcfFactor(pcfFactor);
}

//  void QQuick3DAbstractLight::setUse32BitShadowmap(bool use32BitShadowmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight20setUse32BitShadowmapEb(
    QQuick3DAbstractLight *self,
    bool use32BitShadowmap) {
  self->setUse32BitShadowmap(use32BitShadowmap);
}

//  QSSGRenderGraphObject
//      *QQuick3DAbstractLight::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN21QQuick3DAbstractLight17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DAbstractLight *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DAbstractLight::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DAbstractLight12markAllDirtyEv(
    QQuick3DAbstractLight *self) {
  self->markAllDirty();
}

//  quint32 QQuick3DAbstractLight::mapToShadowResolution(QSSGShadowMapQuality
//      resolution)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN21QQuick3DAbstractLight21mapToShadowResolutionENS_20QSSGShadowMapQualityE(
    QQuick3DAbstractLight *self,
    QQuick3DAbstractLight::QSSGShadowMapQuality resolution) {
  return self->mapToShadowResolution(resolution);
}

//  a Python function taken by a CuteQQuick3DAbstractLight, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DAbstractLight(
    QQuick3DAbstractLight *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DAbstractLight *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DAbstractLight::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN21QQuick3DAbstractLight17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DAbstractLight *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DAbstractLight *>(self)->OwnQQuick3DAbstractLight::updateSpatialNode(
      node);
}

//  void QQuick3DAbstractLight::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuick3DAbstractLight12markAllDirtyEv(
    QQuick3DAbstractLight *self) {
  static_cast<OwnQQuick3DAbstractLight *>(self)->OwnQQuick3DAbstractLight::markAllDirty();
}
