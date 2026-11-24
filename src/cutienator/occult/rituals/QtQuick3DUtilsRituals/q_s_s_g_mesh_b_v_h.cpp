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

//  const QSSGMeshBVHNode &QSSGMeshBVH::value(qsizetype idx) const
extern "C" Q_DECL_EXPORT
QSSGMeshBVHNode *ritual_ZNK11QSSGMeshBVH5valueEx(
    const QSSGMeshBVH *self,
    qsizetype idx) {
  return new QSSGMeshBVHNode(self->value(idx));
}
