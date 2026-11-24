//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlespritesequence_p.h
//  , Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlespritesequence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DParticleSpriteSequence may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleSpriteSequence : QQuick3DParticleSpriteSequence {
  using QQuick3DParticleSpriteSequence::componentComplete;
  using QQuick3DParticleSpriteSequence::classBegin;
};

//  A QQuick3DParticleSpriteSequence that Python can take functions over in. Every QQuick3DParticleSpriteSequence
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DParticleSpriteSequenceCall0)(const void *, int *);
typedef void (*CuteQQuick3DParticleSpriteSequenceCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSpriteSequenceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSpriteSequenceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteSequenceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteSequenceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteSequenceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteSequenceCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteSequenceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleSpriteSequence : public QQuick3DParticleSpriteSequence {
public:
  using QQuick3DParticleSpriteSequence::QQuick3DParticleSpriteSequence;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DParticleSpriteSequence::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteSequenceCall0 call = reinterpret_cast<CuteQQuick3DParticleSpriteSequenceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteSequence::componentComplete();
  }

  //  void QQuick3DParticleSpriteSequence::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteSequenceCall1 call = reinterpret_cast<CuteQQuick3DParticleSpriteSequenceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleSpriteSequence::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteSequenceCall2 call = reinterpret_cast<CuteQQuick3DParticleSpriteSequenceCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteSequenceCall3 call = reinterpret_cast<CuteQQuick3DParticleSpriteSequenceCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteSequenceCall4 call = reinterpret_cast<CuteQQuick3DParticleSpriteSequenceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteSequenceCall5 call = reinterpret_cast<CuteQQuick3DParticleSpriteSequenceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteSequenceCall6 call = reinterpret_cast<CuteQQuick3DParticleSpriteSequenceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteSequenceCall7 call = reinterpret_cast<CuteQQuick3DParticleSpriteSequenceCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteSequenceCall8 call = reinterpret_cast<CuteQQuick3DParticleSpriteSequenceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleSpriteSequence::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QQuick3DParticleSpriteSequence10metaObjectEv(
    const QQuick3DParticleSpriteSequence *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleSpriteSequence::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQuick3DParticleSpriteSequence2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleSpriteSequence::tr(s, c, n));
}

//  QQuick3DParticleSpriteSequence::QQuick3DParticleSpriteSequence(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleSpriteSequence *ritual_ZN30QQuick3DParticleSpriteSequenceC1EP7QObject(
    QObject *parent) {
  return new CuteQQuick3DParticleSpriteSequence(parent);
}

//  QQuick3DParticleSpriteSequence::~QQuick3DParticleSpriteSequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequenceD1Ev(
    QQuick3DParticleSpriteSequence *self) {
  delete self;
}

//  int QQuick3DParticleSpriteSequence::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DParticleSpriteSequence10frameCountEv(
    const QQuick3DParticleSpriteSequence *self) {
  return self->frameCount();
}

//  int QQuick3DParticleSpriteSequence::frameIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DParticleSpriteSequence10frameIndexEv(
    const QQuick3DParticleSpriteSequence *self) {
  return self->frameIndex();
}

//  bool QQuick3DParticleSpriteSequence::interpolate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DParticleSpriteSequence11interpolateEv(
    const QQuick3DParticleSpriteSequence *self) {
  return self->interpolate();
}

//  int QQuick3DParticleSpriteSequence::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DParticleSpriteSequence8durationEv(
    const QQuick3DParticleSpriteSequence *self) {
  return self->duration();
}

//  int QQuick3DParticleSpriteSequence::durationVariation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuick3DParticleSpriteSequence17durationVariationEv(
    const QQuick3DParticleSpriteSequence *self) {
  return self->durationVariation();
}

//  bool QQuick3DParticleSpriteSequence::randomStart() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuick3DParticleSpriteSequence11randomStartEv(
    const QQuick3DParticleSpriteSequence *self) {
  return self->randomStart();
}

//  AnimationDirection QQuick3DParticleSpriteSequence::animationDirection()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DParticleSpriteSequence::AnimationDirection ritual_ZNK30QQuick3DParticleSpriteSequence18animationDirectionEv(
    const QQuick3DParticleSpriteSequence *self) {
  return self->animationDirection();
}

//  void QQuick3DParticleSpriteSequence::setFrameCount(int frameCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence13setFrameCountEi(
    QQuick3DParticleSpriteSequence *self,
    int frameCount) {
  self->setFrameCount(frameCount);
}

//  void QQuick3DParticleSpriteSequence::setFrameIndex(int frameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence13setFrameIndexEi(
    QQuick3DParticleSpriteSequence *self,
    int frameIndex) {
  self->setFrameIndex(frameIndex);
}

//  void QQuick3DParticleSpriteSequence::setInterpolate(bool interpolate)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence14setInterpolateEb(
    QQuick3DParticleSpriteSequence *self,
    bool interpolate) {
  self->setInterpolate(interpolate);
}

//  void QQuick3DParticleSpriteSequence::setDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence11setDurationEi(
    QQuick3DParticleSpriteSequence *self,
    int duration) {
  self->setDuration(duration);
}

//  void QQuick3DParticleSpriteSequence::setDurationVariation(int
//      durationVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence20setDurationVariationEi(
    QQuick3DParticleSpriteSequence *self,
    int durationVariation) {
  self->setDurationVariation(durationVariation);
}

//  void QQuick3DParticleSpriteSequence::setRandomStart(bool randomStart)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence14setRandomStartEb(
    QQuick3DParticleSpriteSequence *self,
    bool randomStart) {
  self->setRandomStart(randomStart);
}

//  void QQuick3DParticleSpriteSequence::setAnimationDirection(QQuick3DPartic
//      leSpriteSequence::AnimationDirection animationDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence21setAnimationDirectionENS_18AnimationDirectionE(
    QQuick3DParticleSpriteSequence *self,
    QQuick3DParticleSpriteSequence::AnimationDirection animationDirection) {
  self->setAnimationDirection(animationDirection);
}

//  void QQuick3DParticleSpriteSequence::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence17componentCompleteEv(
    QQuick3DParticleSpriteSequence *self) {
  self->componentComplete();
}

//  void QQuick3DParticleSpriteSequence::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence10classBeginEv(
    QQuick3DParticleSpriteSequence *self) {
  self->classBegin();
}

//  void QQuick3DParticleSpriteSequence::markNodesDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DParticleSpriteSequence14markNodesDirtyEv(
    QQuick3DParticleSpriteSequence *self) {
  self->markNodesDirty();
}

//  float QQuick3DParticleSpriteSequence::firstFrame(int index, bool
//      singleFrame)
extern "C" Q_DECL_EXPORT
float ritual_ZN30QQuick3DParticleSpriteSequence10firstFrameEib(
    QQuick3DParticleSpriteSequence *self,
    int index,
    bool singleFrame) {
  return self->firstFrame(index, singleFrame);
}

//  QQuick3DParticleSpriteSequence as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuick3DParticleSpriteSequence_QQmlParserStatus(
    QQuick3DParticleSpriteSequence *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuick3DParticleSpriteSequence, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleSpriteSequence(
    QQuick3DParticleSpriteSequence *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleSpriteSequence *>(self)->take(key, call);
}

//  void QQuick3DParticleSpriteSequence::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteSequence17componentCompleteEv(
    QQuick3DParticleSpriteSequence *self) {
  static_cast<OwnQQuick3DParticleSpriteSequence *>(self)->OwnQQuick3DParticleSpriteSequence::componentComplete();
}

//  void QQuick3DParticleSpriteSequence::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuick3DParticleSpriteSequence10classBeginEv(
    QQuick3DParticleSpriteSequence *self) {
  static_cast<OwnQQuick3DParticleSpriteSequence *>(self)->OwnQQuick3DParticleSpriteSequence::classBegin();
}
