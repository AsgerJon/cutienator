//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/btraii_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  1. Kept as it is when the generator runs again.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btraii_p.h>)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/btraii_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  DarwinBluetooth::StrongReference::StrongReference()
extern "C" Q_DECL_EXPORT
DarwinBluetooth::StrongReference *ritual_ZN15DarwinBluetooth15StrongReferenceC1Ev() {
  return new DarwinBluetooth::StrongReference();
}

//  void DarwinBluetooth::StrongReference::swap(StrongReference &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth15StrongReference4swapERS0_(
    DarwinBluetooth::StrongReference *self,
    DarwinBluetooth::StrongReference *other) {
  self->swap(*other);
}

//  bool DarwinBluetooth::StrongReference::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DarwinBluetooth15StrongReferencecvbEv(
    const DarwinBluetooth::StrongReference *self) {
  return self->operator bool();
}

//  void *DarwinBluetooth::StrongReference::getAs<void>() const
extern "C" Q_DECL_EXPORT
void * ritual_ZNK15DarwinBluetooth15StrongReference5getAsIvEEPT_v(
    const DarwinBluetooth::StrongReference *self) {
  return self->getAs<void>();
}

#endif  // __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btraii_p.h>)
