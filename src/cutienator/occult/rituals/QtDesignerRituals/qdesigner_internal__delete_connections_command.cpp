//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::DeleteConnectionsCommand::DeleteConnectionsCommand(Co
//      nnectionEdit *edit, const ConnectionList &con_list)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeleteConnectionsCommand *ritual_ZN18qdesigner_internal24DeleteConnectionsCommandC1EPNS_14ConnectionEditERK5QListIPNS_10ConnectionEE(
    qdesigner_internal::ConnectionEdit *edit,
    const qdesigner_internal::CETypes::ConnectionList *con_list) {
  return new qdesigner_internal::DeleteConnectionsCommand(edit, *con_list);
}

//  void qdesigner_internal::DeleteConnectionsCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24DeleteConnectionsCommand4redoEv(
    qdesigner_internal::DeleteConnectionsCommand *self) {
  self->redo();
}

//  void qdesigner_internal::DeleteConnectionsCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24DeleteConnectionsCommand4undoEv(
    qdesigner_internal::DeleteConnectionsCommand *self) {
  self->undo();
}

//  void qdesigner_internal::DeleteConnectionsCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal24DeleteConnectionsCommand4redoEv(
    qdesigner_internal::DeleteConnectionsCommand *self) {
  self->qdesigner_internal::DeleteConnectionsCommand::redo();
}

//  void qdesigner_internal::DeleteConnectionsCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal24DeleteConnectionsCommand4undoEv(
    qdesigner_internal::DeleteConnectionsCommand *self) {
  self->qdesigner_internal::DeleteConnectionsCommand::undo();
}
