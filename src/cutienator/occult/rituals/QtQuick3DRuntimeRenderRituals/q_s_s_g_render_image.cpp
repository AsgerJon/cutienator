//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimage_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderImage::QSSGRenderImage(QSSGRenderGraphObject::Type type)
extern "C" Q_DECL_EXPORT
QSSGRenderImage *ritual_ZN15QSSGRenderImageC1EN21QSSGRenderGraphObject4TypeE(
    QSSGRenderGraphObject::Type type) {
  return new QSSGRenderImage(type);
}

//  QSSGRenderImage::~QSSGRenderImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGRenderImageD1Ev(QSSGRenderImage *self) {
  delete self;
}

//  bool QSSGRenderImage::clearDirty()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSSGRenderImage10clearDirtyEv(QSSGRenderImage *self) {
  return self->clearDirty();
}

//  void QSSGRenderImage::calculateTextureTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGRenderImage25calculateTextureTransformEv(
    QSSGRenderImage *self) {
  self->calculateTextureTransform();
}

//  bool QSSGRenderImage::isImageTransformIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderImage24isImageTransformIdentityEv(
    const QSSGRenderImage *self) {
  return self->isImageTransformIdentity();
}
