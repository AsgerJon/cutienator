//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlBoundSignal::QQmlBoundSignal(QObject *target, int signal, QObject
//      *owner, QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
QQmlBoundSignal *ritual_ZN15QQmlBoundSignalC1EP7QObjectiS1_P10QQmlEngine(
    QObject *target,
    int signal,
    QObject *owner,
    QQmlEngine *engine) {
  return new QQmlBoundSignal(target, signal, owner, engine);
}

//  QQmlBoundSignal::~QQmlBoundSignal()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlBoundSignalD1Ev(QQmlBoundSignal *self) {
  delete self;
}

//  void QQmlBoundSignal::removeFromObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlBoundSignal16removeFromObjectEv(QQmlBoundSignal *self) {
  self->removeFromObject();
}

//  QQmlBoundSignalExpression *QQmlBoundSignal::expression() const
extern "C" Q_DECL_EXPORT
QQmlBoundSignalExpression *ritual_ZNK15QQmlBoundSignal10expressionEv(
    const QQmlBoundSignal *self) {
  return self->expression();
}

//  void QQmlBoundSignal::takeExpression(QQmlBoundSignalExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlBoundSignal14takeExpressionEP25QQmlBoundSignalExpression(
    QQmlBoundSignal *self,
    QQmlBoundSignalExpression *a0) {
  self->takeExpression(a0);
}

//  void QQmlBoundSignal::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlBoundSignal10setEnabledEb(
    QQmlBoundSignal *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QQmlBoundSignal::addToObject(QObject *owner)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlBoundSignal11addToObjectEP7QObject(
    QQmlBoundSignal *self,
    QObject *owner) {
  self->addToObject(owner);
}
