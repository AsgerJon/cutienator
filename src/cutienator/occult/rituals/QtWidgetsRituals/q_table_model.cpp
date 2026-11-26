//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QTableModel' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tablewidget)
#if QT_CONFIG(tablewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtWidgets/qtablewidget.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtCore/QList>
#include <QtWidgets/QTableWidgetItem>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWidgets/qtablewidget.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/private/qtablewidget_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtWidgets__QTableModel.cpp, line 1, as moc:QTableModel
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN11QTableModelE_t {};
} // unnamed namespace

template <> constexpr inline auto QTableModel::qt_create_metaobjectdata<qt_meta_tag_ZN11QTableModelE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QTableModel"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QTableModel, qt_meta_tag_ZN11QTableModelE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QTableModel::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstractTableModel::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN11QTableModelE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN11QTableModelE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN11QTableModelE_t>.metaTypes,
    nullptr
} };

void QTableModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QTableModel *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QTableModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QTableModel::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN11QTableModelE_t>.strings))
        return static_cast<void*>(this);
    return QAbstractTableModel::qt_metacast(_clname);
}

int QTableModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractTableModel::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from src/widgets/itemviews/qtablewidget.cpp, line 28, as _ZN11QTableModel10insertRowsEiiRK11QModelIndex
inline bool QTableModel::insertRows(int row, int count, const QModelIndex &)
{
    if (count < 1 || row < 0 || row > verticalHeaderItems.size())
        return false;

    beginInsertRows(QModelIndex(), row, row + count - 1);
    int rc = verticalHeaderItems.size();
    int cc = horizontalHeaderItems.size();
    verticalHeaderItems.insert(row, count, 0);
    if (rc == 0)
        tableItems.resize(cc * count);
    else
        tableItems.insert(tableIndex(row, 0), cc * count, 0);
    endInsertRows();
    return true;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 63, as _ZN11QTableModel10removeRowsEiiRK11QModelIndex
inline bool QTableModel::removeRows(int row, int count, const QModelIndex &)
{
    if (count < 1 || row < 0 || row + count > verticalHeaderItems.size())
        return false;

    beginRemoveRows(QModelIndex(), row, row + count - 1);
    int i = tableIndex(row, 0);
    int n = count * columnCount();
    QTableWidgetItem *oldItem = nullptr;
    for (int j = i; j < n + i; ++j) {
        oldItem = tableItems.at(j);
        if (oldItem)
            oldItem->view = nullptr;
        delete oldItem;
    }
    tableItems.remove(qMax(i, 0), n);
    for (int v = row; v < row + count; ++v) {
        oldItem = verticalHeaderItems.at(v);
        if (oldItem)
            oldItem->view = nullptr;
        delete oldItem;
    }
    verticalHeaderItems.remove(row, count);
    endRemoveRows();
    return true;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 433, as _ZN11QTableModel11setItemDataERK11QModelIndexRK4QMapIi8QVariantE
inline bool QTableModel::setItemData(const QModelIndex &index, const QMap<int, QVariant> &roles)
{
    if (!index.isValid())
        return false;

    QTableWidget *view = this->view();
    QTableWidgetItem *itm = item(index);
    if (itm) {
        itm->view = nullptr; // prohibits item from calling itemChanged()
        QList<int> rolesVec;
        for (QMap<int, QVariant>::ConstIterator it = roles.constBegin(); it != roles.constEnd(); ++it) {
            const int role = (it.key() == Qt::EditRole ? Qt::DisplayRole : it.key());
            if (itm->data(role) != it.value()) {
                itm->setData(role, it.value());
                rolesVec += role;
                if (role == Qt::DisplayRole)
                    rolesVec += Qt::EditRole;
            }
        }
        itm->view = view;
        if (!rolesVec.isEmpty())
            itemChanged(itm, rolesVec);
        return true;
    }

    if (!view)
        return false;

    itm = createItem();
    for (QMap<int, QVariant>::ConstIterator it = roles.constBegin(); it != roles.constEnd(); ++it)
        itm->setData(it.key(), it.value());
    view->setItem(index.row(), index.column(), itm);
    return true;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 849, as _ZN11QTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex
inline bool QTableModel::dropMimeData(const QMimeData *data, Qt::DropAction action,
                              int row , int column, const QModelIndex &index)
{
    if (index.isValid()) {
        row = index.row();
        column = index.column();
    } else if (row == -1 || column == -1) { // The user dropped outside the table.
        row = rowCount();
        column = 0;
    } else { // The user dropped between two rows
        // This means inserting a row, which only makes sense at column 0
        column = 0;
    }

    QTableWidget *view = this->view();
    return (view ? view->dropMimeData(row, column, data, action) : false);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 468, as _ZN11QTableModel13clearItemDataERK11QModelIndex
inline bool QTableModel::clearItemData(const QModelIndex &index)
{
    if (!checkIndex(index, CheckIndexOption::IndexIsValid))
        return false;
    QTableWidgetItem *itm = item(index);
    if (!itm)
        return false;
    const auto beginIter = itm->values.cbegin();
    const auto endIter = itm->values.cend();
    if (std::all_of(beginIter, endIter, [](const QWidgetItemData& data) -> bool { return !data.value.isValid(); }))
        return true; //it's already cleared
    itm->values.clear();
    emit dataChanged(index, index, QList<int> {});
    return true;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 45, as _ZN11QTableModel13insertColumnsEiiRK11QModelIndex
inline bool QTableModel::insertColumns(int column, int count, const QModelIndex &)
{
    if (count < 1 || column < 0 || column > horizontalHeaderItems.size())
        return false;

    beginInsertColumns(QModelIndex(), column, column + count - 1);
    int rc = verticalHeaderItems.size();
    int cc = horizontalHeaderItems.size();
    horizontalHeaderItems.insert(column, count, 0);
    if (cc == 0)
        tableItems.resize(rc * count);
    else
        for (int row = 0; row < rc; ++row)
            tableItems.insert(tableIndex(row, column), count, 0);
    endInsertColumns();
    return true;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 90, as _ZN11QTableModel13removeColumnsEiiRK11QModelIndex
inline bool QTableModel::removeColumns(int column, int count, const QModelIndex &)
{
    if (count < 1 || column < 0 || column + count >  horizontalHeaderItems.size())
        return false;

    beginRemoveColumns(QModelIndex(), column, column + count - 1);
    QTableWidgetItem *oldItem = nullptr;
    for (int row = rowCount() - 1; row >= 0; --row) {
        int i = tableIndex(row, column);
        for (int j = i; j < i + count; ++j) {
            oldItem = tableItems.at(j);
            if (oldItem)
                oldItem->view = nullptr;
            delete oldItem;
        }
        tableItems.remove(i, count);
    }
    for (int h=column; h<column+count; ++h) {
        oldItem = horizontalHeaderItems.at(h);
        if (oldItem)
            oldItem->view = nullptr;
        delete oldItem;
    }
    horizontalHeaderItems.remove(column, count);
    endRemoveColumns();
    return true;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 722, as _ZN11QTableModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti
inline bool QTableModel::setHeaderData(int section, Qt::Orientation orientation,
                                const QVariant &value, int role)
{
    if (section < 0 ||
       (orientation == Qt::Horizontal && horizontalHeaderItems.size() <= section) ||
       (orientation == Qt::Vertical && verticalHeaderItems.size() <= section))
    return false;

    QTableWidgetItem *itm = nullptr;
    if (orientation == Qt::Horizontal)
        itm = horizontalHeaderItems.at(section);
    else
        itm = verticalHeaderItems.at(section);
    if (itm) {
        itm->setData(role, value);
        return true;
    }
    return false;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 498, as _ZN11QTableModel4sortEiN2Qt9SortOrderE
inline void QTableModel::sort(int column, Qt::SortOrder order)
{
    QList<std::pair<QTableWidgetItem *, int>> sortable;
    QList<int> unsortable;
    const int numRows = rowCount();

    sortable.reserve(numRows);
    unsortable.reserve(numRows);

    for (int row = 0; row < numRows; ++row) {
        if (QTableWidgetItem *itm = item(row, column))
            sortable.emplace_back(itm, row);
        else
            unsortable.append(row);
    }

    const auto compare = (order == Qt::AscendingOrder ? &itemLessThan : &itemGreaterThan);
    std::stable_sort(sortable.begin(), sortable.end(), compare);

    QList<QTableWidgetItem *> sorted_table(tableItems.size());
    QModelIndexList from;
    QModelIndexList to;
    const int numColumns = columnCount();
    from.reserve(numRows * numColumns);
    to.reserve(numRows * numColumns);
    for (int i = 0; i < numRows; ++i) {
        int r = (i < sortable.size()
                 ? sortable.at(i).second
                 : unsortable.at(i - sortable.size()));
        for (int c = 0; c < numColumns; ++c) {
            sorted_table[tableIndex(i, c)] = item(r, c);
            from.append(createIndex(r, c));
            to.append(createIndex(i, c));
        }
    }

    emit layoutAboutToBeChanged({}, QAbstractItemModel::VerticalSortHint);

    tableItems = sorted_table;
    changePersistentIndexList(from, to); // ### slow

    emit layoutChanged({}, QAbstractItemModel::VerticalSortHint);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 394, as _ZN11QTableModel7setDataERK11QModelIndexRK8QVarianti
inline bool QTableModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (!index.isValid())
        return false;

    QTableWidgetItem *itm = item(index);
    if (itm) {
        itm->setData(role, value);
        return true;
    }

    // don't create dummy table items for empty values
    if (!value.isValid())
        return false;

    QTableWidget *view = this->view();
    if (!view)
        return false;

    itm = createItem();
    itm->setData(role, value);
    view->setItem(index.row(), index.column(), itm);
    return true;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 118, as _ZN11QTableModel8moveRowsERK11QModelIndexiiS2_i
inline bool QTableModel::moveRows(const QModelIndex &sourceParent, int sourceRow, int count, const QModelIndex &destinationParent, int destinationChild)
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
    if (!beginMoveRows(sourceParent, sourceRow, sourceRow + count - 1, destinationParent, destinationChild))
        return false;

    // Table items
    int numItems = count * columnCount();
    int fromIndex = tableIndex(sourceRow, 0);
    int destinationIndex = tableIndex(destinationChild, 0);
    if (destinationChild < sourceRow)
        fromIndex += numItems - 1;
    else
        destinationIndex--;
    while (numItems--)
        tableItems.move(fromIndex, destinationIndex);

    // Header items
    int fromRow = sourceRow;
    if (destinationChild < sourceRow)
        fromRow += count - 1;
    else
        destinationChild--;
    while (count--)
        verticalHeaderItems.move(fromRow, destinationChild);

    endMoveRows();
    return true;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 702, as _ZNK11QTableModel10headerDataEiN2Qt11OrientationEi
inline QVariant QTableModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (section < 0)
        return QVariant();

    QTableWidgetItem *itm = nullptr;
    if (orientation == Qt::Horizontal && section < horizontalHeaderItems.size())
        itm = horizontalHeaderItems.at(section);
    else if (orientation == Qt::Vertical && section < verticalHeaderItems.size())
        itm = verticalHeaderItems.at(section);
    else
        return QVariant(); // section is out of bounds

    if (itm)
        return itm->data(role);
    if (role == Qt::DisplayRole)
        return section + 1;
    return QVariant();
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 381, as _ZNK11QTableModel11columnCountERK11QModelIndex
inline int QTableModel::columnCount(const QModelIndex &parent) const
{
    return parent.isValid() ? 0 : horizontalHeaderItems.size();
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 873, as _ZNK11QTableModel20supportedDragActionsEv
inline Qt::DropActions QTableModel::supportedDragActions() const
{
#if QT_CONFIG(draganddrop)
    const QTableWidget *view = this->view();
    return (view ? view->supportedDragActions() : Qt::DropActions(Qt::IgnoreAction));
#else
    return Qt::DropActions(Qt::IgnoreAction);
#endif
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 867, as _ZNK11QTableModel20supportedDropActionsEv
inline Qt::DropActions QTableModel::supportedDropActions() const
{
    const QTableWidget *view = this->view();
    return (view ? view->supportedDropActions() : Qt::DropActions(Qt::IgnoreAction));
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 386, as _ZNK11QTableModel4dataERK11QModelIndexi
inline QVariant QTableModel::data(const QModelIndex &index, int role) const
{
    QTableWidgetItem *itm = item(index);
    if (itm)
        return itm->data(role);
    return QVariant();
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 484, as _ZNK11QTableModel5flagsERK11QModelIndex
inline Qt::ItemFlags QTableModel::flags(const QModelIndex &index) const
{
    if (!index.isValid())
        return Qt::ItemIsDropEnabled;
    if (QTableWidgetItem *itm = item(index))
        return itm->flags();
    return (Qt::ItemIsEditable
            |Qt::ItemIsSelectable
            |Qt::ItemIsUserCheckable
            |Qt::ItemIsEnabled
            |Qt::ItemIsDragEnabled
            |Qt::ItemIsDropEnabled);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 419, as _ZNK11QTableModel8itemDataERK11QModelIndex
inline QMap<int, QVariant> QTableModel::itemData(const QModelIndex &index) const
{
    QMap<int, QVariant> roles;
    QTableWidgetItem *itm = item(index);
    if (itm) {
        for (int i = 0; i < itm->values.size(); ++i) {
            roles.insert(itm->values.at(i).role,
                         itm->values.at(i).value);
        }
    }
    return roles;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 832, as _ZNK11QTableModel8mimeDataERK5QListI11QModelIndexE
inline QMimeData *QTableModel::mimeData(const QModelIndexList &indexes) const
{
    QList<QTableWidgetItem*> items;
    const int indexesCount = indexes.size();
    items.reserve(indexesCount);
    for (int i = 0; i < indexesCount; ++i)
        items << item(indexes.at(i));
    const QTableWidget *view = this->view();

    // cachedIndexes is a little hack to avoid copying from QModelIndexList to
    // QList<QTreeWidgetItem*> and back again in the view
    cachedIndexes = indexes;
    QMimeData *mimeData = (view ? view->mimeData(items) : nullptr);
    cachedIndexes.clear();
    return mimeData;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 376, as _ZNK11QTableModel8rowCountERK11QModelIndex
inline int QTableModel::rowCount(const QModelIndex &parent) const
{
    return parent.isValid() ? 0 : verticalHeaderItems.size();
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 819, as _ZNK11QTableModel9mimeTypesEv
inline QStringList QTableModel::mimeTypes() const
{
    auto v = view();
    if (v)
        return v->mimeTypes();
    return {};
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 14, as _ZN11QTableModelC1EiiP12QTableWidget
inline QTableModel::QTableModel(int rows, int columns, QTableWidget *parent)
    : QAbstractTableModel(parent),
      prototype(nullptr),
      tableItems(rows * columns, 0),
      verticalHeaderItems(rows, 0),
      horizontalHeaderItems(columns, 0)
{}

//  from src/widgets/itemviews/qtablewidget.cpp, line 22, as _ZN11QTableModelD1Ev
inline QTableModel::~QTableModel()
{
    clear();
    delete prototype;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 158, as _ZN11QTableModel7setItemEiiP16QTableWidgetItem
inline void QTableModel::setItem(int row, int column, QTableWidgetItem *item)
{
    int i = tableIndex(row, column);
    if (i < 0 || i >= tableItems.size())
        return;
    QTableWidgetItem *oldItem = tableItems.at(i);
    if (item == oldItem)
        return;

    // remove old
    if (oldItem)
        oldItem->view = nullptr;
    delete tableItems.at(i);

    QTableWidget *view = this->view();

    // set new
    if (item)
        item->d->id = i;
    tableItems[i] = item;

    if (view && view->isSortingEnabled()
        && view->horizontalHeader()->sortIndicatorSection() == column) {
        // sorted insertion
        Qt::SortOrder order = view->horizontalHeader()->sortIndicatorOrder();
        QList<QTableWidgetItem *> colItems = columnItems(column);
        if (row < colItems.size())
            colItems.remove(row);
        int sortedRow;
        if (item == nullptr) {
            // move to after all non-0 (sortable) items
            sortedRow = colItems.size();
        } else {
            QList<QTableWidgetItem *>::iterator it;
            it = sortedInsertionIterator(colItems.begin(), colItems.end(), order, item);
            sortedRow = qMax((int)(it - colItems.begin()), 0);
        }
        if (sortedRow != row) {
            const int destinationChild = sortedRow > row ? sortedRow + 1 : sortedRow;
            moveRows(QModelIndex(), row, 1, QModelIndex(), destinationChild);
            return;
        }
    }
    QModelIndex idx = QAbstractTableModel::index(row, column);
    emit dataChanged(idx, idx);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 205, as _ZN11QTableModel8takeItemEii
inline QTableWidgetItem *QTableModel::takeItem(int row, int column)
{
    long i = tableIndex(row, column);
    QTableWidgetItem *itm = tableItems.value(i);
    if (itm) {
        itm->view = nullptr;
        itm->d->id = -1;
        tableItems[i] = 0;
        const QModelIndex ind = index(row, column);
        emit dataChanged(ind, ind);
    }
    return itm;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 219, as _ZNK11QTableModel4itemEii
inline QTableWidgetItem *QTableModel::item(int row, int column) const
{
    return item(index(row, column));
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 224, as _ZNK11QTableModel4itemERK11QModelIndex
inline QTableWidgetItem *QTableModel::item(const QModelIndex &index) const
{
    if (!isValid(index))
        return nullptr;
    return tableItems.at(tableIndex(index.row(), index.column()));
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 231, as _ZN11QTableModel10removeItemEP16QTableWidgetItem
inline void QTableModel::removeItem(QTableWidgetItem *item)
{
    int i = tableItems.indexOf(item);
    if (i != -1) {
        QModelIndex idx = index(item);
        tableItems[i] = nullptr;
        emit dataChanged(idx, idx);
        return;
    }

    i = verticalHeaderItems.indexOf(item);

    if (i != -1) {
        verticalHeaderItems[i] = 0;
        emit headerDataChanged(Qt::Vertical, i, i);
        return;
    }
    i = horizontalHeaderItems.indexOf(item);
    if (i != -1) {
        horizontalHeaderItems[i] = 0;
        emit headerDataChanged(Qt::Horizontal, i, i);
        return;
    }
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 256, as _ZN11QTableModel23setHorizontalHeaderItemEiP16QTableWidgetItem
inline void QTableModel::setHorizontalHeaderItem(int section, QTableWidgetItem *item)
{
    if (section < 0 || section >= horizontalHeaderItems.size())
        return;
    QTableWidgetItem *oldItem = horizontalHeaderItems.at(section);
    if (item == oldItem)
        return;

    if (oldItem)
        oldItem->view = nullptr;
    delete oldItem;

    QTableWidget *view = this->view();

    if (item) {
        item->view = view;
        item->d->headerItem = true;
    }
    horizontalHeaderItems[section] = item;
    emit headerDataChanged(Qt::Horizontal, section, section);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 278, as _ZN11QTableModel21setVerticalHeaderItemEiP16QTableWidgetItem
inline void QTableModel::setVerticalHeaderItem(int section, QTableWidgetItem *item)
{
    if (section < 0 || section >= verticalHeaderItems.size())
        return;
    QTableWidgetItem *oldItem = verticalHeaderItems.at(section);
    if (item == oldItem)
        return;

    if (oldItem)
        oldItem->view = nullptr;
    delete oldItem;

    QTableWidget *view = this->view();

    if (item) {
        item->view = view;
        item->d->headerItem = true;
    }
    verticalHeaderItems[section] = item;
    emit headerDataChanged(Qt::Vertical, section, section);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 300, as _ZN11QTableModel24takeHorizontalHeaderItemEi
inline QTableWidgetItem *QTableModel::takeHorizontalHeaderItem(int section)
{
    if (section < 0 || section >= horizontalHeaderItems.size())
        return nullptr;
    QTableWidgetItem *itm = horizontalHeaderItems.at(section);
    if (itm) {
        itm->view = nullptr;
        itm->d->headerItem = false;
        horizontalHeaderItems[section] = 0;
    }
    return itm;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 313, as _ZN11QTableModel22takeVerticalHeaderItemEi
inline QTableWidgetItem *QTableModel::takeVerticalHeaderItem(int section)
{
    if (section < 0 || section >= verticalHeaderItems.size())
        return nullptr;
    QTableWidgetItem *itm = verticalHeaderItems.at(section);
    if (itm) {
        itm->view = nullptr;
        itm->d->headerItem = false;
        verticalHeaderItems[section] = 0;
    }
    return itm;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 326, as _ZN11QTableModel20horizontalHeaderItemEi
inline QTableWidgetItem *QTableModel::horizontalHeaderItem(int section)
{
    return horizontalHeaderItems.value(section);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 331, as _ZN11QTableModel18verticalHeaderItemEi
inline QTableWidgetItem *QTableModel::verticalHeaderItem(int section)
{
    return verticalHeaderItems.value(section);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 336, as _ZNK11QTableModel5indexEPK16QTableWidgetItem
inline QModelIndex QTableModel::index(const QTableWidgetItem *item) const
{
    if (!item)
        return QModelIndex();
    int i = -1;
    const int id = item->d->id;
    if (id >= 0 && id < tableItems.size() && tableItems.at(id) == item) {
        i = id;
    } else { // we need to search for the item
        i = tableItems.indexOf(const_cast<QTableWidgetItem*>(item));
        if (i == -1) // not found
            return QModelIndex();
    }
    int row = i / columnCount();
    int col = i % columnCount();
    return QAbstractTableModel::index(row, col);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 354, as _ZN11QTableModel11setRowCountEi
inline void QTableModel::setRowCount(int rows)
{
    int rc = verticalHeaderItems.size();
    if (rows < 0 || rc == rows)
        return;
    if (rc < rows)
        insertRows(qMax(rc, 0), rows - rc);
    else
        removeRows(qMax(rows, 0), rc - rows);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 365, as _ZN11QTableModel14setColumnCountEi
inline void QTableModel::setColumnCount(int columns)
{
    int cc = horizontalHeaderItems.size();
    if (columns < 0 || cc == columns)
        return;
    if (cc < columns)
        insertColumns(qMax(cc, 0), columns - cc);
    else
        removeColumns(qMax(columns, 0), cc - columns);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 690, as _ZN11QTableModel12itemLessThanERKSt4pairIP16QTableWidgetItemiES5_
inline bool QTableModel::itemLessThan(const std::pair<QTableWidgetItem*,int> &left,
                               const std::pair<QTableWidgetItem*,int> &right)
{
    return *(left.first) < *(right.first);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 696, as _ZN11QTableModel15itemGreaterThanERKSt4pairIP16QTableWidgetItemiES5_
inline bool QTableModel::itemGreaterThan(const std::pair<QTableWidgetItem*,int> &left,
                                  const std::pair<QTableWidgetItem*,int> &right)
{
    return (*(right.first) < *(left .first));
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 549, as _ZN11QTableModel12ensureSortedEiN2Qt9SortOrderEii
inline void QTableModel::ensureSorted(int column, Qt::SortOrder order,
                               int start, int end)
{
    int count = end - start + 1;
    QList<std::pair<QTableWidgetItem *, int>> sorting;
    sorting.reserve(count);
    for (int row = start; row <= end; ++row) {
        QTableWidgetItem *itm = item(row, column);
        if (itm == nullptr) {
            // no more sortable items (all 0-items are
            // at the end of the table when it is sorted)
            break;
        }
        sorting.emplace_back(itm, row);
    }

    const auto compare = (order == Qt::AscendingOrder ? &itemLessThan : &itemGreaterThan);
    std::stable_sort(sorting.begin(), sorting.end(), compare);
    QModelIndexList oldPersistentIndexes, newPersistentIndexes;
    QList<QTableWidgetItem *> newTable = tableItems;
    QList<QTableWidgetItem *> newVertical = verticalHeaderItems;
    QList<QTableWidgetItem *> colItems = columnItems(column);
    QList<QTableWidgetItem *>::iterator vit = colItems.begin();
    qsizetype distanceFromBegin = 0;
    bool changed = false;
    for (int i = 0; i < sorting.size(); ++i) {
        distanceFromBegin = std::distance(colItems.begin(), vit);
        int oldRow = sorting.at(i).second;
        QTableWidgetItem *item = colItems.at(oldRow);
        colItems.remove(oldRow);
        vit = sortedInsertionIterator(colItems.begin() + distanceFromBegin, colItems.end(), order,
                                      item);
        int newRow = qMax((int)(vit - colItems.begin()), 0);
        if ((newRow < oldRow) && !(*item < *colItems.at(oldRow - 1)) && !(*colItems.at(oldRow - 1) < *item))
            newRow = oldRow;
        vit = colItems.insert(vit, item);
        if (newRow != oldRow) {
            if (!changed) {
                emit layoutAboutToBeChanged({}, QAbstractItemModel::VerticalSortHint);
                oldPersistentIndexes = persistentIndexList();
                newPersistentIndexes = oldPersistentIndexes;
                changed = true;
            }
            // move the items @ oldRow to newRow
            int cc = columnCount();
            QList<QTableWidgetItem *> rowItems(cc);
            for (int j = 0; j < cc; ++j)
                rowItems[j] = newTable.at(tableIndex(oldRow, j));
            newTable.remove(tableIndex(oldRow, 0), cc);
            newTable.insert(tableIndex(newRow, 0), cc, 0);
            for (int j = 0; j < cc; ++j)
                newTable[tableIndex(newRow, j)] = rowItems.at(j);
            QTableWidgetItem *header = newVertical.at(oldRow);
            newVertical.remove(oldRow);
            newVertical.insert(newRow, header);
            // update persistent indexes
            updateRowIndexes(newPersistentIndexes, oldRow, newRow);
            // the index of the remaining rows may have changed
            for (int j = i + 1; j < sorting.size(); ++j) {
                int otherRow = sorting.at(j).second;
                if (oldRow < otherRow && newRow >= otherRow)
                    --sorting[j].second;
                else if (oldRow > otherRow && newRow <= otherRow)
                    ++sorting[j].second;
            }
        }
    }

    if (changed) {
        tableItems = newTable;
        verticalHeaderItems = newVertical;
        changePersistentIndexList(oldPersistentIndexes,
                                  newPersistentIndexes);
        emit layoutChanged({}, QAbstractItemModel::VerticalSortHint);
    }
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 631, as _ZNK11QTableModel11columnItemsEi
inline QList<QTableWidgetItem *> QTableModel::columnItems(int column) const
{
    QList<QTableWidgetItem *> items;
    int rc = rowCount();
    items.reserve(rc);
    for (int row = 0; row < rc; ++row) {
        QTableWidgetItem *itm = item(row, column);
        if (itm == nullptr) {
            // no more sortable items (all 0-items are
            // at the end of the table when it is sorted)
            break;
        }
        items.append(itm);
    }
    return items;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 655, as _ZN11QTableModel16updateRowIndexesER5QListI11QModelIndexEii
inline void QTableModel::updateRowIndexes(QModelIndexList &indexes,
                                   int movedFromRow, int movedToRow)
{
    QModelIndexList::iterator it;
    for (it = indexes.begin(); it != indexes.end(); ++it) {
        int oldRow = (*it).row();
        int newRow = oldRow;
        if (oldRow == movedFromRow)
            newRow = movedToRow;
        else if (movedFromRow < oldRow && movedToRow >= oldRow)
            newRow = oldRow - 1;
        else if (movedFromRow > oldRow && movedToRow <= oldRow)
            newRow = oldRow + 1;
        if (newRow != oldRow)
            *it = index(newRow, (*it).column(), (*it).parent());
    }
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 680, as _ZN11QTableModel23sortedInsertionIteratorERKN5QListIP16QTableWidgetItemE8iteratorES6_N2Qt9SortOrderES2_
inline QList<QTableWidgetItem *>::iterator
QTableModel::sortedInsertionIterator(const QList<QTableWidgetItem *>::iterator &begin,
                                     const QList<QTableWidgetItem *>::iterator &end,
                                     Qt::SortOrder order, QTableWidgetItem *item)
{
    if (order == Qt::AscendingOrder)
        return std::lower_bound(begin, end, item, QTableModelLessThan());
    return std::lower_bound(begin, end, item, QTableModelGreaterThan());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 742, as _ZNK11QTableModel7isValidERK11QModelIndex
inline bool QTableModel::isValid(const QModelIndex &index) const
{
    return (index.isValid()
            && index.row() < verticalHeaderItems.size()
            && index.column() < horizontalHeaderItems.size());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 749, as _ZN11QTableModel5clearEv
inline void QTableModel::clear()
{
    for (int j = 0; j < verticalHeaderItems.size(); ++j) {
        if (verticalHeaderItems.at(j)) {
            verticalHeaderItems.at(j)->view = nullptr;
            delete verticalHeaderItems.at(j);
            verticalHeaderItems[j] = 0;
        }
    }
    for (int k = 0; k < horizontalHeaderItems.size(); ++k) {
        if (horizontalHeaderItems.at(k)) {
            horizontalHeaderItems.at(k)->view = nullptr;
            delete horizontalHeaderItems.at(k);
            horizontalHeaderItems[k] = 0;
        }
    }
    clearContents();
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 768, as _ZN11QTableModel13clearContentsEv
inline void QTableModel::clearContents()
{
    beginResetModel();
    for (int i = 0; i < tableItems.size(); ++i) {
        if (tableItems.at(i)) {
            tableItems.at(i)->view = nullptr;
            delete tableItems.at(i);
            tableItems[i] = 0;
        }
    }
    endResetModel();
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 781, as _ZN11QTableModel11itemChangedEP16QTableWidgetItemRK5QListIiE
inline void QTableModel::itemChanged(QTableWidgetItem *item, const QList<int> &roles)
{
    if (!item)
        return;
    if (item->d->headerItem) {
        int row = verticalHeaderItems.indexOf(item);
        if (row >= 0) {
            emit headerDataChanged(Qt::Vertical, row, row);
        } else {
            int column = horizontalHeaderItems.indexOf(item);
            if (column >= 0)
                emit headerDataChanged(Qt::Horizontal, column, column);
        }
    } else {
        QModelIndex idx = index(item);
        if (idx.isValid())
            emit dataChanged(idx, idx, roles);
    }
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 801, as _ZNK11QTableModel10createItemEv
inline QTableWidgetItem* QTableModel::createItem() const
{
    return prototype ? prototype->clone() : new QTableWidgetItem;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 806, as _ZNK11QTableModel13itemPrototypeEv
inline const QTableWidgetItem *QTableModel::itemPrototype() const
{
    return prototype;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 811, as _ZN11QTableModel16setItemPrototypeEPK16QTableWidgetItem
inline void QTableModel::setItemPrototype(const QTableWidgetItem *item)
{
    if (prototype != item) {
        delete prototype;
        prototype = item;
    }
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 827, as _ZNK11QTableModel16internalMimeDataEv
inline QMimeData *QTableModel::internalMimeData()  const
{
    return QAbstractTableModel::mimeData(cachedIndexes);
}
//  -----------------------------------------------------------------------

//  A QTableModel that Python can take functions over in. Every QTableModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableModelCall1)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableModelCall2)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableModelCall3)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableModelCall4)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef const QModelIndex * (*CuteQTableModelCall5)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef int (*CuteQTableModelCall6)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef int (*CuteQTableModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef const QVariant * (*CuteQTableModelCall8)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableModelCall9)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef const QVariant * (*CuteQTableModelCall11)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableModelCall12)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef int (*CuteQTableModelCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef void (*CuteQTableModelCall14)(const void *, int, int, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableModelCall15)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef int (*CuteQTableModelCall16)(const void *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
typedef int (*CuteQTableModelCall17)(const void *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQTableModelCall18)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQTableModelCall19)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTableModelCall20)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTableModelCall21)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTableModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQTableModelCall23)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTableModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQTableModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQTableModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQTableModelCall27)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQTableModelCall28)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQTableModelCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQTableModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTableModelCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTableModelCall32)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableModelCall33)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTableModel : public QTableModel {
public:
  using QTableModel::QTableModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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
#if QT_CONFIG(tablewidget)
  //  bool QTableModel::insertRows(int row, int count, const QModelIndex
  //      &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTableModelCall0 call = reinterpret_cast<CuteQTableModelCall0>(taken[0]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QTableModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  bool QTableModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTableModelCall1 call = reinterpret_cast<CuteQTableModelCall1>(taken[1]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QTableModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  bool QTableModel::removeRows(int row, int count, const QModelIndex
  //      &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTableModelCall2 call = reinterpret_cast<CuteQTableModelCall2>(taken[2]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QTableModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  bool QTableModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTableModelCall3 call = reinterpret_cast<CuteQTableModelCall3>(taken[3]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QTableModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  bool QTableModel::moveRows(const QModelIndex &sourceParent, int
  //      sourceRow, int count, const QModelIndex &destinationParent, int
  //      destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTableModelCall4 call = reinterpret_cast<CuteQTableModelCall4>(taken[4]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QTableModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  QModelIndex QTableModel::index(int row, int column, const QModelIndex
  //      &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTableModelCall5 call = reinterpret_cast<CuteQTableModelCall5>(taken[5]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QTableModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  int QTableModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTableModelCall6 call = reinterpret_cast<CuteQTableModelCall6>(taken[6]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QTableModel::rowCount(parent);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  int QTableModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTableModelCall7 call = reinterpret_cast<CuteQTableModelCall7>(taken[7]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QTableModel::columnCount(parent);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  QVariant QTableModel::data(const QModelIndex &index, int role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTableModelCall8 call = reinterpret_cast<CuteQTableModelCall8>(taken[8]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QTableModel::data(index, role);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  bool QTableModel::setData(const QModelIndex &index, const QVariant
  //      &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTableModelCall9 call = reinterpret_cast<CuteQTableModelCall9>(taken[9]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QTableModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  bool QTableModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTableModelCall10 call = reinterpret_cast<CuteQTableModelCall10>(taken[10]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QTableModel::clearItemData(index);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  QVariant QTableModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQTableModelCall11 call = reinterpret_cast<CuteQTableModelCall11>(taken[11]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QTableModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  bool QTableModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTableModelCall12 call = reinterpret_cast<CuteQTableModelCall12>(taken[12]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QTableModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  Qt::ItemFlags QTableModel::flags(const QModelIndex &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQTableModelCall13 call = reinterpret_cast<CuteQTableModelCall13>(taken[13]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QTableModel::flags(index);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  void QTableModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTableModelCall14 call = reinterpret_cast<CuteQTableModelCall14>(taken[14]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QTableModel::sort(column, order);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  bool QTableModel::dropMimeData(const QMimeData *data, Qt::DropAction
  //      action, int row, int column, const QModelIndex &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTableModelCall15 call = reinterpret_cast<CuteQTableModelCall15>(taken[15]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QTableModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  Qt::DropActions QTableModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTableModelCall16 call = reinterpret_cast<CuteQTableModelCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QTableModel::supportedDropActions();
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(tablewidget)
  //  Qt::DropActions QTableModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQTableModelCall17 call = reinterpret_cast<CuteQTableModelCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QTableModel::supportedDragActions();
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractTableModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQTableModelCall18 call = reinterpret_cast<CuteQTableModelCall18>(taken[18]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractTableModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractTableModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQTableModelCall19 call = reinterpret_cast<CuteQTableModelCall19>(taken[19]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QAbstractTableModel::parent(child);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractTableModel::hasChildren(const QModelIndex &parent)
  //      const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQTableModelCall20 call = reinterpret_cast<CuteQTableModelCall20>(taken[20]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractTableModel::hasChildren(parent);
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
    if (taken[21]) {
      int handled = 0;
      CuteQTableModelCall21 call = reinterpret_cast<CuteQTableModelCall21>(taken[21]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
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
    if (taken[22]) {
      int handled = 0;
      CuteQTableModelCall22 call = reinterpret_cast<CuteQTableModelCall22>(taken[22]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTableModelCall23 call = reinterpret_cast<CuteQTableModelCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQTableModelCall24 call = reinterpret_cast<CuteQTableModelCall24>(taken[24]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQTableModelCall25 call = reinterpret_cast<CuteQTableModelCall25>(taken[25]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQTableModelCall26 call = reinterpret_cast<CuteQTableModelCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQTableModelCall27 call = reinterpret_cast<CuteQTableModelCall27>(taken[27]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[28]) {
      int handled = 0;
      CuteQTableModelCall28 call = reinterpret_cast<CuteQTableModelCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[29]) {
      int handled = 0;
      CuteQTableModelCall29 call = reinterpret_cast<CuteQTableModelCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[30]) {
      int handled = 0;
      CuteQTableModelCall30 call = reinterpret_cast<CuteQTableModelCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQTableModelCall31 call = reinterpret_cast<CuteQTableModelCall31>(taken[31]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQTableModelCall32 call = reinterpret_cast<CuteQTableModelCall32>(taken[32]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTableModelCall33 call = reinterpret_cast<CuteQTableModelCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQTableModelCall34 call = reinterpret_cast<CuteQTableModelCall34>(taken[34]);
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
      CuteQTableModelCall35 call = reinterpret_cast<CuteQTableModelCall35>(taken[35]);
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
      CuteQTableModelCall36 call = reinterpret_cast<CuteQTableModelCall36>(taken[36]);
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
      CuteQTableModelCall37 call = reinterpret_cast<CuteQTableModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTableModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTableModel10metaObjectEv(
    const QTableModel *self) {
  return self->metaObject();
}

//  void *QTableModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QTableModel11qt_metacastEPKc(
    QTableModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTableModel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QTableModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QTableModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTableModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTableModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTableModel::tr(s, c, n));
}

//  QTableModel::QTableModel(int rows, int columns, QTableWidget *parent)
extern "C" Q_DECL_EXPORT
QTableModel *ritual_ZN11QTableModelC1EiiP12QTableWidget(
    int rows,
    int columns,
    QTableWidget *parent) {
  return new CuteQTableModel(rows, columns, parent);
}

//  QTableModel::~QTableModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModelD1Ev(QTableModel *self) {
  delete self;
}

//  QTableWidget *QTableModel::view() const
extern "C" Q_DECL_EXPORT
QTableWidget *ritual_ZNK11QTableModel4viewEv(const QTableModel *self) {
  return self->view();
}

//  bool QTableModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel10insertRowsEiiRK11QModelIndex(
    QTableModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QTableModel::insertColumns(int column, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel13insertColumnsEiiRK11QModelIndex(
    QTableModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QTableModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel10removeRowsEiiRK11QModelIndex(
    QTableModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QTableModel::removeColumns(int column, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel13removeColumnsEiiRK11QModelIndex(
    QTableModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QTableModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel8moveRowsERK11QModelIndexiiS2_i(
    QTableModel *self,
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

//  void QTableModel::setItem(int row, int column, QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel7setItemEiiP16QTableWidgetItem(
    QTableModel *self,
    int row,
    int column,
    QTableWidgetItem *item) {
  self->setItem(row, column, item);
}

//  QTableWidgetItem *QTableModel::takeItem(int row, int column)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN11QTableModel8takeItemEii(
    QTableModel *self,
    int row,
    int column) {
  return self->takeItem(row, column);
}

//  QTableWidgetItem *QTableModel::item(int row, int column) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK11QTableModel4itemEii(
    const QTableModel *self,
    int row,
    int column) {
  return self->item(row, column);
}

//  QTableWidgetItem *QTableModel::item(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK11QTableModel4itemERK11QModelIndex(
    const QTableModel *self,
    const QModelIndex *index) {
  return self->item(*index);
}

//  void QTableModel::removeItem(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel10removeItemEP16QTableWidgetItem(
    QTableModel *self,
    QTableWidgetItem *item) {
  self->removeItem(item);
}

//  void QTableModel::setHorizontalHeaderItem(int section, QTableWidgetItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel23setHorizontalHeaderItemEiP16QTableWidgetItem(
    QTableModel *self,
    int section,
    QTableWidgetItem *item) {
  self->setHorizontalHeaderItem(section, item);
}

//  void QTableModel::setVerticalHeaderItem(int section, QTableWidgetItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel21setVerticalHeaderItemEiP16QTableWidgetItem(
    QTableModel *self,
    int section,
    QTableWidgetItem *item) {
  self->setVerticalHeaderItem(section, item);
}

//  QTableWidgetItem *QTableModel::takeHorizontalHeaderItem(int section)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN11QTableModel24takeHorizontalHeaderItemEi(
    QTableModel *self,
    int section) {
  return self->takeHorizontalHeaderItem(section);
}

//  QTableWidgetItem *QTableModel::takeVerticalHeaderItem(int section)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN11QTableModel22takeVerticalHeaderItemEi(
    QTableModel *self,
    int section) {
  return self->takeVerticalHeaderItem(section);
}

//  QTableWidgetItem *QTableModel::horizontalHeaderItem(int section)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN11QTableModel20horizontalHeaderItemEi(
    QTableModel *self,
    int section) {
  return self->horizontalHeaderItem(section);
}

//  QTableWidgetItem *QTableModel::verticalHeaderItem(int section)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN11QTableModel18verticalHeaderItemEi(
    QTableModel *self,
    int section) {
  return self->verticalHeaderItem(section);
}

//  QModelIndex QTableModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QTableModel5indexEiiRK11QModelIndex(
    const QTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QTableModel::index(const QTableWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QTableModel5indexEPK16QTableWidgetItem(
    const QTableModel *self,
    const QTableWidgetItem *item) {
  return new QModelIndex(self->index(item));
}

//  void QTableModel::setRowCount(int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel11setRowCountEi(QTableModel *self, int rows) {
  self->setRowCount(rows);
}

//  void QTableModel::setColumnCount(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel14setColumnCountEi(
    QTableModel *self,
    int columns) {
  self->setColumnCount(columns);
}

//  int QTableModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTableModel8rowCountERK11QModelIndex(
    const QTableModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QTableModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTableModel11columnCountERK11QModelIndex(
    const QTableModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QTableModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QTableModel4dataERK11QModelIndexi(
    const QTableModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QTableModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel7setDataERK11QModelIndexRK8QVarianti(
    QTableModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QTableModel::setItemData(const QModelIndex &index, const QMap<int,
//      QVariant> &roles)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel11setItemDataERK11QModelIndexRK4QMapIi8QVariantE(
    QTableModel *self,
    const QModelIndex *index,
    const QMap<int, QVariant> *roles) {
  return self->setItemData(*index, *roles);
}

//  bool QTableModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel13clearItemDataERK11QModelIndex(
    QTableModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  QMap<int, QVariant> QTableModel::itemData(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK11QTableModel8itemDataERK11QModelIndex(
    const QTableModel *self,
    const QModelIndex *index) {
  return new QMap<int, QVariant>(self->itemData(*index));
}

//  QVariant QTableModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QTableModel10headerDataEiN2Qt11OrientationEi(
    const QTableModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QTableModel::setHeaderData(int section, Qt::Orientation orientation,
//      const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QTableModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  Qt::ItemFlags QTableModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTableModel5flagsERK11QModelIndex(
    const QTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  void QTableModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel4sortEiN2Qt9SortOrderE(
    QTableModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  bool QTableModel::itemLessThan(const std::pair<QTableWidgetItem *, int>
//      &left, const std::pair<QTableWidgetItem *, int> &right)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel12itemLessThanERKSt4pairIP16QTableWidgetItemiES5_(
    const std::pair<QTableWidgetItem *, int> *left,
    const std::pair<QTableWidgetItem *, int> *right) {
  return QTableModel::itemLessThan(*left, *right);
}

//  bool QTableModel::itemGreaterThan(const std::pair<QTableWidgetItem *,
//      int> &left, const std::pair<QTableWidgetItem *, int> &right)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel15itemGreaterThanERKSt4pairIP16QTableWidgetItemiES5_(
    const std::pair<QTableWidgetItem *, int> *left,
    const std::pair<QTableWidgetItem *, int> *right) {
  return QTableModel::itemGreaterThan(*left, *right);
}

//  void QTableModel::ensureSorted(int column, Qt::SortOrder order, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel12ensureSortedEiN2Qt9SortOrderEii(
    QTableModel *self,
    int column,
    Qt::SortOrder order,
    int start,
    int end) {
  self->ensureSorted(column, order, start, end);
}

//  QList<QTableWidgetItem *> QTableModel::columnItems(int column) const
extern "C" Q_DECL_EXPORT
QList<QTableWidgetItem *> *ritual_ZNK11QTableModel11columnItemsEi(
    const QTableModel *self,
    int column) {
  return new QList<QTableWidgetItem *>(self->columnItems(column));
}

//  void QTableModel::updateRowIndexes(QModelIndexList &indexes, int
//      movedFromRow, int movedToRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel16updateRowIndexesER5QListI11QModelIndexEii(
    QTableModel *self,
    QModelIndexList *indexes,
    int movedFromRow,
    int movedToRow) {
  self->updateRowIndexes(*indexes, movedFromRow, movedToRow);
}

//  QList<QTableWidgetItem *>::iterator
//      QTableModel::sortedInsertionIterator(const QList<QTableWidgetItem
//      *>::iterator &begin, const QList<QTableWidgetItem *>::iterator &end,
//      Qt::SortOrder order, QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
QList<QTableWidgetItem *>::iterator *ritual_ZN11QTableModel23sortedInsertionIteratorERKN5QListIP16QTableWidgetItemE8iteratorES6_N2Qt9SortOrderES2_(
    const QList<QTableWidgetItem *>::iterator *begin,
    const QList<QTableWidgetItem *>::iterator *end,
    Qt::SortOrder order,
    QTableWidgetItem *item) {
  return new QList<QTableWidgetItem *>::iterator(
      QTableModel::sortedInsertionIterator(
          *begin,
          *end,
          order,
          item));
}

//  bool QTableModel::isValid(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTableModel7isValidERK11QModelIndex(
    const QTableModel *self,
    const QModelIndex *index) {
  return self->isValid(*index);
}

//  long QTableModel::tableIndex(int row, int column) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK11QTableModel10tableIndexEii(
    const QTableModel *self,
    int row,
    int column) {
  return self->tableIndex(row, column);
}

//  void QTableModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel5clearEv(QTableModel *self) {
  self->clear();
}

//  void QTableModel::clearContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel13clearContentsEv(QTableModel *self) {
  self->clearContents();
}

//  void QTableModel::itemChanged(QTableWidgetItem *item, const QList<int>
//      &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel11itemChangedEP16QTableWidgetItemRK5QListIiE(
    QTableModel *self,
    QTableWidgetItem *item,
    const QList<int> *roles) {
  self->itemChanged(item, *roles);
}

//  QTableWidgetItem *QTableModel::createItem() const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK11QTableModel10createItemEv(
    const QTableModel *self) {
  return self->createItem();
}

//  const QTableWidgetItem *QTableModel::itemPrototype() const
extern "C" Q_DECL_EXPORT
const QTableWidgetItem *ritual_ZNK11QTableModel13itemPrototypeEv(
    const QTableModel *self) {
  return self->itemPrototype();
}

//  void QTableModel::setItemPrototype(const QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTableModel16setItemPrototypeEPK16QTableWidgetItem(
    QTableModel *self,
    const QTableWidgetItem *item) {
  self->setItemPrototype(item);
}

//  QStringList QTableModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QTableModel9mimeTypesEv(
    const QTableModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QTableModel::mimeData(const QModelIndexList &indexes) const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK11QTableModel8mimeDataERK5QListI11QModelIndexE(
    const QTableModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  bool QTableModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QTableModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QTableModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTableModel20supportedDropActionsEv(
    const QTableModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  Qt::DropActions QTableModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTableModel20supportedDragActionsEv(
    const QTableModel *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  QMimeData *QTableModel::internalMimeData() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK11QTableModel16internalMimeDataEv(
    const QTableModel *self) {
  return self->internalMimeData();
}

//  a Python function taken by a CuteQTableModel, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTableModel(
    QTableModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTableModel *>(self)->take(key, call);
}

//  bool QTableModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTableModel10insertRowsEiiRK11QModelIndex(
    QTableModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QTableModel::insertRows(row, count, *parent);
}

//  bool QTableModel::insertColumns(int column, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTableModel13insertColumnsEiiRK11QModelIndex(
    QTableModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QTableModel::insertColumns(column, count, *parent);
}

//  bool QTableModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTableModel10removeRowsEiiRK11QModelIndex(
    QTableModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QTableModel::removeRows(row, count, *parent);
}

//  bool QTableModel::removeColumns(int column, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTableModel13removeColumnsEiiRK11QModelIndex(
    QTableModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QTableModel::removeColumns(column, count, *parent);
}

//  bool QTableModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTableModel8moveRowsERK11QModelIndexiiS2_i(
    QTableModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->QTableModel::moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  QModelIndex QTableModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK11QTableModel5indexEiiRK11QModelIndex(
    const QTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->QTableModel::index(row, column, *parent));
}

//  int QTableModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTableModel8rowCountERK11QModelIndex(
    const QTableModel *self,
    const QModelIndex *parent) {
  return self->QTableModel::rowCount(*parent);
}

//  int QTableModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTableModel11columnCountERK11QModelIndex(
    const QTableModel *self,
    const QModelIndex *parent) {
  return self->QTableModel::columnCount(*parent);
}

//  QVariant QTableModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK11QTableModel4dataERK11QModelIndexi(
    const QTableModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QTableModel::data(*index, role));
}

//  bool QTableModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTableModel7setDataERK11QModelIndexRK8QVarianti(
    QTableModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QTableModel::setData(*index, *value, role);
}

//  bool QTableModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTableModel13clearItemDataERK11QModelIndex(
    QTableModel *self,
    const QModelIndex *index) {
  return self->QTableModel::clearItemData(*index);
}

//  QVariant QTableModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK11QTableModel10headerDataEiN2Qt11OrientationEi(
    const QTableModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QTableModel::headerData(
          section,
          orientation,
          role));
}

//  bool QTableModel::setHeaderData(int section, Qt::Orientation orientation,
//      const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTableModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QTableModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->QTableModel::setHeaderData(
      section,
      orientation,
      *value,
      role);
}

//  Qt::ItemFlags QTableModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTableModel5flagsERK11QModelIndex(
    const QTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QTableModel::flags(*index).toInt());
}

//  void QTableModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QTableModel4sortEiN2Qt9SortOrderE(
    QTableModel *self,
    int column,
    Qt::SortOrder order) {
  self->QTableModel::sort(column, order);
}

//  bool QTableModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QTableModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QTableModel::dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QTableModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTableModel20supportedDropActionsEv(
    const QTableModel *self) {
  return static_cast<int>(self->QTableModel::supportedDropActions().toInt());
}

//  Qt::DropActions QTableModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTableModel20supportedDragActionsEv(
    const QTableModel *self) {
  return static_cast<int>(self->QTableModel::supportedDragActions().toInt());
}

//  a QList<QTableWidgetItem *>::iterator a ritual of QTableModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTableModel__QList_QTableWidgetItem_iterator(
    QList<QTableWidgetItem *>::iterator *self) {
  delete self;
}

#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(tablewidget)
