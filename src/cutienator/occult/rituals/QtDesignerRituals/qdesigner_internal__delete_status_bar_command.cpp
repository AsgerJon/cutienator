//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::DeleteStatusBarCommand::DeleteStatusBarCommand(QDesig
//      nerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeleteStatusBarCommand *ritual_ZN18qdesigner_internal22DeleteStatusBarCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::DeleteStatusBarCommand(formWindow);
}

//  void qdesigner_internal::DeleteStatusBarCommand::init(QStatusBar
//      *statusBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22DeleteStatusBarCommand4initEP10QStatusBar(
    qdesigner_internal::DeleteStatusBarCommand *self,
    QStatusBar *statusBar) {
  self->init(statusBar);
}

//  void qdesigner_internal::DeleteStatusBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22DeleteStatusBarCommand4undoEv(
    qdesigner_internal::DeleteStatusBarCommand *self) {
  self->undo();
}

//  void qdesigner_internal::DeleteStatusBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22DeleteStatusBarCommand4redoEv(
    qdesigner_internal::DeleteStatusBarCommand *self) {
  self->redo();
}

//  void qdesigner_internal::DeleteStatusBarCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal22DeleteStatusBarCommand4undoEv(
    qdesigner_internal::DeleteStatusBarCommand *self) {
  self->qdesigner_internal::DeleteStatusBarCommand::undo();
}

//  void qdesigner_internal::DeleteStatusBarCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal22DeleteStatusBarCommand4redoEv(
    qdesigner_internal::DeleteStatusBarCommand *self) {
  self->qdesigner_internal::DeleteStatusBarCommand::redo();
}
