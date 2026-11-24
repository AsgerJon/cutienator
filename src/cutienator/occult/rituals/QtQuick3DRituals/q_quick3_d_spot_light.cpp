//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dspotlight_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dspotlight_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  Only a class built on QQuick3DSpotLight may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DSpotLight : QQuick3DSpotLight {
  using QQuick3DSpotLight::updateSpatialNode;
};

//  A QQuick3DSpotLight that Python can take functions over in. Every QQuick3DSpotLight
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DSpotLightCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DSpotLightCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpotLightCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpotLightCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpotLightCall4)(const void *, int *);
typedef void (*CuteQQuick3DSpotLightCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DSpotLightCall6)(const void *, int *);
typedef void (*CuteQQuick3DSpotLightCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSpotLightCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSpotLightCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpotLightCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpotLightCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSpotLightCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DSpotLight : public QQuick3DSpotLight {
public:
  using QQuick3DSpotLight::QQuick3DSpotLight;
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
  //      *QQuick3DSpotLight::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DSpotLightCall0 call = reinterpret_cast<CuteQQuick3DSpotLightCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DSpotLight::updateSpatialNode(node);
  }

  //  void QQuick3DAbstractLight::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DSpotLightCall1 call = reinterpret_cast<CuteQQuick3DSpotLightCall1>(taken[1]);
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
      CuteQQuick3DSpotLightCall2 call = reinterpret_cast<CuteQQuick3DSpotLightCall2>(taken[2]);
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
      CuteQQuick3DSpotLightCall3 call = reinterpret_cast<CuteQQuick3DSpotLightCall3>(taken[3]);
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
      CuteQQuick3DSpotLightCall4 call = reinterpret_cast<CuteQQuick3DSpotLightCall4>(taken[4]);
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
      CuteQQuick3DSpotLightCall5 call = reinterpret_cast<CuteQQuick3DSpotLightCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DSpotLightCall6 call = reinterpret_cast<CuteQQuick3DSpotLightCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DSpotLightCall7 call = reinterpret_cast<CuteQQuick3DSpotLightCall7>(taken[7]);
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
      CuteQQuick3DSpotLightCall8 call = reinterpret_cast<CuteQQuick3DSpotLightCall8>(taken[8]);
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
      CuteQQuick3DSpotLightCall9 call = reinterpret_cast<CuteQQuick3DSpotLightCall9>(taken[9]);
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
      CuteQQuick3DSpotLightCall10 call = reinterpret_cast<CuteQQuick3DSpotLightCall10>(taken[10]);
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
      CuteQQuick3DSpotLightCall11 call = reinterpret_cast<CuteQQuick3DSpotLightCall11>(taken[11]);
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
      CuteQQuick3DSpotLightCall12 call = reinterpret_cast<CuteQQuick3DSpotLightCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DSpotLight::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuick3DSpotLight10metaObjectEv(
    const QQuick3DSpotLight *self) {
  return self->metaObject();
}

//  QString QQuick3DSpotLight::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuick3DSpotLight2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DSpotLight::tr(s, c, n));
}

//  QQuick3DSpotLight::QQuick3DSpotLight(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DSpotLight *ritual_ZN17QQuick3DSpotLightC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DSpotLight(parent);
}

//  QQuick3DSpotLight::~QQuick3DSpotLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DSpotLightD1Ev(QQuick3DSpotLight *self) {
  delete self;
}

//  float QQuick3DSpotLight::constantFade() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QQuick3DSpotLight12constantFadeEv(
    const QQuick3DSpotLight *self) {
  return self->constantFade();
}

//  float QQuick3DSpotLight::linearFade() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QQuick3DSpotLight10linearFadeEv(
    const QQuick3DSpotLight *self) {
  return self->linearFade();
}

//  float QQuick3DSpotLight::quadraticFade() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QQuick3DSpotLight13quadraticFadeEv(
    const QQuick3DSpotLight *self) {
  return self->quadraticFade();
}

//  float QQuick3DSpotLight::coneAngle() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QQuick3DSpotLight9coneAngleEv(
    const QQuick3DSpotLight *self) {
  return self->coneAngle();
}

//  float QQuick3DSpotLight::innerConeAngle() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QQuick3DSpotLight14innerConeAngleEv(
    const QQuick3DSpotLight *self) {
  return self->innerConeAngle();
}

//  void QQuick3DSpotLight::setConstantFade(float constantFade)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DSpotLight15setConstantFadeEf(
    QQuick3DSpotLight *self,
    float constantFade) {
  self->setConstantFade(constantFade);
}

//  void QQuick3DSpotLight::setLinearFade(float linearFade)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DSpotLight13setLinearFadeEf(
    QQuick3DSpotLight *self,
    float linearFade) {
  self->setLinearFade(linearFade);
}

//  void QQuick3DSpotLight::setQuadraticFade(float quadraticFade)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DSpotLight16setQuadraticFadeEf(
    QQuick3DSpotLight *self,
    float quadraticFade) {
  self->setQuadraticFade(quadraticFade);
}

//  void QQuick3DSpotLight::setConeAngle(float coneAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DSpotLight12setConeAngleEf(
    QQuick3DSpotLight *self,
    float coneAngle) {
  self->setConeAngle(coneAngle);
}

//  void QQuick3DSpotLight::setInnerConeAngle(float innerConeAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DSpotLight17setInnerConeAngleEf(
    QQuick3DSpotLight *self,
    float innerConeAngle) {
  self->setInnerConeAngle(innerConeAngle);
}

//  QSSGRenderGraphObject
//      *QQuick3DSpotLight::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN17QQuick3DSpotLight17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSpotLight *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  a Python function taken by a CuteQQuick3DSpotLight, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DSpotLight(
    QQuick3DSpotLight *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DSpotLight *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DSpotLight::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN17QQuick3DSpotLight17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSpotLight *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DSpotLight *>(self)->OwnQQuick3DSpotLight::updateSpatialNode(
      node);
}
