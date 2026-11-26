//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>

//  void Qt3DRender::Render::SkeletonManager::addDirtySkeleton(DirtyFlag
//      dirtyFlag, HSkeleton skeletonHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15SkeletonManager16addDirtySkeletonENS1_9DirtyFlagEN8Qt3DCore7QHandleINS0_8SkeletonEEE(
    Qt3DRender::Render::SkeletonManager *self,
    Qt3DRender::Render::SkeletonManager::DirtyFlag dirtyFlag,
    const Qt3DRender::Render::HSkeleton *skeletonHandle) {
  self->addDirtySkeleton(dirtyFlag, *skeletonHandle);
}

//  QList<HSkeleton>
//      Qt3DRender::Render::SkeletonManager::takeDirtySkeletons(DirtyFlag
//      dirtyFlag)
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::Render::HSkeleton> *ritual_ZN10Qt3DRender6Render15SkeletonManager18takeDirtySkeletonsENS1_9DirtyFlagE(
    Qt3DRender::Render::SkeletonManager *self,
    Qt3DRender::Render::SkeletonManager::DirtyFlag dirtyFlag) {
  return new QList<Qt3DRender::Render::HSkeleton>(
      self->takeDirtySkeletons(
          dirtyFlag));
}

//  a QList<Qt3DRender::Render::HSkeleton> a ritual of
//      Qt3DRender::Render::SkeletonManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_SkeletonManager__QList_Qt3DRender_Render_HSkeleton(
    QList<Qt3DRender::Render::HSkeleton> *self) {
  delete self;
}
