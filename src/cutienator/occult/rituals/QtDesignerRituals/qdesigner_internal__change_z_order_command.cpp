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

//  QWidgetList qdesigner_internal::ChangeZOrderCommand::reorderWidget(const
//      QWidgetList &list, QWidget *widget) const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal19ChangeZOrderCommand13reorderWidgetERK5QListIP7QWidgetES3_(
    const qdesigner_internal::ChangeZOrderCommand *self,
    const QList<QWidget *> *list,
    QWidget *widget) {
  return new QList<QWidget *>(self->reorderWidget(*list, widget));
}

//  void qdesigner_internal::ChangeZOrderCommand::reorder(QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal19ChangeZOrderCommand7reorderEP7QWidget(
    const qdesigner_internal::ChangeZOrderCommand *self,
    QWidget *widget) {
  self->reorder(widget);
}

//  void qdesigner_internal::ChangeZOrderCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal19ChangeZOrderCommand4redoEv(
    qdesigner_internal::ChangeZOrderCommand *self) {
  self->qdesigner_internal::ChangeZOrderCommand::redo();
}

//  void qdesigner_internal::ChangeZOrderCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal19ChangeZOrderCommand4undoEv(
    qdesigner_internal::ChangeZOrderCommand *self) {
  self->qdesigner_internal::ChangeZOrderCommand::undo();
}
