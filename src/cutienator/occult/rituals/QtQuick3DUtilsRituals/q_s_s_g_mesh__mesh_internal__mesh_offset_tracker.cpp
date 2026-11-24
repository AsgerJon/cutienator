//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGMesh::MeshInternal::MeshOffsetTracker::MeshOffsetTracker(int offset)
extern "C" Q_DECL_EXPORT
QSSGMesh::MeshInternal::MeshOffsetTracker *ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTrackerC1Ei(
    int offset) {
  return new QSSGMesh::MeshInternal::MeshOffsetTracker(offset);
}

//  int QSSGMesh::MeshInternal::MeshOffsetTracker::offset()
extern "C" Q_DECL_EXPORT
int ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTracker6offsetEv(
    QSSGMesh::MeshInternal::MeshOffsetTracker *self) {
  return self->offset();
}

//  quint32 QSSGMesh::MeshInternal::MeshOffsetTracker::alignedAdvance(int
//      advanceAmount)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTracker14alignedAdvanceEi(
    QSSGMesh::MeshInternal::MeshOffsetTracker *self,
    int advanceAmount) {
  return self->alignedAdvance(advanceAmount);
}

//  void QSSGMesh::MeshInternal::MeshOffsetTracker::advance(int
//      advanceAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTracker7advanceEi(
    QSSGMesh::MeshInternal::MeshOffsetTracker *self,
    int advanceAmount) {
  self->advance(advanceAmount);
}

//  QSSGMesh::MeshInternal::MeshOffsetTracker::~MeshOffsetTracker()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTrackerD1Ev(
    QSSGMesh::MeshInternal::MeshOffsetTracker *self) {
  delete self;
}
