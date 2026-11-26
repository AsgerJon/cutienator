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

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 58, as local:qdesigner_command.cpp:setPropertySheetWindowTitle
static inline void setPropertySheetWindowTitle(const QDesignerFormEditorInterface *core, QObject *o, const QString &t)
{
    if (QDesignerPropertySheetExtension *sheet = qt_extension<QDesignerPropertySheetExtension*>(core->extensionManager(), o)) {
        const int idx = sheet->indexOf(u"windowTitle"_s);
        if (idx != -1) {
            sheet->setProperty(idx, t);
            sheet->setChanged(idx, true);
        }
    }
}

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1603, as _ZN18qdesigner_internal17AddToolBarCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddToolBarCommand::undo()
{
    QDesignerFormEditorInterface *core = formWindow()->core();
    core->metaDataBase()->remove(m_toolBar);
    QDesignerContainerExtension *c = qt_extension<QDesignerContainerExtension*>(core->extensionManager(), m_mainWindow);
    for (int i = 0; i < c->count(); ++i) {
        if (c->widget(i) == m_toolBar) {
            c->remove(i);
            break;
        }
    }
    formWindow()->emitSelectionChanged();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1589, as _ZN18qdesigner_internal17AddToolBarCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddToolBarCommand::redo()
{
    QDesignerFormEditorInterface *core = formWindow()->core();
    core->metaDataBase()->add(m_toolBar);

    QDesignerContainerExtension *c = qt_extension<QDesignerContainerExtension*>(core->extensionManager(), m_mainWindow);
    c->addWidget(m_toolBar);

    m_toolBar->setObjectName(u"toolBar"_s);
    formWindow()->ensureUniqueObjectName(m_toolBar);
    setPropertySheetWindowTitle(core, m_toolBar, m_toolBar->objectName());
    formWindow()->emitSelectionChanged();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1573, as _ZN18qdesigner_internal17AddToolBarCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline AddToolBarCommand::AddToolBarCommand(QDesignerFormWindowInterface *formWindow)
    : QDesignerFormWindowCommand(QApplication::translate("Command", "Add Tool Bar"), formWindow)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1578, as _ZN18qdesigner_internal17AddToolBarCommand4initEP11QMainWindowN2Qt11ToolBarAreaE
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddToolBarCommand::init(QMainWindow *mainWindow, Qt::ToolBarArea area)
{
    m_mainWindow = mainWindow;
    QDesignerWidgetFactoryInterface * wf =  formWindow()->core()->widgetFactory();
    // Pass on 0 parent first to avoid reparenting flicker.
    m_toolBar = qobject_cast<QToolBar*>(wf->createWidget(u"QToolBar"_s, nullptr));
    m_toolBar->setProperty("_q_desiredArea", QVariant(area));
    wf->initialize(m_toolBar);
    m_toolBar->hide();
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  qdesigner_internal::AddToolBarCommand::AddToolBarCommand(QDesignerFormWin
//      dowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::AddToolBarCommand *ritual_ZN18qdesigner_internal17AddToolBarCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::AddToolBarCommand(formWindow);
}

//  void qdesigner_internal::AddToolBarCommand::init(QMainWindow *mainWindow,
//      Qt::ToolBarArea area)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17AddToolBarCommand4initEP11QMainWindowN2Qt11ToolBarAreaE(
    qdesigner_internal::AddToolBarCommand *self,
    QMainWindow *mainWindow,
    Qt::ToolBarArea area) {
  self->init(mainWindow, area);
}

//  void qdesigner_internal::AddToolBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17AddToolBarCommand4undoEv(
    qdesigner_internal::AddToolBarCommand *self) {
  self->undo();
}

//  void qdesigner_internal::AddToolBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17AddToolBarCommand4redoEv(
    qdesigner_internal::AddToolBarCommand *self) {
  self->redo();
}

//  void qdesigner_internal::AddToolBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal17AddToolBarCommand4undoEv(
    qdesigner_internal::AddToolBarCommand *self) {
  self->qdesigner_internal::AddToolBarCommand::undo();
}

//  void qdesigner_internal::AddToolBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal17AddToolBarCommand4redoEv(
    qdesigner_internal::AddToolBarCommand *self) {
  self->qdesigner_internal::AddToolBarCommand::redo();
}
