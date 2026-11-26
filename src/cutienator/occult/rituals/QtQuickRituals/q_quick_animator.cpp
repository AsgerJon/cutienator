//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(easingcurve)
#include <QtCore/qeasingcurve.h>
#endif
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickAnimator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAnimator : QQuickAnimator {
  using QQuickAnimator::threadingModel;
};

//  A QQuickAnimator that Python can take functions over in. Every QQuickAnimator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickAnimatorCall0)(const void *, int *);
typedef void * (*CuteQQuickAnimatorCall1)(const void *, int *);
typedef QString * (*CuteQQuickAnimatorCall2)(const void *, int *);
typedef void (*CuteQQuickAnimatorCall3)(const void *, int *);
typedef void (*CuteQQuickAnimatorCall4)(const void *, int *);
typedef void (*CuteQQuickAnimatorCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatorCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAnimator : public QQuickAnimator {
public:
  using QQuickAnimator::QQuickAnimator;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQuickAnimator9createJobEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQuickAnimator12propertyNameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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

  //  ThreadingModel QQuickAnimator::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimatorCall0 call = reinterpret_cast<CuteQQuickAnimatorCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAnimator::threadingModel();
  }

  //  QQuickAnimatorJob *QQuickAnimator::createJob() const
  QQuickAnimatorJob *createJob() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimatorCall1 call = reinterpret_cast<CuteQQuickAnimatorCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnimatorJob *>(given);
    }
    return {};
  }

  //  QString QQuickAnimator::propertyName() const
  QString propertyName() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnimatorCall2 call = reinterpret_cast<CuteQQuickAnimatorCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnimatorCall3 call = reinterpret_cast<CuteQQuickAnimatorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAnimatorCall4 call = reinterpret_cast<CuteQQuickAnimatorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAnimatorCall5 call = reinterpret_cast<CuteQQuickAnimatorCall5>(taken[5]);
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
      CuteQQuickAnimatorCall6 call = reinterpret_cast<CuteQQuickAnimatorCall6>(taken[6]);
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
      CuteQQuickAnimatorCall7 call = reinterpret_cast<CuteQQuickAnimatorCall7>(taken[7]);
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
      CuteQQuickAnimatorCall8 call = reinterpret_cast<CuteQQuickAnimatorCall8>(taken[8]);
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
      CuteQQuickAnimatorCall9 call = reinterpret_cast<CuteQQuickAnimatorCall9>(taken[9]);
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
      CuteQQuickAnimatorCall10 call = reinterpret_cast<CuteQQuickAnimatorCall10>(taken[10]);
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
      CuteQQuickAnimatorCall11 call = reinterpret_cast<CuteQQuickAnimatorCall11>(taken[11]);
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
      CuteQQuickAnimatorCall12 call = reinterpret_cast<CuteQQuickAnimatorCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAnimator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickAnimator10metaObjectEv(
    const QQuickAnimator *self) {
  return self->metaObject();
}

//  void *QQuickAnimator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickAnimator11qt_metacastEPKc(
    QQuickAnimator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickAnimator::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickAnimator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickAnimator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickAnimator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickAnimator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAnimator::tr(s, c, n));
}

//  QQuickAnimatorPrivate *QQuickAnimator::d_func()
extern "C" Q_DECL_EXPORT
QQuickAnimatorPrivate *ritual_ZN14QQuickAnimator6d_funcEv(
    QQuickAnimator *self) {
  return self->d_func();
}

//  const QQuickAnimatorPrivate *QQuickAnimator::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnimatorPrivate *ritual_ZNK14QQuickAnimator6d_funcEv(
    const QQuickAnimator *self) {
  return self->d_func();
}

//  void QQuickAnimator::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator24qt_qmlMarker_uncreatableEv(
    QQuickAnimator *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickItem *QQuickAnimator::targetItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickAnimator10targetItemEv(
    const QQuickAnimator *self) {
  return self->targetItem();
}

//  void QQuickAnimator::setTargetItem(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator13setTargetItemEP10QQuickItem(
    QQuickAnimator *self,
    QQuickItem *target) {
  self->setTargetItem(target);
}

//  int QQuickAnimator::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickAnimator8durationEv(const QQuickAnimator *self) {
  return self->duration();
}

//  void QQuickAnimator::setDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator11setDurationEi(
    QQuickAnimator *self,
    int duration) {
  self->setDuration(duration);
}

//  QEasingCurve QQuickAnimator::easing() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK14QQuickAnimator6easingEv(
    const QQuickAnimator *self) {
  return new QEasingCurve(self->easing());
}

//  void QQuickAnimator::setEasing(const QEasingCurve &easing)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator9setEasingERK12QEasingCurve(
    QQuickAnimator *self,
    const QEasingCurve *easing) {
  self->setEasing(*easing);
}

//  qreal QQuickAnimator::to() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickAnimator2toEv(const QQuickAnimator *self) {
  return self->to();
}

//  void QQuickAnimator::setTo(qreal to)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator5setToEd(QQuickAnimator *self, qreal to) {
  self->setTo(to);
}

//  qreal QQuickAnimator::from() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickAnimator4fromEv(const QQuickAnimator *self) {
  return self->from();
}

//  void QQuickAnimator::setFrom(qreal from)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator7setFromEd(QQuickAnimator *self, qreal from) {
  self->setFrom(from);
}

//  ThreadingModel QQuickAnimator::threadingModel() const
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation::ThreadingModel ritual_ZNK14QQuickAnimator14threadingModelEv(
    const QQuickAnimator *self) {
  return self->threadingModel();
}

//  QQuickAnimatorJob *QQuickAnimator::createJob() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_ZNK14QQuickAnimator9createJobEv(
    const QQuickAnimator *self) {
  return self->createJob();
}

//  QString QQuickAnimator::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickAnimator12propertyNameEv(
    const QQuickAnimator *self) {
  return new QString(self->propertyName());
}

//  QAbstractAnimationJob *QQuickAnimator::transition(QQuickStateActions
//      &actions, QQmlProperties &modified, TransitionDirection a2, QObject
//      *a3)
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_ZN14QQuickAnimator10transitionER5QListI17QQuickStateActionERS0_I12QQmlPropertyEN23QQuickAbstractAnimation19TransitionDirectionEP7QObject(
    QQuickAnimator *self,
    QQuickStateActions *actions,
    QQmlProperties *modified,
    QQuickAbstractAnimation::TransitionDirection a2,
    QObject *a3) {
  return self->transition(*actions, *modified, a2, a3);
}

//  QQuickAnimator::QQuickAnimator(QQuickAnimatorPrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickAnimator *ritual_ZN14QQuickAnimatorC1ER21QQuickAnimatorPrivateP7QObject(
    QQuickAnimatorPrivate *dd,
    QObject *parent) {
  return new CuteQQuickAnimator(*dd, parent);
}

//  QQuickAnimator::QQuickAnimator(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickAnimator *ritual_ZN14QQuickAnimatorC1EP7QObject(QObject *parent) {
  return new CuteQQuickAnimator(parent);
}

//  void QQuickAnimator::targetItemChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator17targetItemChangedEP10QQuickItem(
    QQuickAnimator *self,
    QQuickItem *a0) {
  self->targetItemChanged(a0);
}

//  void QQuickAnimator::durationChanged(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator15durationChangedEi(
    QQuickAnimator *self,
    int duration) {
  self->durationChanged(duration);
}

//  void QQuickAnimator::easingChanged(const QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator13easingChangedERK12QEasingCurve(
    QQuickAnimator *self,
    const QEasingCurve *curve) {
  self->easingChanged(*curve);
}

//  void QQuickAnimator::toChanged(qreal to)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator9toChangedEd(QQuickAnimator *self, qreal to) {
  self->toChanged(to);
}

//  void QQuickAnimator::fromChanged(qreal from)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickAnimator11fromChangedEd(
    QQuickAnimator *self,
    qreal from) {
  self->fromChanged(from);
}

//  a Python function taken by a CuteQQuickAnimator, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimator(
    QQuickAnimator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimator *>(self)->take(key, call);
}

//  ThreadingModel QQuickAnimator::threadingModel() const
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation::ThreadingModel ritual_own_ZNK14QQuickAnimator14threadingModelEv(
    const QQuickAnimator *self) {
  return static_cast<const OwnQQuickAnimator *>(self)->OwnQQuickAnimator::threadingModel();
}
