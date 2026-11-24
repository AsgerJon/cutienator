//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendereffect_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendereffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderEffect::QSSGRenderEffect()
extern "C" Q_DECL_EXPORT
QSSGRenderEffect *ritual_ZN16QSSGRenderEffectC1Ev() {
  return new QSSGRenderEffect();
}

//  QSSGRenderEffect::~QSSGRenderEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderEffectD1Ev(QSSGRenderEffect *self) {
  delete self;
}

//  void QSSGRenderEffect::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderEffect9markDirtyEv(QSSGRenderEffect *self) {
  self->markDirty();
}

//  void QSSGRenderEffect::clearDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderEffect10clearDirtyEv(QSSGRenderEffect *self) {
  self->clearDirty();
}

//  bool QSSGRenderEffect::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSSGRenderEffect7isDirtyEv(const QSSGRenderEffect *self) {
  return self->isDirty();
}

//  void QSSGRenderEffect::setFlag(QSSGRenderEffect::Flags flag, bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderEffect7setFlagENS_5FlagsEb(
    QSSGRenderEffect *self,
    QSSGRenderEffect::Flags flag,
    bool enabled) {
  self->setFlag(flag, enabled);
}

//  bool QSSGRenderEffect::testFlag(QSSGRenderEffect::Flags flag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSSGRenderEffect8testFlagENS_5FlagsE(
    const QSSGRenderEffect *self,
    QSSGRenderEffect::Flags flag) {
  return self->testFlag(flag);
}

//  void QSSGRenderEffect::resetCommands()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderEffect13resetCommandsEv(QSSGRenderEffect *self) {
  self->resetCommands();
}
