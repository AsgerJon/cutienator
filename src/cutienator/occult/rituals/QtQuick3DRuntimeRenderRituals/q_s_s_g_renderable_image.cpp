//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableimage_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableimage_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimagetexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderableImage::QSSGRenderableImage(Type inMapType, const
//      QSSGRenderImage &inImageNode, const QSSGRenderImageTexture
//      &inTexture)
extern "C" Q_DECL_EXPORT
QSSGRenderableImage *ritual_ZN19QSSGRenderableImageC1ENS_4TypeERK15QSSGRenderImageRK22QSSGRenderImageTexture(
    QSSGRenderableImage::Type inMapType,
    const QSSGRenderImage *inImageNode,
    const QSSGRenderImageTexture *inTexture) {
  return new QSSGRenderableImage(inMapType, *inImageNode, *inTexture);
}

//  QSSGRenderableImage::~QSSGRenderableImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRenderableImageD1Ev(QSSGRenderableImage *self) {
  delete self;
}
