//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/qcollator.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qsize.h>
#include <QtCore/qmimedata.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#if QT_CONFIG(regularexpression)
#  include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qstack.h>
#include <QtCore/qmap.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qloggingcategory.h>
#include <functional>
#include <limits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/itemmodels/qabstractitemmodel.cpp, line 35, as _ZN25QPersistentModelIndexData6createERK11QModelIndex
inline QPersistentModelIndexData *QPersistentModelIndexData::create(const QModelIndex &index)
{
    Q_ASSERT(index.isValid()); // we will _never_ insert an invalid index in the list
    QPersistentModelIndexData *d = nullptr;
    QAbstractItemModel *model = const_cast<QAbstractItemModel *>(index.model());
    QMultiHash<QtPrivate::QModelIndexWrapper, QPersistentModelIndexData *> &indexes = model->d_func()->persistent.indexes;
    const auto it = indexes.constFind(index);
    if (it != indexes.cend()) {
        d = (*it);
    } else {
        d = new QPersistentModelIndexData(index);
        indexes.insert(index, d);
    }
    Q_ASSERT(d);
    return d;
}

//  from src/corelib/itemmodels/qabstractitemmodel.cpp, line 52, as _ZN25QPersistentModelIndexData7destroyEPS_
inline void QPersistentModelIndexData::destroy(QPersistentModelIndexData *data)
{
    Q_ASSERT(data);
    Q_ASSERT(data->ref.loadRelaxed() == 0);
    QAbstractItemModel *model = const_cast<QAbstractItemModel *>(data->index.model());
    // a valid persistent model index with a null model pointer can only happen if the model was destroyed
    if (model) {
        QAbstractItemModelPrivate *p = model->d_func();
        Q_ASSERT(p);
        p->removePersistentIndexData(data);
    }
    delete data;
}
//  -----------------------------------------------------------------------

//  QPersistentModelIndexData::QPersistentModelIndexData()
extern "C" Q_DECL_EXPORT
QPersistentModelIndexData *ritual_ZN25QPersistentModelIndexDataC1Ev() {
  return new QPersistentModelIndexData();
}

//  QPersistentModelIndexData::QPersistentModelIndexData(const QModelIndex
//      &idx)
extern "C" Q_DECL_EXPORT
QPersistentModelIndexData *ritual_ZN25QPersistentModelIndexDataC1ERK11QModelIndex(
    const QModelIndex *idx) {
  return new QPersistentModelIndexData(*idx);
}

//  QPersistentModelIndexData *QPersistentModelIndexData::create(const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
QPersistentModelIndexData *ritual_ZN25QPersistentModelIndexData6createERK11QModelIndex(
    const QModelIndex *index) {
  return QPersistentModelIndexData::create(*index);
}

//  void QPersistentModelIndexData::destroy(QPersistentModelIndexData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPersistentModelIndexData7destroyEPS_(
    QPersistentModelIndexData *data) {
  QPersistentModelIndexData::destroy(data);
}

//  QPersistentModelIndexData::~QPersistentModelIndexData()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPersistentModelIndexDataD1Ev(
    QPersistentModelIndexData *self) {
  delete self;
}

//  QList<QPersistentModelIndexData *>::QList()
extern "C" Q_DECL_EXPORT
QList<QPersistentModelIndexData *> *ritual_list_make_QPersistentModelIndexData_ptr() {
  return new QList<QPersistentModelIndexData *>();
}

//  void QList<QPersistentModelIndexData *>::append(const
//      QPersistentModelIndexData * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPersistentModelIndexData_ptr(
    QList<QPersistentModelIndexData *> *self,
    QPersistentModelIndexData *element) {
  self->append(element);
}

//  qsizetype QList<QPersistentModelIndexData *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPersistentModelIndexData_ptr(
    const QList<QPersistentModelIndexData *> *self) {
  return self->size();
}

//  const QPersistentModelIndexData * &QList<QPersistentModelIndexData
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPersistentModelIndexData *ritual_list_at_QPersistentModelIndexData_ptr(
    const QList<QPersistentModelIndexData *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QPersistentModelIndexData *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPersistentModelIndexData_ptr(
    QList<QPersistentModelIndexData *> *self) {
  delete self;
}

#endif  // QT_CONFIG(itemmodel)
#endif  // QT_CONFIG(itemmodel)
