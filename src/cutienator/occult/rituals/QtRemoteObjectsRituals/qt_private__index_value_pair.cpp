//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtCore/QVariant>
#include <QtCore/QSize>

//  QtPrivate::IndexValuePair::IndexValuePair(const IndexList index_, const
//      QVariantList &data_, bool hasChildren_, const Qt::ItemFlags &flags_,
//      const QSize &size_)
extern "C" Q_DECL_EXPORT
QtPrivate::IndexValuePair *ritual_ZN9QtPrivate14IndexValuePairC1E5QListINS_10ModelIndexEERKS1_I8QVariantEbRK6QFlagsIN2Qt8ItemFlagEERK5QSize(
    const QtPrivate::IndexList *index_,
    const QList<QVariant> *data_,
    bool hasChildren_,
    const Qt::ItemFlags *flags_,
    const QSize *size_) {
  return new QtPrivate::IndexValuePair(
      *index_,
      *data_,
      hasChildren_,
      *flags_,
      *size_);
}

//  bool QtPrivate::IndexValuePair::operator==(const IndexValuePair &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate14IndexValuePaireqERKS0_(
    const QtPrivate::IndexValuePair *self,
    const QtPrivate::IndexValuePair *other) {
  return self->operator==(*other);
}

//  bool QtPrivate::IndexValuePair::operator!=(const IndexValuePair &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate14IndexValuePairneERKS0_(
    const QtPrivate::IndexValuePair *self,
    const QtPrivate::IndexValuePair *other) {
  return self->operator!=(*other);
}

//  QtPrivate::IndexValuePair::~IndexValuePair()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate14IndexValuePairD1Ev(
    QtPrivate::IndexValuePair *self) {
  delete self;
}
