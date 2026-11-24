//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Heap::ReferenceObjectEndpoint::ReferenceObjectEndpoint(ReferenceObje
//      ct *reference)
extern "C" Q_DECL_EXPORT
QV4::Heap::ReferenceObjectEndpoint *ritual_ZN3QV44Heap23ReferenceObjectEndpointC1EPNS0_15ReferenceObjectE(
    QV4::Heap::ReferenceObject *reference) {
  return new QV4::Heap::ReferenceObjectEndpoint(reference);
}

//  QV4::Heap::ReferenceObjectEndpoint::~ReferenceObjectEndpoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap23ReferenceObjectEndpointD1Ev(
    QV4::Heap::ReferenceObjectEndpoint *self) {
  delete self;
}
