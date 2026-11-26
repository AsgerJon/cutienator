//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2787, as _ZN18qdesigner_internal20CreateSubmenuCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline CreateSubmenuCommand::CreateSubmenuCommand(QDesignerFormWindowInterface *formWindow) :
    QDesignerFormWindowCommand(QApplication::translate("Command", "Create submenu"), formWindow),
    m_action(nullptr),
    m_menu(nullptr),
    m_objectToSelect(nullptr)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2795, as _ZN18qdesigner_internal20CreateSubmenuCommand4initEP13QDesignerMenuP7QActionP7QObject
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void CreateSubmenuCommand::init(QDesignerMenu *menu, QAction *action, QObject *objectToSelect)
{
    m_menu = menu;
    m_action = action;
    m_objectToSelect = objectToSelect;
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2802, as _ZN18qdesigner_internal20CreateSubmenuCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void CreateSubmenuCommand::redo()
{
    m_menu->createRealMenuAction(m_action);
    cheapUpdate();
    if (m_objectToSelect)
        selectUnmanagedObject(m_objectToSelect);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2810, as _ZN18qdesigner_internal20CreateSubmenuCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void CreateSubmenuCommand::undo()
{
    m_menu->removeRealMenu(m_action);
    cheapUpdate();
    selectUnmanagedObject(m_menu);
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  qdesigner_internal::CreateSubmenuCommand::CreateSubmenuCommand(QDesignerF
//      ormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::CreateSubmenuCommand *ritual_ZN18qdesigner_internal20CreateSubmenuCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::CreateSubmenuCommand(formWindow);
}

//  void qdesigner_internal::CreateSubmenuCommand::init(QDesignerMenu *menu,
//      QAction *action, QObject *m_objectToSelect)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20CreateSubmenuCommand4initEP13QDesignerMenuP7QActionP7QObject(
    qdesigner_internal::CreateSubmenuCommand *self,
    QDesignerMenu *menu,
    QAction *action,
    QObject *m_objectToSelect) {
  self->init(menu, action, m_objectToSelect);
}

//  void qdesigner_internal::CreateSubmenuCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20CreateSubmenuCommand4redoEv(
    qdesigner_internal::CreateSubmenuCommand *self) {
  self->redo();
}

//  void qdesigner_internal::CreateSubmenuCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20CreateSubmenuCommand4undoEv(
    qdesigner_internal::CreateSubmenuCommand *self) {
  self->undo();
}

//  void qdesigner_internal::CreateSubmenuCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20CreateSubmenuCommand4redoEv(
    qdesigner_internal::CreateSubmenuCommand *self) {
  self->qdesigner_internal::CreateSubmenuCommand::redo();
}

//  void qdesigner_internal::CreateSubmenuCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20CreateSubmenuCommand4undoEv(
    qdesigner_internal::CreateSubmenuCommand *self) {
  self->qdesigner_internal::CreateSubmenuCommand::undo();
}
