//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticleemitter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleemitter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qquaternion.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  Only a class built on QQuick3DParticleEmitter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleEmitter : QQuick3DParticleEmitter {
  using QQuick3DParticleEmitter::componentComplete;
};

//  A QQuick3DParticleEmitter that Python can take functions over in. Every QQuick3DParticleEmitter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DParticleEmitterCall0)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleEmitterCall1)(const void *, int, int, int *);
typedef void (*CuteQQuick3DParticleEmitterCall2)(const void *, int, int, const QVector3D *, int *);
typedef void (*CuteQQuick3DParticleEmitterCall3)(const void *, int *);
typedef void (*CuteQQuick3DParticleEmitterCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuick3DParticleEmitterCall7)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DParticleEmitterCall8)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DParticleEmitterCall9)(const void *, int *);
typedef void (*CuteQQuick3DParticleEmitterCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleEmitterCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleEmitterCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitterCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitterCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitterCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleEmitter : public QQuick3DParticleEmitter {
public:
  using QQuick3DParticleEmitter::QQuick3DParticleEmitter;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QQuick3DParticleEmitter5burstEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQuick3DParticleEmitter5burstEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQuick3DParticleEmitter5burstEiiRK9QVector3D")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
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
    return false;
  }

  //  void QQuick3DParticleEmitter::burst(int count)
  void burst(int count) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall0 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall0>(taken[0]);
      call(this, count, &handled);
      if (handled) return;
    }
    QQuick3DParticleEmitter::burst(count);
  }

  //  void QQuick3DParticleEmitter::burst(int count, int duration)
  void burst(int count, int duration) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall1 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall1>(taken[1]);
      call(this, count, duration, &handled);
      if (handled) return;
    }
    QQuick3DParticleEmitter::burst(count, duration);
  }

  //  void QQuick3DParticleEmitter::burst(int count, int duration, const
  //      QVector3D &position)
  void burst(int count, int duration, const QVector3D &position) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall2 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall2>(taken[2]);
      call(this, count, duration, &position, &handled);
      if (handled) return;
    }
    QQuick3DParticleEmitter::burst(count, duration, position);
  }

  //  void QQuick3DParticleEmitter::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall3 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleEmitter::componentComplete();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall4 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall5 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall6 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall7 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall7>(taken[7]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall8 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall8>(taken[8]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall9 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DParticleEmitterCall10 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall10>(taken[10]);
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
      CuteQQuick3DParticleEmitterCall11 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall11>(taken[11]);
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
      CuteQQuick3DParticleEmitterCall12 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall12>(taken[12]);
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
      CuteQQuick3DParticleEmitterCall13 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall13>(taken[13]);
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
      CuteQQuick3DParticleEmitterCall14 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall14>(taken[14]);
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
      CuteQQuick3DParticleEmitterCall15 call = reinterpret_cast<CuteQQuick3DParticleEmitterCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleEmitter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DParticleEmitter10metaObjectEv(
    const QQuick3DParticleEmitter *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleEmitter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuick3DParticleEmitter11qt_metacastEPKc(
    QQuick3DParticleEmitter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleEmitter::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuick3DParticleEmitter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleEmitter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleEmitter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuick3DParticleEmitter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleEmitter::tr(s, c, n));
}

//  QQuick3DParticleEmitter::QQuick3DParticleEmitter(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleEmitter *ritual_ZN23QQuick3DParticleEmitterC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DParticleEmitter(parent);
}

//  QQuick3DParticleEmitter::~QQuick3DParticleEmitter()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitterD1Ev(QQuick3DParticleEmitter *self) {
  delete self;
}

//  bool QQuick3DParticleEmitter::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuick3DParticleEmitter7enabledEv(
    const QQuick3DParticleEmitter *self) {
  return self->enabled();
}

//  QQuick3DParticleDirection *QQuick3DParticleEmitter::velocity() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleDirection *ritual_ZNK23QQuick3DParticleEmitter8velocityEv(
    const QQuick3DParticleEmitter *self) {
  return self->velocity();
}

//  QQuick3DParticleSystem *QQuick3DParticleEmitter::system() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleSystem *ritual_ZNK23QQuick3DParticleEmitter6systemEv(
    const QQuick3DParticleEmitter *self) {
  return self->system();
}

//  float QQuick3DParticleEmitter::emitRate() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DParticleEmitter8emitRateEv(
    const QQuick3DParticleEmitter *self) {
  return self->emitRate();
}

//  float QQuick3DParticleEmitter::particleScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DParticleEmitter13particleScaleEv(
    const QQuick3DParticleEmitter *self) {
  return self->particleScale();
}

//  float QQuick3DParticleEmitter::particleEndScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DParticleEmitter16particleEndScaleEv(
    const QQuick3DParticleEmitter *self) {
  return self->particleEndScale();
}

//  float QQuick3DParticleEmitter::particleScaleVariation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DParticleEmitter22particleScaleVariationEv(
    const QQuick3DParticleEmitter *self) {
  return self->particleScaleVariation();
}

//  float QQuick3DParticleEmitter::particleEndScaleVariation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DParticleEmitter25particleEndScaleVariationEv(
    const QQuick3DParticleEmitter *self) {
  return self->particleEndScaleVariation();
}

//  int QQuick3DParticleEmitter::lifeSpan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuick3DParticleEmitter8lifeSpanEv(
    const QQuick3DParticleEmitter *self) {
  return self->lifeSpan();
}

//  int QQuick3DParticleEmitter::lifeSpanVariation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuick3DParticleEmitter17lifeSpanVariationEv(
    const QQuick3DParticleEmitter *self) {
  return self->lifeSpanVariation();
}

//  QQuick3DParticle *QQuick3DParticleEmitter::particle() const
extern "C" Q_DECL_EXPORT
QQuick3DParticle *ritual_ZNK23QQuick3DParticleEmitter8particleEv(
    const QQuick3DParticleEmitter *self) {
  return self->particle();
}

//  QQuick3DParticleAbstractShape *QQuick3DParticleEmitter::shape() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleAbstractShape *ritual_ZNK23QQuick3DParticleEmitter5shapeEv(
    const QQuick3DParticleEmitter *self) {
  return self->shape();
}

//  QVector3D QQuick3DParticleEmitter::particleRotation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DParticleEmitter16particleRotationEv(
    const QQuick3DParticleEmitter *self) {
  return new QVector3D(self->particleRotation());
}

//  QVector3D QQuick3DParticleEmitter::particleRotationVariation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DParticleEmitter25particleRotationVariationEv(
    const QQuick3DParticleEmitter *self) {
  return new QVector3D(self->particleRotationVariation());
}

//  QVector3D QQuick3DParticleEmitter::particleRotationVelocity() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DParticleEmitter24particleRotationVelocityEv(
    const QQuick3DParticleEmitter *self) {
  return new QVector3D(self->particleRotationVelocity());
}

//  QVector3D QQuick3DParticleEmitter::particleRotationVelocityVariation()
//      const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DParticleEmitter33particleRotationVelocityVariationEv(
    const QQuick3DParticleEmitter *self) {
  return new QVector3D(self->particleRotationVelocityVariation());
}

//  float QQuick3DParticleEmitter::depthBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DParticleEmitter9depthBiasEv(
    const QQuick3DParticleEmitter *self) {
  return self->depthBias();
}

//  bool QQuick3DParticleEmitter::reversed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuick3DParticleEmitter8reversedEv(
    const QQuick3DParticleEmitter *self) {
  return self->reversed();
}

//  EmitMode QQuick3DParticleEmitter::emitMode() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleEmitter::EmitMode ritual_ZNK23QQuick3DParticleEmitter8emitModeEv(
    const QQuick3DParticleEmitter *self) {
  return self->emitMode();
}

//  QQmlListProperty<QQuick3DParticleEmitBurst>
//      QQuick3DParticleEmitter::emitBursts()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DParticleEmitBurst> *ritual_ZN23QQuick3DParticleEmitter10emitBurstsEv(
    QQuick3DParticleEmitter *self) {
  return new QQmlListProperty<QQuick3DParticleEmitBurst>(self->emitBursts());
}

//  void QQuick3DParticleEmitter::burst(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter5burstEi(
    QQuick3DParticleEmitter *self,
    int count) {
  self->burst(count);
}

//  void QQuick3DParticleEmitter::burst(int count, int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter5burstEii(
    QQuick3DParticleEmitter *self,
    int count,
    int duration) {
  self->burst(count, duration);
}

//  void QQuick3DParticleEmitter::burst(int count, int duration, const
//      QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter5burstEiiRK9QVector3D(
    QQuick3DParticleEmitter *self,
    int count,
    int duration,
    const QVector3D *position) {
  self->burst(count, duration, *position);
}

//  void QQuick3DParticleEmitter::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter10setEnabledEb(
    QQuick3DParticleEmitter *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QQuick3DParticleEmitter::setVelocity(QQuick3DParticleDirection
//      *velocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter11setVelocityEP25QQuick3DParticleDirection(
    QQuick3DParticleEmitter *self,
    QQuick3DParticleDirection *velocity) {
  self->setVelocity(velocity);
}

//  void QQuick3DParticleEmitter::setSystem(QQuick3DParticleSystem *system)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter9setSystemEP22QQuick3DParticleSystem(
    QQuick3DParticleEmitter *self,
    QQuick3DParticleSystem *system) {
  self->setSystem(system);
}

//  void QQuick3DParticleEmitter::setEmitRate(float emitRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter11setEmitRateEf(
    QQuick3DParticleEmitter *self,
    float emitRate) {
  self->setEmitRate(emitRate);
}

//  void QQuick3DParticleEmitter::setParticleScale(float particleScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter16setParticleScaleEf(
    QQuick3DParticleEmitter *self,
    float particleScale) {
  self->setParticleScale(particleScale);
}

//  void QQuick3DParticleEmitter::setParticleEndScale(float particleEndScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter19setParticleEndScaleEf(
    QQuick3DParticleEmitter *self,
    float particleEndScale) {
  self->setParticleEndScale(particleEndScale);
}

//  void QQuick3DParticleEmitter::setParticleScaleVariation(float
//      particleScaleVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter25setParticleScaleVariationEf(
    QQuick3DParticleEmitter *self,
    float particleScaleVariation) {
  self->setParticleScaleVariation(particleScaleVariation);
}

//  void QQuick3DParticleEmitter::setParticleEndScaleVariation(float
//      particleEndScaleVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter28setParticleEndScaleVariationEf(
    QQuick3DParticleEmitter *self,
    float particleEndScaleVariation) {
  self->setParticleEndScaleVariation(particleEndScaleVariation);
}

//  void QQuick3DParticleEmitter::setLifeSpan(int lifeSpan)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter11setLifeSpanEi(
    QQuick3DParticleEmitter *self,
    int lifeSpan) {
  self->setLifeSpan(lifeSpan);
}

//  void QQuick3DParticleEmitter::setLifeSpanVariation(int lifeSpanVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter20setLifeSpanVariationEi(
    QQuick3DParticleEmitter *self,
    int lifeSpanVariation) {
  self->setLifeSpanVariation(lifeSpanVariation);
}

//  void QQuick3DParticleEmitter::setParticle(QQuick3DParticle *particle)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter11setParticleEP16QQuick3DParticle(
    QQuick3DParticleEmitter *self,
    QQuick3DParticle *particle) {
  self->setParticle(particle);
}

//  void QQuick3DParticleEmitter::setShape(QQuick3DParticleAbstractShape
//      *shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter8setShapeEP29QQuick3DParticleAbstractShape(
    QQuick3DParticleEmitter *self,
    QQuick3DParticleAbstractShape *shape) {
  self->setShape(shape);
}

//  void QQuick3DParticleEmitter::setParticleRotation(const QVector3D
//      &particleRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter19setParticleRotationERK9QVector3D(
    QQuick3DParticleEmitter *self,
    const QVector3D *particleRotation) {
  self->setParticleRotation(*particleRotation);
}

//  void QQuick3DParticleEmitter::setParticleRotationVariation(const
//      QVector3D &particleRotationVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter28setParticleRotationVariationERK9QVector3D(
    QQuick3DParticleEmitter *self,
    const QVector3D *particleRotationVariation) {
  self->setParticleRotationVariation(*particleRotationVariation);
}

//  void QQuick3DParticleEmitter::setParticleRotationVelocity(const QVector3D
//      &particleRotationVelocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter27setParticleRotationVelocityERK9QVector3D(
    QQuick3DParticleEmitter *self,
    const QVector3D *particleRotationVelocity) {
  self->setParticleRotationVelocity(*particleRotationVelocity);
}

//  void QQuick3DParticleEmitter::setParticleRotationVelocityVariation(const
//      QVector3D &particleRotationVelocityVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter36setParticleRotationVelocityVariationERK9QVector3D(
    QQuick3DParticleEmitter *self,
    const QVector3D *particleRotationVelocityVariation) {
  self->setParticleRotationVelocityVariation(
      *particleRotationVelocityVariation);
}

//  void QQuick3DParticleEmitter::setDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter12setDepthBiasEf(
    QQuick3DParticleEmitter *self,
    float bias) {
  self->setDepthBias(bias);
}

//  void QQuick3DParticleEmitter::setReversed(bool reversed)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter11setReversedEb(
    QQuick3DParticleEmitter *self,
    bool reversed) {
  self->setReversed(reversed);
}

//  void QQuick3DParticleEmitter::setEmitMode(EmitMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter11setEmitModeENS_8EmitModeE(
    QQuick3DParticleEmitter *self,
    QQuick3DParticleEmitter::EmitMode mode) {
  self->setEmitMode(mode);
}

//  void QQuick3DParticleEmitter::velocityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15velocityChangedEv(
    QQuick3DParticleEmitter *self) {
  self->velocityChanged();
}

//  void QQuick3DParticleEmitter::systemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter13systemChangedEv(
    QQuick3DParticleEmitter *self) {
  self->systemChanged();
}

//  void QQuick3DParticleEmitter::emitRateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15emitRateChangedEv(
    QQuick3DParticleEmitter *self) {
  self->emitRateChanged();
}

//  void QQuick3DParticleEmitter::particleScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter20particleScaleChangedEv(
    QQuick3DParticleEmitter *self) {
  self->particleScaleChanged();
}

//  void QQuick3DParticleEmitter::particleEndScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter23particleEndScaleChangedEv(
    QQuick3DParticleEmitter *self) {
  self->particleEndScaleChanged();
}

//  void QQuick3DParticleEmitter::particleScaleVariationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter29particleScaleVariationChangedEv(
    QQuick3DParticleEmitter *self) {
  self->particleScaleVariationChanged();
}

//  void QQuick3DParticleEmitter::particleEndScaleVariationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter32particleEndScaleVariationChangedEv(
    QQuick3DParticleEmitter *self) {
  self->particleEndScaleVariationChanged();
}

//  void QQuick3DParticleEmitter::lifeSpanChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15lifeSpanChangedEv(
    QQuick3DParticleEmitter *self) {
  self->lifeSpanChanged();
}

//  void QQuick3DParticleEmitter::lifeSpanVariationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter24lifeSpanVariationChangedEv(
    QQuick3DParticleEmitter *self) {
  self->lifeSpanVariationChanged();
}

//  void QQuick3DParticleEmitter::particleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15particleChangedEv(
    QQuick3DParticleEmitter *self) {
  self->particleChanged();
}

//  void QQuick3DParticleEmitter::shapeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter12shapeChangedEv(
    QQuick3DParticleEmitter *self) {
  self->shapeChanged();
}

//  void QQuick3DParticleEmitter::particleRotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter23particleRotationChangedEv(
    QQuick3DParticleEmitter *self) {
  self->particleRotationChanged();
}

//  void QQuick3DParticleEmitter::particleRotationVariationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter32particleRotationVariationChangedEv(
    QQuick3DParticleEmitter *self) {
  self->particleRotationVariationChanged();
}

//  void QQuick3DParticleEmitter::particleRotationVelocityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter31particleRotationVelocityChangedEv(
    QQuick3DParticleEmitter *self) {
  self->particleRotationVelocityChanged();
}

//  void QQuick3DParticleEmitter::particleRotationVariationVelocityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter40particleRotationVariationVelocityChangedEv(
    QQuick3DParticleEmitter *self) {
  self->particleRotationVariationVelocityChanged();
}

//  void QQuick3DParticleEmitter::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter14enabledChangedEv(
    QQuick3DParticleEmitter *self) {
  self->enabledChanged();
}

//  void QQuick3DParticleEmitter::depthBiasChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter16depthBiasChangedEv(
    QQuick3DParticleEmitter *self) {
  self->depthBiasChanged();
}

//  void QQuick3DParticleEmitter::reversedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15reversedChangedEv(
    QQuick3DParticleEmitter *self) {
  self->reversedChanged();
}

//  void QQuick3DParticleEmitter::emitModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15emitModeChangedEv(
    QQuick3DParticleEmitter *self) {
  self->emitModeChanged();
}

//  void QQuick3DParticleEmitter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter17componentCompleteEv(
    QQuick3DParticleEmitter *self) {
  self->componentComplete();
}

//  void QQuick3DParticleEmitter::registerEmitBurst(QQuick3DParticleEmitBurst
//      *emitBurst)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter17registerEmitBurstEP25QQuick3DParticleEmitBurst(
    QQuick3DParticleEmitter *self,
    QQuick3DParticleEmitBurst *emitBurst) {
  self->registerEmitBurst(emitBurst);
}

//  void
//      QQuick3DParticleEmitter::unRegisterEmitBurst(QQuick3DParticleEmitBurs
//      t *emitBurst)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter19unRegisterEmitBurstEP25QQuick3DParticleEmitBurst(
    QQuick3DParticleEmitter *self,
    QQuick3DParticleEmitBurst *emitBurst) {
  self->unRegisterEmitBurst(emitBurst);
}

//  void QQuick3DParticleEmitter::generateEmitBursts()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter18generateEmitBurstsEv(
    QQuick3DParticleEmitter *self) {
  self->generateEmitBursts();
}

//  void QQuick3DParticleEmitter::emitParticle(QQuick3DParticle *particle,
//      float startTime, const QMatrix4x4 &transform, const QQuaternion
//      &parentRotation, const QVector3D &centerPos, int index, const
//      QVector3D &velocity, const QVector3D &normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter12emitParticleEP16QQuick3DParticlefRK10QMatrix4x4RK11QQuaternionRK9QVector3DiSA_SA_(
    QQuick3DParticleEmitter *self,
    QQuick3DParticle *particle,
    float startTime,
    const QMatrix4x4 *transform,
    const QQuaternion *parentRotation,
    const QVector3D *centerPos,
    int index,
    const QVector3D *velocity,
    const QVector3D *normal) {
  self->emitParticle(
      particle,
      startTime,
      *transform,
      *parentRotation,
      *centerPos,
      index,
      *velocity,
      *normal);
}

//  void QQuick3DParticleEmitter::emitParticles()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter13emitParticlesEv(
    QQuick3DParticleEmitter *self) {
  self->emitParticles();
}

//  void QQuick3DParticleEmitter::emitActivationNodeParticles(QQuick3DParticl
//      eModelBlendParticle *particle)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter27emitActivationNodeParticlesEP34QQuick3DParticleModelBlendParticle(
    QQuick3DParticleEmitter *self,
    QQuick3DParticleModelBlendParticle *particle) {
  self->emitActivationNodeParticles(particle);
}

//  void QQuick3DParticleEmitter::emitParticlesBurst(const
//      QQuick3DParticleEmitBurstData &burst)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter18emitParticlesBurstERK29QQuick3DParticleEmitBurstData(
    QQuick3DParticleEmitter *self,
    const QQuick3DParticleEmitBurstData *burst) {
  self->emitParticlesBurst(*burst);
}

//  int QQuick3DParticleEmitter::getEmitAmount()
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuick3DParticleEmitter13getEmitAmountEv(
    QQuick3DParticleEmitter *self) {
  return self->getEmitAmount();
}

//  int QQuick3DParticleEmitter::getEmitAmountFromDynamicBursts(int
//      triggerType)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuick3DParticleEmitter30getEmitAmountFromDynamicBurstsEi(
    QQuick3DParticleEmitter *self,
    int triggerType) {
  return self->getEmitAmountFromDynamicBursts(triggerType);
}

//  void QQuick3DParticleEmitter::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter5resetEv(
    QQuick3DParticleEmitter *self) {
  self->reset();
}

//  void QQuick3DParticleEmitter::appendEmitBurst(QQuick3DParticleEmitBurst
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15appendEmitBurstEP25QQuick3DParticleEmitBurst(
    QQuick3DParticleEmitter *self,
    QQuick3DParticleEmitBurst *a0) {
  self->appendEmitBurst(a0);
}

//  qsizetype QQuick3DParticleEmitter::emitBurstCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QQuick3DParticleEmitter14emitBurstCountEv(
    const QQuick3DParticleEmitter *self) {
  return self->emitBurstCount();
}

//  QQuick3DParticleEmitBurst *QQuick3DParticleEmitter::emitBurst(qsizetype
//      a0) const
extern "C" Q_DECL_EXPORT
QQuick3DParticleEmitBurst *ritual_ZNK23QQuick3DParticleEmitter9emitBurstEx(
    const QQuick3DParticleEmitter *self,
    qsizetype a0) {
  return self->emitBurst(a0);
}

//  void QQuick3DParticleEmitter::clearEmitBursts()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15clearEmitBurstsEv(
    QQuick3DParticleEmitter *self) {
  self->clearEmitBursts();
}

//  void QQuick3DParticleEmitter::replaceEmitBurst(qsizetype a0,
//      QQuick3DParticleEmitBurst *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter16replaceEmitBurstExP25QQuick3DParticleEmitBurst(
    QQuick3DParticleEmitter *self,
    qsizetype a0,
    QQuick3DParticleEmitBurst *a1) {
  self->replaceEmitBurst(a0, a1);
}

//  void QQuick3DParticleEmitter::removeLastEmitBurst()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter19removeLastEmitBurstEv(
    QQuick3DParticleEmitter *self) {
  self->removeLastEmitBurst();
}

//  void QQuick3DParticleEmitter::appendEmitBurst(QQmlListProperty<QQuick3DPa
//      rticleEmitBurst> *a0, QQuick3DParticleEmitBurst *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15appendEmitBurstEP16QQmlListPropertyI25QQuick3DParticleEmitBurstEPS1_(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0,
    QQuick3DParticleEmitBurst *a1) {
  QQuick3DParticleEmitter::appendEmitBurst(a0, a1);
}

//  qsizetype QQuick3DParticleEmitter::emitBurstCount(QQmlListProperty<QQuick
//      3DParticleEmitBurst> *a0)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN23QQuick3DParticleEmitter14emitBurstCountEP16QQmlListPropertyI25QQuick3DParticleEmitBurstE(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0) {
  return QQuick3DParticleEmitter::emitBurstCount(a0);
}

//  QQuick3DParticleEmitBurst *QQuick3DParticleEmitter::emitBurst(QQmlListPro
//      perty<QQuick3DParticleEmitBurst> *a0, qsizetype a1)
extern "C" Q_DECL_EXPORT
QQuick3DParticleEmitBurst *ritual_ZN23QQuick3DParticleEmitter9emitBurstEP16QQmlListPropertyI25QQuick3DParticleEmitBurstEx(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0,
    qsizetype a1) {
  return QQuick3DParticleEmitter::emitBurst(a0, a1);
}

//  void QQuick3DParticleEmitter::clearEmitBursts(QQmlListProperty<QQuick3DPa
//      rticleEmitBurst> *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter15clearEmitBurstsEP16QQmlListPropertyI25QQuick3DParticleEmitBurstE(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0) {
  QQuick3DParticleEmitter::clearEmitBursts(a0);
}

//  void QQuick3DParticleEmitter::replaceEmitBurst(QQmlListProperty<QQuick3DP
//      articleEmitBurst> *a0, qsizetype a1, QQuick3DParticleEmitBurst *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter16replaceEmitBurstEP16QQmlListPropertyI25QQuick3DParticleEmitBurstExPS1_(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0,
    qsizetype a1,
    QQuick3DParticleEmitBurst *a2) {
  QQuick3DParticleEmitter::replaceEmitBurst(a0, a1, a2);
}

//  void QQuick3DParticleEmitter::removeLastEmitBurst(QQmlListProperty<QQuick
//      3DParticleEmitBurst> *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleEmitter19removeLastEmitBurstEP16QQmlListPropertyI25QQuick3DParticleEmitBurstE(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0) {
  QQuick3DParticleEmitter::removeLastEmitBurst(a0);
}

//  a Python function taken by a CuteQQuick3DParticleEmitter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleEmitter(
    QQuick3DParticleEmitter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleEmitter *>(self)->take(key, call);
}

//  void QQuick3DParticleEmitter::burst(int count)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DParticleEmitter5burstEi(
    QQuick3DParticleEmitter *self,
    int count) {
  self->QQuick3DParticleEmitter::burst(count);
}

//  void QQuick3DParticleEmitter::burst(int count, int duration)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DParticleEmitter5burstEii(
    QQuick3DParticleEmitter *self,
    int count,
    int duration) {
  self->QQuick3DParticleEmitter::burst(count, duration);
}

//  void QQuick3DParticleEmitter::burst(int count, int duration, const
//      QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DParticleEmitter5burstEiiRK9QVector3D(
    QQuick3DParticleEmitter *self,
    int count,
    int duration,
    const QVector3D *position) {
  self->QQuick3DParticleEmitter::burst(count, duration, *position);
}

//  void QQuick3DParticleEmitter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DParticleEmitter17componentCompleteEv(
    QQuick3DParticleEmitter *self) {
  static_cast<OwnQQuick3DParticleEmitter *>(self)->OwnQQuick3DParticleEmitter::componentComplete();
}

//  a QQmlListProperty<QQuick3DParticleEmitBurst> a ritual of
//      QQuick3DParticleEmitter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DParticleEmitter__QQmlListProperty_QQuick3DParticleEmitBurst(
    QQmlListProperty<QQuick3DParticleEmitBurst> *self) {
  delete self;
}
