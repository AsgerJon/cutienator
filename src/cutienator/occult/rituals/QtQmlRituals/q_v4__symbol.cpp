//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4symbol_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Symbol::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Symbol10__dataTestEv(QV4::Symbol *self) {
  self->__dataTest();
}

//  QV4::Heap::Symbol *QV4::Symbol::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Symbol *ritual_ZNK3QV46Symbol11d_uncheckedEv(
    const QV4::Symbol *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Symbol *QV4::Symbol::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Symbol *ritual_ZNK3QV46Symbol1dEv(const QV4::Symbol *self) {
  return self->d();
}

//  Heap::InternalClass *QV4::Symbol::defaultInternalClass(QV4::EngineBase
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV46Symbol20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::Symbol::defaultInternalClass(e);
}

//  void QV4::Symbol::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Symbol14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::Symbol::virtualDestroy(b);
}
