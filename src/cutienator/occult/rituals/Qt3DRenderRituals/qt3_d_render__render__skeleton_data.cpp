//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/skeletondata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/skeletondata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/skeletondata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/geometry/skeletondata.cpp, line 11, as _ZN10Qt3DRender6Render12SkeletonDataC1Ev
namespace Qt3DRender::Render {
inline SkeletonData::SkeletonData()
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/skeletondata.cpp, line 15, as _ZN10Qt3DRender6Render12SkeletonData7reserveEi
namespace Qt3DRender::Render {
inline void SkeletonData::reserve(int size)
{
    joints.reserve(size);
    localPoses.reserve(size);
    jointNames.reserve(size);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::SkeletonData::SkeletonData()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SkeletonData *ritual_ZN10Qt3DRender6Render12SkeletonDataC1Ev() {
  return new Qt3DRender::Render::SkeletonData();
}

//  void Qt3DRender::Render::SkeletonData::reserve(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12SkeletonData7reserveEi(
    Qt3DRender::Render::SkeletonData *self,
    int size) {
  self->reserve(size);
}

//  Qt3DRender::Render::SkeletonData::~SkeletonData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12SkeletonDataD1Ev(
    Qt3DRender::Render::SkeletonData *self) {
  delete self;
}
