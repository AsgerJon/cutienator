"""
The 'cutienator.QtQuick3DUtils' package provides the cute classes of the
part of Qt named QtQuick3DUtils, under the name PySide6 has for it.

  from cutienator.QtQuick3DUtils import QQuick3DProfilerData, QSSGAmbientOcclusionSettings

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
    'QQuick3DProfilerData',
    'QSSGAmbientOcclusionSettings',
    'QSSGLightmapUVGeneratorResult',
    'QSSGMeshBVH',
    'QSSGMeshBVHNode',
    'QSSGMeshBVHTriangle',
    'QSSGRenderFlag',
    'QSSGRenderTextureFormat',
    'QQuick3DProfilerSceneGraphData',
    'QSSGBaseTypeHelpers',
    'QSSGRenderVertexBufferEntry',
    'QQsbCollection',
    'QQuick3DProfiler',
    'QSSGBaseTypeProperty',
    'QQsbIODeviceCollection',
    'QQsbInMemoryCollection',
    'QSSGBounds3',
    'QSSGPlane',
    'RotationData',
    'QSSGFrustum',
    'QSSGLightmapUVGenerator',
    'QSSGMeshBVHBuilder',
    'QSSGMesh',
    'QSSGRenderShaderValue',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick3_d_profiler_data import QQuick3DProfilerData
  from ._q_s_s_g_ambient_occlusion_settings import QSSGAmbientOcclusionSettings
  from ._q_s_s_g_lightmap_u_v_generator_result import QSSGLightmapUVGeneratorResult
  from ._q_s_s_g_mesh_b_v_h import QSSGMeshBVH
  from ._q_s_s_g_mesh_b_v_h_node import QSSGMeshBVHNode
  from ._q_s_s_g_mesh_b_v_h_triangle import QSSGMeshBVHTriangle
  from ._q_s_s_g_render_flag import QSSGRenderFlag
  from ._q_s_s_g_render_texture_format import QSSGRenderTextureFormat
  from ._q_quick3_d_profiler_scene_graph_data import QQuick3DProfilerSceneGraphData
  from ._q_s_s_g_base_type_helpers import QSSGBaseTypeHelpers
  from ._q_s_s_g_render_vertex_buffer_entry import QSSGRenderVertexBufferEntry
  from ._q_qsb_collection import QQsbCollection
  from ._q_quick3_d_profiler import QQuick3DProfiler
  from ._q_s_s_g_base_type_property import QSSGBaseTypeProperty
  from ._q_qsb_i_o_device_collection import QQsbIODeviceCollection
  from ._q_qsb_in_memory_collection import QQsbInMemoryCollection
  from ._q_s_s_g_bounds3 import QSSGBounds3
  from ._q_s_s_g_plane import QSSGPlane
  from ._rotation_data import RotationData
  from ._q_s_s_g_frustum import QSSGFrustum
  from ._q_s_s_g_lightmap_u_v_generator import QSSGLightmapUVGenerator
  from ._q_s_s_g_mesh_b_v_h_builder import QSSGMeshBVHBuilder
  from . import QSSGMesh
  from . import QSSGRenderShaderValue
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuick3DProfilerData': '_q_quick3_d_profiler_data',
      'QSSGAmbientOcclusionSettings': '_q_s_s_g_ambient_occlusion_settings',
      'QSSGLightmapUVGeneratorResult': '_q_s_s_g_lightmap_u_v_generator_result',
      'QSSGMeshBVH': '_q_s_s_g_mesh_b_v_h',
      'QSSGMeshBVHNode': '_q_s_s_g_mesh_b_v_h_node',
      'QSSGMeshBVHTriangle': '_q_s_s_g_mesh_b_v_h_triangle',
      'QSSGRenderFlag': '_q_s_s_g_render_flag',
      'QSSGRenderTextureFormat': '_q_s_s_g_render_texture_format',
      'QQuick3DProfilerSceneGraphData': '_q_quick3_d_profiler_scene_graph_data',
      'QSSGBaseTypeHelpers': '_q_s_s_g_base_type_helpers',
      'QSSGRenderVertexBufferEntry': '_q_s_s_g_render_vertex_buffer_entry',
      'QQsbCollection': '_q_qsb_collection',
      'QQuick3DProfiler': '_q_quick3_d_profiler',
      'QSSGBaseTypeProperty': '_q_s_s_g_base_type_property',
      'QQsbIODeviceCollection': '_q_qsb_i_o_device_collection',
      'QQsbInMemoryCollection': '_q_qsb_in_memory_collection',
      'QSSGBounds3': '_q_s_s_g_bounds3',
      'QSSGPlane': '_q_s_s_g_plane',
      'RotationData': '_rotation_data',
      'QSSGFrustum': '_q_s_s_g_frustum',
      'QSSGLightmapUVGenerator': '_q_s_s_g_lightmap_u_v_generator',
      'QSSGMeshBVHBuilder': '_q_s_s_g_mesh_b_v_h_builder',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QSSGMesh', 'QSSGRenderShaderValue',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuick3DUtils import QSSGMeshBVHBuilder'. Python calls
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
