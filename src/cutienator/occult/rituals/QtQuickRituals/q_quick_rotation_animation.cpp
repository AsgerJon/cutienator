//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickRotationAnimation that Python can take functions over in. Every QQuickRotationAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickRotationAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickRotationAnimationCall1)(const void *, int, int *);
typedef void (*CuteQQuickRotationAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickRotationAnimationCall3)(const void *, int *);
typedef int (*CuteQQuickRotationAnimationCall4)(const void *, int *);
typedef void (*CuteQQuickRotationAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRotationAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRotationAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRotationAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRotationAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRotationAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRotationAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRotationAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRotationAnimation : public QQuickRotationAnimation {
public:
  using QQuickRotationAnimation::QQuickRotationAnimation;
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
      CuteQQuickRotationAnimationCall0 call = reinterpret_cast<CuteQQuickRotationAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPropertyAnimation::duration();
  }

  //  void QQuickPropertyAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRotationAnimationCall1 call = reinterpret_cast<CuteQQuickRotationAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRotationAnimationCall2 call = reinterpret_cast<CuteQQuickRotationAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRotationAnimationCall3 call = reinterpret_cast<CuteQQuickRotationAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRotationAnimationCall4 call = reinterpret_cast<CuteQQuickRotationAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRotationAnimationCall5 call = reinterpret_cast<CuteQQuickRotationAnimationCall5>(taken[5]);
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
      CuteQQuickRotationAnimationCall6 call = reinterpret_cast<CuteQQuickRotationAnimationCall6>(taken[6]);
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
      CuteQQuickRotationAnimationCall7 call = reinterpret_cast<CuteQQuickRotationAnimationCall7>(taken[7]);
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
      CuteQQuickRotationAnimationCall8 call = reinterpret_cast<CuteQQuickRotationAnimationCall8>(taken[8]);
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
      CuteQQuickRotationAnimationCall9 call = reinterpret_cast<CuteQQuickRotationAnimationCall9>(taken[9]);
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
      CuteQQuickRotationAnimationCall10 call = reinterpret_cast<CuteQQuickRotationAnimationCall10>(taken[10]);
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
      CuteQQuickRotationAnimationCall11 call = reinterpret_cast<CuteQQuickRotationAnimationCall11>(taken[11]);
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
      CuteQQuickRotationAnimationCall12 call = reinterpret_cast<CuteQQuickRotationAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRotationAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickRotationAnimation10metaObjectEv(
    const QQuickRotationAnimation *self) {
  return self->metaObject();
}

//  QString QQuickRotationAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickRotationAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRotationAnimation::tr(s, c, n));
}

//  QQuickRotationAnimationPrivate *QQuickRotationAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickRotationAnimationPrivate *ritual_ZN23QQuickRotationAnimation6d_funcEv(
    QQuickRotationAnimation *self) {
  return self->d_func();
}

//  const QQuickRotationAnimationPrivate *QQuickRotationAnimation::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickRotationAnimationPrivate *ritual_ZNK23QQuickRotationAnimation6d_funcEv(
    const QQuickRotationAnimation *self) {
  return self->d_func();
}

//  QQuickRotationAnimation::QQuickRotationAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickRotationAnimation *ritual_ZN23QQuickRotationAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickRotationAnimation(parent);
}

//  QQuickRotationAnimation::~QQuickRotationAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRotationAnimationD1Ev(QQuickRotationAnimation *self) {
  delete self;
}

//  qreal QQuickRotationAnimation::from() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickRotationAnimation4fromEv(
    const QQuickRotationAnimation *self) {
  return self->from();
}

//  void QQuickRotationAnimation::setFrom(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRotationAnimation7setFromEd(
    QQuickRotationAnimation *self,
    qreal a0) {
  self->setFrom(a0);
}

//  qreal QQuickRotationAnimation::to() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickRotationAnimation2toEv(
    const QQuickRotationAnimation *self) {
  return self->to();
}

//  void QQuickRotationAnimation::setTo(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRotationAnimation5setToEd(
    QQuickRotationAnimation *self,
    qreal a0) {
  self->setTo(a0);
}

//  RotationDirection QQuickRotationAnimation::direction() const
extern "C" Q_DECL_EXPORT
QQuickRotationAnimation::RotationDirection ritual_ZNK23QQuickRotationAnimation9directionEv(
    const QQuickRotationAnimation *self) {
  return self->direction();
}

//  void QQuickRotationAnimation::setDirection(RotationDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRotationAnimation12setDirectionENS_17RotationDirectionE(
    QQuickRotationAnimation *self,
    QQuickRotationAnimation::RotationDirection direction) {
  self->setDirection(direction);
}

//  a Python function taken by a CuteQQuickRotationAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRotationAnimation(
    QQuickRotationAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRotationAnimation *>(self)->take(key, call);
}
