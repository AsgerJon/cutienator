//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

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

//  bool QQmlBoundSignalExpression::expressionFunctionValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlBoundSignalExpression23expressionFunctionValidEv(
    const QQmlBoundSignalExpression *self) {
  return self->expressionFunctionValid();
}
