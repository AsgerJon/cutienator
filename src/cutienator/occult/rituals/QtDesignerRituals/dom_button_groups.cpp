//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  DomButtonGroups::DomButtonGroups()
extern "C" Q_DECL_EXPORT
DomButtonGroups *ritual_ZN15DomButtonGroupsC1Ev() {
  return new DomButtonGroups();
}

//  DomButtonGroups::~DomButtonGroups()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomButtonGroupsD1Ev(DomButtonGroups *self) {
  delete self;
}

//  QList<DomButtonGroup *> DomButtonGroups::elementButtonGroup() const
extern "C" Q_DECL_EXPORT
QList<DomButtonGroup *> *ritual_ZNK15DomButtonGroups18elementButtonGroupEv(
    const DomButtonGroups *self) {
  return new QList<DomButtonGroup *>(self->elementButtonGroup());
}

//  void DomButtonGroups::setElementButtonGroup(const QList<DomButtonGroup *>
//      &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomButtonGroups21setElementButtonGroupERK5QListIP14DomButtonGroupE(
    DomButtonGroups *self,
    const QList<DomButtonGroup *> *a) {
  self->setElementButtonGroup(*a);
}
