//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlelineparticle_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlelineparticle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DParticleLineParticle that Python can take functions over in. Every QQuick3DParticleLineParticle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DParticleLineParticleCall0)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall1)(const void *, QQuick3DParticleSystem *, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall2)(const void *, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall3)(const void *, float, int *);
typedef int (*CuteQQuick3DParticleLineParticleCall4)(const void *, const QQuick3DParticleEmitter *, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall5)(const void *, int, const QVector3D *, const QVector3D *, const QVector4D *, float, float, float, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall6)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall7)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall8)(const void *, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall9)(const void *, float, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall10)(const void *, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall11)(const void *, int, int *);
typedef void * (*CuteQQuick3DParticleLineParticleCall12)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall13)(const void *, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall14)(const void *, int *);
typedef void (*CuteQQuick3DParticleLineParticleCall15)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleLineParticleCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleLineParticleCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleLineParticleCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleLineParticleCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleLineParticleCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleLineParticleCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleLineParticleCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleLineParticle : public QQuick3DParticleLineParticle {
public:
  using QQuick3DParticleLineParticle::QQuick3DParticleLineParticle;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle22handleMaxAmountChangedEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle19handleSystemChangedEP22QQuick3DParticleSystem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle5resetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle15commitParticlesEf")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle15setParticleDataEiRK9QVector3DS2_RK9QVector4Dfff")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DParticleSpriteParticle17resetParticleDataEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuick3DParticle12setDepthBiasEf")) {
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

  //  void QQuick3DParticleLineParticle::handleMaxAmountChanged(int amount)
  void handleMaxAmountChanged(int amount) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall0 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall0>(taken[0]);
      call(this, amount, &handled);
      if (handled) return;
    }
    QQuick3DParticleLineParticle::handleMaxAmountChanged(amount);
  }

  //  void QQuick3DParticleLineParticle::handleSystemChanged(QQuick3DPartic
  //      leSystem *system)
  void handleSystemChanged(QQuick3DParticleSystem *system) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall1 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall1>(taken[1]);
      call(this, system, &handled);
      if (handled) return;
    }
    QQuick3DParticleLineParticle::handleSystemChanged(system);
  }

  //  void QQuick3DParticleLineParticle::reset()
  void reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall2 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleLineParticle::reset();
  }

  //  void QQuick3DParticleLineParticle::commitParticles(float time)
  void commitParticles(float time) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall3 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall3>(taken[3]);
      call(this, time, &handled);
      if (handled) return;
    }
    QQuick3DParticleLineParticle::commitParticles(time);
  }

  //  int QQuick3DParticleLineParticle::nextCurrentIndex(const
  //      QQuick3DParticleEmitter *emitter)
  int nextCurrentIndex(const QQuick3DParticleEmitter *emitter) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall4 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall4>(taken[4]);
      int given = call(this, emitter, &handled);
      if (handled) return given;
    }
    return QQuick3DParticleLineParticle::nextCurrentIndex(emitter);
  }

  //  void QQuick3DParticleLineParticle::setParticleData(int particleIndex,
  //      const QVector3D &position, const QVector3D &rotation, const
  //      QVector4D &color, float size, float age, float animationFrame)
  void setParticleData(
      int particleIndex,
      const QVector3D &position,
      const QVector3D &rotation,
      const QVector4D &color,
      float size,
      float age,
      float animationFrame) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall5 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall5>(taken[5]);
      call(this, particleIndex, &position, &rotation, &color, size, age, animationFrame, &handled);
      if (handled) return;
    }
    QQuick3DParticleLineParticle::setParticleData(particleIndex, position, rotation, color, size, age, animationFrame);
  }

  //  void QQuick3DParticleLineParticle::resetParticleData(int
  //      particleIndex)
  void resetParticleData(int particleIndex) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall6 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall6>(taken[6]);
      call(this, particleIndex, &handled);
      if (handled) return;
    }
    QQuick3DParticleLineParticle::resetParticleData(particleIndex);
  }

  //  void QQuick3DParticleSpriteParticle::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall7 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall7>(taken[7]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::itemChange(a0, a1);
  }

  //  void QQuick3DParticleSpriteParticle::componentComplete()
  void componentComplete() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall8 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::componentComplete();
  }

  //  void QQuick3DParticleSpriteParticle::setDepthBias(float bias)
  void setDepthBias(float bias) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall9 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall9>(taken[9]);
      call(this, bias, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::setDepthBias(bias);
  }

  //  void QQuick3DParticleSpriteParticle::updateNodeLayers()
  void updateNodeLayers() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall10 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteParticle::updateNodeLayers();
  }

  //  void QQuick3DParticle::doSetMaxAmount(int amount)
  void doSetMaxAmount(int amount) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall11 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall11>(taken[11]);
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
      CuteQQuick3DParticleLineParticleCall12 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall12>(taken[12]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DParticle::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall13 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall14 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuick3DParticleLineParticleCall15 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall15>(taken[15]);
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
      CuteQQuick3DParticleLineParticleCall16 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall16>(taken[16]);
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
      CuteQQuick3DParticleLineParticleCall17 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall17>(taken[17]);
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
      CuteQQuick3DParticleLineParticleCall18 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall18>(taken[18]);
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
      CuteQQuick3DParticleLineParticleCall19 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall19>(taken[19]);
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
      CuteQQuick3DParticleLineParticleCall20 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall20>(taken[20]);
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
      CuteQQuick3DParticleLineParticleCall21 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall21>(taken[21]);
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
      CuteQQuick3DParticleLineParticleCall22 call = reinterpret_cast<CuteQQuick3DParticleLineParticleCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleLineParticle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuick3DParticleLineParticle10metaObjectEv(
    const QQuick3DParticleLineParticle *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleLineParticle::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuick3DParticleLineParticle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleLineParticle::tr(s, c, n));
}

//  QQuick3DParticleLineParticle::QQuick3DParticleLineParticle(QQuick3DNode
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleLineParticle *ritual_ZN28QQuick3DParticleLineParticleC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DParticleLineParticle(parent);
}

//  QQuick3DParticleLineParticle::~QQuick3DParticleLineParticle()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticleD1Ev(
    QQuick3DParticleLineParticle *self) {
  delete self;
}

//  int QQuick3DParticleLineParticle::segmentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuick3DParticleLineParticle12segmentCountEv(
    const QQuick3DParticleLineParticle *self) {
  return self->segmentCount();
}

//  float QQuick3DParticleLineParticle::alphaFade() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK28QQuick3DParticleLineParticle9alphaFadeEv(
    const QQuick3DParticleLineParticle *self) {
  return self->alphaFade();
}

//  float QQuick3DParticleLineParticle::scaleMultiplier() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK28QQuick3DParticleLineParticle15scaleMultiplierEv(
    const QQuick3DParticleLineParticle *self) {
  return self->scaleMultiplier();
}

//  float QQuick3DParticleLineParticle::texcoordMultiplier() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK28QQuick3DParticleLineParticle18texcoordMultiplierEv(
    const QQuick3DParticleLineParticle *self) {
  return self->texcoordMultiplier();
}

//  float QQuick3DParticleLineParticle::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK28QQuick3DParticleLineParticle6lengthEv(
    const QQuick3DParticleLineParticle *self) {
  return self->length();
}

//  float QQuick3DParticleLineParticle::lengthVariation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK28QQuick3DParticleLineParticle15lengthVariationEv(
    const QQuick3DParticleLineParticle *self) {
  return self->lengthVariation();
}

//  float QQuick3DParticleLineParticle::lengthDeltaMin() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK28QQuick3DParticleLineParticle14lengthDeltaMinEv(
    const QQuick3DParticleLineParticle *self) {
  return self->lengthDeltaMin();
}

//  int QQuick3DParticleLineParticle::eolFadeOutDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuick3DParticleLineParticle18eolFadeOutDurationEv(
    const QQuick3DParticleLineParticle *self) {
  return self->eolFadeOutDuration();
}

//  TexcoordMode QQuick3DParticleLineParticle::texcoordMode() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleLineParticle::TexcoordMode ritual_ZNK28QQuick3DParticleLineParticle12texcoordModeEv(
    const QQuick3DParticleLineParticle *self) {
  return self->texcoordMode();
}

//  void QQuick3DParticleLineParticle::setSegmentCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle15setSegmentCountEi(
    QQuick3DParticleLineParticle *self,
    int count) {
  self->setSegmentCount(count);
}

//  void QQuick3DParticleLineParticle::setAlphaFade(float fade)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle12setAlphaFadeEf(
    QQuick3DParticleLineParticle *self,
    float fade) {
  self->setAlphaFade(fade);
}

//  void QQuick3DParticleLineParticle::setScaleMultiplier(float multiplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle18setScaleMultiplierEf(
    QQuick3DParticleLineParticle *self,
    float multiplier) {
  self->setScaleMultiplier(multiplier);
}

//  void QQuick3DParticleLineParticle::setTexcoordMultiplier(float
//      multiplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle21setTexcoordMultiplierEf(
    QQuick3DParticleLineParticle *self,
    float multiplier) {
  self->setTexcoordMultiplier(multiplier);
}

//  void QQuick3DParticleLineParticle::setLength(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle9setLengthEf(
    QQuick3DParticleLineParticle *self,
    float length) {
  self->setLength(length);
}

//  void QQuick3DParticleLineParticle::setLengthVariation(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle18setLengthVariationEf(
    QQuick3DParticleLineParticle *self,
    float length) {
  self->setLengthVariation(length);
}

//  void QQuick3DParticleLineParticle::setLengthDeltaMin(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle17setLengthDeltaMinEf(
    QQuick3DParticleLineParticle *self,
    float min) {
  self->setLengthDeltaMin(min);
}

//  void QQuick3DParticleLineParticle::setEolFadeOutDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle21setEolFadeOutDurationEi(
    QQuick3DParticleLineParticle *self,
    int duration) {
  self->setEolFadeOutDuration(duration);
}

//  void QQuick3DParticleLineParticle::setTexcoordMode(QQuick3DParticleLinePa
//      rticle::TexcoordMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle15setTexcoordModeENS_12TexcoordModeE(
    QQuick3DParticleLineParticle *self,
    QQuick3DParticleLineParticle::TexcoordMode mode) {
  self->setTexcoordMode(mode);
}

//  QSSGRenderGraphObject
//      *QQuick3DParticleLineParticle::updateLineNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN28QQuick3DParticleLineParticle14updateLineNodeEP21QSSGRenderGraphObject(
    QQuick3DParticleLineParticle *self,
    QSSGRenderGraphObject *node) {
  return self->updateLineNode(node);
}

//  void QQuick3DParticleLineParticle::handleSegmentCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle25handleSegmentCountChangedEv(
    QQuick3DParticleLineParticle *self) {
  self->handleSegmentCountChanged();
}

//  void QQuick3DParticleLineParticle::updateLineSegment(int particleIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle17updateLineSegmentEi(
    QQuick3DParticleLineParticle *self,
    int particleIndex) {
  self->updateLineSegment(particleIndex);
}

//  void QQuick3DParticleLineParticle::clearSegment(int particleIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle12clearSegmentEi(
    QQuick3DParticleLineParticle *self,
    int particleIndex) {
  self->clearSegment(particleIndex);
}

//  void QQuick3DParticleLineParticle::handleMaxAmountChanged(int amount)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle22handleMaxAmountChangedEi(
    QQuick3DParticleLineParticle *self,
    int amount) {
  self->handleMaxAmountChanged(amount);
}

//  void
//      QQuick3DParticleLineParticle::handleSystemChanged(QQuick3DParticleSys
//      tem *system)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle19handleSystemChangedEP22QQuick3DParticleSystem(
    QQuick3DParticleLineParticle *self,
    QQuick3DParticleSystem *system) {
  self->handleSystemChanged(system);
}

//  void QQuick3DParticleLineParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle5resetEv(
    QQuick3DParticleLineParticle *self) {
  self->reset();
}

//  void QQuick3DParticleLineParticle::commitParticles(float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle15commitParticlesEf(
    QQuick3DParticleLineParticle *self,
    float time) {
  self->commitParticles(time);
}

//  int QQuick3DParticleLineParticle::nextCurrentIndex(const
//      QQuick3DParticleEmitter *emitter)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuick3DParticleLineParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter(
    QQuick3DParticleLineParticle *self,
    const QQuick3DParticleEmitter *emitter) {
  return self->nextCurrentIndex(emitter);
}

//  void QQuick3DParticleLineParticle::saveLineSegment(int particleIndex,
//      float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle15saveLineSegmentEif(
    QQuick3DParticleLineParticle *self,
    int particleIndex,
    float time) {
  self->saveLineSegment(particleIndex, time);
}

//  void QQuick3DParticleLineParticle::setParticleData(int particleIndex,
//      const QVector3D &position, const QVector3D &rotation, const QVector4D
//      &color, float size, float age, float animationFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle15setParticleDataEiRK9QVector3DS2_RK9QVector4Dfff(
    QQuick3DParticleLineParticle *self,
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

//  void QQuick3DParticleLineParticle::resetParticleData(int particleIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleLineParticle17resetParticleDataEi(
    QQuick3DParticleLineParticle *self,
    int particleIndex) {
  self->resetParticleData(particleIndex);
}

//  a Python function taken by a CuteQQuick3DParticleLineParticle, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleLineParticle(
    QQuick3DParticleLineParticle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleLineParticle *>(self)->take(key, call);
}

//  void QQuick3DParticleLineParticle::handleMaxAmountChanged(int amount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticleLineParticle22handleMaxAmountChangedEi(
    QQuick3DParticleLineParticle *self,
    int amount) {
  self->QQuick3DParticleLineParticle::handleMaxAmountChanged(amount);
}

//  void
//      QQuick3DParticleLineParticle::handleSystemChanged(QQuick3DParticleSys
//      tem *system)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticleLineParticle19handleSystemChangedEP22QQuick3DParticleSystem(
    QQuick3DParticleLineParticle *self,
    QQuick3DParticleSystem *system) {
  self->QQuick3DParticleLineParticle::handleSystemChanged(system);
}

//  void QQuick3DParticleLineParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticleLineParticle5resetEv(
    QQuick3DParticleLineParticle *self) {
  self->QQuick3DParticleLineParticle::reset();
}

//  void QQuick3DParticleLineParticle::commitParticles(float time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticleLineParticle15commitParticlesEf(
    QQuick3DParticleLineParticle *self,
    float time) {
  self->QQuick3DParticleLineParticle::commitParticles(time);
}

//  int QQuick3DParticleLineParticle::nextCurrentIndex(const
//      QQuick3DParticleEmitter *emitter)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN28QQuick3DParticleLineParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter(
    QQuick3DParticleLineParticle *self,
    const QQuick3DParticleEmitter *emitter) {
  return self->QQuick3DParticleLineParticle::nextCurrentIndex(emitter);
}

//  void QQuick3DParticleLineParticle::setParticleData(int particleIndex,
//      const QVector3D &position, const QVector3D &rotation, const QVector4D
//      &color, float size, float age, float animationFrame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticleLineParticle15setParticleDataEiRK9QVector3DS2_RK9QVector4Dfff(
    QQuick3DParticleLineParticle *self,
    int particleIndex,
    const QVector3D *position,
    const QVector3D *rotation,
    const QVector4D *color,
    float size,
    float age,
    float animationFrame) {
  self->QQuick3DParticleLineParticle::setParticleData(
      particleIndex,
      *position,
      *rotation,
      *color,
      size,
      age,
      animationFrame);
}

//  void QQuick3DParticleLineParticle::resetParticleData(int particleIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticleLineParticle17resetParticleDataEi(
    QQuick3DParticleLineParticle *self,
    int particleIndex) {
  self->QQuick3DParticleLineParticle::resetParticleData(particleIndex);
}
