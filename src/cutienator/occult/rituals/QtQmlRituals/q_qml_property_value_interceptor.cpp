//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertyvalueinterceptor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyvalueinterceptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlproperty.h>
#include <QtCore/qvariant.h>
#include <QtCore/qproperty.h>
#include <cstring>

//  A QQmlPropertyValueInterceptor that Python can take functions over in. Every QQmlPropertyValueInterceptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlPropertyValueInterceptorCall0)(const void *, const QQmlProperty *, int *);
typedef void (*CuteQQmlPropertyValueInterceptorCall1)(const void *, const QVariant *, int *);
typedef bool (*CuteQQmlPropertyValueInterceptorCall2)(const void *, QUntypedBindable *, const QUntypedBindable *, int *);
class CuteQQmlPropertyValueInterceptor : public QQmlPropertyValueInterceptor {
public:
  using QQmlPropertyValueInterceptor::QQmlPropertyValueInterceptor;
  void *taken[3] = {};

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
    return false;
  }

  //  void QQmlPropertyValueInterceptor::setTarget(const QQmlProperty
  //      &property)
  void setTarget(const QQmlProperty &property) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlPropertyValueInterceptorCall0 call = reinterpret_cast<CuteQQmlPropertyValueInterceptorCall0>(taken[0]);
      call(this, &property, &handled);
      if (handled) return;
    }
  }

  //  void QQmlPropertyValueInterceptor::write(const QVariant &value)
  void write(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlPropertyValueInterceptorCall1 call = reinterpret_cast<CuteQQmlPropertyValueInterceptorCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlPropertyValueInterceptor::bindable(QUntypedBindable
  //      *bindable, QUntypedBindable target)
  bool bindable(
      QUntypedBindable *bindable,
      QUntypedBindable target) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlPropertyValueInterceptorCall2 call = reinterpret_cast<CuteQQmlPropertyValueInterceptorCall2>(taken[2]);
      bool given = call(this, bindable, &target, &handled);
      if (handled) return given;
    }
    return QQmlPropertyValueInterceptor::bindable(bindable, target);
  }
};

//  QQmlPropertyValueInterceptor::~QQmlPropertyValueInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlPropertyValueInterceptorD1Ev(
    QQmlPropertyValueInterceptor *self) {
  delete self;
}

//  void QQmlPropertyValueInterceptor::setTarget(const QQmlProperty
//      &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlPropertyValueInterceptor9setTargetERK12QQmlProperty(
    QQmlPropertyValueInterceptor *self,
    const QQmlProperty *property) {
  self->setTarget(*property);
}

//  void QQmlPropertyValueInterceptor::write(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlPropertyValueInterceptor5writeERK8QVariant(
    QQmlPropertyValueInterceptor *self,
    const QVariant *value) {
  self->write(*value);
}

//  bool QQmlPropertyValueInterceptor::bindable(QUntypedBindable *bindable,
//      QUntypedBindable target)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QQmlPropertyValueInterceptor8bindableEP16QUntypedBindableS0_(
    QQmlPropertyValueInterceptor *self,
    QUntypedBindable *bindable,
    const QUntypedBindable *target) {
  return self->bindable(bindable, *target);
}

//  a Python function taken by a CuteQQmlPropertyValueInterceptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlPropertyValueInterceptor(
    QQmlPropertyValueInterceptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlPropertyValueInterceptor *>(self)->take(key, call);
}

//  bool QQmlPropertyValueInterceptor::bindable(QUntypedBindable *bindable,
//      QUntypedBindable target)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QQmlPropertyValueInterceptor8bindableEP16QUntypedBindableS0_(
    QQmlPropertyValueInterceptor *self,
    QUntypedBindable *bindable,
    const QUntypedBindable *target) {
  return self->QQmlPropertyValueInterceptor::bindable(bindable, *target);
}
