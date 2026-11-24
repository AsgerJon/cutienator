//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaxvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaxvalue.h>
#include <QtCore/qvariant.h>

//  QOpcUaXValue::QOpcUaXValue()
extern "C" Q_DECL_EXPORT
QOpcUaXValue *ritual_ZN12QOpcUaXValueC1Ev() {
  return new QOpcUaXValue();
}

//  QOpcUaXValue::QOpcUaXValue(const QOpcUaXValue &a0)
extern "C" Q_DECL_EXPORT
QOpcUaXValue *ritual_ZN12QOpcUaXValueC1ERKS_(const QOpcUaXValue *a0) {
  return new QOpcUaXValue(*a0);
}

//  QOpcUaXValue::QOpcUaXValue(double x, float value)
extern "C" Q_DECL_EXPORT
QOpcUaXValue *ritual_ZN12QOpcUaXValueC1Edf(double x, float value) {
  return new QOpcUaXValue(x, value);
}

//  bool QOpcUaXValue::operator==(const QOpcUaXValue &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QOpcUaXValueeqERKS_(
    const QOpcUaXValue *self,
    const QOpcUaXValue *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaXValue::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QOpcUaXValuecv8QVariantEv(const QOpcUaXValue *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaXValue::~QOpcUaXValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaXValueD1Ev(QOpcUaXValue *self) {
  delete self;
}

//  double QOpcUaXValue::x() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12QOpcUaXValue1xEv(const QOpcUaXValue *self) {
  return self->x();
}

//  void QOpcUaXValue::setX(double x)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaXValue4setXEd(QOpcUaXValue *self, double x) {
  self->setX(x);
}

//  float QOpcUaXValue::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QOpcUaXValue5valueEv(const QOpcUaXValue *self) {
  return self->value();
}

//  void QOpcUaXValue::setValue(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpcUaXValue8setValueEf(QOpcUaXValue *self, float value) {
  self->setValue(value);
}
