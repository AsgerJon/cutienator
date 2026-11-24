//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimagetexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererutil_p.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGBufferManager::QSSGBufferManager()
extern "C" Q_DECL_EXPORT
QSSGBufferManager *ritual_ZN17QSSGBufferManagerC1Ev() {
  return new QSSGBufferManager();
}

//  QSSGBufferManager::~QSSGBufferManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManagerD1Ev(QSSGBufferManager *self) {
  delete self;
}

//  void
//      QSSGBufferManager::setRenderContextInterface(QSSGRenderContextInterfa
//      ce *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager25setRenderContextInterfaceEP26QSSGRenderContextInterface(
    QSSGBufferManager *self,
    QSSGRenderContextInterface *ctx) {
  self->setRenderContextInterface(ctx);
}

//  void QSSGBufferManager::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager22releaseCachedResourcesEv(
    QSSGBufferManager *self) {
  self->releaseCachedResources();
}

//  void QSSGBufferManager::releaseResourcesForLayer(QSSGRenderLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager24releaseResourcesForLayerEP15QSSGRenderLayer(
    QSSGBufferManager *self,
    QSSGRenderLayer *layer) {
  self->releaseResourcesForLayer(layer);
}

//  QSSGRenderImageTexture QSSGBufferManager::loadRenderImage(const
//      QSSGRenderImage *image, MipMode inMipMode, LoadRenderImageFlags
//      flags)
extern "C" Q_DECL_EXPORT
QSSGRenderImageTexture *ritual_ZN17QSSGBufferManager15loadRenderImageEPK15QSSGRenderImageNS_7MipModeE6QFlagsINS_19LoadRenderImageFlagEE(
    QSSGBufferManager *self,
    const QSSGRenderImage *image,
    QSSGBufferManager::MipMode inMipMode,
    int flags) {
  return new QSSGRenderImageTexture(
      self->loadRenderImage(
          image,
          inMipMode,
          QFlags<QSSGBufferManager::LoadRenderImageFlag>::fromInt(flags)));
}

//  QSSGRenderImageTexture
//      QSSGBufferManager::loadTextureData(QSSGRenderTextureData *data,
//      MipMode inMipMode)
extern "C" Q_DECL_EXPORT
QSSGRenderImageTexture *ritual_ZN17QSSGBufferManager15loadTextureDataEP21QSSGRenderTextureDataNS_7MipModeE(
    QSSGBufferManager *self,
    QSSGRenderTextureData *data,
    QSSGBufferManager::MipMode inMipMode) {
  return new QSSGRenderImageTexture(self->loadTextureData(data, inMipMode));
}

//  QSSGRenderImageTexture
//      QSSGBufferManager::loadSkinmap(QSSGRenderTextureData *skin)
extern "C" Q_DECL_EXPORT
QSSGRenderImageTexture *ritual_ZN17QSSGBufferManager11loadSkinmapEP21QSSGRenderTextureData(
    QSSGBufferManager *self,
    QSSGRenderTextureData *skin) {
  return new QSSGRenderImageTexture(self->loadSkinmap(skin));
}

//  QSSGBounds3 QSSGBufferManager::getModelBounds(const QSSGRenderModel
//      *model)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN17QSSGBufferManager14getModelBoundsEPK15QSSGRenderModel(
    QSSGBufferManager *self,
    const QSSGRenderModel *model) {
  return new QSSGBounds3(self->getModelBounds(model));
}

//  void QSSGBufferManager::cleanupUnreferencedBuffers(quint32 frameId,
//      QSSGRenderLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager26cleanupUnreferencedBuffersEjP15QSSGRenderLayer(
    QSSGBufferManager *self,
    quint32 frameId,
    QSSGRenderLayer *layer) {
  self->cleanupUnreferencedBuffers(frameId, layer);
}

//  void QSSGBufferManager::resetUsageCounters(quint32 frameId,
//      QSSGRenderLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager18resetUsageCountersEjP15QSSGRenderLayer(
    QSSGBufferManager *self,
    quint32 frameId,
    QSSGRenderLayer *layer) {
  self->resetUsageCounters(frameId, layer);
}

//  void QSSGBufferManager::releaseGeometry(QSSGRenderGeometry *geometry,
//      const QString &lightmapSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager15releaseGeometryEP18QSSGRenderGeometryRK7QString(
    QSSGBufferManager *self,
    QSSGRenderGeometry *geometry,
    const QString *lightmapSource) {
  self->releaseGeometry(geometry, *lightmapSource);
}

//  void QSSGBufferManager::releaseTextureData(const QSSGRenderTextureData
//      *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager18releaseTextureDataEPK21QSSGRenderTextureData(
    QSSGBufferManager *self,
    const QSSGRenderTextureData *data) {
  self->releaseTextureData(data);
}

//  void QSSGBufferManager::releaseTextureData(const CustomImageCacheKey
//      &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager18releaseTextureDataERKNS_19CustomImageCacheKeyE(
    QSSGBufferManager *self,
    const QSSGBufferManager::CustomImageCacheKey *key) {
  self->releaseTextureData(*key);
}

//  void QSSGBufferManager::commitBufferResourceUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager27commitBufferResourceUpdatesEv(
    QSSGBufferManager *self) {
  self->commitBufferResourceUpdates();
}

//  void QSSGBufferManager::processResourceLoader(const
//      QSSGRenderResourceLoader *loader)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager21processResourceLoaderEPK24QSSGRenderResourceLoader(
    QSSGBufferManager *self,
    const QSSGRenderResourceLoader *loader) {
  self->processResourceLoader(loader);
}

//  QSSGMesh::Mesh QSSGBufferManager::loadMeshData(const QSSGRenderPath
//      &inSourcePath)
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh *ritual_ZN17QSSGBufferManager12loadMeshDataERK14QSSGRenderPath(
    const QSSGRenderPath *inSourcePath) {
  return new QSSGMesh::Mesh(QSSGBufferManager::loadMeshData(*inSourcePath));
}

//  QSSGMesh::Mesh QSSGBufferManager::loadMeshData(const QSSGRenderGeometry
//      *geometry)
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh *ritual_ZN17QSSGBufferManager12loadMeshDataEPK18QSSGRenderGeometry(
    QSSGBufferManager *self,
    const QSSGRenderGeometry *geometry) {
  return new QSSGMesh::Mesh(self->loadMeshData(geometry));
}

//  QRhiTexture::Format QSSGBufferManager::toRhiFormat(const
//      QSSGRenderTextureFormat format)
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZN17QSSGBufferManager11toRhiFormatE23QSSGRenderTextureFormat(
    const QSSGRenderTextureFormat *format) {
  return QSSGBufferManager::toRhiFormat(*format);
}

//  void QSSGBufferManager::unregisterMeshData(const QString &assetId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager18unregisterMeshDataERK7QString(
    const QString *assetId) {
  QSSGBufferManager::unregisterMeshData(*assetId);
}

//  QString QSSGBufferManager::runtimeMeshSourceName(const QString &assetId,
//      qsizetype meshId)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QSSGBufferManager21runtimeMeshSourceNameERK7QStringx(
    const QString *assetId,
    qsizetype meshId) {
  return new QString(
      QSSGBufferManager::runtimeMeshSourceName(
          *assetId,
          meshId));
}

//  QString QSSGBufferManager::primitivePath(const QString &primitive)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QSSGBufferManager13primitivePathERK7QString(
    const QString *primitive) {
  return new QString(QSSGBufferManager::primitivePath(*primitive));
}

//  QMutex *QSSGBufferManager::meshUpdateMutex()
extern "C" Q_DECL_EXPORT
QMutex *ritual_ZN17QSSGBufferManager15meshUpdateMutexEv(
    QSSGBufferManager *self) {
  return self->meshUpdateMutex();
}

//  void QSSGBufferManager::increaseMemoryStat(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager18increaseMemoryStatEP11QRhiTexture(
    QSSGBufferManager *self,
    QRhiTexture *texture) {
  self->increaseMemoryStat(texture);
}

//  void QSSGBufferManager::decreaseMemoryStat(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager18decreaseMemoryStatEP11QRhiTexture(
    QSSGBufferManager *self,
    QRhiTexture *texture) {
  self->decreaseMemoryStat(texture);
}

//  void QSSGBufferManager::increaseMemoryStat(QSSGRenderMesh *mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager18increaseMemoryStatEP14QSSGRenderMesh(
    QSSGBufferManager *self,
    QSSGRenderMesh *mesh) {
  self->increaseMemoryStat(mesh);
}

//  void QSSGBufferManager::decreaseMemoryStat(QSSGRenderMesh *mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager18decreaseMemoryStatEP14QSSGRenderMesh(
    QSSGBufferManager *self,
    QSSGRenderMesh *mesh) {
  self->decreaseMemoryStat(mesh);
}

//  void QSSGBufferManager::setLightmapSource(const QString &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager17setLightmapSourceERK7QString(
    QSSGBufferManager *self,
    const QString *source) {
  self->setLightmapSource(*source);
}

//  void QSSGBufferManager::setCurrentlyLightmapBaking(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager26setCurrentlyLightmapBakingEb(
    QSSGBufferManager *self,
    bool value) {
  self->setCurrentlyLightmapBaking(value);
}

//  void QSSGBufferManager::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager5clearEv(QSSGBufferManager *self) {
  self->clear();
}

//  QRhiResourceUpdateBatch *QSSGBufferManager::meshBufferUpdateBatch()
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatch *ritual_ZN17QSSGBufferManager21meshBufferUpdateBatchEv(
    QSSGBufferManager *self) {
  return self->meshBufferUpdateBatch();
}

//  QSSGMesh::Mesh QSSGBufferManager::loadPrimitive(const QString
//      &inRelativePath)
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh *ritual_ZN17QSSGBufferManager13loadPrimitiveERK7QString(
    const QString *inRelativePath) {
  return new QSSGMesh::Mesh(
      QSSGBufferManager::loadPrimitive(
          *inRelativePath));
}

//  QSSGRenderMesh *QSSGBufferManager::loadRenderMesh(const QSSGRenderPath
//      &inSourcePath, QSSGMeshProcessingOptions options)
extern "C" Q_DECL_EXPORT
QSSGRenderMesh *ritual_ZN17QSSGBufferManager14loadRenderMeshERK14QSSGRenderPath25QSSGMeshProcessingOptions(
    QSSGBufferManager *self,
    const QSSGRenderPath *inSourcePath,
    const QSSGMeshProcessingOptions *options) {
  return self->loadRenderMesh(*inSourcePath, *options);
}

//  QSSGRenderMesh *QSSGBufferManager::loadRenderMesh(QSSGRenderGeometry
//      *geometry, QSSGMeshProcessingOptions options)
extern "C" Q_DECL_EXPORT
QSSGRenderMesh *ritual_ZN17QSSGBufferManager14loadRenderMeshEP18QSSGRenderGeometry25QSSGMeshProcessingOptions(
    QSSGBufferManager *self,
    QSSGRenderGeometry *geometry,
    const QSSGMeshProcessingOptions *options) {
  return self->loadRenderMesh(geometry, *options);
}

//  QSSGRenderMesh *QSSGBufferManager::createRenderMesh(const QSSGMesh::Mesh
//      &mesh, const QString &debugObjectName)
extern "C" Q_DECL_EXPORT
QSSGRenderMesh *ritual_ZN17QSSGBufferManager16createRenderMeshERKN8QSSGMesh4MeshERK7QString(
    QSSGBufferManager *self,
    const QSSGMesh::Mesh *mesh,
    const QString *debugObjectName) {
  return self->createRenderMesh(*mesh, *debugObjectName);
}

//  bool QSSGBufferManager::createEnvironmentMap(const QSSGLoadedTexture
//      *inImage, QSSGRenderImageTexture *outTexture, const QString
//      &debugObjectName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSSGBufferManager20createEnvironmentMapEPK17QSSGLoadedTextureP22QSSGRenderImageTextureRK7QString(
    QSSGBufferManager *self,
    const QSSGLoadedTexture *inImage,
    QSSGRenderImageTexture *outTexture,
    const QString *debugObjectName) {
  return self->createEnvironmentMap(inImage, outTexture, *debugObjectName);
}

//  void QSSGBufferManager::releaseMesh(const QSSGRenderPath &inSourcePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager11releaseMeshERK14QSSGRenderPath(
    QSSGBufferManager *self,
    const QSSGRenderPath *inSourcePath) {
  self->releaseMesh(*inSourcePath);
}

//  void QSSGBufferManager::releaseImage(const ImageCacheKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager12releaseImageERKNS_13ImageCacheKeyE(
    QSSGBufferManager *self,
    const QSSGBufferManager::ImageCacheKey *key) {
  self->releaseImage(*key);
}

//  bool QSSGBufferManager::validateLightmap()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSSGBufferManager16validateLightmapEv(
    QSSGBufferManager *self) {
  return self->validateLightmap();
}
