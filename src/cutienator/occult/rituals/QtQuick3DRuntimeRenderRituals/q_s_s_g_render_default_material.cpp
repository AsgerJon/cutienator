//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterial_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderDefaultMaterial::QSSGRenderDefaultMaterial(Type type)
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial *ritual_ZN25QSSGRenderDefaultMaterialC1EN21QSSGRenderGraphObject4TypeE(
    QSSGRenderGraphObject::Type type) {
  return new QSSGRenderDefaultMaterial(type);
}

//  QSSGRenderDefaultMaterial::~QSSGRenderDefaultMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGRenderDefaultMaterialD1Ev(
    QSSGRenderDefaultMaterial *self) {
  delete self;
}

//  bool QSSGRenderDefaultMaterial::isSpecularEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial17isSpecularEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isSpecularEnabled();
}

//  bool QSSGRenderDefaultMaterial::isMetalnessEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial18isMetalnessEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isMetalnessEnabled();
}

//  bool QSSGRenderDefaultMaterial::isFresnelScaleBiasEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial25isFresnelScaleBiasEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isFresnelScaleBiasEnabled();
}

//  bool QSSGRenderDefaultMaterial::isClearcoatFresnelScaleBiasEnabled()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial34isClearcoatFresnelScaleBiasEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isClearcoatFresnelScaleBiasEnabled();
}

//  bool QSSGRenderDefaultMaterial::isFresnelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial16isFresnelEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isFresnelEnabled();
}

//  bool QSSGRenderDefaultMaterial::isVertexColorsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial21isVertexColorsEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isVertexColorsEnabled();
}

//  bool QSSGRenderDefaultMaterial::isVertexColorsMaskEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial25isVertexColorsMaskEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isVertexColorsMaskEnabled();
}

//  bool QSSGRenderDefaultMaterial::isInvertOpacityMapValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial23isInvertOpacityMapValueEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isInvertOpacityMapValue();
}

//  bool QSSGRenderDefaultMaterial::isBaseColorSingleChannelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial31isBaseColorSingleChannelEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isBaseColorSingleChannelEnabled();
}

//  bool QSSGRenderDefaultMaterial::isSpecularAmountSingleChannelEnabled()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial36isSpecularAmountSingleChannelEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isSpecularAmountSingleChannelEnabled();
}

//  bool QSSGRenderDefaultMaterial::isEmissiveSingleChannelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial30isEmissiveSingleChannelEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isEmissiveSingleChannelEnabled();
}

//  bool QSSGRenderDefaultMaterial::hasLighting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial11hasLightingEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->hasLighting();
}

//  bool QSSGRenderDefaultMaterial::isClearcoatEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial18isClearcoatEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isClearcoatEnabled();
}

//  bool QSSGRenderDefaultMaterial::isTransmissionEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial21isTransmissionEnabledEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isTransmissionEnabled();
}

//  bool QSSGRenderDefaultMaterial::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSSGRenderDefaultMaterial7isDirtyEv(
    const QSSGRenderDefaultMaterial *self) {
  return self->isDirty();
}

//  void QSSGRenderDefaultMaterial::clearDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGRenderDefaultMaterial10clearDirtyEv(
    QSSGRenderDefaultMaterial *self) {
  self->clearDirty();
}
