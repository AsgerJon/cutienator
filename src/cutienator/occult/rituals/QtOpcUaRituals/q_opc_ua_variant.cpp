//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuavariant.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuavariant.h>
#include <QtCore/qvariant.h>

//  QOpcUaVariant::QOpcUaVariant()
extern "C" Q_DECL_EXPORT
QOpcUaVariant *ritual_ZN13QOpcUaVariantC1Ev() {
  return new QOpcUaVariant();
}

//  QOpcUaVariant::QOpcUaVariant(ValueType type, const QVariant &value)
extern "C" Q_DECL_EXPORT
QOpcUaVariant *ritual_ZN13QOpcUaVariantC1ENS_9ValueTypeERK8QVariant(
    QOpcUaVariant::ValueType type,
    const QVariant *value) {
  return new QOpcUaVariant(type, *value);
}

//  QOpcUaVariant::QOpcUaVariant(const QOpcUaVariant &other)
extern "C" Q_DECL_EXPORT
QOpcUaVariant *ritual_ZN13QOpcUaVariantC1ERKS_(const QOpcUaVariant *other) {
  return new QOpcUaVariant(*other);
}

//  QOpcUaVariant::~QOpcUaVariant()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaVariantD1Ev(QOpcUaVariant *self) {
  delete self;
}

//  QVariant QOpcUaVariant::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QOpcUaVariant5valueEv(const QOpcUaVariant *self) {
  return new QVariant(self->value());
}

//  void QOpcUaVariant::setValue(ValueType type, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaVariant8setValueENS_9ValueTypeERK8QVariant(
    QOpcUaVariant *self,
    QOpcUaVariant::ValueType type,
    const QVariant *value) {
  self->setValue(type, *value);
}

//  ValueType QOpcUaVariant::type() const
extern "C" Q_DECL_EXPORT
QOpcUaVariant::ValueType ritual_ZNK13QOpcUaVariant4typeEv(
    const QOpcUaVariant *self) {
  return self->type();
}

//  bool QOpcUaVariant::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QOpcUaVariant7isArrayEv(const QOpcUaVariant *self) {
  return self->isArray();
}

//  QVariant QOpcUaVariant::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QOpcUaVariantcv8QVariantEv(const QOpcUaVariant *self) {
  return new QVariant(self->operator QVariant());
}

//  bool operator==(const QOpcUaVariant &lhs, const QOpcUaVariant &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QOpcUaVariantS1_(
    const QOpcUaVariant *lhs,
    const QOpcUaVariant *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaVariant &lhs, const QOpcUaVariant &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QOpcUaVariantS1_(
    const QOpcUaVariant *lhs,
    const QOpcUaVariant *rhs) {
  return operator!=(*lhs, *rhs);
}
