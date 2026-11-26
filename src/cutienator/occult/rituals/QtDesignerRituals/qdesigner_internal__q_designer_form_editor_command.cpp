//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_formeditorcommand_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_formeditorcommand_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::QDesignerFormEditorCommand::QDesignerFormEditorComman
//      d(const QString &description, QDesignerFormEditorInterface *core)
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerFormEditorCommand *ritual_ZN18qdesigner_internal26QDesignerFormEditorCommandC1ERK7QStringP28QDesignerFormEditorInterface(
    const QString *description,
    QDesignerFormEditorInterface *core) {
  return new qdesigner_internal::QDesignerFormEditorCommand(
      *description,
      core);
}

//  QDesignerFormEditorInterface
//      *qdesigner_internal::QDesignerFormEditorCommand::core() const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK18qdesigner_internal26QDesignerFormEditorCommand4coreEv(
    const qdesigner_internal::QDesignerFormEditorCommand *self) {
  return self->core();
}
