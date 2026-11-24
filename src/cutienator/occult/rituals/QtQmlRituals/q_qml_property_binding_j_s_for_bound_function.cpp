//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlPropertyBindingJSForBoundFunction that Python can take functions over in. Every QQmlPropertyBindingJSForBoundFunction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlPropertyBindingJSForBoundFunctionCall0)(const void *, int *);
typedef QString * (*CuteQQmlPropertyBindingJSForBoundFunctionCall1)(const void *, int *);
typedef const QQmlSourceLocation * (*CuteQQmlPropertyBindingJSForBoundFunctionCall2)(const void *, int *);
typedef void (*CuteQQmlPropertyBindingJSForBoundFunctionCall3)(const void *, int *);
class CuteQQmlPropertyBindingJSForBoundFunction : public QQmlPropertyBindingJSForBoundFunction {
public:
  using QQmlPropertyBindingJSForBoundFunction::QQmlPropertyBindingJSForBoundFunction;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQmlJavaScriptExpression17expressionChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQmlJavaScriptExpression20expressionIdentifierEv")) {
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
    return false;
  }

  //  void QQmlPropertyBindingJS::expressionChanged()
  void expressionChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlPropertyBindingJSForBoundFunctionCall0 call = reinterpret_cast<CuteQQmlPropertyBindingJSForBoundFunctionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlPropertyBindingJS::expressionChanged();
  }

  //  QString QQmlJavaScriptExpression::expressionIdentifier() const
  QString expressionIdentifier() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlPropertyBindingJSForBoundFunctionCall1 call = reinterpret_cast<CuteQQmlPropertyBindingJSForBoundFunctionCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlJavaScriptExpression::expressionIdentifier();
  }

  //  QQmlSourceLocation QQmlJavaScriptExpression::sourceLocation() const
  QQmlSourceLocation sourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlPropertyBindingJSForBoundFunctionCall2 call = reinterpret_cast<CuteQQmlPropertyBindingJSForBoundFunctionCall2>(taken[2]);
      const QQmlSourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJavaScriptExpression::sourceLocation();
  }

  //  void QQmlJavaScriptExpression::refresh()
  void refresh() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlPropertyBindingJSForBoundFunctionCall3 call = reinterpret_cast<CuteQQmlPropertyBindingJSForBoundFunctionCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJavaScriptExpression::refresh();
  }
};

//  QV4::ReturnedValue QQmlPropertyBindingJSForBoundFunction::evaluate(bool
//      *isUndefined)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN37QQmlPropertyBindingJSForBoundFunction8evaluateEPb(
    QQmlPropertyBindingJSForBoundFunction *self,
    bool *isUndefined) {
  return self->evaluate(isUndefined);
}

//  a Python function taken by a CuteQQmlPropertyBindingJSForBoundFunction,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlPropertyBindingJSForBoundFunction(
    QQmlPropertyBindingJSForBoundFunction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlPropertyBindingJSForBoundFunction *>(self)->take(key, call);
}
