//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/nodemanagers_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: added by hand, instances of templates of the
//  class: 11. Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h>
#include <Qt3DCore/qnodeid.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::NodeManagers::NodeManagers()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::NodeManagers *ritual_ZN10Qt3DRender6Render12NodeManagersC1Ev() {
  return new Qt3DRender::Render::NodeManagers();
}

//  Qt3DRender::Render::NodeManagers::~NodeManagers()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12NodeManagersD1Ev(
    Qt3DRender::Render::NodeManagers *self) {
  delete self;
}

//  CameraManager *Qt3DRender::Render::NodeManagers::cameraManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::CameraManager *ritual_ZNK10Qt3DRender6Render12NodeManagers13cameraManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->cameraManager();
}

//  EntityManager *Qt3DRender::Render::NodeManagers::renderNodesManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EntityManager *ritual_ZNK10Qt3DRender6Render12NodeManagers18renderNodesManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->renderNodesManager();
}

//  MaterialManager *Qt3DRender::Render::NodeManagers::materialManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::MaterialManager *ritual_ZNK10Qt3DRender6Render12NodeManagers15materialManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->materialManager();
}

//  MatrixManager *Qt3DRender::Render::NodeManagers::worldMatrixManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::MatrixManager *ritual_ZNK10Qt3DRender6Render12NodeManagers18worldMatrixManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->worldMatrixManager();
}

//  ShaderManager *Qt3DRender::Render::NodeManagers::shaderManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ShaderManager *ritual_ZNK10Qt3DRender6Render12NodeManagers13shaderManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->shaderManager();
}

//  ShaderBuilderManager
//      *Qt3DRender::Render::NodeManagers::shaderBuilderManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ShaderBuilderManager *ritual_ZNK10Qt3DRender6Render12NodeManagers20shaderBuilderManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->shaderBuilderManager();
}

//  TechniqueManager *Qt3DRender::Render::NodeManagers::techniqueManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TechniqueManager *ritual_ZNK10Qt3DRender6Render12NodeManagers16techniqueManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->techniqueManager();
}

//  EffectManager *Qt3DRender::Render::NodeManagers::effectManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EffectManager *ritual_ZNK10Qt3DRender6Render12NodeManagers13effectManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->effectManager();
}

//  RenderPassManager *Qt3DRender::Render::NodeManagers::renderPassManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderPassManager *ritual_ZNK10Qt3DRender6Render12NodeManagers17renderPassManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->renderPassManager();
}

//  TextureManager *Qt3DRender::Render::NodeManagers::textureManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TextureManager *ritual_ZNK10Qt3DRender6Render12NodeManagers14textureManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->textureManager();
}

//  LayerManager *Qt3DRender::Render::NodeManagers::layerManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LayerManager *ritual_ZNK10Qt3DRender6Render12NodeManagers12layerManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->layerManager();
}

//  LevelOfDetailManager
//      *Qt3DRender::Render::NodeManagers::levelOfDetailManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LevelOfDetailManager *ritual_ZNK10Qt3DRender6Render12NodeManagers20levelOfDetailManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->levelOfDetailManager();
}

//  FilterKeyManager *Qt3DRender::Render::NodeManagers::filterKeyManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FilterKeyManager *ritual_ZNK10Qt3DRender6Render12NodeManagers16filterKeyManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->filterKeyManager();
}

//  FrameGraphManager *Qt3DRender::Render::NodeManagers::frameGraphManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FrameGraphManager *ritual_ZNK10Qt3DRender6Render12NodeManagers17frameGraphManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->frameGraphManager();
}

//  TransformManager *Qt3DRender::Render::NodeManagers::transformManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TransformManager *ritual_ZNK10Qt3DRender6Render12NodeManagers16transformManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->transformManager();
}

//  RenderTargetManager
//      *Qt3DRender::Render::NodeManagers::renderTargetManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderTargetManager *ritual_ZNK10Qt3DRender6Render12NodeManagers19renderTargetManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->renderTargetManager();
}

//  SceneManager *Qt3DRender::Render::NodeManagers::sceneManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SceneManager *ritual_ZNK10Qt3DRender6Render12NodeManagers12sceneManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->sceneManager();
}

//  AttachmentManager *Qt3DRender::Render::NodeManagers::attachmentManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::AttachmentManager *ritual_ZNK10Qt3DRender6Render12NodeManagers17attachmentManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->attachmentManager();
}

//  ParameterManager *Qt3DRender::Render::NodeManagers::parameterManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ParameterManager *ritual_ZNK10Qt3DRender6Render12NodeManagers16parameterManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->parameterManager();
}

//  ShaderDataManager *Qt3DRender::Render::NodeManagers::shaderDataManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ShaderDataManager *ritual_ZNK10Qt3DRender6Render12NodeManagers17shaderDataManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->shaderDataManager();
}

//  TextureImageManager
//      *Qt3DRender::Render::NodeManagers::textureImageManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TextureImageManager *ritual_ZNK10Qt3DRender6Render12NodeManagers19textureImageManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->textureImageManager();
}

//  BufferManager *Qt3DRender::Render::NodeManagers::bufferManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::BufferManager *ritual_ZNK10Qt3DRender6Render12NodeManagers13bufferManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->bufferManager();
}

//  AttributeManager *Qt3DRender::Render::NodeManagers::attributeManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::AttributeManager *ritual_ZNK10Qt3DRender6Render12NodeManagers16attributeManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->attributeManager();
}

//  GeometryManager *Qt3DRender::Render::NodeManagers::geometryManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::GeometryManager *ritual_ZNK10Qt3DRender6Render12NodeManagers15geometryManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->geometryManager();
}

//  GeometryRendererManager
//      *Qt3DRender::Render::NodeManagers::geometryRendererManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::GeometryRendererManager *ritual_ZNK10Qt3DRender6Render12NodeManagers23geometryRendererManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->geometryRendererManager();
}

//  ObjectPickerManager
//      *Qt3DRender::Render::NodeManagers::objectPickerManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ObjectPickerManager *ritual_ZNK10Qt3DRender6Render12NodeManagers19objectPickerManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->objectPickerManager();
}

//  RayCasterManager *Qt3DRender::Render::NodeManagers::rayCasterManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RayCasterManager *ritual_ZNK10Qt3DRender6Render12NodeManagers16rayCasterManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->rayCasterManager();
}

//  LightManager *Qt3DRender::Render::NodeManagers::lightManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LightManager *ritual_ZNK10Qt3DRender6Render12NodeManagers12lightManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->lightManager();
}

//  EnvironmentLightManager
//      *Qt3DRender::Render::NodeManagers::environmentLightManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EnvironmentLightManager *ritual_ZNK10Qt3DRender6Render12NodeManagers23environmentLightManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->environmentLightManager();
}

//  ComputeCommandManager
//      *Qt3DRender::Render::NodeManagers::computeJobManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ComputeCommandManager *ritual_ZNK10Qt3DRender6Render12NodeManagers17computeJobManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->computeJobManager();
}

//  RenderStateManager
//      *Qt3DRender::Render::NodeManagers::renderStateManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderStateManager *ritual_ZNK10Qt3DRender6Render12NodeManagers18renderStateManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->renderStateManager();
}

//  ArmatureManager *Qt3DRender::Render::NodeManagers::armatureManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ArmatureManager *ritual_ZNK10Qt3DRender6Render12NodeManagers15armatureManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->armatureManager();
}

//  SkeletonManager *Qt3DRender::Render::NodeManagers::skeletonManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SkeletonManager *ritual_ZNK10Qt3DRender6Render12NodeManagers15skeletonManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->skeletonManager();
}

//  JointManager *Qt3DRender::Render::NodeManagers::jointManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::JointManager *ritual_ZNK10Qt3DRender6Render12NodeManagers12jointManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->jointManager();
}

//  ShaderImageManager
//      *Qt3DRender::Render::NodeManagers::shaderImageManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ShaderImageManager *ritual_ZNK10Qt3DRender6Render12NodeManagers18shaderImageManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->shaderImageManager();
}

//  PickingProxyManager
//      *Qt3DRender::Render::NodeManagers::pickingProxyManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingProxyManager *ritual_ZNK10Qt3DRender6Render12NodeManagers19pickingProxyManagerEv(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->pickingProxyManager();
}

//  Qt3DRender::Render::EntityManager
//      *Qt3DRender::Render::NodeManagers::manager<Entity, EntityManager>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EntityManager * ritual_ZNK10Qt3DRender6Render12NodeManagers7managerINS0_6EntityENS0_13EntityManagerEEEPT0_v(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->manager<Qt3DRender::Render::Entity, Qt3DRender::Render::EntityManager>();
}

//  Qt3DRender::Render::MaterialManager
//      *Qt3DRender::Render::NodeManagers::manager<Material,
//      MaterialManager>() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::MaterialManager * ritual_ZNK10Qt3DRender6Render12NodeManagers7managerINS0_8MaterialENS0_15MaterialManagerEEEPT0_v(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->manager<Qt3DRender::Render::Material, Qt3DRender::Render::MaterialManager>();
}

//  Qt3DRender::Render::TextureManager
//      *Qt3DRender::Render::NodeManagers::manager<Texture, TextureManager>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TextureManager * ritual_ZNK10Qt3DRender6Render12NodeManagers7managerINS0_7TextureENS0_14TextureManagerEEEPT0_v(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->manager<Qt3DRender::Render::Texture, Qt3DRender::Render::TextureManager>();
}

//  Qt3DRender::Render::ShaderManager
//      *Qt3DRender::Render::NodeManagers::manager<Shader, ShaderManager>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ShaderManager * ritual_ZNK10Qt3DRender6Render12NodeManagers7managerINS0_6ShaderENS0_13ShaderManagerEEEPT0_v(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->manager<Qt3DRender::Render::Shader, Qt3DRender::Render::ShaderManager>();
}

//  Qt3DRender::Render::TransformManager
//      *Qt3DRender::Render::NodeManagers::manager<Transform,
//      TransformManager>() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TransformManager * ritual_ZNK10Qt3DRender6Render12NodeManagers7managerINS0_9TransformENS0_16TransformManagerEEEPT0_v(
    const Qt3DRender::Render::NodeManagers *self) {
  return self->manager<Qt3DRender::Render::Transform, Qt3DRender::Render::TransformManager>();
}

//  Qt3DRender::Render::Entity
//      *Qt3DRender::Render::NodeManagers::lookupResource<Qt3DRender::Render::Entity,
//      Qt3DRender::Render::EntityManager, Qt3DCore::QNodeId>(const
//      Qt3DCore::QNodeId &id) const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Entity * ritual_ZNK10Qt3DRender6Render12NodeManagers14lookupResourceINS0_6EntityENS0_13EntityManagerEN8Qt3DCore7QNodeIdEEEPT_RKT1_(
    const Qt3DRender::Render::NodeManagers *self,
    const Qt3DCore::QNodeId *id) {
  return self->lookupResource<Qt3DRender::Render::Entity, Qt3DRender::Render::EntityManager, Qt3DCore::QNodeId>(*id);
}

//  Qt3DCore::QHandle<Qt3DRender::Render::Entity>
//      Qt3DRender::Render::NodeManagers::lookupHandle<Qt3DRender::Render::Entity,
//      Qt3DRender::Render::EntityManager,
//      Qt3DCore::QHandle<Qt3DRender::Render::Entity>,
//      Qt3DCore::QNodeId>(const Qt3DCore::QNodeId &id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QHandle<Qt3DRender::Render::Entity> * ritual_ZNK10Qt3DRender6Render12NodeManagers12lookupHandleINS0_6EntityENS0_13EntityManagerEN8Qt3DCore7QHandleIS3_EENS5_7QNodeIdEEET1_RKT2_(
    const Qt3DRender::Render::NodeManagers *self,
    const Qt3DCore::QNodeId *id) {
  return new Qt3DCore::QHandle<Qt3DRender::Render::Entity>(self->lookupHandle<Qt3DRender::Render::Entity, Qt3DRender::Render::EntityManager, Qt3DCore::QHandle<Qt3DRender::Render::Entity>,
      Qt3DCore::QNodeId>(*id));
}

//  Qt3DRender::Render::Entity
//      *Qt3DRender::Render::NodeManagers::data<Qt3DRender::Render::Entity,
//      Qt3DRender::Render::EntityManager,
//      Qt3DCore::QHandle<Qt3DRender::Render::Entity>>(Qt3DCore::QHandle<Qt3DRender::Render::Entity>
//      handle)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Entity * ritual_ZN10Qt3DRender6Render12NodeManagers4dataINS0_6EntityENS0_13EntityManagerEN8Qt3DCore7QHandleIS3_EEEEPT_T1_(
    Qt3DRender::Render::NodeManagers *self,
    const Qt3DCore::QHandle<Qt3DRender::Render::Entity> *handle) {
  return self->data<Qt3DRender::Render::Entity, Qt3DRender::Render::EntityManager, Qt3DCore::QHandle<Qt3DRender::Render::Entity>>(*handle);
}

//  Qt3DRender::Render::Material
//      *Qt3DRender::Render::NodeManagers::lookupResource<Qt3DRender::Render::Material,
//      Qt3DRender::Render::MaterialManager, Qt3DCore::QNodeId>(const
//      Qt3DCore::QNodeId &id) const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Material * ritual_ZNK10Qt3DRender6Render12NodeManagers14lookupResourceINS0_8MaterialENS0_15MaterialManagerEN8Qt3DCore7QNodeIdEEEPT_RKT1_(
    const Qt3DRender::Render::NodeManagers *self,
    const Qt3DCore::QNodeId *id) {
  return self->lookupResource<Qt3DRender::Render::Material, Qt3DRender::Render::MaterialManager, Qt3DCore::QNodeId>(*id);
}

//  Qt3DCore::QHandle<Qt3DRender::Render::Material>
//      Qt3DRender::Render::NodeManagers::lookupHandle<Qt3DRender::Render::Material,
//      Qt3DRender::Render::MaterialManager,
//      Qt3DCore::QHandle<Qt3DRender::Render::Material>,
//      Qt3DCore::QNodeId>(const Qt3DCore::QNodeId &id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QHandle<Qt3DRender::Render::Material> * ritual_ZNK10Qt3DRender6Render12NodeManagers12lookupHandleINS0_8MaterialENS0_15MaterialManagerEN8Qt3DCore7QHandleIS3_EENS5_7QNodeIdEEET1_RKT2_(
    const Qt3DRender::Render::NodeManagers *self,
    const Qt3DCore::QNodeId *id) {
  return new Qt3DCore::QHandle<Qt3DRender::Render::Material>(self->lookupHandle<Qt3DRender::Render::Material, Qt3DRender::Render::MaterialManager, Qt3DCore::QHandle<Qt3DRender::Render::Material>,
      Qt3DCore::QNodeId>(*id));
}

//  Qt3DRender::Render::Material
//      *Qt3DRender::Render::NodeManagers::data<Qt3DRender::Render::Material,
//      Qt3DRender::Render::MaterialManager,
//      Qt3DCore::QHandle<Qt3DRender::Render::Material>>(Qt3DCore::QHandle<Qt3DRender::Render::Material>
//      handle)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Material * ritual_ZN10Qt3DRender6Render12NodeManagers4dataINS0_8MaterialENS0_15MaterialManagerEN8Qt3DCore7QHandleIS3_EEEEPT_T1_(
    Qt3DRender::Render::NodeManagers *self,
    const Qt3DCore::QHandle<Qt3DRender::Render::Material> *handle) {
  return self->data<Qt3DRender::Render::Material, Qt3DRender::Render::MaterialManager, Qt3DCore::QHandle<Qt3DRender::Render::Material>>(*handle);
}
