//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(calendarwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qaccessiblewidgets_p.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qclipboard.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qtextobject.h>
#if QT_CONFIG(textedit)
#include <QtWidgets/qplaintextedit.h>
#include <QtWidgets/qtextedit.h>
#include <QtWidgets/private/qtextedit_p.h>
#endif
#include <QtCore/qtextboundaryfinder.h>
#if QT_CONFIG(scrollbar)
#include <QtWidgets/qscrollbar.h>
#endif
#include <QtCore/qdebug.h>
#include <QtWidgets/QApplication>
#if QT_CONFIG(stackedwidget)
#include <QtWidgets/QStackedWidget>
#endif
#if QT_CONFIG(toolbox)
#include <QtWidgets/QToolBox>
#endif
#if QT_CONFIG(mdiarea)
#include <QtWidgets/QMdiArea>
#include <QtWidgets/QMdiSubWindow>
#endif
#if QT_CONFIG(dialogbuttonbox)
#include <QtWidgets/QDialogButtonBox>
#endif
#include <limits.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/QRubberBand>
#endif
#if QT_CONFIG(textbrowser)
#include <QtWidgets/QTextBrowser>
#endif
#if QT_CONFIG(calendarwidget)
#include <QtWidgets/QCalendarWidget>
#endif
#if QT_CONFIG(itemviews)
#include <QtWidgets/QAbstractItemView>
#endif
#if QT_CONFIG(dockwidget)
#include <QtWidgets/QDockWidget>
#include <QtWidgets/private/qdockwidget_p.h>
#endif
#if QT_CONFIG(mainwindow)
#include <QtWidgets/QMainWindow>
#endif
#include <QtWidgets/QFocusFrame>
#if QT_CONFIG(menu)
#include <QtWidgets/QMenu>
#endif
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

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 510, as _ZNK25QAccessibleCalendarWidget10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(calendarwidget)
inline int QAccessibleCalendarWidget::childCount() const
{
   return calendarWidget()->isNavigationBarVisible() ? 2 : 1;
}
#endif  // QT_CONFIG(calendarwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 515, as _ZNK25QAccessibleCalendarWidget12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(calendarwidget)
inline int QAccessibleCalendarWidget::indexOfChild(const QAccessibleInterface *child) const
{
    if (!child || !child->object() || childCount() <= 0)
        return -1;
    if (qobject_cast<QAbstractItemView *>(child->object()))
        return childCount() - 1; // FIXME
    return 0;
}
#endif  // QT_CONFIG(calendarwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 524, as _ZNK25QAccessibleCalendarWidget5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(calendarwidget)
inline QAccessibleInterface *QAccessibleCalendarWidget::child(int index) const
{
    if (index < 0 || index >= childCount())
        return nullptr;

    if (childCount() > 1 && index == 0)
        return QAccessible::queryAccessibleInterface(navigationBar());

    return QAccessible::queryAccessibleInterface(calendarView());
}
#endif  // QT_CONFIG(calendarwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 535, as _ZNK25QAccessibleCalendarWidget14calendarWidgetEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(calendarwidget)
inline QCalendarWidget *QAccessibleCalendarWidget::calendarWidget() const
{
    return static_cast<QCalendarWidget *>(object());
}
#endif  // QT_CONFIG(calendarwidget)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  int QAccessibleCalendarWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleCalendarWidget10childCountEv(
    const QAccessibleCalendarWidget *self) {
  return self->childCount();
}

//  int QAccessibleCalendarWidget::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleCalendarWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleCalendarWidget *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QAccessibleInterface *QAccessibleCalendarWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK25QAccessibleCalendarWidget5childEi(
    const QAccessibleCalendarWidget *self,
    int index) {
  return self->child(index);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(calendarwidget)
//  QCalendarWidget *QAccessibleCalendarWidget::calendarWidget() const
extern "C" Q_DECL_EXPORT
QCalendarWidget *ritual_ZNK25QAccessibleCalendarWidget14calendarWidgetEv(
    const QAccessibleCalendarWidget *self) {
  return self->calendarWidget();
}
#endif  // QT_CONFIG(calendarwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(calendarwidget)
//  int QAccessibleCalendarWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QAccessibleCalendarWidget10childCountEv(
    const QAccessibleCalendarWidget *self) {
  return self->QAccessibleCalendarWidget::childCount();
}
#endif  // QT_CONFIG(calendarwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(calendarwidget)
//  int QAccessibleCalendarWidget::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QAccessibleCalendarWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleCalendarWidget *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleCalendarWidget::indexOfChild(child);
}
#endif  // QT_CONFIG(calendarwidget)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(calendarwidget)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
