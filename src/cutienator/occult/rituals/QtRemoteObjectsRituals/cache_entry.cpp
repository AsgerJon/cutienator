//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  CacheEntry::CacheEntry()
extern "C" Q_DECL_EXPORT
CacheEntry *ritual_ZN10CacheEntryC1Ev() {
  return new CacheEntry();
}

//  CacheEntry::~CacheEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10CacheEntryD1Ev(CacheEntry *self) {
  delete self;
}
