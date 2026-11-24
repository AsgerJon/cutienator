//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>

//  const char
//      *QSSGShaderFeatures::asDefineString(QSSGShaderFeatures::Feature
//      feature)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QSSGShaderFeatures14asDefineStringENS_7FeatureE(
    QSSGShaderFeatures::Feature feature) {
  return QSSGShaderFeatures::asDefineString(feature);
}

//  Feature QSSGShaderFeatures::fromIndex(quint32 idx)
extern "C" Q_DECL_EXPORT
QSSGShaderFeatures::Feature ritual_ZN18QSSGShaderFeatures9fromIndexEj(
    quint32 idx) {
  return QSSGShaderFeatures::fromIndex(idx);
}

//  bool QSSGShaderFeatures::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSSGShaderFeatures6isNullEv(
    const QSSGShaderFeatures *self) {
  return self->isNull();
}

//  bool QSSGShaderFeatures::isSet(Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSSGShaderFeatures5isSetENS_7FeatureE(
    const QSSGShaderFeatures *self,
    QSSGShaderFeatures::Feature feature) {
  return self->isSet(feature);
}

//  void QSSGShaderFeatures::set(Feature feature, bool val)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGShaderFeatures3setENS_7FeatureEb(
    QSSGShaderFeatures *self,
    QSSGShaderFeatures::Feature feature,
    bool val) {
  self->set(feature, val);
}

//  bool operator==(QSSGShaderFeatures a, QSSGShaderFeatures b)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq18QSSGShaderFeaturesS_(
    const QSSGShaderFeatures *a,
    const QSSGShaderFeatures *b) {
  return operator==(*a, *b);
}

//  void QSSGShaderFeatures::disableTonemapping()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGShaderFeatures18disableTonemappingEv(
    QSSGShaderFeatures *self) {
  self->disableTonemapping();
}

//  QDebug operator<<(QDebug stream, const QSSGShaderFeatures &features)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK18QSSGShaderFeatures(
    const QDebug *stream,
    const QSSGShaderFeatures *features) {
  return new QDebug(operator<<(*stream, *features));
}

//  QSSGShaderFeatures::~QSSGShaderFeatures()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGShaderFeaturesD1Ev(QSSGShaderFeatures *self) {
  delete self;
}
