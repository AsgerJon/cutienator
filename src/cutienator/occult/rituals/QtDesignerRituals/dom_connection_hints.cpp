//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  DomConnectionHints::DomConnectionHints()
extern "C" Q_DECL_EXPORT
DomConnectionHints *ritual_ZN18DomConnectionHintsC1Ev() {
  return new DomConnectionHints();
}

//  DomConnectionHints::~DomConnectionHints()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DomConnectionHintsD1Ev(DomConnectionHints *self) {
  delete self;
}

//  QList<DomConnectionHint *> DomConnectionHints::elementHint() const
extern "C" Q_DECL_EXPORT
QList<DomConnectionHint *> *ritual_ZNK18DomConnectionHints11elementHintEv(
    const DomConnectionHints *self) {
  return new QList<DomConnectionHint *>(self->elementHint());
}

//  void DomConnectionHints::setElementHint(const QList<DomConnectionHint *>
//      &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DomConnectionHints14setElementHintERK5QListIP17DomConnectionHintE(
    DomConnectionHints *self,
    const QList<DomConnectionHint *> *a) {
  self->setElementHint(*a);
}
