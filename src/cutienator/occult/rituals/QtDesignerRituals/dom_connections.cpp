//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  DomConnections::DomConnections()
extern "C" Q_DECL_EXPORT
DomConnections *ritual_ZN14DomConnectionsC1Ev() {
  return new DomConnections();
}

//  DomConnections::~DomConnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomConnectionsD1Ev(DomConnections *self) {
  delete self;
}

//  QList<DomConnection *> DomConnections::elementConnection() const
extern "C" Q_DECL_EXPORT
QList<DomConnection *> *ritual_ZNK14DomConnections17elementConnectionEv(
    const DomConnections *self) {
  return new QList<DomConnection *>(self->elementConnection());
}

//  void DomConnections::setElementConnection(const QList<DomConnection *>
//      &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14DomConnections20setElementConnectionERK5QListIP13DomConnectionE(
    DomConnections *self,
    const QList<DomConnection *> *a) {
  self->setElementConnection(*a);
}
