//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>

//  QAbstractItemModelPrivate::Change::Change()
extern "C" Q_DECL_EXPORT
QAbstractItemModelPrivate::Change *ritual_ZN25QAbstractItemModelPrivate6ChangeC1Ev() {
  return new QAbstractItemModelPrivate::Change();
}

//  QAbstractItemModelPrivate::Change::Change(const QModelIndex &p, int f,
//      int l)
extern "C" Q_DECL_EXPORT
QAbstractItemModelPrivate::Change *ritual_ZN25QAbstractItemModelPrivate6ChangeC1ERK11QModelIndexii(
    const QModelIndex *p,
    int f,
    int l) {
  return new QAbstractItemModelPrivate::Change(*p, f, l);
}

//  bool QAbstractItemModelPrivate::Change::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAbstractItemModelPrivate6Change7isValidEv(
    const QAbstractItemModelPrivate::Change *self) {
  return self->isValid();
}

//  QAbstractItemModelPrivate::Change::~Change()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate6ChangeD1Ev(
    QAbstractItemModelPrivate::Change *self) {
  delete self;
}

#endif  // QT_CONFIG(itemmodel)
