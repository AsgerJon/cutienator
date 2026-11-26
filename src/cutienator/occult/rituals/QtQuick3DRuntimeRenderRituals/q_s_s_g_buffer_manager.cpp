//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimagetexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererutil_p.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <memory>

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

//  QSSGRenderImageTexture QSSGBufferManager::loadLightmap(const
//      QSSGRenderModel &model)
extern "C" Q_DECL_EXPORT
QSSGRenderImageTexture *ritual_ZN17QSSGBufferManager12loadLightmapERK15QSSGRenderModel(
    QSSGBufferManager *self,
    const QSSGRenderModel *model) {
  return new QSSGRenderImageTexture(self->loadLightmap(*model));
}

//  QSSGRenderImageTexture
//      QSSGBufferManager::loadSkinmap(QSSGRenderTextureData *skin)
extern "C" Q_DECL_EXPORT
QSSGRenderImageTexture *ritual_ZN17QSSGBufferManager11loadSkinmapEP21QSSGRenderTextureData(
    QSSGBufferManager *self,
    QSSGRenderTextureData *skin) {
  return new QSSGRenderImageTexture(self->loadSkinmap(skin));
}

//  QSSGRenderMesh *QSSGBufferManager::getMeshForPicking(const
//      QSSGRenderModel &model, const QString &lightmap) const
extern "C" Q_DECL_EXPORT
QSSGRenderMesh *ritual_ZNK17QSSGBufferManager17getMeshForPickingERK15QSSGRenderModelRK7QString(
    const QSSGBufferManager *self,
    const QSSGRenderModel *model,
    const QString *lightmap) {
  return self->getMeshForPicking(*model, *lightmap);
}

//  QSSGBounds3 QSSGBufferManager::getModelBounds(const QSSGRenderModel
//      *model)
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZN17QSSGBufferManager14getModelBoundsEPK15QSSGRenderModel(
    QSSGBufferManager *self,
    const QSSGRenderModel *model) {
  return new QSSGBounds3(self->getModelBounds(model));
}

//  QSSGRenderMesh *QSSGBufferManager::loadMesh(const QSSGRenderModel &model)
extern "C" Q_DECL_EXPORT
QSSGRenderMesh *ritual_ZN17QSSGBufferManager8loadMeshERK15QSSGRenderModel(
    QSSGBufferManager *self,
    const QSSGRenderModel *model) {
  return self->loadMesh(*model);
}

//  QSSGMesh::Mesh QSSGBufferManager::loadLightmapMesh(const QSSGRenderModel
//      &model)
extern "C" Q_DECL_EXPORT
QSSGMesh::Mesh *ritual_ZN17QSSGBufferManager16loadLightmapMeshERK15QSSGRenderModel(
    QSSGBufferManager *self,
    const QSSGRenderModel *model) {
  return new QSSGMesh::Mesh(self->loadLightmapMesh(*model));
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

//  void QSSGBufferManager::releaseExtensionResult(const QSSGRenderExtension
//      &rext)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager22releaseExtensionResultERK19QSSGRenderExtension(
    QSSGBufferManager *self,
    const QSSGRenderExtension *rext) {
  self->releaseExtensionResult(*rext);
}

//  void QSSGBufferManager::releaseUserRenderPass(const QSSGRenderUserPass
//      &upass)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager21releaseUserRenderPassERK18QSSGRenderUserPass(
    QSSGBufferManager *self,
    const QSSGRenderUserPass *upass) {
  self->releaseUserRenderPass(*upass);
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

//  std::unique_ptr<QSSGMeshBVH> QSSGBufferManager::loadMeshBVH(const
//      QSSGRenderPath &inSourcePath)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QSSGMeshBVH> *ritual_ZN17QSSGBufferManager11loadMeshBVHERK14QSSGRenderPath(
    const QSSGRenderPath *inSourcePath) {
  return new std::unique_ptr<QSSGMeshBVH>(
      QSSGBufferManager::loadMeshBVH(
          *inSourcePath));
}

//  std::unique_ptr<QSSGMeshBVH>
//      QSSGBufferManager::loadMeshBVH(QSSGRenderGeometry *geometry)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QSSGMeshBVH> *ritual_ZN17QSSGBufferManager11loadMeshBVHEP18QSSGRenderGeometry(
    QSSGRenderGeometry *geometry) {
  return new std::unique_ptr<QSSGMeshBVH>(
      QSSGBufferManager::loadMeshBVH(
          geometry));
}

//  std::unique_ptr<QSSGMeshBVH> QSSGBufferManager::loadMeshBVH(const
//      QSSGMesh::Mesh &mesh)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QSSGMeshBVH> *ritual_ZN17QSSGBufferManager11loadMeshBVHERKN8QSSGMesh4MeshE(
    const QSSGMesh::Mesh *mesh) {
  return new std::unique_ptr<QSSGMeshBVH>(
      QSSGBufferManager::loadMeshBVH(
          *mesh));
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

//  void QSSGBufferManager::registerExtensionResult(const QSSGRenderExtension
//      &extensions, QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager23registerExtensionResultERK19QSSGRenderExtensionP11QRhiTexture(
    QSSGBufferManager *self,
    const QSSGRenderExtension *extensions,
    QRhiTexture *texture) {
  self->registerExtensionResult(*extensions, texture);
}

//  QRhiTexture::Format QSSGBufferManager::toRhiFormat(const
//      QSSGRenderTextureFormat format)
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZN17QSSGBufferManager11toRhiFormatE23QSSGRenderTextureFormat(
    const QSSGRenderTextureFormat *format) {
  return QSSGBufferManager::toRhiFormat(*format);
}

//  void QSSGBufferManager::registerMeshData(const QString &assetId, const
//      QVector<QSSGMesh::Mesh> &meshData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager16registerMeshDataERK7QStringRK5QListIN8QSSGMesh4MeshEE(
    const QString *assetId,
    const QVector<QSSGMesh::Mesh> *meshData) {
  QSSGBufferManager::registerMeshData(*assetId, *meshData);
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

//  const QHash<ImageCacheKey, ImageData> &QSSGBufferManager::getImageMap()
//      const
extern "C" Q_DECL_EXPORT
const QHash<QSSGBufferManager::ImageCacheKey, QSSGBufferManager::ImageData> *ritual_ZNK17QSSGBufferManager11getImageMapEv(
    const QSSGBufferManager *self) {
  return &(self->getImageMap());
}

//  const QHash<CustomImageCacheKey, ImageData>
//      &QSSGBufferManager::getCustomTextureMap() const
extern "C" Q_DECL_EXPORT
const QHash<QSSGBufferManager::CustomImageCacheKey, QSSGBufferManager::ImageData> *ritual_ZNK17QSSGBufferManager19getCustomTextureMapEv(
    const QSSGBufferManager *self) {
  return &(self->getCustomTextureMap());
}

//  const QHash<QSGTexture *, ImageData> &QSSGBufferManager::getSGImageMap()
//      const
extern "C" Q_DECL_EXPORT
const QHash<QSGTexture *, QSSGBufferManager::ImageData> *ritual_ZNK17QSSGBufferManager13getSGImageMapEv(
    const QSSGBufferManager *self) {
  return &(self->getSGImageMap());
}

//  const QHash<std::pair<QSSGRenderPath, QString>, MeshData>
//      &QSSGBufferManager::getMeshMap() const
extern "C" Q_DECL_EXPORT
const QHash<std::pair<QSSGRenderPath, QString>, QSSGBufferManager::MeshData> *ritual_ZNK17QSSGBufferManager10getMeshMapEv(
    const QSSGBufferManager *self) {
  return &(self->getMeshMap());
}

//  const QHash<std::pair<QSSGRenderGeometry *, QString>, MeshData>
//      &QSSGBufferManager::getCustomMeshMap() const
extern "C" Q_DECL_EXPORT
const QHash<std::pair<QSSGRenderGeometry *, QString>, QSSGBufferManager::MeshData> *ritual_ZNK17QSSGBufferManager16getCustomMeshMapEv(
    const QSSGBufferManager *self) {
  return &(self->getCustomMeshMap());
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

//  void QSSGBufferManager::registerUserRenderPassManager(const
//      QSSGUserRenderPassManagerPtr &userPassManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGBufferManager29registerUserRenderPassManagerERKSt10shared_ptrI25QSSGUserRenderPassManagerE(
    QSSGBufferManager *self,
    const QSSGUserRenderPassManagerPtr *userPassManager) {
  self->registerUserRenderPassManager(*userPassManager);
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

//  bool QSSGBufferManager::setRhiTexture(QSSGRenderImageTexture &texture,
//      const QSSGLoadedTexture *inTexture, MipMode inMipMode,
//      CreateRhiTextureFlags inFlags, const QString &debugObjectName, bool
//      *wasTextureCreated)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSSGBufferManager13setRhiTextureER22QSSGRenderImageTexturePK17QSSGLoadedTextureNS_7MipModeE6QFlagsINS_20CreateRhiTextureFlagEERK7QStringPb(
    QSSGBufferManager *self,
    QSSGRenderImageTexture *texture,
    const QSSGLoadedTexture *inTexture,
    QSSGBufferManager::MipMode inMipMode,
    int inFlags,
    const QString *debugObjectName,
    bool *wasTextureCreated) {
  return self->setRhiTexture(
      *texture,
      inTexture,
      inMipMode,
      QFlags<QSSGBufferManager::CreateRhiTextureFlag>::fromInt(inFlags),
      *debugObjectName,
      wasTextureCreated);
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

//  a std::unique_ptr<QSSGMeshBVH> a ritual of QSSGBufferManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGBufferManager__std_unique_ptr_QSSGMeshBVH(
    std::unique_ptr<QSSGMeshBVH> *self) {
  delete self;
}
