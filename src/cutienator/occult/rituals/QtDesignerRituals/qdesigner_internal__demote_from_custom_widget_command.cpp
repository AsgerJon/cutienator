//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::DemoteFromCustomWidgetCommand::DemoteFromCustomWidget
//      Command(QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DemoteFromCustomWidgetCommand *ritual_ZN18qdesigner_internal29DemoteFromCustomWidgetCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::DemoteFromCustomWidgetCommand(formWindow);
}

//  void qdesigner_internal::DemoteFromCustomWidgetCommand::init(const
//      WidgetList &promoted)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29DemoteFromCustomWidgetCommand4initERK5QListI8QPointerI7QWidgetEE(
    qdesigner_internal::DemoteFromCustomWidgetCommand *self,
    const qdesigner_internal::DemoteFromCustomWidgetCommand::WidgetList *promoted) {
  self->init(*promoted);
}

//  void qdesigner_internal::DemoteFromCustomWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29DemoteFromCustomWidgetCommand4redoEv(
    qdesigner_internal::DemoteFromCustomWidgetCommand *self) {
  self->redo();
}

//  void qdesigner_internal::DemoteFromCustomWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29DemoteFromCustomWidgetCommand4undoEv(
    qdesigner_internal::DemoteFromCustomWidgetCommand *self) {
  self->undo();
}

//  void qdesigner_internal::DemoteFromCustomWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal29DemoteFromCustomWidgetCommand4redoEv(
    qdesigner_internal::DemoteFromCustomWidgetCommand *self) {
  self->qdesigner_internal::DemoteFromCustomWidgetCommand::redo();
}

//  void qdesigner_internal::DemoteFromCustomWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal29DemoteFromCustomWidgetCommand4undoEv(
    qdesigner_internal::DemoteFromCustomWidgetCommand *self) {
  self->qdesigner_internal::DemoteFromCustomWidgetCommand::undo();
}
