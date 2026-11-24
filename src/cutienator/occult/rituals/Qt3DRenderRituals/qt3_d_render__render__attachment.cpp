//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/attachmentpack_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/attachmentpack_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::Attachment::Attachment()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Attachment *ritual_ZN10Qt3DRender6Render10AttachmentC1Ev() {
  return new Qt3DRender::Render::Attachment();
}

//  Qt3DRender::Render::Attachment::~Attachment()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render10AttachmentD1Ev(
    Qt3DRender::Render::Attachment *self) {
  delete self;
}
