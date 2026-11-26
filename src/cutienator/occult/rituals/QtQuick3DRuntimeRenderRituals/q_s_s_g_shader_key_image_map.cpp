//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGShaderKeyImageMap::QSSGShaderKeyImageMap(const char *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyImageMap *ritual_ZN21QSSGShaderKeyImageMapC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyImageMap(inName);
}

//  bool QSSGShaderKeyImageMap::getBitValue(ImageMapBits imageBit,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGShaderKeyImageMap11getBitValueENS_12ImageMapBitsE12QSSGDataViewIjE(
    const QSSGShaderKeyImageMap *self,
    QSSGShaderKeyImageMap::ImageMapBits imageBit,
    const QSSGDataView<quint32> *inKeySet) {
  return self->getBitValue(imageBit, *inKeySet);
}

//  void QSSGShaderKeyImageMap::setBitValue(ImageMapBits imageBit, bool
//      inValue, QSSGDataRef<quint32> inKeySet)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGShaderKeyImageMap11setBitValueENS_12ImageMapBitsEb11QSSGDataRefIjE(
    QSSGShaderKeyImageMap *self,
    QSSGShaderKeyImageMap::ImageMapBits imageBit,
    bool inValue,
    const QSSGDataRef<quint32> *inKeySet) {
  self->setBitValue(imageBit, inValue, *inKeySet);
}

//  bool QSSGShaderKeyImageMap::isEnabled(QSSGDataView<quint32> inKeySet)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGShaderKeyImageMap9isEnabledE12QSSGDataViewIjE(
    const QSSGShaderKeyImageMap *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->isEnabled(*inKeySet);
}

//  void QSSGShaderKeyImageMap::setEnabled(QSSGDataRef<quint32> inKeySet,
//      bool val)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGShaderKeyImageMap10setEnabledE11QSSGDataRefIjEb(
    QSSGShaderKeyImageMap *self,
    const QSSGDataRef<quint32> *inKeySet,
    bool val) {
  self->setEnabled(*inKeySet, val);
}

//  bool QSSGShaderKeyImageMap::isEnvMap(QSSGDataView<quint32> inKeySet)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGShaderKeyImageMap8isEnvMapE12QSSGDataViewIjE(
    const QSSGShaderKeyImageMap *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->isEnvMap(*inKeySet);
}

//  void QSSGShaderKeyImageMap::setEnvMap(QSSGDataRef<quint32> inKeySet, bool
//      val)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGShaderKeyImageMap9setEnvMapE11QSSGDataRefIjEb(
    QSSGShaderKeyImageMap *self,
    const QSSGDataRef<quint32> *inKeySet,
    bool val) {
  self->setEnvMap(*inKeySet, val);
}

//  bool QSSGShaderKeyImageMap::isLightProbe(QSSGDataView<quint32> inKeySet)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGShaderKeyImageMap12isLightProbeE12QSSGDataViewIjE(
    const QSSGShaderKeyImageMap *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->isLightProbe(*inKeySet);
}

//  void QSSGShaderKeyImageMap::setLightProbe(QSSGDataRef<quint32> inKeySet,
//      bool val)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGShaderKeyImageMap13setLightProbeE11QSSGDataRefIjEb(
    QSSGShaderKeyImageMap *self,
    const QSSGDataRef<quint32> *inKeySet,
    bool val) {
  self->setLightProbe(*inKeySet, val);
}

//  bool QSSGShaderKeyImageMap::isIdentityTransform(QSSGDataView<quint32>
//      inKeySet) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGShaderKeyImageMap19isIdentityTransformE12QSSGDataViewIjE(
    const QSSGShaderKeyImageMap *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->isIdentityTransform(*inKeySet);
}

//  void QSSGShaderKeyImageMap::setIdentityTransform(QSSGDataRef<quint32>
//      inKeySet, bool val)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGShaderKeyImageMap20setIdentityTransformE11QSSGDataRefIjEb(
    QSSGShaderKeyImageMap *self,
    const QSSGDataRef<quint32> *inKeySet,
    bool val) {
  self->setIdentityTransform(*inKeySet, val);
}

//  bool QSSGShaderKeyImageMap::isUsingUV1(QSSGDataView<quint32> inKeySet)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGShaderKeyImageMap10isUsingUV1E12QSSGDataViewIjE(
    const QSSGShaderKeyImageMap *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->isUsingUV1(*inKeySet);
}

//  void QSSGShaderKeyImageMap::setUsesUV1(QSSGDataRef<quint32> inKeySet,
//      bool val)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGShaderKeyImageMap10setUsesUV1E11QSSGDataRefIjEb(
    QSSGShaderKeyImageMap *self,
    const QSSGDataRef<quint32> *inKeySet,
    bool val) {
  self->setUsesUV1(*inKeySet, val);
}

//  bool QSSGShaderKeyImageMap::isLinear(QSSGDataView<quint32> inKeySet)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGShaderKeyImageMap8isLinearE12QSSGDataViewIjE(
    const QSSGShaderKeyImageMap *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->isLinear(*inKeySet);
}

//  void QSSGShaderKeyImageMap::setLinear(QSSGDataRef<quint32> inKeySet, bool
//      val)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGShaderKeyImageMap9setLinearE11QSSGDataRefIjEb(
    QSSGShaderKeyImageMap *self,
    const QSSGDataRef<quint32> *inKeySet,
    bool val) {
  self->setLinear(*inKeySet, val);
}

//  bool QSSGShaderKeyImageMap::isPreMultipliedAlpha(QSSGDataView<quint32>
//      inKeySet) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGShaderKeyImageMap20isPreMultipliedAlphaE12QSSGDataViewIjE(
    const QSSGShaderKeyImageMap *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->isPreMultipliedAlpha(*inKeySet);
}

//  void QSSGShaderKeyImageMap::setPreMultipliedAlpha(QSSGDataRef<quint32>
//      inKeySet, bool val)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGShaderKeyImageMap21setPreMultipliedAlphaE11QSSGDataRefIjEb(
    QSSGShaderKeyImageMap *self,
    const QSSGDataRef<quint32> *inKeySet,
    bool val) {
  self->setPreMultipliedAlpha(*inKeySet, val);
}

//  void QSSGShaderKeyImageMap::toString(QByteArray &ioStr,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QSSGShaderKeyImageMap8toStringER10QByteArray12QSSGDataViewIjE(
    const QSSGShaderKeyImageMap *self,
    QByteArray *ioStr,
    const QSSGDataView<quint32> *inKeySet) {
  self->toString(*ioStr, *inKeySet);
}

//  QSSGShaderKeyImageMap::~QSSGShaderKeyImageMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGShaderKeyImageMapD1Ev(QSSGShaderKeyImageMap *self) {
  delete self;
}
