//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxmlQml/6.12.0/QtScxmlQml/private/statemachineextended_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/qscxmlqmlglobals_p.h>
#include <QtScxmlQml/QtScxmlQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/statemachineextended_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QScxmlStateMachineExtended::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QScxmlStateMachineExtended10metaObjectEv(
    const QScxmlStateMachineExtended *self) {
  return self->metaObject();
}

//  QString QScxmlStateMachineExtended::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QScxmlStateMachineExtended2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlStateMachineExtended::tr(s, c, n));
}

//  QScxmlStateMachineExtended::QScxmlStateMachineExtended(QObject *extendee)
extern "C" Q_DECL_EXPORT
QScxmlStateMachineExtended *ritual_ZN26QScxmlStateMachineExtendedC1EP7QObject(
    QObject *extendee) {
  return new QScxmlStateMachineExtended(extendee);
}
