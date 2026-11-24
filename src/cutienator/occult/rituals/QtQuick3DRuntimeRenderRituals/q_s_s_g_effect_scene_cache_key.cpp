//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhieffectsystem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhieffectsystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGEffectSceneCacheKey::updateHashCode()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGEffectSceneCacheKey14updateHashCodeEv(
    QSSGEffectSceneCacheKey *self) {
  self->updateHashCode();
}

//  bool QSSGEffectSceneCacheKey::operator==(const QSSGEffectSceneCacheKey
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSSGEffectSceneCacheKeyeqERKS_(
    const QSSGEffectSceneCacheKey *self,
    const QSSGEffectSceneCacheKey *other) {
  return self->operator==(*other);
}

//  QSSGEffectSceneCacheKey::~QSSGEffectSceneCacheKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGEffectSceneCacheKeyD1Ev(QSSGEffectSceneCacheKey *self) {
  delete self;
}
