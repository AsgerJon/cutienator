//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuavariant.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuavariant.h>
#include <QtCore/qvariant.h>
#include <QtCore/QVariant>
#include <QtCore/QList>

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

//  QOpcUaVariant::QOpcUaVariant(ValueType type, const QVariant &value, const
//      QList<qint32> arrayDimensions)
extern "C" Q_DECL_EXPORT
QOpcUaVariant *ritual_ZN13QOpcUaVariantC1ENS_9ValueTypeERK8QVariant5QListIiE(
    QOpcUaVariant::ValueType type,
    const QVariant *value,
    const QList<qint32> *arrayDimensions) {
  return new QOpcUaVariant(type, *value, *arrayDimensions);
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

//  void QOpcUaVariant::swap(QOpcUaVariant &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaVariant4swapERS_(
    QOpcUaVariant *self,
    QOpcUaVariant *other) {
  self->swap(*other);
}

//  QOpcUaVariant &QOpcUaVariant::operator=(QOpcUaVariant &&other)
extern "C" Q_DECL_EXPORT
QOpcUaVariant *ritual_ZN13QOpcUaVariantaSEOS_(
    QOpcUaVariant *self,
    QOpcUaVariant *other) {
  return &(self->operator=(std::move(*other)));
}

//  QOpcUaVariant::QOpcUaVariant(QOpcUaVariant &&other)
extern "C" Q_DECL_EXPORT
QOpcUaVariant *ritual_ZN13QOpcUaVariantC1EOS_(QOpcUaVariant *other) {
  return new QOpcUaVariant(std::move(*other));
}

//  QOpcUaVariant &QOpcUaVariant::operator=(const QOpcUaVariant &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaVariant *ritual_ZN13QOpcUaVariantaSERKS_(
    QOpcUaVariant *self,
    const QOpcUaVariant *rhs) {
  return &(self->operator=(*rhs));
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

//  void QOpcUaVariant::setValue(ValueType type, const QVariant &value, const
//      QList<qint32> &arrayDimensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaVariant8setValueENS_9ValueTypeERK8QVariantRK5QListIiE(
    QOpcUaVariant *self,
    QOpcUaVariant::ValueType type,
    const QVariant *value,
    const QList<qint32> *arrayDimensions) {
  self->setValue(type, *value, *arrayDimensions);
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

//  QList<qint32> QOpcUaVariant::arrayDimensions() const
extern "C" Q_DECL_EXPORT
QList<qint32> *ritual_ZNK13QOpcUaVariant15arrayDimensionsEv(
    const QOpcUaVariant *self) {
  return new QList<qint32>(self->arrayDimensions());
}

//  void QOpcUaVariant::setArrayDimensions(const QList<qint32>
//      &arrayDimensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaVariant18setArrayDimensionsERK5QListIiE(
    QOpcUaVariant *self,
    const QList<qint32> *arrayDimensions) {
  self->setArrayDimensions(*arrayDimensions);
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

//  a QList<qint32> a ritual of QOpcUaVariant gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpcUaVariant__QList_qint32(QList<qint32> *self) {
  delete self;
}
