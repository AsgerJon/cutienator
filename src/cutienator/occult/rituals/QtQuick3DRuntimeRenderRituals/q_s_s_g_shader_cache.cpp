//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGShaderCache::~QSSGShaderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGShaderCacheD1Ev(QSSGShaderCache *self) {
  delete self;
}

//  void QSSGShaderCache::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGShaderCache22releaseCachedResourcesEv(
    QSSGShaderCache *self) {
  self->releaseCachedResources();
}

//  QByteArray QSSGShaderCache::resourceFolder()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QSSGShaderCache14resourceFolderEv() {
  return new QByteArray(QSSGShaderCache::resourceFolder());
}

//  QByteArray QSSGShaderCache::shaderCollectionFile()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QSSGShaderCache20shaderCollectionFileEv() {
  return new QByteArray(QSSGShaderCache::shaderCollectionFile());
}

//  QByteArray QSSGShaderCache::particleShaderCollectionFile()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QSSGShaderCache28particleShaderCollectionFileEv() {
  return new QByteArray(QSSGShaderCache::particleShaderCollectionFile());
}

//  void QSSGShaderCache::initBakerForPersistentUse(QShaderBaker *baker, QRhi
//      *rhi)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGShaderCache25initBakerForPersistentUseEP12QShaderBakerP4QRhi(
    QShaderBaker *baker,
    QRhi *rhi) {
  QSSGShaderCache::initBakerForPersistentUse(baker, rhi);
}
