//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickParentAnimation that Python can take functions over in. Every QQuickParentAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickParentAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickParentAnimationCall1)(const void *, int *);
typedef int (*CuteQQuickParentAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickParentAnimationCall3)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParentAnimationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParentAnimationCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentAnimationCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentAnimationCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentAnimationCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentAnimationCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentAnimationCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickParentAnimation : public QQuickParentAnimation {
public:
  using QQuickParentAnimation::QQuickParentAnimation;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
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

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickParentAnimationCall0 call = reinterpret_cast<CuteQQuickParentAnimationCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickParentAnimationCall1 call = reinterpret_cast<CuteQQuickParentAnimationCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickParentAnimationCall2 call = reinterpret_cast<CuteQQuickParentAnimationCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickParentAnimationCall3 call = reinterpret_cast<CuteQQuickParentAnimationCall3>(taken[3]);
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
      CuteQQuickParentAnimationCall4 call = reinterpret_cast<CuteQQuickParentAnimationCall4>(taken[4]);
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
      CuteQQuickParentAnimationCall5 call = reinterpret_cast<CuteQQuickParentAnimationCall5>(taken[5]);
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
      CuteQQuickParentAnimationCall6 call = reinterpret_cast<CuteQQuickParentAnimationCall6>(taken[6]);
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
      CuteQQuickParentAnimationCall7 call = reinterpret_cast<CuteQQuickParentAnimationCall7>(taken[7]);
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
      CuteQQuickParentAnimationCall8 call = reinterpret_cast<CuteQQuickParentAnimationCall8>(taken[8]);
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
      CuteQQuickParentAnimationCall9 call = reinterpret_cast<CuteQQuickParentAnimationCall9>(taken[9]);
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
      CuteQQuickParentAnimationCall10 call = reinterpret_cast<CuteQQuickParentAnimationCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickParentAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickParentAnimation10metaObjectEv(
    const QQuickParentAnimation *self) {
  return self->metaObject();
}

//  void *QQuickParentAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickParentAnimation11qt_metacastEPKc(
    QQuickParentAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickParentAnimation::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickParentAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickParentAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickParentAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickParentAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParentAnimation::tr(s, c, n));
}

//  QQuickParentAnimationPrivate *QQuickParentAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickParentAnimationPrivate *ritual_ZN21QQuickParentAnimation6d_funcEv(
    QQuickParentAnimation *self) {
  return self->d_func();
}

//  const QQuickParentAnimationPrivate *QQuickParentAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickParentAnimationPrivate *ritual_ZNK21QQuickParentAnimation6d_funcEv(
    const QQuickParentAnimation *self) {
  return self->d_func();
}

//  QQuickParentAnimation::QQuickParentAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickParentAnimation *ritual_ZN21QQuickParentAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickParentAnimation(parent);
}

//  QQuickItem *QQuickParentAnimation::target() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickParentAnimation6targetEv(
    const QQuickParentAnimation *self) {
  return self->target();
}

//  void QQuickParentAnimation::setTargetObject(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParentAnimation15setTargetObjectEP10QQuickItem(
    QQuickParentAnimation *self,
    QQuickItem *a0) {
  self->setTargetObject(a0);
}

//  QQuickItem *QQuickParentAnimation::newParent() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickParentAnimation9newParentEv(
    const QQuickParentAnimation *self) {
  return self->newParent();
}

//  void QQuickParentAnimation::setNewParent(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParentAnimation12setNewParentEP10QQuickItem(
    QQuickParentAnimation *self,
    QQuickItem *a0) {
  self->setNewParent(a0);
}

//  QQuickItem *QQuickParentAnimation::via() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickParentAnimation3viaEv(
    const QQuickParentAnimation *self) {
  return self->via();
}

//  void QQuickParentAnimation::setVia(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParentAnimation6setViaEP10QQuickItem(
    QQuickParentAnimation *self,
    QQuickItem *a0) {
  self->setVia(a0);
}

//  void QQuickParentAnimation::targetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParentAnimation13targetChangedEv(
    QQuickParentAnimation *self) {
  self->targetChanged();
}

//  void QQuickParentAnimation::newParentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParentAnimation16newParentChangedEv(
    QQuickParentAnimation *self) {
  self->newParentChanged();
}

//  void QQuickParentAnimation::viaChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParentAnimation10viaChangedEv(
    QQuickParentAnimation *self) {
  self->viaChanged();
}

//  QAbstractAnimationJob
//      *QQuickParentAnimation::transition(QQuickStateActions &actions,
//      QQmlProperties &modified, TransitionDirection direction, QObject
//      *defaultTarget)
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_ZN21QQuickParentAnimation10transitionER5QListI17QQuickStateActionERS0_I12QQmlPropertyEN23QQuickAbstractAnimation19TransitionDirectionEP7QObject(
    QQuickParentAnimation *self,
    QQuickStateActions *actions,
    QQmlProperties *modified,
    QQuickAbstractAnimation::TransitionDirection direction,
    QObject *defaultTarget) {
  return self->transition(*actions, *modified, direction, defaultTarget);
}

//  a Python function taken by a CuteQQuickParentAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickParentAnimation(
    QQuickParentAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickParentAnimation *>(self)->take(key, call);
}
