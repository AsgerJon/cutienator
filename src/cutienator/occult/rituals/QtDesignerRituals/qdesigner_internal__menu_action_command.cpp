//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/qdesigner_command_p.h>
#include <QtDesigner/private/qdesigner_utils_p.h>
#include <QtDesigner/private/layout_p.h>
#include <QtDesigner/private/qlayout_widget_p.h>
#include <QtDesigner/private/qdesigner_widget_p.h>
#include <QtDesigner/private/qdesigner_menu_p.h>
#include <QtDesigner/private/shared_enums_p.h>
#include <QtDesigner/private/metadatabase_p.h>
#include <QtDesigner/private/formwindowbase_p.h>
#include <QtDesigner/abstractformbuilder.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/propertysheet.h>
#include <QtDesigner/abstractactioneditor.h>
#include <QtDesigner/abstractpropertyeditor.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtDesigner/container.h>
#include <QtDesigner/layoutdecoration.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtDesigner/abstractobjectinspector.h>
#include <QtDesigner/abstractintegration.h>
#include <QtDesigner/abstractformwindowcursor.h>
#include <QtCore/qdebug.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qqueue.h>
#include <QtWidgets/qmenubar.h>
#include <QtWidgets/qstatusbar.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qtoolbox.h>
#include <QtWidgets/qstackedwidget.h>
#include <QtWidgets/qtabwidget.h>
#include <QtWidgets/qtablewidget.h>
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/qcombobox.h>
#include <QtWidgets/qsplitter.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qwizard.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qformlayout.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2739, as _ZN18qdesigner_internal17MenuActionCommand4initEP7QActionS2_P7QWidgetS4_
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MenuActionCommand::init(QAction *action, QAction *actionBefore,
                             QWidget *associatedWidget, QWidget *objectToSelect)
{
    QMenu *menu = action->menu();
    Q_ASSERT(menu);
    m_menuParent = menu->parentWidget();
    m_action = action;
    m_actionBefore = actionBefore;
    m_associatedWidget = associatedWidget;
    m_objectToSelect = objectToSelect;
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2729, as _ZN18qdesigner_internal17MenuActionCommandC1ERK7QStringP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline MenuActionCommand::MenuActionCommand(const QString &text, QDesignerFormWindowInterface *formWindow) :
    QDesignerFormWindowCommand(text, formWindow),
    m_action(nullptr),
    m_actionBefore(nullptr),
    m_menuParent(nullptr),
    m_associatedWidget(nullptr),
    m_objectToSelect(nullptr)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2751, as _ZN18qdesigner_internal17MenuActionCommand10insertMenuEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MenuActionCommand::insertMenu()
{
    core()->metaDataBase()->add(m_action);
    QMenu *menu = m_action->menu();
    if (m_menuParent && menu->parentWidget() != m_menuParent)
        menu->setParent(m_menuParent);
    core()->metaDataBase()->add(menu);
    m_associatedWidget->insertAction(m_actionBefore, m_action);
    cheapUpdate();
    selectUnmanagedObject(menu);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2763, as _ZN18qdesigner_internal17MenuActionCommand10removeMenuEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MenuActionCommand::removeMenu()
{
    m_action->menu()->setParent(nullptr);
    QMenu *menu = m_action->menu();
    core()->metaDataBase()->remove(menu);
    menu->setParent(nullptr);
    core()->metaDataBase()->remove(m_action);
    m_associatedWidget->removeAction(m_action);
    cheapUpdate();
    selectUnmanagedObject(m_objectToSelect);
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  void qdesigner_internal::MenuActionCommand::init(QAction *action, QAction
//      *actionBefore, QWidget *associatedWidget, QWidget *objectToSelect)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17MenuActionCommand4initEP7QActionS2_P7QWidgetS4_(
    qdesigner_internal::MenuActionCommand *self,
    QAction *action,
    QAction *actionBefore,
    QWidget *associatedWidget,
    QWidget *objectToSelect) {
  self->init(action, actionBefore, associatedWidget, objectToSelect);
}

//  qdesigner_internal::MenuActionCommand::MenuActionCommand(const QString
//      &text, QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::MenuActionCommand *ritual_ZN18qdesigner_internal17MenuActionCommandC1ERK7QStringP28QDesignerFormWindowInterface(
    const QString *text,
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::MenuActionCommand(*text, formWindow);
}

//  void qdesigner_internal::MenuActionCommand::insertMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17MenuActionCommand10insertMenuEv(
    qdesigner_internal::MenuActionCommand *self) {
  self->insertMenu();
}

//  void qdesigner_internal::MenuActionCommand::removeMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17MenuActionCommand10removeMenuEv(
    qdesigner_internal::MenuActionCommand *self) {
  self->removeMenu();
}
