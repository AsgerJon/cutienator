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
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
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

//  from src/corelib/itemmodels/qabstractitemmodel.cpp, line 4239, as _ZN25QAbstractItemModelPrivate10Persistent16insertMultiAtEndERK11QModelIndexP25QPersistentModelIndexData
inline void QAbstractItemModelPrivate::Persistent::insertMultiAtEnd(const QModelIndex& key, QPersistentModelIndexData *data)
{
    auto newIt = indexes.insert(key, data);
    auto it = newIt;
    ++it;
    while (it != indexes.end() && it.key() == key) {
        qSwap(*newIt,*it);
        newIt = it;
        ++it;
    }
}
//  -----------------------------------------------------------------------

//  QAbstractItemModelPrivate::Persistent::Persistent()
extern "C" Q_DECL_EXPORT
QAbstractItemModelPrivate::Persistent *ritual_ZN25QAbstractItemModelPrivate10PersistentC1Ev() {
  return new QAbstractItemModelPrivate::Persistent();
}

//  void QAbstractItemModelPrivate::Persistent::insertMultiAtEnd(const
//      QModelIndex &key, QPersistentModelIndexData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate10Persistent16insertMultiAtEndERK11QModelIndexP25QPersistentModelIndexData(
    QAbstractItemModelPrivate::Persistent *self,
    const QModelIndex *key,
    QPersistentModelIndexData *data) {
  self->insertMultiAtEnd(*key, data);
}

//  QAbstractItemModelPrivate::Persistent::~Persistent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate10PersistentD1Ev(
    QAbstractItemModelPrivate::Persistent *self) {
  delete self;
}

#endif  // QT_CONFIG(itemmodel)
#endif  // QT_CONFIG(itemmodel)
