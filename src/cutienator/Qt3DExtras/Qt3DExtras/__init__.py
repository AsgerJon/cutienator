"""
The namespace 'Qt3DExtras' of Qt, a package of 'cutienator.Qt3DExtras':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DExtras import Qt3DExtras
  Qt3DExtras.AtlasTexture

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'AtlasTexture',
    'QTextureAtlasGenerator',
    'AreaAllocator',
    'QSpriteSheetItem',
    'QSpriteSheetItemPrivate',
    'DistanceFieldTextRenderer',
    'DistanceFieldTextRendererPrivate',
    'QAbstractCameraControllerPrivate',
    'QAbstractSpriteSheet',
    'QAbstractSpriteSheetPrivate',
    'QDistanceFieldGlyphCache',
    'QSkyboxEntity',
    'QSkyboxEntityPrivate',
    'QText2DEntity',
    'QText2DEntityPrivate',
    'QTextureAtlasData',
    'QTextureAtlasPrivate',
    'QDiffuseMapMaterial',
    'QDiffuseMapMaterialPrivate',
    'QDiffuseSpecularMapMaterial',
    'QDiffuseSpecularMapMaterialPrivate',
    'QDiffuseSpecularMaterial',
    'QDiffuseSpecularMaterialPrivate',
    'QForwardRenderer',
    'QForwardRendererPrivate',
    'QGoochMaterial',
    'QGoochMaterialPrivate',
    'QMetalRoughMaterial',
    'QMetalRoughMaterialPrivate',
    'QMorphPhongMaterial',
    'QMorphPhongMaterialPrivate',
    'QNormalDiffuseMapMaterial',
    'QNormalDiffuseMapMaterialPrivate',
    'QNormalDiffuseSpecularMapMaterial',
    'QNormalDiffuseSpecularMapMaterialPrivate',
    'QOrbitCameraControllerPrivate',
    'QPerVertexColorMaterial',
    'QPerVertexColorMaterialPrivate',
    'QPhongAlphaMaterial',
    'QPhongAlphaMaterialPrivate',
    'QPhongMaterial',
    'QPhongMaterialPrivate',
    'QSpriteGrid',
    'QSpriteGridPrivate',
    'QSpriteSheet',
    'QSpriteSheetPrivate',
    'QText2DMaterial',
    'QText2DMaterialPrivate',
    'QTextureAtlas',
    'QTextureMaterial',
    'QTextureMaterialPrivate',
    'QAbstractCameraController',
    'QConeGeometry',
    'QConeGeometryPrivate',
    'QConeGeometryView',
    'QCuboidGeometry',
    'QCuboidGeometryPrivate',
    'QCuboidGeometryView',
    'QCylinderGeometry',
    'QCylinderGeometryPrivate',
    'QCylinderGeometryView',
    'QExtrudedTextGeometry',
    'QExtrudedTextGeometryPrivate',
    'QNormalDiffuseMapAlphaMaterial',
    'QNormalDiffuseMapAlphaMaterialPrivate',
    'QPlaneGeometry',
    'QPlaneGeometryPrivate',
    'QPlaneGeometryView',
    'QSphereGeometry',
    'QSphereGeometryPrivate',
    'QSphereGeometryView',
    'QTorusGeometry',
    'QTorusGeometryPrivate',
    'QTorusGeometryView',
    'QConeMesh',
    'QCuboidMesh',
    'QCylinderMesh',
    'QExtrudedTextMesh',
    'QFirstPersonCameraController',
    'QOrbitCameraController',
    'QPlaneMesh',
    'QSphereMesh',
    'QTorusMesh',
    'Qt3DWindow',
    'Qt3DWindowPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt3_d_extras__atlas_texture import AtlasTexture
  from .._qt3_d_extras__q_texture_atlas_generator import QTextureAtlasGenerator
  from .._qt3_d_extras__area_allocator import AreaAllocator
  from .._qt3_d_extras__q_sprite_sheet_item import QSpriteSheetItem
  from .._qt3_d_extras__q_sprite_sheet_item_private import QSpriteSheetItemPrivate
  from .._qt3_d_extras__distance_field_text_renderer import DistanceFieldTextRenderer
  from .._qt3_d_extras__distance_field_text_renderer_private import DistanceFieldTextRendererPrivate
  from .._qt3_d_extras__q_abstract_camera_controller_private import QAbstractCameraControllerPrivate
  from .._qt3_d_extras__q_abstract_sprite_sheet import QAbstractSpriteSheet
  from .._qt3_d_extras__q_abstract_sprite_sheet_private import QAbstractSpriteSheetPrivate
  from .._qt3_d_extras__q_distance_field_glyph_cache import QDistanceFieldGlyphCache
  from .._qt3_d_extras__q_skybox_entity import QSkyboxEntity
  from .._qt3_d_extras__q_skybox_entity_private import QSkyboxEntityPrivate
  from .._qt3_d_extras__q_text2_d_entity import QText2DEntity
  from .._qt3_d_extras__q_text2_d_entity_private import QText2DEntityPrivate
  from .._qt3_d_extras__q_texture_atlas_data import QTextureAtlasData
  from .._qt3_d_extras__q_texture_atlas_private import QTextureAtlasPrivate
  from .._qt3_d_extras__q_diffuse_map_material import QDiffuseMapMaterial
  from .._qt3_d_extras__q_diffuse_map_material_private import QDiffuseMapMaterialPrivate
  from .._qt3_d_extras__q_diffuse_specular_map_material import QDiffuseSpecularMapMaterial
  from .._qt3_d_extras__q_diffuse_specular_map_material_private import QDiffuseSpecularMapMaterialPrivate
  from .._qt3_d_extras__q_diffuse_specular_material import QDiffuseSpecularMaterial
  from .._qt3_d_extras__q_diffuse_specular_material_private import QDiffuseSpecularMaterialPrivate
  from .._qt3_d_extras__q_forward_renderer import QForwardRenderer
  from .._qt3_d_extras__q_forward_renderer_private import QForwardRendererPrivate
  from .._qt3_d_extras__q_gooch_material import QGoochMaterial
  from .._qt3_d_extras__q_gooch_material_private import QGoochMaterialPrivate
  from .._qt3_d_extras__q_metal_rough_material import QMetalRoughMaterial
  from .._qt3_d_extras__q_metal_rough_material_private import QMetalRoughMaterialPrivate
  from .._qt3_d_extras__q_morph_phong_material import QMorphPhongMaterial
  from .._qt3_d_extras__q_morph_phong_material_private import QMorphPhongMaterialPrivate
  from .._qt3_d_extras__q_normal_diffuse_map_material import QNormalDiffuseMapMaterial
  from .._qt3_d_extras__q_normal_diffuse_map_material_private import QNormalDiffuseMapMaterialPrivate
  from .._qt3_d_extras__q_normal_diffuse_specular_map_material import QNormalDiffuseSpecularMapMaterial
  from .._qt3_d_extras__q_normal_diffuse_specular_map_material_private import QNormalDiffuseSpecularMapMaterialPrivate
  from .._qt3_d_extras__q_orbit_camera_controller_private import QOrbitCameraControllerPrivate
  from .._qt3_d_extras__q_per_vertex_color_material import QPerVertexColorMaterial
  from .._qt3_d_extras__q_per_vertex_color_material_private import QPerVertexColorMaterialPrivate
  from .._qt3_d_extras__q_phong_alpha_material import QPhongAlphaMaterial
  from .._qt3_d_extras__q_phong_alpha_material_private import QPhongAlphaMaterialPrivate
  from .._qt3_d_extras__q_phong_material import QPhongMaterial
  from .._qt3_d_extras__q_phong_material_private import QPhongMaterialPrivate
  from .._qt3_d_extras__q_sprite_grid import QSpriteGrid
  from .._qt3_d_extras__q_sprite_grid_private import QSpriteGridPrivate
  from .._qt3_d_extras__q_sprite_sheet import QSpriteSheet
  from .._qt3_d_extras__q_sprite_sheet_private import QSpriteSheetPrivate
  from .._qt3_d_extras__q_text2_d_material import QText2DMaterial
  from .._qt3_d_extras__q_text2_d_material_private import QText2DMaterialPrivate
  from .._qt3_d_extras__q_texture_atlas import QTextureAtlas
  from .._qt3_d_extras__q_texture_material import QTextureMaterial
  from .._qt3_d_extras__q_texture_material_private import QTextureMaterialPrivate
  from .._qt3_d_extras__q_abstract_camera_controller import QAbstractCameraController
  from .._qt3_d_extras__q_cone_geometry import QConeGeometry
  from .._qt3_d_extras__q_cone_geometry_private import QConeGeometryPrivate
  from .._qt3_d_extras__q_cone_geometry_view import QConeGeometryView
  from .._qt3_d_extras__q_cuboid_geometry import QCuboidGeometry
  from .._qt3_d_extras__q_cuboid_geometry_private import QCuboidGeometryPrivate
  from .._qt3_d_extras__q_cuboid_geometry_view import QCuboidGeometryView
  from .._qt3_d_extras__q_cylinder_geometry import QCylinderGeometry
  from .._qt3_d_extras__q_cylinder_geometry_private import QCylinderGeometryPrivate
  from .._qt3_d_extras__q_cylinder_geometry_view import QCylinderGeometryView
  from .._qt3_d_extras__q_extruded_text_geometry import QExtrudedTextGeometry
  from .._qt3_d_extras__q_extruded_text_geometry_private import QExtrudedTextGeometryPrivate
  from .._qt3_d_extras__q_normal_diffuse_map_alpha_material import QNormalDiffuseMapAlphaMaterial
  from .._qt3_d_extras__q_normal_diffuse_map_alpha_material_private import QNormalDiffuseMapAlphaMaterialPrivate
  from .._qt3_d_extras__q_plane_geometry import QPlaneGeometry
  from .._qt3_d_extras__q_plane_geometry_private import QPlaneGeometryPrivate
  from .._qt3_d_extras__q_plane_geometry_view import QPlaneGeometryView
  from .._qt3_d_extras__q_sphere_geometry import QSphereGeometry
  from .._qt3_d_extras__q_sphere_geometry_private import QSphereGeometryPrivate
  from .._qt3_d_extras__q_sphere_geometry_view import QSphereGeometryView
  from .._qt3_d_extras__q_torus_geometry import QTorusGeometry
  from .._qt3_d_extras__q_torus_geometry_private import QTorusGeometryPrivate
  from .._qt3_d_extras__q_torus_geometry_view import QTorusGeometryView
  from .._qt3_d_extras__q_cone_mesh import QConeMesh
  from .._qt3_d_extras__q_cuboid_mesh import QCuboidMesh
  from .._qt3_d_extras__q_cylinder_mesh import QCylinderMesh
  from .._qt3_d_extras__q_extruded_text_mesh import QExtrudedTextMesh
  from .._qt3_d_extras__q_first_person_camera_controller import QFirstPersonCameraController
  from .._qt3_d_extras__q_orbit_camera_controller import QOrbitCameraController
  from .._qt3_d_extras__q_plane_mesh import QPlaneMesh
  from .._qt3_d_extras__q_sphere_mesh import QSphereMesh
  from .._qt3_d_extras__q_torus_mesh import QTorusMesh
  from .._qt3_d_extras__qt3_d_window import Qt3DWindow
  from .._qt3_d_extras__qt3_d_window_private import Qt3DWindowPrivate
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'AtlasTexture': '_qt3_d_extras__atlas_texture',
      'QTextureAtlasGenerator': '_qt3_d_extras__q_texture_atlas_generator',
      'AreaAllocator': '_qt3_d_extras__area_allocator',
      'QSpriteSheetItem': '_qt3_d_extras__q_sprite_sheet_item',
      'QSpriteSheetItemPrivate': '_qt3_d_extras__q_sprite_sheet_item_private',
      'DistanceFieldTextRenderer': '_qt3_d_extras__distance_field_text_renderer',
      'DistanceFieldTextRendererPrivate': '_qt3_d_extras__distance_field_text_renderer_private',
      'QAbstractCameraControllerPrivate': '_qt3_d_extras__q_abstract_camera_controller_private',
      'QAbstractSpriteSheet': '_qt3_d_extras__q_abstract_sprite_sheet',
      'QAbstractSpriteSheetPrivate': '_qt3_d_extras__q_abstract_sprite_sheet_private',
      'QDistanceFieldGlyphCache': '_qt3_d_extras__q_distance_field_glyph_cache',
      'QSkyboxEntity': '_qt3_d_extras__q_skybox_entity',
      'QSkyboxEntityPrivate': '_qt3_d_extras__q_skybox_entity_private',
      'QText2DEntity': '_qt3_d_extras__q_text2_d_entity',
      'QText2DEntityPrivate': '_qt3_d_extras__q_text2_d_entity_private',
      'QTextureAtlasData': '_qt3_d_extras__q_texture_atlas_data',
      'QTextureAtlasPrivate': '_qt3_d_extras__q_texture_atlas_private',
      'QDiffuseMapMaterial': '_qt3_d_extras__q_diffuse_map_material',
      'QDiffuseMapMaterialPrivate': '_qt3_d_extras__q_diffuse_map_material_private',
      'QDiffuseSpecularMapMaterial': '_qt3_d_extras__q_diffuse_specular_map_material',
      'QDiffuseSpecularMapMaterialPrivate': '_qt3_d_extras__q_diffuse_specular_map_material_private',
      'QDiffuseSpecularMaterial': '_qt3_d_extras__q_diffuse_specular_material',
      'QDiffuseSpecularMaterialPrivate': '_qt3_d_extras__q_diffuse_specular_material_private',
      'QForwardRenderer': '_qt3_d_extras__q_forward_renderer',
      'QForwardRendererPrivate': '_qt3_d_extras__q_forward_renderer_private',
      'QGoochMaterial': '_qt3_d_extras__q_gooch_material',
      'QGoochMaterialPrivate': '_qt3_d_extras__q_gooch_material_private',
      'QMetalRoughMaterial': '_qt3_d_extras__q_metal_rough_material',
      'QMetalRoughMaterialPrivate': '_qt3_d_extras__q_metal_rough_material_private',
      'QMorphPhongMaterial': '_qt3_d_extras__q_morph_phong_material',
      'QMorphPhongMaterialPrivate': '_qt3_d_extras__q_morph_phong_material_private',
      'QNormalDiffuseMapMaterial': '_qt3_d_extras__q_normal_diffuse_map_material',
      'QNormalDiffuseMapMaterialPrivate': '_qt3_d_extras__q_normal_diffuse_map_material_private',
      'QNormalDiffuseSpecularMapMaterial': '_qt3_d_extras__q_normal_diffuse_specular_map_material',
      'QNormalDiffuseSpecularMapMaterialPrivate': '_qt3_d_extras__q_normal_diffuse_specular_map_material_private',
      'QOrbitCameraControllerPrivate': '_qt3_d_extras__q_orbit_camera_controller_private',
      'QPerVertexColorMaterial': '_qt3_d_extras__q_per_vertex_color_material',
      'QPerVertexColorMaterialPrivate': '_qt3_d_extras__q_per_vertex_color_material_private',
      'QPhongAlphaMaterial': '_qt3_d_extras__q_phong_alpha_material',
      'QPhongAlphaMaterialPrivate': '_qt3_d_extras__q_phong_alpha_material_private',
      'QPhongMaterial': '_qt3_d_extras__q_phong_material',
      'QPhongMaterialPrivate': '_qt3_d_extras__q_phong_material_private',
      'QSpriteGrid': '_qt3_d_extras__q_sprite_grid',
      'QSpriteGridPrivate': '_qt3_d_extras__q_sprite_grid_private',
      'QSpriteSheet': '_qt3_d_extras__q_sprite_sheet',
      'QSpriteSheetPrivate': '_qt3_d_extras__q_sprite_sheet_private',
      'QText2DMaterial': '_qt3_d_extras__q_text2_d_material',
      'QText2DMaterialPrivate': '_qt3_d_extras__q_text2_d_material_private',
      'QTextureAtlas': '_qt3_d_extras__q_texture_atlas',
      'QTextureMaterial': '_qt3_d_extras__q_texture_material',
      'QTextureMaterialPrivate': '_qt3_d_extras__q_texture_material_private',
      'QAbstractCameraController': '_qt3_d_extras__q_abstract_camera_controller',
      'QConeGeometry': '_qt3_d_extras__q_cone_geometry',
      'QConeGeometryPrivate': '_qt3_d_extras__q_cone_geometry_private',
      'QConeGeometryView': '_qt3_d_extras__q_cone_geometry_view',
      'QCuboidGeometry': '_qt3_d_extras__q_cuboid_geometry',
      'QCuboidGeometryPrivate': '_qt3_d_extras__q_cuboid_geometry_private',
      'QCuboidGeometryView': '_qt3_d_extras__q_cuboid_geometry_view',
      'QCylinderGeometry': '_qt3_d_extras__q_cylinder_geometry',
      'QCylinderGeometryPrivate': '_qt3_d_extras__q_cylinder_geometry_private',
      'QCylinderGeometryView': '_qt3_d_extras__q_cylinder_geometry_view',
      'QExtrudedTextGeometry': '_qt3_d_extras__q_extruded_text_geometry',
      'QExtrudedTextGeometryPrivate': '_qt3_d_extras__q_extruded_text_geometry_private',
      'QNormalDiffuseMapAlphaMaterial': '_qt3_d_extras__q_normal_diffuse_map_alpha_material',
      'QNormalDiffuseMapAlphaMaterialPrivate': '_qt3_d_extras__q_normal_diffuse_map_alpha_material_private',
      'QPlaneGeometry': '_qt3_d_extras__q_plane_geometry',
      'QPlaneGeometryPrivate': '_qt3_d_extras__q_plane_geometry_private',
      'QPlaneGeometryView': '_qt3_d_extras__q_plane_geometry_view',
      'QSphereGeometry': '_qt3_d_extras__q_sphere_geometry',
      'QSphereGeometryPrivate': '_qt3_d_extras__q_sphere_geometry_private',
      'QSphereGeometryView': '_qt3_d_extras__q_sphere_geometry_view',
      'QTorusGeometry': '_qt3_d_extras__q_torus_geometry',
      'QTorusGeometryPrivate': '_qt3_d_extras__q_torus_geometry_private',
      'QTorusGeometryView': '_qt3_d_extras__q_torus_geometry_view',
      'QConeMesh': '_qt3_d_extras__q_cone_mesh',
      'QCuboidMesh': '_qt3_d_extras__q_cuboid_mesh',
      'QCylinderMesh': '_qt3_d_extras__q_cylinder_mesh',
      'QExtrudedTextMesh': '_qt3_d_extras__q_extruded_text_mesh',
      'QFirstPersonCameraController': '_qt3_d_extras__q_first_person_camera_controller',
      'QOrbitCameraController': '_qt3_d_extras__q_orbit_camera_controller',
      'QPlaneMesh': '_qt3_d_extras__q_plane_mesh',
      'QSphereMesh': '_qt3_d_extras__q_sphere_mesh',
      'QTorusMesh': '_qt3_d_extras__q_torus_mesh',
      'Qt3DWindow': '_qt3_d_extras__qt3_d_window',
      'Qt3DWindowPrivate': '_qt3_d_extras__qt3_d_window_private',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DExtras.AtlasTexture'. Python calls this for a name
    the package does not hold yet, and what it gives is kept here for the
    next time.

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
    return [*__all__]
