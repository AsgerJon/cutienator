//  Written by hand on 2026-11-25 from
//  QtBluetooth/6.12.0/QtBluetooth/private/btraii_p.h, Qt 6.12.0, from
//  Qt's source. Kept as it is when the generator runs again. Objective-C++:
//  Qt writes these functions only in 'btraii.mm', and Qt's library has no
//  name for them, so their code is copied here, which only a compiler of
//  Objective-C++ on Apple's systems reads; 'summon' builds this file there
//  only. The rituals the generator writes for the class are in
//  'darwin_bluetooth__strong_reference.cpp'.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btraii_p.h>)
#include <QtBluetooth/6.12.0/QtBluetooth/private/btraii_p.h>
#include <Foundation/Foundation.h>
#include <utility>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from qtconnectivity/src/bluetooth/darwin/btraii.mm, lines 16-79
QT_BEGIN_NAMESPACE

namespace DarwinBluetooth {

inline StrongReference::StrongReference(void *object, RetainPolicy policy)
    : objCInstance(object)
{
    if (objCInstance && policy == RetainPolicy::doInitialRetain)
        objCInstance = [getAs<NSObject>() retain];
}

inline StrongReference::StrongReference(const StrongReference &other)
{
    if ((objCInstance = other.getAs<NSObject>()))
        objCInstance = [other.getAs<NSObject>() retain];
}

inline StrongReference::StrongReference(StrongReference &&other)
{
    std::swap(objCInstance, other.objCInstance);
}

inline StrongReference::~StrongReference()
{
    [getAs<NSObject>() release];
}

inline StrongReference &StrongReference::operator = (const StrongReference &other) noexcept
{
    if (this != &other) {
        [getAs<NSObject>() release];
        objCInstance = [other.getAs<NSObject>() retain];
    }

    return *this;
}

inline StrongReference &StrongReference::operator = (StrongReference &&other) noexcept
{
    swap(other);

    return *this;
}

inline void *StrongReference::release()
{
    void *released = objCInstance;
    objCInstance = nullptr;

    return released;
}

inline void StrongReference::reset()
{
    [getAs<NSObject>() release];
    objCInstance = nullptr;
}

inline void StrongReference::reset(void *obj, RetainPolicy policy)
{
    [getAs<NSObject>() release];
    objCInstance = obj;

    if (objCInstance && policy == RetainPolicy::doInitialRetain)
        objCInstance = [getAs<NSObject>() retain];
}

} // namespace DarwinBluetooth

QT_END_NAMESPACE
//  ---------------------------------------------------------------------

//  DarwinBluetooth::StrongReference::StrongReference(void *object,
//      RetainPolicy policy)
extern "C" Q_DECL_EXPORT
DarwinBluetooth::StrongReference *ritual_ZN15DarwinBluetooth15StrongReferenceC1EPvNS_12RetainPolicyE(
    void *object,
    int policy) {
  return new DarwinBluetooth::StrongReference(
      object, static_cast<DarwinBluetooth::RetainPolicy>(policy));
}

//  DarwinBluetooth::StrongReference::StrongReference(const
//      StrongReference &other)
extern "C" Q_DECL_EXPORT
DarwinBluetooth::StrongReference *ritual_ZN15DarwinBluetooth15StrongReferenceC1ERKS0_(
    const DarwinBluetooth::StrongReference *other) {
  return new DarwinBluetooth::StrongReference(*other);
}

//  DarwinBluetooth::StrongReference::StrongReference(StrongReference
//      &&other)
extern "C" Q_DECL_EXPORT
DarwinBluetooth::StrongReference *ritual_ZN15DarwinBluetooth15StrongReferenceC1EOS0_(
    DarwinBluetooth::StrongReference *other) {
  return new DarwinBluetooth::StrongReference(std::move(*other));
}

//  DarwinBluetooth::StrongReference::~StrongReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth15StrongReferenceD1Ev(
    DarwinBluetooth::StrongReference *self) {
  delete self;
}

//  StrongReference &DarwinBluetooth::StrongReference::operator=(const
//      StrongReference &other)
extern "C" Q_DECL_EXPORT
DarwinBluetooth::StrongReference *ritual_ZN15DarwinBluetooth15StrongReferenceaSERKS0_(
    DarwinBluetooth::StrongReference *self,
    const DarwinBluetooth::StrongReference *other) {
  return &(*self = *other);
}

//  StrongReference &DarwinBluetooth::StrongReference::operator=(
//      StrongReference &&other)
extern "C" Q_DECL_EXPORT
DarwinBluetooth::StrongReference *ritual_ZN15DarwinBluetooth15StrongReferenceaSEOS0_(
    DarwinBluetooth::StrongReference *self,
    DarwinBluetooth::StrongReference *other) {
  return &(*self = std::move(*other));
}

//  void *DarwinBluetooth::StrongReference::release()
extern "C" Q_DECL_EXPORT
void *ritual_ZN15DarwinBluetooth15StrongReference7releaseEv(
    DarwinBluetooth::StrongReference *self) {
  return self->release();
}

//  void DarwinBluetooth::StrongReference::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth15StrongReference5resetEv(
    DarwinBluetooth::StrongReference *self) {
  self->reset();
}

//  void DarwinBluetooth::StrongReference::reset(void *newInstance,
//      RetainPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth15StrongReference5resetEPvNS_12RetainPolicyE(
    DarwinBluetooth::StrongReference *self,
    void *newInstance,
    int policy) {
  self->reset(newInstance, static_cast<DarwinBluetooth::RetainPolicy>(policy));
}

#endif
