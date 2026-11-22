//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qvariant.h>

//  QAccessibleValueChangeEvent::QAccessibleValueChangeEvent(QObject *obj,
//      const QVariant &val)
extern "C" Q_DECL_EXPORT
QAccessibleValueChangeEvent *ritual_ZN27QAccessibleValueChangeEventC1EP7QObjectRK8QVariant(
    QObject *obj,
    const QVariant *val) {
  return new QAccessibleValueChangeEvent(obj, *val);
}

//  QAccessibleValueChangeEvent::QAccessibleValueChangeEvent(QAccessibleInter
//      face *iface, const QVariant &val)
extern "C" Q_DECL_EXPORT
QAccessibleValueChangeEvent *ritual_ZN27QAccessibleValueChangeEventC1EP20QAccessibleInterfaceRK8QVariant(
    QAccessibleInterface *iface,
    const QVariant *val) {
  return new QAccessibleValueChangeEvent(iface, *val);
}

//  QAccessibleValueChangeEvent::~QAccessibleValueChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAccessibleValueChangeEventD1Ev(
    QAccessibleValueChangeEvent *self) {
  delete self;
}

//  void QAccessibleValueChangeEvent::setValue(const QVariant &val)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAccessibleValueChangeEvent8setValueERK8QVariant(
    QAccessibleValueChangeEvent *self,
    const QVariant *val) {
  self->setValue(*val);
}

//  QVariant QAccessibleValueChangeEvent::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QAccessibleValueChangeEvent5valueEv(
    const QAccessibleValueChangeEvent *self) {
  return new QVariant(self->value());
}
