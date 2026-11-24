//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ScriptFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414ScriptFunction10__dataTestEv(QV4::ScriptFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::ScriptFunction *QV4::ScriptFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ScriptFunction *ritual_ZNK3QV414ScriptFunction11d_uncheckedEv(
    const QV4::ScriptFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ScriptFunction *QV4::ScriptFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ScriptFunction *ritual_ZNK3QV414ScriptFunction1dEv(
    const QV4::ScriptFunction *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ScriptFunction::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV414ScriptFunction20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ScriptFunction::defaultInternalClass(e);
}
