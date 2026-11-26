//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/QByteArray>

//  QSSGShaderKeyShadowSoftness::QSSGShaderKeyShadowSoftness(const char
//      *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyShadowSoftness *ritual_ZN27QSSGShaderKeyShadowSoftnessC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyShadowSoftness(inName);
}

//  void QSSGShaderKeyShadowSoftness::setShadowSoftness(QSSGDataRef<quint32>
//      inKeySet, QSSGRenderLight::SoftShadowQuality inQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGShaderKeyShadowSoftness17setShadowSoftnessE11QSSGDataRefIjEN15QSSGRenderLight17SoftShadowQualityE(
    QSSGShaderKeyShadowSoftness *self,
    const QSSGDataRef<quint32> *inKeySet,
    QSSGRenderLight::SoftShadowQuality inQuality) {
  self->setShadowSoftness(*inKeySet, inQuality);
}

//  QSSGRenderLight::SoftShadowQuality
//      QSSGShaderKeyShadowSoftness::getShadowSoftness(QSSGDataView<quint32>
//      inKeySet) const
extern "C" Q_DECL_EXPORT
QSSGRenderLight::SoftShadowQuality ritual_ZNK27QSSGShaderKeyShadowSoftness17getShadowSoftnessE12QSSGDataViewIjE(
    const QSSGShaderKeyShadowSoftness *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->getShadowSoftness(*inKeySet);
}

//  void QSSGShaderKeyShadowSoftness::toString(QByteArray &ioStr,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK27QSSGShaderKeyShadowSoftness8toStringER10QByteArray12QSSGDataViewIjE(
    const QSSGShaderKeyShadowSoftness *self,
    QByteArray *ioStr,
    const QSSGDataView<quint32> *inKeySet) {
  self->toString(*ioStr, *inKeySet);
}

//  void QSSGShaderKeyShadowSoftness::fromString(const QByteArray &ioStr,
//      QSSGDataRef<quint32> inKeySet)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGShaderKeyShadowSoftness10fromStringERK10QByteArray11QSSGDataRefIjE(
    QSSGShaderKeyShadowSoftness *self,
    const QByteArray *ioStr,
    const QSSGDataRef<quint32> *inKeySet) {
  self->fromString(*ioStr, *inKeySet);
}

//  QSSGShaderKeyShadowSoftness::~QSSGShaderKeyShadowSoftness()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGShaderKeyShadowSoftnessD1Ev(
    QSSGShaderKeyShadowSoftness *self) {
  delete self;
}
