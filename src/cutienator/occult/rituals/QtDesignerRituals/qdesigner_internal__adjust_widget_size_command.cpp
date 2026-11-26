//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::AdjustWidgetSizeCommand::AdjustWidgetSizeCommand(QDes
//      ignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::AdjustWidgetSizeCommand *ritual_ZN18qdesigner_internal23AdjustWidgetSizeCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::AdjustWidgetSizeCommand(formWindow);
}

//  void qdesigner_internal::AdjustWidgetSizeCommand::init(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23AdjustWidgetSizeCommand4initEP7QWidget(
    qdesigner_internal::AdjustWidgetSizeCommand *self,
    QWidget *widget) {
  self->init(widget);
}

//  void qdesigner_internal::AdjustWidgetSizeCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23AdjustWidgetSizeCommand4redoEv(
    qdesigner_internal::AdjustWidgetSizeCommand *self) {
  self->redo();
}

//  void qdesigner_internal::AdjustWidgetSizeCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23AdjustWidgetSizeCommand4undoEv(
    qdesigner_internal::AdjustWidgetSizeCommand *self) {
  self->undo();
}

//  QWidget *qdesigner_internal::AdjustWidgetSizeCommand::widgetForAdjust()
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal23AdjustWidgetSizeCommand15widgetForAdjustEv(
    const qdesigner_internal::AdjustWidgetSizeCommand *self) {
  return self->widgetForAdjust();
}

//  void qdesigner_internal::AdjustWidgetSizeCommand::updatePropertyEditor()
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal23AdjustWidgetSizeCommand20updatePropertyEditorEv(
    const qdesigner_internal::AdjustWidgetSizeCommand *self) {
  self->updatePropertyEditor();
}

//  void qdesigner_internal::AdjustWidgetSizeCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal23AdjustWidgetSizeCommand4redoEv(
    qdesigner_internal::AdjustWidgetSizeCommand *self) {
  self->qdesigner_internal::AdjustWidgetSizeCommand::redo();
}

//  void qdesigner_internal::AdjustWidgetSizeCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal23AdjustWidgetSizeCommand4undoEv(
    qdesigner_internal::AdjustWidgetSizeCommand *self) {
  self->qdesigner_internal::AdjustWidgetSizeCommand::undo();
}
