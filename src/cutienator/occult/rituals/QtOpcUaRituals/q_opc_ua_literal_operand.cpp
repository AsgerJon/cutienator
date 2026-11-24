//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcualiteraloperand.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcualiteraloperand.h>
#include <QtCore/qvariant.h>

//  QOpcUaLiteralOperand::QOpcUaLiteralOperand()
extern "C" Q_DECL_EXPORT
QOpcUaLiteralOperand *ritual_ZN20QOpcUaLiteralOperandC1Ev() {
  return new QOpcUaLiteralOperand();
}

//  QOpcUaLiteralOperand::QOpcUaLiteralOperand(const QOpcUaLiteralOperand
//      &a0)
extern "C" Q_DECL_EXPORT
QOpcUaLiteralOperand *ritual_ZN20QOpcUaLiteralOperandC1ERKS_(
    const QOpcUaLiteralOperand *a0) {
  return new QOpcUaLiteralOperand(*a0);
}

//  QOpcUaLiteralOperand::QOpcUaLiteralOperand(const QVariant &value,
//      QOpcUa::Types type)
extern "C" Q_DECL_EXPORT
QOpcUaLiteralOperand *ritual_ZN20QOpcUaLiteralOperandC1ERK8QVariantN6QOpcUa5TypesE(
    const QVariant *value,
    QOpcUa::Types type) {
  return new QOpcUaLiteralOperand(*value, type);
}

//  QVariant QOpcUaLiteralOperand::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QOpcUaLiteralOperandcv8QVariantEv(
    const QOpcUaLiteralOperand *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaLiteralOperand::~QOpcUaLiteralOperand()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaLiteralOperandD1Ev(QOpcUaLiteralOperand *self) {
  delete self;
}

//  QVariant QOpcUaLiteralOperand::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QOpcUaLiteralOperand5valueEv(
    const QOpcUaLiteralOperand *self) {
  return new QVariant(self->value());
}

//  void QOpcUaLiteralOperand::setValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaLiteralOperand8setValueERK8QVariant(
    QOpcUaLiteralOperand *self,
    const QVariant *value) {
  self->setValue(*value);
}

//  QOpcUa::Types QOpcUaLiteralOperand::type() const
extern "C" Q_DECL_EXPORT
QOpcUa::Types ritual_ZNK20QOpcUaLiteralOperand4typeEv(
    const QOpcUaLiteralOperand *self) {
  return self->type();
}

//  void QOpcUaLiteralOperand::setType(QOpcUa::Types type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaLiteralOperand7setTypeEN6QOpcUa5TypesE(
    QOpcUaLiteralOperand *self,
    QOpcUa::Types type) {
  self->setType(type);
}

//  bool operator==(const QOpcUaLiteralOperand &lhs, const
//      QOpcUaLiteralOperand &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QOpcUaLiteralOperandS1_(
    const QOpcUaLiteralOperand *lhs,
    const QOpcUaLiteralOperand *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaLiteralOperand &lhs, const
//      QOpcUaLiteralOperand &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QOpcUaLiteralOperandS1_(
    const QOpcUaLiteralOperand *lhs,
    const QOpcUaLiteralOperand *rhs) {
  return operator!=(*lhs, *rhs);
}
