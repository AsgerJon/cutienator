//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::PromoteToCustomWidgetCommand::PromoteToCustomWidgetCo
//      mmand(QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PromoteToCustomWidgetCommand *ritual_ZN18qdesigner_internal28PromoteToCustomWidgetCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::PromoteToCustomWidgetCommand(formWindow);
}

//  void qdesigner_internal::PromoteToCustomWidgetCommand::init(const
//      WidgetPointerList &widgets, const QString &customClassName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal28PromoteToCustomWidgetCommand4initERK5QListI8QPointerI7QWidgetEERK7QString(
    qdesigner_internal::PromoteToCustomWidgetCommand *self,
    const qdesigner_internal::PromoteToCustomWidgetCommand::WidgetPointerList *widgets,
    const QString *customClassName) {
  self->init(*widgets, *customClassName);
}

//  void qdesigner_internal::PromoteToCustomWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal28PromoteToCustomWidgetCommand4redoEv(
    qdesigner_internal::PromoteToCustomWidgetCommand *self) {
  self->redo();
}

//  void qdesigner_internal::PromoteToCustomWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal28PromoteToCustomWidgetCommand4undoEv(
    qdesigner_internal::PromoteToCustomWidgetCommand *self) {
  self->undo();
}

//  void qdesigner_internal::PromoteToCustomWidgetCommand::updateSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal28PromoteToCustomWidgetCommand15updateSelectionEv(
    qdesigner_internal::PromoteToCustomWidgetCommand *self) {
  self->updateSelection();
}

//  void qdesigner_internal::PromoteToCustomWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal28PromoteToCustomWidgetCommand4redoEv(
    qdesigner_internal::PromoteToCustomWidgetCommand *self) {
  self->qdesigner_internal::PromoteToCustomWidgetCommand::redo();
}

//  void qdesigner_internal::PromoteToCustomWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal28PromoteToCustomWidgetCommand4undoEv(
    qdesigner_internal::PromoteToCustomWidgetCommand *self) {
  self->qdesigner_internal::PromoteToCustomWidgetCommand::undo();
}
