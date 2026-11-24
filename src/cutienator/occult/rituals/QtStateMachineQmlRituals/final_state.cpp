//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachineQml/6.12.0/QtStateMachineQml/private/finalstate_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/qstatemachineqmlglobals_p.h>
#include <QtStateMachineQml/QtStateMachineQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/finalstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *FinalState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10FinalState10metaObjectEv(
    const FinalState *self) {
  return self->metaObject();
}

//  QString FinalState::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10FinalState2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(FinalState::tr(s, c, n));
}

//  FinalState::FinalState(QState *parent)
extern "C" Q_DECL_EXPORT
FinalState *ritual_ZN10FinalStateC1EP6QState(QState *parent) {
  return new FinalState(parent);
}

//  void FinalState::childrenContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10FinalState22childrenContentChangedEv(FinalState *self) {
  self->childrenContentChanged();
}
