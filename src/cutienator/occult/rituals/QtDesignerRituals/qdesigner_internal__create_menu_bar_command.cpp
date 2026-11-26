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

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1400, as _ZN18qdesigner_internal20CreateMenuBarCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline CreateMenuBarCommand::CreateMenuBarCommand(QDesignerFormWindowInterface *formWindow)
    : QDesignerFormWindowCommand(QApplication::translate("Command", "Create Menu Bar"), formWindow)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1405, as _ZN18qdesigner_internal20CreateMenuBarCommand4initEP11QMainWindow
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void CreateMenuBarCommand::init(QMainWindow *mainWindow)
{
    m_mainWindow = mainWindow;
    QDesignerFormEditorInterface *core = formWindow()->core();
    m_menuBar = qobject_cast<QMenuBar*>(core->widgetFactory()->createWidget(u"QMenuBar"_s, m_mainWindow));
    core->widgetFactory()->initialize(m_menuBar);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1426, as _ZN18qdesigner_internal20CreateMenuBarCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void CreateMenuBarCommand::undo()
{
    QDesignerFormEditorInterface *core = formWindow()->core();
    auto *c = qt_extension<QDesignerContainerExtension*>(core->extensionManager(), m_mainWindow);
    for (int i = 0; i < c->count(); ++i) {
        if (c->widget(i) == m_menuBar) {
            c->remove(i);
            break;
        }
    }

    core->metaDataBase()->remove(m_menuBar);
    formWindow()->emitSelectionChanged();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1413, as _ZN18qdesigner_internal20CreateMenuBarCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void CreateMenuBarCommand::redo()
{
    QDesignerFormEditorInterface *core = formWindow()->core();
    auto *c = qt_extension<QDesignerContainerExtension*>(core->extensionManager(), m_mainWindow);
    c->addWidget(m_menuBar);

    m_menuBar->setObjectName(u"menuBar"_s);
    formWindow()->ensureUniqueObjectName(m_menuBar);
    core->metaDataBase()->add(m_menuBar);
    formWindow()->emitSelectionChanged();
    m_menuBar->setFocus();
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  qdesigner_internal::CreateMenuBarCommand::CreateMenuBarCommand(QDesignerF
//      ormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::CreateMenuBarCommand *ritual_ZN18qdesigner_internal20CreateMenuBarCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::CreateMenuBarCommand(formWindow);
}

//  void qdesigner_internal::CreateMenuBarCommand::init(QMainWindow
//      *mainWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20CreateMenuBarCommand4initEP11QMainWindow(
    qdesigner_internal::CreateMenuBarCommand *self,
    QMainWindow *mainWindow) {
  self->init(mainWindow);
}

//  void qdesigner_internal::CreateMenuBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20CreateMenuBarCommand4undoEv(
    qdesigner_internal::CreateMenuBarCommand *self) {
  self->undo();
}

//  void qdesigner_internal::CreateMenuBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20CreateMenuBarCommand4redoEv(
    qdesigner_internal::CreateMenuBarCommand *self) {
  self->redo();
}

//  void qdesigner_internal::CreateMenuBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20CreateMenuBarCommand4undoEv(
    qdesigner_internal::CreateMenuBarCommand *self) {
  self->qdesigner_internal::CreateMenuBarCommand::undo();
}

//  void qdesigner_internal::CreateMenuBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20CreateMenuBarCommand4redoEv(
    qdesigner_internal::CreateMenuBarCommand *self) {
  self->qdesigner_internal::CreateMenuBarCommand::redo();
}
