//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraydata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::ArrayElementLessThan::ArrayElementLessThan(ExecutionEngine *engine,
//      const Value &comparefn)
extern "C" Q_DECL_EXPORT
QV4::ArrayElementLessThan *ritual_ZN3QV420ArrayElementLessThanC1EPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::ExecutionEngine *engine,
    const QV4::Value *comparefn) {
  return new QV4::ArrayElementLessThan(engine, *comparefn);
}

//  QV4::ArrayElementLessThan::~ArrayElementLessThan()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV420ArrayElementLessThanD1Ev(
    QV4::ArrayElementLessThan *self) {
  delete self;
}
