//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QBindingObserverPtr::QBindingObserverPtr()
extern "C" Q_DECL_EXPORT
QBindingObserverPtr *ritual_ZN19QBindingObserverPtrC1Ev() {
  return new QBindingObserverPtr();
}

//  void QBindingObserverPtr::swap(QBindingObserverPtr &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBindingObserverPtr4swapERS_(
    QBindingObserverPtr *self,
    QBindingObserverPtr *other) {
  self->swap(*other);
}

//  QBindingObserverPtr::QBindingObserverPtr(QBindingObserverPtr &&other)
extern "C" Q_DECL_EXPORT
QBindingObserverPtr *ritual_ZN19QBindingObserverPtrC1EOS_(
    QBindingObserverPtr *other) {
  return new QBindingObserverPtr(std::move(*other));
}

//  QBindingObserverPtr &QBindingObserverPtr::operator=(QBindingObserverPtr
//      &&other)
extern "C" Q_DECL_EXPORT
QBindingObserverPtr *ritual_ZN19QBindingObserverPtraSEOS_(
    QBindingObserverPtr *self,
    QBindingObserverPtr *other) {
  return &(self->operator=(std::move(*other)));
}

//  QBindingObserverPtr::QBindingObserverPtr(QPropertyObserver *observer)
extern "C" Q_DECL_EXPORT
QBindingObserverPtr *ritual_ZN19QBindingObserverPtrC1EP17QPropertyObserver(
    QPropertyObserver *observer) {
  return new QBindingObserverPtr(observer);
}

//  QBindingObserverPtr::~QBindingObserverPtr()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBindingObserverPtrD1Ev(QBindingObserverPtr *self) {
  delete self;
}

//  QPropertyBindingPrivate *QBindingObserverPtr::binding() const
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivate *ritual_ZNK19QBindingObserverPtr7bindingEv(
    const QBindingObserverPtr *self) {
  return self->binding();
}

//  QPropertyObserver *QBindingObserverPtr::operator->()
extern "C" Q_DECL_EXPORT
QPropertyObserver *ritual_ZN19QBindingObserverPtrptEv(
    QBindingObserverPtr *self) {
  return self->operator->();
}
