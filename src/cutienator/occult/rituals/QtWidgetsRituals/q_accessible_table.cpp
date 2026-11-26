//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility) && QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/itemviews_p.h>
#include <QtWidgets/qheaderview.h>
#if QT_CONFIG(tableview)
#include <QtWidgets/qtableview.h>
#endif
#if QT_CONFIG(listview)
#include <QtWidgets/qlistview.h>
#endif
#if QT_CONFIG(treeview)
#include <QtWidgets/qtreeview.h>
#include <QtWidgets/private/qtreeview_p.h>
#endif
#include <QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from src/widgets/accessible/itemviews.cpp, line 270, as _ZN16QAccessibleTable9selectRowEi
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::selectRow(int row)
{
    QAbstractItemView *theView = view();
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel || !view()->selectionModel())
        return false;

    const QModelIndex rootIndex = theView->rootIndex();
    const QModelIndex index = theModel->index(row, 0, rootIndex);

    if (!index.isValid() || view()->selectionBehavior() == QAbstractItemView::SelectColumns)
        return false;

    switch (view()->selectionMode()) {
    case QAbstractItemView::NoSelection:
        return false;
    case QAbstractItemView::SingleSelection:
        if (view()->selectionBehavior() != QAbstractItemView::SelectRows && columnCount() > 1 )
            return false;
        view()->clearSelection();
        break;
    case QAbstractItemView::ContiguousSelection:
        if ((!row || !theView->selectionModel()->isRowSelected(row - 1, rootIndex))
            && !theView->selectionModel()->isRowSelected(row + 1, rootIndex)) {
            theView->clearSelection();
        }
        break;
    default:
        break;
    }

    view()->selectionModel()->select(index, QItemSelectionModel::Select | QItemSelectionModel::Rows);
    return true;
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

//  from src/widgets/accessible/itemviews.cpp, line 522, as _ZNK16QAccessibleTable10childCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTable::childCount() const
{
    const QAbstractItemView *theView = view();
    if (!theView)
        return 0;
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return 0;
    const QModelIndex rootIndex = theView->rootIndex();
    int vHeader = verticalHeader() ? 1 : 0;
    int hHeader = horizontalHeader() ? 1 : 0;
    return (theModel->rowCount(rootIndex) + hHeader) * (columnCount() + vHeader);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 513, as _ZNK16QAccessibleTable10focusChildEv
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTable::focusChild() const
{
    QModelIndex index = view()->currentIndex();
    if (!index.isValid())
        return nullptr;

    return child(logicalIndex(index));
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

//  from src/widgets/accessible/itemviews.cpp, line 536, as _ZNK16QAccessibleTable12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
inline int QAccessibleTable::indexOfChild(const QAccessibleInterface *iface) const
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

    const QModelIndex rootIndex = theView->rootIndex();
    Q_ASSERT(iface->role() != QAccessible::TreeItem); // should be handled by tree class
    if (iface->role() == QAccessible::Cell || iface->role() == QAccessible::ListItem) {
        const QAccessibleTableCell* cell = static_cast<const QAccessibleTableCell*>(iface);
        return logicalIndex(cell->m_index);
    } else if (iface->role() == QAccessible::ColumnHeader){
        const QAccessibleTableHeaderCell* cell = static_cast<const QAccessibleTableHeaderCell*>(iface);
        return cell->index + (verticalHeader() ? 1 : 0);
    } else if (iface->role() == QAccessible::RowHeader){
        const QAccessibleTableHeaderCell* cell = static_cast<const QAccessibleTableHeaderCell*>(iface);
        return (cell->index + 1) * (theModel->columnCount(rootIndex) + 1);
    } else if (iface->role() == QAccessible::Pane) {
        return 0; // corner button
    } else {
        qWarning() << "WARNING QAccessibleTable::indexOfChild Fix my children..."
                   << iface->role() << iface->text(QAccessible::Name);
    }
    // FIXME: we are in denial of our children. this should stop.
    return -1;
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

//  from src/widgets/accessible/itemviews.cpp, line 263, as _ZNK16QAccessibleTable13isRowSelectedEi
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::isRowSelected(int row) const
{
    if (!view()->selectionModel())
        return false;
    return view()->selectionModel()->isRowSelected(row, QModelIndex());
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

//  from src/widgets/accessible/itemviews.cpp, line 204, as _ZNK16QAccessibleTable14rowDescriptionEi
#if QT_CONFIG(accessibility)
inline QString QAccessibleTable::rowDescription(int row) const
{
    const QAbstractItemView *theView = view();
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return QString();
    return theModel->headerData(row, Qt::Vertical).toString();
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

//  from src/widgets/accessible/itemviews.cpp, line 580, as _ZNK16QAccessibleTable5childEi
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTable::child(int logicalIndex) const
{
    QAbstractItemView *theView = view();
    if (!theView)
        return nullptr;

    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return nullptr;

    const QModelIndex rootIndex = theView->rootIndex();
    auto id = childToId.constFind(logicalIndex);
    if (id != childToId.constEnd())
        return QAccessible::accessibleInterface(id.value());

    int vHeader = verticalHeader() ? 1 : 0;
    int hHeader = horizontalHeader() ? 1 : 0;

    int columns = theModel->columnCount(rootIndex) + vHeader;

    int row = logicalIndex / columns;
    int column = logicalIndex % columns;

    QAccessibleInterface *iface = nullptr;

    if (vHeader) {
        if (column == 0) {
            if (hHeader && row == 0) {
                iface = new QAccessibleTableCornerButton(theView);
            } else {
                iface = new QAccessibleTableHeaderCell(theView, row - hHeader, Qt::Vertical);
            }
        }
        --column;
    }
    if (!iface && hHeader) {
        if (row == 0) {
            iface = new QAccessibleTableHeaderCell(theView, column, Qt::Horizontal);
        }
        --row;
    }

    if (!iface) {
        QModelIndex index = theModel->index(row, column, rootIndex);
        if (Q_UNLIKELY(!index.isValid())) {
            qWarning("QAccessibleTable::child: Invalid index at: %d %d", row, column);
            return nullptr;
        }
        iface = new QAccessibleTableCell(theView, index, cellRole());
    }

    QAccessible::registerAccessibleInterface(iface);
    childToId.insert(logicalIndex, QAccessible::uniqueId(iface));
    return iface;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 118, as _ZNK16QAccessibleTable6cellAtEii
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTable::cellAt(int row, int column) const
{
    const QAbstractItemView *theView = view();
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return nullptr;
    Q_ASSERT(role() != QAccessible::List);
    Q_ASSERT(role() != QAccessible::Tree);

    const int vHeader = verticalHeader() ? 1 : 0;
    const int hHeader = horizontalHeader() ? 1 : 0;

    const int doHHeader = ((row == -1) && hHeader);
    const int doVHeader = ((column == -1) && vHeader);

    if (doVHeader && doHHeader)
        return child(0);

    if (doVHeader)
        return child((row + hHeader) * (columnCount() + vHeader) + (column + vHeader));

    if (doHHeader)
        return child((row + hHeader) * (columnCount() + vHeader) + (column + vHeader));

    QModelIndex index = theModel->index(row, column, theView->rootIndex());
    if (Q_UNLIKELY(!index.isValid())) {
        qWarning() << "QAccessibleTable::cellAt: invalid index: " << index << " for " << theView;
        return nullptr;
    }
    return child(logicalIndex(index));
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

//  from src/widgets/accessible/itemviews.cpp, line 501, as _ZNK16QAccessibleTable7childAtEii
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTable::childAt(int x, int y) const
{
    QPoint viewportOffset = view()->viewport()->mapTo(view(), QPoint(0,0));
    QPoint indexPosition = view()->mapFromGlobal(QPoint(x, y) - viewportOffset);
    // FIXME: if indexPosition < 0 in one coordinate, return header

    const QModelIndex index = view()->indexAt(indexPosition);
    if (index.isValid())
        return child(logicalIndex(index));
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

//  from src/widgets/accessible/itemviews.cpp, line 174, as _ZNK16QAccessibleTable8rowCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTable::rowCount() const
{
    const QAbstractItemView *theView = view();
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return 0;
    return theModel->rowCount(theView->rootIndex());
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

//  from src/widgets/accessible/itemviews.cpp, line 1184, as _ZN20QAccessibleTableCell10selectCellEv
#if QT_CONFIG(accessibility)
inline void QAccessibleTableCell::selectCell()
{
    if (!isValid())
        return;
    QAbstractItemView::SelectionMode selectionMode = view->selectionMode();
    if (selectionMode == QAbstractItemView::NoSelection)
        return;
    Q_ASSERT(table());
    QAccessibleTableInterface *cellTable = table()->tableInterface();

    switch (view->selectionBehavior()) {
    case QAbstractItemView::SelectItems:
        break;
    case QAbstractItemView::SelectColumns:
        if (cellTable)
            cellTable->selectColumn(m_index.column());
        return;
    case QAbstractItemView::SelectRows:
        if (cellTable)
            cellTable->selectRow(m_index.row());
        return;
    }

    if (selectionMode == QAbstractItemView::SingleSelection) {
        view->clearSelection();
    }

    view->selectionModel()->select(m_index, QItemSelectionModel::Select);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1214, as _ZN20QAccessibleTableCell12unselectCellEv
#if QT_CONFIG(accessibility)
inline void QAccessibleTableCell::unselectCell()
{
    if (!isValid())
        return;
    QAbstractItemView::SelectionMode selectionMode = view->selectionMode();
    if (selectionMode == QAbstractItemView::NoSelection)
        return;

    QAccessibleTableInterface *cellTable = table()->tableInterface();

    switch (view->selectionBehavior()) {
    case QAbstractItemView::SelectItems:
        break;
    case QAbstractItemView::SelectColumns:
        if (cellTable)
            cellTable->unselectColumn(m_index.column());
        return;
    case QAbstractItemView::SelectRows:
        if (cellTable)
            cellTable->unselectRow(m_index.row());
        return;
    }

    //If the mode is not MultiSelection or ExtendedSelection and only
    //one cell is selected it cannot be unselected by the user
    if ((selectionMode != QAbstractItemView::MultiSelection)
        && (selectionMode != QAbstractItemView::ExtendedSelection)
        && (view->selectionModel()->selectedIndexes().size() <= 1))
        return;

    view->selectionModel()->select(m_index, QItemSelectionModel::Deselect);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1054, as _ZN20QAccessibleTableCell14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
inline void *QAccessibleTableCell::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::TableCellInterface)
        return static_cast<QAccessibleTableCellInterface*>(this);
    if (t == QAccessible::ActionInterface)
        return static_cast<QAccessibleActionInterface*>(this);
    return nullptr;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1252, as _ZNK20QAccessibleTableCell4roleEv
#if QT_CONFIG(accessibility)
inline QAccessible::Role QAccessibleTableCell::role() const
{
    return m_role;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1257, as _ZNK20QAccessibleTableCell5stateEv
#if QT_CONFIG(accessibility)
inline QAccessible::State QAccessibleTableCell::state() const
{
    QAccessible::State st;
    if (!isValid())
        return st;

    QRect globalRect = view->rect();
    globalRect.translate(view->mapToGlobal(QPoint(0,0)));
    if (!globalRect.intersects(rect()))
        st.invisible = true;

    if (view->selectionModel()->isSelected(m_index))
        st.selected = true;
    if (view->selectionModel()->currentIndex() == m_index)
        st.focused = true;

    const QVariant checkState = m_index.data(Qt::CheckStateRole);
    if (checkState.toInt() == Qt::Checked)
        st.checked = true;

    Qt::ItemFlags flags = m_index.flags();
    if ((flags & Qt::ItemIsUserCheckable) && checkState.isValid())
        st.checkable = true;
    if (flags & Qt::ItemIsSelectable) {
        st.selectable = true;
        st.focusable = true;
        if (view->selectionMode() == QAbstractItemView::MultiSelection)
            st.multiSelectable = true;
        if (view->selectionMode() == QAbstractItemView::ExtendedSelection)
            st.extSelectable = true;
    }
#if QT_CONFIG(treeview)
    if (m_role == QAccessible::TreeItem) {
        const QTreeView *treeView = qobject_cast<const QTreeView*>(view);
        if (treeView->model()->hasChildren(m_index))
            st.expandable = true;
        if (treeView->isExpanded(m_index))
            st.expanded = true;
    }
#endif
    return st;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1301, as _ZNK20QAccessibleTableCell4rectEv
#if QT_CONFIG(accessibility)
inline QRect QAccessibleTableCell::rect() const
{
    QRect r;
    if (!isValid())
        return r;
    r = view->visualRect(m_index);

    if (!r.isNull()) {
        r.translate(view->viewport()->mapTo(view, QPoint(0,0)));
        r.translate(view->mapToGlobal(QPoint(0, 0)));
    }
    return r;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1343, as _ZNK20QAccessibleTableCell7isValidEv
#if QT_CONFIG(accessibility)
inline bool QAccessibleTableCell::isValid() const
{
    return view && !qt_widget_private(view)->data.in_destructor
            && view->model() && m_index.isValid();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1315, as _ZNK20QAccessibleTableCell4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
inline QString QAccessibleTableCell::text(QAccessible::Text t) const
{
    QString value;
    if (!isValid())
        return value;
    QAbstractItemModel *model = view->model();
    switch (t) {
    case QAccessible::Name:
        value = model->data(m_index, Qt::AccessibleTextRole).toString();
        if (value.isEmpty())
            value = model->data(m_index, Qt::DisplayRole).toString();
        break;
    case QAccessible::Description:
        value = model->data(m_index, Qt::AccessibleDescriptionRole).toString();
        break;
    default:
        break;
    }
    return value;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1336, as _ZN20QAccessibleTableCell7setTextEN11QAccessible4TextERK7QString
#if QT_CONFIG(accessibility)
inline void QAccessibleTableCell::setText(QAccessible::Text /*t*/, const QString &text)
{
    if (!isValid() || !(m_index.flags() & Qt::ItemIsEditable))
        return;
    view->model()->setData(m_index, text);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1349, as _ZNK20QAccessibleTableCell6parentEv
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTableCell::parent() const
{
    return QAccessible::queryAccessibleInterface(view);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1354, as _ZNK20QAccessibleTableCell5childEi
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTableCell::child(int) const
{
    return nullptr;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1063, as _ZNK20QAccessibleTableCell12columnExtentEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTableCell::columnExtent() const { return 1; }
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1076, as _ZNK20QAccessibleTableCell17columnHeaderCellsEv
#if QT_CONFIG(accessibility)
inline QList<QAccessibleInterface*> QAccessibleTableCell::columnHeaderCells() const
{
    QList<QAccessibleInterface*> headerCell;
    if (horizontalHeader()) {
        // FIXME
        headerCell.append(new QAccessibleTableHeaderCell(view, m_index.column(), Qt::Horizontal));
    }
    return headerCell;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1114, as _ZNK20QAccessibleTableCell11columnIndexEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTableCell::columnIndex() const
{
    if (!isValid())
        return -1;
#if QT_CONFIG(listview)
    if (role() == QAccessible::ListItem) {
        return 0;
    }
#endif
    return m_index.column();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1064, as _ZNK20QAccessibleTableCell9rowExtentEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTableCell::rowExtent() const { return 1; }
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1066, as _ZNK20QAccessibleTableCell14rowHeaderCellsEv
#if QT_CONFIG(accessibility)
inline QList<QAccessibleInterface*> QAccessibleTableCell::rowHeaderCells() const
{
    QList<QAccessibleInterface*> headerCell;
    if (verticalHeader()) {
        // FIXME
        headerCell.append(new QAccessibleTableHeaderCell(view, m_index.row(), Qt::Vertical));
    }
    return headerCell;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1126, as _ZNK20QAccessibleTableCell8rowIndexEv
#if QT_CONFIG(accessibility)
inline int QAccessibleTableCell::rowIndex() const
{
    if (!isValid())
        return -1;
#if QT_CONFIG(treeview)
    if (role() == QAccessible::TreeItem) {
       const QTreeView *treeView = qobject_cast<const QTreeView*>(view);
       Q_ASSERT(treeView);
       int row = treeView->d_func()->viewIndex(m_index);
       return row;
    }
#endif
    return m_index.row();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1141, as _ZNK20QAccessibleTableCell10isSelectedEv
#if QT_CONFIG(accessibility)
inline bool QAccessibleTableCell::isSelected() const
{
    if (!isValid())
        return false;
    return view->selectionModel()->isSelected(m_index);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1247, as _ZNK20QAccessibleTableCell5tableEv
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTableCell::table() const
{
    return QAccessible::queryAccessibleInterface(view);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1148, as _ZNK20QAccessibleTableCell11actionNamesEv
#if QT_CONFIG(accessibility)
inline QStringList QAccessibleTableCell::actionNames() const
{
    QStringList names;
    names << toggleAction();
    return names;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1155, as _ZN20QAccessibleTableCell8doActionERK7QString
#if QT_CONFIG(accessibility)
#if defined(Q_OS_LINUX)
inline void QAccessibleTableCell::doAction(const QString& actionName)
{
    if (actionName == toggleAction()) {
#if defined(Q_OS_ANDROID)
        QAccessibleInterface *parentInterface = parent();
        while (parentInterface){
            if (parentInterface->role() == QAccessible::ComboBox) {
                selectCell();
                parentInterface->actionInterface()->doAction(pressAction());
                return;
            } else {
                parentInterface = parentInterface->parent();
            }
        }
#endif
        if (isSelected()) {
            unselectCell();
        } else {
            selectCell();
        }
    }
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1178, as _ZNK20QAccessibleTableCell20keyBindingsForActionERK7QString
#if QT_CONFIG(accessibility)
inline QStringList QAccessibleTableCell::keyBindingsForAction(const QString &) const
{
    return QStringList();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1365, as _ZNK26QAccessibleTableHeaderCell4roleEv
#if QT_CONFIG(accessibility)
inline QAccessible::Role QAccessibleTableHeaderCell::role() const
{
    if (orientation == Qt::Horizontal)
        return QAccessible::ColumnHeader;
    return QAccessible::RowHeader;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1372, as _ZNK26QAccessibleTableHeaderCell5stateEv
#if QT_CONFIG(accessibility)
inline QAccessible::State QAccessibleTableHeaderCell::state() const
{
    QAccessible::State s;
    if (QHeaderView *h = headerView()) {
        s.invisible = !h->testAttribute(Qt::WA_WState_Visible);
        s.disabled = !h->isEnabled();
    }
    return s;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1382, as _ZNK26QAccessibleTableHeaderCell4rectEv
#if QT_CONFIG(accessibility)
inline QRect QAccessibleTableHeaderCell::rect() const
{
    QHeaderView *header = nullptr;
    if (false) {
#if QT_CONFIG(tableview)
    } else if (const QTableView *tv = qobject_cast<const QTableView*>(view)) {
        if (orientation == Qt::Horizontal) {
            header = tv->horizontalHeader();
        } else {
            header = tv->verticalHeader();
        }
#endif
#if QT_CONFIG(treeview)
    } else if (const QTreeView *tv = qobject_cast<const QTreeView*>(view)) {
        header = tv->header();
#endif
    }
    if (!header)
        return QRect();
    QPoint zero = header->mapToGlobal(QPoint(0, 0));
    int sectionSize = header->sectionSize(index);
    int sectionPos = header->sectionPosition(index);
    return orientation == Qt::Horizontal
            ? QRect(zero.x() + sectionPos, zero.y(), sectionSize, header->height())
            : QRect(zero.x(), zero.y() + sectionPos, header->width(), sectionSize);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1433, as _ZNK26QAccessibleTableHeaderCell7isValidEv
#if QT_CONFIG(accessibility)
inline bool QAccessibleTableHeaderCell::isValid() const
{
    const QAbstractItemModel *theModel = view && !qt_widget_private(view)->data.in_destructor
                                       ? view->model() : nullptr;
    if (!theModel)
        return false;
    const QModelIndex rootIndex = view->rootIndex();
    return (index >= 0) && ((orientation == Qt::Horizontal)
                        ? (index < theModel->columnCount(rootIndex))
                        : (index < theModel->rowCount(rootIndex)));
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1409, as _ZNK26QAccessibleTableHeaderCell4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
inline QString QAccessibleTableHeaderCell::text(QAccessible::Text t) const
{
    QAbstractItemModel *model = view->model();
    QString value;
    switch (t) {
    case QAccessible::Name:
        value = model->headerData(index, orientation, Qt::AccessibleTextRole).toString();
        if (value.isEmpty())
            value = model->headerData(index, orientation, Qt::DisplayRole).toString();
        break;
    case QAccessible::Description:
        value = model->headerData(index, orientation, Qt::AccessibleDescriptionRole).toString();
        break;
    default:
        break;
    }
    return value;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1428, as _ZN26QAccessibleTableHeaderCell7setTextEN11QAccessible4TextERK7QString
#if QT_CONFIG(accessibility)
inline void QAccessibleTableHeaderCell::setText(QAccessible::Text, const QString &)
{
    return;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1445, as _ZNK26QAccessibleTableHeaderCell6parentEv
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTableHeaderCell::parent() const
{
    return QAccessible::queryAccessibleInterface(view);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1450, as _ZNK26QAccessibleTableHeaderCell5childEi
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleTableHeaderCell::child(int) const
{
    return nullptr;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1104, as _ZNK20QAccessibleTableCell14verticalHeaderEv
#if QT_CONFIG(accessibility)
inline QHeaderView *QAccessibleTableCell::verticalHeader() const
{
    QHeaderView *header = nullptr;
#if QT_CONFIG(tableview)
    if (const QTableView *tv = qobject_cast<const QTableView*>(view))
        header = tv->verticalHeader();
#endif
    return header;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1086, as _ZNK20QAccessibleTableCell16horizontalHeaderEv
#if QT_CONFIG(accessibility)
inline QHeaderView *QAccessibleTableCell::horizontalHeader() const
{
    QHeaderView *header = nullptr;

    if (false) {
#if QT_CONFIG(tableview)
    } else if (const QTableView *tv = qobject_cast<const QTableView*>(view)) {
        header = tv->horizontalHeader();
#endif
#if QT_CONFIG(treeview)
    } else if (const QTreeView *tv = qobject_cast<const QTreeView*>(view)) {
        header = tv->header();
#endif
    }

    return header;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1455, as _ZNK26QAccessibleTableHeaderCell10headerViewEv
#if QT_CONFIG(accessibility)
inline QHeaderView *QAccessibleTableHeaderCell::headerView() const
{
    QHeaderView *header = nullptr;
    if (false) {
#if QT_CONFIG(tableview)
    } else if (const QTableView *tv = qobject_cast<const QTableView*>(view)) {
        if (orientation == Qt::Horizontal) {
            header = tv->horizontalHeader();
        } else {
            header = tv->verticalHeader();
        }
#endif
#if QT_CONFIG(treeview)
    } else if (const QTreeView *tv = qobject_cast<const QTreeView*>(view)) {
        header = tv->header();
#endif
    }
    return header;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 36, as _ZNK16QAccessibleTable4viewEv
#if QT_CONFIG(accessibility)
inline QAbstractItemView *QAccessibleTable::view() const
{
    return qobject_cast<QAbstractItemView*>(object());
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

//  from src/widgets/accessible/itemviews.cpp, line 91, as _ZNK16QAccessibleTable14verticalHeaderEv
#if QT_CONFIG(accessibility)
inline QHeaderView *QAccessibleTable::verticalHeader() const
{
    QHeaderView *header = nullptr;
    if (false) {
#if QT_CONFIG(tableview)
    } else if (const QTableView *tv = qobject_cast<const QTableView*>(view())) {
        header = tv->verticalHeader();
#endif
    }
    return header;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 41, as _ZNK16QAccessibleTable12logicalIndexERK11QModelIndex
#if QT_CONFIG(accessibility)
inline int QAccessibleTable::logicalIndex(const QModelIndex &index) const
{
    const QAbstractItemModel *theModel = index.model();
    if (!theModel || !index.isValid())
        return -1;

#if QT_CONFIG(listview)
    if (role() == QAccessible::List) {
        if (index.column() != qobject_cast<const QListView*>(view())->modelColumn())
            return -1;
        else
            return index.row();
    } else
#endif
    {
        const int vHeader = verticalHeader() ? 1 : 0;
        const int hHeader = horizontalHeader() ? 1 : 0;
        return (index.row() + hHeader) * (columnCount() + vHeader)
             + (index.column() + vHeader);
    }
}
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleTable that Python can take functions over in. Every QAccessibleTable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleTableCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleTableCall1)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleTableCall2)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleTableCall3)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleTableCall4)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleTableCall5)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleTableCall6)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleTableCall7)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleTableCall8)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleTableCall9)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef QString * (*CuteQAccessibleTableCall10)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef QString * (*CuteQAccessibleTableCall11)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleTableCall12)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleTableCall13)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleTableCall14)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleTableCall15)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleTableCall16)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall17)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall18)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall19)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall20)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall21)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall22)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleTableCall23)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall24)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall25)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall26)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall27)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleTableCall28)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAccessibleTableCall29)(const void *, QAccessibleTableModelChangeEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleTableCall30)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTableCall31)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTableCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleTableCall33)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTableCall34)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTableCall35)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleTableCall36)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTableCall37)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTableCall38)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTableCall39)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTableCall40)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTableCall41)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTableCall42)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTableCall43)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTableCall44)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTableCall45)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleTable : public QAccessibleTable {
public:
  using QAccessibleTable::QAccessibleTable;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface6cellAtEii")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface7captionEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface7summaryEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface17columnDescriptionEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface14rowDescriptionEi")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface11columnCountEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface8rowCountEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface17selectedCellCountEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface19selectedColumnCountEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface16selectedRowCountEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface16isColumnSelectedEi")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface13isRowSelectedEi")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface9selectRowEi")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface12selectColumnEi")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface11unselectRowEi")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface14unselectColumnEi")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface17selectedItemCountEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface10isSelectedEP20QAccessibleInterface")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface6selectEP20QAccessibleInterface")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface8unselectEP20QAccessibleInterface")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface9selectAllEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface5clearEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface11modelChangeEP32QAccessibleTableModelChangeEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface12selectedItemEi")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface12virtual_hookEiPv")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QAccessibleInterface *QAccessibleTable::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleTableCall0 call = reinterpret_cast<CuteQAccessibleTableCall0>(taken[0]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTable::childAt(x, y);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QAccessibleInterface *QAccessibleTable::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleTableCall1 call = reinterpret_cast<CuteQAccessibleTableCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTable::focusChild();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  int QAccessibleTable::childCount() const
  int childCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleTableCall2 call = reinterpret_cast<CuteQAccessibleTableCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::childCount();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  int QAccessibleTable::indexOfChild(const QAccessibleInterface *a0)
  //      const
  int indexOfChild(const QAccessibleInterface *a0) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleTableCall3 call = reinterpret_cast<CuteQAccessibleTableCall3>(taken[3]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::indexOfChild(a0);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QAccessibleInterface *QAccessibleTable::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleTableCall4 call = reinterpret_cast<CuteQAccessibleTableCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTable::parent();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QAccessibleInterface *QAccessibleTable::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleTableCall5 call = reinterpret_cast<CuteQAccessibleTableCall5>(taken[5]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTable::child(index);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  void *QAccessibleTable::interface_cast(QAccessible::InterfaceType t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleTableCall6 call = reinterpret_cast<CuteQAccessibleTableCall6>(taken[6]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleTable::interface_cast(t);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QAccessibleInterface *QAccessibleTable::cellAt(int row, int column)
  //      const
  QAccessibleInterface *cellAt(int row, int column) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleTableCall7 call = reinterpret_cast<CuteQAccessibleTableCall7>(taken[7]);
      void * given = call(this, row, column, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTable::cellAt(row, column);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QAccessibleInterface *QAccessibleTable::caption() const
  QAccessibleInterface *caption() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleTableCall8 call = reinterpret_cast<CuteQAccessibleTableCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTable::caption();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QAccessibleInterface *QAccessibleTable::summary() const
  QAccessibleInterface *summary() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleTableCall9 call = reinterpret_cast<CuteQAccessibleTableCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTable::summary();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QString QAccessibleTable::columnDescription(int column) const
  QString columnDescription(int column) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleTableCall10 call = reinterpret_cast<CuteQAccessibleTableCall10>(taken[10]);
      QString * given = call(this, column, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleTable::columnDescription(column);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QString QAccessibleTable::rowDescription(int row) const
  QString rowDescription(int row) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleTableCall11 call = reinterpret_cast<CuteQAccessibleTableCall11>(taken[11]);
      QString * given = call(this, row, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleTable::rowDescription(row);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  int QAccessibleTable::columnCount() const
  int columnCount() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleTableCall12 call = reinterpret_cast<CuteQAccessibleTableCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::columnCount();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  int QAccessibleTable::rowCount() const
  int rowCount() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleTableCall13 call = reinterpret_cast<CuteQAccessibleTableCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::rowCount();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  int QAccessibleTable::selectedCellCount() const
  int selectedCellCount() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleTableCall14 call = reinterpret_cast<CuteQAccessibleTableCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::selectedCellCount();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  int QAccessibleTable::selectedColumnCount() const
  int selectedColumnCount() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleTableCall15 call = reinterpret_cast<CuteQAccessibleTableCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::selectedColumnCount();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  int QAccessibleTable::selectedRowCount() const
  int selectedRowCount() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleTableCall16 call = reinterpret_cast<CuteQAccessibleTableCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::selectedRowCount();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::isColumnSelected(int column) const
  bool isColumnSelected(int column) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleTableCall17 call = reinterpret_cast<CuteQAccessibleTableCall17>(taken[17]);
      bool given = call(this, column, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::isColumnSelected(column);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::isRowSelected(int row) const
  bool isRowSelected(int row) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleTableCall18 call = reinterpret_cast<CuteQAccessibleTableCall18>(taken[18]);
      bool given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::isRowSelected(row);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::selectRow(int row)
  bool selectRow(int row) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleTableCall19 call = reinterpret_cast<CuteQAccessibleTableCall19>(taken[19]);
      bool given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::selectRow(row);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::selectColumn(int column)
  bool selectColumn(int column) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleTableCall20 call = reinterpret_cast<CuteQAccessibleTableCall20>(taken[20]);
      bool given = call(this, column, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::selectColumn(column);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::unselectRow(int row)
  bool unselectRow(int row) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleTableCall21 call = reinterpret_cast<CuteQAccessibleTableCall21>(taken[21]);
      bool given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::unselectRow(row);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::unselectColumn(int column)
  bool unselectColumn(int column) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleTableCall22 call = reinterpret_cast<CuteQAccessibleTableCall22>(taken[22]);
      bool given = call(this, column, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::unselectColumn(column);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  int QAccessibleTable::selectedItemCount() const
  int selectedItemCount() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleTableCall23 call = reinterpret_cast<CuteQAccessibleTableCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::selectedItemCount();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::isSelected(QAccessibleInterface *childCell)
  //      const
  bool isSelected(QAccessibleInterface *childCell) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleTableCall24 call = reinterpret_cast<CuteQAccessibleTableCall24>(taken[24]);
      bool given = call(this, childCell, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::isSelected(childCell);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::select(QAccessibleInterface *childCell)
  bool select(QAccessibleInterface *childCell) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleTableCall25 call = reinterpret_cast<CuteQAccessibleTableCall25>(taken[25]);
      bool given = call(this, childCell, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::select(childCell);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::unselect(QAccessibleInterface *childCell)
  bool unselect(QAccessibleInterface *childCell) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleTableCall26 call = reinterpret_cast<CuteQAccessibleTableCall26>(taken[26]);
      bool given = call(this, childCell, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::unselect(childCell);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::selectAll()
  bool selectAll() override {
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleTableCall27 call = reinterpret_cast<CuteQAccessibleTableCall27>(taken[27]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::selectAll();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  bool QAccessibleTable::clear()
  bool clear() override {
    if (taken[28]) {
      int handled = 0;
      CuteQAccessibleTableCall28 call = reinterpret_cast<CuteQAccessibleTableCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::clear();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  void QAccessibleTable::modelChange(QAccessibleTableModelChangeEvent
  //      *event)
  void modelChange(QAccessibleTableModelChangeEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAccessibleTableCall29 call = reinterpret_cast<CuteQAccessibleTableCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAccessibleTable::modelChange(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQAccessibleTableCall30 call = reinterpret_cast<CuteQAccessibleTableCall30>(taken[30]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQAccessibleTableCall31 call = reinterpret_cast<CuteQAccessibleTableCall31>(taken[31]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQAccessibleTableCall32 call = reinterpret_cast<CuteQAccessibleTableCall32>(taken[32]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQAccessibleTableCall33 call = reinterpret_cast<CuteQAccessibleTableCall33>(taken[33]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQAccessibleTableCall34 call = reinterpret_cast<CuteQAccessibleTableCall34>(taken[34]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleWidget::text(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQAccessibleTableCall35 call = reinterpret_cast<CuteQAccessibleTableCall35>(taken[35]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQAccessibleTableCall36 call = reinterpret_cast<CuteQAccessibleTableCall36>(taken[36]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQAccessibleTableCall37 call = reinterpret_cast<CuteQAccessibleTableCall37>(taken[37]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQAccessibleTableCall38 call = reinterpret_cast<CuteQAccessibleTableCall38>(taken[38]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[39]) {
      int handled = 0;
      CuteQAccessibleTableCall39 call = reinterpret_cast<CuteQAccessibleTableCall39>(taken[39]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQAccessibleTableCall40 call = reinterpret_cast<CuteQAccessibleTableCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleObject::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[41]) {
      int handled = 0;
      CuteQAccessibleTableCall41 call = reinterpret_cast<CuteQAccessibleTableCall41>(taken[41]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleSelectionInterface::selectedItem(int
  //      selectionIndex) const
  QAccessibleInterface *selectedItem(int selectionIndex) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQAccessibleTableCall42 call = reinterpret_cast<CuteQAccessibleTableCall42>(taken[42]);
      void * given = call(this, selectionIndex, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleSelectionInterface::selectedItem(selectionIndex);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[43]) {
      int handled = 0;
      CuteQAccessibleTableCall43 call = reinterpret_cast<CuteQAccessibleTableCall43>(taken[43]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QAccessibleInterface::virtual_hook(id, data);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQAccessibleTableCall44 call = reinterpret_cast<CuteQAccessibleTableCall44>(taken[44]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionName(name);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionDescription(const
  //      QString &name) const
  QString localizedActionDescription(const QString &name) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQAccessibleTableCall45 call = reinterpret_cast<CuteQAccessibleTableCall45>(taken[45]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionDescription(name);
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleInterface *QAccessibleTable::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleTable7childAtEii(
    const QAccessibleTable *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  QAccessibleInterface *QAccessibleTable::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleTable10focusChildEv(
    const QAccessibleTable *self) {
  return self->focusChild();
}

//  int QAccessibleTable::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleTable10childCountEv(
    const QAccessibleTable *self) {
  return self->childCount();
}

//  int QAccessibleTable::indexOfChild(const QAccessibleInterface *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleTable12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTable *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QAccessibleInterface *QAccessibleTable::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleTable6parentEv(
    const QAccessibleTable *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleTable::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleTable5childEi(
    const QAccessibleTable *self,
    int index) {
  return self->child(index);
}

//  void *QAccessibleTable::interface_cast(QAccessible::InterfaceType t)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QAccessibleTable14interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleTable *self,
    QAccessible::InterfaceType t) {
  return self->interface_cast(t);
}

//  QAccessibleInterface *QAccessibleTable::cellAt(int row, int column) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleTable6cellAtEii(
    const QAccessibleTable *self,
    int row,
    int column) {
  return self->cellAt(row, column);
}

//  QAccessibleInterface *QAccessibleTable::caption() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleTable7captionEv(
    const QAccessibleTable *self) {
  return self->caption();
}

//  QAccessibleInterface *QAccessibleTable::summary() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleTable7summaryEv(
    const QAccessibleTable *self) {
  return self->summary();
}

//  QString QAccessibleTable::columnDescription(int column) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QAccessibleTable17columnDescriptionEi(
    const QAccessibleTable *self,
    int column) {
  return new QString(self->columnDescription(column));
}

//  QString QAccessibleTable::rowDescription(int row) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QAccessibleTable14rowDescriptionEi(
    const QAccessibleTable *self,
    int row) {
  return new QString(self->rowDescription(row));
}

//  int QAccessibleTable::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleTable11columnCountEv(
    const QAccessibleTable *self) {
  return self->columnCount();
}

//  int QAccessibleTable::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleTable8rowCountEv(const QAccessibleTable *self) {
  return self->rowCount();
}

//  int QAccessibleTable::selectedCellCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleTable17selectedCellCountEv(
    const QAccessibleTable *self) {
  return self->selectedCellCount();
}

//  int QAccessibleTable::selectedColumnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleTable19selectedColumnCountEv(
    const QAccessibleTable *self) {
  return self->selectedColumnCount();
}

//  int QAccessibleTable::selectedRowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleTable16selectedRowCountEv(
    const QAccessibleTable *self) {
  return self->selectedRowCount();
}

//  QList<QAccessibleInterface *> QAccessibleTable::selectedCells() const
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_ZNK16QAccessibleTable13selectedCellsEv(
    const QAccessibleTable *self) {
  return new QList<QAccessibleInterface *>(self->selectedCells());
}

//  QList<int> QAccessibleTable::selectedColumns() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK16QAccessibleTable15selectedColumnsEv(
    const QAccessibleTable *self) {
  return new QList<int>(self->selectedColumns());
}

//  QList<int> QAccessibleTable::selectedRows() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK16QAccessibleTable12selectedRowsEv(
    const QAccessibleTable *self) {
  return new QList<int>(self->selectedRows());
}

//  bool QAccessibleTable::isColumnSelected(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAccessibleTable16isColumnSelectedEi(
    const QAccessibleTable *self,
    int column) {
  return self->isColumnSelected(column);
}

//  bool QAccessibleTable::isRowSelected(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAccessibleTable13isRowSelectedEi(
    const QAccessibleTable *self,
    int row) {
  return self->isRowSelected(row);
}

//  bool QAccessibleTable::selectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAccessibleTable9selectRowEi(
    QAccessibleTable *self,
    int row) {
  return self->selectRow(row);
}

//  bool QAccessibleTable::selectColumn(int column)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAccessibleTable12selectColumnEi(
    QAccessibleTable *self,
    int column) {
  return self->selectColumn(column);
}

//  bool QAccessibleTable::unselectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAccessibleTable11unselectRowEi(
    QAccessibleTable *self,
    int row) {
  return self->unselectRow(row);
}

//  bool QAccessibleTable::unselectColumn(int column)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAccessibleTable14unselectColumnEi(
    QAccessibleTable *self,
    int column) {
  return self->unselectColumn(column);
}

//  int QAccessibleTable::selectedItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleTable17selectedItemCountEv(
    const QAccessibleTable *self) {
  return self->selectedItemCount();
}

//  QList<QAccessibleInterface *> QAccessibleTable::selectedItems() const
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_ZNK16QAccessibleTable13selectedItemsEv(
    const QAccessibleTable *self) {
  return new QList<QAccessibleInterface *>(self->selectedItems());
}

//  bool QAccessibleTable::isSelected(QAccessibleInterface *childCell) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAccessibleTable10isSelectedEP20QAccessibleInterface(
    const QAccessibleTable *self,
    QAccessibleInterface *childCell) {
  return self->isSelected(childCell);
}

//  bool QAccessibleTable::select(QAccessibleInterface *childCell)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAccessibleTable6selectEP20QAccessibleInterface(
    QAccessibleTable *self,
    QAccessibleInterface *childCell) {
  return self->select(childCell);
}

//  bool QAccessibleTable::unselect(QAccessibleInterface *childCell)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAccessibleTable8unselectEP20QAccessibleInterface(
    QAccessibleTable *self,
    QAccessibleInterface *childCell) {
  return self->unselect(childCell);
}

//  bool QAccessibleTable::selectAll()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAccessibleTable9selectAllEv(QAccessibleTable *self) {
  return self->selectAll();
}

//  bool QAccessibleTable::clear()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAccessibleTable5clearEv(QAccessibleTable *self) {
  return self->clear();
}

#if QT_CONFIG(accessibility)
//  QAbstractItemView *QAccessibleTable::view() const
extern "C" Q_DECL_EXPORT
QAbstractItemView *ritual_ZNK16QAccessibleTable4viewEv(
    const QAccessibleTable *self) {
  return self->view();
}
#endif  // QT_CONFIG(accessibility)

//  void QAccessibleTable::modelChange(QAccessibleTableModelChangeEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleTable11modelChangeEP32QAccessibleTableModelChangeEvent(
    QAccessibleTable *self,
    QAccessibleTableModelChangeEvent *event) {
  self->modelChange(event);
}

//  QAccessible::Role QAccessibleTable::cellRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK16QAccessibleTable8cellRoleEv(
    const QAccessibleTable *self) {
  return self->cellRole();
}

#if QT_CONFIG(accessibility)
//  QHeaderView *QAccessibleTable::horizontalHeader() const
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZNK16QAccessibleTable16horizontalHeaderEv(
    const QAccessibleTable *self) {
  return self->horizontalHeader();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QHeaderView *QAccessibleTable::verticalHeader() const
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZNK16QAccessibleTable14verticalHeaderEv(
    const QAccessibleTable *self) {
  return self->verticalHeader();
}
#endif  // QT_CONFIG(accessibility)

//  QAccessibleTable::~QAccessibleTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleTableD1Ev(QAccessibleTable *self) {
  delete self;
}

#if QT_CONFIG(accessibility)
//  int QAccessibleTable::logicalIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleTable12logicalIndexERK11QModelIndex(
    const QAccessibleTable *self,
    const QModelIndex *index) {
  return self->logicalIndex(*index);
}
#endif  // QT_CONFIG(accessibility)

//  QAccessibleTable as the QAccessibleSelectionInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleSelectionInterface *ritual_cast_QAccessibleTable_QAccessibleSelectionInterface(
    QAccessibleTable *self) {
  return static_cast<QAccessibleSelectionInterface *>(self);
}

//  QAccessibleTable as the QAccessibleWidgetV2 it is built on
extern "C" Q_DECL_EXPORT
QAccessibleWidgetV2 *ritual_cast_QAccessibleTable_QAccessibleWidgetV2(
    QAccessibleTable *self) {
  return static_cast<QAccessibleWidgetV2 *>(self);
}

//  a Python function taken by a CuteQAccessibleTable, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTable(
    QAccessibleTable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTable *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTable::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK16QAccessibleTable7childAtEii(
    const QAccessibleTable *self,
    int x,
    int y) {
  return self->QAccessibleTable::childAt(x, y);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTable::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK16QAccessibleTable10focusChildEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::focusChild();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTable::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QAccessibleTable10childCountEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::childCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTable::indexOfChild(const QAccessibleInterface *a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QAccessibleTable12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTable *self,
    const QAccessibleInterface *a0) {
  return self->QAccessibleTable::indexOfChild(a0);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTable::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK16QAccessibleTable6parentEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::parent();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if defined(Q_OS_LINUX)
//  QAccessibleInterface *QAccessibleTable::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK16QAccessibleTable5childEi(
    const QAccessibleTable *self,
    int index) {
  return self->QAccessibleTable::child(index);
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void *QAccessibleTable::interface_cast(QAccessible::InterfaceType t)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN16QAccessibleTable14interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleTable *self,
    QAccessible::InterfaceType t) {
  return self->QAccessibleTable::interface_cast(t);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTable::cellAt(int row, int column) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK16QAccessibleTable6cellAtEii(
    const QAccessibleTable *self,
    int row,
    int column) {
  return self->QAccessibleTable::cellAt(row, column);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTable::caption() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK16QAccessibleTable7captionEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::caption();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTable::summary() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK16QAccessibleTable7summaryEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::summary();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QString QAccessibleTable::columnDescription(int column) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QAccessibleTable17columnDescriptionEi(
    const QAccessibleTable *self,
    int column) {
  return new QString(self->QAccessibleTable::columnDescription(column));
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QString QAccessibleTable::rowDescription(int row) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QAccessibleTable14rowDescriptionEi(
    const QAccessibleTable *self,
    int row) {
  return new QString(self->QAccessibleTable::rowDescription(row));
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTable::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QAccessibleTable11columnCountEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::columnCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTable::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QAccessibleTable8rowCountEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::rowCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTable::selectedCellCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QAccessibleTable17selectedCellCountEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::selectedCellCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTable::selectedColumnCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QAccessibleTable19selectedColumnCountEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::selectedColumnCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTable::selectedRowCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QAccessibleTable16selectedRowCountEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::selectedRowCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::isColumnSelected(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QAccessibleTable16isColumnSelectedEi(
    const QAccessibleTable *self,
    int column) {
  return self->QAccessibleTable::isColumnSelected(column);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::isRowSelected(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QAccessibleTable13isRowSelectedEi(
    const QAccessibleTable *self,
    int row) {
  return self->QAccessibleTable::isRowSelected(row);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::selectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAccessibleTable9selectRowEi(
    QAccessibleTable *self,
    int row) {
  return self->QAccessibleTable::selectRow(row);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::selectColumn(int column)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAccessibleTable12selectColumnEi(
    QAccessibleTable *self,
    int column) {
  return self->QAccessibleTable::selectColumn(column);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::unselectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAccessibleTable11unselectRowEi(
    QAccessibleTable *self,
    int row) {
  return self->QAccessibleTable::unselectRow(row);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::unselectColumn(int column)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAccessibleTable14unselectColumnEi(
    QAccessibleTable *self,
    int column) {
  return self->QAccessibleTable::unselectColumn(column);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTable::selectedItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QAccessibleTable17selectedItemCountEv(
    const QAccessibleTable *self) {
  return self->QAccessibleTable::selectedItemCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::isSelected(QAccessibleInterface *childCell) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QAccessibleTable10isSelectedEP20QAccessibleInterface(
    const QAccessibleTable *self,
    QAccessibleInterface *childCell) {
  return self->QAccessibleTable::isSelected(childCell);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::select(QAccessibleInterface *childCell)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAccessibleTable6selectEP20QAccessibleInterface(
    QAccessibleTable *self,
    QAccessibleInterface *childCell) {
  return self->QAccessibleTable::select(childCell);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::unselect(QAccessibleInterface *childCell)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAccessibleTable8unselectEP20QAccessibleInterface(
    QAccessibleTable *self,
    QAccessibleInterface *childCell) {
  return self->QAccessibleTable::unselect(childCell);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::selectAll()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAccessibleTable9selectAllEv(QAccessibleTable *self) {
  return self->QAccessibleTable::selectAll();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTable::clear()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAccessibleTable5clearEv(QAccessibleTable *self) {
  return self->QAccessibleTable::clear();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QAccessibleTable::modelChange(QAccessibleTableModelChangeEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAccessibleTable11modelChangeEP32QAccessibleTableModelChangeEvent(
    QAccessibleTable *self,
    QAccessibleTableModelChangeEvent *event) {
  self->QAccessibleTable::modelChange(event);
}
#endif  // QT_CONFIG(accessibility)

//  a QList<int> a ritual of QAccessibleTable gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAccessibleTable__QList_int(QList<int> *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility) && QT_CONFIG(itemviews)
