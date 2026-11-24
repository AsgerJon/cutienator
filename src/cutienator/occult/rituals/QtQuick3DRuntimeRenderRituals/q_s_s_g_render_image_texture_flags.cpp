//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimagetexture_p.h
//  , Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimagetexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSSGRenderImageTextureFlags::hasTransparency() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSSGRenderImageTextureFlags15hasTransparencyEv(
    const QSSGRenderImageTextureFlags *self) {
  return self->hasTransparency();
}

//  void QSSGRenderImageTextureFlags::setHasTransparency(bool inValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGRenderImageTextureFlags18setHasTransparencyEb(
    QSSGRenderImageTextureFlags *self,
    bool inValue) {
  self->setHasTransparency(inValue);
}

//  bool QSSGRenderImageTextureFlags::isRgbe8() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSSGRenderImageTextureFlags7isRgbe8Ev(
    const QSSGRenderImageTextureFlags *self) {
  return self->isRgbe8();
}

//  void QSSGRenderImageTextureFlags::setRgbe8(bool inValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGRenderImageTextureFlags8setRgbe8Eb(
    QSSGRenderImageTextureFlags *self,
    bool inValue) {
  self->setRgbe8(inValue);
}

//  bool QSSGRenderImageTextureFlags::isLinear() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSSGRenderImageTextureFlags8isLinearEv(
    const QSSGRenderImageTextureFlags *self) {
  return self->isLinear();
}

//  void QSSGRenderImageTextureFlags::setLinear(bool inValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGRenderImageTextureFlags9setLinearEb(
    QSSGRenderImageTextureFlags *self,
    bool inValue) {
  self->setLinear(inValue);
}

//  bool QSSGRenderImageTextureFlags::isPreMultipliedAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSSGRenderImageTextureFlags20isPreMultipliedAlphaEv(
    const QSSGRenderImageTextureFlags *self) {
  return self->isPreMultipliedAlpha();
}

//  void QSSGRenderImageTextureFlags::setPreMultipliedAlpha(bool inValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGRenderImageTextureFlags21setPreMultipliedAlphaEb(
    QSSGRenderImageTextureFlags *self,
    bool inValue) {
  self->setPreMultipliedAlpha(inValue);
}

//  QSSGRenderImageTextureFlags::~QSSGRenderImageTextureFlags()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGRenderImageTextureFlagsD1Ev(
    QSSGRenderImageTextureFlags *self) {
  delete self;
}
