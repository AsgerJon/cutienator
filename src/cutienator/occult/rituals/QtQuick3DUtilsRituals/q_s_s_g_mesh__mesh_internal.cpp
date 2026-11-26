//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  MultiMeshInfo QSSGMesh::MeshInternal::readFileHeader(QIODevice *device)
extern "C" Q_DECL_EXPORT
QSSGMesh::MeshInternal::MultiMeshInfo *ritual_ZN8QSSGMesh12MeshInternal14readFileHeaderEP9QIODevice(
    QIODevice *device) {
  return new QSSGMesh::MeshInternal::MultiMeshInfo(
      QSSGMesh::MeshInternal::readFileHeader(
          device));
}

//  void QSSGMesh::MeshInternal::writeFileHeader(QIODevice *device, const
//      MultiMeshInfo &meshFileInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh12MeshInternal15writeFileHeaderEP9QIODeviceRKNS0_13MultiMeshInfoE(
    QIODevice *device,
    const QSSGMesh::MeshInternal::MultiMeshInfo *meshFileInfo) {
  QSSGMesh::MeshInternal::writeFileHeader(device, *meshFileInfo);
}

//  quint64 QSSGMesh::MeshInternal::readMeshData(QIODevice *device, quint64
//      offset, Mesh *mesh, MeshDataHeader *header)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN8QSSGMesh12MeshInternal12readMeshDataEP9QIODeviceyPNS_4MeshEPNS0_14MeshDataHeaderE(
    QIODevice *device,
    quint64 offset,
    QSSGMesh::Mesh *mesh,
    QSSGMesh::MeshInternal::MeshDataHeader *header) {
  return QSSGMesh::MeshInternal::readMeshData(device, offset, mesh, header);
}

//  void QSSGMesh::MeshInternal::writeMeshHeader(QIODevice *device, const
//      MeshDataHeader &header)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh12MeshInternal15writeMeshHeaderEP9QIODeviceRKNS0_14MeshDataHeaderE(
    QIODevice *device,
    const QSSGMesh::MeshInternal::MeshDataHeader *header) {
  QSSGMesh::MeshInternal::writeMeshHeader(device, *header);
}

//  quint64 QSSGMesh::MeshInternal::writeMeshData(QIODevice *device, const
//      Mesh &mesh)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN8QSSGMesh12MeshInternal13writeMeshDataEP9QIODeviceRKNS_4MeshE(
    QIODevice *device,
    const QSSGMesh::Mesh *mesh) {
  return QSSGMesh::MeshInternal::writeMeshData(device, *mesh);
}

//  quint32
//      QSSGMesh::MeshInternal::byteSizeForComponentType(Mesh::ComponentType
//      componentType)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN8QSSGMesh12MeshInternal24byteSizeForComponentTypeE23QSSGRenderComponentType(
    QSSGMesh::Mesh::ComponentType componentType) {
  return QSSGMesh::MeshInternal::byteSizeForComponentType(componentType);
}

//  const char *QSSGMesh::MeshInternal::getPositionAttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal19getPositionAttrNameEv() {
  return QSSGMesh::MeshInternal::getPositionAttrName();
}

//  const char *QSSGMesh::MeshInternal::getNormalAttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal17getNormalAttrNameEv() {
  return QSSGMesh::MeshInternal::getNormalAttrName();
}

//  const char *QSSGMesh::MeshInternal::getUV0AttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal14getUV0AttrNameEv() {
  return QSSGMesh::MeshInternal::getUV0AttrName();
}

//  const char *QSSGMesh::MeshInternal::getUV1AttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal14getUV1AttrNameEv() {
  return QSSGMesh::MeshInternal::getUV1AttrName();
}

//  const char *QSSGMesh::MeshInternal::getLightmapUVAttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal21getLightmapUVAttrNameEv() {
  return QSSGMesh::MeshInternal::getLightmapUVAttrName();
}

//  const char *QSSGMesh::MeshInternal::getTexTanAttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal17getTexTanAttrNameEv() {
  return QSSGMesh::MeshInternal::getTexTanAttrName();
}

//  const char *QSSGMesh::MeshInternal::getTexBinormalAttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal22getTexBinormalAttrNameEv() {
  return QSSGMesh::MeshInternal::getTexBinormalAttrName();
}

//  const char *QSSGMesh::MeshInternal::getColorAttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal16getColorAttrNameEv() {
  return QSSGMesh::MeshInternal::getColorAttrName();
}

//  const char *QSSGMesh::MeshInternal::getJointAttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal16getJointAttrNameEv() {
  return QSSGMesh::MeshInternal::getJointAttrName();
}

//  const char *QSSGMesh::MeshInternal::getWeightAttrName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN8QSSGMesh12MeshInternal17getWeightAttrNameEv() {
  return QSSGMesh::MeshInternal::getWeightAttrName();
}

//  QSSGBounds3 QSSGMesh::MeshInternal::calculateSubsetBounds(const
//      Mesh::VertexBufferEntry &entry, const QByteArray &vertexBufferData,
//      quint32 vertexBufferStride, const QByteArray &indexBufferData,
//      Mesh::ComponentType indexComponentType, quint32 subsetCount, quint32
//      subsetOffset)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN8QSSGMesh12MeshInternal21calculateSubsetBoundsERKNS_4Mesh17VertexBufferEntryERK10QByteArrayjS7_23QSSGRenderComponentTypejj(
    const QSSGMesh::Mesh::VertexBufferEntry *entry,
    const QByteArray *vertexBufferData,
    quint32 vertexBufferStride,
    const QByteArray *indexBufferData,
    QSSGMesh::Mesh::ComponentType indexComponentType,
    quint32 subsetCount,
    quint32 subsetOffset) {
  return new QSSGBounds3(
      QSSGMesh::MeshInternal::calculateSubsetBounds(
          *entry,
          *vertexBufferData,
          vertexBufferStride,
          *indexBufferData,
          indexComponentType,
          subsetCount,
          subsetOffset));
}

//  QSSGMesh::MeshInternal::~MeshInternal()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh12MeshInternalD1Ev(QSSGMesh::MeshInternal *self) {
  delete self;
}
