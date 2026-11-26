//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const quint32_le *QV4::CompiledData::Block::localsTable() const
extern "C" Q_DECL_EXPORT
const quint32_le *ritual_ZNK3QV412CompiledData5Block11localsTableEv(
    const QV4::CompiledData::Block *self) {
  return self->localsTable();
}

//  int QV4::CompiledData::Block::calculateSize(int nLocals)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV412CompiledData5Block13calculateSizeEi(int nLocals) {
  return QV4::CompiledData::Block::calculateSize(nLocals);
}

//  size_t QV4::CompiledData::Block::align(size_t a)
extern "C" Q_DECL_EXPORT
size_t ritual_ZN3QV412CompiledData5Block5alignEm(size_t a) {
  return QV4::CompiledData::Block::align(a);
}

//  QV4::CompiledData::Block::~Block()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData5BlockD1Ev(QV4::CompiledData::Block *self) {
  delete self;
}
