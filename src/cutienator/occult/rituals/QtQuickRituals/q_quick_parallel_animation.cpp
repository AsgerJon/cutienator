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

//  Only a class built on QQuickParallelAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickParallelAnimation : QQuickParallelAnimation {
  using QQuickParallelAnimation::threadingModel;
};

//  A QQuickParallelAnimation that Python can take functions over in. Every QQuickParallelAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickParallelAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickParallelAnimationCall1)(const void *, int *);
typedef void (*CuteQQuickParallelAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickParallelAnimationCall3)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParallelAnimationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParallelAnimationCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParallelAnimationCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParallelAnimationCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParallelAnimationCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParallelAnimationCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParallelAnimationCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickParallelAnimation : public QQuickParallelAnimation {
public:
  using QQuickParallelAnimation::QQuickParallelAnimation;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  ThreadingModel QQuickParallelAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall0 call = reinterpret_cast<CuteQQuickParallelAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickParallelAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall1 call = reinterpret_cast<CuteQQuickParallelAnimationCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall2 call = reinterpret_cast<CuteQQuickParallelAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall3 call = reinterpret_cast<CuteQQuickParallelAnimationCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::setTarget(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall4 call = reinterpret_cast<CuteQQuickParallelAnimationCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall5 call = reinterpret_cast<CuteQQuickParallelAnimationCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall6 call = reinterpret_cast<CuteQQuickParallelAnimationCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall7 call = reinterpret_cast<CuteQQuickParallelAnimationCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall8 call = reinterpret_cast<CuteQQuickParallelAnimationCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall9 call = reinterpret_cast<CuteQQuickParallelAnimationCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickParallelAnimationCall10 call = reinterpret_cast<CuteQQuickParallelAnimationCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickParallelAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickParallelAnimation10metaObjectEv(
    const QQuickParallelAnimation *self) {
  return self->metaObject();
}

//  void *QQuickParallelAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickParallelAnimation11qt_metacastEPKc(
    QQuickParallelAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickParallelAnimation::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickParallelAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickParallelAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickParallelAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickParallelAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParallelAnimation::tr(s, c, n));
}

//  QQuickAnimationGroupPrivate *QQuickParallelAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickAnimationGroupPrivate *ritual_ZN23QQuickParallelAnimation6d_funcEv(
    QQuickParallelAnimation *self) {
  return self->d_func();
}

//  const QQuickAnimationGroupPrivate *QQuickParallelAnimation::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickAnimationGroupPrivate *ritual_ZNK23QQuickParallelAnimation6d_funcEv(
    const QQuickParallelAnimation *self) {
  return self->d_func();
}

//  QQuickParallelAnimation::QQuickParallelAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickParallelAnimation *ritual_ZN23QQuickParallelAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickParallelAnimation(parent);
}

//  QQuickParallelAnimation::~QQuickParallelAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickParallelAnimationD1Ev(QQuickParallelAnimation *self) {
  delete self;
}

//  ThreadingModel QQuickParallelAnimation::threadingModel() const
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation::ThreadingModel ritual_ZNK23QQuickParallelAnimation14threadingModelEv(
    const QQuickParallelAnimation *self) {
  return self->threadingModel();
}

//  QAbstractAnimationJob
//      *QQuickParallelAnimation::transition(QQuickStateActions &actions,
//      QQmlProperties &modified, TransitionDirection direction, QObject
//      *defaultTarget)
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_ZN23QQuickParallelAnimation10transitionER5QListI17QQuickStateActionERS0_I12QQmlPropertyEN23QQuickAbstractAnimation19TransitionDirectionEP7QObject(
    QQuickParallelAnimation *self,
    QQuickStateActions *actions,
    QQmlProperties *modified,
    QQuickAbstractAnimation::TransitionDirection direction,
    QObject *defaultTarget) {
  return self->transition(*actions, *modified, direction, defaultTarget);
}

//  a Python function taken by a CuteQQuickParallelAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickParallelAnimation(
    QQuickParallelAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickParallelAnimation *>(self)->take(key, call);
}

//  ThreadingModel QQuickParallelAnimation::threadingModel() const
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation::ThreadingModel ritual_own_ZNK23QQuickParallelAnimation14threadingModelEv(
    const QQuickParallelAnimation *self) {
  return static_cast<const OwnQQuickParallelAnimation *>(self)->OwnQQuickParallelAnimation::threadingModel();
}
