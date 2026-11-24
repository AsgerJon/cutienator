//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlerror.h>
#include <cstring>

//  A QQmlJavaScriptExpression that Python can take functions over in. Every QQmlJavaScriptExpression
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQQmlJavaScriptExpressionCall0)(const void *, int *);
typedef void (*CuteQQmlJavaScriptExpressionCall1)(const void *, int *);
typedef const QQmlSourceLocation * (*CuteQQmlJavaScriptExpressionCall2)(const void *, int *);
typedef void (*CuteQQmlJavaScriptExpressionCall3)(const void *, int *);
typedef bool (*CuteQQmlJavaScriptExpressionCall4)(const void *, int *);
class CuteQQmlJavaScriptExpression : public QQmlJavaScriptExpression {
public:
  using QQmlJavaScriptExpression::QQmlJavaScriptExpression;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK24QQmlJavaScriptExpression20expressionIdentifierEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQmlJavaScriptExpression17expressionChangedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQmlJavaScriptExpression14sourceLocationEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQmlJavaScriptExpression7refreshEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQmlJavaScriptExpression27mustCaptureBindablePropertyEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QString QQmlJavaScriptExpression::expressionIdentifier() const
  QString expressionIdentifier() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJavaScriptExpressionCall0 call = reinterpret_cast<CuteQQmlJavaScriptExpressionCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlJavaScriptExpression::expressionIdentifier();
  }

  //  void QQmlJavaScriptExpression::expressionChanged()
  void expressionChanged() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJavaScriptExpressionCall1 call = reinterpret_cast<CuteQQmlJavaScriptExpressionCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QQmlSourceLocation QQmlJavaScriptExpression::sourceLocation() const
  QQmlSourceLocation sourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJavaScriptExpressionCall2 call = reinterpret_cast<CuteQQmlJavaScriptExpressionCall2>(taken[2]);
      const QQmlSourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJavaScriptExpression::sourceLocation();
  }

  //  void QQmlJavaScriptExpression::refresh()
  void refresh() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJavaScriptExpressionCall3 call = reinterpret_cast<CuteQQmlJavaScriptExpressionCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJavaScriptExpression::refresh();
  }

  //  bool QQmlJavaScriptExpression::mustCaptureBindableProperty() const
  bool mustCaptureBindableProperty() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJavaScriptExpressionCall4 call = reinterpret_cast<CuteQQmlJavaScriptExpressionCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlJavaScriptExpression::mustCaptureBindableProperty();
  }
};

//  QQmlJavaScriptExpression::~QQmlJavaScriptExpression()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpressionD1Ev(
    QQmlJavaScriptExpression *self) {
  delete self;
}

//  QString QQmlJavaScriptExpression::expressionIdentifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQmlJavaScriptExpression20expressionIdentifierEv(
    const QQmlJavaScriptExpression *self) {
  return new QString(self->expressionIdentifier());
}

//  void QQmlJavaScriptExpression::expressionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression17expressionChangedEv(
    QQmlJavaScriptExpression *self) {
  self->expressionChanged();
}

//  QV4::ReturnedValue QQmlJavaScriptExpression::evaluate(bool *isUndefined)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN24QQmlJavaScriptExpression8evaluateEPb(
    QQmlJavaScriptExpression *self,
    bool *isUndefined) {
  return self->evaluate(isUndefined);
}

//  QV4::ReturnedValue QQmlJavaScriptExpression::evaluate(QV4::CallData
//      *callData, bool *isUndefined)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN24QQmlJavaScriptExpression8evaluateEPN3QV48CallDataEPb(
    QQmlJavaScriptExpression *self,
    QV4::CallData *callData,
    bool *isUndefined) {
  return self->evaluate(callData, isUndefined);
}

//  bool QQmlJavaScriptExpression::notifyOnValueChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJavaScriptExpression20notifyOnValueChangedEv(
    const QQmlJavaScriptExpression *self) {
  return self->notifyOnValueChanged();
}

//  void QQmlJavaScriptExpression::setNotifyOnValueChanged(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression23setNotifyOnValueChangedEb(
    QQmlJavaScriptExpression *self,
    bool v) {
  self->setNotifyOnValueChanged(v);
}

//  void QQmlJavaScriptExpression::resetNotifyOnValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression25resetNotifyOnValueChangedEv(
    QQmlJavaScriptExpression *self) {
  self->resetNotifyOnValueChanged();
}

//  QObject *QQmlJavaScriptExpression::scopeObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK24QQmlJavaScriptExpression11scopeObjectEv(
    const QQmlJavaScriptExpression *self) {
  return self->scopeObject();
}

//  void QQmlJavaScriptExpression::setScopeObject(QObject *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression14setScopeObjectEP7QObject(
    QQmlJavaScriptExpression *self,
    QObject *v) {
  self->setScopeObject(v);
}

//  QQmlSourceLocation QQmlJavaScriptExpression::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSourceLocation *ritual_ZNK24QQmlJavaScriptExpression14sourceLocationEv(
    const QQmlJavaScriptExpression *self) {
  return new QQmlSourceLocation(self->sourceLocation());
}

//  bool QQmlJavaScriptExpression::hasContext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJavaScriptExpression10hasContextEv(
    const QQmlJavaScriptExpression *self) {
  return self->hasContext();
}

//  bool QQmlJavaScriptExpression::hasValidContext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJavaScriptExpression15hasValidContextEv(
    const QQmlJavaScriptExpression *self) {
  return self->hasValidContext();
}

//  QQmlContext *QQmlJavaScriptExpression::publicContext() const
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZNK24QQmlJavaScriptExpression13publicContextEv(
    const QQmlJavaScriptExpression *self) {
  return self->publicContext();
}

//  QV4::Function *QQmlJavaScriptExpression::function() const
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZNK24QQmlJavaScriptExpression8functionEv(
    const QQmlJavaScriptExpression *self) {
  return self->function();
}

//  void QQmlJavaScriptExpression::setFunction(QV4::Function *f)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression11setFunctionEPN3QV48FunctionE(
    QQmlJavaScriptExpression *self,
    QV4::Function *f) {
  self->setFunction(f);
}

//  QV4::ExecutableCompilationUnit
//      *QQmlJavaScriptExpression::compilationUnit() const
extern "C" Q_DECL_EXPORT
QV4::ExecutableCompilationUnit *ritual_ZNK24QQmlJavaScriptExpression15compilationUnitEv(
    const QQmlJavaScriptExpression *self) {
  return self->compilationUnit();
}

//  QQmlJavaScriptExpression *QQmlJavaScriptExpression::nextExpression()
//      const
extern "C" Q_DECL_EXPORT
QQmlJavaScriptExpression *ritual_ZNK24QQmlJavaScriptExpression14nextExpressionEv(
    const QQmlJavaScriptExpression *self) {
  return self->nextExpression();
}

//  void QQmlJavaScriptExpression::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression7refreshEv(
    QQmlJavaScriptExpression *self) {
  self->refresh();
}

//  bool QQmlJavaScriptExpression::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJavaScriptExpression8hasErrorEv(
    const QQmlJavaScriptExpression *self) {
  return self->hasError();
}

//  bool QQmlJavaScriptExpression::hasDelayedError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJavaScriptExpression15hasDelayedErrorEv(
    const QQmlJavaScriptExpression *self) {
  return self->hasDelayedError();
}

//  QQmlError QQmlJavaScriptExpression::error(QQmlEngine *a0) const
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZNK24QQmlJavaScriptExpression5errorEP10QQmlEngine(
    const QQmlJavaScriptExpression *self,
    QQmlEngine *a0) {
  return new QQmlError(self->error(a0));
}

//  void QQmlJavaScriptExpression::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression10clearErrorEv(
    QQmlJavaScriptExpression *self) {
  self->clearError();
}

//  void QQmlJavaScriptExpression::clearActiveGuards()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression17clearActiveGuardsEv(
    QQmlJavaScriptExpression *self) {
  self->clearActiveGuards();
}

//  QQmlDelayedError *QQmlJavaScriptExpression::delayedError()
extern "C" Q_DECL_EXPORT
QQmlDelayedError *ritual_ZN24QQmlJavaScriptExpression12delayedErrorEv(
    QQmlJavaScriptExpression *self) {
  return self->delayedError();
}

//  bool QQmlJavaScriptExpression::mustCaptureBindableProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJavaScriptExpression27mustCaptureBindablePropertyEv(
    const QQmlJavaScriptExpression *self) {
  return self->mustCaptureBindableProperty();
}

//  QQmlEngine *QQmlJavaScriptExpression::engine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK24QQmlJavaScriptExpression6engineEv(
    const QQmlJavaScriptExpression *self) {
  return self->engine();
}

//  bool QQmlJavaScriptExpression::hasUnresolvedNames() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJavaScriptExpression18hasUnresolvedNamesEv(
    const QQmlJavaScriptExpression *self) {
  return self->hasUnresolvedNames();
}

//  bool QQmlJavaScriptExpression::needsPropertyChangeTrigger(QObject
//      *target, int propertyIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQmlJavaScriptExpression26needsPropertyChangeTriggerEP7QObjecti(
    QQmlJavaScriptExpression *self,
    QObject *target,
    int propertyIndex) {
  return self->needsPropertyChangeTrigger(target, propertyIndex);
}

//  QPropertyChangeTrigger
//      *QQmlJavaScriptExpression::allocatePropertyChangeTrigger(QObject
//      *target, int propertyIndex)
extern "C" Q_DECL_EXPORT
QPropertyChangeTrigger *ritual_ZN24QQmlJavaScriptExpression29allocatePropertyChangeTriggerEP7QObjecti(
    QQmlJavaScriptExpression *self,
    QObject *target,
    int propertyIndex) {
  return self->allocatePropertyChangeTrigger(target, propertyIndex);
}

//  void QQmlJavaScriptExpression::setupFunction(QV4::ExecutionContext
//      *qmlContext, QV4::Function *f)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression13setupFunctionEPN3QV416ExecutionContextEPNS0_8FunctionE(
    QQmlJavaScriptExpression *self,
    QV4::ExecutionContext *qmlContext,
    QV4::Function *f) {
  self->setupFunction(qmlContext, f);
}

//  a Python function taken by a CuteQQmlJavaScriptExpression, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJavaScriptExpression(
    QQmlJavaScriptExpression *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJavaScriptExpression *>(self)->take(key, call);
}

//  QString QQmlJavaScriptExpression::expressionIdentifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK24QQmlJavaScriptExpression20expressionIdentifierEv(
    const QQmlJavaScriptExpression *self) {
  return new QString(self->QQmlJavaScriptExpression::expressionIdentifier());
}

//  QQmlSourceLocation QQmlJavaScriptExpression::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSourceLocation *ritual_own_ZNK24QQmlJavaScriptExpression14sourceLocationEv(
    const QQmlJavaScriptExpression *self) {
  return new QQmlSourceLocation(
      self->QQmlJavaScriptExpression::sourceLocation());
}

//  void QQmlJavaScriptExpression::refresh()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQmlJavaScriptExpression7refreshEv(
    QQmlJavaScriptExpression *self) {
  self->QQmlJavaScriptExpression::refresh();
}

//  bool QQmlJavaScriptExpression::mustCaptureBindableProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QQmlJavaScriptExpression27mustCaptureBindablePropertyEv(
    const QQmlJavaScriptExpression *self) {
  return self->QQmlJavaScriptExpression::mustCaptureBindableProperty();
}
