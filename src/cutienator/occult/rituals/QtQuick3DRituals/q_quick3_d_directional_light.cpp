//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3ddirectionallight_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3ddirectionallight_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  Only a class built on QQuick3DDirectionalLight may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DDirectionalLight : QQuick3DDirectionalLight {
  using QQuick3DDirectionalLight::updateSpatialNode;
};

//  A QQuick3DDirectionalLight that Python can take functions over in. Every QQuick3DDirectionalLight
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DDirectionalLightCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DDirectionalLightCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDirectionalLightCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDirectionalLightCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDirectionalLightCall4)(const void *, int *);
typedef void (*CuteQQuick3DDirectionalLightCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DDirectionalLightCall6)(const void *, int *);
typedef void (*CuteQQuick3DDirectionalLightCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DDirectionalLightCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DDirectionalLightCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDirectionalLightCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDirectionalLightCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DDirectionalLightCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DDirectionalLight : public QQuick3DDirectionalLight {
public:
  using QQuick3DDirectionalLight::QQuick3DDirectionalLight;
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
  //      *QQuick3DDirectionalLight::updateSpatialNode(QSSGRenderGraphObjec
  //      t *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DDirectionalLightCall0 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DDirectionalLight::updateSpatialNode(node);
  }

  //  void QQuick3DAbstractLight::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DDirectionalLightCall1 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall1>(taken[1]);
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
      CuteQQuick3DDirectionalLightCall2 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall2>(taken[2]);
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
      CuteQQuick3DDirectionalLightCall3 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall3>(taken[3]);
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
      CuteQQuick3DDirectionalLightCall4 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall4>(taken[4]);
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
      CuteQQuick3DDirectionalLightCall5 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DDirectionalLightCall6 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DDirectionalLightCall7 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall7>(taken[7]);
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
      CuteQQuick3DDirectionalLightCall8 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall8>(taken[8]);
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
      CuteQQuick3DDirectionalLightCall9 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall9>(taken[9]);
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
      CuteQQuick3DDirectionalLightCall10 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall10>(taken[10]);
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
      CuteQQuick3DDirectionalLightCall11 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall11>(taken[11]);
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
      CuteQQuick3DDirectionalLightCall12 call = reinterpret_cast<CuteQQuick3DDirectionalLightCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DDirectionalLight::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuick3DDirectionalLight10metaObjectEv(
    const QQuick3DDirectionalLight *self) {
  return self->metaObject();
}

//  QString QQuick3DDirectionalLight::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuick3DDirectionalLight2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DDirectionalLight::tr(s, c, n));
}

//  QQuick3DDirectionalLight::QQuick3DDirectionalLight(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DDirectionalLight *ritual_ZN24QQuick3DDirectionalLightC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DDirectionalLight(parent);
}

//  QQuick3DDirectionalLight::~QQuick3DDirectionalLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DDirectionalLightD1Ev(
    QQuick3DDirectionalLight *self) {
  delete self;
}

//  float QQuick3DDirectionalLight::csmSplit1() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DDirectionalLight9csmSplit1Ev(
    const QQuick3DDirectionalLight *self) {
  return self->csmSplit1();
}

//  float QQuick3DDirectionalLight::csmSplit2() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DDirectionalLight9csmSplit2Ev(
    const QQuick3DDirectionalLight *self) {
  return self->csmSplit2();
}

//  float QQuick3DDirectionalLight::csmSplit3() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DDirectionalLight9csmSplit3Ev(
    const QQuick3DDirectionalLight *self) {
  return self->csmSplit3();
}

//  int QQuick3DDirectionalLight::csmNumSplits() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuick3DDirectionalLight12csmNumSplitsEv(
    const QQuick3DDirectionalLight *self) {
  return self->csmNumSplits();
}

//  float QQuick3DDirectionalLight::csmBlendRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DDirectionalLight13csmBlendRatioEv(
    const QQuick3DDirectionalLight *self) {
  return self->csmBlendRatio();
}

//  bool QQuick3DDirectionalLight::lockShadowmapTexels() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DDirectionalLight19lockShadowmapTexelsEv(
    const QQuick3DDirectionalLight *self) {
  return self->lockShadowmapTexels();
}

//  void QQuick3DDirectionalLight::setCsmSplit1(float newcsmSplit1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DDirectionalLight12setCsmSplit1Ef(
    QQuick3DDirectionalLight *self,
    float newcsmSplit1) {
  self->setCsmSplit1(newcsmSplit1);
}

//  void QQuick3DDirectionalLight::setCsmSplit2(float newcsmSplit2)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DDirectionalLight12setCsmSplit2Ef(
    QQuick3DDirectionalLight *self,
    float newcsmSplit2) {
  self->setCsmSplit2(newcsmSplit2);
}

//  void QQuick3DDirectionalLight::setCsmSplit3(float newcsmSplit3)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DDirectionalLight12setCsmSplit3Ef(
    QQuick3DDirectionalLight *self,
    float newcsmSplit3) {
  self->setCsmSplit3(newcsmSplit3);
}

//  void QQuick3DDirectionalLight::setCsmNumSplits(int newcsmNumSplits)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DDirectionalLight15setCsmNumSplitsEi(
    QQuick3DDirectionalLight *self,
    int newcsmNumSplits) {
  self->setCsmNumSplits(newcsmNumSplits);
}

//  void QQuick3DDirectionalLight::setCsmBlendRatio(float newcsmBlendRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DDirectionalLight16setCsmBlendRatioEf(
    QQuick3DDirectionalLight *self,
    float newcsmBlendRatio) {
  self->setCsmBlendRatio(newcsmBlendRatio);
}

//  void QQuick3DDirectionalLight::setLockShadowmapTexels(bool
//      newLockShadowmapTexels)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DDirectionalLight22setLockShadowmapTexelsEb(
    QQuick3DDirectionalLight *self,
    bool newLockShadowmapTexels) {
  self->setLockShadowmapTexels(newLockShadowmapTexels);
}

//  QSSGRenderGraphObject
//      *QQuick3DDirectionalLight::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN24QQuick3DDirectionalLight17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DDirectionalLight *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  a Python function taken by a CuteQQuick3DDirectionalLight, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DDirectionalLight(
    QQuick3DDirectionalLight *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DDirectionalLight *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DDirectionalLight::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN24QQuick3DDirectionalLight17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DDirectionalLight *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DDirectionalLight *>(self)->OwnQQuick3DDirectionalLight::updateSpatialNode(
      node);
}
