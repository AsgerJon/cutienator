//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  DomPropertySpecifications::DomPropertySpecifications()
extern "C" Q_DECL_EXPORT
DomPropertySpecifications *ritual_ZN25DomPropertySpecificationsC1Ev() {
  return new DomPropertySpecifications();
}

//  DomPropertySpecifications::~DomPropertySpecifications()
extern "C" Q_DECL_EXPORT
void ritual_ZN25DomPropertySpecificationsD1Ev(
    DomPropertySpecifications *self) {
  delete self;
}

//  QList<DomPropertyToolTip *> DomPropertySpecifications::elementTooltip()
//      const
extern "C" Q_DECL_EXPORT
QList<DomPropertyToolTip *> *ritual_ZNK25DomPropertySpecifications14elementTooltipEv(
    const DomPropertySpecifications *self) {
  return new QList<DomPropertyToolTip *>(self->elementTooltip());
}

//  void DomPropertySpecifications::setElementTooltip(const
//      QList<DomPropertyToolTip *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN25DomPropertySpecifications17setElementTooltipERK5QListIP18DomPropertyToolTipE(
    DomPropertySpecifications *self,
    const QList<DomPropertyToolTip *> *a) {
  self->setElementTooltip(*a);
}

//  QList<DomStringPropertySpecification *>
//      DomPropertySpecifications::elementStringpropertyspecification() const
extern "C" Q_DECL_EXPORT
QList<DomStringPropertySpecification *> *ritual_ZNK25DomPropertySpecifications34elementStringpropertyspecificationEv(
    const DomPropertySpecifications *self) {
  return new QList<DomStringPropertySpecification *>(
      self->elementStringpropertyspecification());
}

//  void
//      DomPropertySpecifications::setElementStringpropertyspecification(cons
//      t QList<DomStringPropertySpecification *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN25DomPropertySpecifications37setElementStringpropertyspecificationERK5QListIP30DomStringPropertySpecificationE(
    DomPropertySpecifications *self,
    const QList<DomStringPropertySpecification *> *a) {
  self->setElementStringpropertyspecification(*a);
}
