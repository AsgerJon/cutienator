"""
The namespace 'Qt3DRender::Render::PickingUtils' of Qt, a package of 'cutienator.Qt3DRender':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DRender import Qt3DRender
  Qt3DRender.Render.PickingUtils.HierarchicalEntityPicker

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
    'HierarchicalEntityPicker',
    'PickConfiguration',
    'ViewportCameraAreaDetails',
    'ViewportCameraAreaGatherer',
    'AbstractCollisionGathererFunctor',
    'EntityCollisionGathererFunctor',
    'LineCollisionGathererFunctor',
    'PointCollisionGathererFunctor',
    'TriangleCollisionGathererFunctor',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ...._qt3_d_render__render__picking_utils__hierarchical_entity_picker import HierarchicalEntityPicker
  from ...._qt3_d_render__render__picking_utils__pick_configuration import PickConfiguration
  from ...._qt3_d_render__render__picking_utils__viewport_camera_area_details import ViewportCameraAreaDetails
  from ...._qt3_d_render__render__picking_utils__viewport_camera_area_gatherer import ViewportCameraAreaGatherer
  from ...._qt3_d_render__render__picking_utils__abstract_collision_gatherer_functor import AbstractCollisionGathererFunctor
  from ...._qt3_d_render__render__picking_utils__entity_collision_gatherer_functor import EntityCollisionGathererFunctor
  from ...._qt3_d_render__render__picking_utils__line_collision_gatherer_functor import LineCollisionGathererFunctor
  from ...._qt3_d_render__render__picking_utils__point_collision_gatherer_functor import PointCollisionGathererFunctor
  from ...._qt3_d_render__render__picking_utils__triangle_collision_gatherer_functor import TriangleCollisionGathererFunctor
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'HierarchicalEntityPicker': '_qt3_d_render__render__picking_utils__hierarchical_entity_picker',
      'PickConfiguration': '_qt3_d_render__render__picking_utils__pick_configuration',
      'ViewportCameraAreaDetails': '_qt3_d_render__render__picking_utils__viewport_camera_area_details',
      'ViewportCameraAreaGatherer': '_qt3_d_render__render__picking_utils__viewport_camera_area_gatherer',
      'AbstractCollisionGathererFunctor': '_qt3_d_render__render__picking_utils__abstract_collision_gatherer_functor',
      'EntityCollisionGathererFunctor': '_qt3_d_render__render__picking_utils__entity_collision_gatherer_functor',
      'LineCollisionGathererFunctor': '_qt3_d_render__render__picking_utils__line_collision_gatherer_functor',
      'PointCollisionGathererFunctor': '_qt3_d_render__render__picking_utils__point_collision_gatherer_functor',
      'TriangleCollisionGathererFunctor': '_qt3_d_render__render__picking_utils__triangle_collision_gatherer_functor',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by
    'Qt3DRender.Render.PickingUtils.HierarchicalEntityPicker'. Python calls
    this for a name the package does not hold yet, and what it gives is kept
    here for the next time.

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
      module = importlib.import_module('....%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
