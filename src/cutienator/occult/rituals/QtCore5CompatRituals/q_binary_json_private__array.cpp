//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const Value *QBinaryJsonPrivate::Array::at(uint i) const
extern "C" Q_DECL_EXPORT
const QBinaryJsonPrivate::Value *ritual_ZNK18QBinaryJsonPrivate5Array2atEj(
    const QBinaryJsonPrivate::Array *self,
    uint i) {
  return self->at(i);
}

//  Value *QBinaryJsonPrivate::Array::at(uint i)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::Value *ritual_ZN18QBinaryJsonPrivate5Array2atEj(
    QBinaryJsonPrivate::Array *self,
    uint i) {
  return self->at(i);
}

//  QBinaryJsonPrivate::Array::~Array()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5ArrayD1Ev(
    QBinaryJsonPrivate::Array *self) {
  delete self;
}
