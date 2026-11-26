//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolortransfergeneric_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolortransfergeneric_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QColorTransferGenericFunction::QColorTransferGenericFunction(ConverterPtr
//      toLinear, ConverterPtr fromLinear)
extern "C" Q_DECL_EXPORT
QColorTransferGenericFunction *ritual_ZN29QColorTransferGenericFunctionC1EPFffES1_(
    void *toLinear,
    void *fromLinear) {
  return new QColorTransferGenericFunction(
      reinterpret_cast<QColorTransferGenericFunction::ConverterPtr>(toLinear),
      reinterpret_cast<QColorTransferGenericFunction::ConverterPtr>(fromLinear));
}

//  QColorTransferGenericFunction QColorTransferGenericFunction::hlg()
extern "C" Q_DECL_EXPORT
QColorTransferGenericFunction *ritual_ZN29QColorTransferGenericFunction3hlgEv() {
  return new QColorTransferGenericFunction(
      QColorTransferGenericFunction::hlg());
}

//  QColorTransferGenericFunction QColorTransferGenericFunction::pq()
extern "C" Q_DECL_EXPORT
QColorTransferGenericFunction *ritual_ZN29QColorTransferGenericFunction2pqEv() {
  return new QColorTransferGenericFunction(
      QColorTransferGenericFunction::pq());
}

//  float QColorTransferGenericFunction::apply(float x) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK29QColorTransferGenericFunction5applyEf(
    const QColorTransferGenericFunction *self,
    float x) {
  return self->apply(x);
}

//  float QColorTransferGenericFunction::applyInverse(float x) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK29QColorTransferGenericFunction12applyInverseEf(
    const QColorTransferGenericFunction *self,
    float x) {
  return self->applyInverse(x);
}

//  bool QColorTransferGenericFunction::operator==(const
//      QColorTransferGenericFunction &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QColorTransferGenericFunctioneqERKS_(
    const QColorTransferGenericFunction *self,
    const QColorTransferGenericFunction *o) {
  return self->operator==(*o);
}

//  bool QColorTransferGenericFunction::operator!=(const
//      QColorTransferGenericFunction &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QColorTransferGenericFunctionneERKS_(
    const QColorTransferGenericFunction *self,
    const QColorTransferGenericFunction *o) {
  return self->operator!=(*o);
}

//  float QColorTransferGenericFunction::hlgFromLinear(float x)
extern "C" Q_DECL_EXPORT
float ritual_ZN29QColorTransferGenericFunction13hlgFromLinearEf(float x) {
  return QColorTransferGenericFunction::hlgFromLinear(x);
}

//  float QColorTransferGenericFunction::hlgToLinear(float x)
extern "C" Q_DECL_EXPORT
float ritual_ZN29QColorTransferGenericFunction11hlgToLinearEf(float x) {
  return QColorTransferGenericFunction::hlgToLinear(x);
}

//  float QColorTransferGenericFunction::pqToLinear(float e)
extern "C" Q_DECL_EXPORT
float ritual_ZN29QColorTransferGenericFunction10pqToLinearEf(float e) {
  return QColorTransferGenericFunction::pqToLinear(e);
}

//  float QColorTransferGenericFunction::pqFromLinear(float fd)
extern "C" Q_DECL_EXPORT
float ritual_ZN29QColorTransferGenericFunction12pqFromLinearEf(float fd) {
  return QColorTransferGenericFunction::pqFromLinear(fd);
}

//  QColorTransferGenericFunction::~QColorTransferGenericFunction()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QColorTransferGenericFunctionD1Ev(
    QColorTransferGenericFunction *self) {
  delete self;
}
