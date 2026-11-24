//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "itemviews_p.h"
#include <qheaderview.h>
#if QT_CONFIG(tableview)
#include <qtableview.h>
#endif
#if QT_CONFIG(listview)
#include <qlistview.h>
#endif
#if QT_CONFIG(treeview)
#include <qtreeview.h>
#include <private/qtreeview_p.h>
#endif
#include <private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/accessible/itemviews.cpp, line 645, as _ZN16QAccessibleTable11modelChangeEP32QAccessibleTableModelChangeEvent
#if QT_CONFIG(accessibility)
inline void QAccessibleTable::modelChange(QAccessibleTableModelChangeEvent *event)
{
    // if there is no cache yet, we don't update anything
    if (childToId.isEmpty())
        return;

    switch (event->modelChangeType()) {
    case QAccessibleTableModelChangeEvent::ModelReset:
        for (QAccessible::Id id : std::as_const(childToId))
            QAccessible::deleteAccessibleInterface(id);
        childToId.clear();
        break;

    // rows are inserted: move every row after that
    case QAccessibleTableModelChangeEvent::RowsInserted:
    case QAccessibleTableModelChangeEvent::ColumnsInserted: {
        int newRows = event->lastRow() - event->firstRow() + 1;
        int newColumns = event->lastColumn() - event->firstColumn() + 1;

        ChildCache newCache;
        ChildCache::ConstIterator iter = childToId.constBegin();

        while (iter != childToId.constEnd()) {
            QAccessible::Id id = iter.value();
            QAccessibleInterface *iface = QAccessible::accessibleInterface(id);
            Q_ASSERT(iface);
            if (event->modelChangeType() == QAccessibleTableModelChangeEvent::RowsInserted
                && iface->role() == QAccessible::RowHeader) {
                QAccessibleTableHeaderCell *cell = static_cast<QAccessibleTableHeaderCell*>(iface);
                if (cell->index >= event->firstRow()) {
                    cell->index += newRows;
                }
            } else if (event->modelChangeType() == QAccessibleTableModelChangeEvent::ColumnsInserted
                   && iface->role() == QAccessible::ColumnHeader) {
                QAccessibleTableHeaderCell *cell = static_cast<QAccessibleTableHeaderCell*>(iface);
                if (cell->index >= event->firstColumn()) {
                    cell->index += newColumns;
                }
            }
            if (indexOfChild(iface) >= 0) {
                newCache.insert(indexOfChild(iface), id);
            } else {
                // ### This should really not happen,
                // but it might if the view has a root index set.
                // This needs to be fixed.
                QAccessible::deleteAccessibleInterface(id);
            }
            ++iter;
        }
        childToId = newCache;
        break;
    }

    case QAccessibleTableModelChangeEvent::ColumnsRemoved:
    case QAccessibleTableModelChangeEvent::RowsRemoved: {
        int deletedColumns = event->lastColumn() - event->firstColumn() + 1;
        int deletedRows = event->lastRow() - event->firstRow() + 1;
        ChildCache newCache;
        ChildCache::ConstIterator iter = childToId.constBegin();
        while (iter != childToId.constEnd()) {
            QAccessible::Id id = iter.value();
            QAccessibleInterface *iface = QAccessible::accessibleInterface(id);
            Q_ASSERT(iface);
            if (iface->role() == QAccessible::Cell || iface->role() == QAccessible::ListItem) {
                Q_ASSERT(iface->tableCellInterface());
                QAccessibleTableCell *cell = static_cast<QAccessibleTableCell*>(iface->tableCellInterface());
                // Since it is a QPersistentModelIndex, we only need to check if it is valid
                if (cell->m_index.isValid())
                    newCache.insert(indexOfChild(cell), id);
                else
                    QAccessible::deleteAccessibleInterface(id);
            } else if (event->modelChangeType() == QAccessibleTableModelChangeEvent::RowsRemoved
                       && iface->role() == QAccessible::RowHeader) {
                QAccessibleTableHeaderCell *cell = static_cast<QAccessibleTableHeaderCell*>(iface);
                if (cell->index < event->firstRow()) {
                    newCache.insert(indexOfChild(cell), id);
                } else if (cell->index > event->lastRow()) {
                    cell->index -= deletedRows;
                    newCache.insert(indexOfChild(cell), id);
                } else {
                    QAccessible::deleteAccessibleInterface(id);
                }
            } else if (event->modelChangeType() == QAccessibleTableModelChangeEvent::ColumnsRemoved
                   && iface->role() == QAccessible::ColumnHeader) {
                QAccessibleTableHeaderCell *cell = static_cast<QAccessibleTableHeaderCell*>(iface);
                if (cell->index < event->firstColumn()) {
                    newCache.insert(indexOfChild(cell), id);
                } else if (cell->index > event->lastColumn()) {
                    cell->index -= deletedColumns;
                    newCache.insert(indexOfChild(cell), id);
                } else {
                    QAccessible::deleteAccessibleInterface(id);
                }
            }
            ++iter;
        }
        childToId = newCache;
        break;
    }

    case QAccessibleTableModelChangeEvent::DataChanged:
        // nothing to do in this case
        break;
    }
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 340, as _ZN16QAccessibleTable11unselectRowEi
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::unselectRow(int row)
{
    const QAbstractItemView *theView = view();
    const QAbstractItemModel *theModel = theView->model();
    auto *selectionModel = theView->selectionModel();
    if (!theModel || !selectionModel)
        return false;

    const QModelIndex rootIndex = theView->rootIndex();
    const QModelIndex index = view()->model()->index(row, 0, rootIndex);
    if (!index.isValid())
        return false;

    QItemSelection selection(index, index);

    switch (theView->selectionMode()) {
    case QAbstractItemView::SingleSelection:
        //In SingleSelection and ContiguousSelection once an item
        //is selected, there's no way for the user to unselect all items
        if (selectedRowCount() == 1)
            return false;
        break;
    case QAbstractItemView::ContiguousSelection:
        if (selectedRowCount() == 1)
            return false;

        if ((!row || selectionModel->isRowSelected(row - 1, rootIndex))
            && selectionModel->isRowSelected(row + 1, rootIndex)) {
            //If there are rows selected both up the current row and down the current rown,
            //the ones which are down the current row will be deselected
            selection = QItemSelection(index, theModel->index(rowCount() - 1, 0, rootIndex));
        }
        break;
    default:
        break;
    }

    selectionModel->select(selection, QItemSelectionModel::Deselect | QItemSelectionModel::Rows);
    return true;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 305, as _ZN16QAccessibleTable12selectColumnEi
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::selectColumn(int column)
{
    QAbstractItemView *theView = view();
    const QAbstractItemModel *theModel = theView->model();
    auto *selectionModel = theView->selectionModel();
    if (!theModel || !selectionModel)
        return false;

    const QModelIndex rootIndex = theView->rootIndex();
    const QModelIndex index = theModel->index(0, column, rootIndex);

    if (!index.isValid() || view()->selectionBehavior() == QAbstractItemView::SelectRows)
        return false;

    switch (theView->selectionMode()) {
    case QAbstractItemView::NoSelection:
        return false;
    case QAbstractItemView::SingleSelection:
        if (theView->selectionBehavior() != QAbstractItemView::SelectColumns && rowCount() > 1)
            return false;
        Q_FALLTHROUGH();
    case QAbstractItemView::ContiguousSelection:
        if ((!column || !selectionModel->isColumnSelected(column - 1, rootIndex))
            && !selectionModel->isColumnSelected(column + 1, rootIndex)) {
            theView->clearSelection();
        }
        break;
    default:
        break;
    }

    selectionModel->select(index, QItemSelectionModel::Select | QItemSelectionModel::Columns);
    return true;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 636, as _ZN16QAccessibleTable14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
inline void *QAccessibleTable::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::SelectionInterface)
       return static_cast<QAccessibleSelectionInterface*>(this);
    if (t == QAccessible::TableInterface)
       return static_cast<QAccessibleTableInterface*>(this);
    return QAccessibleWidgetV2::interface_cast(t);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 381, as _ZN16QAccessibleTable14unselectColumnEi
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::unselectColumn(int column)
{
    const QAbstractItemView *theView = view();
    const QAbstractItemModel *theModel = theView->model();
    auto *selectionModel = theView->selectionModel();
    if (!theModel || !selectionModel)
        return false;

    const QModelIndex rootIndex = theView->rootIndex();
    const QModelIndex index = view()->model()->index(0, column, rootIndex);
    if (!index.isValid())
        return false;

    QItemSelection selection(index, index);

    switch (view()->selectionMode()) {
    case QAbstractItemView::SingleSelection:
        //In SingleSelection and ContiguousSelection once an item
        //is selected, there's no way for the user to unselect all items
        if (selectedColumnCount() == 1)
            return false;
        break;
    case QAbstractItemView::ContiguousSelection:
        if (selectedColumnCount() == 1)
            return false;

        if ((!column || selectionModel->isColumnSelected(column - 1, rootIndex))
            && selectionModel->isColumnSelected(column + 1, rootIndex)) {
            //If there are columns selected both at the left of the current row and at the right
            //of the current rown, the ones which are at the right will be deselected
            selection = QItemSelection(index, theModel->index(0, columnCount() - 1, rootIndex));
        }
        break;
    default:
        break;
    }

    selectionModel->select(selection, QItemSelectionModel::Deselect | QItemSelectionModel::Columns);
    return true;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 494, as _ZN16QAccessibleTable5clearEv
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::clear()
{
    view()->selectionModel()->clearSelection();
    return true;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 446, as _ZN16QAccessibleTable6selectEP20QAccessibleInterface
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::select(QAccessibleInterface *childCell)
{
    if (!childCell || childCell->parent() != this) {
        qWarning() << "QAccessibleTable::select: Accessible interface must be a direct child of the table interface.";
        return false;
    }

    if (!childCell->tableCellInterface()) {
        qWarning() << "QAccessibleTable::select: Accessible interface doesn't implement table cell interface.";
        return false;
    }

    if (childCell->role() == QAccessible::Cell || childCell->role() == QAccessible::ListItem || childCell->role() == QAccessible::TreeItem) {
        QAccessibleTableCell* cell = static_cast<QAccessibleTableCell*>(childCell);
        cell->selectCell();
        return true;
    }

    return false;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 467, as _ZN16QAccessibleTable8unselectEP20QAccessibleInterface
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::unselect(QAccessibleInterface *childCell)
{
    if (!childCell || childCell->parent() != this) {
        qWarning() << "QAccessibleTable::select: Accessible interface must be a direct child of the table interface.";
        return false;
    }

    if (!childCell->tableCellInterface()) {
        qWarning() << "QAccessibleTable::unselect: Accessible interface doesn't implement table cell interface.";
        return false;
    }

    if (childCell->role() == QAccessible::Cell || childCell->role() == QAccessible::ListItem || childCell->role() == QAccessible::TreeItem) {
        QAccessibleTableCell* cell = static_cast<QAccessibleTableCell*>(childCell);
        cell->unselectCell();
        return true;
    }

    return false;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 488, as _ZN16QAccessibleTable9selectAllEv
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::selectAll()
{
    view()->selectAll();
    return true;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 63, as _ZN16QAccessibleTableC2EP7QWidgetN11QAccessible4RoleE
#if QT_CONFIG(accessibility)
inline QAccessibleTable::QAccessibleTable(QWidget *w, QAccessible::Role role)
    : QAccessibleWidgetV2(w, role)
{
    Q_ASSERT(view());
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 69, as _ZN16QAccessibleTableD2Ev
#if QT_CONFIG(accessibility)
inline QAccessibleTable::~QAccessibleTable()
{
    for (QAccessible::Id id : std::as_const(childToId))
        QAccessible::deleteAccessibleInterface(id);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1047, as _ZN20QAccessibleTableCellC1EP17QAbstractItemViewRK11QModelIndexN11QAccessible4RoleE
#if QT_CONFIG(accessibility)
inline QAccessibleTableCell::QAccessibleTableCell(QAbstractItemView *view_, const QModelIndex &index_, QAccessible::Role role_)
    : /* QAccessibleSimpleEditableTextInterface(this), */ view(view_), m_index(index_), m_role(role_)
{
    if (Q_UNLIKELY(!index_.isValid()))
        qWarning() << "QAccessibleTableCell::QAccessibleTableCell with invalid index: " << index_;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1359, as _ZN26QAccessibleTableHeaderCellC1EP17QAbstractItemViewiN2Qt11OrientationE
#if QT_CONFIG(accessibility)
inline QAccessibleTableHeaderCell::QAccessibleTableHeaderCell(QAbstractItemView *view_, int index_, Qt::Orientation orientation_)
    : view(view_), index(index_), orientation(orientation_)
{
    Q_ASSERT(index_ >= 0);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 432, as _ZNK16QAccessibleTable10isSelectedEP20QAccessibleInterface
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::isSelected(QAccessibleInterface *childCell) const
{
    if (!childCell || childCell->parent() != this) {
        qWarning() << "QAccessibleTable::isSelected: Accessible interface must be a direct child of the table interface.";
        return false;
    }

    const QAccessibleTableCellInterface *cell = childCell->tableCellInterface();
    if (cell)
        return cell->isSelected();

    return false;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 164, as _ZNK16QAccessibleTable11columnCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTable::columnCount() const
{
    const QAbstractItemView *theView = view();
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return 0;
    const int modelColumnCount = theModel->columnCount(theView->rootIndex());
    return role() == QAccessible::List ? qMin(1, modelColumnCount) : modelColumnCount;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 238, as _ZNK16QAccessibleTable12selectedRowsEv
#if QT_CONFIG(accessibility)
inline QList<int> QAccessibleTable::selectedRows() const
{
    if (!view()->selectionModel())
        return QList<int>();
    QList<int> rows;
    const QModelIndexList selectedRows = view()->selectionModel()->selectedRows();
    rows.reserve(selectedRows.size());
    for (const QModelIndex &index : selectedRows)
        rows.append(index.row());

    return rows;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 213, as _ZNK16QAccessibleTable13selectedCellsEv
#if QT_CONFIG(accessibility)
inline QList<QAccessibleInterface *> QAccessibleTable::selectedCells() const
{
    QList<QAccessibleInterface*> cells;
    if (!view()->selectionModel())
        return cells;
    const QModelIndexList selectedIndexes = view()->selectionModel()->selectedIndexes();
    cells.reserve(selectedIndexes.size());
    for (const QModelIndex &index : selectedIndexes)
        cells.append(child(logicalIndex(index)));
    return cells;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 427, as _ZNK16QAccessibleTable13selectedItemsEv
#if QT_CONFIG(accessibility)
inline QList<QAccessibleInterface*> QAccessibleTable::selectedItems() const
{
    return selectedCells();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 225, as _ZNK16QAccessibleTable15selectedColumnsEv
#if QT_CONFIG(accessibility)
inline QList<int> QAccessibleTable::selectedColumns() const
{
    if (!view()->selectionModel())
        return QList<int>();
    QList<int> columns;
    const QModelIndexList selectedColumns = view()->selectionModel()->selectedColumns();
    columns.reserve(selectedColumns.size());
    for (const QModelIndex &index : selectedColumns)
        columns.append(index.column());

    return columns;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 75, as _ZNK16QAccessibleTable16horizontalHeaderEv
#if QT_CONFIG(accessibility)
inline QHeaderView *QAccessibleTable::horizontalHeader() const
{
    QHeaderView *header = nullptr;
    if (false) {
#if QT_CONFIG(tableview)
    } else if (const QTableView *tv = qobject_cast<const QTableView*>(view())) {
        header = tv->horizontalHeader();
#endif
#if QT_CONFIG(treeview)
    } else if (const QTreeView *tv = qobject_cast<const QTreeView*>(view())) {
        header = tv->header();
#endif
    }
    return header;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 256, as _ZNK16QAccessibleTable16isColumnSelectedEi
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::isColumnSelected(int column) const
{
    if (!view()->selectionModel())
        return false;
    return view()->selectionModel()->isColumnSelected(column, QModelIndex());
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 197, as _ZNK16QAccessibleTable16selectedRowCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTable::selectedRowCount() const
{
    if (!view()->selectionModel())
        return 0;
    return view()->selectionModel()->selectedRows().size();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 155, as _ZNK16QAccessibleTable17columnDescriptionEi
#if QT_CONFIG(accessibility)
inline QString QAccessibleTable::columnDescription(int column) const
{
    const QAbstractItemView *theView = view();
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return QString();
    return theModel->headerData(column, Qt::Horizontal).toString();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 183, as _ZNK16QAccessibleTable17selectedCellCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTable::selectedCellCount() const
{
    if (!view()->selectionModel())
        return 0;
    return view()->selectionModel()->selectedIndexes().size();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 422, as _ZNK16QAccessibleTable17selectedItemCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTable::selectedItemCount() const
{
    return selectedCellCount();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 190, as _ZNK16QAccessibleTable19selectedColumnCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTable::selectedColumnCount() const
{
    if (!view()->selectionModel())
        return 0;
    return view()->selectionModel()->selectedColumns().size();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 36, as _ZNK16QAccessibleTable4viewEv
#if QT_CONFIG(accessibility)
inline QAbstractItemView *QAccessibleTable::view() const
{
    return qobject_cast<QAbstractItemView*>(object());
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 569, as _ZNK16QAccessibleTable6parentEv
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTable::parent() const
{
    if (view() && view()->parent()) {
        if (qstrcmp("QComboBoxPrivateContainer", view()->parent()->metaObject()->className()) == 0) {
            return QAccessible::queryAccessibleInterface(view()->parent()->parent());
        }
        return QAccessible::queryAccessibleInterface(view()->parent());
    }
    return QAccessible::queryAccessibleInterface(qApp);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 150, as _ZNK16QAccessibleTable7captionEv
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTable::caption() const
{
    return nullptr;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 251, as _ZNK16QAccessibleTable7summaryEv
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTable::summary() const
{
    return nullptr;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 773, as _ZNK15QAccessibleTree7childAtEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline QAccessibleInterface *QAccessibleTree::childAt(int x, int y) const
{
    const QAbstractItemView *theView = view();
    if (!theView)
        return nullptr;
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return nullptr;

    const QPoint viewportOffset = theView->viewport()->mapTo(theView, QPoint(0, 0));
    const QPoint indexPosition = theView->mapFromGlobal(QPoint(x, y) - viewportOffset);

    const QModelIndex index = theView->indexAt(indexPosition);
    if (!index.isValid())
        return nullptr;

    const QTreeView *treeView = qobject_cast<const QTreeView *>(theView);
    int row = treeView->d_func()->viewIndex(index) + (horizontalHeader() ? 1 : 0);
    int column = index.column();

    int i = row * theModel->columnCount(theView->rootIndex()) + column;
    return child(i);
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 797, as _ZNK15QAccessibleTree10focusChildEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline QAccessibleInterface *QAccessibleTree::focusChild() const
{
    const QAbstractItemView *theView = view();
    if (!theView)
        return nullptr;
    const QAbstractItemModel *theModel = theView->model();
    const QModelIndex index = theView->currentIndex();
    if (!index.isValid())
        return nullptr;

    const QTreeView *treeView = qobject_cast<const QTreeView *>(theView);
    const int row = treeView->d_func()->viewIndex(index) + (horizontalHeader() ? 1 : 0);
    const int column = index.column();

    int i = row * theModel->columnCount(theView->rootIndex()) + column;
    return child(i);
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 815, as _ZNK15QAccessibleTree10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline int QAccessibleTree::childCount() const
{
    const QTreeView *treeView = qobject_cast<const QTreeView*>(view());
    if (!treeView)
        return 0;
    const QAbstractItemModel *theModel = treeView->model();
    if (!theModel)
        return 0;

    int hHeader = horizontalHeader() ? 1 : 0;
    return (treeView->d_func()->viewItems.size() + hHeader)
            * theModel->columnCount(treeView->rootIndex());
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 829, as _ZNK15QAccessibleTree5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline QAccessibleInterface *QAccessibleTree::child(int logicalIndex) const
{
    QAbstractItemView *theView = view();
    if (!theView)
        return nullptr;
    const QAbstractItemModel *theModel = theView->model();
    const QModelIndex rootIndex = theView->rootIndex();
    if (logicalIndex < 0 || !theModel || !theModel->columnCount(rootIndex))
        return nullptr;

    auto id = childToId.constFind(logicalIndex);
    if (id != childToId.constEnd())
        return QAccessible::accessibleInterface(id.value());

    QAccessibleInterface *iface = nullptr;
    int index = logicalIndex;

    if (horizontalHeader()) {
        if (index < theModel->columnCount(rootIndex))
            iface = new QAccessibleTableHeaderCell(theView, index, Qt::Horizontal);
        else
            index -= theModel->columnCount(rootIndex);
    }

    if (!iface) {
        const int row = index / theModel->columnCount(rootIndex);
        const int column = index % theModel->columnCount(rootIndex);
        const QModelIndex modelIndex = indexFromLogical(row, column);
        if (!modelIndex.isValid())
            return nullptr;
        iface = new QAccessibleTableCell(theView, modelIndex, cellRole());
    }
    QAccessible::registerAccessibleInterface(iface);
    childToId.insert(logicalIndex, QAccessible::uniqueId(iface));
    return iface;
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 874, as _ZNK15QAccessibleTree12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline int QAccessibleTree::indexOfChild(const QAccessibleInterface *iface) const
{
    const QAbstractItemView *theView = view();
    if (!theView)
        return -1;
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return -1;
    QAccessibleInterface *parent = iface->parent();
    if (parent->object() != theView)
        return -1;

    if (iface->role() == QAccessible::TreeItem) {
        const QAccessibleTableCell* cell = static_cast<const QAccessibleTableCell*>(iface);
        const QTreeView *treeView = qobject_cast<const QTreeView *>(theView);
        Q_ASSERT(treeView);
        int row = treeView->d_func()->viewIndex(cell->m_index) + (horizontalHeader() ? 1 : 0);
        int column = cell->m_index.column();

        int index = row * theModel->columnCount(theView->rootIndex()) + column;
        return index;
    } else if (iface->role() == QAccessible::ColumnHeader){
        const QAccessibleTableHeaderCell* cell = static_cast<const QAccessibleTableHeaderCell*>(iface);
        return cell->index;
    } else {
        qWarning() << "WARNING QAccessibleTable::indexOfChild invalid child"
                   << iface->role() << iface->text(QAccessible::Name);
    }
    // FIXME: add scrollbars and don't just ignore them
    return -1;
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 866, as _ZNK15QAccessibleTree8rowCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline int QAccessibleTree::rowCount() const
{
    const QTreeView *treeView = qobject_cast<const QTreeView*>(view());
    if (!treeView)
        return 0;
    return treeView->d_func()->viewItems.size();
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 906, as _ZNK15QAccessibleTree6cellAtEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline QAccessibleInterface *QAccessibleTree::cellAt(int row, int column) const
{
    QModelIndex index = indexFromLogical(row, column);
    if (Q_UNLIKELY(!index.isValid())) {
        qWarning("Requested invalid tree cell: %d %d", row, column);
        return nullptr;
    }
    const QTreeView *treeView = qobject_cast<const QTreeView*>(view());
    Q_ASSERT(treeView);
    int logicalIndex = treeView->d_func()->accessibleTable2Index(index);

    return child(logicalIndex);
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 920, as _ZNK15QAccessibleTree14rowDescriptionEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline QString QAccessibleTree::rowDescription(int) const
{
    return QString(); // no headers for rows in trees
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 925, as _ZNK15QAccessibleTree13isRowSelectedEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline bool QAccessibleTree::isRowSelected(int row) const
{
    if (!view()->selectionModel())
        return false;
    QModelIndex index = indexFromLogical(row);
    return view()->selectionModel()->isRowSelected(index.row(), index.parent());
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 933, as _ZN15QAccessibleTree9selectRowEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline bool QAccessibleTree::selectRow(int row)
{
    if (!view()->selectionModel())
        return false;
    QModelIndex index = indexFromLogical(row);

    if (!index.isValid() || view()->selectionBehavior() == QAbstractItemView::SelectColumns)
        return false;

    switch (view()->selectionMode()) {
    case QAbstractItemView::NoSelection:
        return false;
    case QAbstractItemView::SingleSelection:
        if ((view()->selectionBehavior() != QAbstractItemView::SelectRows) && (columnCount() > 1))
            return false;
        view()->clearSelection();
        break;
    case QAbstractItemView::ContiguousSelection:
        if ((!row || !view()->selectionModel()->isRowSelected(row - 1, view()->rootIndex()))
            && !view()->selectionModel()->isRowSelected(row + 1, view()->rootIndex()))
            view()->clearSelection();
        break;
    default:
        break;
    }

    view()->selectionModel()->select(index, QItemSelectionModel::Select | QItemSelectionModel::Rows);
    return true;
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 755, as _ZNK15QAccessibleTree16indexFromLogicalEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
inline QModelIndex QAccessibleTree::indexFromLogical(int row, int column) const
{
    if (!isValid() || !view()->model())
        return QModelIndex();

    const QTreeView *treeView = qobject_cast<const QTreeView*>(view());
    if (Q_UNLIKELY(row < 0 || column < 0 || treeView->d_func()->viewItems.size() <= row)) {
        qWarning() << "QAccessibleTree::indexFromLogical: invalid index: " << row << column << " for " << treeView;
        return QModelIndex();
    }
    QModelIndex modelIndex = treeView->d_func()->viewItems.at(row).index;

    if (modelIndex.isValid() && column > 0) {
        modelIndex = view()->model()->index(modelIndex.row(), column, modelIndex.parent());
    }
    return modelIndex;
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  QAccessibleInterface *QAccessibleTree::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QAccessibleTree7childAtEii(
    const QAccessibleTree *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  QAccessibleInterface *QAccessibleTree::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QAccessibleTree10focusChildEv(
    const QAccessibleTree *self) {
  return self->focusChild();
}

//  int QAccessibleTree::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAccessibleTree10childCountEv(const QAccessibleTree *self) {
  return self->childCount();
}

//  QAccessibleInterface *QAccessibleTree::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QAccessibleTree5childEi(
    const QAccessibleTree *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleTree::indexOfChild(const QAccessibleInterface *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAccessibleTree12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTree *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  int QAccessibleTree::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAccessibleTree8rowCountEv(const QAccessibleTree *self) {
  return self->rowCount();
}

//  QAccessibleInterface *QAccessibleTree::cellAt(int row, int column) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QAccessibleTree6cellAtEii(
    const QAccessibleTree *self,
    int row,
    int column) {
  return self->cellAt(row, column);
}

//  QString QAccessibleTree::rowDescription(int row) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAccessibleTree14rowDescriptionEi(
    const QAccessibleTree *self,
    int row) {
  return new QString(self->rowDescription(row));
}

//  bool QAccessibleTree::isRowSelected(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAccessibleTree13isRowSelectedEi(
    const QAccessibleTree *self,
    int row) {
  return self->isRowSelected(row);
}

//  bool QAccessibleTree::selectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAccessibleTree9selectRowEi(QAccessibleTree *self, int row) {
  return self->selectRow(row);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  QModelIndex QAccessibleTree::indexFromLogical(int row, int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK15QAccessibleTree16indexFromLogicalEii(
    const QAccessibleTree *self,
    int row,
    int column) {
  return new QModelIndex(self->indexFromLogical(row, column));
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  QAccessibleInterface *QAccessibleTree::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK15QAccessibleTree7childAtEii(
    const QAccessibleTree *self,
    int x,
    int y) {
  return self->QAccessibleTree::childAt(x, y);
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  QAccessibleInterface *QAccessibleTree::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK15QAccessibleTree10focusChildEv(
    const QAccessibleTree *self) {
  return self->QAccessibleTree::focusChild();
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  int QAccessibleTree::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QAccessibleTree10childCountEv(
    const QAccessibleTree *self) {
  return self->QAccessibleTree::childCount();
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  int QAccessibleTree::indexOfChild(const QAccessibleInterface *a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QAccessibleTree12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTree *self,
    const QAccessibleInterface *a0) {
  return self->QAccessibleTree::indexOfChild(a0);
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  int QAccessibleTree::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QAccessibleTree8rowCountEv(const QAccessibleTree *self) {
  return self->QAccessibleTree::rowCount();
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  QAccessibleInterface *QAccessibleTree::cellAt(int row, int column) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK15QAccessibleTree6cellAtEii(
    const QAccessibleTree *self,
    int row,
    int column) {
  return self->QAccessibleTree::cellAt(row, column);
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  QString QAccessibleTree::rowDescription(int row) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QAccessibleTree14rowDescriptionEi(
    const QAccessibleTree *self,
    int row) {
  return new QString(self->QAccessibleTree::rowDescription(row));
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  bool QAccessibleTree::isRowSelected(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QAccessibleTree13isRowSelectedEi(
    const QAccessibleTree *self,
    int row) {
  return self->QAccessibleTree::isRowSelected(row);
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
//  bool QAccessibleTree::selectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAccessibleTree9selectRowEi(
    QAccessibleTree *self,
    int row) {
  return self->QAccessibleTree::selectRow(row);
}
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
