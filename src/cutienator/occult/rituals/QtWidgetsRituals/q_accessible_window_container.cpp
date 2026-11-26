//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/simplewidgets_p.h>
#if QT_CONFIG(abstractbutton)
#include <QtWidgets/qabstractbutton.h>
#endif
#if QT_CONFIG(checkbox)
#include <QtWidgets/qcheckbox.h>
#endif
#if QT_CONFIG(pushbutton)
#include <QtWidgets/qpushbutton.h>
#endif
#if QT_CONFIG(progressbar)
#include <QtWidgets/qprogressbar.h>
#endif
#if QT_CONFIG(statusbar)
#include <QtWidgets/qstatusbar.h>
#endif
#if QT_CONFIG(radiobutton)
#include <QtWidgets/qradiobutton.h>
#endif
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#endif
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#if QT_CONFIG(label)
#include <QtWidgets/qlabel.h>
#endif
#if QT_CONFIG(groupbox)
#include <QtWidgets/qgroupbox.h>
#endif
#if QT_CONFIG(lcdnumber)
#include <QtWidgets/qlcdnumber.h>
#endif
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/private/qlineedit_p.h>
#endif
#ifndef QT_NO_PICTURE
#include <QtGui/qpicture.h>
#endif
#if QT_CONFIG(messagebox)
#include <QtWidgets/qmessagebox.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qwindow.h>
#include <QtWidgets/private/qwindowcontainer_p.h>
#include <QtCore/qvarlengtharray.h>
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#include <QtGui/qvalidator.h>
#ifdef Q_OS_MACOS
#include <QtWidgets/qfocusframe.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/accessible/simplewidgets.cpp, line 921, as _ZN26QAccessibleWindowContainerC1EP7QWidget
#if QT_CONFIG(accessibility)
inline QAccessibleWindowContainer::QAccessibleWindowContainer(QWidget *w)
    : QAccessibleWidgetV2(w)
{
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 926, as _ZNK26QAccessibleWindowContainer4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
inline QString QAccessibleWindowContainer::text(QAccessible::Text) const
{
    return QString();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 931, as _ZNK26QAccessibleWindowContainer10childCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleWindowContainer::childCount() const
{
    if (container()->containedWindow() && QAccessible::queryAccessibleInterface(container()->containedWindow()))
        return 1;
    return 0;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 938, as _ZNK26QAccessibleWindowContainer12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
inline int QAccessibleWindowContainer::indexOfChild(const QAccessibleInterface *child) const
{
    if (child->object() == container()->containedWindow())
        return 0;
    return -1;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 945, as _ZNK26QAccessibleWindowContainer5childEi
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleWindowContainer::child(int i) const
{
    if (i == 0)
        return QAccessible::queryAccessibleInterface(container()->containedWindow());
    return nullptr;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 952, as _ZNK26QAccessibleWindowContainer9containerEv
#if QT_CONFIG(accessibility)
inline QWindowContainer *QAccessibleWindowContainer::container() const
{
    return static_cast<QWindowContainer *>(widget());
}
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

#if QT_CONFIG(accessibility)
//  QAccessibleWindowContainer::QAccessibleWindowContainer(QWidget *w)
extern "C" Q_DECL_EXPORT
QAccessibleWindowContainer *ritual_ZN26QAccessibleWindowContainerC1EP7QWidget(
    QWidget *w) {
  return new QAccessibleWindowContainer(w);
}
#endif  // QT_CONFIG(accessibility)

//  QString QAccessibleWindowContainer::text(QAccessible::Text a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleWindowContainer4textEN11QAccessible4TextE(
    const QAccessibleWindowContainer *self,
    QAccessible::Text a0) {
  return new QString(self->text(a0));
}

//  int QAccessibleWindowContainer::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleWindowContainer10childCountEv(
    const QAccessibleWindowContainer *self) {
  return self->childCount();
}

//  int QAccessibleWindowContainer::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleWindowContainer12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleWindowContainer *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QAccessibleInterface *QAccessibleWindowContainer::child(int i) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK26QAccessibleWindowContainer5childEi(
    const QAccessibleWindowContainer *self,
    int i) {
  return self->child(i);
}

#if QT_CONFIG(accessibility)
//  QWindowContainer *QAccessibleWindowContainer::container() const
extern "C" Q_DECL_EXPORT
QWindowContainer *ritual_ZNK26QAccessibleWindowContainer9containerEv(
    const QAccessibleWindowContainer *self) {
  return self->container();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QString QAccessibleWindowContainer::text(QAccessible::Text a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK26QAccessibleWindowContainer4textEN11QAccessible4TextE(
    const QAccessibleWindowContainer *self,
    QAccessible::Text a0) {
  return new QString(self->QAccessibleWindowContainer::text(a0));
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleWindowContainer::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QAccessibleWindowContainer10childCountEv(
    const QAccessibleWindowContainer *self) {
  return self->QAccessibleWindowContainer::childCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleWindowContainer::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QAccessibleWindowContainer12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleWindowContainer *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleWindowContainer::indexOfChild(child);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleWindowContainer::child(int i) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK26QAccessibleWindowContainer5childEi(
    const QAccessibleWindowContainer *self,
    int i) {
  return self->QAccessibleWindowContainer::child(i);
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
