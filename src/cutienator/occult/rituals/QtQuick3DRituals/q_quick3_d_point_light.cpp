//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dpointlight_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dpointlight_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  Only a class built on QQuick3DPointLight may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DPointLight : QQuick3DPointLight {
  using QQuick3DPointLight::updateSpatialNode;
};

//  A QQuick3DPointLight that Python can take functions over in. Every QQuick3DPointLight
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DPointLightCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DPointLightCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPointLightCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPointLightCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPointLightCall4)(const void *, int *);
typedef void (*CuteQQuick3DPointLightCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DPointLightCall6)(const void *, int *);
typedef void (*CuteQQuick3DPointLightCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DPointLightCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DPointLightCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPointLightCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPointLightCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DPointLightCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DPointLight : public QQuick3DPointLight {
public:
  using QQuick3DPointLight::QQuick3DPointLight;
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
  //      *QQuick3DPointLight::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DPointLightCall0 call = reinterpret_cast<CuteQQuick3DPointLightCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DPointLight::updateSpatialNode(node);
  }

  //  void QQuick3DAbstractLight::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DPointLightCall1 call = reinterpret_cast<CuteQQuick3DPointLightCall1>(taken[1]);
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
      CuteQQuick3DPointLightCall2 call = reinterpret_cast<CuteQQuick3DPointLightCall2>(taken[2]);
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
      CuteQQuick3DPointLightCall3 call = reinterpret_cast<CuteQQuick3DPointLightCall3>(taken[3]);
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
      CuteQQuick3DPointLightCall4 call = reinterpret_cast<CuteQQuick3DPointLightCall4>(taken[4]);
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
      CuteQQuick3DPointLightCall5 call = reinterpret_cast<CuteQQuick3DPointLightCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DPointLightCall6 call = reinterpret_cast<CuteQQuick3DPointLightCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DPointLightCall7 call = reinterpret_cast<CuteQQuick3DPointLightCall7>(taken[7]);
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
      CuteQQuick3DPointLightCall8 call = reinterpret_cast<CuteQQuick3DPointLightCall8>(taken[8]);
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
      CuteQQuick3DPointLightCall9 call = reinterpret_cast<CuteQQuick3DPointLightCall9>(taken[9]);
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
      CuteQQuick3DPointLightCall10 call = reinterpret_cast<CuteQQuick3DPointLightCall10>(taken[10]);
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
      CuteQQuick3DPointLightCall11 call = reinterpret_cast<CuteQQuick3DPointLightCall11>(taken[11]);
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
      CuteQQuick3DPointLightCall12 call = reinterpret_cast<CuteQQuick3DPointLightCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DPointLight::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuick3DPointLight10metaObjectEv(
    const QQuick3DPointLight *self) {
  return self->metaObject();
}

//  void *QQuick3DPointLight::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuick3DPointLight11qt_metacastEPKc(
    QQuick3DPointLight *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DPointLight::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuick3DPointLight11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DPointLight *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DPointLight::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuick3DPointLight2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DPointLight::tr(s, c, n));
}

//  QQuick3DPointLight::QQuick3DPointLight(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DPointLight *ritual_ZN18QQuick3DPointLightC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DPointLight(parent);
}

//  QQuick3DPointLight::~QQuick3DPointLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DPointLightD1Ev(QQuick3DPointLight *self) {
  delete self;
}

//  float QQuick3DPointLight::constantFade() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK18QQuick3DPointLight12constantFadeEv(
    const QQuick3DPointLight *self) {
  return self->constantFade();
}

//  float QQuick3DPointLight::linearFade() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK18QQuick3DPointLight10linearFadeEv(
    const QQuick3DPointLight *self) {
  return self->linearFade();
}

//  float QQuick3DPointLight::quadraticFade() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK18QQuick3DPointLight13quadraticFadeEv(
    const QQuick3DPointLight *self) {
  return self->quadraticFade();
}

//  void QQuick3DPointLight::setConstantFade(float constantFade)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DPointLight15setConstantFadeEf(
    QQuick3DPointLight *self,
    float constantFade) {
  self->setConstantFade(constantFade);
}

//  void QQuick3DPointLight::setLinearFade(float linearFade)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DPointLight13setLinearFadeEf(
    QQuick3DPointLight *self,
    float linearFade) {
  self->setLinearFade(linearFade);
}

//  void QQuick3DPointLight::setQuadraticFade(float quadraticFade)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DPointLight16setQuadraticFadeEf(
    QQuick3DPointLight *self,
    float quadraticFade) {
  self->setQuadraticFade(quadraticFade);
}

//  void QQuick3DPointLight::constantFadeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DPointLight19constantFadeChangedEv(
    QQuick3DPointLight *self) {
  self->constantFadeChanged();
}

//  void QQuick3DPointLight::linearFadeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DPointLight17linearFadeChangedEv(
    QQuick3DPointLight *self) {
  self->linearFadeChanged();
}

//  void QQuick3DPointLight::quadraticFadeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DPointLight20quadraticFadeChangedEv(
    QQuick3DPointLight *self) {
  self->quadraticFadeChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DPointLight::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN18QQuick3DPointLight17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DPointLight *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  a Python function taken by a CuteQQuick3DPointLight, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DPointLight(
    QQuick3DPointLight *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DPointLight *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DPointLight::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN18QQuick3DPointLight17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DPointLight *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DPointLight *>(self)->OwnQQuick3DPointLight::updateSpatialNode(
      node);
}
