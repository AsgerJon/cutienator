//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qdestructionidandtypecollector_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qdestructionidandtypecollector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/private/qdestructionidandtypecollector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/core/nodes/qdestructionidandtypecollector.cpp, line 10, as _ZN8Qt3DCore30QDestructionIdAndTypeCollectorC1EPNS_5QNodeE
namespace Qt3DCore {
inline QDestructionIdAndTypeCollector::QDestructionIdAndTypeCollector(QNode *rootNode)
{
    QNodeVisitor visitor;
    visitor.traverse(rootNode, this, &QDestructionIdAndTypeCollector::collectIdAndType);
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  Qt3DCore::QDestructionIdAndTypeCollector::QDestructionIdAndTypeCollector(
//      QNode *rootNode)
extern "C" Q_DECL_EXPORT
Qt3DCore::QDestructionIdAndTypeCollector *ritual_ZN8Qt3DCore30QDestructionIdAndTypeCollectorC1EPNS_5QNodeE(
    Qt3DCore::QNode *rootNode) {
  return new Qt3DCore::QDestructionIdAndTypeCollector(rootNode);
}

//  QList<QNodeIdTypePair>
//      Qt3DCore::QDestructionIdAndTypeCollector::subtreeIdsAndTypes() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeIdTypePair> *ritual_ZNK8Qt3DCore30QDestructionIdAndTypeCollector18subtreeIdsAndTypesEv(
    const Qt3DCore::QDestructionIdAndTypeCollector *self) {
  return new QList<Qt3DCore::QNodeIdTypePair>(self->subtreeIdsAndTypes());
}

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

//  a QList<Qt3DCore::QNodeIdTypePair> a ritual of
//      Qt3DCore::QDestructionIdAndTypeCollector gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QDestructionIdAndTypeCollector__QList_Qt3DCore_QNodeIdTypePair(
    QList<Qt3DCore::QNodeIdTypePair> *self) {
  delete self;
}
