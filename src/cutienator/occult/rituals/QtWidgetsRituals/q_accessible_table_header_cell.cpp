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

//  from src/widgets/accessible/itemviews.cpp, line 1359, as _ZN26QAccessibleTableHeaderCellC1EP17QAbstractItemViewiN2Qt11OrientationE
#if QT_CONFIG(accessibility)
inline QAccessibleTableHeaderCell::QAccessibleTableHeaderCell(QAbstractItemView *view_, int index_, Qt::Orientation orientation_)
    : view(view_), index(index_), orientation(orientation_)
{
    Q_ASSERT(index_ >= 0);
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
//  -----------------------------------------------------------------------

#if QT_CONFIG(accessibility)
//  QAccessibleTableHeaderCell::QAccessibleTableHeaderCell(QAbstractItemView
//      *view, int index, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
QAccessibleTableHeaderCell *ritual_ZN26QAccessibleTableHeaderCellC1EP17QAbstractItemViewiN2Qt11OrientationE(
    QAbstractItemView *view,
    int index,
    Qt::Orientation orientation) {
  return new QAccessibleTableHeaderCell(view, index, orientation);
}
#endif  // QT_CONFIG(accessibility)

//  QObject *QAccessibleTableHeaderCell::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK26QAccessibleTableHeaderCell6objectEv(
    const QAccessibleTableHeaderCell *self) {
  return self->object();
}

//  QAccessible::Role QAccessibleTableHeaderCell::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK26QAccessibleTableHeaderCell4roleEv(
    const QAccessibleTableHeaderCell *self) {
  return self->role();
}

//  QAccessible::State QAccessibleTableHeaderCell::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK26QAccessibleTableHeaderCell5stateEv(
    const QAccessibleTableHeaderCell *self) {
  return new QAccessible::State(self->state());
}

//  QRect QAccessibleTableHeaderCell::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK26QAccessibleTableHeaderCell4rectEv(
    const QAccessibleTableHeaderCell *self) {
  return new QRect(self->rect());
}

//  bool QAccessibleTableHeaderCell::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QAccessibleTableHeaderCell7isValidEv(
    const QAccessibleTableHeaderCell *self) {
  return self->isValid();
}

//  QAccessibleInterface *QAccessibleTableHeaderCell::childAt(int a0, int a1)
//      const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK26QAccessibleTableHeaderCell7childAtEii(
    const QAccessibleTableHeaderCell *self,
    int a0,
    int a1) {
  return self->childAt(a0, a1);
}

//  int QAccessibleTableHeaderCell::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTableHeaderCell10childCountEv(
    const QAccessibleTableHeaderCell *self) {
  return self->childCount();
}

//  int QAccessibleTableHeaderCell::indexOfChild(const QAccessibleInterface
//      *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTableHeaderCell12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTableHeaderCell *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QString QAccessibleTableHeaderCell::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleTableHeaderCell4textEN11QAccessible4TextE(
    const QAccessibleTableHeaderCell *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  void QAccessibleTableHeaderCell::setText(QAccessible::Text t, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTableHeaderCell7setTextEN11QAccessible4TextERK7QString(
    QAccessibleTableHeaderCell *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QAccessibleInterface *QAccessibleTableHeaderCell::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK26QAccessibleTableHeaderCell6parentEv(
    const QAccessibleTableHeaderCell *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleTableHeaderCell::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK26QAccessibleTableHeaderCell5childEi(
    const QAccessibleTableHeaderCell *self,
    int index) {
  return self->child(index);
}

#if QT_CONFIG(accessibility)
//  QHeaderView *QAccessibleTableHeaderCell::headerView() const
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZNK26QAccessibleTableHeaderCell10headerViewEv(
    const QAccessibleTableHeaderCell *self) {
  return self->headerView();
}
#endif  // QT_CONFIG(accessibility)

//  QObject *QAccessibleTableHeaderCell::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK26QAccessibleTableHeaderCell6objectEv(
    const QAccessibleTableHeaderCell *self) {
  return self->QAccessibleTableHeaderCell::object();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QAccessibleTableHeaderCell::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK26QAccessibleTableHeaderCell4roleEv(
    const QAccessibleTableHeaderCell *self) {
  return self->QAccessibleTableHeaderCell::role();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::State QAccessibleTableHeaderCell::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK26QAccessibleTableHeaderCell5stateEv(
    const QAccessibleTableHeaderCell *self) {
  return new QAccessible::State(self->QAccessibleTableHeaderCell::state());
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QRect QAccessibleTableHeaderCell::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK26QAccessibleTableHeaderCell4rectEv(
    const QAccessibleTableHeaderCell *self) {
  return new QRect(self->QAccessibleTableHeaderCell::rect());
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  bool QAccessibleTableHeaderCell::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QAccessibleTableHeaderCell7isValidEv(
    const QAccessibleTableHeaderCell *self) {
  return self->QAccessibleTableHeaderCell::isValid();
}
#endif  // QT_CONFIG(accessibility)

//  QAccessibleInterface *QAccessibleTableHeaderCell::childAt(int a0, int a1)
//      const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK26QAccessibleTableHeaderCell7childAtEii(
    const QAccessibleTableHeaderCell *self,
    int a0,
    int a1) {
  return self->QAccessibleTableHeaderCell::childAt(a0, a1);
}

//  int QAccessibleTableHeaderCell::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QAccessibleTableHeaderCell10childCountEv(
    const QAccessibleTableHeaderCell *self) {
  return self->QAccessibleTableHeaderCell::childCount();
}

//  int QAccessibleTableHeaderCell::indexOfChild(const QAccessibleInterface
//      *a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QAccessibleTableHeaderCell12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTableHeaderCell *self,
    const QAccessibleInterface *a0) {
  return self->QAccessibleTableHeaderCell::indexOfChild(a0);
}

#if QT_CONFIG(accessibility)
//  QString QAccessibleTableHeaderCell::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK26QAccessibleTableHeaderCell4textEN11QAccessible4TextE(
    const QAccessibleTableHeaderCell *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleTableHeaderCell::text(t));
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QAccessibleTableHeaderCell::setText(QAccessible::Text t, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleTableHeaderCell7setTextEN11QAccessible4TextERK7QString(
    QAccessibleTableHeaderCell *self,
    QAccessible::Text t,
    const QString *text) {
  self->QAccessibleTableHeaderCell::setText(t, *text);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTableHeaderCell::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK26QAccessibleTableHeaderCell6parentEv(
    const QAccessibleTableHeaderCell *self) {
  return self->QAccessibleTableHeaderCell::parent();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleTableHeaderCell::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK26QAccessibleTableHeaderCell5childEi(
    const QAccessibleTableHeaderCell *self,
    int index) {
  return self->QAccessibleTableHeaderCell::child(index);
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility) && QT_CONFIG(itemviews)
