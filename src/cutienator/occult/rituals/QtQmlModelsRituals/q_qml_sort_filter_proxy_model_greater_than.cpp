//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>

//  QQmlSortFilterProxyModelGreaterThan::QQmlSortFilterProxyModelGreaterThan(
//      int column, const QModelIndex &parent, const QAbstractItemModel
//      *source, const QSortFilterProxyModelHelper *helper)
extern "C" Q_DECL_EXPORT
QQmlSortFilterProxyModelGreaterThan *ritual_ZN35QQmlSortFilterProxyModelGreaterThanC1EiRK11QModelIndexPK18QAbstractItemModelPK27QSortFilterProxyModelHelper(
    int column,
    const QModelIndex *parent,
    const QAbstractItemModel *source,
    const QSortFilterProxyModelHelper *helper) {
  return new QQmlSortFilterProxyModelGreaterThan(
      column,
      *parent,
      source,
      helper);
}

//  bool QQmlSortFilterProxyModelGreaterThan::operator()(int r1, int r2)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QQmlSortFilterProxyModelGreaterThanclEii(
    const QQmlSortFilterProxyModelGreaterThan *self,
    int r1,
    int r2) {
  return self->operator()(r1, r2);
}

//  QQmlSortFilterProxyModelGreaterThan::~QQmlSortFilterProxyModelGreaterThan
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QQmlSortFilterProxyModelGreaterThanD1Ev(
    QQmlSortFilterProxyModelGreaterThan *self) {
  delete self;
}
