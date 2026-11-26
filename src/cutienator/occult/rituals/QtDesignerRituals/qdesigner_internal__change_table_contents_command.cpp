//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::ChangeTableContentsCommand::ChangeTableContentsComman
//      d(QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ChangeTableContentsCommand *ritual_ZN18qdesigner_internal26ChangeTableContentsCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::ChangeTableContentsCommand(formWindow);
}

//  void qdesigner_internal::ChangeTableContentsCommand::init(QTableWidget
//      *tableWidget, const TableWidgetContents &oldCont, const
//      TableWidgetContents &newCont)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26ChangeTableContentsCommand4initEP12QTableWidgetRKNS_19TableWidgetContentsES5_(
    qdesigner_internal::ChangeTableContentsCommand *self,
    QTableWidget *tableWidget,
    const qdesigner_internal::TableWidgetContents *oldCont,
    const qdesigner_internal::TableWidgetContents *newCont) {
  self->init(tableWidget, *oldCont, *newCont);
}

//  void qdesigner_internal::ChangeTableContentsCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26ChangeTableContentsCommand4redoEv(
    qdesigner_internal::ChangeTableContentsCommand *self) {
  self->redo();
}

//  void qdesigner_internal::ChangeTableContentsCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26ChangeTableContentsCommand4undoEv(
    qdesigner_internal::ChangeTableContentsCommand *self) {
  self->undo();
}

//  void qdesigner_internal::ChangeTableContentsCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal26ChangeTableContentsCommand4redoEv(
    qdesigner_internal::ChangeTableContentsCommand *self) {
  self->qdesigner_internal::ChangeTableContentsCommand::redo();
}

//  void qdesigner_internal::ChangeTableContentsCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal26ChangeTableContentsCommand4undoEv(
    qdesigner_internal::ChangeTableContentsCommand *self) {
  self->qdesigner_internal::ChangeTableContentsCommand::undo();
}
