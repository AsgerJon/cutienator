//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <cstring>
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

//  from src/widgets/accessible/itemviews.cpp, line 969, as _ZNK15QAccessibleList5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
inline QAccessibleInterface *QAccessibleList::child(int logicalIndex) const
{
    QAbstractItemView *theView = view();
    if (!theView)
        return nullptr;
    const QAbstractItemModel *theModel = theView->model();
    if (!theModel)
        return nullptr;

    if (columnCount() == 0) {
        return nullptr;
    }

    const auto id = childToId.constFind(logicalIndex);
    if (id != childToId.constEnd())
        return QAccessible::accessibleInterface(id.value());

    const QListView *listView = qobject_cast<const QListView*>(theView);
    Q_ASSERT(listView);
    int row = logicalIndex;
    int column = listView->modelColumn();

    const QModelIndex rootIndex = theView->rootIndex();
    const QModelIndex index = theModel->index(row, column, rootIndex);
    if (Q_UNLIKELY(!index.isValid())) {
        qWarning("QAccessibleList::child: Invalid index at: %d %d", row, column);
        return nullptr;
    }
    const auto iface = new QAccessibleTableCell(theView, index, cellRole());

    QAccessible::registerAccessibleInterface(iface);
    childToId.insert(logicalIndex, QAccessible::uniqueId(iface));
    return iface;
}
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1004, as _ZNK15QAccessibleList6cellAtEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
inline QAccessibleInterface *QAccessibleList::cellAt(int row, int column) const
{
    if (column != 0)
        return nullptr;

    return child(row);
}
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1012, as _ZNK15QAccessibleList17selectedCellCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
inline int QAccessibleList::selectedCellCount() const
{
    QAbstractItemView *theView = view();
    if (!theView->selectionModel())
        return 0;
    const QListView *listView = qobject_cast<const QListView*>(theView);
    const int modelColumn = listView->modelColumn();
    const QModelIndexList selectedIndexes = theView->selectionModel()->selectedIndexes();
    return std::count_if(selectedIndexes.cbegin(), selectedIndexes.cend(),
                         [modelColumn](const auto &index) {
                             return index.column() == modelColumn;
                         });
}
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/itemviews.cpp, line 1026, as _ZNK15QAccessibleList13selectedCellsEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
inline QList<QAccessibleInterface *> QAccessibleList::selectedCells() const
{
    QAbstractItemView *theView = view();
    QList<QAccessibleInterface*> cells;
    if (!view()->selectionModel() || columnCount() == 0)
        return cells;
    const QListView *listView = qobject_cast<const QListView*>(theView);
    const int modelColumn = listView->modelColumn();
    const QModelIndexList selectedIndexes = theView->selectionModel()->selectedIndexes();
    cells.reserve(qMin(selectedIndexes.size(), rowCount()));
    for (const QModelIndex &index : selectedIndexes)
        if (index.column() == modelColumn) {
            cells.append(child(index.row()));
        }
    return cells;
}
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleList that Python can take functions over in. Every QAccessibleList
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void * (*CuteQAccessibleListCall0)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void * (*CuteQAccessibleListCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef int (*CuteQAccessibleListCall2)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleListCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleListCall4)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleListCall5)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleListCall6)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleListCall7)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleListCall8)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAccessibleListCall9)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef QString * (*CuteQAccessibleListCall10)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef QString * (*CuteQAccessibleListCall11)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleListCall12)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleListCall13)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleListCall14)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleListCall15)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall16)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall17)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall18)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall19)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall20)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall21)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAccessibleListCall22)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall23)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall24)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall25)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall26)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAccessibleListCall27)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAccessibleListCall28)(const void *, QAccessibleTableModelChangeEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleListCall29)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleListCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleListCall31)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleListCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleListCall33)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleListCall34)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleListCall35)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleListCall36)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleListCall37)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleListCall38)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleListCall39)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleListCall40)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleListCall41)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleListCall42)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleListCall43)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleList : public QAccessibleList {
public:
  using QAccessibleList::QAccessibleList;
  void *taken[44] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface6cellAtEii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface17selectedCellCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
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
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface19selectedColumnCountEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface16selectedRowCountEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface16isColumnSelectedEi")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK25QAccessibleTableInterface13isRowSelectedEi")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface9selectRowEi")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface12selectColumnEi")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface11unselectRowEi")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface14unselectColumnEi")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface17selectedItemCountEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface10isSelectedEP20QAccessibleInterface")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface6selectEP20QAccessibleInterface")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface8unselectEP20QAccessibleInterface")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface9selectAllEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface5clearEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN25QAccessibleTableInterface11modelChangeEP32QAccessibleTableModelChangeEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface12selectedItemEi")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  QAccessibleInterface *QAccessibleList::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleListCall0 call = reinterpret_cast<CuteQAccessibleListCall0>(taken[0]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleList::child(index);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  QAccessibleInterface *QAccessibleList::cellAt(int row, int column)
  //      const
  QAccessibleInterface *cellAt(int row, int column) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleListCall1 call = reinterpret_cast<CuteQAccessibleListCall1>(taken[1]);
      void * given = call(this, row, column, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleList::cellAt(row, column);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  int QAccessibleList::selectedCellCount() const
  int selectedCellCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleListCall2 call = reinterpret_cast<CuteQAccessibleListCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleList::selectedCellCount();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QAccessibleInterface *QAccessibleTable::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleListCall3 call = reinterpret_cast<CuteQAccessibleListCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleListCall4 call = reinterpret_cast<CuteQAccessibleListCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleListCall5 call = reinterpret_cast<CuteQAccessibleListCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleListCall6 call = reinterpret_cast<CuteQAccessibleListCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleListCall7 call = reinterpret_cast<CuteQAccessibleListCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTable::parent();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  QAccessibleInterface *QAccessibleTable::caption() const
  QAccessibleInterface *caption() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleListCall8 call = reinterpret_cast<CuteQAccessibleListCall8>(taken[8]);
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
      CuteQAccessibleListCall9 call = reinterpret_cast<CuteQAccessibleListCall9>(taken[9]);
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
      CuteQAccessibleListCall10 call = reinterpret_cast<CuteQAccessibleListCall10>(taken[10]);
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
      CuteQAccessibleListCall11 call = reinterpret_cast<CuteQAccessibleListCall11>(taken[11]);
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
      CuteQAccessibleListCall12 call = reinterpret_cast<CuteQAccessibleListCall12>(taken[12]);
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
      CuteQAccessibleListCall13 call = reinterpret_cast<CuteQAccessibleListCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTable::rowCount();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(itemviews)
  //  int QAccessibleTable::selectedColumnCount() const
  int selectedColumnCount() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleListCall14 call = reinterpret_cast<CuteQAccessibleListCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleListCall15 call = reinterpret_cast<CuteQAccessibleListCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleListCall16 call = reinterpret_cast<CuteQAccessibleListCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleListCall17 call = reinterpret_cast<CuteQAccessibleListCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleListCall18 call = reinterpret_cast<CuteQAccessibleListCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleListCall19 call = reinterpret_cast<CuteQAccessibleListCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleListCall20 call = reinterpret_cast<CuteQAccessibleListCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleListCall21 call = reinterpret_cast<CuteQAccessibleListCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleListCall22 call = reinterpret_cast<CuteQAccessibleListCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleListCall23 call = reinterpret_cast<CuteQAccessibleListCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleListCall24 call = reinterpret_cast<CuteQAccessibleListCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleListCall25 call = reinterpret_cast<CuteQAccessibleListCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleListCall26 call = reinterpret_cast<CuteQAccessibleListCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleListCall27 call = reinterpret_cast<CuteQAccessibleListCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQAccessibleListCall28 call = reinterpret_cast<CuteQAccessibleListCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQAccessibleListCall29 call = reinterpret_cast<CuteQAccessibleListCall29>(taken[29]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQAccessibleListCall30 call = reinterpret_cast<CuteQAccessibleListCall30>(taken[30]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQAccessibleListCall31 call = reinterpret_cast<CuteQAccessibleListCall31>(taken[31]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQAccessibleListCall32 call = reinterpret_cast<CuteQAccessibleListCall32>(taken[32]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQAccessibleListCall33 call = reinterpret_cast<CuteQAccessibleListCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQAccessibleListCall34 call = reinterpret_cast<CuteQAccessibleListCall34>(taken[34]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQAccessibleListCall35 call = reinterpret_cast<CuteQAccessibleListCall35>(taken[35]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQAccessibleListCall36 call = reinterpret_cast<CuteQAccessibleListCall36>(taken[36]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQAccessibleListCall37 call = reinterpret_cast<CuteQAccessibleListCall37>(taken[37]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAccessibleListCall38 call = reinterpret_cast<CuteQAccessibleListCall38>(taken[38]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQAccessibleListCall39 call = reinterpret_cast<CuteQAccessibleListCall39>(taken[39]);
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
    if (taken[40]) {
      int handled = 0;
      CuteQAccessibleListCall40 call = reinterpret_cast<CuteQAccessibleListCall40>(taken[40]);
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
    if (taken[41]) {
      int handled = 0;
      CuteQAccessibleListCall41 call = reinterpret_cast<CuteQAccessibleListCall41>(taken[41]);
      void * given = call(this, selectionIndex, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleSelectionInterface::selectedItem(selectionIndex);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQAccessibleListCall42 call = reinterpret_cast<CuteQAccessibleListCall42>(taken[42]);
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
    if (taken[43]) {
      int handled = 0;
      CuteQAccessibleListCall43 call = reinterpret_cast<CuteQAccessibleListCall43>(taken[43]);
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

//  QAccessibleInterface *QAccessibleList::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QAccessibleList5childEi(
    const QAccessibleList *self,
    int index) {
  return self->child(index);
}

//  QAccessibleInterface *QAccessibleList::cellAt(int row, int column) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QAccessibleList6cellAtEii(
    const QAccessibleList *self,
    int row,
    int column) {
  return self->cellAt(row, column);
}

//  int QAccessibleList::selectedCellCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAccessibleList17selectedCellCountEv(
    const QAccessibleList *self) {
  return self->selectedCellCount();
}

//  QList<QAccessibleInterface *> QAccessibleList::selectedCells() const
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_ZNK15QAccessibleList13selectedCellsEv(
    const QAccessibleList *self) {
  return new QList<QAccessibleInterface *>(self->selectedCells());
}

//  a Python function taken by a CuteQAccessibleList, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleList(
    QAccessibleList *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleList *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
//  QAccessibleInterface *QAccessibleList::cellAt(int row, int column) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK15QAccessibleList6cellAtEii(
    const QAccessibleList *self,
    int row,
    int column) {
  return self->QAccessibleList::cellAt(row, column);
}
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
//  int QAccessibleList::selectedCellCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QAccessibleList17selectedCellCountEv(
    const QAccessibleList *self) {
  return self->QAccessibleList::selectedCellCount();
}
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
