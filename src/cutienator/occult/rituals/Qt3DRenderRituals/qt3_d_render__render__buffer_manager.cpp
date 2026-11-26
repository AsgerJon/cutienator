//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/buffermanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/buffermanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  Qt3DRender::Render::BufferManager::BufferManager()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::BufferManager *ritual_ZN10Qt3DRender6Render13BufferManagerC1Ev() {
  return new Qt3DRender::Render::BufferManager();
}

//  Qt3DRender::Render::BufferManager::~BufferManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13BufferManagerD1Ev(
    Qt3DRender::Render::BufferManager *self) {
  delete self;
}

//  void Qt3DRender::Render::BufferManager::addDirtyBuffer(Qt3DCore::QNodeId
//      bufferId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13BufferManager14addDirtyBufferEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::BufferManager *self,
    const Qt3DCore::QNodeId *bufferId) {
  self->addDirtyBuffer(*bufferId);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::BufferManager::takeDirtyBuffers()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZN10Qt3DRender6Render13BufferManager16takeDirtyBuffersEv(
    Qt3DRender::Render::BufferManager *self) {
  return new QList<Qt3DCore::QNodeId>(self->takeDirtyBuffers());
}

//  void
//      Qt3DRender::Render::BufferManager::addBufferReference(Qt3DCore::QNode
//      Id bufferId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13BufferManager18addBufferReferenceEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::BufferManager *self,
    const Qt3DCore::QNodeId *bufferId) {
  self->addBufferReference(*bufferId);
}

//  void Qt3DRender::Render::BufferManager::removeBufferReference(Qt3DCore::Q
//      NodeId bufferId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13BufferManager21removeBufferReferenceEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::BufferManager *self,
    const Qt3DCore::QNodeId *bufferId) {
  self->removeBufferReference(*bufferId);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::BufferManager::takeBuffersToRelease()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZN10Qt3DRender6Render13BufferManager20takeBuffersToReleaseEv(
    Qt3DRender::Render::BufferManager *self) {
  return new QList<Qt3DCore::QNodeId>(self->takeBuffersToRelease());
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::BufferManager
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_BufferManager__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
