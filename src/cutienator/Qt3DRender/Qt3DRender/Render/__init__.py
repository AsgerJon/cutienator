"""
The namespace 'Qt3DRender::Render' of Qt, a package of 'cutienator.Qt3DRender':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DRender import Qt3DRender
  Qt3DRender.Render.AlphaCoverage

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from ..._qt3_d_render__render import Render as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'AlphaCoverage',
    'AlphaFunc',
    'ArmatureManager',
    'Attachment',
    'AttachmentManager',
    'AttachmentPack',
    'AttributeManager',
    'BlendEquation',
    'BlendEquationArguments',
    'BufferInfo',
    'CameraManager',
    'ClipPlane',
    'ColorMask',
    'ComputeCommandManager',
    'CullFace',
    'DepthRange',
    'DepthTest',
    'Dithering',
    'EffectManager',
    'EntityAccumulator',
    'EntityManager',
    'EntityVisitor',
    'EnvironmentLightManager',
    'FilterKeyManager',
    'FrameGraphVisitor',
    'FrontFace',
    'GeometryFunctorResult',
    'GeometryManager',
    'JointInfo',
    'LayerManager',
    'LevelOfDetailManager',
    'LightManager',
    'LightSource',
    'LineWidth',
    'MSAAEnabled',
    'MaterialManager',
    'MatrixManager',
    'NoDepthMask',
    'NodeManagers',
    'ObjectPickerManager',
    'ParameterInfo',
    'ParameterManager',
    'PickingProxyManager',
    'PointSize',
    'PolygonOffset',
    'RasterMode',
    'RayCasterManager',
    'RenderPassManager',
    'RenderPassParameterData',
    'RenderStateImpl',
    'RenderStateManager',
    'RenderStateSet',
    'ScissorTest',
    'SeamlessCubemap',
    'ShaderBuilderManager',
    'ShaderBuilderUpdate',
    'ShaderDataManager',
    'ShaderImageManager',
    'SkeletonData',
    'SkeletonManager',
    'StateVariant',
    'StencilMask',
    'StencilOp',
    'StencilTest',
    'TextureImageManager',
    'TextureParameters',
    'TextureProperties',
    'TransformManager',
    'BufferFunctor',
    'BufferManager',
    'CameraLensFunctor',
    'ExpandBoundingVolumeJob',
    'FilterCompatibleTechniqueJob',
    'FilterLayerEntityJob',
    'FilterProximityDistanceJob',
    'FrameCleanupJob',
    'FrameGraphManager',
    'FrustumCullingJob',
    'GeometryRendererFunctor',
    'GeometryRendererManager',
    'JointFunctor',
    'JointManager',
    'LightGatherer',
    'LoadGeometryJob',
    'MaterialParameterGathererJob',
    'ParameterPack',
    'PickingProxyFunctor',
    'RenderEntityFunctor',
    'RenderLightFunctor',
    'RenderSceneFunctor',
    'RenderSettingsFunctor',
    'RenderShaderDataFunctor',
    'RenderTargetFunctor',
    'RenderTargetManager',
    'ShaderFunctor',
    'ShaderManager',
    'SkeletonFunctor',
    'TechniqueFunctor',
    'TechniqueManager',
    'TextureFunctor',
    'TextureImageFunctor',
    'TextureManager',
    'TriangleBoundingVolume',
    'UpdateEntityLayersJob',
    'UpdateLevelOfDetailJob',
    'UpdateShaderDataTransformJob',
    'UpdateSkinningPaletteJob',
    'UpdateTreeEnabledJob',
    'UpdateWorldBoundingVolumeJob',
    'UpdateWorldTransformJob',
    'SendBufferCaptureJob',
    'Sphere',
    'CoordinateReader',
    'QRenderPluginFactory',
    'QRendererPluginFactory',
    'RenderBackendResourceAccessor',
    'UniformBlockValueBuilder',
    'LoadSceneJob',
    'ResourceAccessor',
    'StringToInt',
    'AbstractPickingJob',
    'OffscreenSurfaceHelper',
    'PickEventFilter',
    'QRenderPlugin',
    'QRenderPluginFactoryIf',
    'QRendererPlugin',
    'SceneDownloader',
    'BackendNode',
    'CalculateBoundingVolumeJob',
    'EntityPrivate',
    'PlatformSurfaceFilter',
    'RayCastingJob',
    'SurfaceLocker',
    'Armature',
    'Attribute',
    'Buffer',
    'ComputeCommand',
    'Effect',
    'Entity',
    'EnvironmentLight',
    'FilterKey',
    'FrameGraphNode',
    'GLTFSkeletonLoader',
    'GeometryRenderer',
    'Joint',
    'Layer',
    'LevelOfDetail',
    'Light',
    'Material',
    'ObjectPicker',
    'Parameter',
    'PickingProxy',
    'PointsVisitor',
    'RayCaster',
    'RenderPass',
    'RenderSettings',
    'RenderStateNode',
    'RenderTarget',
    'RenderTargetOutput',
    'Scene',
    'SceneManager',
    'SegmentsVisitor',
    'Shader',
    'ShaderBuilder',
    'ShaderData',
    'ShaderImage',
    'Technique',
    'Texture',
    'TextureImage',
    'Transform',
    'TrianglesVisitor',
    'VSyncFrameAdvanceService',
    'BlitFramebuffer',
    'BufferCapture',
    'CameraLens',
    'CameraSelector',
    'ClearBuffers',
    'ComputeFilteredBoundingVolumeJob',
    'DebugOverlay',
    'DispatchCompute',
    'FrustumCulling',
    'Geometry',
    'LayerFilterNode',
    'LoadSceneJobPrivate',
    'LoadSkeletonJob',
    'MemoryBarrier',
    'NoDraw',
    'NoPicking',
    'ProximityFilter',
    'RenderCapture',
    'RenderPassFilter',
    'RenderSurfaceSelector',
    'RenderTargetSelector',
    'SetFence',
    'SortPolicy',
    'StateSetNode',
    'SubtreeEnabler',
    'TechniqueFilter',
    'UniformValue',
    'ViewportNode',
    'WaitFence',
    'Skeleton',
    'PickBoundingVolumeJob',
    'AbstractRenderer',
    'JobTypes',
    'PickingUtils',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._qt3_d_render__render__alpha_coverage import AlphaCoverage
  from ..._qt3_d_render__render__alpha_func import AlphaFunc
  from ..._qt3_d_render__render__armature_manager import ArmatureManager
  from ..._qt3_d_render__render__attachment import Attachment
  from ..._qt3_d_render__render__attachment_manager import AttachmentManager
  from ..._qt3_d_render__render__attachment_pack import AttachmentPack
  from ..._qt3_d_render__render__attribute_manager import AttributeManager
  from ..._qt3_d_render__render__blend_equation import BlendEquation
  from ..._qt3_d_render__render__blend_equation_arguments import BlendEquationArguments
  from ..._qt3_d_render__render__buffer_info import BufferInfo
  from ..._qt3_d_render__render__camera_manager import CameraManager
  from ..._qt3_d_render__render__clip_plane import ClipPlane
  from ..._qt3_d_render__render__color_mask import ColorMask
  from ..._qt3_d_render__render__compute_command_manager import ComputeCommandManager
  from ..._qt3_d_render__render__cull_face import CullFace
  from ..._qt3_d_render__render__depth_range import DepthRange
  from ..._qt3_d_render__render__depth_test import DepthTest
  from ..._qt3_d_render__render__dithering import Dithering
  from ..._qt3_d_render__render__effect_manager import EffectManager
  from ..._qt3_d_render__render__entity_accumulator import EntityAccumulator
  from ..._qt3_d_render__render__entity_manager import EntityManager
  from ..._qt3_d_render__render__entity_visitor import EntityVisitor
  from ..._qt3_d_render__render__environment_light_manager import EnvironmentLightManager
  from ..._qt3_d_render__render__filter_key_manager import FilterKeyManager
  from ..._qt3_d_render__render__frame_graph_visitor import FrameGraphVisitor
  from ..._qt3_d_render__render__front_face import FrontFace
  from ..._qt3_d_render__render__geometry_functor_result import GeometryFunctorResult
  from ..._qt3_d_render__render__geometry_manager import GeometryManager
  from ..._qt3_d_render__render__joint_info import JointInfo
  from ..._qt3_d_render__render__layer_manager import LayerManager
  from ..._qt3_d_render__render__level_of_detail_manager import LevelOfDetailManager
  from ..._qt3_d_render__render__light_manager import LightManager
  from ..._qt3_d_render__render__light_source import LightSource
  from ..._qt3_d_render__render__line_width import LineWidth
  from ..._qt3_d_render__render__m_s_a_a_enabled import MSAAEnabled
  from ..._qt3_d_render__render__material_manager import MaterialManager
  from ..._qt3_d_render__render__matrix_manager import MatrixManager
  from ..._qt3_d_render__render__no_depth_mask import NoDepthMask
  from ..._qt3_d_render__render__node_managers import NodeManagers
  from ..._qt3_d_render__render__object_picker_manager import ObjectPickerManager
  from ..._qt3_d_render__render__parameter_info import ParameterInfo
  from ..._qt3_d_render__render__parameter_manager import ParameterManager
  from ..._qt3_d_render__render__picking_proxy_manager import PickingProxyManager
  from ..._qt3_d_render__render__point_size import PointSize
  from ..._qt3_d_render__render__polygon_offset import PolygonOffset
  from ..._qt3_d_render__render__raster_mode import RasterMode
  from ..._qt3_d_render__render__ray_caster_manager import RayCasterManager
  from ..._qt3_d_render__render__render_pass_manager import RenderPassManager
  from ..._qt3_d_render__render__render_pass_parameter_data import RenderPassParameterData
  from ..._qt3_d_render__render__render_state_impl import RenderStateImpl
  from ..._qt3_d_render__render__render_state_manager import RenderStateManager
  from ..._qt3_d_render__render__render_state_set import RenderStateSet
  from ..._qt3_d_render__render__scissor_test import ScissorTest
  from ..._qt3_d_render__render__seamless_cubemap import SeamlessCubemap
  from ..._qt3_d_render__render__shader_builder_manager import ShaderBuilderManager
  from ..._qt3_d_render__render__shader_builder_update import ShaderBuilderUpdate
  from ..._qt3_d_render__render__shader_data_manager import ShaderDataManager
  from ..._qt3_d_render__render__shader_image_manager import ShaderImageManager
  from ..._qt3_d_render__render__skeleton_data import SkeletonData
  from ..._qt3_d_render__render__skeleton_manager import SkeletonManager
  from ..._qt3_d_render__render__state_variant import StateVariant
  from ..._qt3_d_render__render__stencil_mask import StencilMask
  from ..._qt3_d_render__render__stencil_op import StencilOp
  from ..._qt3_d_render__render__stencil_test import StencilTest
  from ..._qt3_d_render__render__texture_image_manager import TextureImageManager
  from ..._qt3_d_render__render__texture_parameters import TextureParameters
  from ..._qt3_d_render__render__texture_properties import TextureProperties
  from ..._qt3_d_render__render__transform_manager import TransformManager
  from ..._qt3_d_render__render__buffer_functor import BufferFunctor
  from ..._qt3_d_render__render__buffer_manager import BufferManager
  from ..._qt3_d_render__render__camera_lens_functor import CameraLensFunctor
  from ..._qt3_d_render__render__expand_bounding_volume_job import ExpandBoundingVolumeJob
  from ..._qt3_d_render__render__filter_compatible_technique_job import FilterCompatibleTechniqueJob
  from ..._qt3_d_render__render__filter_layer_entity_job import FilterLayerEntityJob
  from ..._qt3_d_render__render__filter_proximity_distance_job import FilterProximityDistanceJob
  from ..._qt3_d_render__render__frame_cleanup_job import FrameCleanupJob
  from ..._qt3_d_render__render__frame_graph_manager import FrameGraphManager
  from ..._qt3_d_render__render__frustum_culling_job import FrustumCullingJob
  from ..._qt3_d_render__render__geometry_renderer_functor import GeometryRendererFunctor
  from ..._qt3_d_render__render__geometry_renderer_manager import GeometryRendererManager
  from ..._qt3_d_render__render__joint_functor import JointFunctor
  from ..._qt3_d_render__render__joint_manager import JointManager
  from ..._qt3_d_render__render__light_gatherer import LightGatherer
  from ..._qt3_d_render__render__load_geometry_job import LoadGeometryJob
  from ..._qt3_d_render__render__material_parameter_gatherer_job import MaterialParameterGathererJob
  from ..._qt3_d_render__render__parameter_pack import ParameterPack
  from ..._qt3_d_render__render__picking_proxy_functor import PickingProxyFunctor
  from ..._qt3_d_render__render__render_entity_functor import RenderEntityFunctor
  from ..._qt3_d_render__render__render_light_functor import RenderLightFunctor
  from ..._qt3_d_render__render__render_scene_functor import RenderSceneFunctor
  from ..._qt3_d_render__render__render_settings_functor import RenderSettingsFunctor
  from ..._qt3_d_render__render__render_shader_data_functor import RenderShaderDataFunctor
  from ..._qt3_d_render__render__render_target_functor import RenderTargetFunctor
  from ..._qt3_d_render__render__render_target_manager import RenderTargetManager
  from ..._qt3_d_render__render__shader_functor import ShaderFunctor
  from ..._qt3_d_render__render__shader_manager import ShaderManager
  from ..._qt3_d_render__render__skeleton_functor import SkeletonFunctor
  from ..._qt3_d_render__render__technique_functor import TechniqueFunctor
  from ..._qt3_d_render__render__technique_manager import TechniqueManager
  from ..._qt3_d_render__render__texture_functor import TextureFunctor
  from ..._qt3_d_render__render__texture_image_functor import TextureImageFunctor
  from ..._qt3_d_render__render__texture_manager import TextureManager
  from ..._qt3_d_render__render__triangle_bounding_volume import TriangleBoundingVolume
  from ..._qt3_d_render__render__update_entity_layers_job import UpdateEntityLayersJob
  from ..._qt3_d_render__render__update_level_of_detail_job import UpdateLevelOfDetailJob
  from ..._qt3_d_render__render__update_shader_data_transform_job import UpdateShaderDataTransformJob
  from ..._qt3_d_render__render__update_skinning_palette_job import UpdateSkinningPaletteJob
  from ..._qt3_d_render__render__update_tree_enabled_job import UpdateTreeEnabledJob
  from ..._qt3_d_render__render__update_world_bounding_volume_job import UpdateWorldBoundingVolumeJob
  from ..._qt3_d_render__render__update_world_transform_job import UpdateWorldTransformJob
  from ..._qt3_d_render__render__send_buffer_capture_job import SendBufferCaptureJob
  from ..._qt3_d_render__render__sphere import Sphere
  from ..._qt3_d_render__render__coordinate_reader import CoordinateReader
  from ..._qt3_d_render__render__q_render_plugin_factory import QRenderPluginFactory
  from ..._qt3_d_render__render__q_renderer_plugin_factory import QRendererPluginFactory
  from ..._qt3_d_render__render__render_backend_resource_accessor import RenderBackendResourceAccessor
  from ..._qt3_d_render__render__uniform_block_value_builder import UniformBlockValueBuilder
  from ..._qt3_d_render__render__load_scene_job import LoadSceneJob
  from ..._qt3_d_render__render__resource_accessor import ResourceAccessor
  from ..._qt3_d_render__render__string_to_int import StringToInt
  from ..._qt3_d_render__render__abstract_picking_job import AbstractPickingJob
  from ..._qt3_d_render__render__offscreen_surface_helper import OffscreenSurfaceHelper
  from ..._qt3_d_render__render__pick_event_filter import PickEventFilter
  from ..._qt3_d_render__render__q_render_plugin import QRenderPlugin
  from ..._qt3_d_render__render__q_render_plugin_factory_if import QRenderPluginFactoryIf
  from ..._qt3_d_render__render__q_renderer_plugin import QRendererPlugin
  from ..._qt3_d_render__render__scene_downloader import SceneDownloader
  from ..._qt3_d_render__render__backend_node import BackendNode
  from ..._qt3_d_render__render__calculate_bounding_volume_job import CalculateBoundingVolumeJob
  from ..._qt3_d_render__render__entity_private import EntityPrivate
  from ..._qt3_d_render__render__platform_surface_filter import PlatformSurfaceFilter
  from ..._qt3_d_render__render__ray_casting_job import RayCastingJob
  from ..._qt3_d_render__render__surface_locker import SurfaceLocker
  from ..._qt3_d_render__render__armature import Armature
  from ..._qt3_d_render__render__attribute import Attribute
  from ..._qt3_d_render__render__buffer import Buffer
  from ..._qt3_d_render__render__compute_command import ComputeCommand
  from ..._qt3_d_render__render__effect import Effect
  from ..._qt3_d_render__render__entity import Entity
  from ..._qt3_d_render__render__environment_light import EnvironmentLight
  from ..._qt3_d_render__render__filter_key import FilterKey
  from ..._qt3_d_render__render__frame_graph_node import FrameGraphNode
  from ..._qt3_d_render__render__g_l_t_f_skeleton_loader import GLTFSkeletonLoader
  from ..._qt3_d_render__render__geometry_renderer import GeometryRenderer
  from ..._qt3_d_render__render__joint import Joint
  from ..._qt3_d_render__render__layer import Layer
  from ..._qt3_d_render__render__level_of_detail import LevelOfDetail
  from ..._qt3_d_render__render__light import Light
  from ..._qt3_d_render__render__material import Material
  from ..._qt3_d_render__render__object_picker import ObjectPicker
  from ..._qt3_d_render__render__parameter import Parameter
  from ..._qt3_d_render__render__picking_proxy import PickingProxy
  from ..._qt3_d_render__render__points_visitor import PointsVisitor
  from ..._qt3_d_render__render__ray_caster import RayCaster
  from ..._qt3_d_render__render__render_pass import RenderPass
  from ..._qt3_d_render__render__render_settings import RenderSettings
  from ..._qt3_d_render__render__render_state_node import RenderStateNode
  from ..._qt3_d_render__render__render_target import RenderTarget
  from ..._qt3_d_render__render__render_target_output import RenderTargetOutput
  from ..._qt3_d_render__render__scene import Scene
  from ..._qt3_d_render__render__scene_manager import SceneManager
  from ..._qt3_d_render__render__segments_visitor import SegmentsVisitor
  from ..._qt3_d_render__render__shader import Shader
  from ..._qt3_d_render__render__shader_builder import ShaderBuilder
  from ..._qt3_d_render__render__shader_data import ShaderData
  from ..._qt3_d_render__render__shader_image import ShaderImage
  from ..._qt3_d_render__render__technique import Technique
  from ..._qt3_d_render__render__texture import Texture
  from ..._qt3_d_render__render__texture_image import TextureImage
  from ..._qt3_d_render__render__transform import Transform
  from ..._qt3_d_render__render__triangles_visitor import TrianglesVisitor
  from ..._qt3_d_render__render__v_sync_frame_advance_service import VSyncFrameAdvanceService
  from ..._qt3_d_render__render__blit_framebuffer import BlitFramebuffer
  from ..._qt3_d_render__render__buffer_capture import BufferCapture
  from ..._qt3_d_render__render__camera_lens import CameraLens
  from ..._qt3_d_render__render__camera_selector import CameraSelector
  from ..._qt3_d_render__render__clear_buffers import ClearBuffers
  from ..._qt3_d_render__render__compute_filtered_bounding_volume_job import ComputeFilteredBoundingVolumeJob
  from ..._qt3_d_render__render__debug_overlay import DebugOverlay
  from ..._qt3_d_render__render__dispatch_compute import DispatchCompute
  from ..._qt3_d_render__render__frustum_culling import FrustumCulling
  from ..._qt3_d_render__render__geometry import Geometry
  from ..._qt3_d_render__render__layer_filter_node import LayerFilterNode
  from ..._qt3_d_render__render__load_scene_job_private import LoadSceneJobPrivate
  from ..._qt3_d_render__render__load_skeleton_job import LoadSkeletonJob
  from ..._qt3_d_render__render__memory_barrier import MemoryBarrier
  from ..._qt3_d_render__render__no_draw import NoDraw
  from ..._qt3_d_render__render__no_picking import NoPicking
  from ..._qt3_d_render__render__proximity_filter import ProximityFilter
  from ..._qt3_d_render__render__render_capture import RenderCapture
  from ..._qt3_d_render__render__render_pass_filter import RenderPassFilter
  from ..._qt3_d_render__render__render_surface_selector import RenderSurfaceSelector
  from ..._qt3_d_render__render__render_target_selector import RenderTargetSelector
  from ..._qt3_d_render__render__set_fence import SetFence
  from ..._qt3_d_render__render__sort_policy import SortPolicy
  from ..._qt3_d_render__render__state_set_node import StateSetNode
  from ..._qt3_d_render__render__subtree_enabler import SubtreeEnabler
  from ..._qt3_d_render__render__technique_filter import TechniqueFilter
  from ..._qt3_d_render__render__uniform_value import UniformValue
  from ..._qt3_d_render__render__viewport_node import ViewportNode
  from ..._qt3_d_render__render__wait_fence import WaitFence
  from ..._qt3_d_render__render__skeleton import Skeleton
  from ..._qt3_d_render__render__pick_bounding_volume_job import PickBoundingVolumeJob
  from ..._qt3_d_render__render__abstract_renderer import AbstractRenderer
  from . import JobTypes
  from . import PickingUtils
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'AlphaCoverage': '_qt3_d_render__render__alpha_coverage',
      'AlphaFunc': '_qt3_d_render__render__alpha_func',
      'ArmatureManager': '_qt3_d_render__render__armature_manager',
      'Attachment': '_qt3_d_render__render__attachment',
      'AttachmentManager': '_qt3_d_render__render__attachment_manager',
      'AttachmentPack': '_qt3_d_render__render__attachment_pack',
      'AttributeManager': '_qt3_d_render__render__attribute_manager',
      'BlendEquation': '_qt3_d_render__render__blend_equation',
      'BlendEquationArguments': '_qt3_d_render__render__blend_equation_arguments',
      'BufferInfo': '_qt3_d_render__render__buffer_info',
      'CameraManager': '_qt3_d_render__render__camera_manager',
      'ClipPlane': '_qt3_d_render__render__clip_plane',
      'ColorMask': '_qt3_d_render__render__color_mask',
      'ComputeCommandManager': '_qt3_d_render__render__compute_command_manager',
      'CullFace': '_qt3_d_render__render__cull_face',
      'DepthRange': '_qt3_d_render__render__depth_range',
      'DepthTest': '_qt3_d_render__render__depth_test',
      'Dithering': '_qt3_d_render__render__dithering',
      'EffectManager': '_qt3_d_render__render__effect_manager',
      'EntityAccumulator': '_qt3_d_render__render__entity_accumulator',
      'EntityManager': '_qt3_d_render__render__entity_manager',
      'EntityVisitor': '_qt3_d_render__render__entity_visitor',
      'EnvironmentLightManager': '_qt3_d_render__render__environment_light_manager',
      'FilterKeyManager': '_qt3_d_render__render__filter_key_manager',
      'FrameGraphVisitor': '_qt3_d_render__render__frame_graph_visitor',
      'FrontFace': '_qt3_d_render__render__front_face',
      'GeometryFunctorResult': '_qt3_d_render__render__geometry_functor_result',
      'GeometryManager': '_qt3_d_render__render__geometry_manager',
      'JointInfo': '_qt3_d_render__render__joint_info',
      'LayerManager': '_qt3_d_render__render__layer_manager',
      'LevelOfDetailManager': '_qt3_d_render__render__level_of_detail_manager',
      'LightManager': '_qt3_d_render__render__light_manager',
      'LightSource': '_qt3_d_render__render__light_source',
      'LineWidth': '_qt3_d_render__render__line_width',
      'MSAAEnabled': '_qt3_d_render__render__m_s_a_a_enabled',
      'MaterialManager': '_qt3_d_render__render__material_manager',
      'MatrixManager': '_qt3_d_render__render__matrix_manager',
      'NoDepthMask': '_qt3_d_render__render__no_depth_mask',
      'NodeManagers': '_qt3_d_render__render__node_managers',
      'ObjectPickerManager': '_qt3_d_render__render__object_picker_manager',
      'ParameterInfo': '_qt3_d_render__render__parameter_info',
      'ParameterManager': '_qt3_d_render__render__parameter_manager',
      'PickingProxyManager': '_qt3_d_render__render__picking_proxy_manager',
      'PointSize': '_qt3_d_render__render__point_size',
      'PolygonOffset': '_qt3_d_render__render__polygon_offset',
      'RasterMode': '_qt3_d_render__render__raster_mode',
      'RayCasterManager': '_qt3_d_render__render__ray_caster_manager',
      'RenderPassManager': '_qt3_d_render__render__render_pass_manager',
      'RenderPassParameterData': '_qt3_d_render__render__render_pass_parameter_data',
      'RenderStateImpl': '_qt3_d_render__render__render_state_impl',
      'RenderStateManager': '_qt3_d_render__render__render_state_manager',
      'RenderStateSet': '_qt3_d_render__render__render_state_set',
      'ScissorTest': '_qt3_d_render__render__scissor_test',
      'SeamlessCubemap': '_qt3_d_render__render__seamless_cubemap',
      'ShaderBuilderManager': '_qt3_d_render__render__shader_builder_manager',
      'ShaderBuilderUpdate': '_qt3_d_render__render__shader_builder_update',
      'ShaderDataManager': '_qt3_d_render__render__shader_data_manager',
      'ShaderImageManager': '_qt3_d_render__render__shader_image_manager',
      'SkeletonData': '_qt3_d_render__render__skeleton_data',
      'SkeletonManager': '_qt3_d_render__render__skeleton_manager',
      'StateVariant': '_qt3_d_render__render__state_variant',
      'StencilMask': '_qt3_d_render__render__stencil_mask',
      'StencilOp': '_qt3_d_render__render__stencil_op',
      'StencilTest': '_qt3_d_render__render__stencil_test',
      'TextureImageManager': '_qt3_d_render__render__texture_image_manager',
      'TextureParameters': '_qt3_d_render__render__texture_parameters',
      'TextureProperties': '_qt3_d_render__render__texture_properties',
      'TransformManager': '_qt3_d_render__render__transform_manager',
      'BufferFunctor': '_qt3_d_render__render__buffer_functor',
      'BufferManager': '_qt3_d_render__render__buffer_manager',
      'CameraLensFunctor': '_qt3_d_render__render__camera_lens_functor',
      'ExpandBoundingVolumeJob': '_qt3_d_render__render__expand_bounding_volume_job',
      'FilterCompatibleTechniqueJob': '_qt3_d_render__render__filter_compatible_technique_job',
      'FilterLayerEntityJob': '_qt3_d_render__render__filter_layer_entity_job',
      'FilterProximityDistanceJob': '_qt3_d_render__render__filter_proximity_distance_job',
      'FrameCleanupJob': '_qt3_d_render__render__frame_cleanup_job',
      'FrameGraphManager': '_qt3_d_render__render__frame_graph_manager',
      'FrustumCullingJob': '_qt3_d_render__render__frustum_culling_job',
      'GeometryRendererFunctor': '_qt3_d_render__render__geometry_renderer_functor',
      'GeometryRendererManager': '_qt3_d_render__render__geometry_renderer_manager',
      'JointFunctor': '_qt3_d_render__render__joint_functor',
      'JointManager': '_qt3_d_render__render__joint_manager',
      'LightGatherer': '_qt3_d_render__render__light_gatherer',
      'LoadGeometryJob': '_qt3_d_render__render__load_geometry_job',
      'MaterialParameterGathererJob': '_qt3_d_render__render__material_parameter_gatherer_job',
      'ParameterPack': '_qt3_d_render__render__parameter_pack',
      'PickingProxyFunctor': '_qt3_d_render__render__picking_proxy_functor',
      'RenderEntityFunctor': '_qt3_d_render__render__render_entity_functor',
      'RenderLightFunctor': '_qt3_d_render__render__render_light_functor',
      'RenderSceneFunctor': '_qt3_d_render__render__render_scene_functor',
      'RenderSettingsFunctor': '_qt3_d_render__render__render_settings_functor',
      'RenderShaderDataFunctor': '_qt3_d_render__render__render_shader_data_functor',
      'RenderTargetFunctor': '_qt3_d_render__render__render_target_functor',
      'RenderTargetManager': '_qt3_d_render__render__render_target_manager',
      'ShaderFunctor': '_qt3_d_render__render__shader_functor',
      'ShaderManager': '_qt3_d_render__render__shader_manager',
      'SkeletonFunctor': '_qt3_d_render__render__skeleton_functor',
      'TechniqueFunctor': '_qt3_d_render__render__technique_functor',
      'TechniqueManager': '_qt3_d_render__render__technique_manager',
      'TextureFunctor': '_qt3_d_render__render__texture_functor',
      'TextureImageFunctor': '_qt3_d_render__render__texture_image_functor',
      'TextureManager': '_qt3_d_render__render__texture_manager',
      'TriangleBoundingVolume': '_qt3_d_render__render__triangle_bounding_volume',
      'UpdateEntityLayersJob': '_qt3_d_render__render__update_entity_layers_job',
      'UpdateLevelOfDetailJob': '_qt3_d_render__render__update_level_of_detail_job',
      'UpdateShaderDataTransformJob': '_qt3_d_render__render__update_shader_data_transform_job',
      'UpdateSkinningPaletteJob': '_qt3_d_render__render__update_skinning_palette_job',
      'UpdateTreeEnabledJob': '_qt3_d_render__render__update_tree_enabled_job',
      'UpdateWorldBoundingVolumeJob': '_qt3_d_render__render__update_world_bounding_volume_job',
      'UpdateWorldTransformJob': '_qt3_d_render__render__update_world_transform_job',
      'SendBufferCaptureJob': '_qt3_d_render__render__send_buffer_capture_job',
      'Sphere': '_qt3_d_render__render__sphere',
      'CoordinateReader': '_qt3_d_render__render__coordinate_reader',
      'QRenderPluginFactory': '_qt3_d_render__render__q_render_plugin_factory',
      'QRendererPluginFactory': '_qt3_d_render__render__q_renderer_plugin_factory',
      'RenderBackendResourceAccessor': '_qt3_d_render__render__render_backend_resource_accessor',
      'UniformBlockValueBuilder': '_qt3_d_render__render__uniform_block_value_builder',
      'LoadSceneJob': '_qt3_d_render__render__load_scene_job',
      'ResourceAccessor': '_qt3_d_render__render__resource_accessor',
      'StringToInt': '_qt3_d_render__render__string_to_int',
      'AbstractPickingJob': '_qt3_d_render__render__abstract_picking_job',
      'OffscreenSurfaceHelper': '_qt3_d_render__render__offscreen_surface_helper',
      'PickEventFilter': '_qt3_d_render__render__pick_event_filter',
      'QRenderPlugin': '_qt3_d_render__render__q_render_plugin',
      'QRenderPluginFactoryIf': '_qt3_d_render__render__q_render_plugin_factory_if',
      'QRendererPlugin': '_qt3_d_render__render__q_renderer_plugin',
      'SceneDownloader': '_qt3_d_render__render__scene_downloader',
      'BackendNode': '_qt3_d_render__render__backend_node',
      'CalculateBoundingVolumeJob': '_qt3_d_render__render__calculate_bounding_volume_job',
      'EntityPrivate': '_qt3_d_render__render__entity_private',
      'PlatformSurfaceFilter': '_qt3_d_render__render__platform_surface_filter',
      'RayCastingJob': '_qt3_d_render__render__ray_casting_job',
      'SurfaceLocker': '_qt3_d_render__render__surface_locker',
      'Armature': '_qt3_d_render__render__armature',
      'Attribute': '_qt3_d_render__render__attribute',
      'Buffer': '_qt3_d_render__render__buffer',
      'ComputeCommand': '_qt3_d_render__render__compute_command',
      'Effect': '_qt3_d_render__render__effect',
      'Entity': '_qt3_d_render__render__entity',
      'EnvironmentLight': '_qt3_d_render__render__environment_light',
      'FilterKey': '_qt3_d_render__render__filter_key',
      'FrameGraphNode': '_qt3_d_render__render__frame_graph_node',
      'GLTFSkeletonLoader': '_qt3_d_render__render__g_l_t_f_skeleton_loader',
      'GeometryRenderer': '_qt3_d_render__render__geometry_renderer',
      'Joint': '_qt3_d_render__render__joint',
      'Layer': '_qt3_d_render__render__layer',
      'LevelOfDetail': '_qt3_d_render__render__level_of_detail',
      'Light': '_qt3_d_render__render__light',
      'Material': '_qt3_d_render__render__material',
      'ObjectPicker': '_qt3_d_render__render__object_picker',
      'Parameter': '_qt3_d_render__render__parameter',
      'PickingProxy': '_qt3_d_render__render__picking_proxy',
      'PointsVisitor': '_qt3_d_render__render__points_visitor',
      'RayCaster': '_qt3_d_render__render__ray_caster',
      'RenderPass': '_qt3_d_render__render__render_pass',
      'RenderSettings': '_qt3_d_render__render__render_settings',
      'RenderStateNode': '_qt3_d_render__render__render_state_node',
      'RenderTarget': '_qt3_d_render__render__render_target',
      'RenderTargetOutput': '_qt3_d_render__render__render_target_output',
      'Scene': '_qt3_d_render__render__scene',
      'SceneManager': '_qt3_d_render__render__scene_manager',
      'SegmentsVisitor': '_qt3_d_render__render__segments_visitor',
      'Shader': '_qt3_d_render__render__shader',
      'ShaderBuilder': '_qt3_d_render__render__shader_builder',
      'ShaderData': '_qt3_d_render__render__shader_data',
      'ShaderImage': '_qt3_d_render__render__shader_image',
      'Technique': '_qt3_d_render__render__technique',
      'Texture': '_qt3_d_render__render__texture',
      'TextureImage': '_qt3_d_render__render__texture_image',
      'Transform': '_qt3_d_render__render__transform',
      'TrianglesVisitor': '_qt3_d_render__render__triangles_visitor',
      'VSyncFrameAdvanceService': '_qt3_d_render__render__v_sync_frame_advance_service',
      'BlitFramebuffer': '_qt3_d_render__render__blit_framebuffer',
      'BufferCapture': '_qt3_d_render__render__buffer_capture',
      'CameraLens': '_qt3_d_render__render__camera_lens',
      'CameraSelector': '_qt3_d_render__render__camera_selector',
      'ClearBuffers': '_qt3_d_render__render__clear_buffers',
      'ComputeFilteredBoundingVolumeJob': '_qt3_d_render__render__compute_filtered_bounding_volume_job',
      'DebugOverlay': '_qt3_d_render__render__debug_overlay',
      'DispatchCompute': '_qt3_d_render__render__dispatch_compute',
      'FrustumCulling': '_qt3_d_render__render__frustum_culling',
      'Geometry': '_qt3_d_render__render__geometry',
      'LayerFilterNode': '_qt3_d_render__render__layer_filter_node',
      'LoadSceneJobPrivate': '_qt3_d_render__render__load_scene_job_private',
      'LoadSkeletonJob': '_qt3_d_render__render__load_skeleton_job',
      'MemoryBarrier': '_qt3_d_render__render__memory_barrier',
      'NoDraw': '_qt3_d_render__render__no_draw',
      'NoPicking': '_qt3_d_render__render__no_picking',
      'ProximityFilter': '_qt3_d_render__render__proximity_filter',
      'RenderCapture': '_qt3_d_render__render__render_capture',
      'RenderPassFilter': '_qt3_d_render__render__render_pass_filter',
      'RenderSurfaceSelector': '_qt3_d_render__render__render_surface_selector',
      'RenderTargetSelector': '_qt3_d_render__render__render_target_selector',
      'SetFence': '_qt3_d_render__render__set_fence',
      'SortPolicy': '_qt3_d_render__render__sort_policy',
      'StateSetNode': '_qt3_d_render__render__state_set_node',
      'SubtreeEnabler': '_qt3_d_render__render__subtree_enabler',
      'TechniqueFilter': '_qt3_d_render__render__technique_filter',
      'UniformValue': '_qt3_d_render__render__uniform_value',
      'ViewportNode': '_qt3_d_render__render__viewport_node',
      'WaitFence': '_qt3_d_render__render__wait_fence',
      'Skeleton': '_qt3_d_render__render__skeleton',
      'PickBoundingVolumeJob': '_qt3_d_render__render__pick_bounding_volume_job',
      'AbstractRenderer': '_qt3_d_render__render__abstract_renderer',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('JobTypes', 'PickingUtils',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DRender.Render.AlphaCoverage'. Python calls this for
    a name the package does not hold yet, and what it gives is kept here for
    the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('...%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
