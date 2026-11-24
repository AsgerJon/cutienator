//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QtPrivate::DataEntries::operator==(const DataEntries &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate11DataEntrieseqERKS0_(
    const QtPrivate::DataEntries *self,
    const QtPrivate::DataEntries *other) {
  return self->operator==(*other);
}

//  bool QtPrivate::DataEntries::operator!=(const DataEntries &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate11DataEntriesneERKS0_(
    const QtPrivate::DataEntries *self,
    const QtPrivate::DataEntries *other) {
  return self->operator!=(*other);
}

//  QtPrivate::DataEntries::~DataEntries()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate11DataEntriesD1Ev(QtPrivate::DataEntries *self) {
  delete self;
}
