//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickSmoothedAnimation that Python can take functions over in. Every QQuickSmoothedAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickSmoothedAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickSmoothedAnimationCall1)(const void *, int, int *);
typedef void (*CuteQQuickSmoothedAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickSmoothedAnimationCall3)(const void *, int *);
typedef int (*CuteQQuickSmoothedAnimationCall4)(const void *, int *);
typedef void (*CuteQQuickSmoothedAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSmoothedAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSmoothedAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSmoothedAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSmoothedAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSmoothedAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSmoothedAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSmoothedAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSmoothedAnimation : public QQuickSmoothedAnimation {
public:
  using QQuickSmoothedAnimation::QQuickSmoothedAnimation;
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

  //  int QQuickSmoothedAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationCall0 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickSmoothedAnimation::duration();
  }

  //  void QQuickSmoothedAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationCall1 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickSmoothedAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationCall2 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationCall3 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationCall4 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationCall5 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall5>(taken[5]);
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
      CuteQQuickSmoothedAnimationCall6 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall6>(taken[6]);
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
      CuteQQuickSmoothedAnimationCall7 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall7>(taken[7]);
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
      CuteQQuickSmoothedAnimationCall8 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall8>(taken[8]);
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
      CuteQQuickSmoothedAnimationCall9 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall9>(taken[9]);
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
      CuteQQuickSmoothedAnimationCall10 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall10>(taken[10]);
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
      CuteQQuickSmoothedAnimationCall11 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall11>(taken[11]);
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
      CuteQQuickSmoothedAnimationCall12 call = reinterpret_cast<CuteQQuickSmoothedAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSmoothedAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickSmoothedAnimation10metaObjectEv(
    const QQuickSmoothedAnimation *self) {
  return self->metaObject();
}

//  void *QQuickSmoothedAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickSmoothedAnimation11qt_metacastEPKc(
    QQuickSmoothedAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSmoothedAnimation::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickSmoothedAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSmoothedAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSmoothedAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickSmoothedAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSmoothedAnimation::tr(s, c, n));
}

//  QQuickSmoothedAnimationPrivate *QQuickSmoothedAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickSmoothedAnimationPrivate *ritual_ZN23QQuickSmoothedAnimation6d_funcEv(
    QQuickSmoothedAnimation *self) {
  return self->d_func();
}

//  const QQuickSmoothedAnimationPrivate *QQuickSmoothedAnimation::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickSmoothedAnimationPrivate *ritual_ZNK23QQuickSmoothedAnimation6d_funcEv(
    const QQuickSmoothedAnimation *self) {
  return self->d_func();
}

//  QQuickSmoothedAnimation::QQuickSmoothedAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickSmoothedAnimation *ritual_ZN23QQuickSmoothedAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickSmoothedAnimation(parent);
}

//  ReversingMode QQuickSmoothedAnimation::reversingMode() const
extern "C" Q_DECL_EXPORT
QQuickSmoothedAnimation::ReversingMode ritual_ZNK23QQuickSmoothedAnimation13reversingModeEv(
    const QQuickSmoothedAnimation *self) {
  return self->reversingMode();
}

//  void QQuickSmoothedAnimation::setReversingMode(ReversingMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickSmoothedAnimation16setReversingModeENS_13ReversingModeE(
    QQuickSmoothedAnimation *self,
    QQuickSmoothedAnimation::ReversingMode a0) {
  self->setReversingMode(a0);
}

//  int QQuickSmoothedAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickSmoothedAnimation8durationEv(
    const QQuickSmoothedAnimation *self) {
  return self->duration();
}

//  void QQuickSmoothedAnimation::setDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickSmoothedAnimation11setDurationEi(
    QQuickSmoothedAnimation *self,
    int a0) {
  self->setDuration(a0);
}

//  qreal QQuickSmoothedAnimation::velocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickSmoothedAnimation8velocityEv(
    const QQuickSmoothedAnimation *self) {
  return self->velocity();
}

//  void QQuickSmoothedAnimation::setVelocity(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickSmoothedAnimation11setVelocityEd(
    QQuickSmoothedAnimation *self,
    qreal a0) {
  self->setVelocity(a0);
}

//  int QQuickSmoothedAnimation::maximumEasingTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickSmoothedAnimation17maximumEasingTimeEv(
    const QQuickSmoothedAnimation *self) {
  return self->maximumEasingTime();
}

//  void QQuickSmoothedAnimation::setMaximumEasingTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickSmoothedAnimation20setMaximumEasingTimeEi(
    QQuickSmoothedAnimation *self,
    int a0) {
  self->setMaximumEasingTime(a0);
}

//  QAbstractAnimationJob
//      *QQuickSmoothedAnimation::transition(QQuickStateActions &actions,
//      QQmlProperties &modified, TransitionDirection direction, QObject
//      *defaultTarget)
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_ZN23QQuickSmoothedAnimation10transitionER5QListI17QQuickStateActionERS0_I12QQmlPropertyEN23QQuickAbstractAnimation19TransitionDirectionEP7QObject(
    QQuickSmoothedAnimation *self,
    QQuickStateActions *actions,
    QQmlProperties *modified,
    QQuickAbstractAnimation::TransitionDirection direction,
    QObject *defaultTarget) {
  return self->transition(*actions, *modified, direction, defaultTarget);
}

//  void QQuickSmoothedAnimation::velocityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickSmoothedAnimation15velocityChangedEv(
    QQuickSmoothedAnimation *self) {
  self->velocityChanged();
}

//  void QQuickSmoothedAnimation::reversingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickSmoothedAnimation20reversingModeChangedEv(
    QQuickSmoothedAnimation *self) {
  self->reversingModeChanged();
}

//  void QQuickSmoothedAnimation::maximumEasingTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickSmoothedAnimation24maximumEasingTimeChangedEv(
    QQuickSmoothedAnimation *self) {
  self->maximumEasingTimeChanged();
}

//  a Python function taken by a CuteQQuickSmoothedAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSmoothedAnimation(
    QQuickSmoothedAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSmoothedAnimation *>(self)->take(key, call);
}

//  int QQuickSmoothedAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QQuickSmoothedAnimation8durationEv(
    const QQuickSmoothedAnimation *self) {
  return self->QQuickSmoothedAnimation::duration();
}

//  void QQuickSmoothedAnimation::setDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickSmoothedAnimation11setDurationEi(
    QQuickSmoothedAnimation *self,
    int a0) {
  self->QQuickSmoothedAnimation::setDuration(a0);
}
