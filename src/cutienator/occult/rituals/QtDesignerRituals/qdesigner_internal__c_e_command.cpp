//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::CECommand::CECommand(ConnectionEdit *edit)
extern "C" Q_DECL_EXPORT
qdesigner_internal::CECommand *ritual_ZN18qdesigner_internal9CECommandC1EPNS_14ConnectionEditE(
    qdesigner_internal::ConnectionEdit *edit) {
  return new qdesigner_internal::CECommand(edit);
}

//  bool qdesigner_internal::CECommand::mergeWith(const QUndoCommand *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal9CECommand9mergeWithEPK12QUndoCommand(
    qdesigner_internal::CECommand *self,
    const QUndoCommand *a0) {
  return self->mergeWith(a0);
}

//  ConnectionEdit *qdesigner_internal::CECommand::edit() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::ConnectionEdit *ritual_ZNK18qdesigner_internal9CECommand4editEv(
    const qdesigner_internal::CECommand *self) {
  return self->edit();
}

//  qdesigner_internal::CECommand as the qdesigner_internal::CETypes it is
//      built on
extern "C" Q_DECL_EXPORT
qdesigner_internal::CETypes *ritual_cast_qdesigner_internal_CECommand_qdesigner_internal_CETypes(
    qdesigner_internal::CECommand *self) {
  return static_cast<qdesigner_internal::CETypes *>(self);
}

//  bool qdesigner_internal::CECommand::mergeWith(const QUndoCommand *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal9CECommand9mergeWithEPK12QUndoCommand(
    qdesigner_internal::CECommand *self,
    const QUndoCommand *a0) {
  return self->qdesigner_internal::CECommand::mergeWith(a0);
}
