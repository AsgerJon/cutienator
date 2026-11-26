//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGMeshBVH::QSSGMeshBVH()
extern "C" Q_DECL_EXPORT
QSSGMeshBVH *ritual_ZN11QSSGMeshBVHC1Ev() {
  return new QSSGMeshBVH();
}

//  QSSGMeshBVH::~QSSGMeshBVH()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGMeshBVHD1Ev(QSSGMeshBVH *self) {
  delete self;
}

//  QSSGMeshBVHNode::Handle QSSGMeshBVH::newHandle()
extern "C" Q_DECL_EXPORT
QSSGMeshBVHNode::Handle *ritual_ZN11QSSGMeshBVH9newHandleEv(
    QSSGMeshBVH *self) {
  return new QSSGMeshBVHNode::Handle(self->newHandle());
}

//  const QSSGMeshBVHTriangles &QSSGMeshBVH::triangles() const
extern "C" Q_DECL_EXPORT
const QSSGMeshBVHTriangles *ritual_ZNK11QSSGMeshBVH9trianglesEv(
    const QSSGMeshBVH *self) {
  return &(self->triangles());
}

//  const QSSGMeshBVHRoots &QSSGMeshBVH::roots() const
extern "C" Q_DECL_EXPORT
const QSSGMeshBVHRoots *ritual_ZNK11QSSGMeshBVH5rootsEv(
    const QSSGMeshBVH *self) {
  return &(self->roots());
}

//  const QSSGMeshBVHNodes &QSSGMeshBVH::nodes() const
extern "C" Q_DECL_EXPORT
const QSSGMeshBVHNodes *ritual_ZNK11QSSGMeshBVH5nodesEv(
    const QSSGMeshBVH *self) {
  return &(self->nodes());
}

//  size_t QSSGMeshBVH::getNodeIndex(size_t idx, FallbackIndex op) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK11QSSGMeshBVH12getNodeIndexEmN15QSSGMeshBVHNode13FallbackIndexE(
    const QSSGMeshBVH *self,
    size_t idx,
    QSSGMeshBVH::FallbackIndex op) {
  return self->getNodeIndex(idx, op);
}

//  QSSGMeshBVHNode &QSSGMeshBVH::mutableValue(qsizetype idx)
extern "C" Q_DECL_EXPORT
QSSGMeshBVHNode *ritual_ZN11QSSGMeshBVH12mutableValueEx(
    QSSGMeshBVH *self,
    qsizetype idx) {
  return &(self->mutableValue(idx));
}

//  const QSSGMeshBVHNode &QSSGMeshBVH::value(qsizetype idx) const
extern "C" Q_DECL_EXPORT
QSSGMeshBVHNode *ritual_ZNK11QSSGMeshBVH5valueEx(
    const QSSGMeshBVH *self,
    qsizetype idx) {
  return new QSSGMeshBVHNode(self->value(idx));
}
