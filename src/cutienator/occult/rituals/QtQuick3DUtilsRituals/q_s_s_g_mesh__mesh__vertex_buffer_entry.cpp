//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderVertexBufferEntry
//      QSSGMesh::Mesh::VertexBufferEntry::toRenderVertexBufferEntry() const
extern "C" Q_DECL_EXPORT
QSSGRenderVertexBufferEntry *ritual_ZNK8QSSGMesh4Mesh17VertexBufferEntry25toRenderVertexBufferEntryEv(
    const QSSGMesh::Mesh::VertexBufferEntry *self) {
  return new QSSGRenderVertexBufferEntry(self->toRenderVertexBufferEntry());
}

//  QSSGMesh::Mesh::VertexBufferEntry::~VertexBufferEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh4Mesh17VertexBufferEntryD1Ev(
    QSSGMesh::Mesh::VertexBufferEntry *self) {
  delete self;
}
