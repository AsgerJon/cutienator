//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsAnimation/6.12.0/QtLabsAnimation/private/qquickboundaryrule_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsAnimation/6.12.0/QtLabsAnimation/private/qqmlanimationglobal_p.h>
#include <QtLabsAnimation/QtLabsAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsAnimation/6.12.0/QtLabsAnimation/private/qquickboundaryrule_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qvariant.h>
#if QT_CONFIG(easingcurve)
#include <QtCore/qeasingcurve.h>
#endif
#include <QtCore/qproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickBoundaryRule that Python can take functions over in. Every QQuickBoundaryRule
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickBoundaryRuleCall0)(const void *, const QQmlProperty *, int *);
typedef void (*CuteQQuickBoundaryRuleCall1)(const void *, const QVariant *, int *);
typedef void (*CuteQQuickBoundaryRuleCall2)(const void *, int *);
typedef void (*CuteQQuickBoundaryRuleCall3)(const void *, int *);
typedef bool (*CuteQQuickBoundaryRuleCall4)(const void *, QUntypedBindable *, const QUntypedBindable *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickBoundaryRuleCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickBoundaryRuleCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBoundaryRuleCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBoundaryRuleCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBoundaryRuleCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBoundaryRuleCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBoundaryRuleCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickBoundaryRule : public QQuickBoundaryRule {
public:
  using QQuickBoundaryRule::QQuickBoundaryRule;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QQmlPropertyValueInterceptor9setTargetERK12QQmlProperty")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQmlPropertyValueInterceptor5writeERK8QVariant")) {
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
    if (!std::strcmp(key, "_ZN28QQmlPropertyValueInterceptor8bindableEP16QUntypedBindableS0_")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickBoundaryRule::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall0 call = reinterpret_cast<CuteQQuickBoundaryRuleCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickBoundaryRule::setTarget(a0);
  }

  //  void QQuickBoundaryRule::write(const QVariant &value)
  void write(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall1 call = reinterpret_cast<CuteQQuickBoundaryRuleCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QQuickBoundaryRule::write(value);
  }

  //  void QQuickBoundaryRule::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall2 call = reinterpret_cast<CuteQQuickBoundaryRuleCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBoundaryRule::classBegin();
  }

  //  void QQuickBoundaryRule::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall3 call = reinterpret_cast<CuteQQuickBoundaryRuleCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBoundaryRule::componentComplete();
  }

  //  bool QQmlPropertyValueInterceptor::bindable(QUntypedBindable
  //      *bindable, QUntypedBindable target)
  bool bindable(
      QUntypedBindable *bindable,
      QUntypedBindable target) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall4 call = reinterpret_cast<CuteQQuickBoundaryRuleCall4>(taken[4]);
      bool given = call(this, bindable, &target, &handled);
      if (handled) return given;
    }
    return QQmlPropertyValueInterceptor::bindable(bindable, target);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall5 call = reinterpret_cast<CuteQQuickBoundaryRuleCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall6 call = reinterpret_cast<CuteQQuickBoundaryRuleCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall7 call = reinterpret_cast<CuteQQuickBoundaryRuleCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall8 call = reinterpret_cast<CuteQQuickBoundaryRuleCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall9 call = reinterpret_cast<CuteQQuickBoundaryRuleCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall10 call = reinterpret_cast<CuteQQuickBoundaryRuleCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickBoundaryRuleCall11 call = reinterpret_cast<CuteQQuickBoundaryRuleCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickBoundaryRule::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickBoundaryRule10metaObjectEv(
    const QQuickBoundaryRule *self) {
  return self->metaObject();
}

//  void *QQuickBoundaryRule::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickBoundaryRule11qt_metacastEPKc(
    QQuickBoundaryRule *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickBoundaryRule::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickBoundaryRule11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickBoundaryRule *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickBoundaryRule::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickBoundaryRule2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickBoundaryRule::tr(s, c, n));
}

//  QQuickBoundaryRulePrivate *QQuickBoundaryRule::d_func()
extern "C" Q_DECL_EXPORT
QQuickBoundaryRulePrivate *ritual_ZN18QQuickBoundaryRule6d_funcEv(
    QQuickBoundaryRule *self) {
  return self->d_func();
}

//  const QQuickBoundaryRulePrivate *QQuickBoundaryRule::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickBoundaryRulePrivate *ritual_ZNK18QQuickBoundaryRule6d_funcEv(
    const QQuickBoundaryRule *self) {
  return self->d_func();
}

//  QQuickBoundaryRule::QQuickBoundaryRule(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickBoundaryRule *ritual_ZN18QQuickBoundaryRuleC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickBoundaryRule(parent);
}

//  QQuickBoundaryRule::~QQuickBoundaryRule()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRuleD1Ev(QQuickBoundaryRule *self) {
  delete self;
}

//  void QQuickBoundaryRule::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule9setTargetERK12QQmlProperty(
    QQuickBoundaryRule *self,
    const QQmlProperty *a0) {
  self->setTarget(*a0);
}

//  void QQuickBoundaryRule::write(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule5writeERK8QVariant(
    QQuickBoundaryRule *self,
    const QVariant *value) {
  self->write(*value);
}

//  bool QQuickBoundaryRule::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickBoundaryRule7enabledEv(
    const QQuickBoundaryRule *self) {
  return self->enabled();
}

//  void QQuickBoundaryRule::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule10setEnabledEb(
    QQuickBoundaryRule *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  qreal QQuickBoundaryRule::minimum() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickBoundaryRule7minimumEv(
    const QQuickBoundaryRule *self) {
  return self->minimum();
}

//  void QQuickBoundaryRule::setMinimum(qreal minimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule10setMinimumEd(
    QQuickBoundaryRule *self,
    qreal minimum) {
  self->setMinimum(minimum);
}

//  qreal QQuickBoundaryRule::minimumOvershoot() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickBoundaryRule16minimumOvershootEv(
    const QQuickBoundaryRule *self) {
  return self->minimumOvershoot();
}

//  void QQuickBoundaryRule::setMinimumOvershoot(qreal minimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule19setMinimumOvershootEd(
    QQuickBoundaryRule *self,
    qreal minimum) {
  self->setMinimumOvershoot(minimum);
}

//  qreal QQuickBoundaryRule::maximum() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickBoundaryRule7maximumEv(
    const QQuickBoundaryRule *self) {
  return self->maximum();
}

//  void QQuickBoundaryRule::setMaximum(qreal maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule10setMaximumEd(
    QQuickBoundaryRule *self,
    qreal maximum) {
  self->setMaximum(maximum);
}

//  qreal QQuickBoundaryRule::maximumOvershoot() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickBoundaryRule16maximumOvershootEv(
    const QQuickBoundaryRule *self) {
  return self->maximumOvershoot();
}

//  void QQuickBoundaryRule::setMaximumOvershoot(qreal maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule19setMaximumOvershootEd(
    QQuickBoundaryRule *self,
    qreal maximum) {
  self->setMaximumOvershoot(maximum);
}

//  qreal QQuickBoundaryRule::overshootScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickBoundaryRule14overshootScaleEv(
    const QQuickBoundaryRule *self) {
  return self->overshootScale();
}

//  void QQuickBoundaryRule::setOvershootScale(qreal scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule17setOvershootScaleEd(
    QQuickBoundaryRule *self,
    qreal scale) {
  self->setOvershootScale(scale);
}

//  qreal QQuickBoundaryRule::currentOvershoot() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickBoundaryRule16currentOvershootEv(
    const QQuickBoundaryRule *self) {
  return self->currentOvershoot();
}

//  qreal QQuickBoundaryRule::peakOvershoot() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickBoundaryRule13peakOvershootEv(
    const QQuickBoundaryRule *self) {
  return self->peakOvershoot();
}

//  OvershootFilter QQuickBoundaryRule::overshootFilter() const
extern "C" Q_DECL_EXPORT
QQuickBoundaryRule::OvershootFilter ritual_ZNK18QQuickBoundaryRule15overshootFilterEv(
    const QQuickBoundaryRule *self) {
  return self->overshootFilter();
}

//  void QQuickBoundaryRule::setOvershootFilter(OvershootFilter
//      overshootFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule18setOvershootFilterENS_15OvershootFilterE(
    QQuickBoundaryRule *self,
    QQuickBoundaryRule::OvershootFilter overshootFilter) {
  self->setOvershootFilter(overshootFilter);
}

//  bool QQuickBoundaryRule::returnToBounds()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickBoundaryRule14returnToBoundsEv(
    QQuickBoundaryRule *self) {
  return self->returnToBounds();
}

//  QEasingCurve QQuickBoundaryRule::easing() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK18QQuickBoundaryRule6easingEv(
    const QQuickBoundaryRule *self) {
  return new QEasingCurve(self->easing());
}

//  void QQuickBoundaryRule::setEasing(const QEasingCurve &easing)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule9setEasingERK12QEasingCurve(
    QQuickBoundaryRule *self,
    const QEasingCurve *easing) {
  self->setEasing(*easing);
}

//  int QQuickBoundaryRule::returnDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickBoundaryRule14returnDurationEv(
    const QQuickBoundaryRule *self) {
  return self->returnDuration();
}

//  void QQuickBoundaryRule::setReturnDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule17setReturnDurationEi(
    QQuickBoundaryRule *self,
    int duration) {
  self->setReturnDuration(duration);
}

//  void QQuickBoundaryRule::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule10classBeginEv(QQuickBoundaryRule *self) {
  self->classBegin();
}

//  void QQuickBoundaryRule::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule17componentCompleteEv(
    QQuickBoundaryRule *self) {
  self->componentComplete();
}

//  void QQuickBoundaryRule::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule14enabledChangedEv(
    QQuickBoundaryRule *self) {
  self->enabledChanged();
}

//  void QQuickBoundaryRule::minimumChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule14minimumChangedEv(
    QQuickBoundaryRule *self) {
  self->minimumChanged();
}

//  void QQuickBoundaryRule::minimumOvershootChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule23minimumOvershootChangedEv(
    QQuickBoundaryRule *self) {
  self->minimumOvershootChanged();
}

//  void QQuickBoundaryRule::maximumChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule14maximumChangedEv(
    QQuickBoundaryRule *self) {
  self->maximumChanged();
}

//  void QQuickBoundaryRule::maximumOvershootChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule23maximumOvershootChangedEv(
    QQuickBoundaryRule *self) {
  self->maximumOvershootChanged();
}

//  void QQuickBoundaryRule::overshootScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule21overshootScaleChangedEv(
    QQuickBoundaryRule *self) {
  self->overshootScaleChanged();
}

//  void QQuickBoundaryRule::currentOvershootChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule23currentOvershootChangedEv(
    QQuickBoundaryRule *self) {
  self->currentOvershootChanged();
}

//  void QQuickBoundaryRule::peakOvershootChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule20peakOvershootChangedEv(
    QQuickBoundaryRule *self) {
  self->peakOvershootChanged();
}

//  void QQuickBoundaryRule::overshootFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule22overshootFilterChangedEv(
    QQuickBoundaryRule *self) {
  self->overshootFilterChanged();
}

//  void QQuickBoundaryRule::easingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule13easingChangedEv(
    QQuickBoundaryRule *self) {
  self->easingChanged();
}

//  void QQuickBoundaryRule::returnDurationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule21returnDurationChangedEv(
    QQuickBoundaryRule *self) {
  self->returnDurationChanged();
}

//  void QQuickBoundaryRule::returnedToBounds()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickBoundaryRule16returnedToBoundsEv(
    QQuickBoundaryRule *self) {
  self->returnedToBounds();
}

//  QQuickBoundaryRule as the QQmlPropertyValueInterceptor it is built on
extern "C" Q_DECL_EXPORT
QQmlPropertyValueInterceptor *ritual_cast_QQuickBoundaryRule_QQmlPropertyValueInterceptor(
    QQuickBoundaryRule *self) {
  return static_cast<QQmlPropertyValueInterceptor *>(self);
}

//  QQuickBoundaryRule as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickBoundaryRule_QQmlParserStatus(
    QQuickBoundaryRule *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickBoundaryRule, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickBoundaryRule(
    QQuickBoundaryRule *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickBoundaryRule *>(self)->take(key, call);
}

//  void QQuickBoundaryRule::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickBoundaryRule9setTargetERK12QQmlProperty(
    QQuickBoundaryRule *self,
    const QQmlProperty *a0) {
  self->QQuickBoundaryRule::setTarget(*a0);
}

//  void QQuickBoundaryRule::write(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickBoundaryRule5writeERK8QVariant(
    QQuickBoundaryRule *self,
    const QVariant *value) {
  self->QQuickBoundaryRule::write(*value);
}

//  void QQuickBoundaryRule::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickBoundaryRule10classBeginEv(
    QQuickBoundaryRule *self) {
  self->QQuickBoundaryRule::classBegin();
}

//  void QQuickBoundaryRule::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickBoundaryRule17componentCompleteEv(
    QQuickBoundaryRule *self) {
  self->QQuickBoundaryRule::componentComplete();
}
