//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGAllocateTexture::QSSGAllocateTexture()
extern "C" Q_DECL_EXPORT
QSSGAllocateTexture *ritual_ZN19QSSGAllocateTextureC1Ev() {
  return new QSSGAllocateTexture();
}

//  QSSGAllocateTexture::QSSGAllocateTexture(QSSGRenderTextureFormat
//      inFormat)
extern "C" Q_DECL_EXPORT
QSSGAllocateTexture *ritual_ZN19QSSGAllocateTextureC1E23QSSGRenderTextureFormat(
    const QSSGRenderTextureFormat *inFormat) {
  return new QSSGAllocateTexture(*inFormat);
}

//  QSSGRenderTextureFormat QSSGAllocateTexture::format() const
extern "C" Q_DECL_EXPORT
QSSGRenderTextureFormat *ritual_ZNK19QSSGAllocateTexture6formatEv(
    const QSSGAllocateTexture *self) {
  return new QSSGRenderTextureFormat(self->format());
}

//  void QSSGAllocateTexture::setFormat(QSSGRenderTextureFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGAllocateTexture9setFormatE23QSSGRenderTextureFormat(
    QSSGAllocateTexture *self,
    const QSSGRenderTextureFormat *format) {
  self->setFormat(*format);
}
