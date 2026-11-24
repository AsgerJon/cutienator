//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QmlIR::Signal::parameterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Signal14parameterCountEv(const QmlIR::Signal *self) {
  return self->parameterCount();
}

//  QmlIR::Signal::~Signal()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6SignalD1Ev(QmlIR::Signal *self) {
  delete self;
}
