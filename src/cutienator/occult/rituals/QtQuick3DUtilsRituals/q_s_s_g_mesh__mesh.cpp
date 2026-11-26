//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/QVector>
#include <QtCore/QMap>

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

//  QVector<Subset> QSSGMesh::Mesh::subsets() const
extern "C" Q_DECL_EXPORT
QVector<QSSGMesh::Mesh::Subset> *ritual_ZNK8QSSGMesh4Mesh7subsetsEv(
    const QSSGMesh::Mesh *self) {
  return new QVector<QSSGMesh::Mesh::Subset>(self->subsets());
}

//  Mesh QSSGMesh::Mesh::loadMesh(QIODevice *device, quint32 id)
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh *ritual_ZN8QSSGMesh4Mesh8loadMeshEP9QIODevicej(
    QIODevice *device,
    quint32 id) {
  return new QSSGMesh::Mesh(QSSGMesh::Mesh::loadMesh(device, id));
}

//  QMap<quint32, Mesh> QSSGMesh::Mesh::loadAll(QIODevice *device)
extern "C" Q_DECL_EXPORT
QMap<quint32, QSSGMesh::Mesh> *ritual_ZN8QSSGMesh4Mesh7loadAllEP9QIODevice(
    QIODevice *device) {
  return new QMap<quint32, QSSGMesh::Mesh>(QSSGMesh::Mesh::loadAll(device));
}

//  Mesh QSSGMesh::Mesh::fromAssetData(const QVector<AssetVertexEntry>
//      &vbufEntries, const QByteArray &indexBufferData, ComponentType
//      indexComponentType, const QVector<AssetMeshSubset> &subsets, quint32
//      numTargets, quint32 numTargetComps)
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh *ritual_ZN8QSSGMesh4Mesh13fromAssetDataERK5QListINS_16AssetVertexEntryEERK10QByteArray23QSSGRenderComponentTypeRKS1_INS_15AssetMeshSubsetEEjj(
    const QVector<QSSGMesh::AssetVertexEntry> *vbufEntries,
    const QByteArray *indexBufferData,
    QSSGMesh::Mesh::ComponentType indexComponentType,
    const QVector<QSSGMesh::AssetMeshSubset> *subsets,
    quint32 numTargets,
    quint32 numTargetComps) {
  return new QSSGMesh::Mesh(
      QSSGMesh::Mesh::fromAssetData(
          *vbufEntries,
          *indexBufferData,
          indexComponentType,
          *subsets,
          numTargets,
          numTargetComps));
}

//  Mesh QSSGMesh::Mesh::fromRuntimeData(const RuntimeMeshData &data, QString
//      *error)
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh *ritual_ZN8QSSGMesh4Mesh15fromRuntimeDataERKNS_15RuntimeMeshDataEP7QString(
    const QSSGMesh::RuntimeMeshData *data,
    QString *error) {
  return new QSSGMesh::Mesh(QSSGMesh::Mesh::fromRuntimeData(*data, error));
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

//  quint32 QSSGMesh::Mesh::save(QIODevice *device, quint32 id) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK8QSSGMesh4Mesh4saveEP9QIODevicej(
    const QSSGMesh::Mesh *self,
    QIODevice *device,
    quint32 id) {
  return self->save(device, id);
}

//  bool QSSGMesh::Mesh::hasLightmapUVChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSSGMesh4Mesh20hasLightmapUVChannelEv(
    const QSSGMesh::Mesh *self) {
  return self->hasLightmapUVChannel();
}

//  bool QSSGMesh::Mesh::createLightmapUVChannel(float texelsPerUnit, const
//      QMatrix4x4 &scale)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QSSGMesh4Mesh23createLightmapUVChannelEfRK10QMatrix4x4(
    QSSGMesh::Mesh *self,
    float texelsPerUnit,
    const QMatrix4x4 *scale) {
  return self->createLightmapUVChannel(texelsPerUnit, *scale);
}

//  QSSGMesh::Mesh::~Mesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh4MeshD1Ev(QSSGMesh::Mesh *self) {
  delete self;
}

//  a QVector<QSSGMesh::Mesh::Subset> a ritual of QSSGMesh::Mesh gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGMesh_Mesh__QVector_QSSGMesh_Mesh_Subset(
    QVector<QSSGMesh::Mesh::Subset> *self) {
  delete self;
}

//  a QMap<quint32, QSSGMesh::Mesh> a ritual of QSSGMesh::Mesh gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGMesh_Mesh__QMap_quint32_QSSGMesh_Mesh(
    QMap<quint32, QSSGMesh::Mesh> *self) {
  delete self;
}
