//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcollator_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcollator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlocale.h>
#include <QtCore/qcollator.h>

//  QCollatorPrivate::QCollatorPrivate(const QLocale &locale)
extern "C" Q_DECL_EXPORT
QCollatorPrivate *ritual_ZN16QCollatorPrivateC1ERK7QLocale(
    const QLocale *locale) {
  return new QCollatorPrivate(*locale);
}

//  bool QCollatorPrivate::isC() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCollatorPrivate3isCEv(const QCollatorPrivate *self) {
  return self->isC();
}

//  QCollatorSortKey QCollatorPrivate::sortKeyFromData(CollatorKeyType
//      &&data)
extern "C" Q_DECL_EXPORT
QCollatorSortKey *ritual_ZN16QCollatorPrivate15sortKeyFromDataEO10QByteArray(
    CollatorKeyType *data) {
  return new QCollatorSortKey(
      QCollatorPrivate::sortKeyFromData(
          std::move(*data)));
}
