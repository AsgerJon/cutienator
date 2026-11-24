//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvme_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdeadlinetimer.h>

//  QQmlInstantiationInterrupt::QQmlInstantiationInterrupt()
extern "C" Q_DECL_EXPORT
QQmlInstantiationInterrupt *ritual_ZN26QQmlInstantiationInterruptC1Ev() {
  return new QQmlInstantiationInterrupt();
}

//  QQmlInstantiationInterrupt::QQmlInstantiationInterrupt(QDeadlineTimer
//      deadline)
extern "C" Q_DECL_EXPORT
QQmlInstantiationInterrupt *ritual_ZN26QQmlInstantiationInterruptC1E14QDeadlineTimer(
    const QDeadlineTimer *deadline) {
  return new QQmlInstantiationInterrupt(*deadline);
}

//  bool QQmlInstantiationInterrupt::shouldInterrupt() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQmlInstantiationInterrupt15shouldInterruptEv(
    const QQmlInstantiationInterrupt *self) {
  return self->shouldInterrupt();
}

//  QQmlInstantiationInterrupt::~QQmlInstantiationInterrupt()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlInstantiationInterruptD1Ev(
    QQmlInstantiationInterrupt *self) {
  delete self;
}
