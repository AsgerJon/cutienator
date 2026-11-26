//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlespriteparticle_p.h
//  , Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlespriteparticle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  Only a class built on QQuick3DParticleSpriteParticle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleSpriteParticle : QQuick3DParticleSpriteParticle {
  using QQuick3DParticleSpriteParticle::itemChange;
  using QQuick3DParticleSpriteParticle::reset;
  using QQuick3DParticleSpriteParticle::componentComplete;
  using QQuick3DParticleSpriteParticle::nextCurrentIndex;
  using QQuick3DParticleSpriteParticle::setParticleData;
  using QQuick3DParticleSpriteParticle::resetParticleData;
  using QQuick3DParticleSpriteParticle::commitParticles;
  using QQuick3DParticleSpriteParticle::setDepthBias;
  using QQuick3DParticleSpriteParticle::handleMaxAmountChanged;
  using QQuick3DParticleSpriteParticle::handleSystemChanged;
  using QQuick3DParticleSpriteParticle::updateNodeLayers;
};

//  A QQuick3DParticleSpriteParticle that Python can take functions over in. Every QQuick3DParticleSpriteParticle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DParticleSpriteParticleCall0)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall1)(const void *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall2)(const void *, int *);
typedef int (*CuteQQuick3DParticleSpriteParticleCall3)(const void *, const QQuick3DParticleEmitter *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall4)(const void *, int, const QVector3D *, const QVector3D *, const QVector4D *, float, float, float, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall5)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall6)(const void *, float, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall7)(const void *, float, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall8)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall9)(const void *, QQuick3DParticleSystem *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall10)(const void *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall11)(const void *, int, int *);
typedef void * (*CuteQQuick3DParticleSpriteParticleCall12)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall13)(const void *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall14)(const void *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticleCall15)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSpriteParticleCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSpriteParticleCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticleCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticleCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticleCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticleCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticleCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleSpriteParticle : public QQuick3DParticleSpriteParticle {
public:
  using QQuick3DParticleSpriteParticle::QQuick3DParticleSpriteParticle;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle5resetEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle15setParticleDataEiRK9QVector3DS2_RK9QVector4Dfff")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle17resetParticleDataEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle15commitParticlesEf")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle12setDepthBiasEf")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle22handleMaxAmountChangedEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle19handleSystemChangedEP22QQuick3DParticleSystem")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle16updateNodeLayersEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle14doSetMaxAmountEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DParticleSpriteParticle::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall0 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall0>(taken[0]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::itemChange(a0, a1);
  }

  //  void QQuick3DParticleSpriteParticle::reset()
  void reset() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall1 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::reset();
  }

  //  void QQuick3DParticleSpriteParticle::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall2 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::componentComplete();
  }

  //  int QQuick3DParticleSpriteParticle::nextCurrentIndex(const
  //      QQuick3DParticleEmitter *emitter)
  int nextCurrentIndex(const QQuick3DParticleEmitter *emitter) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall3 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall3>(taken[3]);
      int given = call(this, emitter, &handled);
      if (handled) return given;
    }
    return QQuick3DParticleSpriteParticle::nextCurrentIndex(emitter);
  }

  //  void QQuick3DParticleSpriteParticle::setParticleData(int
  //      particleIndex, const QVector3D &position, const QVector3D
  //      &rotation, const QVector4D &color, float size, float age, float
  //      animationFrame)
  void setParticleData(
      int particleIndex,
      const QVector3D &position,
      const QVector3D &rotation,
      const QVector4D &color,
      float size,
      float age,
      float animationFrame) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall4 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall4>(taken[4]);
      call(this, particleIndex, &position, &rotation, &color, size, age, animationFrame, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::setParticleData(particleIndex, position, rotation, color, size, age, animationFrame);
  }

  //  void QQuick3DParticleSpriteParticle::resetParticleData(int
  //      particleIndex)
  void resetParticleData(int particleIndex) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall5 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall5>(taken[5]);
      call(this, particleIndex, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::resetParticleData(particleIndex);
  }

  //  void QQuick3DParticleSpriteParticle::commitParticles(float a0)
  void commitParticles(float a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall6 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::commitParticles(a0);
  }

  //  void QQuick3DParticleSpriteParticle::setDepthBias(float bias)
  void setDepthBias(float bias) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall7 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall7>(taken[7]);
      call(this, bias, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::setDepthBias(bias);
  }

  //  void QQuick3DParticleSpriteParticle::handleMaxAmountChanged(int
  //      amount)
  void handleMaxAmountChanged(int amount) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall8 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall8>(taken[8]);
      call(this, amount, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::handleMaxAmountChanged(amount);
  }

  //  void QQuick3DParticleSpriteParticle::handleSystemChanged(QQuick3DPart
  //      icleSystem *system)
  void handleSystemChanged(QQuick3DParticleSystem *system) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall9 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall9>(taken[9]);
      call(this, system, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::handleSystemChanged(system);
  }

  //  void QQuick3DParticleSpriteParticle::updateNodeLayers()
  void updateNodeLayers() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall10 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::updateNodeLayers();
  }

  //  void QQuick3DParticle::doSetMaxAmount(int amount)
  void doSetMaxAmount(int amount) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall11 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall11>(taken[11]);
      call(this, amount, &handled);
      if (handled) return;
    }
    QQuick3DParticle::doSetMaxAmount(amount);
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DParticle::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall12 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall12>(taken[12]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DParticle::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall13 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall14 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall15 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall16 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall17 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall18 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall19 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall20 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall21 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticleCall22 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticleCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleSpriteParticle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QQuick3DParticleSpriteParticle10metaObjectEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleSpriteParticle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QQuick3DParticleSpriteParticle11qt_metacastEPKc(
    QQuick3DParticleSpriteParticle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleSpriteParticle::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QQuick3DParticleSpriteParticle11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleSpriteParticle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleSpriteParticle::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQuick3DParticleSpriteParticle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleSpriteParticle::tr(s, c, n));
}

//  QQuick3DParticleSpriteParticle::QQuick3DParticleSpriteParticle(QQuick3DNo
//      de *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleSpriteParticle *ritual_ZN30QQuick3DParticleSpriteParticleC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DParticleSpriteParticle(parent);
}

//  QQuick3DParticleSpriteParticle::~QQuick3DParticleSpriteParticle()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticleD1Ev(
    QQuick3DParticleSpriteParticle *self) {
  delete self;
}

//  BlendMode QQuick3DParticleSpriteParticle::blendMode() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleSpriteParticle::BlendMode ritual_ZNK30QQuick3DParticleSpriteParticle9blendModeEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->blendMode();
}

//  QQuick3DTexture *QQuick3DParticleSpriteParticle::sprite() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DParticleSpriteParticle6spriteEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->sprite();
}

//  QQuick3DParticleSpriteSequence
//      *QQuick3DParticleSpriteParticle::spriteSequence() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleSpriteSequence *ritual_ZNK30QQuick3DParticleSpriteParticle14spriteSequenceEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->spriteSequence();
}

//  bool QQuick3DParticleSpriteParticle::billboard() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DParticleSpriteParticle9billboardEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->billboard();
}

//  float QQuick3DParticleSpriteParticle::particleScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DParticleSpriteParticle13particleScaleEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->particleScale();
}

//  QQuick3DTexture *QQuick3DParticleSpriteParticle::colorTable() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK30QQuick3DParticleSpriteParticle10colorTableEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->colorTable();
}

//  QQmlListProperty<QQuick3DAbstractLight>
//      QQuick3DParticleSpriteParticle::lights()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DAbstractLight> *ritual_ZN30QQuick3DParticleSpriteParticle6lightsEv(
    QQuick3DParticleSpriteParticle *self) {
  return new QQmlListProperty<QQuick3DAbstractLight>(self->lights());
}

//  float QQuick3DParticleSpriteParticle::offsetX() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DParticleSpriteParticle7offsetXEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->offsetX();
}

//  float QQuick3DParticleSpriteParticle::offsetY() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK30QQuick3DParticleSpriteParticle7offsetYEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->offsetY();
}

//  bool QQuick3DParticleSpriteParticle::castsReflections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DParticleSpriteParticle16castsReflectionsEv(
    const QQuick3DParticleSpriteParticle *self) {
  return self->castsReflections();
}

//  void QQuick3DParticleSpriteParticle::setBlendMode(QQuick3DParticleSpriteP
//      article::BlendMode blendMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle12setBlendModeENS_9BlendModeE(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DParticleSpriteParticle::BlendMode blendMode) {
  self->setBlendMode(blendMode);
}

//  void QQuick3DParticleSpriteParticle::setSprite(QQuick3DTexture *sprite)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle9setSpriteEP15QQuick3DTexture(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DTexture *sprite) {
  self->setSprite(sprite);
}

//  void QQuick3DParticleSpriteParticle::setSpriteSequence(QQuick3DParticleSp
//      riteSequence *spriteSequence)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle17setSpriteSequenceEP30QQuick3DParticleSpriteSequence(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DParticleSpriteSequence *spriteSequence) {
  self->setSpriteSequence(spriteSequence);
}

//  void QQuick3DParticleSpriteParticle::setBillboard(bool billboard)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle12setBillboardEb(
    QQuick3DParticleSpriteParticle *self,
    bool billboard) {
  self->setBillboard(billboard);
}

//  void QQuick3DParticleSpriteParticle::setParticleScale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle16setParticleScaleEf(
    QQuick3DParticleSpriteParticle *self,
    float scale) {
  self->setParticleScale(scale);
}

//  void QQuick3DParticleSpriteParticle::setColorTable(QQuick3DTexture
//      *colorTable)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle13setColorTableEP15QQuick3DTexture(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DTexture *colorTable) {
  self->setColorTable(colorTable);
}

//  void QQuick3DParticleSpriteParticle::setOffsetX(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle10setOffsetXEf(
    QQuick3DParticleSpriteParticle *self,
    float value) {
  self->setOffsetX(value);
}

//  void QQuick3DParticleSpriteParticle::setOffsetY(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle10setOffsetYEf(
    QQuick3DParticleSpriteParticle *self,
    float value) {
  self->setOffsetY(value);
}

//  void QQuick3DParticleSpriteParticle::setCastsReflections(bool
//      castsReflections)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle19setCastsReflectionsEb(
    QQuick3DParticleSpriteParticle *self,
    bool castsReflections) {
  self->setCastsReflections(castsReflections);
}

//  void QQuick3DParticleSpriteParticle::blendModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle16blendModeChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->blendModeChanged();
}

//  void QQuick3DParticleSpriteParticle::spriteChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle13spriteChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->spriteChanged();
}

//  void QQuick3DParticleSpriteParticle::spriteSequenceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle21spriteSequenceChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->spriteSequenceChanged();
}

//  void QQuick3DParticleSpriteParticle::billboardChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle16billboardChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->billboardChanged();
}

//  void QQuick3DParticleSpriteParticle::particleScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle20particleScaleChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->particleScaleChanged();
}

//  void QQuick3DParticleSpriteParticle::colorTableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle17colorTableChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->colorTableChanged();
}

//  void QQuick3DParticleSpriteParticle::lightsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle13lightsChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->lightsChanged();
}

//  void QQuick3DParticleSpriteParticle::offsetXChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle14offsetXChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->offsetXChanged();
}

//  void QQuick3DParticleSpriteParticle::offsetYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle14offsetYChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->offsetYChanged();
}

//  void QQuick3DParticleSpriteParticle::castsReflectionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle23castsReflectionsChangedEv(
    QQuick3DParticleSpriteParticle *self) {
  self->castsReflectionsChanged();
}

//  void QQuick3DParticleSpriteParticle::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DParticleSpriteParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle5resetEv(
    QQuick3DParticleSpriteParticle *self) {
  self->reset();
}

//  void QQuick3DParticleSpriteParticle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle17componentCompleteEv(
    QQuick3DParticleSpriteParticle *self) {
  self->componentComplete();
}

//  int QQuick3DParticleSpriteParticle::nextCurrentIndex(const
//      QQuick3DParticleEmitter *emitter)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QQuick3DParticleSpriteParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter(
    QQuick3DParticleSpriteParticle *self,
    const QQuick3DParticleEmitter *emitter) {
  return self->nextCurrentIndex(emitter);
}

//  void QQuick3DParticleSpriteParticle::setParticleData(int particleIndex,
//      const QVector3D &position, const QVector3D &rotation, const QVector4D
//      &color, float size, float age, float animationFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle15setParticleDataEiRK9QVector3DS2_RK9QVector4Dfff(
    QQuick3DParticleSpriteParticle *self,
    int particleIndex,
    const QVector3D *position,
    const QVector3D *rotation,
    const QVector4D *color,
    float size,
    float age,
    float animationFrame) {
  self->setParticleData(
      particleIndex,
      *position,
      *rotation,
      *color,
      size,
      age,
      animationFrame);
}

//  void QQuick3DParticleSpriteParticle::resetParticleData(int particleIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle17resetParticleDataEi(
    QQuick3DParticleSpriteParticle *self,
    int particleIndex) {
  self->resetParticleData(particleIndex);
}

//  void QQuick3DParticleSpriteParticle::commitParticles(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle15commitParticlesEf(
    QQuick3DParticleSpriteParticle *self,
    float a0) {
  self->commitParticles(a0);
}

//  void QQuick3DParticleSpriteParticle::setDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle12setDepthBiasEf(
    QQuick3DParticleSpriteParticle *self,
    float bias) {
  self->setDepthBias(bias);
}

//  void QQuick3DParticleSpriteParticle::onLightDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle16onLightDestroyedEP7QObject(
    QQuick3DParticleSpriteParticle *self,
    QObject *object) {
  self->onLightDestroyed(object);
}

//  PerEmitterData &QQuick3DParticleSpriteParticle::perEmitterData(const
//      QQuick3DNode *updateNode)
extern "C" Q_DECL_EXPORT
QQuick3DParticleSpriteParticle::PerEmitterData *ritual_ZN30QQuick3DParticleSpriteParticle14perEmitterDataEPK12QQuick3DNode(
    QQuick3DParticleSpriteParticle *self,
    const QQuick3DNode *updateNode) {
  return &(self->perEmitterData(updateNode));
}

//  PerEmitterData &QQuick3DParticleSpriteParticle::perEmitterData(int
//      emitterIndex)
extern "C" Q_DECL_EXPORT
QQuick3DParticleSpriteParticle::PerEmitterData *ritual_ZN30QQuick3DParticleSpriteParticle14perEmitterDataEi(
    QQuick3DParticleSpriteParticle *self,
    int emitterIndex) {
  return &(self->perEmitterData(emitterIndex));
}

//  QSSGRenderGraphObject
//      *QQuick3DParticleSpriteParticle::updateParticleNode(const
//      ParticleUpdateNode *updateNode, QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN30QQuick3DParticleSpriteParticle18updateParticleNodeEPKNS_18ParticleUpdateNodeEP21QSSGRenderGraphObject(
    QQuick3DParticleSpriteParticle *self,
    const QQuick3DParticleSpriteParticle::ParticleUpdateNode *updateNode,
    QSSGRenderGraphObject *node) {
  return self->updateParticleNode(updateNode, node);
}

//  void QQuick3DParticleSpriteParticle::handleMaxAmountChanged(int amount)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle22handleMaxAmountChangedEi(
    QQuick3DParticleSpriteParticle *self,
    int amount) {
  self->handleMaxAmountChanged(amount);
}

//  void QQuick3DParticleSpriteParticle::handleSystemChanged(QQuick3DParticle
//      System *system)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle19handleSystemChangedEP22QQuick3DParticleSystem(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DParticleSystem *system) {
  self->handleSystemChanged(system);
}

//  void QQuick3DParticleSpriteParticle::updateNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle11updateNodesEv(
    QQuick3DParticleSpriteParticle *self) {
  self->updateNodes();
}

//  void QQuick3DParticleSpriteParticle::deleteNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle11deleteNodesEv(
    QQuick3DParticleSpriteParticle *self) {
  self->deleteNodes();
}

//  void QQuick3DParticleSpriteParticle::markNodesDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle14markNodesDirtyEv(
    QQuick3DParticleSpriteParticle *self) {
  self->markNodesDirty();
}

//  void QQuick3DParticleSpriteParticle::updateNodeLayers()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle16updateNodeLayersEv(
    QQuick3DParticleSpriteParticle *self) {
  self->updateNodeLayers();
}

//  QSSGRenderParticles::FeatureLevel QQuick3DParticleSpriteParticle::mapFeat
//      ureLevel(QQuick3DParticleSpriteParticle::FeatureLevel level)
extern "C" Q_DECL_EXPORT
QSSGRenderParticles::FeatureLevel ritual_ZN30QQuick3DParticleSpriteParticle15mapFeatureLevelENS_12FeatureLevelE(
    QQuick3DParticleSpriteParticle::FeatureLevel level) {
  return QQuick3DParticleSpriteParticle::mapFeatureLevel(level);
}

//  void
//      QQuick3DParticleSpriteParticle::updateParticleBuffer(ParticleUpdateNo
//      de *updateNode, QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle20updateParticleBufferEPNS_18ParticleUpdateNodeEP21QSSGRenderGraphObject(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DParticleSpriteParticle::ParticleUpdateNode *updateNode,
    QSSGRenderGraphObject *node) {
  self->updateParticleBuffer(updateNode, node);
}

//  void QQuick3DParticleSpriteParticle::updateAnimatedParticleBuffer(Particl
//      eUpdateNode *updateNode, QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle28updateAnimatedParticleBufferEPNS_18ParticleUpdateNodeEP21QSSGRenderGraphObject(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DParticleSpriteParticle::ParticleUpdateNode *updateNode,
    QSSGRenderGraphObject *node) {
  self->updateAnimatedParticleBuffer(updateNode, node);
}

//  void
//      QQuick3DParticleSpriteParticle::updateSceneManager(QQuick3DSceneManag
//      er *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DSceneManager *window) {
  self->updateSceneManager(window);
}

//  void QQuick3DParticleSpriteParticle::updateFeatureLevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle18updateFeatureLevelEv(
    QQuick3DParticleSpriteParticle *self) {
  self->updateFeatureLevel();
}

//  void QQuick3DParticleSpriteParticle::qmlAppendLight(QQmlListProperty<QQui
//      ck3DAbstractLight> *list, QQuick3DAbstractLight *light)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle14qmlAppendLightEP16QQmlListPropertyI21QQuick3DAbstractLightEPS1_(
    QQmlListProperty<QQuick3DAbstractLight> *list,
    QQuick3DAbstractLight *light) {
  QQuick3DParticleSpriteParticle::qmlAppendLight(list, light);
}

//  QQuick3DAbstractLight *QQuick3DParticleSpriteParticle::qmlLightAt(QQmlLis
//      tProperty<QQuick3DAbstractLight> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DAbstractLight *ritual_ZN30QQuick3DParticleSpriteParticle10qmlLightAtEP16QQmlListPropertyI21QQuick3DAbstractLightEx(
    QQmlListProperty<QQuick3DAbstractLight> *list,
    qsizetype index) {
  return QQuick3DParticleSpriteParticle::qmlLightAt(list, index);
}

//  qsizetype QQuick3DParticleSpriteParticle::qmlLightsCount(QQmlListProperty
//      <QQuick3DAbstractLight> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN30QQuick3DParticleSpriteParticle14qmlLightsCountEP16QQmlListPropertyI21QQuick3DAbstractLightE(
    QQmlListProperty<QQuick3DAbstractLight> *list) {
  return QQuick3DParticleSpriteParticle::qmlLightsCount(list);
}

//  void QQuick3DParticleSpriteParticle::qmlClearLights(QQmlListProperty<QQui
//      ck3DAbstractLight> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteParticle14qmlClearLightsEP16QQmlListPropertyI21QQuick3DAbstractLightE(
    QQmlListProperty<QQuick3DAbstractLight> *list) {
  QQuick3DParticleSpriteParticle::qmlClearLights(list);
}

//  a Python function taken by a CuteQQuick3DParticleSpriteParticle, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleSpriteParticle(
    QQuick3DParticleSpriteParticle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleSpriteParticle *>(self)->take(key, call);
}

//  void QQuick3DParticleSpriteParticle::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::itemChange(
      a0,
      *a1);
}

//  void QQuick3DParticleSpriteParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle5resetEv(
    QQuick3DParticleSpriteParticle *self) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::reset();
}

//  void QQuick3DParticleSpriteParticle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle17componentCompleteEv(
    QQuick3DParticleSpriteParticle *self) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::componentComplete();
}

//  int QQuick3DParticleSpriteParticle::nextCurrentIndex(const
//      QQuick3DParticleEmitter *emitter)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN30QQuick3DParticleSpriteParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter(
    QQuick3DParticleSpriteParticle *self,
    const QQuick3DParticleEmitter *emitter) {
  return static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::nextCurrentIndex(
      emitter);
}

//  void QQuick3DParticleSpriteParticle::setParticleData(int particleIndex,
//      const QVector3D &position, const QVector3D &rotation, const QVector4D
//      &color, float size, float age, float animationFrame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle15setParticleDataEiRK9QVector3DS2_RK9QVector4Dfff(
    QQuick3DParticleSpriteParticle *self,
    int particleIndex,
    const QVector3D *position,
    const QVector3D *rotation,
    const QVector4D *color,
    float size,
    float age,
    float animationFrame) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::setParticleData(
      particleIndex,
      *position,
      *rotation,
      *color,
      size,
      age,
      animationFrame);
}

//  void QQuick3DParticleSpriteParticle::resetParticleData(int particleIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle17resetParticleDataEi(
    QQuick3DParticleSpriteParticle *self,
    int particleIndex) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::resetParticleData(
      particleIndex);
}

//  void QQuick3DParticleSpriteParticle::commitParticles(float a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle15commitParticlesEf(
    QQuick3DParticleSpriteParticle *self,
    float a0) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::commitParticles(
      a0);
}

//  void QQuick3DParticleSpriteParticle::setDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle12setDepthBiasEf(
    QQuick3DParticleSpriteParticle *self,
    float bias) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::setDepthBias(
      bias);
}

//  void QQuick3DParticleSpriteParticle::handleMaxAmountChanged(int amount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle22handleMaxAmountChangedEi(
    QQuick3DParticleSpriteParticle *self,
    int amount) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::handleMaxAmountChanged(
      amount);
}

//  void QQuick3DParticleSpriteParticle::handleSystemChanged(QQuick3DParticle
//      System *system)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle19handleSystemChangedEP22QQuick3DParticleSystem(
    QQuick3DParticleSpriteParticle *self,
    QQuick3DParticleSystem *system) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::handleSystemChanged(
      system);
}

//  void QQuick3DParticleSpriteParticle::updateNodeLayers()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteParticle16updateNodeLayersEv(
    QQuick3DParticleSpriteParticle *self) {
  static_cast<OwnQQuick3DParticleSpriteParticle *>(self)->OwnQQuick3DParticleSpriteParticle::updateNodeLayers();
}

//  a QQmlListProperty<QQuick3DAbstractLight> a ritual of
//      QQuick3DParticleSpriteParticle gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DParticleSpriteParticle__QQmlListProperty_QQuick3DAbstractLight(
    QQmlListProperty<QQuick3DAbstractLight> *self) {
  delete self;
}
