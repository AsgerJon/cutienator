//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstandarditemmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(standarditemmodel)
#if QT_CONFIG(standarditemmodel)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstandarditemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qstandarditemmodel.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qmimedata.h>
#include <QtCore/qiodevice.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtGui/private/qstandarditemmodel_p.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 356, as _ZN20QStandardItemPrivate8setModelEP18QStandardItemModel
inline void QStandardItemPrivate::setModel(QStandardItemModel *mod)
{
    if (children.isEmpty()) {
        if (model)
            model->d_func()->invalidatePersistentIndex(model->indexFromItem(q_ptr));
        model = mod;
    } else {
        QStack<QStandardItem*> stack;
        stack.push(q_ptr);
        while (!stack.isEmpty()) {
            QStandardItem *itm = stack.pop();
            if (itm->d_func()->model) {
                itm->d_func()->model->d_func()->invalidatePersistentIndex(itm->d_func()->model->indexFromItem(itm));
            }
            itm->d_func()->model = mod;
            const QList<QStandardItem*> &childList = itm->d_func()->children;
            for (int i = 0; i < childList.size(); ++i) {
                QStandardItem *chi = childList.at(i);
                if (chi)
                    stack.push(chi);
            }
        }
    }
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 384, as _ZN25QStandardItemModelPrivateC1Ev
inline QStandardItemModelPrivate::QStandardItemModelPrivate()
    : root(new QStandardItem), itemPrototype(nullptr)
{
    root->setFlags(Qt::ItemIsDropEnabled);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 393, as _ZN25QStandardItemModelPrivateD1Ev
inline QStandardItemModelPrivate::~QStandardItemModelPrivate()
{
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 400, as _ZN25QStandardItemModelPrivate4initEv
inline void QStandardItemModelPrivate::init()
{
    Q_Q(QStandardItemModel);
    QObject::connect(q, SIGNAL(dataChanged(QModelIndex,QModelIndex)),
                     q, SLOT(_q_emitItemChanged(QModelIndex,QModelIndex)));
    roleNames = QAbstractItemModelPrivate::defaultRoleNames();
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 575, as _ZN25QStandardItemModelPrivate21rowsAboutToBeInsertedEP13QStandardItemii
inline void QStandardItemModelPrivate::rowsAboutToBeInserted(QStandardItem *parent,
                                                      int start, int end)
{
    Q_Q(QStandardItemModel);
    QModelIndex index = q->indexFromItem(parent);
    q->beginInsertRows(index, start, end);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 586, as _ZN25QStandardItemModelPrivate24columnsAboutToBeInsertedEP13QStandardItemii
inline void QStandardItemModelPrivate::columnsAboutToBeInserted(QStandardItem *parent,
                                                         int start, int end)
{
    Q_Q(QStandardItemModel);
    QModelIndex index = q->indexFromItem(parent);
    q->beginInsertColumns(index, start, end);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 597, as _ZN25QStandardItemModelPrivate20rowsAboutToBeRemovedEP13QStandardItemii
inline void QStandardItemModelPrivate::rowsAboutToBeRemoved(QStandardItem *parent,
                                                     int start, int end)
{
    Q_Q(QStandardItemModel);
    QModelIndex index = q->indexFromItem(parent);
    q->beginRemoveRows(index, start, end);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 608, as _ZN25QStandardItemModelPrivate23columnsAboutToBeRemovedEP13QStandardItemii
inline void QStandardItemModelPrivate::columnsAboutToBeRemoved(QStandardItem *parent,
                                                        int start, int end)
{
    Q_Q(QStandardItemModel);
    QModelIndex index = q->indexFromItem(parent);
    q->beginRemoveColumns(index, start, end);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 619, as _ZN25QStandardItemModelPrivate12rowsInsertedEP13QStandardItemii
inline void QStandardItemModelPrivate::rowsInserted(QStandardItem *parent,
                                             int row, int count)
{
    Q_Q(QStandardItemModel);
    if (parent == root.data())
        rowHeaderItems.insert(row, count, nullptr);
    q->endInsertRows();
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 631, as _ZN25QStandardItemModelPrivate15columnsInsertedEP13QStandardItemii
inline void QStandardItemModelPrivate::columnsInserted(QStandardItem *parent,
                                                int column, int count)
{
    Q_Q(QStandardItemModel);
    if (parent == root.data())
        columnHeaderItems.insert(column, count, nullptr);
    q->endInsertColumns();
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 643, as _ZN25QStandardItemModelPrivate11rowsRemovedEP13QStandardItemii
inline void QStandardItemModelPrivate::rowsRemoved(QStandardItem *parent,
                                            int row, int count)
{
    Q_Q(QStandardItemModel);
    if (parent == root.data()) {
        for (int i = row; i < row + count; ++i) {
            QStandardItem *oldItem = rowHeaderItems.at(i);
            if (oldItem)
                oldItem->d_func()->setModel(nullptr);
            delete oldItem;
        }
        rowHeaderItems.remove(row, count);
    }
    q->endRemoveRows();
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 662, as _ZN25QStandardItemModelPrivate14columnsRemovedEP13QStandardItemii
inline void QStandardItemModelPrivate::columnsRemoved(QStandardItem *parent,
                                               int column, int count)
{
    Q_Q(QStandardItemModel);
    if (parent == root.data()) {
        for (int i = column; i < column + count; ++i) {
            QStandardItem *oldItem = columnHeaderItems.at(i);
            if (oldItem)
                oldItem->d_func()->setModel(nullptr);
            delete oldItem;
        }
        columnHeaderItems.remove(column, count);
    }
    q->endRemoveColumns();
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 411, as _ZN25QStandardItemModelPrivate18_q_emitItemChangedERK11QModelIndexS2_
inline void QStandardItemModelPrivate::_q_emitItemChanged(const QModelIndex &topLeft,
                                                   const QModelIndex &bottomRight)
{
    Q_Q(QStandardItemModel);
    QModelIndex parent = topLeft.parent();
    for (int row = topLeft.row(); row <= bottomRight.row(); ++row) {
        for (int column = topLeft.column(); column <= bottomRight.column(); ++column) {
            QModelIndex index = q->index(row, column, parent);
            if (QStandardItem *item = itemFromIndex(index))
                emit q->itemChanged(item);
        }
    }
}
//  -----------------------------------------------------------------------

//  A QStandardItemModelPrivate that Python can take functions over in. Every QStandardItemModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef void (*CuteQStandardItemModelPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
class CuteQStandardItemModelPrivate : public QStandardItemModelPrivate {
public:
  using QStandardItemModelPrivate::QStandardItemModelPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    return false;
  }

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModelPrivate::executePendingOperations() const
  void executePendingOperations() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQStandardItemModelPrivateCall0 call = reinterpret_cast<CuteQStandardItemModelPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModelPrivate::executePendingOperations();
  }
#endif  // QT_CONFIG(itemmodel)
};

//  QStandardItemModel *QStandardItemModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QStandardItemModel *ritual_ZN25QStandardItemModelPrivate6q_funcEv(
    QStandardItemModelPrivate *self) {
  return self->q_func();
}

//  const QStandardItemModel *QStandardItemModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QStandardItemModel *ritual_ZNK25QStandardItemModelPrivate6q_funcEv(
    const QStandardItemModelPrivate *self) {
  return self->q_func();
}

//  QStandardItemModelPrivate::QStandardItemModelPrivate()
extern "C" Q_DECL_EXPORT
QStandardItemModelPrivate *ritual_ZN25QStandardItemModelPrivateC1Ev() {
  return new CuteQStandardItemModelPrivate();
}

//  QStandardItemModelPrivate::~QStandardItemModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivateD1Ev(
    QStandardItemModelPrivate *self) {
  delete self;
}

//  void QStandardItemModelPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate4initEv(
    QStandardItemModelPrivate *self) {
  self->init();
}

//  QStandardItem *QStandardItemModelPrivate::createItem() const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK25QStandardItemModelPrivate10createItemEv(
    const QStandardItemModelPrivate *self) {
  return self->createItem();
}

//  QStandardItem *QStandardItemModelPrivate::itemFromIndex(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK25QStandardItemModelPrivate13itemFromIndexERK11QModelIndex(
    const QStandardItemModelPrivate *self,
    const QModelIndex *index) {
  return self->itemFromIndex(*index);
}

//  void QStandardItemModelPrivate::rowsAboutToBeInserted(QStandardItem
//      *parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate21rowsAboutToBeInsertedEP13QStandardItemii(
    QStandardItemModelPrivate *self,
    QStandardItem *parent,
    int start,
    int end) {
  self->rowsAboutToBeInserted(parent, start, end);
}

//  void QStandardItemModelPrivate::columnsAboutToBeInserted(QStandardItem
//      *parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate24columnsAboutToBeInsertedEP13QStandardItemii(
    QStandardItemModelPrivate *self,
    QStandardItem *parent,
    int start,
    int end) {
  self->columnsAboutToBeInserted(parent, start, end);
}

//  void QStandardItemModelPrivate::rowsAboutToBeRemoved(QStandardItem
//      *parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate20rowsAboutToBeRemovedEP13QStandardItemii(
    QStandardItemModelPrivate *self,
    QStandardItem *parent,
    int start,
    int end) {
  self->rowsAboutToBeRemoved(parent, start, end);
}

//  void QStandardItemModelPrivate::columnsAboutToBeRemoved(QStandardItem
//      *parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate23columnsAboutToBeRemovedEP13QStandardItemii(
    QStandardItemModelPrivate *self,
    QStandardItem *parent,
    int start,
    int end) {
  self->columnsAboutToBeRemoved(parent, start, end);
}

//  void QStandardItemModelPrivate::rowsInserted(QStandardItem *parent, int
//      row, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate12rowsInsertedEP13QStandardItemii(
    QStandardItemModelPrivate *self,
    QStandardItem *parent,
    int row,
    int count) {
  self->rowsInserted(parent, row, count);
}

//  void QStandardItemModelPrivate::columnsInserted(QStandardItem *parent,
//      int column, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate15columnsInsertedEP13QStandardItemii(
    QStandardItemModelPrivate *self,
    QStandardItem *parent,
    int column,
    int count) {
  self->columnsInserted(parent, column, count);
}

//  void QStandardItemModelPrivate::rowsRemoved(QStandardItem *parent, int
//      row, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate11rowsRemovedEP13QStandardItemii(
    QStandardItemModelPrivate *self,
    QStandardItem *parent,
    int row,
    int count) {
  self->rowsRemoved(parent, row, count);
}

//  void QStandardItemModelPrivate::columnsRemoved(QStandardItem *parent, int
//      column, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate14columnsRemovedEP13QStandardItemii(
    QStandardItemModelPrivate *self,
    QStandardItem *parent,
    int column,
    int count) {
  self->columnsRemoved(parent, column, count);
}

//  void QStandardItemModelPrivate::_q_emitItemChanged(const QModelIndex
//      &topLeft, const QModelIndex &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QStandardItemModelPrivate18_q_emitItemChangedERK11QModelIndexS2_(
    QStandardItemModelPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->_q_emitItemChanged(*topLeft, *bottomRight);
}

//  a Python function taken by a CuteQStandardItemModelPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStandardItemModelPrivate(
    QStandardItemModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStandardItemModelPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(standarditemmodel)
