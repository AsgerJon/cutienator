//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticleaffector_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleaffector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  A QQuick3DParticleAffector that Python can take functions over in. Every QQuick3DParticleAffector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DParticleAffectorCall0)(const void *, int *);
typedef void (*CuteQQuick3DParticleAffectorCall1)(const void *, int *);
typedef void (*CuteQQuick3DParticleAffectorCall2)(const void *, const QQuick3DParticleData *, QQuick3DParticleDataCurrent *, float, int *);
typedef void (*CuteQQuick3DParticleAffectorCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAffectorCall4)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAffectorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuick3DParticleAffectorCall6)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DParticleAffectorCall7)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DParticleAffectorCall8)(const void *, int *);
typedef void (*CuteQQuick3DParticleAffectorCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleAffectorCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleAffectorCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAffectorCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAffectorCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAffectorCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleAffector : public QQuick3DParticleAffector {
public:
  using QQuick3DParticleAffector::QQuick3DParticleAffector;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuick3DParticleAffector15prepareToAffectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuick3DParticleAffector14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DParticleAffector::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall0 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleAffector::componentComplete();
  }

  //  void QQuick3DParticleAffector::prepareToAffect()
  void prepareToAffect() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall1 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleAffector::prepareToAffect();
  }

  //  void QQuick3DParticleAffector::affectParticle(const
  //      QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float
  //      time)
  void affectParticle(
      const QQuick3DParticleData &sd,
      QQuick3DParticleDataCurrent *d,
      float time) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall2 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall2>(taken[2]);
      call(this, &sd, d, time, &handled);
      if (handled) return;
    }
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall3 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall4 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall4>(taken[4]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall5 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall6 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall7 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall7>(taken[7]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall8 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall9 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall10 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall11 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall12 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall13 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuick3DParticleAffectorCall14 call = reinterpret_cast<CuteQQuick3DParticleAffectorCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuick3DParticleAffector10metaObjectEv(
    const QQuick3DParticleAffector *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleAffector::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuick3DParticleAffector11qt_metacastEPKc(
    QQuick3DParticleAffector *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleAffector::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuick3DParticleAffector11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleAffector *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuick3DParticleAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleAffector::tr(s, c, n));
}

//  void QQuick3DParticleAffector::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector24qt_qmlMarker_uncreatableEv(
    QQuick3DParticleAffector *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DParticleAffector::QQuick3DParticleAffector(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleAffector *ritual_ZN24QQuick3DParticleAffectorC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DParticleAffector(parent);
}

//  QQuick3DParticleAffector::~QQuick3DParticleAffector()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffectorD1Ev(
    QQuick3DParticleAffector *self) {
  delete self;
}

//  QQuick3DParticleSystem *QQuick3DParticleAffector::system() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleSystem *ritual_ZNK24QQuick3DParticleAffector6systemEv(
    const QQuick3DParticleAffector *self) {
  return self->system();
}

//  bool QQuick3DParticleAffector::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DParticleAffector7enabledEv(
    const QQuick3DParticleAffector *self) {
  return self->enabled();
}

//  QQmlListProperty<QQuick3DParticle> QQuick3DParticleAffector::particles()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DParticle> *ritual_ZN24QQuick3DParticleAffector9particlesEv(
    QQuick3DParticleAffector *self) {
  return new QQmlListProperty<QQuick3DParticle>(self->particles());
}

//  void QQuick3DParticleAffector::appendParticle(QQuick3DParticle *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector14appendParticleEP16QQuick3DParticle(
    QQuick3DParticleAffector *self,
    QQuick3DParticle *a0) {
  self->appendParticle(a0);
}

//  qsizetype QQuick3DParticleAffector::particleCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK24QQuick3DParticleAffector13particleCountEv(
    const QQuick3DParticleAffector *self) {
  return self->particleCount();
}

//  QQuick3DParticle *QQuick3DParticleAffector::particle(qsizetype a0) const
extern "C" Q_DECL_EXPORT
QQuick3DParticle *ritual_ZNK24QQuick3DParticleAffector8particleEx(
    const QQuick3DParticleAffector *self,
    qsizetype a0) {
  return self->particle(a0);
}

//  void QQuick3DParticleAffector::clearParticles()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector14clearParticlesEv(
    QQuick3DParticleAffector *self) {
  self->clearParticles();
}

//  void QQuick3DParticleAffector::replaceParticle(qsizetype a0,
//      QQuick3DParticle *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector15replaceParticleExP16QQuick3DParticle(
    QQuick3DParticleAffector *self,
    qsizetype a0,
    QQuick3DParticle *a1) {
  self->replaceParticle(a0, a1);
}

//  void QQuick3DParticleAffector::removeLastParticle()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector18removeLastParticleEv(
    QQuick3DParticleAffector *self) {
  self->removeLastParticle();
}

//  void QQuick3DParticleAffector::setSystem(QQuick3DParticleSystem *system)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector9setSystemEP22QQuick3DParticleSystem(
    QQuick3DParticleAffector *self,
    QQuick3DParticleSystem *system) {
  self->setSystem(system);
}

//  void QQuick3DParticleAffector::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector10setEnabledEb(
    QQuick3DParticleAffector *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QQuick3DParticleAffector::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector6updateEv(
    QQuick3DParticleAffector *self) {
  self->update();
}

//  void QQuick3DParticleAffector::systemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector13systemChangedEv(
    QQuick3DParticleAffector *self) {
  self->systemChanged();
}

//  void QQuick3DParticleAffector::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector14enabledChangedEv(
    QQuick3DParticleAffector *self) {
  self->enabledChanged();
}

//  void QQuick3DParticleAffector::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector17componentCompleteEv(
    QQuick3DParticleAffector *self) {
  self->componentComplete();
}

//  void QQuick3DParticleAffector::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector15prepareToAffectEv(
    QQuick3DParticleAffector *self) {
  self->prepareToAffect();
}

//  void QQuick3DParticleAffector::affectParticle(const QQuick3DParticleData
//      &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleAffector *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  self->affectParticle(*sd, d, time);
}

//  void QQuick3DParticleAffector::appendParticle(QQmlListProperty<QQuick3DPa
//      rticle> *a0, QQuick3DParticle *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector14appendParticleEP16QQmlListPropertyI16QQuick3DParticleEPS1_(
    QQmlListProperty<QQuick3DParticle> *a0,
    QQuick3DParticle *a1) {
  QQuick3DParticleAffector::appendParticle(a0, a1);
}

//  qsizetype QQuick3DParticleAffector::particleCount(QQmlListProperty<QQuick
//      3DParticle> *a0)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN24QQuick3DParticleAffector13particleCountEP16QQmlListPropertyI16QQuick3DParticleE(
    QQmlListProperty<QQuick3DParticle> *a0) {
  return QQuick3DParticleAffector::particleCount(a0);
}

//  QQuick3DParticle
//      *QQuick3DParticleAffector::particle(QQmlListProperty<QQuick3DParticle
//      > *a0, qsizetype a1)
extern "C" Q_DECL_EXPORT
QQuick3DParticle *ritual_ZN24QQuick3DParticleAffector8particleEP16QQmlListPropertyI16QQuick3DParticleEx(
    QQmlListProperty<QQuick3DParticle> *a0,
    qsizetype a1) {
  return QQuick3DParticleAffector::particle(a0, a1);
}

//  void QQuick3DParticleAffector::clearParticles(QQmlListProperty<QQuick3DPa
//      rticle> *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector14clearParticlesEP16QQmlListPropertyI16QQuick3DParticleE(
    QQmlListProperty<QQuick3DParticle> *a0) {
  QQuick3DParticleAffector::clearParticles(a0);
}

//  void QQuick3DParticleAffector::replaceParticle(QQmlListProperty<QQuick3DP
//      article> *a0, qsizetype a1, QQuick3DParticle *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector15replaceParticleEP16QQmlListPropertyI16QQuick3DParticleExPS1_(
    QQmlListProperty<QQuick3DParticle> *a0,
    qsizetype a1,
    QQuick3DParticle *a2) {
  QQuick3DParticleAffector::replaceParticle(a0, a1, a2);
}

//  void QQuick3DParticleAffector::removeLastParticle(QQmlListProperty<QQuick
//      3DParticle> *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleAffector18removeLastParticleEP16QQmlListPropertyI16QQuick3DParticleE(
    QQmlListProperty<QQuick3DParticle> *a0) {
  QQuick3DParticleAffector::removeLastParticle(a0);
}

//  a Python function taken by a CuteQQuick3DParticleAffector, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleAffector(
    QQuick3DParticleAffector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleAffector *>(self)->take(key, call);
}

//  void QQuick3DParticleAffector::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuick3DParticleAffector17componentCompleteEv(
    QQuick3DParticleAffector *self) {
  self->QQuick3DParticleAffector::componentComplete();
}

//  void QQuick3DParticleAffector::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuick3DParticleAffector15prepareToAffectEv(
    QQuick3DParticleAffector *self) {
  self->QQuick3DParticleAffector::prepareToAffect();
}

//  a QQmlListProperty<QQuick3DParticle> a ritual of QQuick3DParticleAffector
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DParticleAffector__QQmlListProperty_QQuick3DParticle(
    QQmlListProperty<QQuick3DParticle> *self) {
  delete self;
}
