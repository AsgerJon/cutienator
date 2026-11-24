//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticle_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DParticle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticle : QQuick3DParticle {
  using QQuick3DParticle::componentComplete;
  using QQuick3DParticle::reset;
  using QQuick3DParticle::doSetMaxAmount;
  using QQuick3DParticle::updateNodeLayers;
  using QQuick3DParticle::nextCurrentIndex;
  using QQuick3DParticle::updateSpatialNode;
  using QQuick3DParticle::setDepthBias;
};

//  A QQuick3DParticle that Python can take functions over in. Every QQuick3DParticle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DParticleCall0)(const void *, int *);
typedef void (*CuteQQuick3DParticleCall1)(const void *, int *);
typedef void (*CuteQQuick3DParticleCall2)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleCall3)(const void *, int *);
typedef int (*CuteQQuick3DParticleCall4)(const void *, const QQuick3DParticleEmitter *, int *);
typedef void * (*CuteQQuick3DParticleCall5)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DParticleCall6)(const void *, float, int *);
typedef void (*CuteQQuick3DParticleCall7)(const void *, int *);
typedef void (*CuteQQuick3DParticleCall8)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DParticleCall9)(const void *, int *);
typedef void (*CuteQQuick3DParticleCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticle : public QQuick3DParticle {
public:
  using QQuick3DParticle::QQuick3DParticle;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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
    if (!std::strcmp(key, "_ZN16QQuick3DParticle16updateNodeLayersEv")) {
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
    if (!std::strcmp(key, "_ZN16QQuick3DParticle12setDepthBiasEf")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
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

  //  void QQuick3DParticle::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleCall0 call = reinterpret_cast<CuteQQuick3DParticleCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticle::componentComplete();
  }

  //  void QQuick3DParticle::reset()
  void reset() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleCall1 call = reinterpret_cast<CuteQQuick3DParticleCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticle::reset();
  }

  //  void QQuick3DParticle::doSetMaxAmount(int amount)
  void doSetMaxAmount(int amount) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleCall2 call = reinterpret_cast<CuteQQuick3DParticleCall2>(taken[2]);
      call(this, amount, &handled);
      if (handled) return;
    }
    QQuick3DParticle::doSetMaxAmount(amount);
  }

  //  void QQuick3DParticle::updateNodeLayers()
  void updateNodeLayers() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleCall3 call = reinterpret_cast<CuteQQuick3DParticleCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticle::updateNodeLayers();
  }

  //  int QQuick3DParticle::nextCurrentIndex(const QQuick3DParticleEmitter
  //      *emitter)
  int nextCurrentIndex(const QQuick3DParticleEmitter *emitter) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleCall4 call = reinterpret_cast<CuteQQuick3DParticleCall4>(taken[4]);
      int given = call(this, emitter, &handled);
      if (handled) return given;
    }
    return QQuick3DParticle::nextCurrentIndex(emitter);
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DParticle::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleCall5 call = reinterpret_cast<CuteQQuick3DParticleCall5>(taken[5]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DParticle::updateSpatialNode(node);
  }

  //  void QQuick3DParticle::setDepthBias(float bias)
  void setDepthBias(float bias) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleCall6 call = reinterpret_cast<CuteQQuick3DParticleCall6>(taken[6]);
      call(this, bias, &handled);
      if (handled) return;
    }
    QQuick3DParticle::setDepthBias(bias);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleCall7 call = reinterpret_cast<CuteQQuick3DParticleCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DParticleCall8 call = reinterpret_cast<CuteQQuick3DParticleCall8>(taken[8]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DParticleCall9 call = reinterpret_cast<CuteQQuick3DParticleCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DParticleCall10 call = reinterpret_cast<CuteQQuick3DParticleCall10>(taken[10]);
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
      CuteQQuick3DParticleCall11 call = reinterpret_cast<CuteQQuick3DParticleCall11>(taken[11]);
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
      CuteQQuick3DParticleCall12 call = reinterpret_cast<CuteQQuick3DParticleCall12>(taken[12]);
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
      CuteQQuick3DParticleCall13 call = reinterpret_cast<CuteQQuick3DParticleCall13>(taken[13]);
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
      CuteQQuick3DParticleCall14 call = reinterpret_cast<CuteQQuick3DParticleCall14>(taken[14]);
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
      CuteQQuick3DParticleCall15 call = reinterpret_cast<CuteQQuick3DParticleCall15>(taken[15]);
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
      CuteQQuick3DParticleCall16 call = reinterpret_cast<CuteQQuick3DParticleCall16>(taken[16]);
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
      CuteQQuick3DParticleCall17 call = reinterpret_cast<CuteQQuick3DParticleCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuick3DParticle10metaObjectEv(
    const QQuick3DParticle *self) {
  return self->metaObject();
}

//  QString QQuick3DParticle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuick3DParticle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticle::tr(s, c, n));
}

//  void QQuick3DParticle::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle24qt_qmlMarker_uncreatableEv(
    QQuick3DParticle *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DParticle::QQuick3DParticle(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticle *ritual_ZN16QQuick3DParticleC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DParticle(parent);
}

//  QQuick3DParticle::~QQuick3DParticle()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticleD1Ev(QQuick3DParticle *self) {
  delete self;
}

//  QQuick3DParticleSystem *QQuick3DParticle::system() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleSystem *ritual_ZNK16QQuick3DParticle6systemEv(
    const QQuick3DParticle *self) {
  return self->system();
}

//  int QQuick3DParticle::maxAmount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DParticle9maxAmountEv(const QQuick3DParticle *self) {
  return self->maxAmount();
}

//  QColor QQuick3DParticle::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuick3DParticle5colorEv(const QQuick3DParticle *self) {
  return new QColor(self->color());
}

//  QVector4D QQuick3DParticle::colorVariation() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK16QQuick3DParticle14colorVariationEv(
    const QQuick3DParticle *self) {
  return new QVector4D(self->colorVariation());
}

//  bool QQuick3DParticle::unifiedColorVariation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuick3DParticle21unifiedColorVariationEv(
    const QQuick3DParticle *self) {
  return self->unifiedColorVariation();
}

//  FadeType QQuick3DParticle::fadeInEffect() const
extern "C" Q_DECL_EXPORT
QQuick3DParticle::FadeType ritual_ZNK16QQuick3DParticle12fadeInEffectEv(
    const QQuick3DParticle *self) {
  return self->fadeInEffect();
}

//  FadeType QQuick3DParticle::fadeOutEffect() const
extern "C" Q_DECL_EXPORT
QQuick3DParticle::FadeType ritual_ZNK16QQuick3DParticle13fadeOutEffectEv(
    const QQuick3DParticle *self) {
  return self->fadeOutEffect();
}

//  int QQuick3DParticle::fadeInDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DParticle14fadeInDurationEv(
    const QQuick3DParticle *self) {
  return self->fadeInDuration();
}

//  int QQuick3DParticle::fadeOutDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DParticle15fadeOutDurationEv(
    const QQuick3DParticle *self) {
  return self->fadeOutDuration();
}

//  AlignMode QQuick3DParticle::alignMode() const
extern "C" Q_DECL_EXPORT
QQuick3DParticle::AlignMode ritual_ZNK16QQuick3DParticle9alignModeEv(
    const QQuick3DParticle *self) {
  return self->alignMode();
}

//  QVector3D QQuick3DParticle::alignTargetPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuick3DParticle19alignTargetPositionEv(
    const QQuick3DParticle *self) {
  return new QVector3D(self->alignTargetPosition());
}

//  bool QQuick3DParticle::hasTransparency() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuick3DParticle15hasTransparencyEv(
    const QQuick3DParticle *self) {
  return self->hasTransparency();
}

//  SortMode QQuick3DParticle::sortMode() const
extern "C" Q_DECL_EXPORT
QQuick3DParticle::SortMode ritual_ZNK16QQuick3DParticle8sortModeEv(
    const QQuick3DParticle *self) {
  return self->sortMode();
}

//  float QQuick3DParticle::opacity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuick3DParticle7opacityEv(const QQuick3DParticle *self) {
  return self->opacity();
}

//  void QQuick3DParticle::resetColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle10resetColorEv(QQuick3DParticle *self) {
  self->resetColor();
}

//  void QQuick3DParticle::setSystem(QQuick3DParticleSystem *system)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle9setSystemEP22QQuick3DParticleSystem(
    QQuick3DParticle *self,
    QQuick3DParticleSystem *system) {
  self->setSystem(system);
}

//  void QQuick3DParticle::setMaxAmount(int maxAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle12setMaxAmountEi(
    QQuick3DParticle *self,
    int maxAmount) {
  self->setMaxAmount(maxAmount);
}

//  void QQuick3DParticle::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle8setColorE6QColor(
    QQuick3DParticle *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuick3DParticle::setColorVariation(QVector4D colorVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle17setColorVariationE9QVector4D(
    QQuick3DParticle *self,
    const QVector4D *colorVariation) {
  self->setColorVariation(*colorVariation);
}

//  void QQuick3DParticle::setUnifiedColorVariation(bool unified)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle24setUnifiedColorVariationEb(
    QQuick3DParticle *self,
    bool unified) {
  self->setUnifiedColorVariation(unified);
}

//  void QQuick3DParticle::setFadeInEffect(QQuick3DParticle::FadeType
//      fadeInEffect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle15setFadeInEffectENS_8FadeTypeE(
    QQuick3DParticle *self,
    QQuick3DParticle::FadeType fadeInEffect) {
  self->setFadeInEffect(fadeInEffect);
}

//  void QQuick3DParticle::setFadeOutEffect(QQuick3DParticle::FadeType
//      fadeOutEffect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle16setFadeOutEffectENS_8FadeTypeE(
    QQuick3DParticle *self,
    QQuick3DParticle::FadeType fadeOutEffect) {
  self->setFadeOutEffect(fadeOutEffect);
}

//  void QQuick3DParticle::setFadeInDuration(int fadeInDuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle17setFadeInDurationEi(
    QQuick3DParticle *self,
    int fadeInDuration) {
  self->setFadeInDuration(fadeInDuration);
}

//  void QQuick3DParticle::setFadeOutDuration(int fadeOutDuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle18setFadeOutDurationEi(
    QQuick3DParticle *self,
    int fadeOutDuration) {
  self->setFadeOutDuration(fadeOutDuration);
}

//  void QQuick3DParticle::setAlignMode(QQuick3DParticle::AlignMode
//      alignMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle12setAlignModeENS_9AlignModeE(
    QQuick3DParticle *self,
    QQuick3DParticle::AlignMode alignMode) {
  self->setAlignMode(alignMode);
}

//  void QQuick3DParticle::setAlignTargetPosition(const QVector3D
//      &alignPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle22setAlignTargetPositionERK9QVector3D(
    QQuick3DParticle *self,
    const QVector3D *alignPosition) {
  self->setAlignTargetPosition(*alignPosition);
}

//  void QQuick3DParticle::setHasTransparency(bool transparency)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle18setHasTransparencyEb(
    QQuick3DParticle *self,
    bool transparency) {
  self->setHasTransparency(transparency);
}

//  void QQuick3DParticle::setSortMode(QQuick3DParticle::SortMode sortMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle11setSortModeENS_8SortModeE(
    QQuick3DParticle *self,
    QQuick3DParticle::SortMode sortMode) {
  self->setSortMode(sortMode);
}

//  void QQuick3DParticle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle17componentCompleteEv(
    QQuick3DParticle *self) {
  self->componentComplete();
}

//  void QQuick3DParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle5resetEv(QQuick3DParticle *self) {
  self->reset();
}

//  void QQuick3DParticle::doSetMaxAmount(int amount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle14doSetMaxAmountEi(
    QQuick3DParticle *self,
    int amount) {
  self->doSetMaxAmount(amount);
}

//  void QQuick3DParticle::updateNodeLayers()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle16updateNodeLayersEv(
    QQuick3DParticle *self) {
  self->updateNodeLayers();
}

//  void QQuick3DParticle::updateBurstIndex(int amount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle16updateBurstIndexEi(
    QQuick3DParticle *self,
    int amount) {
  self->updateBurstIndex(amount);
}

//  int QQuick3DParticle::nextCurrentIndex(const QQuick3DParticleEmitter
//      *emitter)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuick3DParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter(
    QQuick3DParticle *self,
    const QQuick3DParticleEmitter *emitter) {
  return self->nextCurrentIndex(emitter);
}

//  QSSGRenderGraphObject
//      *QQuick3DParticle::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN16QQuick3DParticle17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DParticle *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DParticle::setDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DParticle12setDepthBiasEf(
    QQuick3DParticle *self,
    float bias) {
  self->setDepthBias(bias);
}

//  float QQuick3DParticle::depthBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuick3DParticle9depthBiasEv(
    const QQuick3DParticle *self) {
  return self->depthBias();
}

//  a Python function taken by a CuteQQuick3DParticle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticle(
    QQuick3DParticle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticle *>(self)->take(key, call);
}

//  void QQuick3DParticle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DParticle17componentCompleteEv(
    QQuick3DParticle *self) {
  static_cast<OwnQQuick3DParticle *>(self)->OwnQQuick3DParticle::componentComplete();
}

//  void QQuick3DParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DParticle5resetEv(QQuick3DParticle *self) {
  static_cast<OwnQQuick3DParticle *>(self)->OwnQQuick3DParticle::reset();
}

//  void QQuick3DParticle::doSetMaxAmount(int amount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DParticle14doSetMaxAmountEi(
    QQuick3DParticle *self,
    int amount) {
  static_cast<OwnQQuick3DParticle *>(self)->OwnQQuick3DParticle::doSetMaxAmount(
      amount);
}

//  void QQuick3DParticle::updateNodeLayers()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DParticle16updateNodeLayersEv(
    QQuick3DParticle *self) {
  static_cast<OwnQQuick3DParticle *>(self)->OwnQQuick3DParticle::updateNodeLayers();
}

//  int QQuick3DParticle::nextCurrentIndex(const QQuick3DParticleEmitter
//      *emitter)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN16QQuick3DParticle16nextCurrentIndexEPK23QQuick3DParticleEmitter(
    QQuick3DParticle *self,
    const QQuick3DParticleEmitter *emitter) {
  return static_cast<OwnQQuick3DParticle *>(self)->OwnQQuick3DParticle::nextCurrentIndex(
      emitter);
}

//  QSSGRenderGraphObject
//      *QQuick3DParticle::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN16QQuick3DParticle17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DParticle *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DParticle *>(self)->OwnQQuick3DParticle::updateSpatialNode(
      node);
}

//  void QQuick3DParticle::setDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DParticle12setDepthBiasEf(
    QQuick3DParticle *self,
    float bias) {
  static_cast<OwnQQuick3DParticle *>(self)->OwnQQuick3DParticle::setDepthBias(
      bias);
}
