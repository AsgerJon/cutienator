//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtPrivate::ModelIndex::ModelIndex()
extern "C" Q_DECL_EXPORT
QtPrivate::ModelIndex *ritual_ZN9QtPrivate10ModelIndexC1Ev() {
  return new QtPrivate::ModelIndex();
}

//  QtPrivate::ModelIndex::ModelIndex(int row_, int column_)
extern "C" Q_DECL_EXPORT
QtPrivate::ModelIndex *ritual_ZN9QtPrivate10ModelIndexC1Eii(
    int row_,
    int column_) {
  return new QtPrivate::ModelIndex(row_, column_);
}

//  bool QtPrivate::ModelIndex::operator==(const ModelIndex &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate10ModelIndexeqERKS0_(
    const QtPrivate::ModelIndex *self,
    const QtPrivate::ModelIndex *other) {
  return self->operator==(*other);
}

//  bool QtPrivate::ModelIndex::operator!=(const ModelIndex &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate10ModelIndexneERKS0_(
    const QtPrivate::ModelIndex *self,
    const QtPrivate::ModelIndex *other) {
  return self->operator!=(*other);
}

//  QtPrivate::ModelIndex::~ModelIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate10ModelIndexD1Ev(QtPrivate::ModelIndex *self) {
  delete self;
}
