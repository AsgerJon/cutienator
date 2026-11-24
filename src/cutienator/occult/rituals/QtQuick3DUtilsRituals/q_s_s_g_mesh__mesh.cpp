//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  VertexBuffer QSSGMesh::Mesh::vertexBuffer() const
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh::VertexBuffer *ritual_ZNK8QSSGMesh4Mesh12vertexBufferEv(
    const QSSGMesh::Mesh *self) {
  return new QSSGMesh::Mesh::VertexBuffer(self->vertexBuffer());
}

//  IndexBuffer QSSGMesh::Mesh::indexBuffer() const
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh::IndexBuffer *ritual_ZNK8QSSGMesh4Mesh11indexBufferEv(
    const QSSGMesh::Mesh *self) {
  return new QSSGMesh::Mesh::IndexBuffer(self->indexBuffer());
}

//  TargetBuffer QSSGMesh::Mesh::targetBuffer() const
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh::TargetBuffer *ritual_ZNK8QSSGMesh4Mesh12targetBufferEv(
    const QSSGMesh::Mesh *self) {
  return new QSSGMesh::Mesh::TargetBuffer(self->targetBuffer());
}

//  bool QSSGMesh::Mesh::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSSGMesh4Mesh7isValidEv(const QSSGMesh::Mesh *self) {
  return self->isValid();
}

//  DrawMode QSSGMesh::Mesh::drawMode() const
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh::DrawMode ritual_ZNK8QSSGMesh4Mesh8drawModeEv(
    const QSSGMesh::Mesh *self) {
  return self->drawMode();
}

//  Winding QSSGMesh::Mesh::winding() const
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh::Winding ritual_ZNK8QSSGMesh4Mesh7windingEv(
    const QSSGMesh::Mesh *self) {
  return self->winding();
}

//  QSSGMesh::Mesh::~Mesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh4MeshD1Ev(QSSGMesh::Mesh *self) {
  delete self;
}
