//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::UpdateBlocker::UpdateBlocker(QWidget *w)
extern "C" Q_DECL_EXPORT
qdesigner_internal::UpdateBlocker *ritual_ZN18qdesigner_internal13UpdateBlockerC1EP7QWidget(
    QWidget *w) {
  return new qdesigner_internal::UpdateBlocker(w);
}

//  qdesigner_internal::UpdateBlocker::~UpdateBlocker()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13UpdateBlockerD1Ev(
    qdesigner_internal::UpdateBlocker *self) {
  delete self;
}
