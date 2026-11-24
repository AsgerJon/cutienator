//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qwidget.h>
#include <QtCore/qlist.h>

//  QWidgetList qdesigner_internal::TabOrderCommand::oldTabOrder() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal15TabOrderCommand11oldTabOrderEv(
    const qdesigner_internal::TabOrderCommand *self) {
  return new QList<QWidget *>(self->oldTabOrder());
}

//  QWidgetList qdesigner_internal::TabOrderCommand::newTabOrder() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal15TabOrderCommand11newTabOrderEv(
    const qdesigner_internal::TabOrderCommand *self) {
  return new QList<QWidget *>(self->newTabOrder());
}

//  void qdesigner_internal::TabOrderCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal15TabOrderCommand4redoEv(
    qdesigner_internal::TabOrderCommand *self) {
  self->qdesigner_internal::TabOrderCommand::redo();
}

//  void qdesigner_internal::TabOrderCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal15TabOrderCommand4undoEv(
    qdesigner_internal::TabOrderCommand *self) {
  self->qdesigner_internal::TabOrderCommand::undo();
}
