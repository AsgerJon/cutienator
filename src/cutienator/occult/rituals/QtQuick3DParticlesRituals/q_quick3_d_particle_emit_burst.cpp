//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticleemitburst_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleemitburst_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DParticleEmitBurst may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleEmitBurst : QQuick3DParticleEmitBurst {
  using QQuick3DParticleEmitBurst::componentComplete;
  using QQuick3DParticleEmitBurst::classBegin;
};

//  A QQuick3DParticleEmitBurst that Python can take functions over in. Every QQuick3DParticleEmitBurst
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DParticleEmitBurstCall0)(const void *, int *);
typedef void (*CuteQQuick3DParticleEmitBurstCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleEmitBurstCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleEmitBurstCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitBurstCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitBurstCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitBurstCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitBurstCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleEmitBurstCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleEmitBurst : public QQuick3DParticleEmitBurst {
public:
  using QQuick3DParticleEmitBurst::QQuick3DParticleEmitBurst;
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

  //  void QQuick3DParticleEmitBurst::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleEmitBurstCall0 call = reinterpret_cast<CuteQQuick3DParticleEmitBurstCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleEmitBurst::componentComplete();
  }

  //  void QQuick3DParticleEmitBurst::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleEmitBurstCall1 call = reinterpret_cast<CuteQQuick3DParticleEmitBurstCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleEmitBurst::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleEmitBurstCall2 call = reinterpret_cast<CuteQQuick3DParticleEmitBurstCall2>(taken[2]);
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
      CuteQQuick3DParticleEmitBurstCall3 call = reinterpret_cast<CuteQQuick3DParticleEmitBurstCall3>(taken[3]);
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
      CuteQQuick3DParticleEmitBurstCall4 call = reinterpret_cast<CuteQQuick3DParticleEmitBurstCall4>(taken[4]);
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
      CuteQQuick3DParticleEmitBurstCall5 call = reinterpret_cast<CuteQQuick3DParticleEmitBurstCall5>(taken[5]);
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
      CuteQQuick3DParticleEmitBurstCall6 call = reinterpret_cast<CuteQQuick3DParticleEmitBurstCall6>(taken[6]);
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
      CuteQQuick3DParticleEmitBurstCall7 call = reinterpret_cast<CuteQQuick3DParticleEmitBurstCall7>(taken[7]);
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
      CuteQQuick3DParticleEmitBurstCall8 call = reinterpret_cast<CuteQQuick3DParticleEmitBurstCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleEmitBurst::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuick3DParticleEmitBurst10metaObjectEv(
    const QQuick3DParticleEmitBurst *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleEmitBurst::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuick3DParticleEmitBurst2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleEmitBurst::tr(s, c, n));
}

//  QQuick3DParticleEmitBurst::QQuick3DParticleEmitBurst(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleEmitBurst *ritual_ZN25QQuick3DParticleEmitBurstC1EP7QObject(
    QObject *parent) {
  return new CuteQQuick3DParticleEmitBurst(parent);
}

//  QQuick3DParticleEmitBurst::~QQuick3DParticleEmitBurst()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleEmitBurstD1Ev(
    QQuick3DParticleEmitBurst *self) {
  delete self;
}

//  int QQuick3DParticleEmitBurst::time() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuick3DParticleEmitBurst4timeEv(
    const QQuick3DParticleEmitBurst *self) {
  return self->time();
}

//  int QQuick3DParticleEmitBurst::amount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuick3DParticleEmitBurst6amountEv(
    const QQuick3DParticleEmitBurst *self) {
  return self->amount();
}

//  int QQuick3DParticleEmitBurst::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuick3DParticleEmitBurst8durationEv(
    const QQuick3DParticleEmitBurst *self) {
  return self->duration();
}

//  void QQuick3DParticleEmitBurst::setTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleEmitBurst7setTimeEi(
    QQuick3DParticleEmitBurst *self,
    int time) {
  self->setTime(time);
}

//  void QQuick3DParticleEmitBurst::setAmount(int amount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleEmitBurst9setAmountEi(
    QQuick3DParticleEmitBurst *self,
    int amount) {
  self->setAmount(amount);
}

//  void QQuick3DParticleEmitBurst::setDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleEmitBurst11setDurationEi(
    QQuick3DParticleEmitBurst *self,
    int duration) {
  self->setDuration(duration);
}

//  void QQuick3DParticleEmitBurst::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleEmitBurst17componentCompleteEv(
    QQuick3DParticleEmitBurst *self) {
  self->componentComplete();
}

//  void QQuick3DParticleEmitBurst::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleEmitBurst10classBeginEv(
    QQuick3DParticleEmitBurst *self) {
  self->classBegin();
}

//  QQuick3DParticleEmitBurst as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuick3DParticleEmitBurst_QQmlParserStatus(
    QQuick3DParticleEmitBurst *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuick3DParticleEmitBurst, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleEmitBurst(
    QQuick3DParticleEmitBurst *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleEmitBurst *>(self)->take(key, call);
}

//  void QQuick3DParticleEmitBurst::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuick3DParticleEmitBurst17componentCompleteEv(
    QQuick3DParticleEmitBurst *self) {
  static_cast<OwnQQuick3DParticleEmitBurst *>(self)->OwnQQuick3DParticleEmitBurst::componentComplete();
}

//  void QQuick3DParticleEmitBurst::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuick3DParticleEmitBurst10classBeginEv(
    QQuick3DParticleEmitBurst *self) {
  static_cast<OwnQQuick3DParticleEmitBurst *>(self)->OwnQQuick3DParticleEmitBurst::classBegin();
}
