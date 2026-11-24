//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  MeshDataHeader QSSGMesh::MeshInternal::MeshDataHeader::withDefaults()
extern "C" Q_DECL_EXPORT
QSSGMesh::MeshInternal::MeshDataHeader *ritual_ZN8QSSGMesh12MeshInternal14MeshDataHeader12withDefaultsEv() {
  return new QSSGMesh::MeshInternal::MeshDataHeader(
      QSSGMesh::MeshInternal::MeshDataHeader::withDefaults());
}

//  bool QSSGMesh::MeshInternal::MeshDataHeader::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSSGMesh12MeshInternal14MeshDataHeader7isValidEv(
    const QSSGMesh::MeshInternal::MeshDataHeader *self) {
  return self->isValid();
}

//  bool QSSGMesh::MeshInternal::MeshDataHeader::hasLightmapSizeHint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSSGMesh12MeshInternal14MeshDataHeader19hasLightmapSizeHintEv(
    const QSSGMesh::MeshInternal::MeshDataHeader *self) {
  return self->hasLightmapSizeHint();
}

//  bool QSSGMesh::MeshInternal::MeshDataHeader::hasLodDataHint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSSGMesh12MeshInternal14MeshDataHeader14hasLodDataHintEv(
    const QSSGMesh::MeshInternal::MeshDataHeader *self) {
  return self->hasLodDataHint();
}

//  bool QSSGMesh::MeshInternal::MeshDataHeader::hasSeparateTargetBuffer()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSSGMesh12MeshInternal14MeshDataHeader23hasSeparateTargetBufferEv(
    const QSSGMesh::MeshInternal::MeshDataHeader *self) {
  return self->hasSeparateTargetBuffer();
}

//  QSSGMesh::MeshInternal::MeshDataHeader::~MeshDataHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh12MeshInternal14MeshDataHeaderD1Ev(
    QSSGMesh::MeshInternal::MeshDataHeader *self) {
  delete self;
}
