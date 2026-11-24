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
#include <QtGui/qaccessible.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
//  -----------------------------------------------------------------------

//  QObject *QAccessibleTableCell::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QAccessibleTableCell6objectEv(
    const QAccessibleTableCell *self) {
  return self->object();
}

//  QAccessible::Role QAccessibleTableCell::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK20QAccessibleTableCell4roleEv(
    const QAccessibleTableCell *self) {
  return self->role();
}

//  QAccessible::State QAccessibleTableCell::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK20QAccessibleTableCell5stateEv(
    const QAccessibleTableCell *self) {
  return new QAccessible::State(self->state());
}

//  QRect QAccessibleTableCell::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK20QAccessibleTableCell4rectEv(
    const QAccessibleTableCell *self) {
  return new QRect(self->rect());
}

//  bool QAccessibleTableCell::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAccessibleTableCell7isValidEv(
    const QAccessibleTableCell *self) {
  return self->isValid();
}

//  QAccessibleInterface *QAccessibleTableCell::childAt(int a0, int a1) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleTableCell7childAtEii(
    const QAccessibleTableCell *self,
    int a0,
    int a1) {
  return self->childAt(a0, a1);
}

//  int QAccessibleTableCell::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleTableCell10childCountEv(
    const QAccessibleTableCell *self) {
  return self->childCount();
}

//  int QAccessibleTableCell::indexOfChild(const QAccessibleInterface *a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleTableCell12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTableCell *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QString QAccessibleTableCell::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleTableCell4textEN11QAccessible4TextE(
    const QAccessibleTableCell *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  void QAccessibleTableCell::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleTableCell7setTextEN11QAccessible4TextERK7QString(
    QAccessibleTableCell *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QAccessibleInterface *QAccessibleTableCell::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleTableCell6parentEv(
    const QAccessibleTableCell *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleTableCell::child(int a0) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleTableCell5childEi(
    const QAccessibleTableCell *self,
    int a0) {
  return self->child(a0);
}

//  int QAccessibleTableCell::columnExtent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleTableCell12columnExtentEv(
    const QAccessibleTableCell *self) {
  return self->columnExtent();
}

//  QList<QAccessibleInterface *> QAccessibleTableCell::columnHeaderCells()
//      const
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_ZNK20QAccessibleTableCell17columnHeaderCellsEv(
    const QAccessibleTableCell *self) {
  return new QList<QAccessibleInterface *>(self->columnHeaderCells());
}

//  int QAccessibleTableCell::columnIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleTableCell11columnIndexEv(
    const QAccessibleTableCell *self) {
  return self->columnIndex();
}

//  int QAccessibleTableCell::rowExtent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleTableCell9rowExtentEv(
    const QAccessibleTableCell *self) {
  return self->rowExtent();
}

//  QList<QAccessibleInterface *> QAccessibleTableCell::rowHeaderCells()
//      const
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_ZNK20QAccessibleTableCell14rowHeaderCellsEv(
    const QAccessibleTableCell *self) {
  return new QList<QAccessibleInterface *>(self->rowHeaderCells());
}

//  int QAccessibleTableCell::rowIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleTableCell8rowIndexEv(
    const QAccessibleTableCell *self) {
  return self->rowIndex();
}

//  bool QAccessibleTableCell::isSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAccessibleTableCell10isSelectedEv(
    const QAccessibleTableCell *self) {
  return self->isSelected();
}

//  QAccessibleInterface *QAccessibleTableCell::table() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleTableCell5tableEv(
    const QAccessibleTableCell *self) {
  return self->table();
}

//  QStringList QAccessibleTableCell::actionNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QAccessibleTableCell11actionNamesEv(
    const QAccessibleTableCell *self) {
  return new QList<QString>(self->actionNames());
}

//  void QAccessibleTableCell::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleTableCell8doActionERK7QString(
    QAccessibleTableCell *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

//  QStringList QAccessibleTableCell::keyBindingsForAction(const QString
//      &actionName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QAccessibleTableCell20keyBindingsForActionERK7QString(
    const QAccessibleTableCell *self,
    const QString *actionName) {
  return new QList<QString>(self->keyBindingsForAction(*actionName));
}

#if QT_CONFIG(accessibility)
//  QHeaderView *QAccessibleTableCell::verticalHeader() const
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZNK20QAccessibleTableCell14verticalHeaderEv(
    const QAccessibleTableCell *self) {
  return self->verticalHeader();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QHeaderView *QAccessibleTableCell::horizontalHeader() const
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZNK20QAccessibleTableCell16horizontalHeaderEv(
    const QAccessibleTableCell *self) {
  return self->horizontalHeader();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QAccessibleTableCell::selectCell()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleTableCell10selectCellEv(
    QAccessibleTableCell *self) {
  self->selectCell();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QAccessibleTableCell::unselectCell()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleTableCell12unselectCellEv(
    QAccessibleTableCell *self) {
  self->unselectCell();
}
#endif  // QT_CONFIG(accessibility)

//  QAccessibleTableCell as the QAccessibleTableCellInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleTableCellInterface *ritual_cast_QAccessibleTableCell_QAccessibleTableCellInterface(
    QAccessibleTableCell *self) {
  return static_cast<QAccessibleTableCellInterface *>(self);
}

//  QAccessibleTableCell as the QAccessibleActionInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleActionInterface *ritual_cast_QAccessibleTableCell_QAccessibleActionInterface(
    QAccessibleTableCell *self) {
  return static_cast<QAccessibleActionInterface *>(self);
}

//  QObject *QAccessibleTableCell::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK20QAccessibleTableCell6objectEv(
    const QAccessibleTableCell *self) {
  return self->QAccessibleTableCell::object();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QAccessibleTableCell::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK20QAccessibleTableCell4roleEv(
    const QAccessibleTableCell *self) {
  return self->QAccessibleTableCell::role();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::State QAccessibleTableCell::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK20QAccessibleTableCell5stateEv(
    const QAccessibleTableCell *self) {
  return new QAccessible::State(self->QAccessibleTableCell::state());
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QRect QAccessibleTableCell::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK20QAccessibleTableCell4rectEv(
    const QAccessibleTableCell *self) {
  return new QRect(self->QAccessibleTableCell::rect());
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTableCell::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QAccessibleTableCell7isValidEv(
    const QAccessibleTableCell *self) {
  return self->QAccessibleTableCell::isValid();
}
#endif  // QT_CONFIG(accessibility)

//  QAccessibleInterface *QAccessibleTableCell::childAt(int a0, int a1) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK20QAccessibleTableCell7childAtEii(
    const QAccessibleTableCell *self,
    int a0,
    int a1) {
  return self->QAccessibleTableCell::childAt(a0, a1);
}

//  int QAccessibleTableCell::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleTableCell10childCountEv(
    const QAccessibleTableCell *self) {
  return self->QAccessibleTableCell::childCount();
}

//  int QAccessibleTableCell::indexOfChild(const QAccessibleInterface *a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleTableCell12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTableCell *self,
    const QAccessibleInterface *a0) {
  return self->QAccessibleTableCell::indexOfChild(a0);
}

#if QT_CONFIG(accessibility)
//  QString QAccessibleTableCell::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QAccessibleTableCell4textEN11QAccessible4TextE(
    const QAccessibleTableCell *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleTableCell::text(t));
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QAccessibleTableCell::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleTableCell7setTextEN11QAccessible4TextERK7QString(
    QAccessibleTableCell *self,
    QAccessible::Text t,
    const QString *text) {
  self->QAccessibleTableCell::setText(t, *text);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTableCell::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK20QAccessibleTableCell6parentEv(
    const QAccessibleTableCell *self) {
  return self->QAccessibleTableCell::parent();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTableCell::child(int a0) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK20QAccessibleTableCell5childEi(
    const QAccessibleTableCell *self,
    int a0) {
  return self->QAccessibleTableCell::child(a0);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTableCell::columnIndex() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleTableCell11columnIndexEv(
    const QAccessibleTableCell *self) {
  return self->QAccessibleTableCell::columnIndex();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleTableCell::rowIndex() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleTableCell8rowIndexEv(
    const QAccessibleTableCell *self) {
  return self->QAccessibleTableCell::rowIndex();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTableCell::isSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QAccessibleTableCell10isSelectedEv(
    const QAccessibleTableCell *self) {
  return self->QAccessibleTableCell::isSelected();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTableCell::table() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK20QAccessibleTableCell5tableEv(
    const QAccessibleTableCell *self) {
  return self->QAccessibleTableCell::table();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if defined(Q_OS_LINUX)
//  void QAccessibleTableCell::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAccessibleTableCell8doActionERK7QString(
    QAccessibleTableCell *self,
    const QString *actionName) {
  self->QAccessibleTableCell::doAction(*actionName);
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility) && QT_CONFIG(itemviews)
