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

//  qdesigner_internal::ManageWidgetCommandHelper::ManageWidgetCommandHelper(
//      )
extern "C" Q_DECL_EXPORT
qdesigner_internal::ManageWidgetCommandHelper *ritual_ZN18qdesigner_internal25ManageWidgetCommandHelperC1Ev() {
  return new qdesigner_internal::ManageWidgetCommandHelper();
}

//  void qdesigner_internal::ManageWidgetCommandHelper::init(const
//      QDesignerFormWindowInterface *fw, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ManageWidgetCommandHelper4initEPK28QDesignerFormWindowInterfaceP7QWidget(
    qdesigner_internal::ManageWidgetCommandHelper *self,
    const QDesignerFormWindowInterface *fw,
    QWidget *widget) {
  self->init(fw, widget);
}

//  void qdesigner_internal::ManageWidgetCommandHelper::init(QWidget *widget,
//      const QWidgetList &managedChildren)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ManageWidgetCommandHelper4initEP7QWidgetRK5QListIS2_E(
    qdesigner_internal::ManageWidgetCommandHelper *self,
    QWidget *widget,
    const QList<QWidget *> *managedChildren) {
  self->init(widget, *managedChildren);
}

//  void qdesigner_internal::ManageWidgetCommandHelper::manage(QDesignerFormW
//      indowInterface *fw)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ManageWidgetCommandHelper6manageEP28QDesignerFormWindowInterface(
    qdesigner_internal::ManageWidgetCommandHelper *self,
    QDesignerFormWindowInterface *fw) {
  self->manage(fw);
}

//  void qdesigner_internal::ManageWidgetCommandHelper::unmanage(QDesignerFor
//      mWindowInterface *fw)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal25ManageWidgetCommandHelper8unmanageEP28QDesignerFormWindowInterface(
    qdesigner_internal::ManageWidgetCommandHelper *self,
    QDesignerFormWindowInterface *fw) {
  self->unmanage(fw);
}

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
