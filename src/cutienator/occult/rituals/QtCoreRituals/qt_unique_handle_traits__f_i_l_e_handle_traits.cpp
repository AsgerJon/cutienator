//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/quniquehandle_types_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/quniquehandle_types_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Type QtUniqueHandleTraits::FILEHandleTraits::invalidValue()
extern "C" Q_DECL_EXPORT
QtUniqueHandleTraits::FILEHandleTraits::Type ritual_ZN20QtUniqueHandleTraits16FILEHandleTraits12invalidValueEv() {
  return QtUniqueHandleTraits::FILEHandleTraits::invalidValue();
}

//  bool QtUniqueHandleTraits::FILEHandleTraits::close(Type handle)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QtUniqueHandleTraits16FILEHandleTraits5closeEP8_IO_FILE(
    QtUniqueHandleTraits::FILEHandleTraits::Type handle) {
  return QtUniqueHandleTraits::FILEHandleTraits::close(handle);
}

//  QtUniqueHandleTraits::FILEHandleTraits::~FILEHandleTraits()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QtUniqueHandleTraits16FILEHandleTraitsD1Ev(
    QtUniqueHandleTraits::FILEHandleTraits *self) {
  delete self;
}
