//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qsimpleresource_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qsimpleresource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::FormBuilderClipboard::FormBuilderClipboard()
extern "C" Q_DECL_EXPORT
qdesigner_internal::FormBuilderClipboard *ritual_ZN18qdesigner_internal20FormBuilderClipboardC1Ev() {
  return new qdesigner_internal::FormBuilderClipboard();
}

//  qdesigner_internal::FormBuilderClipboard::FormBuilderClipboard(QWidget
//      *w)
extern "C" Q_DECL_EXPORT
qdesigner_internal::FormBuilderClipboard *ritual_ZN18qdesigner_internal20FormBuilderClipboardC1EP7QWidget(
    QWidget *w) {
  return new qdesigner_internal::FormBuilderClipboard(w);
}

//  bool qdesigner_internal::FormBuilderClipboard::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal20FormBuilderClipboard5emptyEv(
    const qdesigner_internal::FormBuilderClipboard *self) {
  return self->empty();
}

//  qdesigner_internal::FormBuilderClipboard::~FormBuilderClipboard()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20FormBuilderClipboardD1Ev(
    qdesigner_internal::FormBuilderClipboard *self) {
  delete self;
}
