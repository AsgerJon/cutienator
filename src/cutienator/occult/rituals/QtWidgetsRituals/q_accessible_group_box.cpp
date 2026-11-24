//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
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

//  from src/widgets/accessible/simplewidgets.cpp, line 601, as _ZNK19QAccessibleGroupBox5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
inline QAccessible::State QAccessibleGroupBox::state() const
{
    QAccessible::State st = QAccessibleWidgetV2::state();
    st.checkable = groupBox()->isCheckable();
    st.checked = groupBox()->isChecked();
    return st;
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 609, as _ZNK19QAccessibleGroupBox4roleEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
inline QAccessible::Role QAccessibleGroupBox::role() const
{
    return groupBox()->isCheckable() ? QAccessible::CheckBox : QAccessible::Grouping;
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 631, as _ZNK19QAccessibleGroupBox11actionNamesEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
inline QStringList QAccessibleGroupBox::actionNames() const
{
    QStringList actions = QAccessibleWidgetV2::actionNames();

    if (groupBox()->isCheckable()) {
        actions.prepend(QAccessibleActionInterface::toggleAction());
    }
    return actions;
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 641, as _ZN19QAccessibleGroupBox8doActionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
inline void QAccessibleGroupBox::doAction(const QString &actionName)
{
    if (actionName == QAccessibleActionInterface::toggleAction())
        groupBox()->setChecked(!groupBox()->isChecked());
    else
        QAccessibleWidgetV2::doAction(actionName);
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 649, as _ZNK19QAccessibleGroupBox20keyBindingsForActionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
inline QStringList QAccessibleGroupBox::keyBindingsForAction(const QString &) const
{
    return QStringList();
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 571, as _ZNK19QAccessibleGroupBox8groupBoxEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
inline QGroupBox* QAccessibleGroupBox::groupBox() const
{
    return static_cast<QGroupBox *>(widget());
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  QAccessible::State QAccessibleGroupBox::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK19QAccessibleGroupBox5stateEv(
    const QAccessibleGroupBox *self) {
  return new QAccessible::State(self->state());
}

//  QAccessible::Role QAccessibleGroupBox::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QAccessibleGroupBox4roleEv(
    const QAccessibleGroupBox *self) {
  return self->role();
}

//  QStringList QAccessibleGroupBox::actionNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QAccessibleGroupBox11actionNamesEv(
    const QAccessibleGroupBox *self) {
  return new QList<QString>(self->actionNames());
}

//  void QAccessibleGroupBox::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleGroupBox8doActionERK7QString(
    QAccessibleGroupBox *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

//  QStringList QAccessibleGroupBox::keyBindingsForAction(const QString &a0)
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QAccessibleGroupBox20keyBindingsForActionERK7QString(
    const QAccessibleGroupBox *self,
    const QString *a0) {
  return new QList<QString>(self->keyBindingsForAction(*a0));
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
//  QGroupBox *QAccessibleGroupBox::groupBox() const
extern "C" Q_DECL_EXPORT
QGroupBox *ritual_ZNK19QAccessibleGroupBox8groupBoxEv(
    const QAccessibleGroupBox *self) {
  return self->groupBox();
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
//  QAccessible::State QAccessibleGroupBox::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK19QAccessibleGroupBox5stateEv(
    const QAccessibleGroupBox *self) {
  return new QAccessible::State(self->QAccessibleGroupBox::state());
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
//  QAccessible::Role QAccessibleGroupBox::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QAccessibleGroupBox4roleEv(
    const QAccessibleGroupBox *self) {
  return self->QAccessibleGroupBox::role();
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(groupbox)
//  void QAccessibleGroupBox::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleGroupBox8doActionERK7QString(
    QAccessibleGroupBox *self,
    const QString *actionName) {
  self->QAccessibleGroupBox::doAction(*actionName);
}
#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
