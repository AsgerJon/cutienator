//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickspringanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickspringanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickSpringAnimation that Python can take functions over in. Every QQuickSpringAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickSpringAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickSpringAnimationCall1)(const void *, int, int *);
typedef void (*CuteQQuickSpringAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickSpringAnimationCall3)(const void *, int *);
typedef int (*CuteQQuickSpringAnimationCall4)(const void *, int *);
typedef void (*CuteQQuickSpringAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSpringAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSpringAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpringAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpringAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpringAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpringAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpringAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSpringAnimation : public QQuickSpringAnimation {
public:
  using QQuickSpringAnimation::QQuickSpringAnimation;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation8durationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQuickPropertyAnimation11setDurationEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int QQuickPropertyAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall0 call = reinterpret_cast<CuteQQuickSpringAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPropertyAnimation::duration();
  }

  //  void QQuickPropertyAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall1 call = reinterpret_cast<CuteQQuickSpringAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall2 call = reinterpret_cast<CuteQQuickSpringAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall3 call = reinterpret_cast<CuteQQuickSpringAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall4 call = reinterpret_cast<CuteQQuickSpringAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall5 call = reinterpret_cast<CuteQQuickSpringAnimationCall5>(taken[5]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::setTarget(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall6 call = reinterpret_cast<CuteQQuickSpringAnimationCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall7 call = reinterpret_cast<CuteQQuickSpringAnimationCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall8 call = reinterpret_cast<CuteQQuickSpringAnimationCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall9 call = reinterpret_cast<CuteQQuickSpringAnimationCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall10 call = reinterpret_cast<CuteQQuickSpringAnimationCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall11 call = reinterpret_cast<CuteQQuickSpringAnimationCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickSpringAnimationCall12 call = reinterpret_cast<CuteQQuickSpringAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSpringAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickSpringAnimation10metaObjectEv(
    const QQuickSpringAnimation *self) {
  return self->metaObject();
}

//  QString QQuickSpringAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickSpringAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSpringAnimation::tr(s, c, n));
}

//  QQuickSpringAnimation::QQuickSpringAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickSpringAnimation *ritual_ZN21QQuickSpringAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickSpringAnimation(parent);
}

//  QQuickSpringAnimation::~QQuickSpringAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickSpringAnimationD1Ev(QQuickSpringAnimation *self) {
  delete self;
}

//  qreal QQuickSpringAnimation::velocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickSpringAnimation8velocityEv(
    const QQuickSpringAnimation *self) {
  return self->velocity();
}

//  void QQuickSpringAnimation::setVelocity(qreal velocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickSpringAnimation11setVelocityEd(
    QQuickSpringAnimation *self,
    qreal velocity) {
  self->setVelocity(velocity);
}

//  qreal QQuickSpringAnimation::spring() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickSpringAnimation6springEv(
    const QQuickSpringAnimation *self) {
  return self->spring();
}

//  void QQuickSpringAnimation::setSpring(qreal spring)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickSpringAnimation9setSpringEd(
    QQuickSpringAnimation *self,
    qreal spring) {
  self->setSpring(spring);
}

//  qreal QQuickSpringAnimation::damping() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickSpringAnimation7dampingEv(
    const QQuickSpringAnimation *self) {
  return self->damping();
}

//  void QQuickSpringAnimation::setDamping(qreal damping)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickSpringAnimation10setDampingEd(
    QQuickSpringAnimation *self,
    qreal damping) {
  self->setDamping(damping);
}

//  qreal QQuickSpringAnimation::epsilon() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickSpringAnimation7epsilonEv(
    const QQuickSpringAnimation *self) {
  return self->epsilon();
}

//  void QQuickSpringAnimation::setEpsilon(qreal epsilon)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickSpringAnimation10setEpsilonEd(
    QQuickSpringAnimation *self,
    qreal epsilon) {
  self->setEpsilon(epsilon);
}

//  qreal QQuickSpringAnimation::mass() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickSpringAnimation4massEv(
    const QQuickSpringAnimation *self) {
  return self->mass();
}

//  void QQuickSpringAnimation::setMass(qreal modulus)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickSpringAnimation7setMassEd(
    QQuickSpringAnimation *self,
    qreal modulus) {
  self->setMass(modulus);
}

//  qreal QQuickSpringAnimation::modulus() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickSpringAnimation7modulusEv(
    const QQuickSpringAnimation *self) {
  return self->modulus();
}

//  void QQuickSpringAnimation::setModulus(qreal modulus)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickSpringAnimation10setModulusEd(
    QQuickSpringAnimation *self,
    qreal modulus) {
  self->setModulus(modulus);
}

//  a Python function taken by a CuteQQuickSpringAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSpringAnimation(
    QQuickSpringAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSpringAnimation *>(self)->take(key, call);
}
