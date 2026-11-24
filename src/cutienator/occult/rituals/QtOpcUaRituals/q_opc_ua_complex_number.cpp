//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuacomplexnumber.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuacomplexnumber.h>
#include <QtCore/qvariant.h>

//  QOpcUaComplexNumber::QOpcUaComplexNumber()
extern "C" Q_DECL_EXPORT
QOpcUaComplexNumber *ritual_ZN19QOpcUaComplexNumberC1Ev() {
  return new QOpcUaComplexNumber();
}

//  QOpcUaComplexNumber::QOpcUaComplexNumber(const QOpcUaComplexNumber &a0)
extern "C" Q_DECL_EXPORT
QOpcUaComplexNumber *ritual_ZN19QOpcUaComplexNumberC1ERKS_(
    const QOpcUaComplexNumber *a0) {
  return new QOpcUaComplexNumber(*a0);
}

//  QOpcUaComplexNumber::QOpcUaComplexNumber(float real, float imaginary)
extern "C" Q_DECL_EXPORT
QOpcUaComplexNumber *ritual_ZN19QOpcUaComplexNumberC1Eff(
    float real,
    float imaginary) {
  return new QOpcUaComplexNumber(real, imaginary);
}

//  bool QOpcUaComplexNumber::operator==(const QOpcUaComplexNumber &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QOpcUaComplexNumbereqERKS_(
    const QOpcUaComplexNumber *self,
    const QOpcUaComplexNumber *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaComplexNumber::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QOpcUaComplexNumbercv8QVariantEv(
    const QOpcUaComplexNumber *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaComplexNumber::~QOpcUaComplexNumber()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaComplexNumberD1Ev(QOpcUaComplexNumber *self) {
  delete self;
}

//  float QOpcUaComplexNumber::real() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QOpcUaComplexNumber4realEv(
    const QOpcUaComplexNumber *self) {
  return self->real();
}

//  void QOpcUaComplexNumber::setReal(float real)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaComplexNumber7setRealEf(
    QOpcUaComplexNumber *self,
    float real) {
  self->setReal(real);
}

//  float QOpcUaComplexNumber::imaginary() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QOpcUaComplexNumber9imaginaryEv(
    const QOpcUaComplexNumber *self) {
  return self->imaginary();
}

//  void QOpcUaComplexNumber::setImaginary(float imaginary)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaComplexNumber12setImaginaryEf(
    QOpcUaComplexNumber *self,
    float imaginary) {
  self->setImaginary(imaginary);
}
