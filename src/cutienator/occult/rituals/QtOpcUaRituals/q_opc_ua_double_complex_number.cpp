//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuadoublecomplexnumber.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuadoublecomplexnumber.h>
#include <QtCore/qvariant.h>

//  QOpcUaDoubleComplexNumber::QOpcUaDoubleComplexNumber()
extern "C" Q_DECL_EXPORT
QOpcUaDoubleComplexNumber *ritual_ZN25QOpcUaDoubleComplexNumberC1Ev() {
  return new QOpcUaDoubleComplexNumber();
}

//  QOpcUaDoubleComplexNumber::QOpcUaDoubleComplexNumber(const
//      QOpcUaDoubleComplexNumber &a0)
extern "C" Q_DECL_EXPORT
QOpcUaDoubleComplexNumber *ritual_ZN25QOpcUaDoubleComplexNumberC1ERKS_(
    const QOpcUaDoubleComplexNumber *a0) {
  return new QOpcUaDoubleComplexNumber(*a0);
}

//  QOpcUaDoubleComplexNumber::QOpcUaDoubleComplexNumber(double real, double
//      imaginary)
extern "C" Q_DECL_EXPORT
QOpcUaDoubleComplexNumber *ritual_ZN25QOpcUaDoubleComplexNumberC1Edd(
    double real,
    double imaginary) {
  return new QOpcUaDoubleComplexNumber(real, imaginary);
}

//  bool QOpcUaDoubleComplexNumber::operator==(const
//      QOpcUaDoubleComplexNumber &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QOpcUaDoubleComplexNumbereqERKS_(
    const QOpcUaDoubleComplexNumber *self,
    const QOpcUaDoubleComplexNumber *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaDoubleComplexNumber::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QOpcUaDoubleComplexNumbercv8QVariantEv(
    const QOpcUaDoubleComplexNumber *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaDoubleComplexNumber::~QOpcUaDoubleComplexNumber()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaDoubleComplexNumberD1Ev(
    QOpcUaDoubleComplexNumber *self) {
  delete self;
}

//  double QOpcUaDoubleComplexNumber::real() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK25QOpcUaDoubleComplexNumber4realEv(
    const QOpcUaDoubleComplexNumber *self) {
  return self->real();
}

//  void QOpcUaDoubleComplexNumber::setReal(double real)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaDoubleComplexNumber7setRealEd(
    QOpcUaDoubleComplexNumber *self,
    double real) {
  self->setReal(real);
}

//  double QOpcUaDoubleComplexNumber::imaginary() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK25QOpcUaDoubleComplexNumber9imaginaryEv(
    const QOpcUaDoubleComplexNumber *self) {
  return self->imaginary();
}

//  void QOpcUaDoubleComplexNumber::setImaginary(double imaginary)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaDoubleComplexNumber12setImaginaryEd(
    QOpcUaDoubleComplexNumber *self,
    double imaginary) {
  self->setImaginary(imaginary);
}
