//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>

//  QSortFilterProxyModelDataChanged::QSortFilterProxyModelDataChanged(const
//      QModelIndex &tl, const QModelIndex &br)
extern "C" Q_DECL_EXPORT
QSortFilterProxyModelDataChanged *ritual_ZN32QSortFilterProxyModelDataChangedC1ERK11QModelIndexS2_(
    const QModelIndex *tl,
    const QModelIndex *br) {
  return new QSortFilterProxyModelDataChanged(*tl, *br);
}

//  QSortFilterProxyModelDataChanged::~QSortFilterProxyModelDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSortFilterProxyModelDataChangedD1Ev(
    QSortFilterProxyModelDataChanged *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
