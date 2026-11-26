//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qwidget.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/complexwidgets_p.h>
#include <QtGui/qaccessible.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qevent.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qheaderview.h>
#endif
#if QT_CONFIG(tabbar)
#include <QtWidgets/qtabbar.h>
#include <QtWidgets/private/qtabbar_p.h>
#endif
#if QT_CONFIG(combobox)
#include <QtWidgets/qcombobox.h>
#endif
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#if QT_CONFIG(whatsthis)
#include <QtWidgets/qwhatsthis.h>
#endif
#include <QtWidgets/QAbstractScrollArea>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/QScrollArea>
#endif
#if QT_CONFIG(scrollbar)
#include <QtWidgets/QScrollBar>
#endif
#include <QtCore/QDebug>
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/accessible/complexwidgets.cpp, line 507, as _ZNK29QAccessibleAbstractScrollArea5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline QAccessibleInterface *QAccessibleAbstractScrollArea::child(int index) const
{
    return QAccessible::queryAccessibleInterface(accessibleChildren().at(index));
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 512, as _ZNK29QAccessibleAbstractScrollArea10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline int QAccessibleAbstractScrollArea::childCount() const
{
    return accessibleChildren().size();
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 517, as _ZNK29QAccessibleAbstractScrollArea12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline int QAccessibleAbstractScrollArea::indexOfChild(const QAccessibleInterface *child) const
{
    if (!child || !child->object())
        return -1;
    return accessibleChildren().indexOf(qobject_cast<QWidget *>(child->object()));
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 524, as _ZNK29QAccessibleAbstractScrollArea7isValidEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline bool QAccessibleAbstractScrollArea::isValid() const
{
    return (QAccessibleWidgetV2::isValid() && abstractScrollArea() && abstractScrollArea()->viewport());
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 529, as _ZNK29QAccessibleAbstractScrollArea7childAtEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline QAccessibleInterface *QAccessibleAbstractScrollArea::childAt(int x, int y) const
{
    if (!abstractScrollArea()->isVisible())
        return nullptr;

    for (int i = 0; i < childCount(); ++i) {
        QPoint wpos = accessibleChildren().at(i)->mapToGlobal(QPoint(0, 0));
        QRect rect = QRect(wpos, accessibleChildren().at(i)->size());
        if (rect.contains(x, y))
            return child(i);
    }
    return nullptr;
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 501, as _ZN29QAccessibleAbstractScrollAreaC1EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline QAccessibleAbstractScrollArea::QAccessibleAbstractScrollArea(QWidget *widget)
    : QAccessibleWidgetV2(widget, QAccessible::Client)
{
    Q_ASSERT(qobject_cast<QAbstractScrollArea *>(widget));
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 543, as _ZNK29QAccessibleAbstractScrollArea18abstractScrollAreaEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline QAbstractScrollArea *QAccessibleAbstractScrollArea::abstractScrollArea() const
{
    return static_cast<QAbstractScrollArea *>(object());
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 548, as _ZNK29QAccessibleAbstractScrollArea18accessibleChildrenEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline QWidgetList QAccessibleAbstractScrollArea::accessibleChildren() const
{
    QWidgetList children;

    // Viewport.
    QWidget * viewport = abstractScrollArea()->viewport();
    if (viewport)
        children.append(viewport);

    // Horizontal scrollBar container.
    QScrollBar *horizontalScrollBar = abstractScrollArea()->horizontalScrollBar();
    if (horizontalScrollBar && horizontalScrollBar->isVisible()) {
        QWidget *scrollBarParent = horizontalScrollBar->parentWidget();
        // Add container only if scroll bar is in the container
        if (elementType(scrollBarParent) == HorizontalContainer)
            children.append(scrollBarParent);
    }

    // Vertical scrollBar container.
    QScrollBar *verticalScrollBar = abstractScrollArea()->verticalScrollBar();
    if (verticalScrollBar && verticalScrollBar->isVisible()) {
        QWidget *scrollBarParent = verticalScrollBar->parentWidget();
        // Add container only if scroll bar is in the container
        if (elementType(scrollBarParent) == VerticalContainer)
            children.append(scrollBarParent);
    }

    // CornerWidget.
    QWidget *cornerWidget = abstractScrollArea()->cornerWidget();
    if (cornerWidget && cornerWidget->isVisible())
        children.append(cornerWidget);

    return children;
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 583, as _ZNK29QAccessibleAbstractScrollArea11elementTypeEP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline QAccessibleAbstractScrollArea::AbstractScrollAreaElement
QAccessibleAbstractScrollArea::elementType(QWidget *widget) const
{
    if (!widget)
        return Undefined;

    if (widget == abstractScrollArea())
        return Self;
    if (widget == abstractScrollArea()->viewport())
        return Viewport;
    if (widget->objectName() == "qt_scrollarea_hcontainer"_L1)
        return HorizontalContainer;
    if (widget->objectName() == "qt_scrollarea_vcontainer"_L1)
        return VerticalContainer;
    if (widget == abstractScrollArea()->cornerWidget())
        return CornerWidget;

    return Undefined;
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 603, as _ZNK29QAccessibleAbstractScrollArea13isLeftToRightEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline bool QAccessibleAbstractScrollArea::isLeftToRight() const
{
    return abstractScrollArea()->isLeftToRight();
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  QAccessibleAbstractScrollArea::QAccessibleAbstractScrollArea(QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
QAccessibleAbstractScrollArea *ritual_ZN29QAccessibleAbstractScrollAreaC1EP7QWidget(
    QWidget *widget) {
  return new QAccessibleAbstractScrollArea(widget);
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  QAccessibleInterface *QAccessibleAbstractScrollArea::child(int index)
//      const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK29QAccessibleAbstractScrollArea5childEi(
    const QAccessibleAbstractScrollArea *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleAbstractScrollArea::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleAbstractScrollArea10childCountEv(
    const QAccessibleAbstractScrollArea *self) {
  return self->childCount();
}

//  int QAccessibleAbstractScrollArea::indexOfChild(const
//      QAccessibleInterface *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleAbstractScrollArea12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleAbstractScrollArea *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  bool QAccessibleAbstractScrollArea::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QAccessibleAbstractScrollArea7isValidEv(
    const QAccessibleAbstractScrollArea *self) {
  return self->isValid();
}

//  QAccessibleInterface *QAccessibleAbstractScrollArea::childAt(int x, int
//      y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK29QAccessibleAbstractScrollArea7childAtEii(
    const QAccessibleAbstractScrollArea *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  QAbstractScrollArea *QAccessibleAbstractScrollArea::abstractScrollArea()
//      const
extern "C" Q_DECL_EXPORT
QAbstractScrollArea *ritual_ZNK29QAccessibleAbstractScrollArea18abstractScrollAreaEv(
    const QAccessibleAbstractScrollArea *self) {
  return self->abstractScrollArea();
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  QWidgetList QAccessibleAbstractScrollArea::accessibleChildren() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK29QAccessibleAbstractScrollArea18accessibleChildrenEv(
    const QAccessibleAbstractScrollArea *self) {
  return new QList<QWidget *>(self->accessibleChildren());
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  AbstractScrollAreaElement
//      QAccessibleAbstractScrollArea::elementType(QWidget *widget) const
extern "C" Q_DECL_EXPORT
QAccessibleAbstractScrollArea::AbstractScrollAreaElement ritual_ZNK29QAccessibleAbstractScrollArea11elementTypeEP7QWidget(
    const QAccessibleAbstractScrollArea *self,
    QWidget *widget) {
  return self->elementType(widget);
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  bool QAccessibleAbstractScrollArea::isLeftToRight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QAccessibleAbstractScrollArea13isLeftToRightEv(
    const QAccessibleAbstractScrollArea *self) {
  return self->isLeftToRight();
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  QAccessibleInterface *QAccessibleAbstractScrollArea::child(int index)
//      const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK29QAccessibleAbstractScrollArea5childEi(
    const QAccessibleAbstractScrollArea *self,
    int index) {
  return self->QAccessibleAbstractScrollArea::child(index);
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  int QAccessibleAbstractScrollArea::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QAccessibleAbstractScrollArea10childCountEv(
    const QAccessibleAbstractScrollArea *self) {
  return self->QAccessibleAbstractScrollArea::childCount();
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  int QAccessibleAbstractScrollArea::indexOfChild(const
//      QAccessibleInterface *child) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QAccessibleAbstractScrollArea12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleAbstractScrollArea *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleAbstractScrollArea::indexOfChild(child);
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  bool QAccessibleAbstractScrollArea::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QAccessibleAbstractScrollArea7isValidEv(
    const QAccessibleAbstractScrollArea *self) {
  return self->QAccessibleAbstractScrollArea::isValid();
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
//  QAccessibleInterface *QAccessibleAbstractScrollArea::childAt(int x, int
//      y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK29QAccessibleAbstractScrollArea7childAtEii(
    const QAccessibleAbstractScrollArea *self,
    int x,
    int y) {
  return self->QAccessibleAbstractScrollArea::childAt(x, y);
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
