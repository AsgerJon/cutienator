//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlengine_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlJavaScriptExpressionGuard::QQmlJavaScriptExpressionGuard(QQmlJavaScri
//      ptExpression *a0)
extern "C" Q_DECL_EXPORT
QQmlJavaScriptExpressionGuard *ritual_ZN29QQmlJavaScriptExpressionGuardC1EP24QQmlJavaScriptExpression(
    QQmlJavaScriptExpression *a0) {
  return new QQmlJavaScriptExpressionGuard(a0);
}

//  QQmlJavaScriptExpressionGuard
//      *QQmlJavaScriptExpressionGuard::New(QQmlJavaScriptExpression *e,
//      QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
QQmlJavaScriptExpressionGuard *ritual_ZN29QQmlJavaScriptExpressionGuard3NewEP24QQmlJavaScriptExpressionP10QQmlEngine(
    QQmlJavaScriptExpression *e,
    QQmlEngine *engine) {
  return QQmlJavaScriptExpressionGuard::New(e, engine);
}

//  void QQmlJavaScriptExpressionGuard::Delete()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlJavaScriptExpressionGuard6DeleteEv(
    QQmlJavaScriptExpressionGuard *self) {
  self->Delete();
}

//  QQmlJavaScriptExpressionGuard::~QQmlJavaScriptExpressionGuard()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlJavaScriptExpressionGuardD1Ev(
    QQmlJavaScriptExpressionGuard *self) {
  delete self;
}
