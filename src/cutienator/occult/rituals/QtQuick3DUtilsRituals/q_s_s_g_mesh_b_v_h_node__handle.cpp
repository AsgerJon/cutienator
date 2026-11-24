//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGMeshBVHNode::Handle::Handle()
extern "C" Q_DECL_EXPORT
QSSGMeshBVHNode::Handle *ritual_ZN15QSSGMeshBVHNode6HandleC1Ev() {
  return new QSSGMeshBVHNode::Handle();
}

//  bool QSSGMeshBVHNode::Handle::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGMeshBVHNode6Handle6isNullEv(
    const QSSGMeshBVHNode::Handle *self) {
  return self->isNull();
}

//  const QSSGMeshBVHNode *QSSGMeshBVHNode::Handle::operator const
//      QSSGMeshBVHNode *() const
extern "C" Q_DECL_EXPORT
const QSSGMeshBVHNode *ritual_ZNK15QSSGMeshBVHNode6HandlecvPKS_Ev(
    const QSSGMeshBVHNode::Handle *self) {
  return self->operator const QSSGMeshBVHNode *();
}

//  QSSGMeshBVHNode *QSSGMeshBVHNode::Handle::operator->() const
extern "C" Q_DECL_EXPORT
QSSGMeshBVHNode *ritual_ZNK15QSSGMeshBVHNode6HandleptEv(
    const QSSGMeshBVHNode::Handle *self) {
  return self->operator->();
}

//  QSSGMeshBVHNode::Handle::Handle(QSSGMeshBVH *owner, size_t idx)
extern "C" Q_DECL_EXPORT
QSSGMeshBVHNode::Handle *ritual_ZN15QSSGMeshBVHNode6HandleC1EP11QSSGMeshBVHm(
    QSSGMeshBVH *owner,
    size_t idx) {
  return new QSSGMeshBVHNode::Handle(owner, idx);
}

//  QSSGMeshBVHNode::Handle::~Handle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGMeshBVHNode6HandleD1Ev(QSSGMeshBVHNode::Handle *self) {
  delete self;
}
