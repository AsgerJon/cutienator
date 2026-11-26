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

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1487, as _ZN18qdesigner_internal22CreateStatusBarCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline CreateStatusBarCommand::CreateStatusBarCommand(QDesignerFormWindowInterface *formWindow)
    : QDesignerFormWindowCommand(QApplication::translate("Command", "Create Status Bar"), formWindow)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1492, as _ZN18qdesigner_internal22CreateStatusBarCommand4initEP11QMainWindow
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void CreateStatusBarCommand::init(QMainWindow *mainWindow)
{
    m_mainWindow = mainWindow;
    QDesignerFormEditorInterface *core = formWindow()->core();
    m_statusBar = qobject_cast<QStatusBar*>(core->widgetFactory()->createWidget(u"QStatusBar"_s, m_mainWindow));
    core->widgetFactory()->initialize(m_statusBar);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1512, as _ZN18qdesigner_internal22CreateStatusBarCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void CreateStatusBarCommand::undo()
{
    QDesignerFormEditorInterface *core = formWindow()->core();
    QDesignerContainerExtension *c = qt_extension<QDesignerContainerExtension*>(core->extensionManager(), m_mainWindow);
    for (int i = 0; i < c->count(); ++i) {
        if (c->widget(i) == m_statusBar) {
            c->remove(i);
            break;
        }
    }

    core->metaDataBase()->remove(m_statusBar);
    formWindow()->emitSelectionChanged();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1500, as _ZN18qdesigner_internal22CreateStatusBarCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void CreateStatusBarCommand::redo()
{
    QDesignerFormEditorInterface *core = formWindow()->core();
    auto *c = qt_extension<QDesignerContainerExtension*>(core->extensionManager(), m_mainWindow);
    c->addWidget(m_statusBar);

    m_statusBar->setObjectName(u"statusBar"_s);
    formWindow()->ensureUniqueObjectName(m_statusBar);
    core->metaDataBase()->add(m_statusBar);
    formWindow()->emitSelectionChanged();
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  qdesigner_internal::CreateStatusBarCommand::CreateStatusBarCommand(QDesig
//      nerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::CreateStatusBarCommand *ritual_ZN18qdesigner_internal22CreateStatusBarCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::CreateStatusBarCommand(formWindow);
}

//  void qdesigner_internal::CreateStatusBarCommand::init(QMainWindow
//      *mainWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22CreateStatusBarCommand4initEP11QMainWindow(
    qdesigner_internal::CreateStatusBarCommand *self,
    QMainWindow *mainWindow) {
  self->init(mainWindow);
}

//  void qdesigner_internal::CreateStatusBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22CreateStatusBarCommand4undoEv(
    qdesigner_internal::CreateStatusBarCommand *self) {
  self->undo();
}

//  void qdesigner_internal::CreateStatusBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22CreateStatusBarCommand4redoEv(
    qdesigner_internal::CreateStatusBarCommand *self) {
  self->redo();
}

//  void qdesigner_internal::CreateStatusBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal22CreateStatusBarCommand4undoEv(
    qdesigner_internal::CreateStatusBarCommand *self) {
  self->qdesigner_internal::CreateStatusBarCommand::undo();
}

//  void qdesigner_internal::CreateStatusBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal22CreateStatusBarCommand4redoEv(
    qdesigner_internal::CreateStatusBarCommand *self) {
  self->qdesigner_internal::CreateStatusBarCommand::redo();
}
