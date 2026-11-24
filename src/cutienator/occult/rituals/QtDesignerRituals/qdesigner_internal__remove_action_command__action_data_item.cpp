//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::RemoveActionCommand::ActionDataItem::ActionDataItem(Q
//      Action *_before, QWidget *_widget)
extern "C" Q_DECL_EXPORT
qdesigner_internal::RemoveActionCommand::ActionDataItem *ritual_ZN18qdesigner_internal19RemoveActionCommand14ActionDataItemC1EP7QActionP7QWidget(
    QAction *_before,
    QWidget *_widget) {
  return new qdesigner_internal::RemoveActionCommand::ActionDataItem(
      _before,
      _widget);
}

//  qdesigner_internal::RemoveActionCommand::ActionDataItem::~ActionDataItem(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19RemoveActionCommand14ActionDataItemD1Ev(
    qdesigner_internal::RemoveActionCommand::ActionDataItem *self) {
  delete self;
}
