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

//  const QWidgetList
//      &qdesigner_internal::ManageWidgetCommandHelper::managedChildren()
//      const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal25ManageWidgetCommandHelper15managedChildrenEv(
    const qdesigner_internal::ManageWidgetCommandHelper *self) {
  return new QList<QWidget *>(self->managedChildren());
}

//  qdesigner_internal::ManageWidgetCommandHelper::~ManageWidgetCommandHelper
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ManageWidgetCommandHelperD1Ev(
    qdesigner_internal::ManageWidgetCommandHelper *self) {
  delete self;
}
