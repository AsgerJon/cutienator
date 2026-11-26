//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility) && QT_CONFIG(itemviews)
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

//  from src/widgets/accessible/itemviews.cpp, line 63, as _ZN16QAccessibleTableC2EP7QWidgetN11QAccessible4RoleE
#if QT_CONFIG(accessibility)
inline QAccessibleTable::QAccessibleTable(QWidget *w, QAccessible::Role role)
    : QAccessibleWidgetV2(w, role)
{
    Q_ASSERT(view());
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

//  from src/widgets/accessible/itemviews.cpp, line 36, as _ZNK16QAccessibleTable4viewEv
#if QT_CONFIG(accessibility)
inline QAbstractItemView *QAccessibleTable::view() const
{
    return qobject_cast<QAbstractItemView*>(object());
}
#endif  // QT_CONFIG(accessibility)

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

//  from src/widgets/accessible/itemviews.cpp, line 263, as _ZNK16QAccessibleTable13isRowSelectedEi
#if QT_CONFIG(accessibility)
inline bool QAccessibleTable::isRowSelected(int row) const
{
    if (!view()->selectionModel())
        return false;
    return view()->selectionModel()->isRowSelected(row, QModelIndex());
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
#if defined(Q_OS_LINUX)
#if QT_CONFIG(treeview)
//  QAccessibleInterface *QAccessibleTree::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK15QAccessibleTree5childEi(
    const QAccessibleTree *self,
    int index) {
  return self->QAccessibleTree::child(index);
}
#endif  // QT_CONFIG(treeview)
#endif  // defined(Q_OS_LINUX)
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
#endif  // QT_CONFIG(accessibility) && QT_CONFIG(itemviews)
