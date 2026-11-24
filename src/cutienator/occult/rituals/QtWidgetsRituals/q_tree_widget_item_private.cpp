//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treewidget)
#if QT_CONFIG(treewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/qheaderview.h>
#include <QtGui/qpainter.h>
#include <QtCore/qstack.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qtreewidget_p.h>
#include <QtWidgets/private/qwidgetitemdata_p.h>
#include <QtWidgets/private/qtreewidgetitemiterator_p.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qtreewidget.cpp, line 191, as _ZNK10QTreeModel5indexEPK15QTreeWidgetItemi
inline QModelIndex QTreeModel::index(const QTreeWidgetItem *item, int column) const
{
    executePendingSort();

    if (!item || (item == rootItem))
        return QModelIndex();
    const QTreeWidgetItem *par = item->parent();
    QTreeWidgetItem *itm = const_cast<QTreeWidgetItem*>(item);
    if (!par)
        par = rootItem;
    int row;
    int guess = item->d->rowGuess;
    if (guess >= 0
        && par->children.size() > guess
        && par->children.at(guess) == itm) {
        row = guess;
    } else {
        row = par->children.lastIndexOf(itm);
        itm->d->rowGuess = row;
    }
    return createIndex(row, column, itm);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 836, as _ZN10QTreeModel9sortItemsEP5QListIP15QTreeWidgetItemEiN2Qt9SortOrderE
inline void QTreeModel::sortItems(QList<QTreeWidgetItem*> *items, int column, Qt::SortOrder order)
{
    // see QTreeViewItem::operator<
    Q_UNUSED(column);
    if (isChanging())
        return;

    // store the original order of indexes
    QList<std::pair<QTreeWidgetItem *, int>> sorting(items->size());
    for (int i = 0; i < sorting.size(); ++i) {
        sorting[i].first = items->at(i);
        sorting[i].second = i;
    }

    // do the sorting
    const auto compare = (order == Qt::AscendingOrder ? &itemLessThan : &itemGreaterThan);
    std::stable_sort(sorting.begin(), sorting.end(), compare);

    QModelIndexList fromList;
    QModelIndexList toList;
    int colCount = columnCount();
    for (int r = 0; r < sorting.size(); ++r) {
        int oldRow = sorting.at(r).second;
        if (oldRow == r)
            continue;
        QTreeWidgetItem *item = sorting.at(r).first;
        items->replace(r, item);
        for (int c = 0; c < colCount; ++c) {
            QModelIndex from = createIndex(oldRow, c, item);
            if (static_cast<QAbstractItemModelPrivate *>(d_ptr.data())->persistent.indexes.contains(from)) {
                QModelIndex to = createIndex(r, c, item);
                fromList << from;
                toList << to;
            }
        }
    }
    changePersistentIndexList(fromList, toList);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 766, as _ZNK10QTreeModel10isChangingEv
inline bool QTreeModel::isChanging() const
{
    Q_D(const QTreeModel);
    return !d->changes.isEmpty();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 668, as _ZN10QTreeModel12itemLessThanERKSt4pairIP15QTreeWidgetItemiES5_
inline bool QTreeModel::itemLessThan(const std::pair<QTreeWidgetItem*,int> &left,
                              const std::pair<QTreeWidgetItem*,int> &right)
{
    return *(left.first) < *(right.first);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 683, as _ZN10QTreeModel15itemGreaterThanERKSt4pairIP15QTreeWidgetItemiES5_
inline bool QTreeModel::itemGreaterThan(const std::pair<QTreeWidgetItem*,int> &left,
                                 const std::pair<QTreeWidgetItem*,int> &right)
{
    return *(right.first) < *(left.first);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 1690, as _ZN22QTreeWidgetItemPrivate17propagateDisabledEP15QTreeWidgetItem
inline void QTreeWidgetItemPrivate::propagateDisabled(QTreeWidgetItem *item)
{
    Q_ASSERT(item);
    const bool enable = item->par ? (item->par->itemFlags.testFlag(Qt::ItemIsEnabled)) : true;

    QStack<QTreeWidgetItem*> parents;
    parents.push(item);
    while (!parents.isEmpty()) {
        QTreeWidgetItem *parent = parents.pop();
        if (!parent->d->disabled) { // if not explicitly disabled
            Qt::ItemFlags oldFlags = parent->itemFlags;
            if (enable)
                parent->itemFlags = parent->itemFlags | Qt::ItemIsEnabled;
            else
                parent->itemFlags = parent->itemFlags & ~Qt::ItemIsEnabled;
            if (parent->itemFlags != oldFlags)
                parent->itemChanged();
        }

        for (int i = 0; i < parent->children.size(); ++i) {
            QTreeWidgetItem *child = parent->children.at(i);
            parents.push(child);
        }
    }
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 1670, as _ZN22QTreeWidgetItemPrivate18updateHiddenStatusEP15QTreeWidgetItemb
inline void QTreeWidgetItemPrivate::updateHiddenStatus(QTreeWidgetItem *item, bool inserting)
{
    QTreeModel *model = item->treeModel();
    if (!model)
        return;
    QStack<QTreeWidgetItem *> parents;
    parents.push(item);
    while (!parents.isEmpty()) {
        QTreeWidgetItem *parent = parents.pop();
        if (parent->d->hidden) {
            const QModelIndex index = model->index(parent, 0);
            item->view->setRowHidden(index.row(), index.parent(), inserting);
        }
        for (int i = 0; i < parent->children.size(); ++i) {
            QTreeWidgetItem *child = parent->children.at(i);
            parents.push(child);
        }
    }
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2132, as _ZN22QTreeWidgetItemPrivate12sortChildrenEiN2Qt9SortOrderEb
inline void QTreeWidgetItemPrivate::sortChildren(int column, Qt::SortOrder order, bool climb)
{
    QTreeModel *model = q->treeModel();
    if (!model)
        return;
    model->sortItems(&q->children, column, order);
    if (climb) {
        QList<QTreeWidgetItem*>::iterator it = q->children.begin();
        for (; it != q->children.end(); ++it) {
            //here we call the private object's method to avoid emitting
            //the layoutAboutToBeChanged and layoutChanged signals
            (*it)->d->sortChildren(column, order, climb);
        }
    }
}
//  -----------------------------------------------------------------------

//  QTreeWidgetItemPrivate::QTreeWidgetItemPrivate(QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemPrivate *ritual_ZN22QTreeWidgetItemPrivateC1EP15QTreeWidgetItem(
    QTreeWidgetItem *item) {
  return new QTreeWidgetItemPrivate(item);
}

//  void QTreeWidgetItemPrivate::propagateDisabled(QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTreeWidgetItemPrivate17propagateDisabledEP15QTreeWidgetItem(
    QTreeWidgetItemPrivate *self,
    QTreeWidgetItem *item) {
  self->propagateDisabled(item);
}

//  void QTreeWidgetItemPrivate::updateHiddenStatus(QTreeWidgetItem *item,
//      bool inserting)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTreeWidgetItemPrivate18updateHiddenStatusEP15QTreeWidgetItemb(
    QTreeWidgetItemPrivate *self,
    QTreeWidgetItem *item,
    bool inserting) {
  self->updateHiddenStatus(item, inserting);
}

//  void QTreeWidgetItemPrivate::sortChildren(int column, Qt::SortOrder
//      order, bool climb)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTreeWidgetItemPrivate12sortChildrenEiN2Qt9SortOrderEb(
    QTreeWidgetItemPrivate *self,
    int column,
    Qt::SortOrder order,
    bool climb) {
  self->sortChildren(column, order, climb);
}

//  QTreeWidgetItemPrivate::~QTreeWidgetItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTreeWidgetItemPrivateD1Ev(QTreeWidgetItemPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(treewidget)
