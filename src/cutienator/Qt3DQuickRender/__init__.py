"""
The 'cutienator.Qt3DQuickRender' package provides the cute classes of
the part of Qt named Qt3DQuickRender, under the name PySide6 has for it.

  from cutienator.Qt3DQuickRender import QAbstractLightForeign, QAbstractTextureForeign

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
    'QAbstractLightForeign',
    'QAbstractTextureForeign',
    'QAbstractTextureImageForeign',
    'QAlphaCoverageForeign',
    'QAlphaTestForeign',
    'QBlendEquationArgumentsForeign',
    'QBlendEquationForeign',
    'QBlitFramebufferForeign',
    'QBufferCaptureForeign',
    'QCameraForeign',
    'QCameraLensForeign',
    'QCameraSelectorForeign',
    'QClearBuffersForeign',
    'QClipPlaneForeign',
    'QColorMaskForeign',
    'QComputeCommandForeign',
    'QCullFaceForeign',
    'QDebugOverlayForeign',
    'QDepthRangeForeign',
    'QDepthTestForeign',
    'QDirectionalLightForeign',
    'QDispatchComputeForeign',
    'QDitheringForeign',
    'QEffectForeign',
    'QEnvironmentLightForeign',
    'QFilterKeyForeign',
    'QFrameGraphNodeForeign',
    'QFrontFaceForeign',
    'QFrustumCullingForeign',
    'QGeometryRendererForeign',
    'QGraphicsApiFilterForeign',
    'QLayerFilterForeign',
    'QLayerForeign',
    'QLevelOfDetailBoundingSphereForeign',
    'QLevelOfDetailForeign',
    'QLevelOfDetailSwitchForeign',
    'QLineWidthForeign',
    'QMaterialForeign',
    'QMemoryBarrierForeign',
    'QMeshForeign',
    'QMultiSampleAntiAliasingForeign',
    'QNoDepthMaskForeign',
    'QNoDrawForeign',
    'QNoPickingForeign',
    'QObjectPickerForeign',
    'QParameterForeign',
    'QPickEventForeign',
    'QPickingProxyForeign',
    'QPickingSettingsForeign',
    'QPointLightForeign',
    'QPointSizeForeign',
    'QPolygonOffsetForeign',
    'QProximityFilterForeign',
    'QRasterModeForeign',
    'QRenderCapabilitiesForeign',
    'QRenderCaptureForeign',
    'QRenderCaptureReplyForeign',
    'QRenderPassFilterForeign',
    'QRenderPassForeign',
    'QRenderSettingsForeign',
    'QRenderStateForeign',
    'QRenderStateSetForeign',
    'QRenderSurfaceSelectorForeign',
    'QRenderTargetForeign',
    'QRenderTargetOutputForeign',
    'QRenderTargetSelectorForeign',
    'QSceneLoaderForeign',
    'QScissorTestForeign',
    'QSeamlessCubemapForeign',
    'QSetFenceForeign',
    'QShaderDataForeign',
    'QShaderImageForeign',
    'QShaderProgramBuilderForeign',
    'QShaderProgramForeign',
    'QSharedGLTextureForeign',
    'QSortPolicyForeign',
    'QSpotLightForeign',
    'QStencilMaskForeign',
    'QStencilOperationArgumentsForeign',
    'QStencilOperationForeign',
    'QStencilTestArgumentsForeign',
    'QStencilTestForeign',
    'QSubtreeEnablerForeign',
    'QTechniqueFilterForeign',
    'QTechniqueForeign',
    'QTexture1DArrayForeign',
    'QTexture1DForeign',
    'QTexture2DArrayForeign',
    'QTexture2DForeign',
    'QTexture2DMultisampleArrayForeign',
    'QTexture2DMultisampleForeign',
    'QTexture3DForeign',
    'QTextureBufferForeign',
    'QTextureCubeMapArrayForeign',
    'QTextureCubeMapForeign',
    'QTextureImageForeign',
    'QTextureLoaderForeign',
    'QTextureRectangleForeign',
    'QTextureWrapModeForeign',
    'QViewportForeign',
    'QWaitFenceForeign',
    'Quick3DRayCasterHitForeign',
    'Quick3DRayCasterHitsForeign',
    'Qt3DQuick3DRenderPlugin',
    'Qt3DRender',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_abstract_light_foreign import QAbstractLightForeign
  from ._q_abstract_texture_foreign import QAbstractTextureForeign
  from ._q_abstract_texture_image_foreign import QAbstractTextureImageForeign
  from ._q_alpha_coverage_foreign import QAlphaCoverageForeign
  from ._q_alpha_test_foreign import QAlphaTestForeign
  from ._q_blend_equation_arguments_foreign import QBlendEquationArgumentsForeign
  from ._q_blend_equation_foreign import QBlendEquationForeign
  from ._q_blit_framebuffer_foreign import QBlitFramebufferForeign
  from ._q_buffer_capture_foreign import QBufferCaptureForeign
  from ._q_camera_foreign import QCameraForeign
  from ._q_camera_lens_foreign import QCameraLensForeign
  from ._q_camera_selector_foreign import QCameraSelectorForeign
  from ._q_clear_buffers_foreign import QClearBuffersForeign
  from ._q_clip_plane_foreign import QClipPlaneForeign
  from ._q_color_mask_foreign import QColorMaskForeign
  from ._q_compute_command_foreign import QComputeCommandForeign
  from ._q_cull_face_foreign import QCullFaceForeign
  from ._q_debug_overlay_foreign import QDebugOverlayForeign
  from ._q_depth_range_foreign import QDepthRangeForeign
  from ._q_depth_test_foreign import QDepthTestForeign
  from ._q_directional_light_foreign import QDirectionalLightForeign
  from ._q_dispatch_compute_foreign import QDispatchComputeForeign
  from ._q_dithering_foreign import QDitheringForeign
  from ._q_effect_foreign import QEffectForeign
  from ._q_environment_light_foreign import QEnvironmentLightForeign
  from ._q_filter_key_foreign import QFilterKeyForeign
  from ._q_frame_graph_node_foreign import QFrameGraphNodeForeign
  from ._q_front_face_foreign import QFrontFaceForeign
  from ._q_frustum_culling_foreign import QFrustumCullingForeign
  from ._q_geometry_renderer_foreign import QGeometryRendererForeign
  from ._q_graphics_api_filter_foreign import QGraphicsApiFilterForeign
  from ._q_layer_filter_foreign import QLayerFilterForeign
  from ._q_layer_foreign import QLayerForeign
  from ._q_level_of_detail_bounding_sphere_foreign import QLevelOfDetailBoundingSphereForeign
  from ._q_level_of_detail_foreign import QLevelOfDetailForeign
  from ._q_level_of_detail_switch_foreign import QLevelOfDetailSwitchForeign
  from ._q_line_width_foreign import QLineWidthForeign
  from ._q_material_foreign import QMaterialForeign
  from ._q_memory_barrier_foreign import QMemoryBarrierForeign
  from ._q_mesh_foreign import QMeshForeign
  from ._q_multi_sample_anti_aliasing_foreign import QMultiSampleAntiAliasingForeign
  from ._q_no_depth_mask_foreign import QNoDepthMaskForeign
  from ._q_no_draw_foreign import QNoDrawForeign
  from ._q_no_picking_foreign import QNoPickingForeign
  from ._q_object_picker_foreign import QObjectPickerForeign
  from ._q_parameter_foreign import QParameterForeign
  from ._q_pick_event_foreign import QPickEventForeign
  from ._q_picking_proxy_foreign import QPickingProxyForeign
  from ._q_picking_settings_foreign import QPickingSettingsForeign
  from ._q_point_light_foreign import QPointLightForeign
  from ._q_point_size_foreign import QPointSizeForeign
  from ._q_polygon_offset_foreign import QPolygonOffsetForeign
  from ._q_proximity_filter_foreign import QProximityFilterForeign
  from ._q_raster_mode_foreign import QRasterModeForeign
  from ._q_render_capabilities_foreign import QRenderCapabilitiesForeign
  from ._q_render_capture_foreign import QRenderCaptureForeign
  from ._q_render_capture_reply_foreign import QRenderCaptureReplyForeign
  from ._q_render_pass_filter_foreign import QRenderPassFilterForeign
  from ._q_render_pass_foreign import QRenderPassForeign
  from ._q_render_settings_foreign import QRenderSettingsForeign
  from ._q_render_state_foreign import QRenderStateForeign
  from ._q_render_state_set_foreign import QRenderStateSetForeign
  from ._q_render_surface_selector_foreign import QRenderSurfaceSelectorForeign
  from ._q_render_target_foreign import QRenderTargetForeign
  from ._q_render_target_output_foreign import QRenderTargetOutputForeign
  from ._q_render_target_selector_foreign import QRenderTargetSelectorForeign
  from ._q_scene_loader_foreign import QSceneLoaderForeign
  from ._q_scissor_test_foreign import QScissorTestForeign
  from ._q_seamless_cubemap_foreign import QSeamlessCubemapForeign
  from ._q_set_fence_foreign import QSetFenceForeign
  from ._q_shader_data_foreign import QShaderDataForeign
  from ._q_shader_image_foreign import QShaderImageForeign
  from ._q_shader_program_builder_foreign import QShaderProgramBuilderForeign
  from ._q_shader_program_foreign import QShaderProgramForeign
  from ._q_shared_g_l_texture_foreign import QSharedGLTextureForeign
  from ._q_sort_policy_foreign import QSortPolicyForeign
  from ._q_spot_light_foreign import QSpotLightForeign
  from ._q_stencil_mask_foreign import QStencilMaskForeign
  from ._q_stencil_operation_arguments_foreign import QStencilOperationArgumentsForeign
  from ._q_stencil_operation_foreign import QStencilOperationForeign
  from ._q_stencil_test_arguments_foreign import QStencilTestArgumentsForeign
  from ._q_stencil_test_foreign import QStencilTestForeign
  from ._q_subtree_enabler_foreign import QSubtreeEnablerForeign
  from ._q_technique_filter_foreign import QTechniqueFilterForeign
  from ._q_technique_foreign import QTechniqueForeign
  from ._q_texture1_d_array_foreign import QTexture1DArrayForeign
  from ._q_texture1_d_foreign import QTexture1DForeign
  from ._q_texture2_d_array_foreign import QTexture2DArrayForeign
  from ._q_texture2_d_foreign import QTexture2DForeign
  from ._q_texture2_d_multisample_array_foreign import QTexture2DMultisampleArrayForeign
  from ._q_texture2_d_multisample_foreign import QTexture2DMultisampleForeign
  from ._q_texture3_d_foreign import QTexture3DForeign
  from ._q_texture_buffer_foreign import QTextureBufferForeign
  from ._q_texture_cube_map_array_foreign import QTextureCubeMapArrayForeign
  from ._q_texture_cube_map_foreign import QTextureCubeMapForeign
  from ._q_texture_image_foreign import QTextureImageForeign
  from ._q_texture_loader_foreign import QTextureLoaderForeign
  from ._q_texture_rectangle_foreign import QTextureRectangleForeign
  from ._q_texture_wrap_mode_foreign import QTextureWrapModeForeign
  from ._q_viewport_foreign import QViewportForeign
  from ._q_wait_fence_foreign import QWaitFenceForeign
  from ._quick3_d_ray_caster_hit_foreign import Quick3DRayCasterHitForeign
  from ._quick3_d_ray_caster_hits_foreign import Quick3DRayCasterHitsForeign
  from ._qt3_d_quick3_d_render_plugin import Qt3DQuick3DRenderPlugin
  from . import Qt3DRender
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QAbstractLightForeign': '_q_abstract_light_foreign',
      'QAbstractTextureForeign': '_q_abstract_texture_foreign',
      'QAbstractTextureImageForeign': '_q_abstract_texture_image_foreign',
      'QAlphaCoverageForeign': '_q_alpha_coverage_foreign',
      'QAlphaTestForeign': '_q_alpha_test_foreign',
      'QBlendEquationArgumentsForeign': '_q_blend_equation_arguments_foreign',
      'QBlendEquationForeign': '_q_blend_equation_foreign',
      'QBlitFramebufferForeign': '_q_blit_framebuffer_foreign',
      'QBufferCaptureForeign': '_q_buffer_capture_foreign',
      'QCameraForeign': '_q_camera_foreign',
      'QCameraLensForeign': '_q_camera_lens_foreign',
      'QCameraSelectorForeign': '_q_camera_selector_foreign',
      'QClearBuffersForeign': '_q_clear_buffers_foreign',
      'QClipPlaneForeign': '_q_clip_plane_foreign',
      'QColorMaskForeign': '_q_color_mask_foreign',
      'QComputeCommandForeign': '_q_compute_command_foreign',
      'QCullFaceForeign': '_q_cull_face_foreign',
      'QDebugOverlayForeign': '_q_debug_overlay_foreign',
      'QDepthRangeForeign': '_q_depth_range_foreign',
      'QDepthTestForeign': '_q_depth_test_foreign',
      'QDirectionalLightForeign': '_q_directional_light_foreign',
      'QDispatchComputeForeign': '_q_dispatch_compute_foreign',
      'QDitheringForeign': '_q_dithering_foreign',
      'QEffectForeign': '_q_effect_foreign',
      'QEnvironmentLightForeign': '_q_environment_light_foreign',
      'QFilterKeyForeign': '_q_filter_key_foreign',
      'QFrameGraphNodeForeign': '_q_frame_graph_node_foreign',
      'QFrontFaceForeign': '_q_front_face_foreign',
      'QFrustumCullingForeign': '_q_frustum_culling_foreign',
      'QGeometryRendererForeign': '_q_geometry_renderer_foreign',
      'QGraphicsApiFilterForeign': '_q_graphics_api_filter_foreign',
      'QLayerFilterForeign': '_q_layer_filter_foreign',
      'QLayerForeign': '_q_layer_foreign',
      'QLevelOfDetailBoundingSphereForeign': '_q_level_of_detail_bounding_sphere_foreign',
      'QLevelOfDetailForeign': '_q_level_of_detail_foreign',
      'QLevelOfDetailSwitchForeign': '_q_level_of_detail_switch_foreign',
      'QLineWidthForeign': '_q_line_width_foreign',
      'QMaterialForeign': '_q_material_foreign',
      'QMemoryBarrierForeign': '_q_memory_barrier_foreign',
      'QMeshForeign': '_q_mesh_foreign',
      'QMultiSampleAntiAliasingForeign': '_q_multi_sample_anti_aliasing_foreign',
      'QNoDepthMaskForeign': '_q_no_depth_mask_foreign',
      'QNoDrawForeign': '_q_no_draw_foreign',
      'QNoPickingForeign': '_q_no_picking_foreign',
      'QObjectPickerForeign': '_q_object_picker_foreign',
      'QParameterForeign': '_q_parameter_foreign',
      'QPickEventForeign': '_q_pick_event_foreign',
      'QPickingProxyForeign': '_q_picking_proxy_foreign',
      'QPickingSettingsForeign': '_q_picking_settings_foreign',
      'QPointLightForeign': '_q_point_light_foreign',
      'QPointSizeForeign': '_q_point_size_foreign',
      'QPolygonOffsetForeign': '_q_polygon_offset_foreign',
      'QProximityFilterForeign': '_q_proximity_filter_foreign',
      'QRasterModeForeign': '_q_raster_mode_foreign',
      'QRenderCapabilitiesForeign': '_q_render_capabilities_foreign',
      'QRenderCaptureForeign': '_q_render_capture_foreign',
      'QRenderCaptureReplyForeign': '_q_render_capture_reply_foreign',
      'QRenderPassFilterForeign': '_q_render_pass_filter_foreign',
      'QRenderPassForeign': '_q_render_pass_foreign',
      'QRenderSettingsForeign': '_q_render_settings_foreign',
      'QRenderStateForeign': '_q_render_state_foreign',
      'QRenderStateSetForeign': '_q_render_state_set_foreign',
      'QRenderSurfaceSelectorForeign': '_q_render_surface_selector_foreign',
      'QRenderTargetForeign': '_q_render_target_foreign',
      'QRenderTargetOutputForeign': '_q_render_target_output_foreign',
      'QRenderTargetSelectorForeign': '_q_render_target_selector_foreign',
      'QSceneLoaderForeign': '_q_scene_loader_foreign',
      'QScissorTestForeign': '_q_scissor_test_foreign',
      'QSeamlessCubemapForeign': '_q_seamless_cubemap_foreign',
      'QSetFenceForeign': '_q_set_fence_foreign',
      'QShaderDataForeign': '_q_shader_data_foreign',
      'QShaderImageForeign': '_q_shader_image_foreign',
      'QShaderProgramBuilderForeign': '_q_shader_program_builder_foreign',
      'QShaderProgramForeign': '_q_shader_program_foreign',
      'QSharedGLTextureForeign': '_q_shared_g_l_texture_foreign',
      'QSortPolicyForeign': '_q_sort_policy_foreign',
      'QSpotLightForeign': '_q_spot_light_foreign',
      'QStencilMaskForeign': '_q_stencil_mask_foreign',
      'QStencilOperationArgumentsForeign': '_q_stencil_operation_arguments_foreign',
      'QStencilOperationForeign': '_q_stencil_operation_foreign',
      'QStencilTestArgumentsForeign': '_q_stencil_test_arguments_foreign',
      'QStencilTestForeign': '_q_stencil_test_foreign',
      'QSubtreeEnablerForeign': '_q_subtree_enabler_foreign',
      'QTechniqueFilterForeign': '_q_technique_filter_foreign',
      'QTechniqueForeign': '_q_technique_foreign',
      'QTexture1DArrayForeign': '_q_texture1_d_array_foreign',
      'QTexture1DForeign': '_q_texture1_d_foreign',
      'QTexture2DArrayForeign': '_q_texture2_d_array_foreign',
      'QTexture2DForeign': '_q_texture2_d_foreign',
      'QTexture2DMultisampleArrayForeign': '_q_texture2_d_multisample_array_foreign',
      'QTexture2DMultisampleForeign': '_q_texture2_d_multisample_foreign',
      'QTexture3DForeign': '_q_texture3_d_foreign',
      'QTextureBufferForeign': '_q_texture_buffer_foreign',
      'QTextureCubeMapArrayForeign': '_q_texture_cube_map_array_foreign',
      'QTextureCubeMapForeign': '_q_texture_cube_map_foreign',
      'QTextureImageForeign': '_q_texture_image_foreign',
      'QTextureLoaderForeign': '_q_texture_loader_foreign',
      'QTextureRectangleForeign': '_q_texture_rectangle_foreign',
      'QTextureWrapModeForeign': '_q_texture_wrap_mode_foreign',
      'QViewportForeign': '_q_viewport_foreign',
      'QWaitFenceForeign': '_q_wait_fence_foreign',
      'Quick3DRayCasterHitForeign': '_quick3_d_ray_caster_hit_foreign',
      'Quick3DRayCasterHitsForeign': '_quick3_d_ray_caster_hits_foreign',
      'Qt3DQuick3DRenderPlugin': '_qt3_d_quick3_d_render_plugin',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('Qt3DRender',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.Qt3DQuickRender import Qt3DQuick3DRenderPlugin'. Python calls
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
