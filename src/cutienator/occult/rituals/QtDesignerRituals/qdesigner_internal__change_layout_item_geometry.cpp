//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  qdesigner_internal::ChangeLayoutItemGeometry::ChangeLayoutItemGeometry(QD
//      esignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ChangeLayoutItemGeometry *ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometryC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::ChangeLayoutItemGeometry(formWindow);
}

//  void qdesigner_internal::ChangeLayoutItemGeometry::init(QWidget *widget,
//      int row, int column, int rowspan, int colspan)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometry4initEP7QWidgetiiii(
    qdesigner_internal::ChangeLayoutItemGeometry *self,
    QWidget *widget,
    int row,
    int column,
    int rowspan,
    int colspan) {
  self->init(widget, row, column, rowspan, colspan);
}

//  void qdesigner_internal::ChangeLayoutItemGeometry::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometry4redoEv(
    qdesigner_internal::ChangeLayoutItemGeometry *self) {
  self->redo();
}

//  void qdesigner_internal::ChangeLayoutItemGeometry::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometry4undoEv(
    qdesigner_internal::ChangeLayoutItemGeometry *self) {
  self->undo();
}

//  void
//      qdesigner_internal::ChangeLayoutItemGeometry::changeItemPosition(cons
//      t QRect &g)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometry18changeItemPositionERK5QRect(
    qdesigner_internal::ChangeLayoutItemGeometry *self,
    const QRect *g) {
  self->changeItemPosition(*g);
}

//  void qdesigner_internal::ChangeLayoutItemGeometry::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal24ChangeLayoutItemGeometry4redoEv(
    qdesigner_internal::ChangeLayoutItemGeometry *self) {
  self->qdesigner_internal::ChangeLayoutItemGeometry::redo();
}

//  void qdesigner_internal::ChangeLayoutItemGeometry::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal24ChangeLayoutItemGeometry4undoEv(
    qdesigner_internal::ChangeLayoutItemGeometry *self) {
  self->qdesigner_internal::ChangeLayoutItemGeometry::undo();
}
