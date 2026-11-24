//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstandarditemmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(standarditemmodel)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstandarditemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  QStandardItemData::QStandardItemData()
extern "C" Q_DECL_EXPORT
QStandardItemData *ritual_ZN17QStandardItemDataC1Ev() {
  return new QStandardItemData();
}

//  QStandardItemData::QStandardItemData(int r, const QVariant &v)
extern "C" Q_DECL_EXPORT
QStandardItemData *ritual_ZN17QStandardItemDataC1EiRK8QVariant(
    int r,
    const QVariant *v) {
  return new QStandardItemData(r, *v);
}

//  bool QStandardItemData::operator==(const QStandardItemData &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QStandardItemDataeqERKS_(
    const QStandardItemData *self,
    const QStandardItemData *other) {
  return self->operator==(*other);
}

//  QStandardItemData::~QStandardItemData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QStandardItemDataD1Ev(QStandardItemData *self) {
  delete self;
}

#endif  // QT_CONFIG(standarditemmodel)
