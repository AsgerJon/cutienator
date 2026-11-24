//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qcameralens_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qcameralens_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool Qt3DRender::CameraLensRequest::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender17CameraLensRequestcvbEv(
    const Qt3DRender::CameraLensRequest *self) {
  return self->operator bool();
}

//  Qt3DRender::CameraLensRequest::~CameraLensRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17CameraLensRequestD1Ev(
    Qt3DRender::CameraLensRequest *self) {
  delete self;
}
