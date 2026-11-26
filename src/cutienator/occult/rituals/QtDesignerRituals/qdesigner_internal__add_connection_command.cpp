//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::AddConnectionCommand::AddConnectionCommand(Connection
//      Edit *edit, Connection *con)
extern "C" Q_DECL_EXPORT
qdesigner_internal::AddConnectionCommand *ritual_ZN18qdesigner_internal20AddConnectionCommandC1EPNS_14ConnectionEditEPNS_10ConnectionE(
    qdesigner_internal::ConnectionEdit *edit,
    qdesigner_internal::Connection *con) {
  return new qdesigner_internal::AddConnectionCommand(edit, con);
}

//  void qdesigner_internal::AddConnectionCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20AddConnectionCommand4redoEv(
    qdesigner_internal::AddConnectionCommand *self) {
  self->redo();
}

//  void qdesigner_internal::AddConnectionCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20AddConnectionCommand4undoEv(
    qdesigner_internal::AddConnectionCommand *self) {
  self->undo();
}

//  void qdesigner_internal::AddConnectionCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20AddConnectionCommand4redoEv(
    qdesigner_internal::AddConnectionCommand *self) {
  self->qdesigner_internal::AddConnectionCommand::redo();
}

//  void qdesigner_internal::AddConnectionCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20AddConnectionCommand4undoEv(
    qdesigner_internal::AddConnectionCommand *self) {
  self->qdesigner_internal::AddConnectionCommand::undo();
}
