//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::ReparentWidgetCommand::ReparentWidgetCommand(QDesigne
//      rFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ReparentWidgetCommand *ritual_ZN18qdesigner_internal21ReparentWidgetCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::ReparentWidgetCommand(formWindow);
}

//  void qdesigner_internal::ReparentWidgetCommand::init(QWidget *widget,
//      QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21ReparentWidgetCommand4initEP7QWidgetS2_(
    qdesigner_internal::ReparentWidgetCommand *self,
    QWidget *widget,
    QWidget *parentWidget) {
  self->init(widget, parentWidget);
}

//  void qdesigner_internal::ReparentWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21ReparentWidgetCommand4redoEv(
    qdesigner_internal::ReparentWidgetCommand *self) {
  self->redo();
}

//  void qdesigner_internal::ReparentWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21ReparentWidgetCommand4undoEv(
    qdesigner_internal::ReparentWidgetCommand *self) {
  self->undo();
}

//  void qdesigner_internal::ReparentWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal21ReparentWidgetCommand4redoEv(
    qdesigner_internal::ReparentWidgetCommand *self) {
  self->qdesigner_internal::ReparentWidgetCommand::redo();
}

//  void qdesigner_internal::ReparentWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal21ReparentWidgetCommand4undoEv(
    qdesigner_internal::ReparentWidgetCommand *self) {
  self->qdesigner_internal::ReparentWidgetCommand::undo();
}
