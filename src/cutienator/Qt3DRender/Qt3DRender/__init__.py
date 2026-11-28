"""
The namespace 'Qt3DRender' of Qt, a package of 'cutienator.Qt3DRender':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DRender import Qt3DRender
  Qt3DRender.CameraLensRequest

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._qt3_d_render import Qt3DRender as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'CameraLensRequest',
    'GraphicsApiFilterData',
    'QAlphaTestData',
    'QBlendEquationData',
    'QCameraLensData',
    'QComputeCommandData',
    'QLayerData',
    'QLevelOfDetailData',
    'QObjectPickerEvent',
    'QRenderCaptureRequest',
    'QRenderSettingsData',
    'QRenderTargetData',
    'QRenderTargetOutputData',
    'QShaderGenerator',
    'QShaderGraph',
    'QShaderNodePort',
    'QStencilOperationArgumentsData',
    'QStencilOperationData',
    'QStencilTestArgumentsData',
    'QStencilTestData',
    'QTextureData',
    'QTextureDataUpdate',
    'RenderCaptureData',
    'QTextureDataUpdatePrivate',
    'QTextureGenerator',
    'QTextureImageDataGenerator',
    'QSceneExportFactory',
    'QSceneImportFactory',
    'QTextureImageDataPrivate',
    'QImageTextureDataFunctor',
    'QShaderFormat',
    'MeshDownloadRequest',
    'PropertyReaderInterface',
    'QGeometryLoaderFactory',
    'QGeometryLoaderInterface',
    'QGraphicsApiFilter',
    'QGraphicsApiFilterPrivate',
    'QPickEventPrivate',
    'QRenderCapabilities',
    'QRenderCapabilitiesPrivate',
    'QRenderCaptureReply',
    'QRenderCaptureReplyPrivate',
    'QSceneExportPlugin',
    'QSceneImportPlugin',
    'QSceneImporter',
    'QShaderGraphLoader',
    'QShaderNode',
    'QShaderNodesLoader',
    'QStencilOperationArguments',
    'QStencilOperationArgumentsPrivate',
    'QStencilTestArguments',
    'QStencilTestArgumentsPrivate',
    'QTextureWrapMode',
    'TextureLoadingHelper',
    'QAbstractTexture',
    'QAbstractTextureImage',
    'QAbstractTextureImagePrivate',
    'QAbstractTexturePrivate',
    'QEffect',
    'QEffectPrivate',
    'QFilterKey',
    'QFilterKeyPrivate',
    'QFrameGraphNode',
    'QFrameGraphNodePrivate',
    'QParameter',
    'QParameterPrivate',
    'QPickTriangleEventPrivate',
    'QPickingSettings',
    'QPickingSettingsPrivate',
    'QRenderAspect',
    'QRenderPass',
    'QRenderPassPrivate',
    'QRenderState',
    'QRenderStatePrivate',
    'QRenderTargetOutput',
    'QRenderTargetOutputPrivate',
    'QShaderDataPropertyReader',
    'QShaderImagePrivate',
    'QShaderProgram',
    'QShaderProgramBuilderPrivate',
    'QShaderProgramPrivate',
    'QTechnique',
    'QTechniquePrivate',
    'QTextureFromSourceGenerator',
    'TextureDownloadRequest',
    'MeshLoaderFunctor',
    'QAbstractLight',
    'QAbstractLightPrivate',
    'QAbstractRayCaster',
    'QAbstractRayCasterPrivate',
    'QAlphaCoverage',
    'QAlphaTest',
    'QAlphaTestPrivate',
    'QBlendEquation',
    'QBlendEquationArguments',
    'QBlendEquationArgumentsPrivate',
    'QBlendEquationPrivate',
    'QBlitFramebuffer',
    'QBlitFramebufferPrivate',
    'QBufferCapture',
    'QBufferCapturePrivate',
    'QCameraPrivate',
    'QCameraSelector',
    'QCameraSelectorPrivate',
    'QClearBuffers',
    'QClearBuffersPrivate',
    'QClipPlanePrivate',
    'QColorMask',
    'QColorMaskPrivate',
    'QComputeCommand',
    'QComputeCommandPrivate',
    'QCullFace',
    'QCullFacePrivate',
    'QDebugOverlay',
    'QDebugOverlayPrivate',
    'QDepthRange',
    'QDepthRangePrivate',
    'QDepthTest',
    'QDepthTestPrivate',
    'QDispatchCompute',
    'QDispatchComputePrivate',
    'QDithering',
    'QEnvironmentLight',
    'QEnvironmentLightPrivate',
    'QFrontFace',
    'QFrontFacePrivate',
    'QFrustumCulling',
    'QLayer',
    'QLayerFilter',
    'QLayerFilterPrivate',
    'QLayerPrivate',
    'QLineWidth',
    'QLineWidthPrivate',
    'QMaterial',
    'QMaterialPrivate',
    'QMemoryBarrier',
    'QMemoryBarrierPrivate',
    'QMultiSampleAntiAliasing',
    'QNoDepthMask',
    'QNoDraw',
    'QNoPicking',
    'QObjectPickerPrivate',
    'QPaintedTextureImage',
    'QPaintedTextureImageDataGenerator',
    'QPaintedTextureImagePrivate',
    'QPointSize',
    'QPointSizePrivate',
    'QPolygonOffset',
    'QPolygonOffsetPrivate',
    'QProximityFilter',
    'QProximityFilterPrivate',
    'QRasterMode',
    'QRasterModePrivate',
    'QRenderCapture',
    'QRenderCapturePrivate',
    'QRenderPassFilter',
    'QRenderPassFilterPrivate',
    'QRenderSettings',
    'QRenderSettingsPrivate',
    'QRenderStateSet',
    'QRenderStateSetPrivate',
    'QRenderSurfaceSelector',
    'QRenderSurfaceSelectorPrivate',
    'QRenderTarget',
    'QRenderTargetPrivate',
    'QRenderTargetSelector',
    'QRenderTargetSelectorPrivate',
    'QSceneExporter',
    'QSceneLoader',
    'QSceneLoaderPrivate',
    'QScissorTest',
    'QScissorTestPrivate',
    'QSeamlessCubemap',
    'QSetFence',
    'QSetFencePrivate',
    'QShaderData',
    'QShaderDataPrivate',
    'QShaderImage',
    'QShaderProgramBuilder',
    'QSharedGLTexture',
    'QSortPolicy',
    'QSortPolicyPrivate',
    'QStencilMask',
    'QStencilMaskPrivate',
    'QStencilOperation',
    'QStencilOperationPrivate',
    'QStencilTest',
    'QStencilTestPrivate',
    'QSubtreeEnabler',
    'QSubtreeEnablerPrivate',
    'QTechniqueFilter',
    'QTechniqueFilterPrivate',
    'QTexture1D',
    'QTexture1DArray',
    'QTexture2D',
    'QTexture2DArray',
    'QTexture2DMultisample',
    'QTexture2DMultisampleArray',
    'QTexture3D',
    'QTextureBuffer',
    'QTextureCubeMap',
    'QTextureCubeMapArray',
    'QTextureImage',
    'QTextureImagePrivate',
    'QTextureLoader',
    'QTextureLoaderPrivate',
    'QTextureRectangle',
    'QViewport',
    'QViewportPrivate',
    'QWaitFence',
    'QWaitFencePrivate',
    'QAxisAlignedBoundingBox',
    'QCamera',
    'QCameraLens',
    'QCameraLensPrivate',
    'QClipPlane',
    'QDirectionalLight',
    'QDirectionalLightPrivate',
    'QLevelOfDetailBoundingSphere',
    'QLevelOfDetailPrivate',
    'QPickEvent',
    'QPointLight',
    'QPointLightPrivate',
    'QRayCaster',
    'QRayCasterHit',
    'QScreenRayCaster',
    'QSpotLight',
    'QSpotLightPrivate',
    'QTextureImageData',
    'QGeometryRenderer',
    'QGeometryRendererPrivate',
    'QLevelOfDetailSwitchPrivate',
    'QObjectPicker',
    'QPickLineEvent',
    'QPickPointEvent',
    'QPickTriangleEvent',
    'QPickingProxy',
    'QPickingProxyPrivate',
    'QMesh',
    'QMeshPrivate',
    'QRenderAspectPrivate',
    'QLevelOfDetail',
    'QLevelOfDetailSwitch',
    'RayCasting',
    'Render',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt3_d_render__camera_lens_request import CameraLensRequest
  from .._qt3_d_render__graphics_api_filter_data import GraphicsApiFilterData
  from .._qt3_d_render__q_alpha_test_data import QAlphaTestData
  from .._qt3_d_render__q_blend_equation_data import QBlendEquationData
  from .._qt3_d_render__q_camera_lens_data import QCameraLensData
  from .._qt3_d_render__q_compute_command_data import QComputeCommandData
  from .._qt3_d_render__q_layer_data import QLayerData
  from .._qt3_d_render__q_level_of_detail_data import QLevelOfDetailData
  from .._qt3_d_render__q_object_picker_event import QObjectPickerEvent
  from .._qt3_d_render__q_render_capture_request import QRenderCaptureRequest
  from .._qt3_d_render__q_render_settings_data import QRenderSettingsData
  from .._qt3_d_render__q_render_target_data import QRenderTargetData
  from .._qt3_d_render__q_render_target_output_data import QRenderTargetOutputData
  from .._qt3_d_render__q_shader_generator import QShaderGenerator
  from .._qt3_d_render__q_shader_graph import QShaderGraph
  from .._qt3_d_render__q_shader_node_port import QShaderNodePort
  from .._qt3_d_render__q_stencil_operation_arguments_data import QStencilOperationArgumentsData
  from .._qt3_d_render__q_stencil_operation_data import QStencilOperationData
  from .._qt3_d_render__q_stencil_test_arguments_data import QStencilTestArgumentsData
  from .._qt3_d_render__q_stencil_test_data import QStencilTestData
  from .._qt3_d_render__q_texture_data import QTextureData
  from .._qt3_d_render__q_texture_data_update import QTextureDataUpdate
  from .._qt3_d_render__render_capture_data import RenderCaptureData
  from .._qt3_d_render__q_texture_data_update_private import QTextureDataUpdatePrivate
  from .._qt3_d_render__q_texture_generator import QTextureGenerator
  from .._qt3_d_render__q_texture_image_data_generator import QTextureImageDataGenerator
  from .._qt3_d_render__q_scene_export_factory import QSceneExportFactory
  from .._qt3_d_render__q_scene_import_factory import QSceneImportFactory
  from .._qt3_d_render__q_texture_image_data_private import QTextureImageDataPrivate
  from .._qt3_d_render__q_image_texture_data_functor import QImageTextureDataFunctor
  from .._qt3_d_render__q_shader_format import QShaderFormat
  from .._qt3_d_render__mesh_download_request import MeshDownloadRequest
  from .._qt3_d_render__property_reader_interface import PropertyReaderInterface
  from .._qt3_d_render__q_geometry_loader_factory import QGeometryLoaderFactory
  from .._qt3_d_render__q_geometry_loader_interface import QGeometryLoaderInterface
  from .._qt3_d_render__q_graphics_api_filter import QGraphicsApiFilter
  from .._qt3_d_render__q_graphics_api_filter_private import QGraphicsApiFilterPrivate
  from .._qt3_d_render__q_pick_event_private import QPickEventPrivate
  from .._qt3_d_render__q_render_capabilities import QRenderCapabilities
  from .._qt3_d_render__q_render_capabilities_private import QRenderCapabilitiesPrivate
  from .._qt3_d_render__q_render_capture_reply import QRenderCaptureReply
  from .._qt3_d_render__q_render_capture_reply_private import QRenderCaptureReplyPrivate
  from .._qt3_d_render__q_scene_export_plugin import QSceneExportPlugin
  from .._qt3_d_render__q_scene_import_plugin import QSceneImportPlugin
  from .._qt3_d_render__q_scene_importer import QSceneImporter
  from .._qt3_d_render__q_shader_graph_loader import QShaderGraphLoader
  from .._qt3_d_render__q_shader_node import QShaderNode
  from .._qt3_d_render__q_shader_nodes_loader import QShaderNodesLoader
  from .._qt3_d_render__q_stencil_operation_arguments import QStencilOperationArguments
  from .._qt3_d_render__q_stencil_operation_arguments_private import QStencilOperationArgumentsPrivate
  from .._qt3_d_render__q_stencil_test_arguments import QStencilTestArguments
  from .._qt3_d_render__q_stencil_test_arguments_private import QStencilTestArgumentsPrivate
  from .._qt3_d_render__q_texture_wrap_mode import QTextureWrapMode
  from .._qt3_d_render__texture_loading_helper import TextureLoadingHelper
  from .._qt3_d_render__q_abstract_texture import QAbstractTexture
  from .._qt3_d_render__q_abstract_texture_image import QAbstractTextureImage
  from .._qt3_d_render__q_abstract_texture_image_private import QAbstractTextureImagePrivate
  from .._qt3_d_render__q_abstract_texture_private import QAbstractTexturePrivate
  from .._qt3_d_render__q_effect import QEffect
  from .._qt3_d_render__q_effect_private import QEffectPrivate
  from .._qt3_d_render__q_filter_key import QFilterKey
  from .._qt3_d_render__q_filter_key_private import QFilterKeyPrivate
  from .._qt3_d_render__q_frame_graph_node import QFrameGraphNode
  from .._qt3_d_render__q_frame_graph_node_private import QFrameGraphNodePrivate
  from .._qt3_d_render__q_parameter import QParameter
  from .._qt3_d_render__q_parameter_private import QParameterPrivate
  from .._qt3_d_render__q_pick_triangle_event_private import QPickTriangleEventPrivate
  from .._qt3_d_render__q_picking_settings import QPickingSettings
  from .._qt3_d_render__q_picking_settings_private import QPickingSettingsPrivate
  from .._qt3_d_render__q_render_aspect import QRenderAspect
  from .._qt3_d_render__q_render_pass import QRenderPass
  from .._qt3_d_render__q_render_pass_private import QRenderPassPrivate
  from .._qt3_d_render__q_render_state import QRenderState
  from .._qt3_d_render__q_render_state_private import QRenderStatePrivate
  from .._qt3_d_render__q_render_target_output import QRenderTargetOutput
  from .._qt3_d_render__q_render_target_output_private import QRenderTargetOutputPrivate
  from .._qt3_d_render__q_shader_data_property_reader import QShaderDataPropertyReader
  from .._qt3_d_render__q_shader_image_private import QShaderImagePrivate
  from .._qt3_d_render__q_shader_program import QShaderProgram
  from .._qt3_d_render__q_shader_program_builder_private import QShaderProgramBuilderPrivate
  from .._qt3_d_render__q_shader_program_private import QShaderProgramPrivate
  from .._qt3_d_render__q_technique import QTechnique
  from .._qt3_d_render__q_technique_private import QTechniquePrivate
  from .._qt3_d_render__q_texture_from_source_generator import QTextureFromSourceGenerator
  from .._qt3_d_render__texture_download_request import TextureDownloadRequest
  from .._qt3_d_render__mesh_loader_functor import MeshLoaderFunctor
  from .._qt3_d_render__q_abstract_light import QAbstractLight
  from .._qt3_d_render__q_abstract_light_private import QAbstractLightPrivate
  from .._qt3_d_render__q_abstract_ray_caster import QAbstractRayCaster
  from .._qt3_d_render__q_abstract_ray_caster_private import QAbstractRayCasterPrivate
  from .._qt3_d_render__q_alpha_coverage import QAlphaCoverage
  from .._qt3_d_render__q_alpha_test import QAlphaTest
  from .._qt3_d_render__q_alpha_test_private import QAlphaTestPrivate
  from .._qt3_d_render__q_blend_equation import QBlendEquation
  from .._qt3_d_render__q_blend_equation_arguments import QBlendEquationArguments
  from .._qt3_d_render__q_blend_equation_arguments_private import QBlendEquationArgumentsPrivate
  from .._qt3_d_render__q_blend_equation_private import QBlendEquationPrivate
  from .._qt3_d_render__q_blit_framebuffer import QBlitFramebuffer
  from .._qt3_d_render__q_blit_framebuffer_private import QBlitFramebufferPrivate
  from .._qt3_d_render__q_buffer_capture import QBufferCapture
  from .._qt3_d_render__q_buffer_capture_private import QBufferCapturePrivate
  from .._qt3_d_render__q_camera_private import QCameraPrivate
  from .._qt3_d_render__q_camera_selector import QCameraSelector
  from .._qt3_d_render__q_camera_selector_private import QCameraSelectorPrivate
  from .._qt3_d_render__q_clear_buffers import QClearBuffers
  from .._qt3_d_render__q_clear_buffers_private import QClearBuffersPrivate
  from .._qt3_d_render__q_clip_plane_private import QClipPlanePrivate
  from .._qt3_d_render__q_color_mask import QColorMask
  from .._qt3_d_render__q_color_mask_private import QColorMaskPrivate
  from .._qt3_d_render__q_compute_command import QComputeCommand
  from .._qt3_d_render__q_compute_command_private import QComputeCommandPrivate
  from .._qt3_d_render__q_cull_face import QCullFace
  from .._qt3_d_render__q_cull_face_private import QCullFacePrivate
  from .._qt3_d_render__q_debug_overlay import QDebugOverlay
  from .._qt3_d_render__q_debug_overlay_private import QDebugOverlayPrivate
  from .._qt3_d_render__q_depth_range import QDepthRange
  from .._qt3_d_render__q_depth_range_private import QDepthRangePrivate
  from .._qt3_d_render__q_depth_test import QDepthTest
  from .._qt3_d_render__q_depth_test_private import QDepthTestPrivate
  from .._qt3_d_render__q_dispatch_compute import QDispatchCompute
  from .._qt3_d_render__q_dispatch_compute_private import QDispatchComputePrivate
  from .._qt3_d_render__q_dithering import QDithering
  from .._qt3_d_render__q_environment_light import QEnvironmentLight
  from .._qt3_d_render__q_environment_light_private import QEnvironmentLightPrivate
  from .._qt3_d_render__q_front_face import QFrontFace
  from .._qt3_d_render__q_front_face_private import QFrontFacePrivate
  from .._qt3_d_render__q_frustum_culling import QFrustumCulling
  from .._qt3_d_render__q_layer import QLayer
  from .._qt3_d_render__q_layer_filter import QLayerFilter
  from .._qt3_d_render__q_layer_filter_private import QLayerFilterPrivate
  from .._qt3_d_render__q_layer_private import QLayerPrivate
  from .._qt3_d_render__q_line_width import QLineWidth
  from .._qt3_d_render__q_line_width_private import QLineWidthPrivate
  from .._qt3_d_render__q_material import QMaterial
  from .._qt3_d_render__q_material_private import QMaterialPrivate
  from .._qt3_d_render__q_memory_barrier import QMemoryBarrier
  from .._qt3_d_render__q_memory_barrier_private import QMemoryBarrierPrivate
  from .._qt3_d_render__q_multi_sample_anti_aliasing import QMultiSampleAntiAliasing
  from .._qt3_d_render__q_no_depth_mask import QNoDepthMask
  from .._qt3_d_render__q_no_draw import QNoDraw
  from .._qt3_d_render__q_no_picking import QNoPicking
  from .._qt3_d_render__q_object_picker_private import QObjectPickerPrivate
  from .._qt3_d_render__q_painted_texture_image import QPaintedTextureImage
  from .._qt3_d_render__q_painted_texture_image_data_generator import QPaintedTextureImageDataGenerator
  from .._qt3_d_render__q_painted_texture_image_private import QPaintedTextureImagePrivate
  from .._qt3_d_render__q_point_size import QPointSize
  from .._qt3_d_render__q_point_size_private import QPointSizePrivate
  from .._qt3_d_render__q_polygon_offset import QPolygonOffset
  from .._qt3_d_render__q_polygon_offset_private import QPolygonOffsetPrivate
  from .._qt3_d_render__q_proximity_filter import QProximityFilter
  from .._qt3_d_render__q_proximity_filter_private import QProximityFilterPrivate
  from .._qt3_d_render__q_raster_mode import QRasterMode
  from .._qt3_d_render__q_raster_mode_private import QRasterModePrivate
  from .._qt3_d_render__q_render_capture import QRenderCapture
  from .._qt3_d_render__q_render_capture_private import QRenderCapturePrivate
  from .._qt3_d_render__q_render_pass_filter import QRenderPassFilter
  from .._qt3_d_render__q_render_pass_filter_private import QRenderPassFilterPrivate
  from .._qt3_d_render__q_render_settings import QRenderSettings
  from .._qt3_d_render__q_render_settings_private import QRenderSettingsPrivate
  from .._qt3_d_render__q_render_state_set import QRenderStateSet
  from .._qt3_d_render__q_render_state_set_private import QRenderStateSetPrivate
  from .._qt3_d_render__q_render_surface_selector import QRenderSurfaceSelector
  from .._qt3_d_render__q_render_surface_selector_private import QRenderSurfaceSelectorPrivate
  from .._qt3_d_render__q_render_target import QRenderTarget
  from .._qt3_d_render__q_render_target_private import QRenderTargetPrivate
  from .._qt3_d_render__q_render_target_selector import QRenderTargetSelector
  from .._qt3_d_render__q_render_target_selector_private import QRenderTargetSelectorPrivate
  from .._qt3_d_render__q_scene_exporter import QSceneExporter
  from .._qt3_d_render__q_scene_loader import QSceneLoader
  from .._qt3_d_render__q_scene_loader_private import QSceneLoaderPrivate
  from .._qt3_d_render__q_scissor_test import QScissorTest
  from .._qt3_d_render__q_scissor_test_private import QScissorTestPrivate
  from .._qt3_d_render__q_seamless_cubemap import QSeamlessCubemap
  from .._qt3_d_render__q_set_fence import QSetFence
  from .._qt3_d_render__q_set_fence_private import QSetFencePrivate
  from .._qt3_d_render__q_shader_data import QShaderData
  from .._qt3_d_render__q_shader_data_private import QShaderDataPrivate
  from .._qt3_d_render__q_shader_image import QShaderImage
  from .._qt3_d_render__q_shader_program_builder import QShaderProgramBuilder
  from .._qt3_d_render__q_shared_g_l_texture import QSharedGLTexture
  from .._qt3_d_render__q_sort_policy import QSortPolicy
  from .._qt3_d_render__q_sort_policy_private import QSortPolicyPrivate
  from .._qt3_d_render__q_stencil_mask import QStencilMask
  from .._qt3_d_render__q_stencil_mask_private import QStencilMaskPrivate
  from .._qt3_d_render__q_stencil_operation import QStencilOperation
  from .._qt3_d_render__q_stencil_operation_private import QStencilOperationPrivate
  from .._qt3_d_render__q_stencil_test import QStencilTest
  from .._qt3_d_render__q_stencil_test_private import QStencilTestPrivate
  from .._qt3_d_render__q_subtree_enabler import QSubtreeEnabler
  from .._qt3_d_render__q_subtree_enabler_private import QSubtreeEnablerPrivate
  from .._qt3_d_render__q_technique_filter import QTechniqueFilter
  from .._qt3_d_render__q_technique_filter_private import QTechniqueFilterPrivate
  from .._qt3_d_render__q_texture1_d import QTexture1D
  from .._qt3_d_render__q_texture1_d_array import QTexture1DArray
  from .._qt3_d_render__q_texture2_d import QTexture2D
  from .._qt3_d_render__q_texture2_d_array import QTexture2DArray
  from .._qt3_d_render__q_texture2_d_multisample import QTexture2DMultisample
  from .._qt3_d_render__q_texture2_d_multisample_array import QTexture2DMultisampleArray
  from .._qt3_d_render__q_texture3_d import QTexture3D
  from .._qt3_d_render__q_texture_buffer import QTextureBuffer
  from .._qt3_d_render__q_texture_cube_map import QTextureCubeMap
  from .._qt3_d_render__q_texture_cube_map_array import QTextureCubeMapArray
  from .._qt3_d_render__q_texture_image import QTextureImage
  from .._qt3_d_render__q_texture_image_private import QTextureImagePrivate
  from .._qt3_d_render__q_texture_loader import QTextureLoader
  from .._qt3_d_render__q_texture_loader_private import QTextureLoaderPrivate
  from .._qt3_d_render__q_texture_rectangle import QTextureRectangle
  from .._qt3_d_render__q_viewport import QViewport
  from .._qt3_d_render__q_viewport_private import QViewportPrivate
  from .._qt3_d_render__q_wait_fence import QWaitFence
  from .._qt3_d_render__q_wait_fence_private import QWaitFencePrivate
  from .._qt3_d_render__q_axis_aligned_bounding_box import QAxisAlignedBoundingBox
  from .._qt3_d_render__q_camera import QCamera
  from .._qt3_d_render__q_camera_lens import QCameraLens
  from .._qt3_d_render__q_camera_lens_private import QCameraLensPrivate
  from .._qt3_d_render__q_clip_plane import QClipPlane
  from .._qt3_d_render__q_directional_light import QDirectionalLight
  from .._qt3_d_render__q_directional_light_private import QDirectionalLightPrivate
  from .._qt3_d_render__q_level_of_detail_bounding_sphere import QLevelOfDetailBoundingSphere
  from .._qt3_d_render__q_level_of_detail_private import QLevelOfDetailPrivate
  from .._qt3_d_render__q_pick_event import QPickEvent
  from .._qt3_d_render__q_point_light import QPointLight
  from .._qt3_d_render__q_point_light_private import QPointLightPrivate
  from .._qt3_d_render__q_ray_caster import QRayCaster
  from .._qt3_d_render__q_ray_caster_hit import QRayCasterHit
  from .._qt3_d_render__q_screen_ray_caster import QScreenRayCaster
  from .._qt3_d_render__q_spot_light import QSpotLight
  from .._qt3_d_render__q_spot_light_private import QSpotLightPrivate
  from .._qt3_d_render__q_texture_image_data import QTextureImageData
  from .._qt3_d_render__q_geometry_renderer import QGeometryRenderer
  from .._qt3_d_render__q_geometry_renderer_private import QGeometryRendererPrivate
  from .._qt3_d_render__q_level_of_detail_switch_private import QLevelOfDetailSwitchPrivate
  from .._qt3_d_render__q_object_picker import QObjectPicker
  from .._qt3_d_render__q_pick_line_event import QPickLineEvent
  from .._qt3_d_render__q_pick_point_event import QPickPointEvent
  from .._qt3_d_render__q_pick_triangle_event import QPickTriangleEvent
  from .._qt3_d_render__q_picking_proxy import QPickingProxy
  from .._qt3_d_render__q_picking_proxy_private import QPickingProxyPrivate
  from .._qt3_d_render__q_mesh import QMesh
  from .._qt3_d_render__q_mesh_private import QMeshPrivate
  from .._qt3_d_render__q_render_aspect_private import QRenderAspectPrivate
  from .._qt3_d_render__q_level_of_detail import QLevelOfDetail
  from .._qt3_d_render__q_level_of_detail_switch import QLevelOfDetailSwitch
  from . import RayCasting
  from . import Render
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'CameraLensRequest': '_qt3_d_render__camera_lens_request',
      'GraphicsApiFilterData': '_qt3_d_render__graphics_api_filter_data',
      'QAlphaTestData': '_qt3_d_render__q_alpha_test_data',
      'QBlendEquationData': '_qt3_d_render__q_blend_equation_data',
      'QCameraLensData': '_qt3_d_render__q_camera_lens_data',
      'QComputeCommandData': '_qt3_d_render__q_compute_command_data',
      'QLayerData': '_qt3_d_render__q_layer_data',
      'QLevelOfDetailData': '_qt3_d_render__q_level_of_detail_data',
      'QObjectPickerEvent': '_qt3_d_render__q_object_picker_event',
      'QRenderCaptureRequest': '_qt3_d_render__q_render_capture_request',
      'QRenderSettingsData': '_qt3_d_render__q_render_settings_data',
      'QRenderTargetData': '_qt3_d_render__q_render_target_data',
      'QRenderTargetOutputData': '_qt3_d_render__q_render_target_output_data',
      'QShaderGenerator': '_qt3_d_render__q_shader_generator',
      'QShaderGraph': '_qt3_d_render__q_shader_graph',
      'QShaderNodePort': '_qt3_d_render__q_shader_node_port',
      'QStencilOperationArgumentsData': '_qt3_d_render__q_stencil_operation_arguments_data',
      'QStencilOperationData': '_qt3_d_render__q_stencil_operation_data',
      'QStencilTestArgumentsData': '_qt3_d_render__q_stencil_test_arguments_data',
      'QStencilTestData': '_qt3_d_render__q_stencil_test_data',
      'QTextureData': '_qt3_d_render__q_texture_data',
      'QTextureDataUpdate': '_qt3_d_render__q_texture_data_update',
      'RenderCaptureData': '_qt3_d_render__render_capture_data',
      'QTextureDataUpdatePrivate': '_qt3_d_render__q_texture_data_update_private',
      'QTextureGenerator': '_qt3_d_render__q_texture_generator',
      'QTextureImageDataGenerator': '_qt3_d_render__q_texture_image_data_generator',
      'QSceneExportFactory': '_qt3_d_render__q_scene_export_factory',
      'QSceneImportFactory': '_qt3_d_render__q_scene_import_factory',
      'QTextureImageDataPrivate': '_qt3_d_render__q_texture_image_data_private',
      'QImageTextureDataFunctor': '_qt3_d_render__q_image_texture_data_functor',
      'QShaderFormat': '_qt3_d_render__q_shader_format',
      'MeshDownloadRequest': '_qt3_d_render__mesh_download_request',
      'PropertyReaderInterface': '_qt3_d_render__property_reader_interface',
      'QGeometryLoaderFactory': '_qt3_d_render__q_geometry_loader_factory',
      'QGeometryLoaderInterface': '_qt3_d_render__q_geometry_loader_interface',
      'QGraphicsApiFilter': '_qt3_d_render__q_graphics_api_filter',
      'QGraphicsApiFilterPrivate': '_qt3_d_render__q_graphics_api_filter_private',
      'QPickEventPrivate': '_qt3_d_render__q_pick_event_private',
      'QRenderCapabilities': '_qt3_d_render__q_render_capabilities',
      'QRenderCapabilitiesPrivate': '_qt3_d_render__q_render_capabilities_private',
      'QRenderCaptureReply': '_qt3_d_render__q_render_capture_reply',
      'QRenderCaptureReplyPrivate': '_qt3_d_render__q_render_capture_reply_private',
      'QSceneExportPlugin': '_qt3_d_render__q_scene_export_plugin',
      'QSceneImportPlugin': '_qt3_d_render__q_scene_import_plugin',
      'QSceneImporter': '_qt3_d_render__q_scene_importer',
      'QShaderGraphLoader': '_qt3_d_render__q_shader_graph_loader',
      'QShaderNode': '_qt3_d_render__q_shader_node',
      'QShaderNodesLoader': '_qt3_d_render__q_shader_nodes_loader',
      'QStencilOperationArguments': '_qt3_d_render__q_stencil_operation_arguments',
      'QStencilOperationArgumentsPrivate': '_qt3_d_render__q_stencil_operation_arguments_private',
      'QStencilTestArguments': '_qt3_d_render__q_stencil_test_arguments',
      'QStencilTestArgumentsPrivate': '_qt3_d_render__q_stencil_test_arguments_private',
      'QTextureWrapMode': '_qt3_d_render__q_texture_wrap_mode',
      'TextureLoadingHelper': '_qt3_d_render__texture_loading_helper',
      'QAbstractTexture': '_qt3_d_render__q_abstract_texture',
      'QAbstractTextureImage': '_qt3_d_render__q_abstract_texture_image',
      'QAbstractTextureImagePrivate': '_qt3_d_render__q_abstract_texture_image_private',
      'QAbstractTexturePrivate': '_qt3_d_render__q_abstract_texture_private',
      'QEffect': '_qt3_d_render__q_effect',
      'QEffectPrivate': '_qt3_d_render__q_effect_private',
      'QFilterKey': '_qt3_d_render__q_filter_key',
      'QFilterKeyPrivate': '_qt3_d_render__q_filter_key_private',
      'QFrameGraphNode': '_qt3_d_render__q_frame_graph_node',
      'QFrameGraphNodePrivate': '_qt3_d_render__q_frame_graph_node_private',
      'QParameter': '_qt3_d_render__q_parameter',
      'QParameterPrivate': '_qt3_d_render__q_parameter_private',
      'QPickTriangleEventPrivate': '_qt3_d_render__q_pick_triangle_event_private',
      'QPickingSettings': '_qt3_d_render__q_picking_settings',
      'QPickingSettingsPrivate': '_qt3_d_render__q_picking_settings_private',
      'QRenderAspect': '_qt3_d_render__q_render_aspect',
      'QRenderPass': '_qt3_d_render__q_render_pass',
      'QRenderPassPrivate': '_qt3_d_render__q_render_pass_private',
      'QRenderState': '_qt3_d_render__q_render_state',
      'QRenderStatePrivate': '_qt3_d_render__q_render_state_private',
      'QRenderTargetOutput': '_qt3_d_render__q_render_target_output',
      'QRenderTargetOutputPrivate': '_qt3_d_render__q_render_target_output_private',
      'QShaderDataPropertyReader': '_qt3_d_render__q_shader_data_property_reader',
      'QShaderImagePrivate': '_qt3_d_render__q_shader_image_private',
      'QShaderProgram': '_qt3_d_render__q_shader_program',
      'QShaderProgramBuilderPrivate': '_qt3_d_render__q_shader_program_builder_private',
      'QShaderProgramPrivate': '_qt3_d_render__q_shader_program_private',
      'QTechnique': '_qt3_d_render__q_technique',
      'QTechniquePrivate': '_qt3_d_render__q_technique_private',
      'QTextureFromSourceGenerator': '_qt3_d_render__q_texture_from_source_generator',
      'TextureDownloadRequest': '_qt3_d_render__texture_download_request',
      'MeshLoaderFunctor': '_qt3_d_render__mesh_loader_functor',
      'QAbstractLight': '_qt3_d_render__q_abstract_light',
      'QAbstractLightPrivate': '_qt3_d_render__q_abstract_light_private',
      'QAbstractRayCaster': '_qt3_d_render__q_abstract_ray_caster',
      'QAbstractRayCasterPrivate': '_qt3_d_render__q_abstract_ray_caster_private',
      'QAlphaCoverage': '_qt3_d_render__q_alpha_coverage',
      'QAlphaTest': '_qt3_d_render__q_alpha_test',
      'QAlphaTestPrivate': '_qt3_d_render__q_alpha_test_private',
      'QBlendEquation': '_qt3_d_render__q_blend_equation',
      'QBlendEquationArguments': '_qt3_d_render__q_blend_equation_arguments',
      'QBlendEquationArgumentsPrivate': '_qt3_d_render__q_blend_equation_arguments_private',
      'QBlendEquationPrivate': '_qt3_d_render__q_blend_equation_private',
      'QBlitFramebuffer': '_qt3_d_render__q_blit_framebuffer',
      'QBlitFramebufferPrivate': '_qt3_d_render__q_blit_framebuffer_private',
      'QBufferCapture': '_qt3_d_render__q_buffer_capture',
      'QBufferCapturePrivate': '_qt3_d_render__q_buffer_capture_private',
      'QCameraPrivate': '_qt3_d_render__q_camera_private',
      'QCameraSelector': '_qt3_d_render__q_camera_selector',
      'QCameraSelectorPrivate': '_qt3_d_render__q_camera_selector_private',
      'QClearBuffers': '_qt3_d_render__q_clear_buffers',
      'QClearBuffersPrivate': '_qt3_d_render__q_clear_buffers_private',
      'QClipPlanePrivate': '_qt3_d_render__q_clip_plane_private',
      'QColorMask': '_qt3_d_render__q_color_mask',
      'QColorMaskPrivate': '_qt3_d_render__q_color_mask_private',
      'QComputeCommand': '_qt3_d_render__q_compute_command',
      'QComputeCommandPrivate': '_qt3_d_render__q_compute_command_private',
      'QCullFace': '_qt3_d_render__q_cull_face',
      'QCullFacePrivate': '_qt3_d_render__q_cull_face_private',
      'QDebugOverlay': '_qt3_d_render__q_debug_overlay',
      'QDebugOverlayPrivate': '_qt3_d_render__q_debug_overlay_private',
      'QDepthRange': '_qt3_d_render__q_depth_range',
      'QDepthRangePrivate': '_qt3_d_render__q_depth_range_private',
      'QDepthTest': '_qt3_d_render__q_depth_test',
      'QDepthTestPrivate': '_qt3_d_render__q_depth_test_private',
      'QDispatchCompute': '_qt3_d_render__q_dispatch_compute',
      'QDispatchComputePrivate': '_qt3_d_render__q_dispatch_compute_private',
      'QDithering': '_qt3_d_render__q_dithering',
      'QEnvironmentLight': '_qt3_d_render__q_environment_light',
      'QEnvironmentLightPrivate': '_qt3_d_render__q_environment_light_private',
      'QFrontFace': '_qt3_d_render__q_front_face',
      'QFrontFacePrivate': '_qt3_d_render__q_front_face_private',
      'QFrustumCulling': '_qt3_d_render__q_frustum_culling',
      'QLayer': '_qt3_d_render__q_layer',
      'QLayerFilter': '_qt3_d_render__q_layer_filter',
      'QLayerFilterPrivate': '_qt3_d_render__q_layer_filter_private',
      'QLayerPrivate': '_qt3_d_render__q_layer_private',
      'QLineWidth': '_qt3_d_render__q_line_width',
      'QLineWidthPrivate': '_qt3_d_render__q_line_width_private',
      'QMaterial': '_qt3_d_render__q_material',
      'QMaterialPrivate': '_qt3_d_render__q_material_private',
      'QMemoryBarrier': '_qt3_d_render__q_memory_barrier',
      'QMemoryBarrierPrivate': '_qt3_d_render__q_memory_barrier_private',
      'QMultiSampleAntiAliasing': '_qt3_d_render__q_multi_sample_anti_aliasing',
      'QNoDepthMask': '_qt3_d_render__q_no_depth_mask',
      'QNoDraw': '_qt3_d_render__q_no_draw',
      'QNoPicking': '_qt3_d_render__q_no_picking',
      'QObjectPickerPrivate': '_qt3_d_render__q_object_picker_private',
      'QPaintedTextureImage': '_qt3_d_render__q_painted_texture_image',
      'QPaintedTextureImageDataGenerator': '_qt3_d_render__q_painted_texture_image_data_generator',
      'QPaintedTextureImagePrivate': '_qt3_d_render__q_painted_texture_image_private',
      'QPointSize': '_qt3_d_render__q_point_size',
      'QPointSizePrivate': '_qt3_d_render__q_point_size_private',
      'QPolygonOffset': '_qt3_d_render__q_polygon_offset',
      'QPolygonOffsetPrivate': '_qt3_d_render__q_polygon_offset_private',
      'QProximityFilter': '_qt3_d_render__q_proximity_filter',
      'QProximityFilterPrivate': '_qt3_d_render__q_proximity_filter_private',
      'QRasterMode': '_qt3_d_render__q_raster_mode',
      'QRasterModePrivate': '_qt3_d_render__q_raster_mode_private',
      'QRenderCapture': '_qt3_d_render__q_render_capture',
      'QRenderCapturePrivate': '_qt3_d_render__q_render_capture_private',
      'QRenderPassFilter': '_qt3_d_render__q_render_pass_filter',
      'QRenderPassFilterPrivate': '_qt3_d_render__q_render_pass_filter_private',
      'QRenderSettings': '_qt3_d_render__q_render_settings',
      'QRenderSettingsPrivate': '_qt3_d_render__q_render_settings_private',
      'QRenderStateSet': '_qt3_d_render__q_render_state_set',
      'QRenderStateSetPrivate': '_qt3_d_render__q_render_state_set_private',
      'QRenderSurfaceSelector': '_qt3_d_render__q_render_surface_selector',
      'QRenderSurfaceSelectorPrivate': '_qt3_d_render__q_render_surface_selector_private',
      'QRenderTarget': '_qt3_d_render__q_render_target',
      'QRenderTargetPrivate': '_qt3_d_render__q_render_target_private',
      'QRenderTargetSelector': '_qt3_d_render__q_render_target_selector',
      'QRenderTargetSelectorPrivate': '_qt3_d_render__q_render_target_selector_private',
      'QSceneExporter': '_qt3_d_render__q_scene_exporter',
      'QSceneLoader': '_qt3_d_render__q_scene_loader',
      'QSceneLoaderPrivate': '_qt3_d_render__q_scene_loader_private',
      'QScissorTest': '_qt3_d_render__q_scissor_test',
      'QScissorTestPrivate': '_qt3_d_render__q_scissor_test_private',
      'QSeamlessCubemap': '_qt3_d_render__q_seamless_cubemap',
      'QSetFence': '_qt3_d_render__q_set_fence',
      'QSetFencePrivate': '_qt3_d_render__q_set_fence_private',
      'QShaderData': '_qt3_d_render__q_shader_data',
      'QShaderDataPrivate': '_qt3_d_render__q_shader_data_private',
      'QShaderImage': '_qt3_d_render__q_shader_image',
      'QShaderProgramBuilder': '_qt3_d_render__q_shader_program_builder',
      'QSharedGLTexture': '_qt3_d_render__q_shared_g_l_texture',
      'QSortPolicy': '_qt3_d_render__q_sort_policy',
      'QSortPolicyPrivate': '_qt3_d_render__q_sort_policy_private',
      'QStencilMask': '_qt3_d_render__q_stencil_mask',
      'QStencilMaskPrivate': '_qt3_d_render__q_stencil_mask_private',
      'QStencilOperation': '_qt3_d_render__q_stencil_operation',
      'QStencilOperationPrivate': '_qt3_d_render__q_stencil_operation_private',
      'QStencilTest': '_qt3_d_render__q_stencil_test',
      'QStencilTestPrivate': '_qt3_d_render__q_stencil_test_private',
      'QSubtreeEnabler': '_qt3_d_render__q_subtree_enabler',
      'QSubtreeEnablerPrivate': '_qt3_d_render__q_subtree_enabler_private',
      'QTechniqueFilter': '_qt3_d_render__q_technique_filter',
      'QTechniqueFilterPrivate': '_qt3_d_render__q_technique_filter_private',
      'QTexture1D': '_qt3_d_render__q_texture1_d',
      'QTexture1DArray': '_qt3_d_render__q_texture1_d_array',
      'QTexture2D': '_qt3_d_render__q_texture2_d',
      'QTexture2DArray': '_qt3_d_render__q_texture2_d_array',
      'QTexture2DMultisample': '_qt3_d_render__q_texture2_d_multisample',
      'QTexture2DMultisampleArray': '_qt3_d_render__q_texture2_d_multisample_array',
      'QTexture3D': '_qt3_d_render__q_texture3_d',
      'QTextureBuffer': '_qt3_d_render__q_texture_buffer',
      'QTextureCubeMap': '_qt3_d_render__q_texture_cube_map',
      'QTextureCubeMapArray': '_qt3_d_render__q_texture_cube_map_array',
      'QTextureImage': '_qt3_d_render__q_texture_image',
      'QTextureImagePrivate': '_qt3_d_render__q_texture_image_private',
      'QTextureLoader': '_qt3_d_render__q_texture_loader',
      'QTextureLoaderPrivate': '_qt3_d_render__q_texture_loader_private',
      'QTextureRectangle': '_qt3_d_render__q_texture_rectangle',
      'QViewport': '_qt3_d_render__q_viewport',
      'QViewportPrivate': '_qt3_d_render__q_viewport_private',
      'QWaitFence': '_qt3_d_render__q_wait_fence',
      'QWaitFencePrivate': '_qt3_d_render__q_wait_fence_private',
      'QAxisAlignedBoundingBox': '_qt3_d_render__q_axis_aligned_bounding_box',
      'QCamera': '_qt3_d_render__q_camera',
      'QCameraLens': '_qt3_d_render__q_camera_lens',
      'QCameraLensPrivate': '_qt3_d_render__q_camera_lens_private',
      'QClipPlane': '_qt3_d_render__q_clip_plane',
      'QDirectionalLight': '_qt3_d_render__q_directional_light',
      'QDirectionalLightPrivate': '_qt3_d_render__q_directional_light_private',
      'QLevelOfDetailBoundingSphere': '_qt3_d_render__q_level_of_detail_bounding_sphere',
      'QLevelOfDetailPrivate': '_qt3_d_render__q_level_of_detail_private',
      'QPickEvent': '_qt3_d_render__q_pick_event',
      'QPointLight': '_qt3_d_render__q_point_light',
      'QPointLightPrivate': '_qt3_d_render__q_point_light_private',
      'QRayCaster': '_qt3_d_render__q_ray_caster',
      'QRayCasterHit': '_qt3_d_render__q_ray_caster_hit',
      'QScreenRayCaster': '_qt3_d_render__q_screen_ray_caster',
      'QSpotLight': '_qt3_d_render__q_spot_light',
      'QSpotLightPrivate': '_qt3_d_render__q_spot_light_private',
      'QTextureImageData': '_qt3_d_render__q_texture_image_data',
      'QGeometryRenderer': '_qt3_d_render__q_geometry_renderer',
      'QGeometryRendererPrivate': '_qt3_d_render__q_geometry_renderer_private',
      'QLevelOfDetailSwitchPrivate': '_qt3_d_render__q_level_of_detail_switch_private',
      'QObjectPicker': '_qt3_d_render__q_object_picker',
      'QPickLineEvent': '_qt3_d_render__q_pick_line_event',
      'QPickPointEvent': '_qt3_d_render__q_pick_point_event',
      'QPickTriangleEvent': '_qt3_d_render__q_pick_triangle_event',
      'QPickingProxy': '_qt3_d_render__q_picking_proxy',
      'QPickingProxyPrivate': '_qt3_d_render__q_picking_proxy_private',
      'QMesh': '_qt3_d_render__q_mesh',
      'QMeshPrivate': '_qt3_d_render__q_mesh_private',
      'QRenderAspectPrivate': '_qt3_d_render__q_render_aspect_private',
      'QLevelOfDetail': '_qt3_d_render__q_level_of_detail',
      'QLevelOfDetailSwitch': '_qt3_d_render__q_level_of_detail_switch',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('RayCasting', 'Render',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DRender.CameraLensRequest'. Python calls this for a
    name the package does not hold yet, and what it gives is kept here for
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
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
