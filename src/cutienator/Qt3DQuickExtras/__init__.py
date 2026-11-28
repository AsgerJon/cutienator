"""
The 'cutienator.Qt3DQuickExtras' package provides the cute classes of
the part of Qt named Qt3DQuickExtras, under the name PySide6 has for it.

  from cutienator.Qt3DQuickExtras import QConeGeometryForeign, QConeGeometryViewForeign

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
    'QConeGeometryForeign',
    'QConeGeometryViewForeign',
    'QConeMeshForeign',
    'QCuboidGeometryForeign',
    'QCuboidGeometryViewForeign',
    'QCuboidMeshForeign',
    'QCylinderGeometryForeign',
    'QCylinderGeometryViewForeign',
    'QCylinderMeshForeign',
    'QDiffuseMapMaterialForeign',
    'QDiffuseSpecularMapMaterialForeign',
    'QDiffuseSpecularMaterialForeign',
    'QExtrudedTextGeometryForeign',
    'QExtrudedTextMeshForeign',
    'QFirstPersonCameraControllerForeign',
    'QForwardRendererForeign',
    'QGoochMaterialForeign',
    'QMetalRoughMaterialForeign',
    'QNormalDiffuseMapAlphaMaterialForeign',
    'QNormalDiffuseMapMaterialForeign',
    'QNormalDiffuseSpecularMapMaterialForeign',
    'QOrbitCameraControllerForeign',
    'QPerVertexColorMaterialForeign',
    'QPhongAlphaMaterialForeign',
    'QPhongMaterialForeign',
    'QPlaneGeometryForeign',
    'QPlaneGeometryViewForeign',
    'QPlaneMeshForeign',
    'QSkyboxEntityForeign',
    'QSphereGeometryForeign',
    'QSphereGeometryViewForeign',
    'QSphereMeshForeign',
    'QSpriteGridForeign',
    'QSpriteItemForeign',
    'QText2DEntityForeign',
    'QTextureMaterialForeign',
    'QTorusGeometryForeign',
    'QTorusGeometryViewForeign',
    'QTorusMeshForeign',
    'Qt3DQuick3DExtrasPlugin',
    'Qt3DExtras',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_cone_geometry_foreign import QConeGeometryForeign
  from ._q_cone_geometry_view_foreign import QConeGeometryViewForeign
  from ._q_cone_mesh_foreign import QConeMeshForeign
  from ._q_cuboid_geometry_foreign import QCuboidGeometryForeign
  from ._q_cuboid_geometry_view_foreign import QCuboidGeometryViewForeign
  from ._q_cuboid_mesh_foreign import QCuboidMeshForeign
  from ._q_cylinder_geometry_foreign import QCylinderGeometryForeign
  from ._q_cylinder_geometry_view_foreign import QCylinderGeometryViewForeign
  from ._q_cylinder_mesh_foreign import QCylinderMeshForeign
  from ._q_diffuse_map_material_foreign import QDiffuseMapMaterialForeign
  from ._q_diffuse_specular_map_material_foreign import QDiffuseSpecularMapMaterialForeign
  from ._q_diffuse_specular_material_foreign import QDiffuseSpecularMaterialForeign
  from ._q_extruded_text_geometry_foreign import QExtrudedTextGeometryForeign
  from ._q_extruded_text_mesh_foreign import QExtrudedTextMeshForeign
  from ._q_first_person_camera_controller_foreign import QFirstPersonCameraControllerForeign
  from ._q_forward_renderer_foreign import QForwardRendererForeign
  from ._q_gooch_material_foreign import QGoochMaterialForeign
  from ._q_metal_rough_material_foreign import QMetalRoughMaterialForeign
  from ._q_normal_diffuse_map_alpha_material_foreign import QNormalDiffuseMapAlphaMaterialForeign
  from ._q_normal_diffuse_map_material_foreign import QNormalDiffuseMapMaterialForeign
  from ._q_normal_diffuse_specular_map_material_foreign import QNormalDiffuseSpecularMapMaterialForeign
  from ._q_orbit_camera_controller_foreign import QOrbitCameraControllerForeign
  from ._q_per_vertex_color_material_foreign import QPerVertexColorMaterialForeign
  from ._q_phong_alpha_material_foreign import QPhongAlphaMaterialForeign
  from ._q_phong_material_foreign import QPhongMaterialForeign
  from ._q_plane_geometry_foreign import QPlaneGeometryForeign
  from ._q_plane_geometry_view_foreign import QPlaneGeometryViewForeign
  from ._q_plane_mesh_foreign import QPlaneMeshForeign
  from ._q_skybox_entity_foreign import QSkyboxEntityForeign
  from ._q_sphere_geometry_foreign import QSphereGeometryForeign
  from ._q_sphere_geometry_view_foreign import QSphereGeometryViewForeign
  from ._q_sphere_mesh_foreign import QSphereMeshForeign
  from ._q_sprite_grid_foreign import QSpriteGridForeign
  from ._q_sprite_item_foreign import QSpriteItemForeign
  from ._q_text2_d_entity_foreign import QText2DEntityForeign
  from ._q_texture_material_foreign import QTextureMaterialForeign
  from ._q_torus_geometry_foreign import QTorusGeometryForeign
  from ._q_torus_geometry_view_foreign import QTorusGeometryViewForeign
  from ._q_torus_mesh_foreign import QTorusMeshForeign
  from ._qt3_d_quick3_d_extras_plugin import Qt3DQuick3DExtrasPlugin
  from . import Qt3DExtras
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QConeGeometryForeign': '_q_cone_geometry_foreign',
      'QConeGeometryViewForeign': '_q_cone_geometry_view_foreign',
      'QConeMeshForeign': '_q_cone_mesh_foreign',
      'QCuboidGeometryForeign': '_q_cuboid_geometry_foreign',
      'QCuboidGeometryViewForeign': '_q_cuboid_geometry_view_foreign',
      'QCuboidMeshForeign': '_q_cuboid_mesh_foreign',
      'QCylinderGeometryForeign': '_q_cylinder_geometry_foreign',
      'QCylinderGeometryViewForeign': '_q_cylinder_geometry_view_foreign',
      'QCylinderMeshForeign': '_q_cylinder_mesh_foreign',
      'QDiffuseMapMaterialForeign': '_q_diffuse_map_material_foreign',
      'QDiffuseSpecularMapMaterialForeign': '_q_diffuse_specular_map_material_foreign',
      'QDiffuseSpecularMaterialForeign': '_q_diffuse_specular_material_foreign',
      'QExtrudedTextGeometryForeign': '_q_extruded_text_geometry_foreign',
      'QExtrudedTextMeshForeign': '_q_extruded_text_mesh_foreign',
      'QFirstPersonCameraControllerForeign': '_q_first_person_camera_controller_foreign',
      'QForwardRendererForeign': '_q_forward_renderer_foreign',
      'QGoochMaterialForeign': '_q_gooch_material_foreign',
      'QMetalRoughMaterialForeign': '_q_metal_rough_material_foreign',
      'QNormalDiffuseMapAlphaMaterialForeign': '_q_normal_diffuse_map_alpha_material_foreign',
      'QNormalDiffuseMapMaterialForeign': '_q_normal_diffuse_map_material_foreign',
      'QNormalDiffuseSpecularMapMaterialForeign': '_q_normal_diffuse_specular_map_material_foreign',
      'QOrbitCameraControllerForeign': '_q_orbit_camera_controller_foreign',
      'QPerVertexColorMaterialForeign': '_q_per_vertex_color_material_foreign',
      'QPhongAlphaMaterialForeign': '_q_phong_alpha_material_foreign',
      'QPhongMaterialForeign': '_q_phong_material_foreign',
      'QPlaneGeometryForeign': '_q_plane_geometry_foreign',
      'QPlaneGeometryViewForeign': '_q_plane_geometry_view_foreign',
      'QPlaneMeshForeign': '_q_plane_mesh_foreign',
      'QSkyboxEntityForeign': '_q_skybox_entity_foreign',
      'QSphereGeometryForeign': '_q_sphere_geometry_foreign',
      'QSphereGeometryViewForeign': '_q_sphere_geometry_view_foreign',
      'QSphereMeshForeign': '_q_sphere_mesh_foreign',
      'QSpriteGridForeign': '_q_sprite_grid_foreign',
      'QSpriteItemForeign': '_q_sprite_item_foreign',
      'QText2DEntityForeign': '_q_text2_d_entity_foreign',
      'QTextureMaterialForeign': '_q_texture_material_foreign',
      'QTorusGeometryForeign': '_q_torus_geometry_foreign',
      'QTorusGeometryViewForeign': '_q_torus_geometry_view_foreign',
      'QTorusMeshForeign': '_q_torus_mesh_foreign',
      'Qt3DQuick3DExtrasPlugin': '_qt3_d_quick3_d_extras_plugin',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('Qt3DExtras',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.Qt3DQuickExtras import Qt3DQuick3DExtrasPlugin'. Python calls
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
