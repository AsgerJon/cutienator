//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendergeometry_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendergeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qstring.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderGeometry::QSSGRenderGeometry()
extern "C" Q_DECL_EXPORT
QSSGRenderGeometry *ritual_ZN18QSSGRenderGeometryC1Ev() {
  return new QSSGRenderGeometry();
}

//  QSSGRenderGeometry::~QSSGRenderGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometryD1Ev(QSSGRenderGeometry *self) {
  delete self;
}

//  const QByteArray &QSSGRenderGeometry::vertexBuffer() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QSSGRenderGeometry12vertexBufferEv(
    const QSSGRenderGeometry *self) {
  return new QByteArray(self->vertexBuffer());
}

//  const QByteArray &QSSGRenderGeometry::indexBuffer() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QSSGRenderGeometry11indexBufferEv(
    const QSSGRenderGeometry *self) {
  return new QByteArray(self->indexBuffer());
}

//  int QSSGRenderGeometry::attributeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSSGRenderGeometry14attributeCountEv(
    const QSSGRenderGeometry *self) {
  return self->attributeCount();
}

//  Attribute QSSGRenderGeometry::attribute(int idx) const
extern "C" Q_DECL_EXPORT
QSSGRenderGeometry::Attribute *ritual_ZNK18QSSGRenderGeometry9attributeEi(
    const QSSGRenderGeometry *self,
    int idx) {
  return new QSSGRenderGeometry::Attribute(self->attribute(idx));
}

//  QSSGMesh::Mesh::DrawMode QSSGRenderGeometry::primitiveType() const
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh::DrawMode ritual_ZNK18QSSGRenderGeometry13primitiveTypeEv(
    const QSSGRenderGeometry *self) {
  return self->primitiveType();
}

//  QVector3D QSSGRenderGeometry::boundsMin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QSSGRenderGeometry9boundsMinEv(
    const QSSGRenderGeometry *self) {
  return new QVector3D(self->boundsMin());
}

//  QVector3D QSSGRenderGeometry::boundsMax() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QSSGRenderGeometry9boundsMaxEv(
    const QSSGRenderGeometry *self) {
  return new QVector3D(self->boundsMax());
}

//  int QSSGRenderGeometry::stride() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSSGRenderGeometry6strideEv(const QSSGRenderGeometry *self) {
  return self->stride();
}

//  void QSSGRenderGeometry::setVertexData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry13setVertexDataERK10QByteArray(
    QSSGRenderGeometry *self,
    const QByteArray *data) {
  self->setVertexData(*data);
}

//  void QSSGRenderGeometry::setIndexData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry12setIndexDataERK10QByteArray(
    QSSGRenderGeometry *self,
    const QByteArray *data) {
  self->setIndexData(*data);
}

//  void QSSGRenderGeometry::setStride(int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry9setStrideEi(
    QSSGRenderGeometry *self,
    int stride) {
  self->setStride(stride);
}

//  void QSSGRenderGeometry::setBounds(const QVector3D &min, const QVector3D
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry9setBoundsERK9QVector3DS2_(
    QSSGRenderGeometry *self,
    const QVector3D *min,
    const QVector3D *max) {
  self->setBounds(*min, *max);
}

//  void QSSGRenderGeometry::setPrimitiveType(QSSGMesh::Mesh::DrawMode type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry16setPrimitiveTypeE18QSSGRenderDrawMode(
    QSSGRenderGeometry *self,
    QSSGMesh::Mesh::DrawMode type) {
  self->setPrimitiveType(type);
}

//  void QSSGRenderGeometry::addAttribute(QSSGMesh::RuntimeMeshData::Attribut
//      e::Semantic semantic, int offset, QSSGMesh::Mesh::ComponentType
//      componentType)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry12addAttributeEN8QSSGMesh15RuntimeMeshData9Attribute8SemanticEi23QSSGRenderComponentType(
    QSSGRenderGeometry *self,
    QSSGMesh::RuntimeMeshData::Attribute::Semantic semantic,
    int offset,
    QSSGMesh::Mesh::ComponentType componentType) {
  self->addAttribute(semantic, offset, componentType);
}

//  void QSSGRenderGeometry::addAttribute(const Attribute &att)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry12addAttributeERKNS_9AttributeE(
    QSSGRenderGeometry *self,
    const QSSGRenderGeometry::Attribute *att) {
  self->addAttribute(*att);
}

//  void QSSGRenderGeometry::addSubset(quint32 offset, quint32 count, const
//      QVector3D &boundsMin, const QVector3D &boundsMax, const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry9addSubsetEjjRK9QVector3DS2_RK7QString(
    QSSGRenderGeometry *self,
    quint32 offset,
    quint32 count,
    const QVector3D *boundsMin,
    const QVector3D *boundsMax,
    const QString *name) {
  self->addSubset(offset, count, *boundsMin, *boundsMax, *name);
}

//  void QSSGRenderGeometry::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry5clearEv(QSSGRenderGeometry *self) {
  self->clear();
}

//  void QSSGRenderGeometry::clearAttributes()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry15clearAttributesEv(
    QSSGRenderGeometry *self) {
  self->clearAttributes();
}

//  const QSSGMesh::RuntimeMeshData &QSSGRenderGeometry::meshData() const
extern "C" Q_DECL_EXPORT
QSSGMesh::RuntimeMeshData *ritual_ZNK18QSSGRenderGeometry8meshDataEv(
    const QSSGRenderGeometry *self) {
  return new QSSGMesh::RuntimeMeshData(self->meshData());
}

//  void QSSGRenderGeometry::clearVertexAndIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry19clearVertexAndIndexEv(
    QSSGRenderGeometry *self) {
  self->clearVertexAndIndex();
}

//  void QSSGRenderGeometry::clearTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry11clearTargetEv(QSSGRenderGeometry *self) {
  self->clearTarget();
}

//  void QSSGRenderGeometry::setTargetData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry13setTargetDataERK10QByteArray(
    QSSGRenderGeometry *self,
    const QByteArray *data) {
  self->setTargetData(*data);
}

//  void QSSGRenderGeometry::addTargetAttribute(quint32 targetId,
//      QSSGMesh::RuntimeMeshData::Attribute::Semantic semantic, int offset,
//      int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry18addTargetAttributeEjN8QSSGMesh15RuntimeMeshData9Attribute8SemanticEii(
    QSSGRenderGeometry *self,
    quint32 targetId,
    QSSGMesh::RuntimeMeshData::Attribute::Semantic semantic,
    int offset,
    int stride) {
  self->addTargetAttribute(targetId, semantic, offset, stride);
}

//  void QSSGRenderGeometry::addTargetAttribute(const TargetAttribute &att)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry18addTargetAttributeERKNS_15TargetAttributeE(
    QSSGRenderGeometry *self,
    const QSSGRenderGeometry::TargetAttribute *att) {
  self->addTargetAttribute(*att);
}

//  void QSSGRenderGeometry::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGRenderGeometry9markDirtyEv(QSSGRenderGeometry *self) {
  self->markDirty();
}
