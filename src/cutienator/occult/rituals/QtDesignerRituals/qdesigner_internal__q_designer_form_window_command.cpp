//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_formwindowcommand_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_formwindowcommand_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::QDesignerFormWindowCommand::QDesignerFormWindowComman
//      d(const QString &description, QDesignerFormWindowInterface
//      *formWindow, QUndoCommand *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerFormWindowCommand *ritual_ZN18qdesigner_internal26QDesignerFormWindowCommandC1ERK7QStringP28QDesignerFormWindowInterfaceP12QUndoCommand(
    const QString *description,
    QDesignerFormWindowInterface *formWindow,
    QUndoCommand *parent) {
  return new qdesigner_internal::QDesignerFormWindowCommand(
      *description,
      formWindow,
      parent);
}

//  void qdesigner_internal::QDesignerFormWindowCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand4undoEv(
    qdesigner_internal::QDesignerFormWindowCommand *self) {
  self->undo();
}

//  void qdesigner_internal::QDesignerFormWindowCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand4redoEv(
    qdesigner_internal::QDesignerFormWindowCommand *self) {
  self->redo();
}

//  void qdesigner_internal::QDesignerFormWindowCommand::updateBuddies(QDesig
//      nerFormWindowInterface *form, const QString &old_name, const QString
//      &new_name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand13updateBuddiesEP28QDesignerFormWindowInterfaceRK7QStringS5_(
    QDesignerFormWindowInterface *form,
    const QString *old_name,
    const QString *new_name) {
  qdesigner_internal::QDesignerFormWindowCommand::updateBuddies(
      form,
      *old_name,
      *new_name);
}

//  QDesignerFormWindowInterface
//      *qdesigner_internal::QDesignerFormWindowCommand::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK18qdesigner_internal26QDesignerFormWindowCommand10formWindowEv(
    const qdesigner_internal::QDesignerFormWindowCommand *self) {
  return self->formWindow();
}

//  QDesignerFormEditorInterface
//      *qdesigner_internal::QDesignerFormWindowCommand::core() const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK18qdesigner_internal26QDesignerFormWindowCommand4coreEv(
    const qdesigner_internal::QDesignerFormWindowCommand *self) {
  return self->core();
}

//  QDesignerPropertySheetExtension
//      *qdesigner_internal::QDesignerFormWindowCommand::propertySheet(QObjec
//      t *object) const
extern "C" Q_DECL_EXPORT
QDesignerPropertySheetExtension *ritual_ZNK18qdesigner_internal26QDesignerFormWindowCommand13propertySheetEP7QObject(
    const qdesigner_internal::QDesignerFormWindowCommand *self,
    QObject *object) {
  return self->propertySheet(object);
}

//  void qdesigner_internal::QDesignerFormWindowCommand::cheapUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand11cheapUpdateEv(
    qdesigner_internal::QDesignerFormWindowCommand *self) {
  self->cheapUpdate();
}

//  void qdesigner_internal::QDesignerFormWindowCommand::selectUnmanagedObjec
//      t(QObject *unmanagedObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand21selectUnmanagedObjectEP7QObject(
    qdesigner_internal::QDesignerFormWindowCommand *self,
    QObject *unmanagedObject) {
  self->selectUnmanagedObject(unmanagedObject);
}

//  void qdesigner_internal::QDesignerFormWindowCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal26QDesignerFormWindowCommand4undoEv(
    qdesigner_internal::QDesignerFormWindowCommand *self) {
  self->qdesigner_internal::QDesignerFormWindowCommand::undo();
}

//  void qdesigner_internal::QDesignerFormWindowCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal26QDesignerFormWindowCommand4redoEv(
    qdesigner_internal::QDesignerFormWindowCommand *self) {
  self->qdesigner_internal::QDesignerFormWindowCommand::redo();
}
