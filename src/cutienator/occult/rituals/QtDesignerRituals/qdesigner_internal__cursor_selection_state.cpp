//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::CursorSelectionState::CursorSelectionState()
extern "C" Q_DECL_EXPORT
qdesigner_internal::CursorSelectionState *ritual_ZN18qdesigner_internal20CursorSelectionStateC1Ev() {
  return new qdesigner_internal::CursorSelectionState();
}

//  void qdesigner_internal::CursorSelectionState::save(const
//      QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20CursorSelectionState4saveEPK28QDesignerFormWindowInterface(
    qdesigner_internal::CursorSelectionState *self,
    const QDesignerFormWindowInterface *formWindow) {
  self->save(formWindow);
}

//  void qdesigner_internal::CursorSelectionState::restore(QDesignerFormWindo
//      wInterface *formWindow) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal20CursorSelectionState7restoreEP28QDesignerFormWindowInterface(
    const qdesigner_internal::CursorSelectionState *self,
    QDesignerFormWindowInterface *formWindow) {
  self->restore(formWindow);
}
