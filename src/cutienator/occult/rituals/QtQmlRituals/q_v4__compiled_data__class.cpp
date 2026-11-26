//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const Method *QV4::CompiledData::Class::methodTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Method *ritual_ZNK3QV412CompiledData5Class11methodTableEv(
    const QV4::CompiledData::Class *self) {
  return self->methodTable();
}

//  int QV4::CompiledData::Class::calculateSize(int nStaticMethods, int
//      nMethods)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV412CompiledData5Class13calculateSizeEii(
    int nStaticMethods,
    int nMethods) {
  return QV4::CompiledData::Class::calculateSize(nStaticMethods, nMethods);
}

//  size_t QV4::CompiledData::Class::align(size_t a)
extern "C" Q_DECL_EXPORT
size_t ritual_ZN3QV412CompiledData5Class5alignEm(size_t a) {
  return QV4::CompiledData::Class::align(a);
}

//  QV4::CompiledData::Class::~Class()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData5ClassD1Ev(QV4::CompiledData::Class *self) {
  delete self;
}
