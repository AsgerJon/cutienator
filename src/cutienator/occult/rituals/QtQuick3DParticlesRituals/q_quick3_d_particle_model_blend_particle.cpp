//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlemodelblendparticle
//  _p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlemodelblendparticle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DParticleModelBlendParticle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleModelBlendParticle : QQuick3DParticleModelBlendParticle {
  using QQuick3DParticleModelBlendParticle::itemChange;
  using QQuick3DParticleModelBlendParticle::reset;
  using QQuick3DParticleModelBlendParticle::doSetMaxAmount;
  using QQuick3DParticleModelBlendParticle::componentComplete;
  using QQuick3DParticleModelBlendParticle::nextCurrentIndex;
};

//  A QQuick3DParticleModelBlendParticle that Python can take functions over in. Every QQuick3DParticleModelBlendParticle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DParticleModelBlendParticleCall0)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DParticleModelBlendParticleCall1)(const void *, int *);
typedef void (*CuteQQuick3DParticleModelBlendParticleCall2)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleModelBlendParticleCall3)(const void *, int *);
typedef int (*CuteQQuick3DParticleModelBlendParticleCall4)(const void *, const QQuick3DParticleEmitter *, int *);
typedef void * (*CuteQQuick3DParticleModelBlendParticleCall5)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DParticleModelBlendParticleCall6)(const void *, int *);
typedef void (*CuteQQuick3DParticleModelBlendParticleCall7)(const void *, float, int *);
typedef void (*CuteQQuick3DParticleModelBlendParticleCall8)(const void *, int *);
typedef void (*CuteQQuick3DParticleModelBlendParticleCall9)(const void *, int *);
typedef void (*CuteQQuick3DParticleModelBlendParticleCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleModelBlendParticleCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleModelBlendParticleCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelBlendParticleCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelBlendParticleCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelBlendParticleCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelBlendParticleCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelBlendParticleCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleModelBlendParticle : public QQuick3DParticleModelBlendParticle {
public:
  using QQuick3DParticleModelBlendParticle::QQuick3DParticleModelBlendParticle;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle5resetEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle14doSetMaxAmountEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle16updateNodeLayersEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle12setDepthBiasEf")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DParticleModelBlendParticle::itemChange(ItemChange a0,
  //      const ItemChangeData &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall0 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall0>(taken[0]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DParticleModelBlendParticle::itemChange(a0, a1);
  }

  //  void QQuick3DParticleModelBlendParticle::reset()
  void reset() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall1 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleModelBlendParticle::reset();
  }

  //  void QQuick3DParticleModelBlendParticle::doSetMaxAmount(int amount)
  void doSetMaxAmount(int amount) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall2 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall2>(taken[2]);
      call(this, amount, &handled);
      if (handled) return;
    }
    QQuick3DParticleModelBlendParticle::doSetMaxAmount(amount);
  }

  //  void QQuick3DParticleModelBlendParticle::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall3 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleModelBlendParticle::componentComplete();
  }

  //  int QQuick3DParticleModelBlendParticle::nextCurrentIndex(const
  //      QQuick3DParticleEmitter *emitter)
  int nextCurrentIndex(const QQuick3DParticleEmitter *emitter) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall4 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall4>(taken[4]);
      int given = call(this, emitter, &handled);
      if (handled) return given;
    }
    return QQuick3DParticleModelBlendParticle::nextCurrentIndex(emitter);
  }

  //  QSSGRenderGraphObject *QQuick3DParticleModelBlendParticle::updateSpat
  //      ialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall5 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall5>(taken[5]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DParticleModelBlendParticle::updateSpatialNode(node);
  }

  //  void QQuick3DParticle::updateNodeLayers()
  void updateNodeLayers() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall6 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticle::updateNodeLayers();
  }

  //  void QQuick3DParticle::setDepthBias(float bias)
  void setDepthBias(float bias) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall7 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall7>(taken[7]);
      call(this, bias, &handled);
      if (handled) return;
    }
    QQuick3DParticle::setDepthBias(bias);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall8 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall9 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall10 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall11 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall12 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall13 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall14 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall15 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall16 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuick3DParticleModelBlendParticleCall17 call = reinterpret_cast<CuteQQuick3DParticleModelBlendParticleCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleModelBlendParticle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK34QQuick3DParticleModelBlendParticle10metaObjectEv(
    const QQuick3DParticleModelBlendParticle *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleModelBlendParticle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN34QQuick3DParticleModelBlendParticle11qt_metacastEPKc(
    QQuick3DParticleModelBlendParticle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleModelBlendParticle::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN34QQuick3DParticleModelBlendParticle11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleModelBlendParticle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleModelBlendParticle::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN34QQuick3DParticleModelBlendParticle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleModelBlendParticle::tr(s, c, n));
}

//  QQuick3DParticleModelBlendParticle::QQuick3DParticleModelBlendParticle(QQ
//      uick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleModelBlendParticle *ritual_ZN34QQuick3DParticleModelBlendParticleC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DParticleModelBlendParticle(parent);
}

//  QQuick3DParticleModelBlendParticle::~QQuick3DParticleModelBlendParticle()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticleD1Ev(
    QQuick3DParticleModelBlendParticle *self) {
  delete self;
}

//  QQmlComponent *QQuick3DParticleModelBlendParticle::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK34QQuick3DParticleModelBlendParticle8delegateEv(
    const QQuick3DParticleModelBlendParticle *self) {
  return self->delegate();
}

//  QQuick3DNode *QQuick3DParticleModelBlendParticle::endNode() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK34QQuick3DParticleModelBlendParticle7endNodeEv(
    const QQuick3DParticleModelBlendParticle *self) {
  return self->endNode();
}

//  ModelBlendMode QQuick3DParticleModelBlendParticle::modelBlendMode() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleModelBlendParticle::ModelBlendMode ritual_ZNK34QQuick3DParticleModelBlendParticle14modelBlendModeEv(
    const QQuick3DParticleModelBlendParticle *self) {
  return self->modelBlendMode();
}

//  int QQuick3DParticleModelBlendParticle::endTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QQuick3DParticleModelBlendParticle7endTimeEv(
    const QQuick3DParticleModelBlendParticle *self) {
  return self->endTime();
}

//  QQuick3DNode *QQuick3DParticleModelBlendParticle::activationNode() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK34QQuick3DParticleModelBlendParticle14activationNodeEv(
    const QQuick3DParticleModelBlendParticle *self) {
  return self->activationNode();
}

//  ModelBlendEmitMode QQuick3DParticleModelBlendParticle::emitMode() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleModelBlendParticle::ModelBlendEmitMode ritual_ZNK34QQuick3DParticleModelBlendParticle8emitModeEv(
    const QQuick3DParticleModelBlendParticle *self) {
  return self->emitMode();
}

//  void QQuick3DParticleModelBlendParticle::setDelegate(QQmlComponent
//      *setDelegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle11setDelegateEP13QQmlComponent(
    QQuick3DParticleModelBlendParticle *self,
    QQmlComponent *setDelegate) {
  self->setDelegate(setDelegate);
}

//  void QQuick3DParticleModelBlendParticle::setEndNode(QQuick3DNode
//      *endNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle10setEndNodeEP12QQuick3DNode(
    QQuick3DParticleModelBlendParticle *self,
    QQuick3DNode *endNode) {
  self->setEndNode(endNode);
}

//  void QQuick3DParticleModelBlendParticle::setEndTime(int endTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle10setEndTimeEi(
    QQuick3DParticleModelBlendParticle *self,
    int endTime) {
  self->setEndTime(endTime);
}

//  void QQuick3DParticleModelBlendParticle::setModelBlendMode(ModelBlendMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle17setModelBlendModeENS_14ModelBlendModeE(
    QQuick3DParticleModelBlendParticle *self,
    QQuick3DParticleModelBlendParticle::ModelBlendMode mode) {
  self->setModelBlendMode(mode);
}

//  void QQuick3DParticleModelBlendParticle::setActivationNode(QQuick3DNode
//      *activationNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle17setActivationNodeEP12QQuick3DNode(
    QQuick3DParticleModelBlendParticle *self,
    QQuick3DNode *activationNode) {
  self->setActivationNode(activationNode);
}

//  void QQuick3DParticleModelBlendParticle::setEmitMode(ModelBlendEmitMode
//      emitMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle11setEmitModeENS_18ModelBlendEmitModeE(
    QQuick3DParticleModelBlendParticle *self,
    QQuick3DParticleModelBlendParticle::ModelBlendEmitMode emitMode) {
  self->setEmitMode(emitMode);
}

//  void QQuick3DParticleModelBlendParticle::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle15delegateChangedEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->delegateChanged();
}

//  void QQuick3DParticleModelBlendParticle::blendFactorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle18blendFactorChangedEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->blendFactorChanged();
}

//  void QQuick3DParticleModelBlendParticle::endNodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle14endNodeChangedEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->endNodeChanged();
}

//  void QQuick3DParticleModelBlendParticle::modelBlendModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle21modelBlendModeChangedEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->modelBlendModeChanged();
}

//  void QQuick3DParticleModelBlendParticle::endTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle14endTimeChangedEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->endTimeChanged();
}

//  void QQuick3DParticleModelBlendParticle::activationNodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle21activationNodeChangedEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->activationNodeChanged();
}

//  void QQuick3DParticleModelBlendParticle::emitModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle15emitModeChangedEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->emitModeChanged();
}

//  void QQuick3DParticleModelBlendParticle::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DParticleModelBlendParticle *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DParticleModelBlendParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle5resetEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->reset();
}

//  bool QQuick3DParticleModelBlendParticle::lastParticle() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QQuick3DParticleModelBlendParticle12lastParticleEv(
    const QQuick3DParticleModelBlendParticle *self) {
  return self->lastParticle();
}

//  void QQuick3DParticleModelBlendParticle::doSetMaxAmount(int amount)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle14doSetMaxAmountEi(
    QQuick3DParticleModelBlendParticle *self,
    int amount) {
  self->doSetMaxAmount(amount);
}

//  void QQuick3DParticleModelBlendParticle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle17componentCompleteEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->componentComplete();
}

//  int QQuick3DParticleModelBlendParticle::nextCurrentIndex(const
//      QQuick3DParticleEmitter *emitter)
extern "C" Q_DECL_EXPORT
int ritual_ZN34QQuick3DParticleModelBlendParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter(
    QQuick3DParticleModelBlendParticle *self,
    const QQuick3DParticleEmitter *emitter) {
  return self->nextCurrentIndex(emitter);
}

//  void QQuick3DParticleModelBlendParticle::setParticleData(int
//      particleIndex, const QVector3D &position, const QVector3D &rotation,
//      const QVector4D &color, float size, float age)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle15setParticleDataEiRK9QVector3DS2_RK9QVector4Dff(
    QQuick3DParticleModelBlendParticle *self,
    int particleIndex,
    const QVector3D *position,
    const QVector3D *rotation,
    const QVector4D *color,
    float size,
    float age) {
  self->setParticleData(
      particleIndex,
      *position,
      *rotation,
      *color,
      size,
      age);
}

//  QVector3D QQuick3DParticleModelBlendParticle::particleCenter(int
//      particleIndex) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK34QQuick3DParticleModelBlendParticle14particleCenterEi(
    const QQuick3DParticleModelBlendParticle *self,
    int particleIndex) {
  return new QVector3D(self->particleCenter(particleIndex));
}

//  QVector3D QQuick3DParticleModelBlendParticle::particleEndPosition(int
//      particleIndex) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK34QQuick3DParticleModelBlendParticle19particleEndPositionEi(
    const QQuick3DParticleModelBlendParticle *self,
    int particleIndex) {
  return new QVector3D(self->particleEndPosition(particleIndex));
}

//  QVector3D QQuick3DParticleModelBlendParticle::particleEndRotation(int
//      particleIndex) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK34QQuick3DParticleModelBlendParticle19particleEndRotationEi(
    const QQuick3DParticleModelBlendParticle *self,
    int particleIndex) {
  return new QVector3D(self->particleEndRotation(particleIndex));
}

//  int QQuick3DParticleModelBlendParticle::randomIndex(int particleIndex)
extern "C" Q_DECL_EXPORT
int ritual_ZN34QQuick3DParticleModelBlendParticle11randomIndexEi(
    QQuick3DParticleModelBlendParticle *self,
    int particleIndex) {
  return self->randomIndex(particleIndex);
}

//  void QQuick3DParticleModelBlendParticle::commitParticles()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle15commitParticlesEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->commitParticles();
}

//  QSSGRenderGraphObject *QQuick3DParticleModelBlendParticle::updateSpatialN
//      ode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN34QQuick3DParticleModelBlendParticle17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DParticleModelBlendParticle *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DParticleModelBlendParticle::updateParticleBuffer(QSSGParticl
//      eBuffer *buffer, const QMatrix4x4 &sceneTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle20updateParticleBufferEP18QSSGParticleBufferRK10QMatrix4x4(
    QQuick3DParticleModelBlendParticle *self,
    QSSGParticleBuffer *buffer,
    const QMatrix4x4 *sceneTransform) {
  self->updateParticleBuffer(buffer, *sceneTransform);
}

//  void QQuick3DParticleModelBlendParticle::regenerate()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle10regenerateEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->regenerate();
}

//  void QQuick3DParticleModelBlendParticle::updateParticles()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle15updateParticlesEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->updateParticles();
}

//  void QQuick3DParticleModelBlendParticle::handleEndNodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuick3DParticleModelBlendParticle20handleEndNodeChangedEv(
    QQuick3DParticleModelBlendParticle *self) {
  self->handleEndNodeChanged();
}

//  PerEmitterData &QQuick3DParticleModelBlendParticle::perEmitterData(int
//      emitterIndex)
extern "C" Q_DECL_EXPORT
QQuick3DParticleModelBlendParticle::PerEmitterData *ritual_ZN34QQuick3DParticleModelBlendParticle14perEmitterDataEi(
    QQuick3DParticleModelBlendParticle *self,
    int emitterIndex) {
  return &(self->perEmitterData(emitterIndex));
}

//  a Python function taken by a CuteQQuick3DParticleModelBlendParticle, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleModelBlendParticle(
    QQuick3DParticleModelBlendParticle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleModelBlendParticle *>(self)->take(key, call);
}

//  void QQuick3DParticleModelBlendParticle::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QQuick3DParticleModelBlendParticle10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DParticleModelBlendParticle *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DParticleModelBlendParticle *>(self)->OwnQQuick3DParticleModelBlendParticle::itemChange(
      a0,
      *a1);
}

//  void QQuick3DParticleModelBlendParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QQuick3DParticleModelBlendParticle5resetEv(
    QQuick3DParticleModelBlendParticle *self) {
  static_cast<OwnQQuick3DParticleModelBlendParticle *>(self)->OwnQQuick3DParticleModelBlendParticle::reset();
}

//  void QQuick3DParticleModelBlendParticle::doSetMaxAmount(int amount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QQuick3DParticleModelBlendParticle14doSetMaxAmountEi(
    QQuick3DParticleModelBlendParticle *self,
    int amount) {
  static_cast<OwnQQuick3DParticleModelBlendParticle *>(self)->OwnQQuick3DParticleModelBlendParticle::doSetMaxAmount(
      amount);
}

//  void QQuick3DParticleModelBlendParticle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QQuick3DParticleModelBlendParticle17componentCompleteEv(
    QQuick3DParticleModelBlendParticle *self) {
  static_cast<OwnQQuick3DParticleModelBlendParticle *>(self)->OwnQQuick3DParticleModelBlendParticle::componentComplete();
}

//  int QQuick3DParticleModelBlendParticle::nextCurrentIndex(const
//      QQuick3DParticleEmitter *emitter)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN34QQuick3DParticleModelBlendParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter(
    QQuick3DParticleModelBlendParticle *self,
    const QQuick3DParticleEmitter *emitter) {
  return static_cast<OwnQQuick3DParticleModelBlendParticle *>(self)->OwnQQuick3DParticleModelBlendParticle::nextCurrentIndex(
      emitter);
}

//  QSSGRenderGraphObject *QQuick3DParticleModelBlendParticle::updateSpatialN
//      ode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN34QQuick3DParticleModelBlendParticle17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DParticleModelBlendParticle *self,
    QSSGRenderGraphObject *node) {
  return self->QQuick3DParticleModelBlendParticle::updateSpatialNode(node);
}
