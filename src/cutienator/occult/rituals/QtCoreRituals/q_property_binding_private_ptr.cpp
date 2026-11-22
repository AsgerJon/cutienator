//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpropertyprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpropertyprivate.h>

//  QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr()
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr *ritual_ZN26QPropertyBindingPrivatePtrC1Ev() {
  return new QPropertyBindingPrivatePtr();
}

//  QPropertyBindingPrivatePtr::~QPropertyBindingPrivatePtr()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPropertyBindingPrivatePtrD1Ev(
    QPropertyBindingPrivatePtr *self) {
  delete self;
}

//  void QPropertyBindingPrivatePtr::destroyAndFreeMemory()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPropertyBindingPrivatePtr20destroyAndFreeMemoryEv(
    QPropertyBindingPrivatePtr *self) {
  self->destroyAndFreeMemory();
}

//  QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr(const
//      QPropertyBindingPrivatePtr &o)
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr *ritual_ZN26QPropertyBindingPrivatePtrC1ERKS_(
    const QPropertyBindingPrivatePtr *o) {
  return new QPropertyBindingPrivatePtr(*o);
}

//  bool QPropertyBindingPrivatePtr::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QPropertyBindingPrivatePtrcvbEv(
    const QPropertyBindingPrivatePtr *self) {
  return self->operator bool();
}

//  bool QPropertyBindingPrivatePtr::operator!() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QPropertyBindingPrivatePtrntEv(
    const QPropertyBindingPrivatePtr *self) {
  return self->operator!();
}

//  bool operator==(const QPropertyBindingPrivatePtr &lhs, const
//      QPropertyBindingPrivatePtr &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QPropertyBindingPrivatePtrS1_(
    const QPropertyBindingPrivatePtr *lhs,
    const QPropertyBindingPrivatePtr *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPropertyBindingPrivatePtr &lhs, const
//      QPropertyBindingPrivatePtr &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QPropertyBindingPrivatePtrS1_(
    const QPropertyBindingPrivatePtr *lhs,
    const QPropertyBindingPrivatePtr *rhs) {
  return operator!=(*lhs, *rhs);
}
