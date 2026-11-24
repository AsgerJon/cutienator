//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treewidget)
#if QT_CONFIG(treewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
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
#include <QtWidgets/private/qtreewidgetitemiterator_p.h>
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/private/qtreewidget_p.h>
#include <QtWidgets/private/qwidgetitemdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/widgets/itemviews/qtreewidgetitemiterator.cpp, line 297, as _ZN30QTreeWidgetItemIteratorPrivate19ensureValidIteratorEPK15QTreeWidgetItem
inline void QTreeWidgetItemIteratorPrivate::ensureValidIterator(const QTreeWidgetItem *itemToBeRemoved)
{
    Q_Q(QTreeWidgetItemIterator);
    Q_ASSERT(itemToBeRemoved);

    if (!q->current) return;
    QTreeWidgetItem *nextItem = q->current;

    // Do not walk to the ancestor to find the other item if they have the same parent.
    if (nextItem->parent() != itemToBeRemoved->parent()) {
        while (nextItem->parent() && nextItem != itemToBeRemoved) {
            nextItem = nextItem->parent();
        }
    }
    // If the item to be removed is an ancestor of the current iterator item,
    // we need to adjust the iterator.
    if (nextItem == itemToBeRemoved) {
        QTreeWidgetItem *parent = nextItem;
        nextItem = nullptr;
        while (parent && !nextItem) {
            nextItem = nextSibling(parent);
            parent = parent->parent();
        }
        if (nextItem) {
            // Ooooh... Set the iterator to the next valid item
            *q = QTreeWidgetItemIterator(nextItem, q->flags);
            if (!(q->matchesFlags(nextItem))) ++(*q);
        } else {
            // set it to null.
            q->current = nullptr;
            m_parentIndex.clear();
            return;
        }
    }
    if (nextItem->parent() == itemToBeRemoved->parent()) {
        // They have the same parent, i.e. we have to adjust the m_currentIndex member of the iterator
        // if the deleted item is to the left of the nextItem.

        QTreeWidgetItem *par = itemToBeRemoved->parent();   // We know they both have the same parent.
        QTreeWidget *tw = itemToBeRemoved->treeWidget();    // ..and widget
        int indexOfItemToBeRemoved = par ? par->indexOfChild(const_cast<QTreeWidgetItem *>(itemToBeRemoved))
            : tw->indexOfTopLevelItem(const_cast<QTreeWidgetItem *>(itemToBeRemoved));
        int indexOfNextItem = par ? par->indexOfChild(nextItem) : tw->indexOfTopLevelItem(nextItem);

        if (indexOfItemToBeRemoved <= indexOfNextItem) {
            // A sibling to the left of us was deleted, adjust the m_currentIndex member of the iterator.
            // Note that the m_currentIndex will be wrong until the item is actually removed!
            m_currentIndex--;
        }
    }
}

//  from src/widgets/itemviews/qtreewidgetitemiterator.cpp, line 231, as _ZNK30QTreeWidgetItemIteratorPrivate11nextSiblingEPK15QTreeWidgetItem
inline QTreeWidgetItem* QTreeWidgetItemIteratorPrivate::nextSibling(const QTreeWidgetItem* item) const
{
    Q_ASSERT(item);
    QTreeWidgetItem *next = nullptr;
    if (QTreeWidgetItem *par = item->parent()) {
        int i = par->indexOfChild(const_cast<QTreeWidgetItem*>(item));
        next = par->child(i + 1);
    } else {
        QTreeWidget *tw = item->treeWidget();
        int i = tw->indexOfTopLevelItem(const_cast<QTreeWidgetItem*>(item));
        next = tw->topLevelItem(i + 1);
    }
    return next;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 105, as _ZN10QTreeModelD1Ev
inline QTreeModel::~QTreeModel()
{
    clear();
    headerItem->view = nullptr;
    delete headerItem;
    rootItem->view = nullptr;
    delete rootItem;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 120, as _ZN10QTreeModel5clearEv
inline void QTreeModel::clear()
{
    SkipSorting skipSorting(this);
    beginResetModel();
    for (int i = 0; i < rootItem->childCount(); ++i) {
        QTreeWidgetItem *item = rootItem->children.at(i);
        item->par = nullptr;
        item->view = nullptr;
        delete item;
    }
    rootItem->children.clear();
    sortPendingTimer.stop();
    endResetModel();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 141, as _ZN10QTreeModel14setColumnCountEi
inline void QTreeModel::setColumnCount(int columns)
{
    SkipSorting skipSorting(this);
    if (columns < 0)
        return;
    if (!headerItem) {
        headerItem = new QTreeWidgetItem();
        headerItem->view = view();
    }
    int count = columnCount();
    if (count == columns)
        return;

    if (columns < count) {
        beginRemoveColumns(QModelIndex(), columns, count - 1);
        headerItem->values.resize(columns);
        endRemoveColumns();
    } else {
        beginInsertColumns(QModelIndex(), count, columns - 1);
        headerItem->values.resize(columns);
        for (int i = count; i < columns; ++i) {// insert data without emitting the dataChanged signal
            headerItem->values[i].append(QWidgetItemData(Qt::DisplayRole, QString::number(i + 1)));
            headerItem->d->display.append(QString::number(i + 1));
        }
        endInsertColumns();
    }
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 177, as _ZNK10QTreeModel4itemERK11QModelIndex
inline QTreeWidgetItem *QTreeModel::item(const QModelIndex &index) const
{
    if (!index.isValid())
        return nullptr;
    return static_cast<QTreeWidgetItem*>(index.internalPointer());
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 756, as _ZN10QTreeModel11itemChangedEP15QTreeWidgetItem
inline void QTreeModel::itemChanged(QTreeWidgetItem *item)
{
    if (item->columnCount() <= 0)
        return;
    SkipSorting skipSorting(this); //this is kind of wrong, but not doing this would kill performance
    QModelIndex left = index(item, 0);
    QModelIndex right = index(item, item->columnCount() - 1);
    emit dataChanged(left, right);
}

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

//  from src/widgets/itemviews/qtreewidget.cpp, line 222, as _ZNK10QTreeModel5indexEiiRK11QModelIndex
inline QModelIndex QTreeModel::index(int row, int column, const QModelIndex &parent) const
{
    executePendingSort();

    int c = columnCount(parent);
    if (row < 0 || column < 0 || column >= c)
        return QModelIndex();

    QTreeWidgetItem *parentItem = parent.isValid() ? item(parent) : rootItem;
    if (parentItem && row < parentItem->childCount()) {
        QTreeWidgetItem *itm = parentItem->child(row);
        if (itm)
            return createIndex(row, column, itm);
        return QModelIndex();
    }

    return QModelIndex();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 249, as _ZNK10QTreeModel6parentERK11QModelIndex
inline QModelIndex QTreeModel::parent(const QModelIndex &child) const
{
    SkipSorting skipSorting(this); //The reason we don't sort here is that this might be called from a valid QPersistentModelIndex
                                   //We don't want it to become suddenly invalid

    if (!child.isValid())
        return QModelIndex();
    QTreeWidgetItem *itm = static_cast<QTreeWidgetItem *>(child.internalPointer());
    if (!itm || itm == rootItem)
        return QModelIndex();
    QTreeWidgetItem *parent = itm->parent();
    return index(parent, 0);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 270, as _ZNK10QTreeModel8rowCountERK11QModelIndex
inline int QTreeModel::rowCount(const QModelIndex &parent) const
{
    if (!parent.isValid())
        return rootItem->childCount();

    QTreeWidgetItem *parentItem = item(parent);
    if (parentItem)
        return parentItem->childCount();
    return 0;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 289, as _ZNK10QTreeModel11columnCountERK11QModelIndex
inline int QTreeModel::columnCount(const QModelIndex &index) const
{
    Q_UNUSED(index);
    if (!headerItem)
        return 0;
    return headerItem->columnCount();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 297, as _ZNK10QTreeModel11hasChildrenERK11QModelIndex
inline bool QTreeModel::hasChildren(const QModelIndex &parent) const
{
    if (!parent.isValid())
        return (rootItem->childCount() > 0);

    QTreeWidgetItem *itm = item(parent);
    if (!itm)
        return false;
    switch (itm->d->policy) {
    case QTreeWidgetItem::ShowIndicator:
        return true;
    case QTreeWidgetItem::DontShowIndicator:
        return false;
    case QTreeWidgetItem::DontShowIndicatorWhenChildless:
        return (itm->childCount() > 0);
    }
    return false;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 324, as _ZNK10QTreeModel4dataERK11QModelIndexi
inline QVariant QTreeModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid())
        return QVariant();
    QTreeWidgetItem *itm = item(index);
    if (itm)
        return itm->data(index.column(), role);
    return QVariant();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 344, as _ZN10QTreeModel7setDataERK11QModelIndexRK8QVarianti
inline bool QTreeModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (!index.isValid())
        return false;
    QTreeWidgetItem *itm = item(index);
    if (itm) {
        itm->setData(index.column(), role, value);
        return true;
    }
    return false;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 356, as _ZN10QTreeModel13clearItemDataERK11QModelIndex
inline bool QTreeModel::clearItemData(const QModelIndex &index)
{
    if (!checkIndex(index, CheckIndexOption::IndexIsValid))
        return false;
    QTreeWidgetItem *itm = item(index);
    if (!itm)
        return false;
    const auto beginIter = itm->values.at(index.column()).cbegin();
    const auto endIter = itm->values.at(index.column()).cend();
    if (std::all_of(beginIter, endIter, [](const QWidgetItemData& data) -> bool { return !data.value.isValid(); })
        && !itm->d->display.at(index.column()).isValid()) {
        return true; //it's already cleared
    }
    itm->d->display[index.column()] = QVariant();
    itm->values[index.column()].clear();
    emit dataChanged(index, index, QList<int> {});
    return true;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 375, as _ZNK10QTreeModel8itemDataERK11QModelIndex
inline QMap<int, QVariant> QTreeModel::itemData(const QModelIndex &index) const
{
    QMap<int, QVariant> roles;
    QTreeWidgetItem *itm = item(index);
    if (itm) {
        int column = index.column();
        if (column < itm->values.size()) {
            for (int i = 0; i < itm->values.at(column).size(); ++i) {
                roles.insert(itm->values.at(column).at(i).role,
                             itm->values.at(column).at(i).value);
            }
        }

        // the two special cases
        QVariant displayValue = itm->data(column, Qt::DisplayRole);
        if (displayValue.isValid())
            roles.insert(Qt::DisplayRole, displayValue);

        QVariant checkValue = itm->data(column, Qt::CheckStateRole);
        if (checkValue.isValid())
            roles.insert(Qt::CheckStateRole, checkValue);
    }
    return roles;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 493, as _ZNK10QTreeModel10headerDataEiN2Qt11OrientationEi
inline QVariant QTreeModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (orientation != Qt::Horizontal)
        return QVariant();

    if (headerItem)
        return headerItem->data(section, role);
    if (role == Qt::DisplayRole)
        return QString::number(section + 1);
    return QVariant();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 515, as _ZN10QTreeModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti
inline bool QTreeModel::setHeaderData(int section, Qt::Orientation orientation,
                               const QVariant &value, int role)
{
    if (section < 0 || orientation != Qt::Horizontal || !headerItem || section >= columnCount())
        return false;

    headerItem->setData(section, role, value);
    return true;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 538, as _ZNK10QTreeModel5flagsERK11QModelIndex
inline Qt::ItemFlags QTreeModel::flags(const QModelIndex &index) const
{
    if (!index.isValid())
        return rootItem->flags();
    QTreeWidgetItem *itm = item(index);
    Q_ASSERT(itm);
    return itm->flags();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 554, as _ZN10QTreeModel4sortEiN2Qt9SortOrderE
inline void QTreeModel::sort(int column, Qt::SortOrder order)
{
    SkipSorting skipSorting(this);
    sortPendingTimer.stop();

    if (column < 0 || column >= columnCount())
        return;

    //layoutAboutToBeChanged and layoutChanged will be called by sortChildren
    rootItem->sortChildren(column, order, true);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 404, as _ZN10QTreeModel10insertRowsEiiRK11QModelIndex
inline bool QTreeModel::insertRows(int row, int count, const QModelIndex &parent)
{
    SkipSorting skipSorting(this);
    if (count < 1 || row < 0 || row > rowCount(parent) || parent.column() > 0)
        return false;

    beginInsertRows(parent, row, row + count - 1);
    QTreeWidgetItem *par = item(parent);
    while (count > 0) {
        QTreeWidgetItem *item = new QTreeWidgetItem();
        item->view = view();
        item->par = par;
        if (par)
            par->children.insert(row++, item);
        else
            rootItem->children.insert(row++, item);
        --count;
    }
    endInsertRows();
    return true;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 430, as _ZN10QTreeModel13insertColumnsEiiRK11QModelIndex
inline bool QTreeModel::insertColumns(int column, int count, const QModelIndex &parent)
{
    SkipSorting skipSorting(this);
    if (count < 1 || column < 0 || column > columnCount(parent) || parent.column() > 0 || !headerItem)
        return false;

    beginInsertColumns(parent, column, column + count - 1);

    int oldCount = columnCount(parent);
    column = qBound(0, column, oldCount);
    headerItem->values.resize(oldCount + count);
    for (int i = oldCount; i < oldCount + count; ++i) {
        headerItem->values[i].append(QWidgetItemData(Qt::DisplayRole, QString::number(i + 1)));
        headerItem->d->display.append(QString::number(i + 1));
    }

    QStack<QTreeWidgetItem*> itemstack;
    itemstack.push(0);
    while (!itemstack.isEmpty()) {
        QTreeWidgetItem *par = itemstack.pop();
        QList<QTreeWidgetItem*> children = par ? par->children : rootItem->children;
        for (int row = 0; row < children.size(); ++row) {
            QTreeWidgetItem *child = children.at(row);
            if (child->children.size())
                itemstack.push(child);
            child->values.insert(column, count, QList<QWidgetItemData>());
        }
    }

    endInsertColumns();
    return true;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 702, as _ZNK10QTreeModel9mimeTypesEv
inline QStringList QTreeModel::mimeTypes() const
{
    auto v = view();
    if (v)
        return v->mimeTypes();
    return {};
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 715, as _ZNK10QTreeModel8mimeDataERK5QListI11QModelIndexE
inline QMimeData *QTreeModel::mimeData(const QModelIndexList &indexes) const
{
    QList<QTreeWidgetItem *> items;
    std::transform(indexes.begin(), indexes.end(), std::back_inserter(items),
                   [this](const QModelIndex &idx) -> QTreeWidgetItem * { return item(idx); });

    // Ensure we only have one item as an item may have more than
    // one index selected if there is more than one column
    std::sort(items.begin(), items.end());
    items.erase(std::unique(items.begin(), items.end()), items.end());

    // cachedIndexes is a little hack to avoid copying from QModelIndexList to
    // QList<QTreeWidgetItem*> and back again in the view
    cachedIndexes = indexes;
    QMimeData *mimeData = view()->mimeData(items);
    cachedIndexes.clear();
    return mimeData;
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 734, as _ZN10QTreeModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex
inline bool QTreeModel::dropMimeData(const QMimeData *data, Qt::DropAction action,
                              int row, int column, const QModelIndex &parent)
{
    if (row == -1 && column == -1)
        row = rowCount(parent); // append
    return view()->dropMimeData(item(parent), row, data, action);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 742, as _ZNK10QTreeModel20supportedDropActionsEv
inline Qt::DropActions QTreeModel::supportedDropActions() const
{
    return view()->supportedDropActions();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 747, as _ZNK10QTreeModel20supportedDragActionsEv
inline Qt::DropActions QTreeModel::supportedDragActions() const
{
#if QT_CONFIG(draganddrop)
    return view()->supportedDragActions();
#else
    return Qt::DropActions(Qt::IgnoreAction);
#endif
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 710, as _ZNK10QTreeModel16internalMimeDataEv
inline QMimeData *QTreeModel::internalMimeData()  const
{
    return QAbstractItemModel::mimeData(cachedIndexes);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 804, as _ZN10QTreeModel16beginInsertItemsEP15QTreeWidgetItemii
inline void QTreeModel::beginInsertItems(QTreeWidgetItem *parent, int row, int count)
{
    QModelIndex par = index(parent, 0);
    beginInsertRows(par, row, row + count - 1);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 810, as _ZN10QTreeModel14endInsertItemsEv
inline void QTreeModel::endInsertItems()
{
    endInsertRows();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 815, as _ZN10QTreeModel16beginRemoveItemsEP15QTreeWidgetItemii
inline void QTreeModel::beginRemoveItems(QTreeWidgetItem *parent, int row, int count)
{
    Q_ASSERT(row >= 0);
    Q_ASSERT(count > 0);
    beginRemoveRows(index(parent, 0), row, row + count - 1);
    if (!parent)
        parent = rootItem;
    // now update the iterators
    for (int i = 0; i < iterators.size(); ++i) {
        for (int j = 0; j < count; j++) {
            QTreeWidgetItem *c = parent->child(row + j);
            iterators[i]->d_func()->ensureValidIterator(c);
        }
    }
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 831, as _ZN10QTreeModel14endRemoveItemsEv
inline void QTreeModel::endRemoveItems()
{
    endRemoveRows();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 875, as _ZN10QTreeModel10timerEventEP11QTimerEvent
inline void QTreeModel::timerEvent(QTimerEvent *ev)
{
    if (ev->timerId() == sortPendingTimer.timerId()) {
        executePendingSort();
    } else {
        QAbstractItemModel::timerEvent(ev);
    }
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 766, as _ZNK10QTreeModel10isChangingEv
inline bool QTreeModel::isChanging() const
{
    Q_D(const QTreeModel);
    return !d->changes.isEmpty();
}
//  -----------------------------------------------------------------------

//  Only a class built on QTreeModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTreeModel : QTreeModel {
  using QTreeModel::timerEvent;
};

//  A QTreeModel that Python can take functions over in. Every QTreeModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef const QModelIndex * (*CuteQTreeModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef const QModelIndex * (*CuteQTreeModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef int (*CuteQTreeModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef int (*CuteQTreeModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef const QVariant * (*CuteQTreeModelCall5)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeModelCall6)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef const QVariant * (*CuteQTreeModelCall8)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeModelCall9)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef int (*CuteQTreeModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef void (*CuteQTreeModelCall11)(const void *, int, int, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeModelCall12)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeModelCall13)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeModelCall14)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeModelCall15)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef int (*CuteQTreeModelCall16)(const void *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
typedef int (*CuteQTreeModelCall17)(const void *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treewidget)
typedef void (*CuteQTreeModelCall18)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQTreeModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTreeModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTreeModelCall21)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTreeModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTreeModelCall23)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQTreeModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTreeModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQTreeModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQTreeModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQTreeModelCall28)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTreeModelCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQTreeModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQTreeModelCall31)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTreeModelCall32)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTreeModelCall33)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTreeModel : public QTreeModel {
public:
  using QTreeModel::QTreeModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  QModelIndex QTreeModel::index(int row, int column, const QModelIndex
  //      &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTreeModelCall0 call = reinterpret_cast<CuteQTreeModelCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QTreeModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  QModelIndex QTreeModel::parent(const QModelIndex &child) const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTreeModelCall1 call = reinterpret_cast<CuteQTreeModelCall1>(taken[1]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QTreeModel::parent(child);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  int QTreeModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTreeModelCall2 call = reinterpret_cast<CuteQTreeModelCall2>(taken[2]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QTreeModel::rowCount(parent);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  int QTreeModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTreeModelCall3 call = reinterpret_cast<CuteQTreeModelCall3>(taken[3]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QTreeModel::columnCount(parent);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  bool QTreeModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQTreeModelCall4 call = reinterpret_cast<CuteQTreeModelCall4>(taken[4]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QTreeModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  QVariant QTreeModel::data(const QModelIndex &index, int role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTreeModelCall5 call = reinterpret_cast<CuteQTreeModelCall5>(taken[5]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QTreeModel::data(index, role);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  bool QTreeModel::setData(const QModelIndex &index, const QVariant
  //      &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTreeModelCall6 call = reinterpret_cast<CuteQTreeModelCall6>(taken[6]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QTreeModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  bool QTreeModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTreeModelCall7 call = reinterpret_cast<CuteQTreeModelCall7>(taken[7]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QTreeModel::clearItemData(index);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  QVariant QTreeModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTreeModelCall8 call = reinterpret_cast<CuteQTreeModelCall8>(taken[8]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QTreeModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  bool QTreeModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTreeModelCall9 call = reinterpret_cast<CuteQTreeModelCall9>(taken[9]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QTreeModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  Qt::ItemFlags QTreeModel::flags(const QModelIndex &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTreeModelCall10 call = reinterpret_cast<CuteQTreeModelCall10>(taken[10]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QTreeModel::flags(index);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  void QTreeModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTreeModelCall11 call = reinterpret_cast<CuteQTreeModelCall11>(taken[11]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QTreeModel::sort(column, order);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  bool QTreeModel::insertRows(int row, int count, const QModelIndex
  //      &a2)
  bool insertRows(int row, int count, const QModelIndex &a2) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTreeModelCall12 call = reinterpret_cast<CuteQTreeModelCall12>(taken[12]);
      bool given = call(this, row, count, &a2, &handled);
      if (handled) return given;
    }
    return QTreeModel::insertRows(row, count, a2);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  bool QTreeModel::insertColumns(int column, int count, const
  //      QModelIndex &a2)
  bool insertColumns(int column, int count, const QModelIndex &a2) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTreeModelCall13 call = reinterpret_cast<CuteQTreeModelCall13>(taken[13]);
      bool given = call(this, column, count, &a2, &handled);
      if (handled) return given;
    }
    return QTreeModel::insertColumns(column, count, a2);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  bool QTreeModel::removeRows(int row, int count, const QModelIndex
  //      &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTreeModelCall14 call = reinterpret_cast<CuteQTreeModelCall14>(taken[14]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QTreeModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  bool QTreeModel::dropMimeData(const QMimeData *data, Qt::DropAction
  //      action, int row, int column, const QModelIndex &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTreeModelCall15 call = reinterpret_cast<CuteQTreeModelCall15>(taken[15]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QTreeModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  Qt::DropActions QTreeModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTreeModelCall16 call = reinterpret_cast<CuteQTreeModelCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QTreeModel::supportedDropActions();
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(treewidget)
  //  Qt::DropActions QTreeModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQTreeModelCall17 call = reinterpret_cast<CuteQTreeModelCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QTreeModel::supportedDragActions();
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treewidget)
  //  void QTreeModel::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQTreeModelCall18 call = reinterpret_cast<CuteQTreeModelCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTreeModel::timerEvent(a0);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQTreeModelCall19 call = reinterpret_cast<CuteQTreeModelCall19>(taken[19]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQTreeModelCall20 call = reinterpret_cast<CuteQTreeModelCall20>(taken[20]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[21]) {
      int handled = 0;
      CuteQTreeModelCall21 call = reinterpret_cast<CuteQTreeModelCall21>(taken[21]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent,
  //      int sourceRow, int count, const QModelIndex &destinationParent,
  //      int destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[22]) {
      int handled = 0;
      CuteQTreeModelCall22 call = reinterpret_cast<CuteQTreeModelCall22>(taken[22]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent,
  //      int sourceColumn, int count, const QModelIndex
  //      &destinationParent, int destinationChild)
  bool moveColumns(
      const QModelIndex &sourceParent,
      int sourceColumn,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTreeModelCall23 call = reinterpret_cast<CuteQTreeModelCall23>(taken[23]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTreeModelCall24 call = reinterpret_cast<CuteQTreeModelCall24>(taken[24]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractItemModel::fetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQTreeModelCall25 call = reinterpret_cast<CuteQTreeModelCall25>(taken[25]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQTreeModelCall26 call = reinterpret_cast<CuteQTreeModelCall26>(taken[26]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQTreeModelCall27 call = reinterpret_cast<CuteQTreeModelCall27>(taken[27]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::span(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQTreeModelCall28 call = reinterpret_cast<CuteQTreeModelCall28>(taken[28]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[29]) {
      int handled = 0;
      CuteQTreeModelCall29 call = reinterpret_cast<CuteQTreeModelCall29>(taken[29]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[30]) {
      int handled = 0;
      CuteQTreeModelCall30 call = reinterpret_cast<CuteQTreeModelCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[31]) {
      int handled = 0;
      CuteQTreeModelCall31 call = reinterpret_cast<CuteQTreeModelCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQTreeModelCall32 call = reinterpret_cast<CuteQTreeModelCall32>(taken[32]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTreeModelCall33 call = reinterpret_cast<CuteQTreeModelCall33>(taken[33]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQTreeModelCall34 call = reinterpret_cast<CuteQTreeModelCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQTreeModelCall35 call = reinterpret_cast<CuteQTreeModelCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[36]) {
      int handled = 0;
      CuteQTreeModelCall36 call = reinterpret_cast<CuteQTreeModelCall36>(taken[36]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[37]) {
      int handled = 0;
      CuteQTreeModelCall37 call = reinterpret_cast<CuteQTreeModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTreeModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTreeModel10metaObjectEv(
    const QTreeModel *self) {
  return self->metaObject();
}

//  QTreeModel::~QTreeModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModelD1Ev(QTreeModel *self) {
  delete self;
}

//  QTreeWidget *QTreeModel::view() const
extern "C" Q_DECL_EXPORT
QTreeWidget *ritual_ZNK10QTreeModel4viewEv(const QTreeModel *self) {
  return self->view();
}

//  void QTreeModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModel5clearEv(QTreeModel *self) {
  self->clear();
}

//  void QTreeModel::setColumnCount(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModel14setColumnCountEi(QTreeModel *self, int columns) {
  self->setColumnCount(columns);
}

//  QTreeWidgetItem *QTreeModel::item(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK10QTreeModel4itemERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *index) {
  return self->item(*index);
}

//  void QTreeModel::itemChanged(QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModel11itemChangedEP15QTreeWidgetItem(
    QTreeModel *self,
    QTreeWidgetItem *item) {
  self->itemChanged(item);
}

//  QModelIndex QTreeModel::index(const QTreeWidgetItem *item, int column)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK10QTreeModel5indexEPK15QTreeWidgetItemi(
    const QTreeModel *self,
    const QTreeWidgetItem *item,
    int column) {
  return new QModelIndex(self->index(item, column));
}

//  QModelIndex QTreeModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK10QTreeModel5indexEiiRK11QModelIndex(
    const QTreeModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QTreeModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK10QTreeModel6parentERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  int QTreeModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTreeModel8rowCountERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QTreeModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTreeModel11columnCountERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  bool QTreeModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTreeModel11hasChildrenERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QVariant QTreeModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QTreeModel4dataERK11QModelIndexi(
    const QTreeModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QTreeModel::setData(const QModelIndex &index, const QVariant &value,
//      int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTreeModel7setDataERK11QModelIndexRK8QVarianti(
    QTreeModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QTreeModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTreeModel13clearItemDataERK11QModelIndex(
    QTreeModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  QMap<int, QVariant> QTreeModel::itemData(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK10QTreeModel8itemDataERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *index) {
  return new QMap<int, QVariant>(self->itemData(*index));
}

//  QVariant QTreeModel::headerData(int section, Qt::Orientation orientation,
//      int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QTreeModel10headerDataEiN2Qt11OrientationEi(
    const QTreeModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QTreeModel::setHeaderData(int section, Qt::Orientation orientation,
//      const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTreeModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QTreeModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  Qt::ItemFlags QTreeModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTreeModel5flagsERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  void QTreeModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModel4sortEiN2Qt9SortOrderE(
    QTreeModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  bool QTreeModel::insertRows(int row, int count, const QModelIndex &a2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTreeModel10insertRowsEiiRK11QModelIndex(
    QTreeModel *self,
    int row,
    int count,
    const QModelIndex *a2) {
  return self->insertRows(row, count, *a2);
}

//  bool QTreeModel::insertColumns(int column, int count, const QModelIndex
//      &a2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTreeModel13insertColumnsEiiRK11QModelIndex(
    QTreeModel *self,
    int column,
    int count,
    const QModelIndex *a2) {
  return self->insertColumns(column, count, *a2);
}

//  QStringList QTreeModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QTreeModel9mimeTypesEv(const QTreeModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QTreeModel::mimeData(const QModelIndexList &indexes) const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK10QTreeModel8mimeDataERK5QListI11QModelIndexE(
    const QTreeModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  bool QTreeModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTreeModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QTreeModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QTreeModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTreeModel20supportedDropActionsEv(const QTreeModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  Qt::DropActions QTreeModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTreeModel20supportedDragActionsEv(const QTreeModel *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  QMimeData *QTreeModel::internalMimeData() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK10QTreeModel16internalMimeDataEv(
    const QTreeModel *self) {
  return self->internalMimeData();
}

//  QModelIndex QTreeModel::createIndexFromItem(int row, int col,
//      QTreeWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK10QTreeModel19createIndexFromItemEiiP15QTreeWidgetItem(
    const QTreeModel *self,
    int row,
    int col,
    QTreeWidgetItem *item) {
  return new QModelIndex(self->createIndexFromItem(row, col, item));
}

//  void QTreeModel::beginInsertItems(QTreeWidgetItem *parent, int row, int
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModel16beginInsertItemsEP15QTreeWidgetItemii(
    QTreeModel *self,
    QTreeWidgetItem *parent,
    int row,
    int count) {
  self->beginInsertItems(parent, row, count);
}

//  void QTreeModel::endInsertItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModel14endInsertItemsEv(QTreeModel *self) {
  self->endInsertItems();
}

//  void QTreeModel::beginRemoveItems(QTreeWidgetItem *parent, int row, int
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModel16beginRemoveItemsEP15QTreeWidgetItemii(
    QTreeModel *self,
    QTreeWidgetItem *parent,
    int row,
    int count) {
  self->beginRemoveItems(parent, row, count);
}

//  void QTreeModel::endRemoveItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModel14endRemoveItemsEv(QTreeModel *self) {
  self->endRemoveItems();
}

//  void QTreeModel::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTreeModel10timerEventEP11QTimerEvent(
    QTreeModel *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  bool QTreeModel::executePendingSort() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTreeModel18executePendingSortEv(const QTreeModel *self) {
  return self->executePendingSort();
}

//  bool QTreeModel::isChanging() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTreeModel10isChangingEv(const QTreeModel *self) {
  return self->isChanging();
}

//  QTreeModelPrivate *QTreeModel::d_func()
extern "C" Q_DECL_EXPORT
QTreeModelPrivate *ritual_ZN10QTreeModel6d_funcEv(QTreeModel *self) {
  return self->d_func();
}

//  const QTreeModelPrivate *QTreeModel::d_func() const
extern "C" Q_DECL_EXPORT
const QTreeModelPrivate *ritual_ZNK10QTreeModel6d_funcEv(
    const QTreeModel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTreeModel, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTreeModel(QTreeModel *self, const char *key, void *call) {
  return static_cast<CuteQTreeModel *>(self)->take(key, call);
}

//  QModelIndex QTreeModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK10QTreeModel5indexEiiRK11QModelIndex(
    const QTreeModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->QTreeModel::index(row, column, *parent));
}

//  QModelIndex QTreeModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK10QTreeModel6parentERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->QTreeModel::parent(*child));
}

//  int QTreeModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTreeModel8rowCountERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *parent) {
  return self->QTreeModel::rowCount(*parent);
}

//  int QTreeModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTreeModel11columnCountERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *parent) {
  return self->QTreeModel::columnCount(*parent);
}

//  bool QTreeModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QTreeModel11hasChildrenERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *parent) {
  return self->QTreeModel::hasChildren(*parent);
}

//  QVariant QTreeModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK10QTreeModel4dataERK11QModelIndexi(
    const QTreeModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QTreeModel::data(*index, role));
}

//  bool QTreeModel::setData(const QModelIndex &index, const QVariant &value,
//      int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QTreeModel7setDataERK11QModelIndexRK8QVarianti(
    QTreeModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QTreeModel::setData(*index, *value, role);
}

//  bool QTreeModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QTreeModel13clearItemDataERK11QModelIndex(
    QTreeModel *self,
    const QModelIndex *index) {
  return self->QTreeModel::clearItemData(*index);
}

//  QVariant QTreeModel::headerData(int section, Qt::Orientation orientation,
//      int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK10QTreeModel10headerDataEiN2Qt11OrientationEi(
    const QTreeModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QTreeModel::headerData(
          section,
          orientation,
          role));
}

//  bool QTreeModel::setHeaderData(int section, Qt::Orientation orientation,
//      const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QTreeModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QTreeModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->QTreeModel::setHeaderData(section, orientation, *value, role);
}

//  Qt::ItemFlags QTreeModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTreeModel5flagsERK11QModelIndex(
    const QTreeModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QTreeModel::flags(*index).toInt());
}

//  void QTreeModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTreeModel4sortEiN2Qt9SortOrderE(
    QTreeModel *self,
    int column,
    Qt::SortOrder order) {
  self->QTreeModel::sort(column, order);
}

//  bool QTreeModel::insertRows(int row, int count, const QModelIndex &a2)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QTreeModel10insertRowsEiiRK11QModelIndex(
    QTreeModel *self,
    int row,
    int count,
    const QModelIndex *a2) {
  return self->QTreeModel::insertRows(row, count, *a2);
}

//  bool QTreeModel::insertColumns(int column, int count, const QModelIndex
//      &a2)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QTreeModel13insertColumnsEiiRK11QModelIndex(
    QTreeModel *self,
    int column,
    int count,
    const QModelIndex *a2) {
  return self->QTreeModel::insertColumns(column, count, *a2);
}

//  bool QTreeModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QTreeModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QTreeModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QTreeModel::dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QTreeModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTreeModel20supportedDropActionsEv(
    const QTreeModel *self) {
  return static_cast<int>(self->QTreeModel::supportedDropActions().toInt());
}

//  Qt::DropActions QTreeModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTreeModel20supportedDragActionsEv(
    const QTreeModel *self) {
  return static_cast<int>(self->QTreeModel::supportedDragActions().toInt());
}

//  void QTreeModel::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTreeModel10timerEventEP11QTimerEvent(
    QTreeModel *self,
    QTimerEvent *a0) {
  static_cast<OwnQTreeModel *>(self)->OwnQTreeModel::timerEvent(a0);
}

#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(treewidget)
