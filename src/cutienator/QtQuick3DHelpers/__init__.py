"""
The 'cutienator.QtQuick3DHelpers' package provides the cute classes of
the part of Qt named QtQuick3DHelpers, under the name PySide6 has for
it.

  from cutienator.QtQuick3DHelpers import ProceduralMeshSubset, QQuick3DInfiniteGrid

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
    'ProceduralMeshSubset',
    'QQuick3DInfiniteGrid',
    'LookAtNode',
    'QQuick3DInstanceRange',
    'CapsuleGeometry',
    'ConeGeometry',
    'CuboidGeometry',
    'CylinderGeometry',
    'ExtrudedTextGeometry',
    'GridGeometry',
    'HeightFieldGeometry',
    'InstanceModel',
    'InstanceRepeater',
    'PlaneGeometry',
    'ProceduralMesh',
    'ProceduralSkyTextureData',
    'QQuick3DRandomInstancing',
    'QQuick3DTextureDataFrontend',
    'SphereGeometry',
    'TorusGeometry',
    'QQuick3DQuadTextureProvider',
    'QQuick3DSimpleQuadRenderer',
    'QQuick3DRenderOutputProvider',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._procedural_mesh_subset import ProceduralMeshSubset
  from ._q_quick3_d_infinite_grid import QQuick3DInfiniteGrid
  from ._look_at_node import LookAtNode
  from ._q_quick3_d_instance_range import QQuick3DInstanceRange
  from ._capsule_geometry import CapsuleGeometry
  from ._cone_geometry import ConeGeometry
  from ._cuboid_geometry import CuboidGeometry
  from ._cylinder_geometry import CylinderGeometry
  from ._extruded_text_geometry import ExtrudedTextGeometry
  from ._grid_geometry import GridGeometry
  from ._height_field_geometry import HeightFieldGeometry
  from ._instance_model import InstanceModel
  from ._instance_repeater import InstanceRepeater
  from ._plane_geometry import PlaneGeometry
  from ._procedural_mesh import ProceduralMesh
  from ._procedural_sky_texture_data import ProceduralSkyTextureData
  from ._q_quick3_d_random_instancing import QQuick3DRandomInstancing
  from ._q_quick3_d_texture_data_frontend import QQuick3DTextureDataFrontend
  from ._sphere_geometry import SphereGeometry
  from ._torus_geometry import TorusGeometry
  from ._q_quick3_d_quad_texture_provider import QQuick3DQuadTextureProvider
  from ._q_quick3_d_simple_quad_renderer import QQuick3DSimpleQuadRenderer
  from ._q_quick3_d_render_output_provider import QQuick3DRenderOutputProvider
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'ProceduralMeshSubset': '_procedural_mesh_subset',
      'QQuick3DInfiniteGrid': '_q_quick3_d_infinite_grid',
      'LookAtNode': '_look_at_node',
      'QQuick3DInstanceRange': '_q_quick3_d_instance_range',
      'CapsuleGeometry': '_capsule_geometry',
      'ConeGeometry': '_cone_geometry',
      'CuboidGeometry': '_cuboid_geometry',
      'CylinderGeometry': '_cylinder_geometry',
      'ExtrudedTextGeometry': '_extruded_text_geometry',
      'GridGeometry': '_grid_geometry',
      'HeightFieldGeometry': '_height_field_geometry',
      'InstanceModel': '_instance_model',
      'InstanceRepeater': '_instance_repeater',
      'PlaneGeometry': '_plane_geometry',
      'ProceduralMesh': '_procedural_mesh',
      'ProceduralSkyTextureData': '_procedural_sky_texture_data',
      'QQuick3DRandomInstancing': '_q_quick3_d_random_instancing',
      'QQuick3DTextureDataFrontend': '_q_quick3_d_texture_data_frontend',
      'SphereGeometry': '_sphere_geometry',
      'TorusGeometry': '_torus_geometry',
      'QQuick3DQuadTextureProvider': '_q_quick3_d_quad_texture_provider',
      'QQuick3DSimpleQuadRenderer': '_q_quick3_d_simple_quad_renderer',
      'QQuick3DRenderOutputProvider': '_q_quick3_d_render_output_provider',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuick3DHelpers import QQuick3DRenderOutputProvider'. Python calls
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
