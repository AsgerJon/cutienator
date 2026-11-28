"""
The 'cutienator.QtQuick3D' package provides the cute classes of the part
of Qt named QtQuick3D, under the name PySide6 has for it.

  from cutienator.QtQuick3D import QQuick3D, QQuick3DTextureInternalChange

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
    'QQuick3D',
    'QQuick3DTextureInternalChange',
    'QQuick3DBakedLightmap',
    'QQuick3DBounds3',
    'QQuick3DContentLayer',
    'QQuick3DDebugSettings',
    'QQuick3DFog',
    'QQuick3DLightmapper',
    'QQuick3DRenderPassTargetBlend',
    'QQuick3DSGRenderNode',
    'QQuick3DQuaternionUtils',
    'QQuick3DObject',
    'QQuick3DNode',
    'QQuick3DSceneManager',
    'QQuick3DObjectChangeListener',
    'QQuick3DObjectPrivate',
    'QQuick3DNodePrivate',
    'QQuick3DQuaternionAnimation',
    'QQuick3DRenderStats',
    'QSSGCleanupObject',
    'QQuick3DAbstractLight',
    'QQuick3DCamera',
    'QQuick3DExtensionHelpers',
    'QQuick3DGeometry',
    'QQuick3DGeometryPrivate',
    'QQuick3DInstanceListEntry',
    'QQuick3DInstancing',
    'QQuick3DInstancingPrivate',
    'QQuick3DItem2D',
    'QQuick3DLoader',
    'QQuick3DMorphTarget',
    'QQuick3DPropertyChangedTracker',
    'QQuick3DRenderExtension',
    'QQuick3DRepeater',
    'QQuick3DShaderUtilsBuffer',
    'QQuick3DShaderUtilsRenderCommand',
    'QQuick3DShaderUtilsRenderPassTexture',
    'QQuick3DShaderUtilsShader',
    'QQuick3DSkeleton',
    'QQuick3DSkin',
    'QQuick3DTextureData',
    'QQuick3DTextureDataPrivate',
    'QQuick3DTextureProviderExtensionPrivate',
    'QQuick3DWindowAttachment',
    'QQuick3DCustomCamera',
    'QQuick3DDirectionalLight',
    'QQuick3DFileInstancing',
    'QQuick3DInstanceList',
    'QQuick3DJoint',
    'QQuick3DLoaderIncubator',
    'QQuick3DOrthographicCamera',
    'QQuick3DPerspectiveCamera',
    'QQuick3DPointLight',
    'QQuick3DPropertyWatcher',
    'QQuick3DShaderUtilsApplyValue',
    'QQuick3DShaderUtilsBufferInput',
    'QQuick3DShaderUtilsPipelineStateOverride',
    'QQuick3DShaderUtilsRenderPass',
    'QQuick3DShaderUtilsRenderPassAddDefine',
    'QQuick3DShaderUtilsRenderPassColorAttachment',
    'QQuick3DShaderUtilsRenderPassDepthStencilAttachment',
    'QQuick3DShaderUtilsRenderPassDepthTextureAttachment',
    'QQuick3DShaderUtilsRenderablesFilter',
    'QQuick3DSkyMaterial',
    'QQuick3DSpotLight',
    'QQuick3DTexture',
    'QQuick3DTextureProviderExtension',
    'SGFramebufferObjectNode',
    'QQuick3DCubeMapTexture',
    'QQuick3DFrustumCamera',
    'QQuick3DMaterial',
    'QQuick3DResourceLoader',
    'QQuick3DShaderUtilsTextureInput',
    'QQuick3DCustomMaterial',
    'QQuick3DDefaultMaterial',
    'QQuick3DEffect',
    'QQuick3DModel',
    'QQuick3DPrincipledMaterial',
    'QQuick3DReflectionProbe',
    'QQuick3DRenderPass',
    'QQuick3DSpecularGlossyMaterial',
    'QQuick3DPickResult',
    'QQuick3DSceneEnvironment',
    'QQuick3DShaderUtilsSubRenderPass',
    'QQuick3DSceneRenderer',
    'QQuick3DViewport',
    'QQuick3DLightmapBaker',
    'QQuick3DRenderLayerHelpers',
    'QQuick3DSGDirectRenderer',
    'QQuick3DSceneRootNode',
    'QQuick3DPickResultEnums',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick3_d import QQuick3D
  from ._q_quick3_d_texture_internal_change import QQuick3DTextureInternalChange
  from ._q_quick3_d_baked_lightmap import QQuick3DBakedLightmap
  from ._q_quick3_d_bounds3 import QQuick3DBounds3
  from ._q_quick3_d_content_layer import QQuick3DContentLayer
  from ._q_quick3_d_debug_settings import QQuick3DDebugSettings
  from ._q_quick3_d_fog import QQuick3DFog
  from ._q_quick3_d_lightmapper import QQuick3DLightmapper
  from ._q_quick3_d_render_pass_target_blend import QQuick3DRenderPassTargetBlend
  from ._q_quick3_d_s_g_render_node import QQuick3DSGRenderNode
  from ._q_quick3_d_quaternion_utils import QQuick3DQuaternionUtils
  from ._q_quick3_d_object import QQuick3DObject
  from ._q_quick3_d_node import QQuick3DNode
  from ._q_quick3_d_scene_manager import QQuick3DSceneManager
  from ._q_quick3_d_object_change_listener import QQuick3DObjectChangeListener
  from ._q_quick3_d_object_private import QQuick3DObjectPrivate
  from ._q_quick3_d_node_private import QQuick3DNodePrivate
  from ._q_quick3_d_quaternion_animation import QQuick3DQuaternionAnimation
  from ._q_quick3_d_render_stats import QQuick3DRenderStats
  from ._q_s_s_g_cleanup_object import QSSGCleanupObject
  from ._q_quick3_d_abstract_light import QQuick3DAbstractLight
  from ._q_quick3_d_camera import QQuick3DCamera
  from ._q_quick3_d_extension_helpers import QQuick3DExtensionHelpers
  from ._q_quick3_d_geometry import QQuick3DGeometry
  from ._q_quick3_d_geometry_private import QQuick3DGeometryPrivate
  from ._q_quick3_d_instance_list_entry import QQuick3DInstanceListEntry
  from ._q_quick3_d_instancing import QQuick3DInstancing
  from ._q_quick3_d_instancing_private import QQuick3DInstancingPrivate
  from ._q_quick3_d_item2_d import QQuick3DItem2D
  from ._q_quick3_d_loader import QQuick3DLoader
  from ._q_quick3_d_morph_target import QQuick3DMorphTarget
  from ._q_quick3_d_property_changed_tracker import QQuick3DPropertyChangedTracker
  from ._q_quick3_d_render_extension import QQuick3DRenderExtension
  from ._q_quick3_d_repeater import QQuick3DRepeater
  from ._q_quick3_d_shader_utils_buffer import QQuick3DShaderUtilsBuffer
  from ._q_quick3_d_shader_utils_render_command import QQuick3DShaderUtilsRenderCommand
  from ._q_quick3_d_shader_utils_render_pass_texture import QQuick3DShaderUtilsRenderPassTexture
  from ._q_quick3_d_shader_utils_shader import QQuick3DShaderUtilsShader
  from ._q_quick3_d_skeleton import QQuick3DSkeleton
  from ._q_quick3_d_skin import QQuick3DSkin
  from ._q_quick3_d_texture_data import QQuick3DTextureData
  from ._q_quick3_d_texture_data_private import QQuick3DTextureDataPrivate
  from ._q_quick3_d_texture_provider_extension_private import QQuick3DTextureProviderExtensionPrivate
  from ._q_quick3_d_window_attachment import QQuick3DWindowAttachment
  from ._q_quick3_d_custom_camera import QQuick3DCustomCamera
  from ._q_quick3_d_directional_light import QQuick3DDirectionalLight
  from ._q_quick3_d_file_instancing import QQuick3DFileInstancing
  from ._q_quick3_d_instance_list import QQuick3DInstanceList
  from ._q_quick3_d_joint import QQuick3DJoint
  from ._q_quick3_d_loader_incubator import QQuick3DLoaderIncubator
  from ._q_quick3_d_orthographic_camera import QQuick3DOrthographicCamera
  from ._q_quick3_d_perspective_camera import QQuick3DPerspectiveCamera
  from ._q_quick3_d_point_light import QQuick3DPointLight
  from ._q_quick3_d_property_watcher import QQuick3DPropertyWatcher
  from ._q_quick3_d_shader_utils_apply_value import QQuick3DShaderUtilsApplyValue
  from ._q_quick3_d_shader_utils_buffer_input import QQuick3DShaderUtilsBufferInput
  from ._q_quick3_d_shader_utils_pipeline_state_override import QQuick3DShaderUtilsPipelineStateOverride
  from ._q_quick3_d_shader_utils_render_pass import QQuick3DShaderUtilsRenderPass
  from ._q_quick3_d_shader_utils_render_pass_add_define import QQuick3DShaderUtilsRenderPassAddDefine
  from ._q_quick3_d_shader_utils_render_pass_color_attachment import QQuick3DShaderUtilsRenderPassColorAttachment
  from ._q_quick3_d_shader_utils_render_pass_depth_stencil_attachment import QQuick3DShaderUtilsRenderPassDepthStencilAttachment
  from ._q_quick3_d_shader_utils_render_pass_depth_texture_attachment import QQuick3DShaderUtilsRenderPassDepthTextureAttachment
  from ._q_quick3_d_shader_utils_renderables_filter import QQuick3DShaderUtilsRenderablesFilter
  from ._q_quick3_d_sky_material import QQuick3DSkyMaterial
  from ._q_quick3_d_spot_light import QQuick3DSpotLight
  from ._q_quick3_d_texture import QQuick3DTexture
  from ._q_quick3_d_texture_provider_extension import QQuick3DTextureProviderExtension
  from ._s_g_framebuffer_object_node import SGFramebufferObjectNode
  from ._q_quick3_d_cube_map_texture import QQuick3DCubeMapTexture
  from ._q_quick3_d_frustum_camera import QQuick3DFrustumCamera
  from ._q_quick3_d_material import QQuick3DMaterial
  from ._q_quick3_d_resource_loader import QQuick3DResourceLoader
  from ._q_quick3_d_shader_utils_texture_input import QQuick3DShaderUtilsTextureInput
  from ._q_quick3_d_custom_material import QQuick3DCustomMaterial
  from ._q_quick3_d_default_material import QQuick3DDefaultMaterial
  from ._q_quick3_d_effect import QQuick3DEffect
  from ._q_quick3_d_model import QQuick3DModel
  from ._q_quick3_d_principled_material import QQuick3DPrincipledMaterial
  from ._q_quick3_d_reflection_probe import QQuick3DReflectionProbe
  from ._q_quick3_d_render_pass import QQuick3DRenderPass
  from ._q_quick3_d_specular_glossy_material import QQuick3DSpecularGlossyMaterial
  from ._q_quick3_d_pick_result import QQuick3DPickResult
  from ._q_quick3_d_scene_environment import QQuick3DSceneEnvironment
  from ._q_quick3_d_shader_utils_sub_render_pass import QQuick3DShaderUtilsSubRenderPass
  from ._q_quick3_d_scene_renderer import QQuick3DSceneRenderer
  from ._q_quick3_d_viewport import QQuick3DViewport
  from ._q_quick3_d_lightmap_baker import QQuick3DLightmapBaker
  from ._q_quick3_d_render_layer_helpers import QQuick3DRenderLayerHelpers
  from ._q_quick3_d_s_g_direct_renderer import QQuick3DSGDirectRenderer
  from ._q_quick3_d_scene_root_node import QQuick3DSceneRootNode
  from . import QQuick3DPickResultEnums
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuick3D': '_q_quick3_d',
      'QQuick3DTextureInternalChange': '_q_quick3_d_texture_internal_change',
      'QQuick3DBakedLightmap': '_q_quick3_d_baked_lightmap',
      'QQuick3DBounds3': '_q_quick3_d_bounds3',
      'QQuick3DContentLayer': '_q_quick3_d_content_layer',
      'QQuick3DDebugSettings': '_q_quick3_d_debug_settings',
      'QQuick3DFog': '_q_quick3_d_fog',
      'QQuick3DLightmapper': '_q_quick3_d_lightmapper',
      'QQuick3DRenderPassTargetBlend': '_q_quick3_d_render_pass_target_blend',
      'QQuick3DSGRenderNode': '_q_quick3_d_s_g_render_node',
      'QQuick3DQuaternionUtils': '_q_quick3_d_quaternion_utils',
      'QQuick3DObject': '_q_quick3_d_object',
      'QQuick3DNode': '_q_quick3_d_node',
      'QQuick3DSceneManager': '_q_quick3_d_scene_manager',
      'QQuick3DObjectChangeListener': '_q_quick3_d_object_change_listener',
      'QQuick3DObjectPrivate': '_q_quick3_d_object_private',
      'QQuick3DNodePrivate': '_q_quick3_d_node_private',
      'QQuick3DQuaternionAnimation': '_q_quick3_d_quaternion_animation',
      'QQuick3DRenderStats': '_q_quick3_d_render_stats',
      'QSSGCleanupObject': '_q_s_s_g_cleanup_object',
      'QQuick3DAbstractLight': '_q_quick3_d_abstract_light',
      'QQuick3DCamera': '_q_quick3_d_camera',
      'QQuick3DExtensionHelpers': '_q_quick3_d_extension_helpers',
      'QQuick3DGeometry': '_q_quick3_d_geometry',
      'QQuick3DGeometryPrivate': '_q_quick3_d_geometry_private',
      'QQuick3DInstanceListEntry': '_q_quick3_d_instance_list_entry',
      'QQuick3DInstancing': '_q_quick3_d_instancing',
      'QQuick3DInstancingPrivate': '_q_quick3_d_instancing_private',
      'QQuick3DItem2D': '_q_quick3_d_item2_d',
      'QQuick3DLoader': '_q_quick3_d_loader',
      'QQuick3DMorphTarget': '_q_quick3_d_morph_target',
      'QQuick3DPropertyChangedTracker': '_q_quick3_d_property_changed_tracker',
      'QQuick3DRenderExtension': '_q_quick3_d_render_extension',
      'QQuick3DRepeater': '_q_quick3_d_repeater',
      'QQuick3DShaderUtilsBuffer': '_q_quick3_d_shader_utils_buffer',
      'QQuick3DShaderUtilsRenderCommand': '_q_quick3_d_shader_utils_render_command',
      'QQuick3DShaderUtilsRenderPassTexture': '_q_quick3_d_shader_utils_render_pass_texture',
      'QQuick3DShaderUtilsShader': '_q_quick3_d_shader_utils_shader',
      'QQuick3DSkeleton': '_q_quick3_d_skeleton',
      'QQuick3DSkin': '_q_quick3_d_skin',
      'QQuick3DTextureData': '_q_quick3_d_texture_data',
      'QQuick3DTextureDataPrivate': '_q_quick3_d_texture_data_private',
      'QQuick3DTextureProviderExtensionPrivate': '_q_quick3_d_texture_provider_extension_private',
      'QQuick3DWindowAttachment': '_q_quick3_d_window_attachment',
      'QQuick3DCustomCamera': '_q_quick3_d_custom_camera',
      'QQuick3DDirectionalLight': '_q_quick3_d_directional_light',
      'QQuick3DFileInstancing': '_q_quick3_d_file_instancing',
      'QQuick3DInstanceList': '_q_quick3_d_instance_list',
      'QQuick3DJoint': '_q_quick3_d_joint',
      'QQuick3DLoaderIncubator': '_q_quick3_d_loader_incubator',
      'QQuick3DOrthographicCamera': '_q_quick3_d_orthographic_camera',
      'QQuick3DPerspectiveCamera': '_q_quick3_d_perspective_camera',
      'QQuick3DPointLight': '_q_quick3_d_point_light',
      'QQuick3DPropertyWatcher': '_q_quick3_d_property_watcher',
      'QQuick3DShaderUtilsApplyValue': '_q_quick3_d_shader_utils_apply_value',
      'QQuick3DShaderUtilsBufferInput': '_q_quick3_d_shader_utils_buffer_input',
      'QQuick3DShaderUtilsPipelineStateOverride': '_q_quick3_d_shader_utils_pipeline_state_override',
      'QQuick3DShaderUtilsRenderPass': '_q_quick3_d_shader_utils_render_pass',
      'QQuick3DShaderUtilsRenderPassAddDefine': '_q_quick3_d_shader_utils_render_pass_add_define',
      'QQuick3DShaderUtilsRenderPassColorAttachment': '_q_quick3_d_shader_utils_render_pass_color_attachment',
      'QQuick3DShaderUtilsRenderPassDepthStencilAttachment': '_q_quick3_d_shader_utils_render_pass_depth_stencil_attachment',
      'QQuick3DShaderUtilsRenderPassDepthTextureAttachment': '_q_quick3_d_shader_utils_render_pass_depth_texture_attachment',
      'QQuick3DShaderUtilsRenderablesFilter': '_q_quick3_d_shader_utils_renderables_filter',
      'QQuick3DSkyMaterial': '_q_quick3_d_sky_material',
      'QQuick3DSpotLight': '_q_quick3_d_spot_light',
      'QQuick3DTexture': '_q_quick3_d_texture',
      'QQuick3DTextureProviderExtension': '_q_quick3_d_texture_provider_extension',
      'SGFramebufferObjectNode': '_s_g_framebuffer_object_node',
      'QQuick3DCubeMapTexture': '_q_quick3_d_cube_map_texture',
      'QQuick3DFrustumCamera': '_q_quick3_d_frustum_camera',
      'QQuick3DMaterial': '_q_quick3_d_material',
      'QQuick3DResourceLoader': '_q_quick3_d_resource_loader',
      'QQuick3DShaderUtilsTextureInput': '_q_quick3_d_shader_utils_texture_input',
      'QQuick3DCustomMaterial': '_q_quick3_d_custom_material',
      'QQuick3DDefaultMaterial': '_q_quick3_d_default_material',
      'QQuick3DEffect': '_q_quick3_d_effect',
      'QQuick3DModel': '_q_quick3_d_model',
      'QQuick3DPrincipledMaterial': '_q_quick3_d_principled_material',
      'QQuick3DReflectionProbe': '_q_quick3_d_reflection_probe',
      'QQuick3DRenderPass': '_q_quick3_d_render_pass',
      'QQuick3DSpecularGlossyMaterial': '_q_quick3_d_specular_glossy_material',
      'QQuick3DPickResult': '_q_quick3_d_pick_result',
      'QQuick3DSceneEnvironment': '_q_quick3_d_scene_environment',
      'QQuick3DShaderUtilsSubRenderPass': '_q_quick3_d_shader_utils_sub_render_pass',
      'QQuick3DSceneRenderer': '_q_quick3_d_scene_renderer',
      'QQuick3DViewport': '_q_quick3_d_viewport',
      'QQuick3DLightmapBaker': '_q_quick3_d_lightmap_baker',
      'QQuick3DRenderLayerHelpers': '_q_quick3_d_render_layer_helpers',
      'QQuick3DSGDirectRenderer': '_q_quick3_d_s_g_direct_renderer',
      'QQuick3DSceneRootNode': '_q_quick3_d_scene_root_node',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QQuick3DPickResultEnums',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuick3D import QQuick3DSceneRootNode'. Python calls
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
