//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::ChangeListContentsCommand::ChangeListContentsCommand(
//      QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ChangeListContentsCommand *ritual_ZN18qdesigner_internal25ChangeListContentsCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::ChangeListContentsCommand(formWindow);
}

//  void qdesigner_internal::ChangeListContentsCommand::init(QListWidget
//      *listWidget, const ListContents &oldItems, const ListContents &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ChangeListContentsCommand4initEP11QListWidgetRKNS_12ListContentsES5_(
    qdesigner_internal::ChangeListContentsCommand *self,
    QListWidget *listWidget,
    const qdesigner_internal::ListContents *oldItems,
    const qdesigner_internal::ListContents *items) {
  self->init(listWidget, *oldItems, *items);
}

//  void qdesigner_internal::ChangeListContentsCommand::init(QComboBox
//      *comboBox, const ListContents &oldItems, const ListContents &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ChangeListContentsCommand4initEP9QComboBoxRKNS_12ListContentsES5_(
    qdesigner_internal::ChangeListContentsCommand *self,
    QComboBox *comboBox,
    const qdesigner_internal::ListContents *oldItems,
    const qdesigner_internal::ListContents *items) {
  self->init(comboBox, *oldItems, *items);
}

//  void qdesigner_internal::ChangeListContentsCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ChangeListContentsCommand4redoEv(
    qdesigner_internal::ChangeListContentsCommand *self) {
  self->redo();
}

//  void qdesigner_internal::ChangeListContentsCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ChangeListContentsCommand4undoEv(
    qdesigner_internal::ChangeListContentsCommand *self) {
  self->undo();
}

//  void qdesigner_internal::ChangeListContentsCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal25ChangeListContentsCommand4redoEv(
    qdesigner_internal::ChangeListContentsCommand *self) {
  self->qdesigner_internal::ChangeListContentsCommand::redo();
}

//  void qdesigner_internal::ChangeListContentsCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal25ChangeListContentsCommand4undoEv(
    qdesigner_internal::ChangeListContentsCommand *self) {
  self->qdesigner_internal::ChangeListContentsCommand::undo();
}
