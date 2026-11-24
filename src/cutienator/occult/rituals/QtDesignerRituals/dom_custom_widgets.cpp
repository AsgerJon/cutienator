//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  DomCustomWidgets::DomCustomWidgets()
extern "C" Q_DECL_EXPORT
DomCustomWidgets *ritual_ZN16DomCustomWidgetsC1Ev() {
  return new DomCustomWidgets();
}

//  DomCustomWidgets::~DomCustomWidgets()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DomCustomWidgetsD1Ev(DomCustomWidgets *self) {
  delete self;
}

//  QList<DomCustomWidget *> DomCustomWidgets::elementCustomWidget() const
extern "C" Q_DECL_EXPORT
QList<DomCustomWidget *> *ritual_ZNK16DomCustomWidgets19elementCustomWidgetEv(
    const DomCustomWidgets *self) {
  return new QList<DomCustomWidget *>(self->elementCustomWidget());
}

//  void DomCustomWidgets::setElementCustomWidget(const QList<DomCustomWidget
//      *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DomCustomWidgets22setElementCustomWidgetERK5QListIP15DomCustomWidgetE(
    DomCustomWidgets *self,
    const QList<DomCustomWidget *> *a) {
  self->setElementCustomWidget(*a);
}
