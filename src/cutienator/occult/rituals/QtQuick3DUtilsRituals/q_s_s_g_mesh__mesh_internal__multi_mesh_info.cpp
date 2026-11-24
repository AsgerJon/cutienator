//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSSGMesh::MeshInternal::MultiMeshInfo::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSSGMesh12MeshInternal13MultiMeshInfo7isValidEv(
    const QSSGMesh::MeshInternal::MultiMeshInfo *self) {
  return self->isValid();
}

//  MultiMeshInfo QSSGMesh::MeshInternal::MultiMeshInfo::withDefaults()
extern "C" Q_DECL_EXPORT
QSSGMesh::MeshInternal::MultiMeshInfo *ritual_ZN8QSSGMesh12MeshInternal13MultiMeshInfo12withDefaultsEv() {
  return new QSSGMesh::MeshInternal::MultiMeshInfo(
      QSSGMesh::MeshInternal::MultiMeshInfo::withDefaults());
}

//  QSSGMesh::MeshInternal::MultiMeshInfo::~MultiMeshInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh12MeshInternal13MultiMeshInfoD1Ev(
    QSSGMesh::MeshInternal::MultiMeshInfo *self) {
  delete self;
}
