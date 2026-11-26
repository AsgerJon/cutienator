//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::ChangeFormLayoutItemRoleCommand::ChangeFormLayoutItem
//      RoleCommand(QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ChangeFormLayoutItemRoleCommand *ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::ChangeFormLayoutItemRoleCommand(formWindow);
}

//  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::init(QWidget
//      *widget, Operation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand4initEP7QWidgetNS0_9OperationE(
    qdesigner_internal::ChangeFormLayoutItemRoleCommand *self,
    QWidget *widget,
    qdesigner_internal::ChangeFormLayoutItemRoleCommand::Operation op) {
  self->init(widget, op);
}

//  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand4redoEv(
    qdesigner_internal::ChangeFormLayoutItemRoleCommand *self) {
  self->redo();
}

//  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand4undoEv(
    qdesigner_internal::ChangeFormLayoutItemRoleCommand *self) {
  self->undo();
}

//  unsigned int qdesigner_internal::ChangeFormLayoutItemRoleCommand::possibl
//      eOperations(QDesignerFormEditorInterface *core, QWidget *w)
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand18possibleOperationsEP28QDesignerFormEditorInterfaceP7QWidget(
    QDesignerFormEditorInterface *core,
    QWidget *w) {
  return qdesigner_internal::ChangeFormLayoutItemRoleCommand::possibleOperations(
      core,
      w);
}

//  QFormLayout *qdesigner_internal::ChangeFormLayoutItemRoleCommand::managed
//      FormLayoutOf(QDesignerFormEditorInterface *core, QWidget *w)
extern "C" Q_DECL_EXPORT
QFormLayout *ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand19managedFormLayoutOfEP28QDesignerFormEditorInterfaceP7QWidget(
    QDesignerFormEditorInterface *core,
    QWidget *w) {
  return qdesigner_internal::ChangeFormLayoutItemRoleCommand::managedFormLayoutOf(
      core,
      w);
}

//  Operation qdesigner_internal::ChangeFormLayoutItemRoleCommand::reverseOpe
//      ration(Operation op)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ChangeFormLayoutItemRoleCommand::Operation ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand16reverseOperationENS0_9OperationE(
    qdesigner_internal::ChangeFormLayoutItemRoleCommand::Operation op) {
  return qdesigner_internal::ChangeFormLayoutItemRoleCommand::reverseOperation(
      op);
}

//  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::doOperation(Ope
//      ration op)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand11doOperationENS0_9OperationE(
    qdesigner_internal::ChangeFormLayoutItemRoleCommand *self,
    qdesigner_internal::ChangeFormLayoutItemRoleCommand::Operation op) {
  self->doOperation(op);
}

//  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand4redoEv(
    qdesigner_internal::ChangeFormLayoutItemRoleCommand *self) {
  self->qdesigner_internal::ChangeFormLayoutItemRoleCommand::redo();
}

//  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand4undoEv(
    qdesigner_internal::ChangeFormLayoutItemRoleCommand *self) {
  self->qdesigner_internal::ChangeFormLayoutItemRoleCommand::undo();
}
