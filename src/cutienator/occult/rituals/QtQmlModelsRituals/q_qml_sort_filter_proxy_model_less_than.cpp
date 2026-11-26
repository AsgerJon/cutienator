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
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif

//  QQmlSortFilterProxyModelLessThan::QQmlSortFilterProxyModelLessThan(int
//      column, const QModelIndex &parent, const QAbstractItemModel *source,
//      const QSortFilterProxyModelHelper *helper)
extern "C" Q_DECL_EXPORT
QQmlSortFilterProxyModelLessThan *ritual_ZN32QQmlSortFilterProxyModelLessThanC1EiRK11QModelIndexPK18QAbstractItemModelPK27QSortFilterProxyModelHelper(
    int column,
    const QModelIndex *parent,
    const QAbstractItemModel *source,
    const QSortFilterProxyModelHelper *helper) {
  return new QQmlSortFilterProxyModelLessThan(
      column,
      *parent,
      source,
      helper);
}

//  bool QQmlSortFilterProxyModelLessThan::operator()(int r1, int r2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQmlSortFilterProxyModelLessThanclEii(
    const QQmlSortFilterProxyModelLessThan *self,
    int r1,
    int r2) {
  return self->operator()(r1, r2);
}

//  QQmlSortFilterProxyModelLessThan::~QQmlSortFilterProxyModelLessThan()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQmlSortFilterProxyModelLessThanD1Ev(
    QQmlSortFilterProxyModelLessThan *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
