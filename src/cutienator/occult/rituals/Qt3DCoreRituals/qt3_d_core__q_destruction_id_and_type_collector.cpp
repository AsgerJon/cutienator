//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qdestructionidandtypecollector_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qdestructionidandtypecollector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DCore::QDestructionIdAndTypeCollector::collectIdAndType(QNode
//      *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore30QDestructionIdAndTypeCollector16collectIdAndTypeEPNS_5QNodeE(
    Qt3DCore::QDestructionIdAndTypeCollector *self,
    Qt3DCore::QNode *node) {
  self->collectIdAndType(node);
}

//  Qt3DCore::QDestructionIdAndTypeCollector::~QDestructionIdAndTypeCollector
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore30QDestructionIdAndTypeCollectorD1Ev(
    Qt3DCore::QDestructionIdAndTypeCollector *self) {
  delete self;
}
