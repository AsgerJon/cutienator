"""
The 'cutienator.QtOpenGL' package provides the cute classes of the part
of Qt named QtOpenGL, under the name PySide6 has for it.

  from cutienator.QtOpenGL import QOpenGLBuffer, QOpenGLEngineShaderProg

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
    'QOpenGLBuffer',
    'QOpenGLEngineShaderProg',
    'QOpenGLFramebufferObjectFormatPrivate',
    'QOpenGLPixelTransferOptions',
    'QOpenGLVersionStatus',
    'QVkConvenience',
    'QOpenGLPoint',
    'QOpenGLDebugMessage',
    'QOpenGLFramebufferObject',
    'QOpenGLFramebufferObjectFormat',
    'QOpenGLRect',
    'QOpenGLDebugLogger',
    'QOpenGLTimeMonitor',
    'QOpenGLTimerQuery',
    'QOpenGLVertexArrayObject',
    'QOpenGLPaintDevice',
    'QOpenGLPaintDevicePrivate',
    'QOpenGLTexture',
    'QOpenGLTextureUploader',
    'QOpenGLVersionProfile',
    'QOpenGL2PaintEngineState',
    'QOpenGLTextureBlitter',
    'QOpenGLTextureHelper',
    'QAbstractOpenGLFunctions',
    'QOpenGL2PEXVertexArray',
    'QOpenGL2PaintEngineEx',
    'QOpenGLCachedTexture',
    'QOpenGLContextVersionData',
    'QOpenGLFramebufferObjectPrivate',
    'QOpenGLQueryHelper',
    'QOpenGLShader',
    'QOpenGLTexturePrivate',
    'QOpenGLVersionFunctionsBackend',
    'QOpenGLVersionFunctionsFactory',
    'QOpenGLVertexArrayObjectHelper',
    'QAbstractOpenGLFunctionsPrivate',
    'QOpenGL2GradientCache',
    'QOpenGLFunctions_1_0',
    'QOpenGLFunctions_1_0_CoreBackend',
    'QOpenGLFunctions_1_0_DeprecatedBackend',
    'QOpenGLFunctions_1_1',
    'QOpenGLFunctions_1_1_CoreBackend',
    'QOpenGLFunctions_1_1_DeprecatedBackend',
    'QOpenGLFunctions_1_2',
    'QOpenGLFunctions_1_2_CoreBackend',
    'QOpenGLFunctions_1_2_DeprecatedBackend',
    'QOpenGLFunctions_1_3',
    'QOpenGLFunctions_1_3_CoreBackend',
    'QOpenGLFunctions_1_3_DeprecatedBackend',
    'QOpenGLFunctions_1_4',
    'QOpenGLFunctions_1_4_CoreBackend',
    'QOpenGLFunctions_1_4_DeprecatedBackend',
    'QOpenGLFunctions_1_5',
    'QOpenGLFunctions_1_5_CoreBackend',
    'QOpenGLFunctions_2_0',
    'QOpenGLFunctions_2_0_CoreBackend',
    'QOpenGLFunctions_2_0_DeprecatedBackend',
    'QOpenGLFunctions_2_1',
    'QOpenGLFunctions_2_1_CoreBackend',
    'QOpenGLFunctions_3_0',
    'QOpenGLFunctions_3_0_CoreBackend',
    'QOpenGLFunctions_3_0_DeprecatedBackend',
    'QOpenGLFunctions_3_1',
    'QOpenGLFunctions_3_1_CoreBackend',
    'QOpenGLFunctions_3_2_Compatibility',
    'QOpenGLFunctions_3_2_Core',
    'QOpenGLFunctions_3_2_CoreBackend',
    'QOpenGLFunctions_3_3_Compatibility',
    'QOpenGLFunctions_3_3_Core',
    'QOpenGLFunctions_3_3_CoreBackend',
    'QOpenGLFunctions_3_3_DeprecatedBackend',
    'QOpenGLFunctions_4_0_Compatibility',
    'QOpenGLFunctions_4_0_Core',
    'QOpenGLFunctions_4_0_CoreBackend',
    'QOpenGLFunctions_4_1_Compatibility',
    'QOpenGLFunctions_4_1_Core',
    'QOpenGLFunctions_4_1_CoreBackend',
    'QOpenGLFunctions_4_2_Compatibility',
    'QOpenGLFunctions_4_2_Core',
    'QOpenGLFunctions_4_2_CoreBackend',
    'QOpenGLFunctions_4_3_Compatibility',
    'QOpenGLFunctions_4_3_Core',
    'QOpenGLFunctions_4_3_CoreBackend',
    'QOpenGLFunctions_4_4_Compatibility',
    'QOpenGLFunctions_4_4_Core',
    'QOpenGLFunctions_4_4_CoreBackend',
    'QOpenGLFunctions_4_5_Compatibility',
    'QOpenGLFunctions_4_5_Core',
    'QOpenGLFunctions_4_5_CoreBackend',
    'QOpenGLFunctions_4_5_DeprecatedBackend',
    'QOpenGLGlyphTexture',
    'QOpenGLShaderProgram',
    'QOpenGLTextureCache',
    'QOpenGLVersionFunctionsStorage',
    'QOpenGLWindow',
    'CachedShader',
    'QOpenGLCompositorBackingStore',
    'QOpenGLCustomShaderStage',
    'QOpenGLCompositorWindow',
    'QOpenGLEngineShaderManager',
    'QOpenGLEngineSharedShaders',
    'QOpenGL2PaintEngineExPrivate',
    'QOpenGLCompositor',
    'QOpenGLTextureGlyphCache',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_open_g_l_buffer import QOpenGLBuffer
  from ._q_open_g_l_engine_shader_prog import QOpenGLEngineShaderProg
  from ._q_open_g_l_framebuffer_object_format_private import QOpenGLFramebufferObjectFormatPrivate
  from ._q_open_g_l_pixel_transfer_options import QOpenGLPixelTransferOptions
  from ._q_open_g_l_version_status import QOpenGLVersionStatus
  from ._q_vk_convenience import QVkConvenience
  from ._q_open_g_l_point import QOpenGLPoint
  from ._q_open_g_l_debug_message import QOpenGLDebugMessage
  from ._q_open_g_l_framebuffer_object import QOpenGLFramebufferObject
  from ._q_open_g_l_framebuffer_object_format import QOpenGLFramebufferObjectFormat
  from ._q_open_g_l_rect import QOpenGLRect
  from ._q_open_g_l_debug_logger import QOpenGLDebugLogger
  from ._q_open_g_l_time_monitor import QOpenGLTimeMonitor
  from ._q_open_g_l_timer_query import QOpenGLTimerQuery
  from ._q_open_g_l_vertex_array_object import QOpenGLVertexArrayObject
  from ._q_open_g_l_paint_device import QOpenGLPaintDevice
  from ._q_open_g_l_paint_device_private import QOpenGLPaintDevicePrivate
  from ._q_open_g_l_texture import QOpenGLTexture
  from ._q_open_g_l_texture_uploader import QOpenGLTextureUploader
  from ._q_open_g_l_version_profile import QOpenGLVersionProfile
  from ._q_open_g_l2_paint_engine_state import QOpenGL2PaintEngineState
  from ._q_open_g_l_texture_blitter import QOpenGLTextureBlitter
  from ._q_open_g_l_texture_helper import QOpenGLTextureHelper
  from ._q_abstract_open_g_l_functions import QAbstractOpenGLFunctions
  from ._q_open_g_l2_p_e_x_vertex_array import QOpenGL2PEXVertexArray
  from ._q_open_g_l2_paint_engine_ex import QOpenGL2PaintEngineEx
  from ._q_open_g_l_cached_texture import QOpenGLCachedTexture
  from ._q_open_g_l_context_version_data import QOpenGLContextVersionData
  from ._q_open_g_l_framebuffer_object_private import QOpenGLFramebufferObjectPrivate
  from ._q_open_g_l_query_helper import QOpenGLQueryHelper
  from ._q_open_g_l_shader import QOpenGLShader
  from ._q_open_g_l_texture_private import QOpenGLTexturePrivate
  from ._q_open_g_l_version_functions_backend import QOpenGLVersionFunctionsBackend
  from ._q_open_g_l_version_functions_factory import QOpenGLVersionFunctionsFactory
  from ._q_open_g_l_vertex_array_object_helper import QOpenGLVertexArrayObjectHelper
  from ._q_abstract_open_g_l_functions_private import QAbstractOpenGLFunctionsPrivate
  from ._q_open_g_l2_gradient_cache import QOpenGL2GradientCache
  from ._q_open_g_l_functions_1_0 import QOpenGLFunctions_1_0
  from ._q_open_g_l_functions_1_0_core_backend import QOpenGLFunctions_1_0_CoreBackend
  from ._q_open_g_l_functions_1_0_deprecated_backend import QOpenGLFunctions_1_0_DeprecatedBackend
  from ._q_open_g_l_functions_1_1 import QOpenGLFunctions_1_1
  from ._q_open_g_l_functions_1_1_core_backend import QOpenGLFunctions_1_1_CoreBackend
  from ._q_open_g_l_functions_1_1_deprecated_backend import QOpenGLFunctions_1_1_DeprecatedBackend
  from ._q_open_g_l_functions_1_2 import QOpenGLFunctions_1_2
  from ._q_open_g_l_functions_1_2_core_backend import QOpenGLFunctions_1_2_CoreBackend
  from ._q_open_g_l_functions_1_2_deprecated_backend import QOpenGLFunctions_1_2_DeprecatedBackend
  from ._q_open_g_l_functions_1_3 import QOpenGLFunctions_1_3
  from ._q_open_g_l_functions_1_3_core_backend import QOpenGLFunctions_1_3_CoreBackend
  from ._q_open_g_l_functions_1_3_deprecated_backend import QOpenGLFunctions_1_3_DeprecatedBackend
  from ._q_open_g_l_functions_1_4 import QOpenGLFunctions_1_4
  from ._q_open_g_l_functions_1_4_core_backend import QOpenGLFunctions_1_4_CoreBackend
  from ._q_open_g_l_functions_1_4_deprecated_backend import QOpenGLFunctions_1_4_DeprecatedBackend
  from ._q_open_g_l_functions_1_5 import QOpenGLFunctions_1_5
  from ._q_open_g_l_functions_1_5_core_backend import QOpenGLFunctions_1_5_CoreBackend
  from ._q_open_g_l_functions_2_0 import QOpenGLFunctions_2_0
  from ._q_open_g_l_functions_2_0_core_backend import QOpenGLFunctions_2_0_CoreBackend
  from ._q_open_g_l_functions_2_0_deprecated_backend import QOpenGLFunctions_2_0_DeprecatedBackend
  from ._q_open_g_l_functions_2_1 import QOpenGLFunctions_2_1
  from ._q_open_g_l_functions_2_1_core_backend import QOpenGLFunctions_2_1_CoreBackend
  from ._q_open_g_l_functions_3_0 import QOpenGLFunctions_3_0
  from ._q_open_g_l_functions_3_0_core_backend import QOpenGLFunctions_3_0_CoreBackend
  from ._q_open_g_l_functions_3_0_deprecated_backend import QOpenGLFunctions_3_0_DeprecatedBackend
  from ._q_open_g_l_functions_3_1 import QOpenGLFunctions_3_1
  from ._q_open_g_l_functions_3_1_core_backend import QOpenGLFunctions_3_1_CoreBackend
  from ._q_open_g_l_functions_3_2_compatibility import QOpenGLFunctions_3_2_Compatibility
  from ._q_open_g_l_functions_3_2_core import QOpenGLFunctions_3_2_Core
  from ._q_open_g_l_functions_3_2_core_backend import QOpenGLFunctions_3_2_CoreBackend
  from ._q_open_g_l_functions_3_3_compatibility import QOpenGLFunctions_3_3_Compatibility
  from ._q_open_g_l_functions_3_3_core import QOpenGLFunctions_3_3_Core
  from ._q_open_g_l_functions_3_3_core_backend import QOpenGLFunctions_3_3_CoreBackend
  from ._q_open_g_l_functions_3_3_deprecated_backend import QOpenGLFunctions_3_3_DeprecatedBackend
  from ._q_open_g_l_functions_4_0_compatibility import QOpenGLFunctions_4_0_Compatibility
  from ._q_open_g_l_functions_4_0_core import QOpenGLFunctions_4_0_Core
  from ._q_open_g_l_functions_4_0_core_backend import QOpenGLFunctions_4_0_CoreBackend
  from ._q_open_g_l_functions_4_1_compatibility import QOpenGLFunctions_4_1_Compatibility
  from ._q_open_g_l_functions_4_1_core import QOpenGLFunctions_4_1_Core
  from ._q_open_g_l_functions_4_1_core_backend import QOpenGLFunctions_4_1_CoreBackend
  from ._q_open_g_l_functions_4_2_compatibility import QOpenGLFunctions_4_2_Compatibility
  from ._q_open_g_l_functions_4_2_core import QOpenGLFunctions_4_2_Core
  from ._q_open_g_l_functions_4_2_core_backend import QOpenGLFunctions_4_2_CoreBackend
  from ._q_open_g_l_functions_4_3_compatibility import QOpenGLFunctions_4_3_Compatibility
  from ._q_open_g_l_functions_4_3_core import QOpenGLFunctions_4_3_Core
  from ._q_open_g_l_functions_4_3_core_backend import QOpenGLFunctions_4_3_CoreBackend
  from ._q_open_g_l_functions_4_4_compatibility import QOpenGLFunctions_4_4_Compatibility
  from ._q_open_g_l_functions_4_4_core import QOpenGLFunctions_4_4_Core
  from ._q_open_g_l_functions_4_4_core_backend import QOpenGLFunctions_4_4_CoreBackend
  from ._q_open_g_l_functions_4_5_compatibility import QOpenGLFunctions_4_5_Compatibility
  from ._q_open_g_l_functions_4_5_core import QOpenGLFunctions_4_5_Core
  from ._q_open_g_l_functions_4_5_core_backend import QOpenGLFunctions_4_5_CoreBackend
  from ._q_open_g_l_functions_4_5_deprecated_backend import QOpenGLFunctions_4_5_DeprecatedBackend
  from ._q_open_g_l_glyph_texture import QOpenGLGlyphTexture
  from ._q_open_g_l_shader_program import QOpenGLShaderProgram
  from ._q_open_g_l_texture_cache import QOpenGLTextureCache
  from ._q_open_g_l_version_functions_storage import QOpenGLVersionFunctionsStorage
  from ._q_open_g_l_window import QOpenGLWindow
  from ._cached_shader import CachedShader
  from ._q_open_g_l_compositor_backing_store import QOpenGLCompositorBackingStore
  from ._q_open_g_l_custom_shader_stage import QOpenGLCustomShaderStage
  from ._q_open_g_l_compositor_window import QOpenGLCompositorWindow
  from ._q_open_g_l_engine_shader_manager import QOpenGLEngineShaderManager
  from ._q_open_g_l_engine_shared_shaders import QOpenGLEngineSharedShaders
  from ._q_open_g_l2_paint_engine_ex_private import QOpenGL2PaintEngineExPrivate
  from ._q_open_g_l_compositor import QOpenGLCompositor
  from ._q_open_g_l_texture_glyph_cache import QOpenGLTextureGlyphCache
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QOpenGLBuffer': '_q_open_g_l_buffer',
      'QOpenGLEngineShaderProg': '_q_open_g_l_engine_shader_prog',
      'QOpenGLFramebufferObjectFormatPrivate': '_q_open_g_l_framebuffer_object_format_private',
      'QOpenGLPixelTransferOptions': '_q_open_g_l_pixel_transfer_options',
      'QOpenGLVersionStatus': '_q_open_g_l_version_status',
      'QVkConvenience': '_q_vk_convenience',
      'QOpenGLPoint': '_q_open_g_l_point',
      'QOpenGLDebugMessage': '_q_open_g_l_debug_message',
      'QOpenGLFramebufferObject': '_q_open_g_l_framebuffer_object',
      'QOpenGLFramebufferObjectFormat': '_q_open_g_l_framebuffer_object_format',
      'QOpenGLRect': '_q_open_g_l_rect',
      'QOpenGLDebugLogger': '_q_open_g_l_debug_logger',
      'QOpenGLTimeMonitor': '_q_open_g_l_time_monitor',
      'QOpenGLTimerQuery': '_q_open_g_l_timer_query',
      'QOpenGLVertexArrayObject': '_q_open_g_l_vertex_array_object',
      'QOpenGLPaintDevice': '_q_open_g_l_paint_device',
      'QOpenGLPaintDevicePrivate': '_q_open_g_l_paint_device_private',
      'QOpenGLTexture': '_q_open_g_l_texture',
      'QOpenGLTextureUploader': '_q_open_g_l_texture_uploader',
      'QOpenGLVersionProfile': '_q_open_g_l_version_profile',
      'QOpenGL2PaintEngineState': '_q_open_g_l2_paint_engine_state',
      'QOpenGLTextureBlitter': '_q_open_g_l_texture_blitter',
      'QOpenGLTextureHelper': '_q_open_g_l_texture_helper',
      'QAbstractOpenGLFunctions': '_q_abstract_open_g_l_functions',
      'QOpenGL2PEXVertexArray': '_q_open_g_l2_p_e_x_vertex_array',
      'QOpenGL2PaintEngineEx': '_q_open_g_l2_paint_engine_ex',
      'QOpenGLCachedTexture': '_q_open_g_l_cached_texture',
      'QOpenGLContextVersionData': '_q_open_g_l_context_version_data',
      'QOpenGLFramebufferObjectPrivate': '_q_open_g_l_framebuffer_object_private',
      'QOpenGLQueryHelper': '_q_open_g_l_query_helper',
      'QOpenGLShader': '_q_open_g_l_shader',
      'QOpenGLTexturePrivate': '_q_open_g_l_texture_private',
      'QOpenGLVersionFunctionsBackend': '_q_open_g_l_version_functions_backend',
      'QOpenGLVersionFunctionsFactory': '_q_open_g_l_version_functions_factory',
      'QOpenGLVertexArrayObjectHelper': '_q_open_g_l_vertex_array_object_helper',
      'QAbstractOpenGLFunctionsPrivate': '_q_abstract_open_g_l_functions_private',
      'QOpenGL2GradientCache': '_q_open_g_l2_gradient_cache',
      'QOpenGLFunctions_1_0': '_q_open_g_l_functions_1_0',
      'QOpenGLFunctions_1_0_CoreBackend': '_q_open_g_l_functions_1_0_core_backend',
      'QOpenGLFunctions_1_0_DeprecatedBackend': '_q_open_g_l_functions_1_0_deprecated_backend',
      'QOpenGLFunctions_1_1': '_q_open_g_l_functions_1_1',
      'QOpenGLFunctions_1_1_CoreBackend': '_q_open_g_l_functions_1_1_core_backend',
      'QOpenGLFunctions_1_1_DeprecatedBackend': '_q_open_g_l_functions_1_1_deprecated_backend',
      'QOpenGLFunctions_1_2': '_q_open_g_l_functions_1_2',
      'QOpenGLFunctions_1_2_CoreBackend': '_q_open_g_l_functions_1_2_core_backend',
      'QOpenGLFunctions_1_2_DeprecatedBackend': '_q_open_g_l_functions_1_2_deprecated_backend',
      'QOpenGLFunctions_1_3': '_q_open_g_l_functions_1_3',
      'QOpenGLFunctions_1_3_CoreBackend': '_q_open_g_l_functions_1_3_core_backend',
      'QOpenGLFunctions_1_3_DeprecatedBackend': '_q_open_g_l_functions_1_3_deprecated_backend',
      'QOpenGLFunctions_1_4': '_q_open_g_l_functions_1_4',
      'QOpenGLFunctions_1_4_CoreBackend': '_q_open_g_l_functions_1_4_core_backend',
      'QOpenGLFunctions_1_4_DeprecatedBackend': '_q_open_g_l_functions_1_4_deprecated_backend',
      'QOpenGLFunctions_1_5': '_q_open_g_l_functions_1_5',
      'QOpenGLFunctions_1_5_CoreBackend': '_q_open_g_l_functions_1_5_core_backend',
      'QOpenGLFunctions_2_0': '_q_open_g_l_functions_2_0',
      'QOpenGLFunctions_2_0_CoreBackend': '_q_open_g_l_functions_2_0_core_backend',
      'QOpenGLFunctions_2_0_DeprecatedBackend': '_q_open_g_l_functions_2_0_deprecated_backend',
      'QOpenGLFunctions_2_1': '_q_open_g_l_functions_2_1',
      'QOpenGLFunctions_2_1_CoreBackend': '_q_open_g_l_functions_2_1_core_backend',
      'QOpenGLFunctions_3_0': '_q_open_g_l_functions_3_0',
      'QOpenGLFunctions_3_0_CoreBackend': '_q_open_g_l_functions_3_0_core_backend',
      'QOpenGLFunctions_3_0_DeprecatedBackend': '_q_open_g_l_functions_3_0_deprecated_backend',
      'QOpenGLFunctions_3_1': '_q_open_g_l_functions_3_1',
      'QOpenGLFunctions_3_1_CoreBackend': '_q_open_g_l_functions_3_1_core_backend',
      'QOpenGLFunctions_3_2_Compatibility': '_q_open_g_l_functions_3_2_compatibility',
      'QOpenGLFunctions_3_2_Core': '_q_open_g_l_functions_3_2_core',
      'QOpenGLFunctions_3_2_CoreBackend': '_q_open_g_l_functions_3_2_core_backend',
      'QOpenGLFunctions_3_3_Compatibility': '_q_open_g_l_functions_3_3_compatibility',
      'QOpenGLFunctions_3_3_Core': '_q_open_g_l_functions_3_3_core',
      'QOpenGLFunctions_3_3_CoreBackend': '_q_open_g_l_functions_3_3_core_backend',
      'QOpenGLFunctions_3_3_DeprecatedBackend': '_q_open_g_l_functions_3_3_deprecated_backend',
      'QOpenGLFunctions_4_0_Compatibility': '_q_open_g_l_functions_4_0_compatibility',
      'QOpenGLFunctions_4_0_Core': '_q_open_g_l_functions_4_0_core',
      'QOpenGLFunctions_4_0_CoreBackend': '_q_open_g_l_functions_4_0_core_backend',
      'QOpenGLFunctions_4_1_Compatibility': '_q_open_g_l_functions_4_1_compatibility',
      'QOpenGLFunctions_4_1_Core': '_q_open_g_l_functions_4_1_core',
      'QOpenGLFunctions_4_1_CoreBackend': '_q_open_g_l_functions_4_1_core_backend',
      'QOpenGLFunctions_4_2_Compatibility': '_q_open_g_l_functions_4_2_compatibility',
      'QOpenGLFunctions_4_2_Core': '_q_open_g_l_functions_4_2_core',
      'QOpenGLFunctions_4_2_CoreBackend': '_q_open_g_l_functions_4_2_core_backend',
      'QOpenGLFunctions_4_3_Compatibility': '_q_open_g_l_functions_4_3_compatibility',
      'QOpenGLFunctions_4_3_Core': '_q_open_g_l_functions_4_3_core',
      'QOpenGLFunctions_4_3_CoreBackend': '_q_open_g_l_functions_4_3_core_backend',
      'QOpenGLFunctions_4_4_Compatibility': '_q_open_g_l_functions_4_4_compatibility',
      'QOpenGLFunctions_4_4_Core': '_q_open_g_l_functions_4_4_core',
      'QOpenGLFunctions_4_4_CoreBackend': '_q_open_g_l_functions_4_4_core_backend',
      'QOpenGLFunctions_4_5_Compatibility': '_q_open_g_l_functions_4_5_compatibility',
      'QOpenGLFunctions_4_5_Core': '_q_open_g_l_functions_4_5_core',
      'QOpenGLFunctions_4_5_CoreBackend': '_q_open_g_l_functions_4_5_core_backend',
      'QOpenGLFunctions_4_5_DeprecatedBackend': '_q_open_g_l_functions_4_5_deprecated_backend',
      'QOpenGLGlyphTexture': '_q_open_g_l_glyph_texture',
      'QOpenGLShaderProgram': '_q_open_g_l_shader_program',
      'QOpenGLTextureCache': '_q_open_g_l_texture_cache',
      'QOpenGLVersionFunctionsStorage': '_q_open_g_l_version_functions_storage',
      'QOpenGLWindow': '_q_open_g_l_window',
      'CachedShader': '_cached_shader',
      'QOpenGLCompositorBackingStore': '_q_open_g_l_compositor_backing_store',
      'QOpenGLCustomShaderStage': '_q_open_g_l_custom_shader_stage',
      'QOpenGLCompositorWindow': '_q_open_g_l_compositor_window',
      'QOpenGLEngineShaderManager': '_q_open_g_l_engine_shader_manager',
      'QOpenGLEngineSharedShaders': '_q_open_g_l_engine_shared_shaders',
      'QOpenGL2PaintEngineExPrivate': '_q_open_g_l2_paint_engine_ex_private',
      'QOpenGLCompositor': '_q_open_g_l_compositor',
      'QOpenGLTextureGlyphCache': '_q_open_g_l_texture_glyph_cache',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtOpenGL import QOpenGLTextureGlyphCache'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
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
