//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>

//  QRowsRemoval::QRowsRemoval(const QModelIndex &parent_source, int start,
//      int end)
extern "C" Q_DECL_EXPORT
QRowsRemoval *ritual_ZN12QRowsRemovalC1ERK11QModelIndexii(
    const QModelIndex *parent_source,
    int start,
    int end) {
  return new QRowsRemoval(*parent_source, start, end);
}

//  QRowsRemoval::QRowsRemoval()
extern "C" Q_DECL_EXPORT
QRowsRemoval *ritual_ZN12QRowsRemovalC1Ev() {
  return new QRowsRemoval();
}

//  bool QRowsRemoval::contains(QModelIndex parent, int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QRowsRemoval8containsE11QModelIndexi(
    const QRowsRemoval *self,
    const QModelIndex *parent,
    int row) {
  return self->contains(*parent, row);
}

//  QRowsRemoval::~QRowsRemoval()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRowsRemovalD1Ev(QRowsRemoval *self) {
  delete self;
}
