//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcollator_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcollator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QCollatorSortKeyPrivate::QCollatorSortKeyPrivate(CollatorKeyType &&list)
extern "C" Q_DECL_EXPORT
QCollatorSortKeyPrivate *ritual_ZN23QCollatorSortKeyPrivateC1EO10QByteArray(
    CollatorKeyType *list) {
  return new QCollatorSortKeyPrivate(std::move(*list));
}
