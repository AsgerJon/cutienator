//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlJavaScriptExpression::DeleteWatcher::DeleteWatcher(QQmlJavaScriptExpr
//      ession *a0)
extern "C" Q_DECL_EXPORT
QQmlJavaScriptExpression::DeleteWatcher *ritual_ZN24QQmlJavaScriptExpression13DeleteWatcherC1EPS_(
    QQmlJavaScriptExpression *a0) {
  return new QQmlJavaScriptExpression::DeleteWatcher(a0);
}

//  QQmlJavaScriptExpression::DeleteWatcher::~DeleteWatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJavaScriptExpression13DeleteWatcherD1Ev(
    QQmlJavaScriptExpression::DeleteWatcher *self) {
  delete self;
}

//  bool QQmlJavaScriptExpression::DeleteWatcher::wasDeleted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJavaScriptExpression13DeleteWatcher10wasDeletedEv(
    const QQmlJavaScriptExpression::DeleteWatcher *self) {
  return self->wasDeleted();
}
