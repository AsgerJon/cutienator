//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::ChangeTreeContentsCommand::ChangeTreeContentsCommand(
//      QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ChangeTreeContentsCommand *ritual_ZN18qdesigner_internal25ChangeTreeContentsCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::ChangeTreeContentsCommand(formWindow);
}

//  void qdesigner_internal::ChangeTreeContentsCommand::init(QTreeWidget
//      *treeWidget, const TreeWidgetContents &oldState, const
//      TreeWidgetContents &newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ChangeTreeContentsCommand4initEP11QTreeWidgetRKNS_18TreeWidgetContentsES5_(
    qdesigner_internal::ChangeTreeContentsCommand *self,
    QTreeWidget *treeWidget,
    const qdesigner_internal::TreeWidgetContents *oldState,
    const qdesigner_internal::TreeWidgetContents *newState) {
  self->init(treeWidget, *oldState, *newState);
}

//  void qdesigner_internal::ChangeTreeContentsCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ChangeTreeContentsCommand4redoEv(
    qdesigner_internal::ChangeTreeContentsCommand *self) {
  self->redo();
}

//  void qdesigner_internal::ChangeTreeContentsCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ChangeTreeContentsCommand4undoEv(
    qdesigner_internal::ChangeTreeContentsCommand *self) {
  self->undo();
}

//  void qdesigner_internal::ChangeTreeContentsCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal25ChangeTreeContentsCommand4redoEv(
    qdesigner_internal::ChangeTreeContentsCommand *self) {
  self->qdesigner_internal::ChangeTreeContentsCommand::redo();
}

//  void qdesigner_internal::ChangeTreeContentsCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal25ChangeTreeContentsCommand4undoEv(
    qdesigner_internal::ChangeTreeContentsCommand *self) {
  self->qdesigner_internal::ChangeTreeContentsCommand::undo();
}
