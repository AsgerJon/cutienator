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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1442, as _ZN18qdesigner_internal20DeleteMenuBarCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline DeleteMenuBarCommand::DeleteMenuBarCommand(QDesignerFormWindowInterface *formWindow)
    : QDesignerFormWindowCommand(QApplication::translate("Command", "Delete Menu Bar"), formWindow)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1447, as _ZN18qdesigner_internal20DeleteMenuBarCommand4initEP8QMenuBar
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void DeleteMenuBarCommand::init(QMenuBar *menuBar)
{
    m_menuBar = menuBar;
    m_mainWindow = qobject_cast<QMainWindow*>(menuBar->parentWidget());
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1472, as _ZN18qdesigner_internal20DeleteMenuBarCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void DeleteMenuBarCommand::undo()
{
    if (m_mainWindow) {
        m_menuBar->setParent(m_mainWindow);
        auto *c = qt_extension<QDesignerContainerExtension*>(core()->extensionManager(), m_mainWindow);

        c->addWidget(m_menuBar);

        core()->metaDataBase()->add(m_menuBar);
        m_menuBar->show();
        formWindow()->emitSelectionChanged();
    }
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1453, as _ZN18qdesigner_internal20DeleteMenuBarCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void DeleteMenuBarCommand::redo()
{
    if (m_mainWindow) {
        auto *c = qt_extension<QDesignerContainerExtension*>(core()->extensionManager(), m_mainWindow);
        Q_ASSERT(c != nullptr);
        for (int i=0; i<c->count(); ++i) {
            if (c->widget(i) == m_menuBar) {
                c->remove(i);
                break;
            }
        }
    }

    core()->metaDataBase()->remove(m_menuBar);
    m_menuBar->hide();
    m_menuBar->setParent(formWindow());
    formWindow()->emitSelectionChanged();
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  qdesigner_internal::DeleteMenuBarCommand::DeleteMenuBarCommand(QDesignerF
//      ormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeleteMenuBarCommand *ritual_ZN18qdesigner_internal20DeleteMenuBarCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::DeleteMenuBarCommand(formWindow);
}

//  void qdesigner_internal::DeleteMenuBarCommand::init(QMenuBar *menuBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20DeleteMenuBarCommand4initEP8QMenuBar(
    qdesigner_internal::DeleteMenuBarCommand *self,
    QMenuBar *menuBar) {
  self->init(menuBar);
}

//  void qdesigner_internal::DeleteMenuBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20DeleteMenuBarCommand4undoEv(
    qdesigner_internal::DeleteMenuBarCommand *self) {
  self->undo();
}

//  void qdesigner_internal::DeleteMenuBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20DeleteMenuBarCommand4redoEv(
    qdesigner_internal::DeleteMenuBarCommand *self) {
  self->redo();
}

//  void qdesigner_internal::DeleteMenuBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20DeleteMenuBarCommand4undoEv(
    qdesigner_internal::DeleteMenuBarCommand *self) {
  self->qdesigner_internal::DeleteMenuBarCommand::undo();
}

//  void qdesigner_internal::DeleteMenuBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20DeleteMenuBarCommand4redoEv(
    qdesigner_internal::DeleteMenuBarCommand *self) {
  self->qdesigner_internal::DeleteMenuBarCommand::redo();
}
