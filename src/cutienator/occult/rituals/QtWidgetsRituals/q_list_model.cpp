//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include "qlistwidget.h"
#include <private/qlistview_p.h>
#include <private/qwidgetitemdata_p.h>
#include <private/qlistwidget_p.h>
#include <algorithm>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/itemviews/qlistwidget.cpp, line 379, as _ZN10QListModel23sortedInsertionIteratorERKN5QListIP15QListWidgetItemE8iteratorES6_N2Qt9SortOrderES2_
inline QList<QListWidgetItem*>::iterator QListModel::sortedInsertionIterator(
    const QList<QListWidgetItem*>::iterator &begin,
    const QList<QListWidgetItem*>::iterator &end,
    Qt::SortOrder order, QListWidgetItem *item)
{
    if (order == Qt::AscendingOrder)
        return std::lower_bound(begin, end, item, QListModelLessThan());
    return std::lower_bound(begin, end, item, QListModelGreaterThan());
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 367, as _ZN10QListModel12itemLessThanERKSt4pairIP15QListWidgetItemiES5_
inline bool QListModel::itemLessThan(const std::pair<QListWidgetItem*,int> &left,
                              const std::pair<QListWidgetItem*,int> &right)
{
    return (*left.first) < (*right.first);
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 373, as _ZN10QListModel15itemGreaterThanERKSt4pairIP15QListWidgetItemiES5_
inline bool QListModel::itemGreaterThan(const std::pair<QListWidgetItem*,int> &left,
                                 const std::pair<QListWidgetItem*,int> &right)
{
    return (*right.first) < (*left.first);
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 31, as _ZN10QListModelD1Ev
inline QListModel::~QListModel()
{
    clear();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 36, as _ZN10QListModel5clearEv
inline void QListModel::clear()
{
    beginResetModel();
    for (int i = 0; i < items.size(); ++i) {
        if (items.at(i)) {
            items.at(i)->d->theid = -1;
            items.at(i)->view = nullptr;
            delete items.at(i);
        }
    }
    items.clear();
    endResetModel();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 50, as _ZNK10QListModel2atEi
inline QListWidgetItem *QListModel::at(int row) const
{
    return items.value(row);
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 68, as _ZN10QListModel6insertEiP15QListWidgetItem
inline void QListModel::insert(int row, QListWidgetItem *item)
{
    if (!item)
        return;

    item->view = this->view();
    if (item->view && item->view->isSortingEnabled()) {
        // sorted insertion
        QList<QListWidgetItem*>::iterator it;
        it = sortedInsertionIterator(items.begin(), items.end(),
                                     item->view->sortOrder(), item);
        row = qMax<qsizetype>(it - items.begin(), 0);
    } else {
        if (row < 0)
            row = 0;
        else if (row > items.size())
            row = items.size();
    }
    beginInsertRows(QModelIndex(), row, row);
    items.insert(row, item);
    item->d->theid = row;
    endInsertRows();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 92, as _ZN10QListModel6insertEiRK5QListI7QStringE
inline void QListModel::insert(int row, const QStringList &labels)
{
    const int count = labels.size();
    if (count <= 0)
        return;
    QListWidget *view = this->view();
    if (view && view->isSortingEnabled()) {
        // sorted insertion
        for (int i = 0; i < count; ++i) {
            QListWidgetItem *item = new QListWidgetItem(labels.at(i));
            insert(row, item);
        }
    } else {
        if (row < 0)
            row = 0;
        else if (row > items.size())
            row = items.size();
        beginInsertRows(QModelIndex(), row, row + count - 1);
        for (int i = 0; i < count; ++i) {
            QListWidgetItem *item = new QListWidgetItem(labels.at(i));
            item->d->theid = row;
            item->view = this->view();
            items.insert(row++, item);
        }
        endInsertRows();
    }
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 55, as _ZN10QListModel6removeEP15QListWidgetItem
inline void QListModel::remove(QListWidgetItem *item)
{
    if (!item)
        return;
    int row = items.indexOf(item); // ### use index(item) - it's faster
    Q_ASSERT(row != -1);
    beginRemoveRows(QModelIndex(), row, row);
    items.at(row)->d->theid = -1;
    items.at(row)->view = nullptr;
    items.removeAt(row);
    endRemoveRows();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 120, as _ZN10QListModel4takeEi
inline QListWidgetItem *QListModel::take(int row)
{
    if (row < 0 || row >= items.size())
        return nullptr;

    beginRemoveRows(QModelIndex(), row, row);
    items.at(row)->d->theid = -1;
    items.at(row)->view = nullptr;
    QListWidgetItem *item = items.takeAt(row);
    endRemoveRows();
    return item;
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 133, as _ZN10QListModel4moveEii
inline void QListModel::move(int srcRow, int dstRow)
{
    if (srcRow == dstRow
        || srcRow < 0 || srcRow >= items.size()
        || dstRow < 0 || dstRow > items.size())
        return;

    if (!beginMoveRows(QModelIndex(), srcRow, srcRow, QModelIndex(), dstRow))
        return;
    if (srcRow < dstRow)
        --dstRow;
    items.move(srcRow, dstRow);
    endMoveRows();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 148, as _ZNK10QListModel8rowCountERK11QModelIndex
inline int QListModel::rowCount(const QModelIndex &parent) const
{
    return parent.isValid() ? 0 : items.size();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 153, as _ZNK10QListModel5indexEPK15QListWidgetItem
inline QModelIndex QListModel::index(const QListWidgetItem *item_) const
{
    QListWidgetItem *item = const_cast<QListWidgetItem *>(item_);
    if (!item || !item->view || static_cast<const QListModel *>(item->view->model()) != this
        || items.isEmpty())
        return QModelIndex();
    int row;
    const int theid = item->d->theid;
    if (theid >= 0 && theid < items.size() && items.at(theid) == item) {
        row = theid;
    } else { // we need to search for the item
        row = items.lastIndexOf(item);  // lastIndexOf is an optimization in favor of indexOf
        if (row == -1) // not found
            return QModelIndex();
        item->d->theid = row;
    }
    return createIndex(row, 0, item);
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 172, as _ZNK10QListModel5indexEiiRK11QModelIndex
inline QModelIndex QListModel::index(int row, int column, const QModelIndex &parent) const
{
    if (hasIndex(row, column, parent))
        return createIndex(row, column, items.at(row));
    return QModelIndex();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 179, as _ZNK10QListModel4dataERK11QModelIndexi
inline QVariant QListModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid() || index.row() >= items.size())
        return QVariant();
    return items.at(index.row())->data(role);
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 186, as _ZN10QListModel7setDataERK11QModelIndexRK8QVarianti
inline bool QListModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (!index.isValid() || index.row() >= items.size())
        return false;
    items.at(index.row())->setData(role, value);
    return true;
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 194, as _ZN10QListModel13clearItemDataERK11QModelIndex
inline bool QListModel::clearItemData(const QModelIndex &index)
{
    if (!checkIndex(index, CheckIndexOption::IndexIsValid))
        return false;
    QListWidgetItem *item = items.at(index.row());
    const auto beginIter = item->d->values.cbegin();
    const auto endIter = item->d->values.cend();
    if (std::all_of(beginIter, endIter, [](const QWidgetItemData& data) -> bool { return !data.value.isValid(); }))
        return true; //it's already cleared
    item->d->values.clear();
    emit dataChanged(index, index, QList<int> {});
    return true;
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 208, as _ZNK10QListModel8itemDataERK11QModelIndex
inline QMap<int, QVariant> QListModel::itemData(const QModelIndex &index) const
{
    QMap<int, QVariant> roles;
    if (!index.isValid() || index.row() >= items.size())
        return roles;
    QListWidgetItem *itm = items.at(index.row());
    for (int i = 0; i < itm->d->values.size(); ++i) {
        roles.insert(itm->d->values.at(i).role,
                     itm->d->values.at(i).value);
    }
    return roles;
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 221, as _ZN10QListModel10insertRowsEiiRK11QModelIndex
inline bool QListModel::insertRows(int row, int count, const QModelIndex &parent)
{
    if (count < 1 || row < 0 || row > rowCount() || parent.isValid())
        return false;

    beginInsertRows(QModelIndex(), row, row + count - 1);
    QListWidget *view = this->view();
    QListWidgetItem *itm = nullptr;

    for (int r = row; r < row + count; ++r) {
        itm = new QListWidgetItem;
        itm->view = view;
        itm->d->theid = r;
        items.insert(r, itm);
    }

    endInsertRows();
    return true;
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 241, as _ZN10QListModel10removeRowsEiiRK11QModelIndex
inline bool QListModel::removeRows(int row, int count, const QModelIndex &parent)
{
    if (count < 1 || row < 0 || (row + count) > rowCount() || parent.isValid())
        return false;

    beginRemoveRows(QModelIndex(), row, row + count - 1);
    QListWidgetItem *itm = nullptr;
    for (int r = row; r < row + count; ++r) {
        itm = items.takeAt(row);
        itm->view = nullptr;
        itm->d->theid = -1;
        delete itm;
    }
    endRemoveRows();
    return true;
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 268, as _ZN10QListModel8moveRowsERK11QModelIndexiiS2_i
inline bool QListModel::moveRows(const QModelIndex &sourceParent, int sourceRow, int count, const QModelIndex &destinationParent, int destinationChild)
{
    if (sourceRow < 0
        || sourceRow + count - 1 >= rowCount(sourceParent)
        || destinationChild < 0
        || destinationChild > rowCount(destinationParent)
        || sourceRow == destinationChild
        || sourceRow == destinationChild - 1
        || count <= 0
        || sourceParent.isValid()
        || destinationParent.isValid()) {
        return false;
    }
    if (!beginMoveRows(QModelIndex(), sourceRow, sourceRow + count - 1, QModelIndex(), destinationChild))
        return false;

    int fromRow = sourceRow;
    if (destinationChild < sourceRow)
        fromRow += count - 1;
    else
        destinationChild--;
    while (count--)
        items.move(fromRow, destinationChild);
    endMoveRows();
    return true;
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 295, as _ZNK10QListModel5flagsERK11QModelIndex
inline Qt::ItemFlags QListModel::flags(const QModelIndex &index) const
{
    if (!index.isValid() || index.row() >= items.size() || index.model() != this)
        return Qt::ItemIsDropEnabled; // we allow drops outside the items
    return items.at(index.row())->flags();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 302, as _ZN10QListModel4sortEiN2Qt9SortOrderE
inline void QListModel::sort(int column, Qt::SortOrder order)
{
    if (column != 0)
        return;

    emit layoutAboutToBeChanged({}, QAbstractItemModel::VerticalSortHint);

    QList<std::pair<QListWidgetItem *, int>> sorting(items.size());
    for (int i = 0; i < items.size(); ++i) {
        QListWidgetItem *item = items.at(i);
        sorting[i].first = item;
        sorting[i].second = i;
    }

    const auto compare = (order == Qt::AscendingOrder ? &itemLessThan : &itemGreaterThan);
    std::stable_sort(sorting.begin(), sorting.end(), compare);
    QModelIndexList fromIndexes;
    QModelIndexList toIndexes;
    const int sortingCount = sorting.size();
    fromIndexes.reserve(sortingCount);
    toIndexes.reserve(sortingCount);
    for (int r = 0; r < sortingCount; ++r) {
        QListWidgetItem *item = sorting.at(r).first;
        toIndexes.append(createIndex(r, 0, item));
        fromIndexes.append(createIndex(sorting.at(r).second, 0, sorting.at(r).first));
        items[r] = sorting.at(r).first;
    }
    changePersistentIndexList(fromIndexes, toIndexes);

    emit layoutChanged({}, QAbstractItemModel::VerticalSortHint);
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 338, as _ZN10QListModel12ensureSortedEiN2Qt9SortOrderEii
inline void QListModel::ensureSorted(int column, Qt::SortOrder order, int start, int end)
{
    if (column != 0)
        return;

    const auto compareLt = [](const QListWidgetItem *left, const QListWidgetItem *right) -> bool {
        return *left < *right;
    };

    const auto compareGt = [](const QListWidgetItem *left, const QListWidgetItem *right) -> bool {
        return *right < *left;
    };

    /** Check if range [start,end] is already in sorted position in list.
     *  Take for this the assumption, that outside [start,end] the list
     *  is already sorted. Therefore the sorted check has to be extended
     *  to the first element that is known to be sorted before the range
     *  [start, end], which is (start-1) and the first element after the
     *  range [start, end], which is (end+2) due to end being included.
    */
    const auto beginChangedIterator = items.constBegin() + qMax(start - 1, 0);
    const auto endChangedIterator = items.constBegin() + qMin(end + 2, items.size());
    const bool needsSorting = !std::is_sorted(beginChangedIterator, endChangedIterator,
                                              order == Qt::AscendingOrder ? compareLt : compareGt);

    if (needsSorting)
        sort(column, order);
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 395, as _ZNK10QListModel9mimeTypesEv
inline QStringList QListModel::mimeTypes() const
{
    const QListWidget *view = this->view();
    if (view)
        return view->mimeTypes();
    return {};
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 408, as _ZNK10QListModel8mimeDataERK5QListI11QModelIndexE
inline QMimeData *QListModel::mimeData(const QModelIndexList &indexes) const
{
    QList<QListWidgetItem*> itemlist;
    const int indexesCount = indexes.size();
    itemlist.reserve(indexesCount);
    for (int i = 0; i < indexesCount; ++i)
        itemlist << at(indexes.at(i).row());

    cachedIndexes = indexes;
    QMimeData *mimeData = view()->mimeData(itemlist);
    cachedIndexes.clear();
    return mimeData;
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 423, as _ZN10QListModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex
inline bool QListModel::dropMimeData(const QMimeData *data, Qt::DropAction action,
                              int row, int column, const QModelIndex &index)
{
    Q_UNUSED(column);
    if (index.isValid())
        row = index.row();
    else if (row == -1)
        row = items.size();

    return view()->dropMimeData(row, data, action);
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 435, as _ZNK10QListModel20supportedDropActionsEv
inline Qt::DropActions QListModel::supportedDropActions() const
{
    return view()->supportedDropActions();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 440, as _ZNK10QListModel20supportedDragActionsEv
inline Qt::DropActions QListModel::supportedDragActions() const
{
    return view()->supportedDragActions();
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 403, as _ZNK10QListModel16internalMimeDataEv
inline QMimeData *QListModel::internalMimeData()  const
{
    return QAbstractItemModel::mimeData(cachedIndexes);
}
//  -----------------------------------------------------------------------

//  A QListModel that Python can take functions over in. Every QListModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQListModelCall0)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQListModelCall1)(const void *, int, int, const QModelIndex *, int *);
typedef const QVariant * (*CuteQListModelCall2)(const void *, const QModelIndex *, int, int *);
typedef bool (*CuteQListModelCall3)(const void *, const QModelIndex *, const QVariant *, int, int *);
typedef bool (*CuteQListModelCall4)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQListModelCall5)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQListModelCall6)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQListModelCall7)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef int (*CuteQListModelCall8)(const void *, const QModelIndex *, int *);
typedef void (*CuteQListModelCall9)(const void *, int, int, int *);
typedef bool (*CuteQListModelCall10)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef int (*CuteQListModelCall11)(const void *, int *);
typedef int (*CuteQListModelCall12)(const void *, int *);
typedef const QModelIndex * (*CuteQListModelCall13)(const void *, int, int, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQListModelCall14)(const void *, const QModelIndex *, int *);
typedef int (*CuteQListModelCall15)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQListModelCall16)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQListModelCall17)(const void *, int, int, int, int *);
typedef bool (*CuteQListModelCall18)(const void *, int, int, const QVariant *, int, int *);
typedef bool (*CuteQListModelCall19)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef bool (*CuteQListModelCall20)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQListModelCall21)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQListModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteQListModelCall23)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQListModelCall24)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQListModelCall25)(const void *, const QModelIndex *, int *);
typedef const QSize * (*CuteQListModelCall26)(const void *, const QModelIndex *, int *);
typedef void (*CuteQListModelCall27)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
typedef bool (*CuteQListModelCall28)(const void *, int *);
typedef void (*CuteQListModelCall29)(const void *, int *);
typedef void (*CuteQListModelCall30)(const void *, int *);
typedef bool (*CuteQListModelCall31)(const void *, QEvent *, int *);
typedef bool (*CuteQListModelCall32)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQListModelCall33)(const void *, QTimerEvent *, int *);
typedef void (*CuteQListModelCall34)(const void *, QChildEvent *, int *);
typedef void (*CuteQListModelCall35)(const void *, QEvent *, int *);
typedef void (*CuteQListModelCall36)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQListModelCall37)(const void *, const QMetaMethod *, int *);
class CuteQListModel : public QListModel {
public:
  using QListModel::QListModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[37] = call;
      return true;
    }
    return false;
  }

  //  int QListModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQListModelCall0 call = reinterpret_cast<CuteQListModelCall0>(taken[0]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QListModel::rowCount(parent);
  }

  //  QModelIndex QListModel::index(int row, int column, const QModelIndex
  //      &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQListModelCall1 call = reinterpret_cast<CuteQListModelCall1>(taken[1]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QListModel::index(row, column, parent);
  }

  //  QVariant QListModel::data(const QModelIndex &index, int role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQListModelCall2 call = reinterpret_cast<CuteQListModelCall2>(taken[2]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QListModel::data(index, role);
  }

  //  bool QListModel::setData(const QModelIndex &index, const QVariant
  //      &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[3]) {
      int handled = 0;
      CuteQListModelCall3 call = reinterpret_cast<CuteQListModelCall3>(taken[3]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QListModel::setData(index, value, role);
  }

  //  bool QListModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[4]) {
      int handled = 0;
      CuteQListModelCall4 call = reinterpret_cast<CuteQListModelCall4>(taken[4]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QListModel::clearItemData(index);
  }

  //  bool QListModel::insertRows(int row, int count, const QModelIndex
  //      &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[5]) {
      int handled = 0;
      CuteQListModelCall5 call = reinterpret_cast<CuteQListModelCall5>(taken[5]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QListModel::insertRows(row, count, parent);
  }

  //  bool QListModel::removeRows(int row, int count, const QModelIndex
  //      &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[6]) {
      int handled = 0;
      CuteQListModelCall6 call = reinterpret_cast<CuteQListModelCall6>(taken[6]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QListModel::removeRows(row, count, parent);
  }

  //  bool QListModel::moveRows(const QModelIndex &sourceParent, int
  //      sourceRow, int count, const QModelIndex &destinationParent, int
  //      destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[7]) {
      int handled = 0;
      CuteQListModelCall7 call = reinterpret_cast<CuteQListModelCall7>(taken[7]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QListModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }

  //  Qt::ItemFlags QListModel::flags(const QModelIndex &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQListModelCall8 call = reinterpret_cast<CuteQListModelCall8>(taken[8]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QListModel::flags(index);
  }

  //  void QListModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[9]) {
      int handled = 0;
      CuteQListModelCall9 call = reinterpret_cast<CuteQListModelCall9>(taken[9]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QListModel::sort(column, order);
  }

  //  bool QListModel::dropMimeData(const QMimeData *data, Qt::DropAction
  //      action, int row, int column, const QModelIndex &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[10]) {
      int handled = 0;
      CuteQListModelCall10 call = reinterpret_cast<CuteQListModelCall10>(taken[10]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QListModel::dropMimeData(data, action, row, column, parent);
  }

  //  Qt::DropActions QListModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQListModelCall11 call = reinterpret_cast<CuteQListModelCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QListModel::supportedDropActions();
  }

  //  Qt::DropActions QListModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQListModelCall12 call = reinterpret_cast<CuteQListModelCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QListModel::supportedDragActions();
  }

  //  QModelIndex QAbstractListModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQListModelCall13 call = reinterpret_cast<CuteQListModelCall13>(taken[13]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractListModel::sibling(row, column, idx);
  }

  //  QModelIndex QAbstractListModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQListModelCall14 call = reinterpret_cast<CuteQListModelCall14>(taken[14]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QAbstractListModel::parent(child);
  }

  //  int QAbstractListModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQListModelCall15 call = reinterpret_cast<CuteQListModelCall15>(taken[15]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractListModel::columnCount(parent);
  }

  //  bool QAbstractListModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQListModelCall16 call = reinterpret_cast<CuteQListModelCall16>(taken[16]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractListModel::hasChildren(parent);
  }

  //  QVariant QAbstractItemModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQListModelCall17 call = reinterpret_cast<CuteQListModelCall17>(taken[17]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::headerData(section, orientation, role);
  }

  //  bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[18]) {
      int handled = 0;
      CuteQListModelCall18 call = reinterpret_cast<CuteQListModelCall18>(taken[18]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }

  //  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQListModelCall19 call = reinterpret_cast<CuteQListModelCall19>(taken[19]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }

  //  bool QAbstractItemModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[20]) {
      int handled = 0;
      CuteQListModelCall20 call = reinterpret_cast<CuteQListModelCall20>(taken[20]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertColumns(column, count, parent);
  }

  //  bool QAbstractItemModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[21]) {
      int handled = 0;
      CuteQListModelCall21 call = reinterpret_cast<CuteQListModelCall21>(taken[21]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeColumns(column, count, parent);
  }

  //  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent,
  //      int sourceColumn, int count, const QModelIndex
  //      &destinationParent, int destinationChild)
  bool moveColumns(
      const QModelIndex &sourceParent,
      int sourceColumn,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[22]) {
      int handled = 0;
      CuteQListModelCall22 call = reinterpret_cast<CuteQListModelCall22>(taken[22]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }

  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[23]) {
      int handled = 0;
      CuteQListModelCall23 call = reinterpret_cast<CuteQListModelCall23>(taken[23]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractItemModel::fetchMore(parent);
  }

  //  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQListModelCall24 call = reinterpret_cast<CuteQListModelCall24>(taken[24]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }

  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQListModelCall25 call = reinterpret_cast<CuteQListModelCall25>(taken[25]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }

  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQListModelCall26 call = reinterpret_cast<CuteQListModelCall26>(taken[26]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::span(index);
  }

  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQListModelCall27 call = reinterpret_cast<CuteQListModelCall27>(taken[27]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }

  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[28]) {
      int handled = 0;
      CuteQListModelCall28 call = reinterpret_cast<CuteQListModelCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }

  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[29]) {
      int handled = 0;
      CuteQListModelCall29 call = reinterpret_cast<CuteQListModelCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }

  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[30]) {
      int handled = 0;
      CuteQListModelCall30 call = reinterpret_cast<CuteQListModelCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQListModelCall31 call = reinterpret_cast<CuteQListModelCall31>(taken[31]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQListModelCall32 call = reinterpret_cast<CuteQListModelCall32>(taken[32]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQListModelCall33 call = reinterpret_cast<CuteQListModelCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQListModelCall34 call = reinterpret_cast<CuteQListModelCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQListModelCall35 call = reinterpret_cast<CuteQListModelCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[36]) {
      int handled = 0;
      CuteQListModelCall36 call = reinterpret_cast<CuteQListModelCall36>(taken[36]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[37]) {
      int handled = 0;
      CuteQListModelCall37 call = reinterpret_cast<CuteQListModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QListModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QListModel10metaObjectEv(
    const QListModel *self) {
  return self->metaObject();
}

//  QListModel::~QListModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QListModelD1Ev(QListModel *self) {
  delete self;
}

//  QListWidget *QListModel::view() const
extern "C" Q_DECL_EXPORT
QListWidget *ritual_ZNK10QListModel4viewEv(const QListModel *self) {
  return self->view();
}

//  void QListModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QListModel5clearEv(QListModel *self) {
  self->clear();
}

//  QListWidgetItem *QListModel::at(int row) const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK10QListModel2atEi(
    const QListModel *self,
    int row) {
  return self->at(row);
}

//  void QListModel::insert(int row, QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QListModel6insertEiP15QListWidgetItem(
    QListModel *self,
    int row,
    QListWidgetItem *item) {
  self->insert(row, item);
}

//  void QListModel::insert(int row, const QStringList &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QListModel6insertEiRK5QListI7QStringE(
    QListModel *self,
    int row,
    const QList<QString> *items) {
  self->insert(row, *items);
}

//  void QListModel::remove(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QListModel6removeEP15QListWidgetItem(
    QListModel *self,
    QListWidgetItem *item) {
  self->remove(item);
}

//  QListWidgetItem *QListModel::take(int row)
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZN10QListModel4takeEi(QListModel *self, int row) {
  return self->take(row);
}

//  void QListModel::move(int srcRow, int dstRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QListModel4moveEii(
    QListModel *self,
    int srcRow,
    int dstRow) {
  self->move(srcRow, dstRow);
}

//  int QListModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QListModel8rowCountERK11QModelIndex(
    const QListModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QModelIndex QListModel::index(const QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK10QListModel5indexEPK15QListWidgetItem(
    const QListModel *self,
    const QListWidgetItem *item) {
  return new QModelIndex(self->index(item));
}

//  QModelIndex QListModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK10QListModel5indexEiiRK11QModelIndex(
    const QListModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QVariant QListModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QListModel4dataERK11QModelIndexi(
    const QListModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QListModel::setData(const QModelIndex &index, const QVariant &value,
//      int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QListModel7setDataERK11QModelIndexRK8QVarianti(
    QListModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QListModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QListModel13clearItemDataERK11QModelIndex(
    QListModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  QMap<int, QVariant> QListModel::itemData(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK10QListModel8itemDataERK11QModelIndex(
    const QListModel *self,
    const QModelIndex *index) {
  return new QMap<int, QVariant>(self->itemData(*index));
}

//  bool QListModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QListModel10insertRowsEiiRK11QModelIndex(
    QListModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QListModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QListModel10removeRowsEiiRK11QModelIndex(
    QListModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QListModel::moveRows(const QModelIndex &sourceParent, int sourceRow,
//      int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QListModel8moveRowsERK11QModelIndexiiS2_i(
    QListModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  Qt::ItemFlags QListModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QListModel5flagsERK11QModelIndex(
    const QListModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  void QListModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QListModel4sortEiN2Qt9SortOrderE(
    QListModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  void QListModel::ensureSorted(int column, Qt::SortOrder order, int start,
//      int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QListModel12ensureSortedEiN2Qt9SortOrderEii(
    QListModel *self,
    int column,
    Qt::SortOrder order,
    int start,
    int end) {
  self->ensureSorted(column, order, start, end);
}

//  QStringList QListModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QListModel9mimeTypesEv(const QListModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QListModel::mimeData(const QModelIndexList &indexes) const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK10QListModel8mimeDataERK5QListI11QModelIndexE(
    const QListModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  bool QListModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QListModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QListModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QListModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QListModel20supportedDropActionsEv(const QListModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  Qt::DropActions QListModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QListModel20supportedDragActionsEv(const QListModel *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  QMimeData *QListModel::internalMimeData() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK10QListModel16internalMimeDataEv(
    const QListModel *self) {
  return self->internalMimeData();
}

//  a Python function taken by a CuteQListModel, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QListModel(QListModel *self, const char *key, void *call) {
  return static_cast<CuteQListModel *>(self)->take(key, call);
}

//  int QListModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QListModel8rowCountERK11QModelIndex(
    const QListModel *self,
    const QModelIndex *parent) {
  return self->QListModel::rowCount(*parent);
}

//  QModelIndex QListModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK10QListModel5indexEiiRK11QModelIndex(
    const QListModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->QListModel::index(row, column, *parent));
}

//  QVariant QListModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK10QListModel4dataERK11QModelIndexi(
    const QListModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QListModel::data(*index, role));
}

//  bool QListModel::setData(const QModelIndex &index, const QVariant &value,
//      int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QListModel7setDataERK11QModelIndexRK8QVarianti(
    QListModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QListModel::setData(*index, *value, role);
}

//  bool QListModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QListModel13clearItemDataERK11QModelIndex(
    QListModel *self,
    const QModelIndex *index) {
  return self->QListModel::clearItemData(*index);
}

//  bool QListModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QListModel10insertRowsEiiRK11QModelIndex(
    QListModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QListModel::insertRows(row, count, *parent);
}

//  bool QListModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QListModel10removeRowsEiiRK11QModelIndex(
    QListModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QListModel::removeRows(row, count, *parent);
}

//  bool QListModel::moveRows(const QModelIndex &sourceParent, int sourceRow,
//      int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QListModel8moveRowsERK11QModelIndexiiS2_i(
    QListModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->QListModel::moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  Qt::ItemFlags QListModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QListModel5flagsERK11QModelIndex(
    const QListModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QListModel::flags(*index).toInt());
}

//  void QListModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QListModel4sortEiN2Qt9SortOrderE(
    QListModel *self,
    int column,
    Qt::SortOrder order) {
  self->QListModel::sort(column, order);
}

//  bool QListModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QListModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QListModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QListModel::dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QListModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QListModel20supportedDropActionsEv(
    const QListModel *self) {
  return static_cast<int>(self->QListModel::supportedDropActions().toInt());
}

//  Qt::DropActions QListModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QListModel20supportedDragActionsEv(
    const QListModel *self) {
  return static_cast<int>(self->QListModel::supportedDragActions().toInt());
}
