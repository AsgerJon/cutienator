//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qvariant.h>

//  QAccessibleValueInterface::~QAccessibleValueInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleValueInterfaceD1Ev(
    QAccessibleValueInterface *self) {
  delete self;
}

//  QVariant QAccessibleValueInterface::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleValueInterface12currentValueEv(
    const QAccessibleValueInterface *self) {
  return new QVariant(self->currentValue());
}

//  void QAccessibleValueInterface::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant(
    QAccessibleValueInterface *self,
    const QVariant *value) {
  self->setCurrentValue(*value);
}

//  QVariant QAccessibleValueInterface::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleValueInterface12maximumValueEv(
    const QAccessibleValueInterface *self) {
  return new QVariant(self->maximumValue());
}

//  QVariant QAccessibleValueInterface::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleValueInterface12minimumValueEv(
    const QAccessibleValueInterface *self) {
  return new QVariant(self->minimumValue());
}

//  QVariant QAccessibleValueInterface::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleValueInterface15minimumStepSizeEv(
    const QAccessibleValueInterface *self) {
  return new QVariant(self->minimumStepSize());
}
