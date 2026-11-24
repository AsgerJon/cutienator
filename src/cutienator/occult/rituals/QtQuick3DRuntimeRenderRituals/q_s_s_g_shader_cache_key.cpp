//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGShaderCacheKey::QSSGShaderCacheKey(const QByteArray &key)
extern "C" Q_DECL_EXPORT
QSSGShaderCacheKey *ritual_ZN18QSSGShaderCacheKeyC1ERK10QByteArray(
    const QByteArray *key) {
  return new QSSGShaderCacheKey(*key);
}

//  QSSGShaderCacheKey::QSSGShaderCacheKey(const QSSGShaderCacheKey &other)
extern "C" Q_DECL_EXPORT
QSSGShaderCacheKey *ritual_ZN18QSSGShaderCacheKeyC1ERKS_(
    const QSSGShaderCacheKey *other) {
  return new QSSGShaderCacheKey(*other);
}

//  void QSSGShaderCacheKey::updateHashCode()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGShaderCacheKey14updateHashCodeEv(
    QSSGShaderCacheKey *self) {
  self->updateHashCode();
}

//  bool QSSGShaderCacheKey::operator==(const QSSGShaderCacheKey &inOther)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSSGShaderCacheKeyeqERKS_(
    const QSSGShaderCacheKey *self,
    const QSSGShaderCacheKey *inOther) {
  return self->operator==(*inOther);
}

//  QSSGShaderCacheKey::~QSSGShaderCacheKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGShaderCacheKeyD1Ev(QSSGShaderCacheKey *self) {
  delete self;
}
