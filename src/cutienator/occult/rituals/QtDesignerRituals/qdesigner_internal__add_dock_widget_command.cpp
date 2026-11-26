//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::AddDockWidgetCommand::AddDockWidgetCommand(QDesignerF
//      ormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::AddDockWidgetCommand *ritual_ZN18qdesigner_internal20AddDockWidgetCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::AddDockWidgetCommand(formWindow);
}

//  void qdesigner_internal::AddDockWidgetCommand::init(QMainWindow
//      *mainWindow, QDockWidget *dockWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20AddDockWidgetCommand4initEP11QMainWindowP11QDockWidget(
    qdesigner_internal::AddDockWidgetCommand *self,
    QMainWindow *mainWindow,
    QDockWidget *dockWidget) {
  self->init(mainWindow, dockWidget);
}

//  void qdesigner_internal::AddDockWidgetCommand::init(QMainWindow
//      *mainWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20AddDockWidgetCommand4initEP11QMainWindow(
    qdesigner_internal::AddDockWidgetCommand *self,
    QMainWindow *mainWindow) {
  self->init(mainWindow);
}

//  void qdesigner_internal::AddDockWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20AddDockWidgetCommand4undoEv(
    qdesigner_internal::AddDockWidgetCommand *self) {
  self->undo();
}

//  void qdesigner_internal::AddDockWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20AddDockWidgetCommand4redoEv(
    qdesigner_internal::AddDockWidgetCommand *self) {
  self->redo();
}

//  void qdesigner_internal::AddDockWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20AddDockWidgetCommand4undoEv(
    qdesigner_internal::AddDockWidgetCommand *self) {
  self->qdesigner_internal::AddDockWidgetCommand::undo();
}

//  void qdesigner_internal::AddDockWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20AddDockWidgetCommand4redoEv(
    qdesigner_internal::AddDockWidgetCommand *self) {
  self->qdesigner_internal::AddDockWidgetCommand::redo();
}
