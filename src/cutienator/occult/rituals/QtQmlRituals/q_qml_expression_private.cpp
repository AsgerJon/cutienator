//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlexpression_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlexpression.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlexpression_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlexpression.h>
#include <QtQml/private/qqmlexpression_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlscriptstring_p.h>
#include <QtQml/private/qqmlbinding_p.h>
#include <QtQml/private/qqmlsourcecoordinate_p.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlexpression.cpp, line 409, as _ZN21QQmlExpressionPrivate17expressionChangedEv
inline void QQmlExpressionPrivate::expressionChanged()
{
    Q_Q(QQmlExpression);
    emit q->valueChanged();
}

//  from ../qtdeclarative/src/qml/qml/qqmlexpression.cpp, line 25, as _ZN21QQmlExpressionPrivateD2Ev
inline QQmlExpressionPrivate::~QQmlExpressionPrivate()
{
}

//  from ../qtdeclarative/src/qml/qml/qqmlexpression.cpp, line 415, as _ZNK21QQmlExpressionPrivate20expressionIdentifierEv
inline QString QQmlExpressionPrivate::expressionIdentifier() const
{
    return QLatin1Char('"') + expression + QLatin1Char('"');
}

//  from ../qtdeclarative/src/qml/qml/qqmlexpression.cpp, line 18, as _ZN21QQmlExpressionPrivateC1Ev
inline QQmlExpressionPrivate::QQmlExpressionPrivate()
: QQmlJavaScriptExpression(),
  expressionFunctionValid(true),
  line(0), column(0)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmlexpression.cpp, line 29, as _ZN21QQmlExpressionPrivate4initERK14QQmlRefPointerI15QQmlContextDataERK7QStringP7QObject
inline void QQmlExpressionPrivate::init(const QQmlRefPointer<QQmlContextData> &ctxt, const QString &expr,
                                 QObject *me)
{
    expression = expr;

    QQmlJavaScriptExpression::setContext(ctxt);
    setScopeObject(me);
    expressionFunctionValid = false;
}

//  from ../qtdeclarative/src/qml/qml/qqmlexpression.cpp, line 39, as _ZN21QQmlExpressionPrivate4initERK14QQmlRefPointerI15QQmlContextDataEPN3QV48FunctionEP7QObject
inline void QQmlExpressionPrivate::init(const QQmlRefPointer<QQmlContextData> &ctxt,
                                 QV4::Function *runtimeFunction, QObject *me)
{
    expressionFunctionValid = true;
    QV4::ExecutionEngine *engine = ctxt->engine()->handle();
    QV4::Scope scope(engine);
    QV4::Scoped<QV4::QmlContext> qmlContext(scope, QV4::QmlContext::create(engine->rootContext(), ctxt, me));
    setupFunction(qmlContext, runtimeFunction);

    QQmlJavaScriptExpression::setContext(ctxt);
    setScopeObject(me);
}

//  from ../qtdeclarative/src/qml/qml/qqmlexpression.cpp, line 236, as _ZN21QQmlExpressionPrivate5valueEPb
inline QVariant QQmlExpressionPrivate::value(bool *isUndefined)
{
    Q_Q(QQmlExpression);

    if (!hasValidContext()) {
        qWarning("QQmlExpression: Attempted to evaluate an expression in an invalid context");
        return QVariant();
    }

    QQmlEngine *engine = q->engine();
    QQmlEnginePrivate *ep = QQmlEnginePrivate::get(engine);
    QVariant rv;

    ep->referenceScarceResources(); // "hold" scarce resources in memory during evaluation.

    {
        QV4::Scope scope(engine->handle());
        QV4::ScopedValue result(scope, v4value(isUndefined));
        if (!hasError())
            rv = QV4::ExecutionEngine::toVariant(result, QMetaType {});
    }

    ep->dereferenceScarceResources(); // "release" scarce resources if top-level expression evaluation is complete.

    return rv;
}

//  from ../qtdeclarative/src/qml/qml/qqmlexpression.cpp, line 221, as _ZN21QQmlExpressionPrivate7v4valueEPb
inline QV4::ReturnedValue QQmlExpressionPrivate::v4value(bool *isUndefined)
{
    if (!expressionFunctionValid) {
        createQmlBinding(context(), scopeObject(), expression, url, line);
        expressionFunctionValid = true;
        if (hasError()) {
            if (isUndefined)
                *isUndefined = true;
            return QV4::Encode::undefined();
        }
    }

    return evaluate(isUndefined);
}
//  -----------------------------------------------------------------------

//  A QQmlExpressionPrivate that Python can take functions over in. Every QQmlExpressionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQQmlExpressionPrivateCall0)(const void *, int *);
typedef void (*CuteQQmlExpressionPrivateCall1)(const void *, int *);
typedef const QQmlSourceLocation * (*CuteQQmlExpressionPrivateCall2)(const void *, int *);
typedef void (*CuteQQmlExpressionPrivateCall3)(const void *, int *);
class CuteQQmlExpressionPrivate : public QQmlExpressionPrivate {
public:
  using QQmlExpressionPrivate::QQmlExpressionPrivate;
  void *taken[4] = {};

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
    return false;
  }

  //  QString QQmlExpressionPrivate::expressionIdentifier() const
  QString expressionIdentifier() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlExpressionPrivateCall0 call = reinterpret_cast<CuteQQmlExpressionPrivateCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlExpressionPrivate::expressionIdentifier();
  }

  //  void QQmlExpressionPrivate::expressionChanged()
  void expressionChanged() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlExpressionPrivateCall1 call = reinterpret_cast<CuteQQmlExpressionPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlExpressionPrivate::expressionChanged();
  }

  //  QQmlSourceLocation QQmlJavaScriptExpression::sourceLocation() const
  QQmlSourceLocation sourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlExpressionPrivateCall2 call = reinterpret_cast<CuteQQmlExpressionPrivateCall2>(taken[2]);
      const QQmlSourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJavaScriptExpression::sourceLocation();
  }

  //  void QQmlJavaScriptExpression::refresh()
  void refresh() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlExpressionPrivateCall3 call = reinterpret_cast<CuteQQmlExpressionPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJavaScriptExpression::refresh();
  }
};

//  QQmlExpression *QQmlExpressionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlExpression *ritual_ZN21QQmlExpressionPrivate6q_funcEv(
    QQmlExpressionPrivate *self) {
  return self->q_func();
}

//  const QQmlExpression *QQmlExpressionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlExpression *ritual_ZNK21QQmlExpressionPrivate6q_funcEv(
    const QQmlExpressionPrivate *self) {
  return self->q_func();
}

//  QQmlExpressionPrivate::QQmlExpressionPrivate()
extern "C" Q_DECL_EXPORT
QQmlExpressionPrivate *ritual_ZN21QQmlExpressionPrivateC1Ev() {
  return new CuteQQmlExpressionPrivate();
}

//  QQmlExpressionPrivate::~QQmlExpressionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlExpressionPrivateD1Ev(QQmlExpressionPrivate *self) {
  delete self;
}

//  void QQmlExpressionPrivate::init(const QQmlRefPointer<QQmlContextData>
//      &a0, const QString &a1, QObject *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlExpressionPrivate4initERK14QQmlRefPointerI15QQmlContextDataERK7QStringP7QObject(
    QQmlExpressionPrivate *self,
    const QQmlRefPointer<QQmlContextData> *a0,
    const QString *a1,
    QObject *a2) {
  self->init(*a0, *a1, a2);
}

//  void QQmlExpressionPrivate::init(const QQmlRefPointer<QQmlContextData>
//      &a0, QV4::Function *runtimeFunction, QObject *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlExpressionPrivate4initERK14QQmlRefPointerI15QQmlContextDataEPN3QV48FunctionEP7QObject(
    QQmlExpressionPrivate *self,
    const QQmlRefPointer<QQmlContextData> *a0,
    QV4::Function *runtimeFunction,
    QObject *a2) {
  self->init(*a0, runtimeFunction, a2);
}

//  QVariant QQmlExpressionPrivate::value(bool *isUndefined)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN21QQmlExpressionPrivate5valueEPb(
    QQmlExpressionPrivate *self,
    bool *isUndefined) {
  return new QVariant(self->value(isUndefined));
}

//  QV4::ReturnedValue QQmlExpressionPrivate::v4value(bool *isUndefined)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN21QQmlExpressionPrivate7v4valueEPb(
    QQmlExpressionPrivate *self,
    bool *isUndefined) {
  return self->v4value(isUndefined);
}

//  bool QQmlExpressionPrivate::mustCaptureBindableProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQmlExpressionPrivate27mustCaptureBindablePropertyEv(
    const QQmlExpressionPrivate *self) {
  return self->mustCaptureBindableProperty();
}

//  QQmlExpressionPrivate *QQmlExpressionPrivate::get(QQmlExpression *expr)
extern "C" Q_DECL_EXPORT
QQmlExpressionPrivate *ritual_ZN21QQmlExpressionPrivate3getEP14QQmlExpression(
    QQmlExpression *expr) {
  return QQmlExpressionPrivate::get(expr);
}

//  QQmlExpression *QQmlExpressionPrivate::get(QQmlExpressionPrivate *expr)
extern "C" Q_DECL_EXPORT
QQmlExpression *ritual_ZN21QQmlExpressionPrivate3getEPS_(
    QQmlExpressionPrivate *expr) {
  return QQmlExpressionPrivate::get(expr);
}

//  QString QQmlExpressionPrivate::expressionIdentifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlExpressionPrivate20expressionIdentifierEv(
    const QQmlExpressionPrivate *self) {
  return new QString(self->expressionIdentifier());
}

//  void QQmlExpressionPrivate::expressionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlExpressionPrivate17expressionChangedEv(
    QQmlExpressionPrivate *self) {
  self->expressionChanged();
}

//  QQmlExpressionPrivate as the QQmlJavaScriptExpression it is built on
extern "C" Q_DECL_EXPORT
QQmlJavaScriptExpression *ritual_cast_QQmlExpressionPrivate_QQmlJavaScriptExpression(
    QQmlExpressionPrivate *self) {
  return static_cast<QQmlJavaScriptExpression *>(self);
}

//  a Python function taken by a CuteQQmlExpressionPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlExpressionPrivate(
    QQmlExpressionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlExpressionPrivate *>(self)->take(key, call);
}

//  QString QQmlExpressionPrivate::expressionIdentifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QQmlExpressionPrivate20expressionIdentifierEv(
    const QQmlExpressionPrivate *self) {
  return new QString(self->QQmlExpressionPrivate::expressionIdentifier());
}

//  void QQmlExpressionPrivate::expressionChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQmlExpressionPrivate17expressionChangedEv(
    QQmlExpressionPrivate *self) {
  self->QQmlExpressionPrivate::expressionChanged();
}
