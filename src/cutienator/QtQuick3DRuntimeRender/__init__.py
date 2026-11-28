"""
The 'cutienator.QtQuick3DRuntimeRender' package provides the cute
classes of the part of Qt named QtQuick3DRuntimeRender, under the name
PySide6 has for it.

  from cutienator.QtQuick3DRuntimeRender import QSSGAllocateBufferFlags, QSSGCameraGlobalCalculationResult

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QSSGAllocateBufferFlags',
    'QSSGCameraGlobalCalculationResult',
    'QSSGCustomMaterialVariableSubstitution',
    'QSSGCustomShaderMetaData',
    'QSSGDefaultMaterialPreparationResult',
    'QSSGLayerRenderPreparationResultFlags',
    'QSSGLightmapBaker',
    'QSSGLightmapperOptions',
    'QSSGLineParticle',
    'QSSGMeshProcessingOptions',
    'QSSGOITRenderContext',
    'QSSGParticleAnimated',
    'QSSGParticleSimple',
    'QSSGPerFrameAllocator',
    'QSSGRenderCameraConfiguration',
    'QSSGRenderCameraData',
    'QSSGRenderCameraFieldOfView',
    'QSSGRenderGraphObject',
    'QSSGRenderImageTexture',
    'QSSGRenderImageTextureFlags',
    'QSSGRenderInstanceTableEntry',
    'QSSGRenderMesh',
    'QSSGRenderPickResult',
    'QSSGRenderSubset',
    'QSSGRenderableObjectFlags',
    'QSSGRhiDrawCallData',
    'QSSGRhiDrawCallDataKey',
    'QSSGRhiDummyTextureKey',
    'QSSGRhiGraphicsPipelineState',
    'QSSGRhiInstanceBufferData',
    'QSSGRhiParticleData',
    'QSSGRhiRenderableTexture',
    'QSSGRhiSamplerDescription',
    'QSSGRhiShaderUniform',
    'QSSGRhiShaderUniformArray',
    'QSSGRhiSortData',
    'QSSGRhiTexture',
    'QSSGShaderDefaultMaterialKeyProperties',
    'QSSGShaderDefine',
    'QSSGShaderDirectionalLightData',
    'QSSGShaderDirectionalLightsUniformData',
    'QSSGShaderFeatures',
    'QSSGShaderLight',
    'QSSGShaderLightData',
    'QSSGShaderLightsUniformData',
    'QSSGShaderParticleMaterialKeyProperties',
    'QSSGShaderReflectionProbe',
    'QSSGShadowMapEntry',
    'QSSGSkyIblFaceTargets',
    'QSSGSkyIblPrefilterTargets',
    'QSSGTextureData',
    'QSSGTriangleParticle',
    'QSSGUserShaderAugmentation',
    'QSSGPickResultProcessResult',
    'QSSGRenderCustomMaterial',
    'QSSGRenderDefaultMaterial',
    'QSSGRenderImage',
    'QSSGRenderMorphTarget',
    'QSSGRenderResourceLoader',
    'QSSGRhiInputAssemblerStatePrivate',
    'QSSGEffectSceneCacheKey',
    'QSSGRenderTextureData',
    'QSSGRenderableImage',
    'QSSGShaderCacheKey',
    'QSSGShaderKeyAlphaMode',
    'QSSGShaderKeyDiffuseModel',
    'QSSGShaderKeyImageMap',
    'QSSGShaderKeyPropertyBase',
    'QSSGShaderKeySpecularModel',
    'QSSGShaderKeyTextureChannel',
    'QSSGShaderKeyVertexAttribute',
    'QSSGInputUtil',
    'QSSGRenderPath',
    'QSSGRenderSkin',
    'QSSGShaderKeyBoolean',
    'QSSGShaderResourceMergeContext',
    'QSSGCommand',
    'QSSGLightmapLoader',
    'QSSGLightmapWriter',
    'QSSGLoadedTexture',
    'QSSGStageGeneratorBase',
    'QSSGAddShaderDefine',
    'QSSGAllocateBuffer',
    'QSSGAllocateTexture',
    'QSSGApplyBufferValue',
    'QSSGApplyInstanceValue',
    'QSSGApplyValue',
    'QSSGBindBuffer',
    'QSSGBindShader',
    'QSSGBindTarget',
    'QSSGColorAttachment',
    'QSSGDepthStencilAttachment',
    'QSSGFragmentShaderGenerator',
    'QSSGPipelineStateOverrideCommand',
    'QSSGRender',
    'QSSGRenderablesFilterCommand',
    'QSSGSubRenderPass',
    'QSSGVertexShaderGenerator',
    'QSSGDepthTextureAttachment',
    'QSSGCameraHelpers',
    'QSSGRenderInstanceTable',
    'QSSGClipPlane',
    'QSSGParticleBuffer',
    'QSSGRenderGeometry',
    'QSSGRenderRay',
    'QSSGRenderableObject',
    'QSSGClippingFrustum',
    'QSSGRenderableObjectHandle',
    'QSSGComputePipelineStateKey',
    'QSSGGraphicsPipelineStateKey',
    'QSSGRhiContext',
    'QSSGRhiShaderResourceBindingList',
    'QSSGReflectionMapEntry',
    'QSSGRhiBuffer',
    'QSSGRhiQuadRenderer',
    'QSSGFrameData',
    'QSSGRenderExtension',
    'QSSGModelContext',
    'QSSGRenderNode',
    'QSSGRenderItem2D',
    'QSSGRenderLayer',
    'QSSGRenderModel',
    'QSSGRenderCamera',
    'QSSGRenderer',
    'QSSGRhiShaderPipeline',
    'QSSGShaderCache',
    'QSSGShaderLibraryManager',
    'QSSGSubsetRenderable',
    'QSSGProgramGenerator',
    'QSSGRenderContextInterface',
    'QSSGRenderHelpers',
    'QSSGRenderRoot',
    'QSSGGlobalRenderNodeData',
    'QSSGLayerRenderData',
    'QSSGRenderUserPass',
    'QSSGBufferManager',
    'QSSGCustomMaterialSystem',
    'QSSGDebugDrawSystem',
    'QSSGRenderEffect',
    'QSSGRenderItem2DData',
    'QSSGRhiCubeRenderer',
    'QSSGBakedLightingModel',
    'QSSGBuiltInRhiShaderCache',
    'QSSGLayerRenderPreparationResult',
    'QSSGManagedRhiTexture',
    'QSSGUserRenderPassManager',
    'QSSGModelHelpers',
    'QSSGRenderDataHelpers',
    'QSSGRenderExtensionHelpers',
    'QSSGRenderJoint',
    'QSSGRenderLight',
    'QSSGRenderModelData',
    'QSSGRenderMotionVectorMap',
    'QSSGRenderParticles',
    'QSSGRenderPass',
    'QSSGRenderReflectionProbe',
    'QSSGRenderShadowMap',
    'QSSGRenderSkeleton',
    'QSSGRenderTextureProviderExtension',
    'QSSGRenderableNodeEntry',
    'QSSGRhiContextPrivate',
    'QSSGRhiContextStats',
    'QSSGRhiEffectSystem',
    'QSSGRhiGraphicsPipelineStatePrivate',
    'QSSGShaderMaterialAdapter',
    'DebugDrawPass',
    'DepthMapPass',
    'InfiniteGridPass',
    'Item2DPass',
    'MotionVectorMapPass',
    'NormalPass',
    'OITCompositePass',
    'OITRenderPass',
    'OpaquePass',
    'QSSGLightmapper',
    'QSSGMaterialVertexPipeline',
    'QSSGParticlesRenderable',
    'QSSGRenderReflectionMap',
    'QSSGRhiRenderableTextureV2',
    'QSSGShaderCustomMaterialAdapter',
    'QSSGShaderDefaultMaterialAdapter',
    'QSSGShaderKeyShadowSoftness',
    'ReflectionMapPass',
    'SSAOMapPass',
    'ScreenMapPass',
    'ScreenReflectionPass',
    'ShadowMapPass',
    'SkyMaterialBackgroundPass',
    'SkyMaterialPass',
    'SkyboxCubeMapPass',
    'SkyboxPass',
    'TransparentPass',
    'UserExtensionPass',
    'UserRenderPass',
    'ZPrePassPass',
    'QSSGMaterialShaderGenerator',
    'QSSGParticleRenderer',
    'QSSGRenderSkyMaterial',
    'QSSGRenderSkyMaterialManager',
    'QSSGRendererPrivate',
    'QSSGRenderableObjectList',
    'QSSGRenderGraphObjectUtils',
    'QSSGRenderResult',
    'QSSGRenderShaderMetadata',
    'QtQuick3DEditorHelpers',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_s_s_g_allocate_buffer_flags import QSSGAllocateBufferFlags
  from ._q_s_s_g_camera_global_calculation_result import QSSGCameraGlobalCalculationResult
  from ._q_s_s_g_custom_material_variable_substitution import QSSGCustomMaterialVariableSubstitution
  from ._q_s_s_g_custom_shader_meta_data import QSSGCustomShaderMetaData
  from ._q_s_s_g_default_material_preparation_result import QSSGDefaultMaterialPreparationResult
  from ._q_s_s_g_layer_render_preparation_result_flags import QSSGLayerRenderPreparationResultFlags
  from ._q_s_s_g_lightmap_baker import QSSGLightmapBaker
  from ._q_s_s_g_lightmapper_options import QSSGLightmapperOptions
  from ._q_s_s_g_line_particle import QSSGLineParticle
  from ._q_s_s_g_mesh_processing_options import QSSGMeshProcessingOptions
  from ._q_s_s_g_o_i_t_render_context import QSSGOITRenderContext
  from ._q_s_s_g_particle_animated import QSSGParticleAnimated
  from ._q_s_s_g_particle_simple import QSSGParticleSimple
  from ._q_s_s_g_per_frame_allocator import QSSGPerFrameAllocator
  from ._q_s_s_g_render_camera_configuration import QSSGRenderCameraConfiguration
  from ._q_s_s_g_render_camera_data import QSSGRenderCameraData
  from ._q_s_s_g_render_camera_field_of_view import QSSGRenderCameraFieldOfView
  from ._q_s_s_g_render_graph_object import QSSGRenderGraphObject
  from ._q_s_s_g_render_image_texture import QSSGRenderImageTexture
  from ._q_s_s_g_render_image_texture_flags import QSSGRenderImageTextureFlags
  from ._q_s_s_g_render_instance_table_entry import QSSGRenderInstanceTableEntry
  from ._q_s_s_g_render_mesh import QSSGRenderMesh
  from ._q_s_s_g_render_pick_result import QSSGRenderPickResult
  from ._q_s_s_g_render_subset import QSSGRenderSubset
  from ._q_s_s_g_renderable_object_flags import QSSGRenderableObjectFlags
  from ._q_s_s_g_rhi_draw_call_data import QSSGRhiDrawCallData
  from ._q_s_s_g_rhi_draw_call_data_key import QSSGRhiDrawCallDataKey
  from ._q_s_s_g_rhi_dummy_texture_key import QSSGRhiDummyTextureKey
  from ._q_s_s_g_rhi_graphics_pipeline_state import QSSGRhiGraphicsPipelineState
  from ._q_s_s_g_rhi_instance_buffer_data import QSSGRhiInstanceBufferData
  from ._q_s_s_g_rhi_particle_data import QSSGRhiParticleData
  from ._q_s_s_g_rhi_renderable_texture import QSSGRhiRenderableTexture
  from ._q_s_s_g_rhi_sampler_description import QSSGRhiSamplerDescription
  from ._q_s_s_g_rhi_shader_uniform import QSSGRhiShaderUniform
  from ._q_s_s_g_rhi_shader_uniform_array import QSSGRhiShaderUniformArray
  from ._q_s_s_g_rhi_sort_data import QSSGRhiSortData
  from ._q_s_s_g_rhi_texture import QSSGRhiTexture
  from ._q_s_s_g_shader_default_material_key_properties import QSSGShaderDefaultMaterialKeyProperties
  from ._q_s_s_g_shader_define import QSSGShaderDefine
  from ._q_s_s_g_shader_directional_light_data import QSSGShaderDirectionalLightData
  from ._q_s_s_g_shader_directional_lights_uniform_data import QSSGShaderDirectionalLightsUniformData
  from ._q_s_s_g_shader_features import QSSGShaderFeatures
  from ._q_s_s_g_shader_light import QSSGShaderLight
  from ._q_s_s_g_shader_light_data import QSSGShaderLightData
  from ._q_s_s_g_shader_lights_uniform_data import QSSGShaderLightsUniformData
  from ._q_s_s_g_shader_particle_material_key_properties import QSSGShaderParticleMaterialKeyProperties
  from ._q_s_s_g_shader_reflection_probe import QSSGShaderReflectionProbe
  from ._q_s_s_g_shadow_map_entry import QSSGShadowMapEntry
  from ._q_s_s_g_sky_ibl_face_targets import QSSGSkyIblFaceTargets
  from ._q_s_s_g_sky_ibl_prefilter_targets import QSSGSkyIblPrefilterTargets
  from ._q_s_s_g_texture_data import QSSGTextureData
  from ._q_s_s_g_triangle_particle import QSSGTriangleParticle
  from ._q_s_s_g_user_shader_augmentation import QSSGUserShaderAugmentation
  from ._q_s_s_g_pick_result_process_result import QSSGPickResultProcessResult
  from ._q_s_s_g_render_custom_material import QSSGRenderCustomMaterial
  from ._q_s_s_g_render_default_material import QSSGRenderDefaultMaterial
  from ._q_s_s_g_render_image import QSSGRenderImage
  from ._q_s_s_g_render_morph_target import QSSGRenderMorphTarget
  from ._q_s_s_g_render_resource_loader import QSSGRenderResourceLoader
  from ._q_s_s_g_rhi_input_assembler_state_private import QSSGRhiInputAssemblerStatePrivate
  from ._q_s_s_g_effect_scene_cache_key import QSSGEffectSceneCacheKey
  from ._q_s_s_g_render_texture_data import QSSGRenderTextureData
  from ._q_s_s_g_renderable_image import QSSGRenderableImage
  from ._q_s_s_g_shader_cache_key import QSSGShaderCacheKey
  from ._q_s_s_g_shader_key_alpha_mode import QSSGShaderKeyAlphaMode
  from ._q_s_s_g_shader_key_diffuse_model import QSSGShaderKeyDiffuseModel
  from ._q_s_s_g_shader_key_image_map import QSSGShaderKeyImageMap
  from ._q_s_s_g_shader_key_property_base import QSSGShaderKeyPropertyBase
  from ._q_s_s_g_shader_key_specular_model import QSSGShaderKeySpecularModel
  from ._q_s_s_g_shader_key_texture_channel import QSSGShaderKeyTextureChannel
  from ._q_s_s_g_shader_key_vertex_attribute import QSSGShaderKeyVertexAttribute
  from ._q_s_s_g_input_util import QSSGInputUtil
  from ._q_s_s_g_render_path import QSSGRenderPath
  from ._q_s_s_g_render_skin import QSSGRenderSkin
  from ._q_s_s_g_shader_key_boolean import QSSGShaderKeyBoolean
  from ._q_s_s_g_shader_resource_merge_context import QSSGShaderResourceMergeContext
  from ._q_s_s_g_command import QSSGCommand
  from ._q_s_s_g_lightmap_loader import QSSGLightmapLoader
  from ._q_s_s_g_lightmap_writer import QSSGLightmapWriter
  from ._q_s_s_g_loaded_texture import QSSGLoadedTexture
  from ._q_s_s_g_stage_generator_base import QSSGStageGeneratorBase
  from ._q_s_s_g_add_shader_define import QSSGAddShaderDefine
  from ._q_s_s_g_allocate_buffer import QSSGAllocateBuffer
  from ._q_s_s_g_allocate_texture import QSSGAllocateTexture
  from ._q_s_s_g_apply_buffer_value import QSSGApplyBufferValue
  from ._q_s_s_g_apply_instance_value import QSSGApplyInstanceValue
  from ._q_s_s_g_apply_value import QSSGApplyValue
  from ._q_s_s_g_bind_buffer import QSSGBindBuffer
  from ._q_s_s_g_bind_shader import QSSGBindShader
  from ._q_s_s_g_bind_target import QSSGBindTarget
  from ._q_s_s_g_color_attachment import QSSGColorAttachment
  from ._q_s_s_g_depth_stencil_attachment import QSSGDepthStencilAttachment
  from ._q_s_s_g_fragment_shader_generator import QSSGFragmentShaderGenerator
  from ._q_s_s_g_pipeline_state_override_command import QSSGPipelineStateOverrideCommand
  from ._q_s_s_g_render import QSSGRender
  from ._q_s_s_g_renderables_filter_command import QSSGRenderablesFilterCommand
  from ._q_s_s_g_sub_render_pass import QSSGSubRenderPass
  from ._q_s_s_g_vertex_shader_generator import QSSGVertexShaderGenerator
  from ._q_s_s_g_depth_texture_attachment import QSSGDepthTextureAttachment
  from ._q_s_s_g_camera_helpers import QSSGCameraHelpers
  from ._q_s_s_g_render_instance_table import QSSGRenderInstanceTable
  from ._q_s_s_g_clip_plane import QSSGClipPlane
  from ._q_s_s_g_particle_buffer import QSSGParticleBuffer
  from ._q_s_s_g_render_geometry import QSSGRenderGeometry
  from ._q_s_s_g_render_ray import QSSGRenderRay
  from ._q_s_s_g_renderable_object import QSSGRenderableObject
  from ._q_s_s_g_clipping_frustum import QSSGClippingFrustum
  from ._q_s_s_g_renderable_object_handle import QSSGRenderableObjectHandle
  from ._q_s_s_g_compute_pipeline_state_key import QSSGComputePipelineStateKey
  from ._q_s_s_g_graphics_pipeline_state_key import QSSGGraphicsPipelineStateKey
  from ._q_s_s_g_rhi_context import QSSGRhiContext
  from ._q_s_s_g_rhi_shader_resource_binding_list import QSSGRhiShaderResourceBindingList
  from ._q_s_s_g_reflection_map_entry import QSSGReflectionMapEntry
  from ._q_s_s_g_rhi_buffer import QSSGRhiBuffer
  from ._q_s_s_g_rhi_quad_renderer import QSSGRhiQuadRenderer
  from ._q_s_s_g_frame_data import QSSGFrameData
  from ._q_s_s_g_render_extension import QSSGRenderExtension
  from ._q_s_s_g_model_context import QSSGModelContext
  from ._q_s_s_g_render_node import QSSGRenderNode
  from ._q_s_s_g_render_item2_d import QSSGRenderItem2D
  from ._q_s_s_g_render_layer import QSSGRenderLayer
  from ._q_s_s_g_render_model import QSSGRenderModel
  from ._q_s_s_g_render_camera import QSSGRenderCamera
  from ._q_s_s_g_renderer import QSSGRenderer
  from ._q_s_s_g_rhi_shader_pipeline import QSSGRhiShaderPipeline
  from ._q_s_s_g_shader_cache import QSSGShaderCache
  from ._q_s_s_g_shader_library_manager import QSSGShaderLibraryManager
  from ._q_s_s_g_subset_renderable import QSSGSubsetRenderable
  from ._q_s_s_g_program_generator import QSSGProgramGenerator
  from ._q_s_s_g_render_context_interface import QSSGRenderContextInterface
  from ._q_s_s_g_render_helpers import QSSGRenderHelpers
  from ._q_s_s_g_render_root import QSSGRenderRoot
  from ._q_s_s_g_global_render_node_data import QSSGGlobalRenderNodeData
  from ._q_s_s_g_layer_render_data import QSSGLayerRenderData
  from ._q_s_s_g_render_user_pass import QSSGRenderUserPass
  from ._q_s_s_g_buffer_manager import QSSGBufferManager
  from ._q_s_s_g_custom_material_system import QSSGCustomMaterialSystem
  from ._q_s_s_g_debug_draw_system import QSSGDebugDrawSystem
  from ._q_s_s_g_render_effect import QSSGRenderEffect
  from ._q_s_s_g_render_item2_d_data import QSSGRenderItem2DData
  from ._q_s_s_g_rhi_cube_renderer import QSSGRhiCubeRenderer
  from ._q_s_s_g_baked_lighting_model import QSSGBakedLightingModel
  from ._q_s_s_g_built_in_rhi_shader_cache import QSSGBuiltInRhiShaderCache
  from ._q_s_s_g_layer_render_preparation_result import QSSGLayerRenderPreparationResult
  from ._q_s_s_g_managed_rhi_texture import QSSGManagedRhiTexture
  from ._q_s_s_g_user_render_pass_manager import QSSGUserRenderPassManager
  from ._q_s_s_g_model_helpers import QSSGModelHelpers
  from ._q_s_s_g_render_data_helpers import QSSGRenderDataHelpers
  from ._q_s_s_g_render_extension_helpers import QSSGRenderExtensionHelpers
  from ._q_s_s_g_render_joint import QSSGRenderJoint
  from ._q_s_s_g_render_light import QSSGRenderLight
  from ._q_s_s_g_render_model_data import QSSGRenderModelData
  from ._q_s_s_g_render_motion_vector_map import QSSGRenderMotionVectorMap
  from ._q_s_s_g_render_particles import QSSGRenderParticles
  from ._q_s_s_g_render_pass import QSSGRenderPass
  from ._q_s_s_g_render_reflection_probe import QSSGRenderReflectionProbe
  from ._q_s_s_g_render_shadow_map import QSSGRenderShadowMap
  from ._q_s_s_g_render_skeleton import QSSGRenderSkeleton
  from ._q_s_s_g_render_texture_provider_extension import QSSGRenderTextureProviderExtension
  from ._q_s_s_g_renderable_node_entry import QSSGRenderableNodeEntry
  from ._q_s_s_g_rhi_context_private import QSSGRhiContextPrivate
  from ._q_s_s_g_rhi_context_stats import QSSGRhiContextStats
  from ._q_s_s_g_rhi_effect_system import QSSGRhiEffectSystem
  from ._q_s_s_g_rhi_graphics_pipeline_state_private import QSSGRhiGraphicsPipelineStatePrivate
  from ._q_s_s_g_shader_material_adapter import QSSGShaderMaterialAdapter
  from ._debug_draw_pass import DebugDrawPass
  from ._depth_map_pass import DepthMapPass
  from ._infinite_grid_pass import InfiniteGridPass
  from ._item2_d_pass import Item2DPass
  from ._motion_vector_map_pass import MotionVectorMapPass
  from ._normal_pass import NormalPass
  from ._o_i_t_composite_pass import OITCompositePass
  from ._o_i_t_render_pass import OITRenderPass
  from ._opaque_pass import OpaquePass
  from ._q_s_s_g_lightmapper import QSSGLightmapper
  from ._q_s_s_g_material_vertex_pipeline import QSSGMaterialVertexPipeline
  from ._q_s_s_g_particles_renderable import QSSGParticlesRenderable
  from ._q_s_s_g_render_reflection_map import QSSGRenderReflectionMap
  from ._q_s_s_g_rhi_renderable_texture_v2 import QSSGRhiRenderableTextureV2
  from ._q_s_s_g_shader_custom_material_adapter import QSSGShaderCustomMaterialAdapter
  from ._q_s_s_g_shader_default_material_adapter import QSSGShaderDefaultMaterialAdapter
  from ._q_s_s_g_shader_key_shadow_softness import QSSGShaderKeyShadowSoftness
  from ._reflection_map_pass import ReflectionMapPass
  from ._s_s_a_o_map_pass import SSAOMapPass
  from ._screen_map_pass import ScreenMapPass
  from ._screen_reflection_pass import ScreenReflectionPass
  from ._shadow_map_pass import ShadowMapPass
  from ._sky_material_background_pass import SkyMaterialBackgroundPass
  from ._sky_material_pass import SkyMaterialPass
  from ._skybox_cube_map_pass import SkyboxCubeMapPass
  from ._skybox_pass import SkyboxPass
  from ._transparent_pass import TransparentPass
  from ._user_extension_pass import UserExtensionPass
  from ._user_render_pass import UserRenderPass
  from ._z_pre_pass_pass import ZPrePassPass
  from ._q_s_s_g_material_shader_generator import QSSGMaterialShaderGenerator
  from ._q_s_s_g_particle_renderer import QSSGParticleRenderer
  from ._q_s_s_g_render_sky_material import QSSGRenderSkyMaterial
  from ._q_s_s_g_render_sky_material_manager import QSSGRenderSkyMaterialManager
  from ._q_s_s_g_renderer_private import QSSGRendererPrivate
  from ._q_s_s_g_renderable_object_handle import QSSGRenderableObjectList
  from . import QSSGRenderGraphObjectUtils
  from . import QSSGRenderResult
  from . import QSSGRenderShaderMetadata
  from . import QtQuick3DEditorHelpers
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QSSGAllocateBufferFlags': '_q_s_s_g_allocate_buffer_flags',
      'QSSGCameraGlobalCalculationResult': '_q_s_s_g_camera_global_calculation_result',
      'QSSGCustomMaterialVariableSubstitution': '_q_s_s_g_custom_material_variable_substitution',
      'QSSGCustomShaderMetaData': '_q_s_s_g_custom_shader_meta_data',
      'QSSGDefaultMaterialPreparationResult': '_q_s_s_g_default_material_preparation_result',
      'QSSGLayerRenderPreparationResultFlags': '_q_s_s_g_layer_render_preparation_result_flags',
      'QSSGLightmapBaker': '_q_s_s_g_lightmap_baker',
      'QSSGLightmapperOptions': '_q_s_s_g_lightmapper_options',
      'QSSGLineParticle': '_q_s_s_g_line_particle',
      'QSSGMeshProcessingOptions': '_q_s_s_g_mesh_processing_options',
      'QSSGOITRenderContext': '_q_s_s_g_o_i_t_render_context',
      'QSSGParticleAnimated': '_q_s_s_g_particle_animated',
      'QSSGParticleSimple': '_q_s_s_g_particle_simple',
      'QSSGPerFrameAllocator': '_q_s_s_g_per_frame_allocator',
      'QSSGRenderCameraConfiguration': '_q_s_s_g_render_camera_configuration',
      'QSSGRenderCameraData': '_q_s_s_g_render_camera_data',
      'QSSGRenderCameraFieldOfView': '_q_s_s_g_render_camera_field_of_view',
      'QSSGRenderGraphObject': '_q_s_s_g_render_graph_object',
      'QSSGRenderImageTexture': '_q_s_s_g_render_image_texture',
      'QSSGRenderImageTextureFlags': '_q_s_s_g_render_image_texture_flags',
      'QSSGRenderInstanceTableEntry': '_q_s_s_g_render_instance_table_entry',
      'QSSGRenderMesh': '_q_s_s_g_render_mesh',
      'QSSGRenderPickResult': '_q_s_s_g_render_pick_result',
      'QSSGRenderSubset': '_q_s_s_g_render_subset',
      'QSSGRenderableObjectFlags': '_q_s_s_g_renderable_object_flags',
      'QSSGRhiDrawCallData': '_q_s_s_g_rhi_draw_call_data',
      'QSSGRhiDrawCallDataKey': '_q_s_s_g_rhi_draw_call_data_key',
      'QSSGRhiDummyTextureKey': '_q_s_s_g_rhi_dummy_texture_key',
      'QSSGRhiGraphicsPipelineState': '_q_s_s_g_rhi_graphics_pipeline_state',
      'QSSGRhiInstanceBufferData': '_q_s_s_g_rhi_instance_buffer_data',
      'QSSGRhiParticleData': '_q_s_s_g_rhi_particle_data',
      'QSSGRhiRenderableTexture': '_q_s_s_g_rhi_renderable_texture',
      'QSSGRhiSamplerDescription': '_q_s_s_g_rhi_sampler_description',
      'QSSGRhiShaderUniform': '_q_s_s_g_rhi_shader_uniform',
      'QSSGRhiShaderUniformArray': '_q_s_s_g_rhi_shader_uniform_array',
      'QSSGRhiSortData': '_q_s_s_g_rhi_sort_data',
      'QSSGRhiTexture': '_q_s_s_g_rhi_texture',
      'QSSGShaderDefaultMaterialKeyProperties': '_q_s_s_g_shader_default_material_key_properties',
      'QSSGShaderDefine': '_q_s_s_g_shader_define',
      'QSSGShaderDirectionalLightData': '_q_s_s_g_shader_directional_light_data',
      'QSSGShaderDirectionalLightsUniformData': '_q_s_s_g_shader_directional_lights_uniform_data',
      'QSSGShaderFeatures': '_q_s_s_g_shader_features',
      'QSSGShaderLight': '_q_s_s_g_shader_light',
      'QSSGShaderLightData': '_q_s_s_g_shader_light_data',
      'QSSGShaderLightsUniformData': '_q_s_s_g_shader_lights_uniform_data',
      'QSSGShaderParticleMaterialKeyProperties': '_q_s_s_g_shader_particle_material_key_properties',
      'QSSGShaderReflectionProbe': '_q_s_s_g_shader_reflection_probe',
      'QSSGShadowMapEntry': '_q_s_s_g_shadow_map_entry',
      'QSSGSkyIblFaceTargets': '_q_s_s_g_sky_ibl_face_targets',
      'QSSGSkyIblPrefilterTargets': '_q_s_s_g_sky_ibl_prefilter_targets',
      'QSSGTextureData': '_q_s_s_g_texture_data',
      'QSSGTriangleParticle': '_q_s_s_g_triangle_particle',
      'QSSGUserShaderAugmentation': '_q_s_s_g_user_shader_augmentation',
      'QSSGPickResultProcessResult': '_q_s_s_g_pick_result_process_result',
      'QSSGRenderCustomMaterial': '_q_s_s_g_render_custom_material',
      'QSSGRenderDefaultMaterial': '_q_s_s_g_render_default_material',
      'QSSGRenderImage': '_q_s_s_g_render_image',
      'QSSGRenderMorphTarget': '_q_s_s_g_render_morph_target',
      'QSSGRenderResourceLoader': '_q_s_s_g_render_resource_loader',
      'QSSGRhiInputAssemblerStatePrivate': '_q_s_s_g_rhi_input_assembler_state_private',
      'QSSGEffectSceneCacheKey': '_q_s_s_g_effect_scene_cache_key',
      'QSSGRenderTextureData': '_q_s_s_g_render_texture_data',
      'QSSGRenderableImage': '_q_s_s_g_renderable_image',
      'QSSGShaderCacheKey': '_q_s_s_g_shader_cache_key',
      'QSSGShaderKeyAlphaMode': '_q_s_s_g_shader_key_alpha_mode',
      'QSSGShaderKeyDiffuseModel': '_q_s_s_g_shader_key_diffuse_model',
      'QSSGShaderKeyImageMap': '_q_s_s_g_shader_key_image_map',
      'QSSGShaderKeyPropertyBase': '_q_s_s_g_shader_key_property_base',
      'QSSGShaderKeySpecularModel': '_q_s_s_g_shader_key_specular_model',
      'QSSGShaderKeyTextureChannel': '_q_s_s_g_shader_key_texture_channel',
      'QSSGShaderKeyVertexAttribute': '_q_s_s_g_shader_key_vertex_attribute',
      'QSSGInputUtil': '_q_s_s_g_input_util',
      'QSSGRenderPath': '_q_s_s_g_render_path',
      'QSSGRenderSkin': '_q_s_s_g_render_skin',
      'QSSGShaderKeyBoolean': '_q_s_s_g_shader_key_boolean',
      'QSSGShaderResourceMergeContext': '_q_s_s_g_shader_resource_merge_context',
      'QSSGCommand': '_q_s_s_g_command',
      'QSSGLightmapLoader': '_q_s_s_g_lightmap_loader',
      'QSSGLightmapWriter': '_q_s_s_g_lightmap_writer',
      'QSSGLoadedTexture': '_q_s_s_g_loaded_texture',
      'QSSGStageGeneratorBase': '_q_s_s_g_stage_generator_base',
      'QSSGAddShaderDefine': '_q_s_s_g_add_shader_define',
      'QSSGAllocateBuffer': '_q_s_s_g_allocate_buffer',
      'QSSGAllocateTexture': '_q_s_s_g_allocate_texture',
      'QSSGApplyBufferValue': '_q_s_s_g_apply_buffer_value',
      'QSSGApplyInstanceValue': '_q_s_s_g_apply_instance_value',
      'QSSGApplyValue': '_q_s_s_g_apply_value',
      'QSSGBindBuffer': '_q_s_s_g_bind_buffer',
      'QSSGBindShader': '_q_s_s_g_bind_shader',
      'QSSGBindTarget': '_q_s_s_g_bind_target',
      'QSSGColorAttachment': '_q_s_s_g_color_attachment',
      'QSSGDepthStencilAttachment': '_q_s_s_g_depth_stencil_attachment',
      'QSSGFragmentShaderGenerator': '_q_s_s_g_fragment_shader_generator',
      'QSSGPipelineStateOverrideCommand': '_q_s_s_g_pipeline_state_override_command',
      'QSSGRender': '_q_s_s_g_render',
      'QSSGRenderablesFilterCommand': '_q_s_s_g_renderables_filter_command',
      'QSSGSubRenderPass': '_q_s_s_g_sub_render_pass',
      'QSSGVertexShaderGenerator': '_q_s_s_g_vertex_shader_generator',
      'QSSGDepthTextureAttachment': '_q_s_s_g_depth_texture_attachment',
      'QSSGCameraHelpers': '_q_s_s_g_camera_helpers',
      'QSSGRenderInstanceTable': '_q_s_s_g_render_instance_table',
      'QSSGClipPlane': '_q_s_s_g_clip_plane',
      'QSSGParticleBuffer': '_q_s_s_g_particle_buffer',
      'QSSGRenderGeometry': '_q_s_s_g_render_geometry',
      'QSSGRenderRay': '_q_s_s_g_render_ray',
      'QSSGRenderableObject': '_q_s_s_g_renderable_object',
      'QSSGClippingFrustum': '_q_s_s_g_clipping_frustum',
      'QSSGRenderableObjectHandle': '_q_s_s_g_renderable_object_handle',
      'QSSGComputePipelineStateKey': '_q_s_s_g_compute_pipeline_state_key',
      'QSSGGraphicsPipelineStateKey': '_q_s_s_g_graphics_pipeline_state_key',
      'QSSGRhiContext': '_q_s_s_g_rhi_context',
      'QSSGRhiShaderResourceBindingList': '_q_s_s_g_rhi_shader_resource_binding_list',
      'QSSGReflectionMapEntry': '_q_s_s_g_reflection_map_entry',
      'QSSGRhiBuffer': '_q_s_s_g_rhi_buffer',
      'QSSGRhiQuadRenderer': '_q_s_s_g_rhi_quad_renderer',
      'QSSGFrameData': '_q_s_s_g_frame_data',
      'QSSGRenderExtension': '_q_s_s_g_render_extension',
      'QSSGModelContext': '_q_s_s_g_model_context',
      'QSSGRenderNode': '_q_s_s_g_render_node',
      'QSSGRenderItem2D': '_q_s_s_g_render_item2_d',
      'QSSGRenderLayer': '_q_s_s_g_render_layer',
      'QSSGRenderModel': '_q_s_s_g_render_model',
      'QSSGRenderCamera': '_q_s_s_g_render_camera',
      'QSSGRenderer': '_q_s_s_g_renderer',
      'QSSGRhiShaderPipeline': '_q_s_s_g_rhi_shader_pipeline',
      'QSSGShaderCache': '_q_s_s_g_shader_cache',
      'QSSGShaderLibraryManager': '_q_s_s_g_shader_library_manager',
      'QSSGSubsetRenderable': '_q_s_s_g_subset_renderable',
      'QSSGProgramGenerator': '_q_s_s_g_program_generator',
      'QSSGRenderContextInterface': '_q_s_s_g_render_context_interface',
      'QSSGRenderHelpers': '_q_s_s_g_render_helpers',
      'QSSGRenderRoot': '_q_s_s_g_render_root',
      'QSSGGlobalRenderNodeData': '_q_s_s_g_global_render_node_data',
      'QSSGLayerRenderData': '_q_s_s_g_layer_render_data',
      'QSSGRenderUserPass': '_q_s_s_g_render_user_pass',
      'QSSGBufferManager': '_q_s_s_g_buffer_manager',
      'QSSGCustomMaterialSystem': '_q_s_s_g_custom_material_system',
      'QSSGDebugDrawSystem': '_q_s_s_g_debug_draw_system',
      'QSSGRenderEffect': '_q_s_s_g_render_effect',
      'QSSGRenderItem2DData': '_q_s_s_g_render_item2_d_data',
      'QSSGRhiCubeRenderer': '_q_s_s_g_rhi_cube_renderer',
      'QSSGBakedLightingModel': '_q_s_s_g_baked_lighting_model',
      'QSSGBuiltInRhiShaderCache': '_q_s_s_g_built_in_rhi_shader_cache',
      'QSSGLayerRenderPreparationResult': '_q_s_s_g_layer_render_preparation_result',
      'QSSGManagedRhiTexture': '_q_s_s_g_managed_rhi_texture',
      'QSSGUserRenderPassManager': '_q_s_s_g_user_render_pass_manager',
      'QSSGModelHelpers': '_q_s_s_g_model_helpers',
      'QSSGRenderDataHelpers': '_q_s_s_g_render_data_helpers',
      'QSSGRenderExtensionHelpers': '_q_s_s_g_render_extension_helpers',
      'QSSGRenderJoint': '_q_s_s_g_render_joint',
      'QSSGRenderLight': '_q_s_s_g_render_light',
      'QSSGRenderModelData': '_q_s_s_g_render_model_data',
      'QSSGRenderMotionVectorMap': '_q_s_s_g_render_motion_vector_map',
      'QSSGRenderParticles': '_q_s_s_g_render_particles',
      'QSSGRenderPass': '_q_s_s_g_render_pass',
      'QSSGRenderReflectionProbe': '_q_s_s_g_render_reflection_probe',
      'QSSGRenderShadowMap': '_q_s_s_g_render_shadow_map',
      'QSSGRenderSkeleton': '_q_s_s_g_render_skeleton',
      'QSSGRenderTextureProviderExtension': '_q_s_s_g_render_texture_provider_extension',
      'QSSGRenderableNodeEntry': '_q_s_s_g_renderable_node_entry',
      'QSSGRhiContextPrivate': '_q_s_s_g_rhi_context_private',
      'QSSGRhiContextStats': '_q_s_s_g_rhi_context_stats',
      'QSSGRhiEffectSystem': '_q_s_s_g_rhi_effect_system',
      'QSSGRhiGraphicsPipelineStatePrivate': '_q_s_s_g_rhi_graphics_pipeline_state_private',
      'QSSGShaderMaterialAdapter': '_q_s_s_g_shader_material_adapter',
      'DebugDrawPass': '_debug_draw_pass',
      'DepthMapPass': '_depth_map_pass',
      'InfiniteGridPass': '_infinite_grid_pass',
      'Item2DPass': '_item2_d_pass',
      'MotionVectorMapPass': '_motion_vector_map_pass',
      'NormalPass': '_normal_pass',
      'OITCompositePass': '_o_i_t_composite_pass',
      'OITRenderPass': '_o_i_t_render_pass',
      'OpaquePass': '_opaque_pass',
      'QSSGLightmapper': '_q_s_s_g_lightmapper',
      'QSSGMaterialVertexPipeline': '_q_s_s_g_material_vertex_pipeline',
      'QSSGParticlesRenderable': '_q_s_s_g_particles_renderable',
      'QSSGRenderReflectionMap': '_q_s_s_g_render_reflection_map',
      'QSSGRhiRenderableTextureV2': '_q_s_s_g_rhi_renderable_texture_v2',
      'QSSGShaderCustomMaterialAdapter': '_q_s_s_g_shader_custom_material_adapter',
      'QSSGShaderDefaultMaterialAdapter': '_q_s_s_g_shader_default_material_adapter',
      'QSSGShaderKeyShadowSoftness': '_q_s_s_g_shader_key_shadow_softness',
      'ReflectionMapPass': '_reflection_map_pass',
      'SSAOMapPass': '_s_s_a_o_map_pass',
      'ScreenMapPass': '_screen_map_pass',
      'ScreenReflectionPass': '_screen_reflection_pass',
      'ShadowMapPass': '_shadow_map_pass',
      'SkyMaterialBackgroundPass': '_sky_material_background_pass',
      'SkyMaterialPass': '_sky_material_pass',
      'SkyboxCubeMapPass': '_skybox_cube_map_pass',
      'SkyboxPass': '_skybox_pass',
      'TransparentPass': '_transparent_pass',
      'UserExtensionPass': '_user_extension_pass',
      'UserRenderPass': '_user_render_pass',
      'ZPrePassPass': '_z_pre_pass_pass',
      'QSSGMaterialShaderGenerator': '_q_s_s_g_material_shader_generator',
      'QSSGParticleRenderer': '_q_s_s_g_particle_renderer',
      'QSSGRenderSkyMaterial': '_q_s_s_g_render_sky_material',
      'QSSGRenderSkyMaterialManager': '_q_s_s_g_render_sky_material_manager',
      'QSSGRendererPrivate': '_q_s_s_g_renderer_private',
      'QSSGRenderableObjectList': '_q_s_s_g_renderable_object_handle',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QSSGRenderGraphObjectUtils', 'QSSGRenderResult', 'QSSGRenderShaderMetadata', 'QtQuick3DEditorHelpers',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuick3DRuntimeRender import QSSGRenderableObjectList'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
