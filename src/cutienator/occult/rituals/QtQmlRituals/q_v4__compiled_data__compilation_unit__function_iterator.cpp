//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::CompiledData::CompilationUnit::FunctionIterator::FunctionIterator(co
//      nst CompiledData::Unit *unit, const CompiledObject *object, int
//      index)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CompilationUnit::FunctionIterator *ritual_ZN3QV412CompiledData15CompilationUnit16FunctionIteratorC1EPKNS0_4UnitEPKNS0_6ObjectEi(
    const QV4::CompiledData::Unit *unit,
    const QV4::CompiledData::CompilationUnit::CompiledObject *object,
    int index) {
  return new QV4::CompiledData::CompilationUnit::FunctionIterator(
      unit,
      object,
      index);
}

//  const CompiledFunction
//      *QV4::CompiledData::CompilationUnit::FunctionIterator::operator->()
//      const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::CompilationUnit::CompiledFunction *ritual_ZNK3QV412CompiledData15CompilationUnit16FunctionIteratorptEv(
    const QV4::CompiledData::CompilationUnit::FunctionIterator *self) {
  return self->operator->();
}

//  void QV4::CompiledData::CompilationUnit::FunctionIterator::operator++()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData15CompilationUnit16FunctionIteratorppEv(
    QV4::CompiledData::CompilationUnit::FunctionIterator *self) {
  self->operator++();
}

//  bool
//      QV4::CompiledData::CompilationUnit::FunctionIterator::operator==(cons
//      t FunctionIterator &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit16FunctionIteratoreqERKS2_(
    const QV4::CompiledData::CompilationUnit::FunctionIterator *self,
    const QV4::CompiledData::CompilationUnit::FunctionIterator *rhs) {
  return self->operator==(*rhs);
}

//  bool
//      QV4::CompiledData::CompilationUnit::FunctionIterator::operator!=(cons
//      t FunctionIterator &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit16FunctionIteratorneERKS2_(
    const QV4::CompiledData::CompilationUnit::FunctionIterator *self,
    const QV4::CompiledData::CompilationUnit::FunctionIterator *rhs) {
  return self->operator!=(*rhs);
}

//  QV4::CompiledData::CompilationUnit::FunctionIterator::~FunctionIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData15CompilationUnit16FunctionIteratorD1Ev(
    QV4::CompiledData::CompilationUnit::FunctionIterator *self) {
  delete self;
}
