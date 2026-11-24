//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaelementoperand.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaelementoperand.h>
#include <QtCore/qvariant.h>

//  QOpcUaElementOperand::QOpcUaElementOperand()
extern "C" Q_DECL_EXPORT
QOpcUaElementOperand *ritual_ZN20QOpcUaElementOperandC1Ev() {
  return new QOpcUaElementOperand();
}

//  QOpcUaElementOperand::QOpcUaElementOperand(const QOpcUaElementOperand
//      &a0)
extern "C" Q_DECL_EXPORT
QOpcUaElementOperand *ritual_ZN20QOpcUaElementOperandC1ERKS_(
    const QOpcUaElementOperand *a0) {
  return new QOpcUaElementOperand(*a0);
}

//  QOpcUaElementOperand::QOpcUaElementOperand(quint32 index)
extern "C" Q_DECL_EXPORT
QOpcUaElementOperand *ritual_ZN20QOpcUaElementOperandC1Ej(quint32 index) {
  return new QOpcUaElementOperand(index);
}

//  QVariant QOpcUaElementOperand::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QOpcUaElementOperandcv8QVariantEv(
    const QOpcUaElementOperand *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaElementOperand::~QOpcUaElementOperand()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaElementOperandD1Ev(QOpcUaElementOperand *self) {
  delete self;
}

//  quint32 QOpcUaElementOperand::index() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK20QOpcUaElementOperand5indexEv(
    const QOpcUaElementOperand *self) {
  return self->index();
}

//  void QOpcUaElementOperand::setIndex(quint32 index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaElementOperand8setIndexEj(
    QOpcUaElementOperand *self,
    quint32 index) {
  self->setIndex(index);
}

//  bool operator==(const QOpcUaElementOperand &lhs, const
//      QOpcUaElementOperand &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QOpcUaElementOperandS1_(
    const QOpcUaElementOperand *lhs,
    const QOpcUaElementOperand *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaElementOperand &lhs, const
//      QOpcUaElementOperand &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QOpcUaElementOperandS1_(
    const QOpcUaElementOperand *lhs,
    const QOpcUaElementOperand *rhs) {
  return operator!=(*lhs, *rhs);
}
