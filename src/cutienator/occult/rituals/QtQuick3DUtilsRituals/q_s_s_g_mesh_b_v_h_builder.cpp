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
#include <memory>

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

//  std::unique_ptr<QSSGMeshBVH> QSSGMeshBVHBuilder::buildTree()
extern "C" Q_DECL_EXPORT
std::unique_ptr<QSSGMeshBVH> *ritual_ZN18QSSGMeshBVHBuilder9buildTreeEv(
    QSSGMeshBVHBuilder *self) {
  return new std::unique_ptr<QSSGMeshBVH>(self->buildTree());
}

//  QSSGMeshBVHTriangles QSSGMeshBVHBuilder::calculateTriangleBounds(quint32
//      indexOffset, quint32 indexCount) const
extern "C" Q_DECL_EXPORT
QSSGMeshBVHTriangles *ritual_ZNK18QSSGMeshBVHBuilder23calculateTriangleBoundsEjj(
    const QSSGMeshBVHBuilder *self,
    quint32 indexOffset,
    quint32 indexCount) {
  return new QSSGMeshBVHTriangles(
      self->calculateTriangleBounds(
          indexOffset,
          indexCount));
}

//  QSSGMeshBVHNode::Handle QSSGMeshBVHBuilder::splitNode(QSSGMeshBVH &bvh,
//      QSSGMeshBVHNode::Handle node, quint32 offset, quint32 count, quint32
//      depth)
extern "C" Q_DECL_EXPORT
QSSGMeshBVHNode::Handle *ritual_ZN18QSSGMeshBVHBuilder9splitNodeER11QSSGMeshBVHN15QSSGMeshBVHNode6HandleEjjj(
    QSSGMeshBVH *bvh,
    const QSSGMeshBVHNode::Handle *node,
    quint32 offset,
    quint32 count,
    quint32 depth) {
  return new QSSGMeshBVHNode::Handle(
      QSSGMeshBVHBuilder::splitNode(
          *bvh,
          *node,
          offset,
          count,
          depth));
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

//  Split QSSGMeshBVHBuilder::getOptimalSplit(const QSSGMeshBVH &bvh, const
//      QSSGBounds3 &nodeBounds, quint32 offset, quint32 count)
extern "C" Q_DECL_EXPORT
QSSGMeshBVHBuilder::Split *ritual_ZN18QSSGMeshBVHBuilder15getOptimalSplitERK11QSSGMeshBVHRK11QSSGBounds3jj(
    const QSSGMeshBVH *bvh,
    const QSSGBounds3 *nodeBounds,
    quint32 offset,
    quint32 count) {
  return new QSSGMeshBVHBuilder::Split(
      QSSGMeshBVHBuilder::getOptimalSplit(
          *bvh,
          *nodeBounds,
          offset,
          count));
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

//  quint32 QSSGMeshBVHBuilder::partition(QSSGMeshBVH &bvh, quint32 offset,
//      quint32 count, const Split &split)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN18QSSGMeshBVHBuilder9partitionER11QSSGMeshBVHjjRKNS_5SplitE(
    QSSGMeshBVH *bvh,
    quint32 offset,
    quint32 count,
    const QSSGMeshBVHBuilder::Split *split) {
  return QSSGMeshBVHBuilder::partition(*bvh, offset, count, *split);
}

//  QSSGMeshBVHBuilder::~QSSGMeshBVHBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGMeshBVHBuilderD1Ev(QSSGMeshBVHBuilder *self) {
  delete self;
}

//  a std::unique_ptr<QSSGMeshBVH> a ritual of QSSGMeshBVHBuilder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGMeshBVHBuilder__std_unique_ptr_QSSGMeshBVH(
    std::unique_ptr<QSSGMeshBVH> *self) {
  delete self;
}

//  a QSSGMeshBVHTriangles a ritual of QSSGMeshBVHBuilder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGMeshBVHBuilder__QSSGMeshBVHTriangles(
    QSSGMeshBVHTriangles *self) {
  delete self;
}

//  a QSSGMeshBVHBuilder::Split a ritual of QSSGMeshBVHBuilder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGMeshBVHBuilder__QSSGMeshBVHBuilder_Split(
    QSSGMeshBVHBuilder::Split *self) {
  delete self;
}
