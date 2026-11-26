//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QQmlBoundSignalExpression::QQmlBoundSignalExpression(const QObject
//      *target, int index, const QQmlRefPointer<QQmlContextData> &ctxt,
//      QObject *scope, const QString &expression, const QString &fileName,
//      quint16 line, quint16 column, const QString &handlerName, const
//      QString &parameterString)
extern "C" Q_DECL_EXPORT
QQmlBoundSignalExpression *ritual_ZN25QQmlBoundSignalExpressionC1EPK7QObjectiRK14QQmlRefPointerI15QQmlContextDataEPS0_RK7QStringSB_ttSB_SB_(
    const QObject *target,
    int index,
    const QQmlRefPointer<QQmlContextData> *ctxt,
    QObject *scope,
    const QString *expression,
    const QString *fileName,
    quint16 line,
    quint16 column,
    const QString *handlerName,
    const QString *parameterString) {
  return new QQmlBoundSignalExpression(
      target,
      index,
      *ctxt,
      scope,
      *expression,
      *fileName,
      line,
      column,
      *handlerName,
      *parameterString);
}

//  QQmlBoundSignalExpression::QQmlBoundSignalExpression(const QObject
//      *target, int index, const QQmlRefPointer<QQmlContextData> &ctxt,
//      QObject *scopeObject, QV4::Function *function, QV4::ExecutionContext
//      *scope)
extern "C" Q_DECL_EXPORT
QQmlBoundSignalExpression *ritual_ZN25QQmlBoundSignalExpressionC1EPK7QObjectiRK14QQmlRefPointerI15QQmlContextDataEPS0_PN3QV48FunctionEPNS9_16ExecutionContextE(
    const QObject *target,
    int index,
    const QQmlRefPointer<QQmlContextData> *ctxt,
    QObject *scopeObject,
    QV4::Function *function,
    QV4::ExecutionContext *scope) {
  return new QQmlBoundSignalExpression(
      target,
      index,
      *ctxt,
      scopeObject,
      function,
      scope);
}

//  QString QQmlBoundSignalExpression::expressionIdentifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QQmlBoundSignalExpression20expressionIdentifierEv(
    const QQmlBoundSignalExpression *self) {
  return new QString(self->expressionIdentifier());
}

//  void QQmlBoundSignalExpression::expressionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlBoundSignalExpression17expressionChangedEv(
    QQmlBoundSignalExpression *self) {
  self->expressionChanged();
}

//  void QQmlBoundSignalExpression::evaluate(void **a)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlBoundSignalExpression8evaluateEPPv(
    QQmlBoundSignalExpression *self,
    void **a) {
  self->evaluate(a);
}

//  bool QQmlBoundSignalExpression::mustCaptureBindableProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlBoundSignalExpression27mustCaptureBindablePropertyEv(
    const QQmlBoundSignalExpression *self) {
  return self->mustCaptureBindableProperty();
}

//  QString QQmlBoundSignalExpression::expression() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QQmlBoundSignalExpression10expressionEv(
    const QQmlBoundSignalExpression *self) {
  return new QString(self->expression());
}

//  const QObject *QQmlBoundSignalExpression::target() const
extern "C" Q_DECL_EXPORT
const QObject *ritual_ZNK25QQmlBoundSignalExpression6targetEv(
    const QQmlBoundSignalExpression *self) {
  return self->target();
}

//  QQmlBoundSignalExpression::~QQmlBoundSignalExpression()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlBoundSignalExpressionD1Ev(
    QQmlBoundSignalExpression *self) {
  delete self;
}

//  void QQmlBoundSignalExpression::init(const
//      QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlBoundSignalExpression4initERK14QQmlRefPointerI15QQmlContextDataEP7QObject(
    QQmlBoundSignalExpression *self,
    const QQmlRefPointer<QQmlContextData> *ctxt,
    QObject *scope) {
  self->init(*ctxt, scope);
}

//  bool QQmlBoundSignalExpression::expressionFunctionValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlBoundSignalExpression23expressionFunctionValidEv(
    const QQmlBoundSignalExpression *self) {
  return self->expressionFunctionValid();
}
