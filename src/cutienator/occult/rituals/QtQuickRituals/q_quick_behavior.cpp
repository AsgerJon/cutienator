//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickbehavior_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickbehavior_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qvariant.h>
#include <QtCore/qproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickBehavior that Python can take functions over in. Every QQuickBehavior
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickBehaviorCall0)(const void *, const QQmlProperty *, int *);
typedef void (*CuteQQuickBehaviorCall1)(const void *, const QVariant *, int *);
typedef bool (*CuteQQuickBehaviorCall2)(const void *, QUntypedBindable *, const QUntypedBindable *, int *);
typedef void (*CuteQQuickBehaviorCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickBehaviorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickBehaviorCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBehaviorCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBehaviorCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBehaviorCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBehaviorCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBehaviorCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickBehavior : public QQuickBehavior {
public:
  using QQuickBehavior::QQuickBehavior;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QQmlPropertyValueInterceptor9setTargetERK12QQmlProperty")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQmlPropertyValueInterceptor5writeERK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QQmlPropertyValueInterceptor8bindableEP16QUntypedBindableS0_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQmlFinalizerHook18componentFinalizedEv")) {
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

  //  void QQuickBehavior::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickBehaviorCall0 call = reinterpret_cast<CuteQQuickBehaviorCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickBehavior::setTarget(a0);
  }

  //  void QQuickBehavior::write(const QVariant &value)
  void write(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickBehaviorCall1 call = reinterpret_cast<CuteQQuickBehaviorCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QQuickBehavior::write(value);
  }

  //  bool QQuickBehavior::bindable(QUntypedBindable *untypedBindable,
  //      QUntypedBindable target)
  bool bindable(
      QUntypedBindable *untypedBindable,
      QUntypedBindable target) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickBehaviorCall2 call = reinterpret_cast<CuteQQuickBehaviorCall2>(taken[2]);
      bool given = call(this, untypedBindable, &target, &handled);
      if (handled) return given;
    }
    return QQuickBehavior::bindable(untypedBindable, target);
  }

  //  void QQuickBehavior::componentFinalized()
  void componentFinalized() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickBehaviorCall3 call = reinterpret_cast<CuteQQuickBehaviorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBehavior::componentFinalized();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickBehaviorCall4 call = reinterpret_cast<CuteQQuickBehaviorCall4>(taken[4]);
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
      CuteQQuickBehaviorCall5 call = reinterpret_cast<CuteQQuickBehaviorCall5>(taken[5]);
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
      CuteQQuickBehaviorCall6 call = reinterpret_cast<CuteQQuickBehaviorCall6>(taken[6]);
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
      CuteQQuickBehaviorCall7 call = reinterpret_cast<CuteQQuickBehaviorCall7>(taken[7]);
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
      CuteQQuickBehaviorCall8 call = reinterpret_cast<CuteQQuickBehaviorCall8>(taken[8]);
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
      CuteQQuickBehaviorCall9 call = reinterpret_cast<CuteQQuickBehaviorCall9>(taken[9]);
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
      CuteQQuickBehaviorCall10 call = reinterpret_cast<CuteQQuickBehaviorCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickBehavior::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickBehavior10metaObjectEv(
    const QQuickBehavior *self) {
  return self->metaObject();
}

//  void *QQuickBehavior::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickBehavior11qt_metacastEPKc(
    QQuickBehavior *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickBehavior::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickBehavior11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickBehavior *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickBehavior::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickBehavior2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickBehavior::tr(s, c, n));
}

//  QQuickBehaviorPrivate *QQuickBehavior::d_func()
extern "C" Q_DECL_EXPORT
QQuickBehaviorPrivate *ritual_ZN14QQuickBehavior6d_funcEv(
    QQuickBehavior *self) {
  return self->d_func();
}

//  const QQuickBehaviorPrivate *QQuickBehavior::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickBehaviorPrivate *ritual_ZNK14QQuickBehavior6d_funcEv(
    const QQuickBehavior *self) {
  return self->d_func();
}

//  QQuickBehavior::QQuickBehavior(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickBehavior *ritual_ZN14QQuickBehaviorC1EP7QObject(QObject *parent) {
  return new CuteQQuickBehavior(parent);
}

//  QQuickBehavior::~QQuickBehavior()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickBehaviorD1Ev(QQuickBehavior *self) {
  delete self;
}

//  void QQuickBehavior::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickBehavior9setTargetERK12QQmlProperty(
    QQuickBehavior *self,
    const QQmlProperty *a0) {
  self->setTarget(*a0);
}

//  void QQuickBehavior::write(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickBehavior5writeERK8QVariant(
    QQuickBehavior *self,
    const QVariant *value) {
  self->write(*value);
}

//  bool QQuickBehavior::bindable(QUntypedBindable *untypedBindable,
//      QUntypedBindable target)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickBehavior8bindableEP16QUntypedBindableS0_(
    QQuickBehavior *self,
    QUntypedBindable *untypedBindable,
    const QUntypedBindable *target) {
  return self->bindable(untypedBindable, *target);
}

//  QQuickAbstractAnimation *QQuickBehavior::animation()
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation *ritual_ZN14QQuickBehavior9animationEv(
    QQuickBehavior *self) {
  return self->animation();
}

//  void QQuickBehavior::setAnimation(QQuickAbstractAnimation *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickBehavior12setAnimationEP23QQuickAbstractAnimation(
    QQuickBehavior *self,
    QQuickAbstractAnimation *a0) {
  self->setAnimation(a0);
}

//  bool QQuickBehavior::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickBehavior7enabledEv(const QQuickBehavior *self) {
  return self->enabled();
}

//  void QQuickBehavior::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickBehavior10setEnabledEb(
    QQuickBehavior *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  QVariant QQuickBehavior::targetValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickBehavior11targetValueEv(
    const QQuickBehavior *self) {
  return new QVariant(self->targetValue());
}

//  QQmlProperty QQuickBehavior::targetProperty() const
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZNK14QQuickBehavior14targetPropertyEv(
    const QQuickBehavior *self) {
  return new QQmlProperty(self->targetProperty());
}

//  void QQuickBehavior::componentFinalized()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickBehavior18componentFinalizedEv(QQuickBehavior *self) {
  self->componentFinalized();
}

//  void QQuickBehavior::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickBehavior14enabledChangedEv(QQuickBehavior *self) {
  self->enabledChanged();
}

//  void QQuickBehavior::targetValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickBehavior18targetValueChangedEv(QQuickBehavior *self) {
  self->targetValueChanged();
}

//  void QQuickBehavior::targetPropertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickBehavior21targetPropertyChangedEv(
    QQuickBehavior *self) {
  self->targetPropertyChanged();
}

//  QQuickBehavior as the QQmlPropertyValueInterceptor it is built on
extern "C" Q_DECL_EXPORT
QQmlPropertyValueInterceptor *ritual_cast_QQuickBehavior_QQmlPropertyValueInterceptor(
    QQuickBehavior *self) {
  return static_cast<QQmlPropertyValueInterceptor *>(self);
}

//  QQuickBehavior as the QQmlFinalizerHook it is built on
extern "C" Q_DECL_EXPORT
QQmlFinalizerHook *ritual_cast_QQuickBehavior_QQmlFinalizerHook(
    QQuickBehavior *self) {
  return static_cast<QQmlFinalizerHook *>(self);
}

//  a Python function taken by a CuteQQuickBehavior, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickBehavior(
    QQuickBehavior *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickBehavior *>(self)->take(key, call);
}

//  void QQuickBehavior::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickBehavior9setTargetERK12QQmlProperty(
    QQuickBehavior *self,
    const QQmlProperty *a0) {
  self->QQuickBehavior::setTarget(*a0);
}

//  void QQuickBehavior::write(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickBehavior5writeERK8QVariant(
    QQuickBehavior *self,
    const QVariant *value) {
  self->QQuickBehavior::write(*value);
}

//  bool QQuickBehavior::bindable(QUntypedBindable *untypedBindable,
//      QUntypedBindable target)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QQuickBehavior8bindableEP16QUntypedBindableS0_(
    QQuickBehavior *self,
    QUntypedBindable *untypedBindable,
    const QUntypedBindable *target) {
  return self->QQuickBehavior::bindable(untypedBindable, *target);
}

//  void QQuickBehavior::componentFinalized()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickBehavior18componentFinalizedEv(
    QQuickBehavior *self) {
  self->QQuickBehavior::componentFinalized();
}
