//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>

//  bool QSSGRenderLayer::isDirty(DirtyFlag dirtyFlag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderLayer7isDirtyENS_9DirtyFlagE(
    const QSSGRenderLayer *self,
    QSSGRenderLayer::DirtyFlag dirtyFlag) {
  return self->isDirty(dirtyFlag);
}

//  void QSSGRenderLayer::markDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGRenderLayer9markDirtyENS_9DirtyFlagE(
    QSSGRenderLayer *self,
    QSSGRenderLayer::DirtyFlag dirtyFlag) {
  self->markDirty(dirtyFlag);
}

//  void QSSGRenderLayer::clearDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGRenderLayer10clearDirtyENS_9DirtyFlagE(
    QSSGRenderLayer *self,
    QSSGRenderLayer::DirtyFlag dirtyFlag) {
  self->clearDirty(dirtyFlag);
}

//  void QSSGRenderLayer::ref(QSSGRenderRoot *inRootNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGRenderLayer3refEP14QSSGRenderRoot(
    QSSGRenderLayer *self,
    QSSGRenderRoot *inRootNode) {
  self->ref(inRootNode);
}

//  bool QSSGRenderLayer::ssaoEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderLayer11ssaoEnabledEv(
    const QSSGRenderLayer *self) {
  return self->ssaoEnabled();
}

//  QSSGRenderLayer::QSSGRenderLayer()
extern "C" Q_DECL_EXPORT
QSSGRenderLayer *ritual_ZN15QSSGRenderLayerC1Ev() {
  return new QSSGRenderLayer();
}

//  QSSGRenderLayer::~QSSGRenderLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGRenderLayerD1Ev(QSSGRenderLayer *self) {
  delete self;
}

//  void QSSGRenderLayer::setProbeOrientation(const QVector3D &angles)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGRenderLayer19setProbeOrientationERK9QVector3D(
    QSSGRenderLayer *self,
    const QVector3D *angles) {
  self->setProbeOrientation(*angles);
}

//  bool QSSGRenderLayer::hasEffect(QSSGRenderEffect *inEffect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderLayer9hasEffectEP16QSSGRenderEffect(
    const QSSGRenderLayer *self,
    QSSGRenderEffect *inEffect) {
  return self->hasEffect(inEffect);
}

//  bool QSSGRenderLayer::isMsaaEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderLayer13isMsaaEnabledEv(
    const QSSGRenderLayer *self) {
  return self->isMsaaEnabled();
}

//  bool QSSGRenderLayer::isSsaaEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderLayer13isSsaaEnabledEv(
    const QSSGRenderLayer *self) {
  return self->isSsaaEnabled();
}

//  bool QSSGRenderLayer::isProgressiveAAEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderLayer22isProgressiveAAEnabledEv(
    const QSSGRenderLayer *self) {
  return self->isProgressiveAAEnabled();
}

//  bool QSSGRenderLayer::isTemporalAAEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderLayer19isTemporalAAEnabledEv(
    const QSSGRenderLayer *self) {
  return self->isTemporalAAEnabled();
}

//  float
//      QSSGRenderLayer::ssaaMultiplierForQuality(QSSGRenderLayer::AAQuality
//      quality)
extern "C" Q_DECL_EXPORT
float ritual_ZN15QSSGRenderLayer24ssaaMultiplierForQualityENS_9AAQualityE(
    QSSGRenderLayer::AAQuality quality) {
  return QSSGRenderLayer::ssaaMultiplierForQuality(quality);
}
