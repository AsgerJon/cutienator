//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::AddActionCommand::AddActionCommand(QDesignerFormWindo
//      wInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::AddActionCommand *ritual_ZN18qdesigner_internal16AddActionCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::AddActionCommand(formWindow);
}

//  void qdesigner_internal::AddActionCommand::init(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16AddActionCommand4initEP7QAction(
    qdesigner_internal::AddActionCommand *self,
    QAction *action) {
  self->init(action);
}

//  void qdesigner_internal::AddActionCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16AddActionCommand4redoEv(
    qdesigner_internal::AddActionCommand *self) {
  self->redo();
}

//  void qdesigner_internal::AddActionCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16AddActionCommand4undoEv(
    qdesigner_internal::AddActionCommand *self) {
  self->undo();
}

//  void qdesigner_internal::AddActionCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal16AddActionCommand4redoEv(
    qdesigner_internal::AddActionCommand *self) {
  self->qdesigner_internal::AddActionCommand::redo();
}

//  void qdesigner_internal::AddActionCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal16AddActionCommand4undoEv(
    qdesigner_internal::AddActionCommand *self) {
  self->qdesigner_internal::AddActionCommand::undo();
}
