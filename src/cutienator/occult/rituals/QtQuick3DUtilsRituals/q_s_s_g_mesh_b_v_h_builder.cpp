//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvhbuilder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvhbuilder_p.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvh_p.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGMeshBVHBuilder::QSSGMeshBVHBuilder(const QSSGMesh::Mesh &mesh)
extern "C" Q_DECL_EXPORT
QSSGMeshBVHBuilder *ritual_ZN18QSSGMeshBVHBuilderC1ERKN8QSSGMesh4MeshE(
    const QSSGMesh::Mesh *mesh) {
  return new QSSGMeshBVHBuilder(*mesh);
}

//  QSSGMeshBVHBuilder::QSSGMeshBVHBuilder(const QByteArray &vertexBuffer,
//      int stride, int posOffset, bool hasUV, int uvOffset, bool
//      hasIndexBuffer, const QByteArray &indexBuffer,
//      QSSGRenderComponentType indexBufferType)
extern "C" Q_DECL_EXPORT
QSSGMeshBVHBuilder *ritual_ZN18QSSGMeshBVHBuilderC1ERK10QByteArrayiibibS2_23QSSGRenderComponentType(
    const QByteArray *vertexBuffer,
    int stride,
    int posOffset,
    bool hasUV,
    int uvOffset,
    bool hasIndexBuffer,
    const QByteArray *indexBuffer,
    QSSGRenderComponentType indexBufferType) {
  return new QSSGMeshBVHBuilder(
      *vertexBuffer,
      stride,
      posOffset,
      hasUV,
      uvOffset,
      hasIndexBuffer,
      *indexBuffer,
      indexBufferType);
}

//  QSSGBounds3 QSSGMeshBVHBuilder::getBounds(const QSSGMeshBVH &bvh, quint32
//      offset, quint32 count)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN18QSSGMeshBVHBuilder9getBoundsERK11QSSGMeshBVHjj(
    const QSSGMeshBVH *bvh,
    quint32 offset,
    quint32 count) {
  return new QSSGBounds3(QSSGMeshBVHBuilder::getBounds(*bvh, offset, count));
}

//  Axis QSSGMeshBVHBuilder::getLongestDimension(const QSSGBounds3
//      &nodeBounds)
extern "C" Q_DECL_EXPORT
QSSGMeshBVHBuilder::Axis ritual_ZN18QSSGMeshBVHBuilder19getLongestDimensionERK11QSSGBounds3(
    const QSSGBounds3 *nodeBounds) {
  return QSSGMeshBVHBuilder::getLongestDimension(*nodeBounds);
}

//  float QSSGMeshBVHBuilder::getAverageValue(const QSSGMeshBVH &bvh, quint32
//      offset, quint32 count, Axis axis)
extern "C" Q_DECL_EXPORT
float ritual_ZN18QSSGMeshBVHBuilder15getAverageValueERK11QSSGMeshBVHjjNS_4AxisE(
    const QSSGMeshBVH *bvh,
    quint32 offset,
    quint32 count,
    QSSGMeshBVHBuilder::Axis axis) {
  return QSSGMeshBVHBuilder::getAverageValue(*bvh, offset, count, axis);
}

//  QSSGMeshBVHBuilder::~QSSGMeshBVHBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGMeshBVHBuilderD1Ev(QSSGMeshBVHBuilder *self) {
  delete self;
}
