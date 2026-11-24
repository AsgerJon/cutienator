//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Mesh::Subset QSSGMesh::MeshInternal::Subset::toMeshSubset() const
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh::Subset *ritual_ZNK8QSSGMesh12MeshInternal6Subset12toMeshSubsetEv(
    const QSSGMesh::MeshInternal::Subset *self) {
  return new QSSGMesh::Mesh::Subset(self->toMeshSubset());
}

//  QSSGMesh::MeshInternal::Subset::~Subset()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh12MeshInternal6SubsetD1Ev(
    QSSGMesh::MeshInternal::Subset *self) {
  delete self;
}
