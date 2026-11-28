"""
The namespace 'Qt3DRender::RayCasting' of Qt, a package of 'cutienator.Qt3DRender':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DRender import Qt3DRender
  Qt3DRender.RayCasting.QBoundingVolume

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
    'QBoundingVolume',
    'QBoundingVolumeProvider',
    'QCollisionQueryResult',
    'QRay3D',
    'BoundingSphere',
    'QCollisionQueryResultPrivate',
    'QAbstractCollisionQueryService',
    'QAbstractCollisionQueryServicePrivate',
    'QRayCastingService',
    'QRayCastingServicePrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._qt3_d_render__ray_casting__q_bounding_volume import QBoundingVolume
  from ..._qt3_d_render__ray_casting__q_bounding_volume_provider import QBoundingVolumeProvider
  from ..._qt3_d_render__ray_casting__q_collision_query_result import QCollisionQueryResult
  from ..._qt3_d_render__ray_casting__q_ray3_d import QRay3D
  from ..._qt3_d_render__ray_casting__bounding_sphere import BoundingSphere
  from ..._qt3_d_render__ray_casting__q_collision_query_result_private import QCollisionQueryResultPrivate
  from ..._qt3_d_render__ray_casting__q_abstract_collision_query_service import QAbstractCollisionQueryService
  from ..._qt3_d_render__ray_casting__q_abstract_collision_query_service_private import QAbstractCollisionQueryServicePrivate
  from ..._qt3_d_render__ray_casting__q_ray_casting_service import QRayCastingService
  from ..._qt3_d_render__ray_casting__q_ray_casting_service_private import QRayCastingServicePrivate
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'QBoundingVolume': '_qt3_d_render__ray_casting__q_bounding_volume',
      'QBoundingVolumeProvider': '_qt3_d_render__ray_casting__q_bounding_volume_provider',
      'QCollisionQueryResult': '_qt3_d_render__ray_casting__q_collision_query_result',
      'QRay3D': '_qt3_d_render__ray_casting__q_ray3_d',
      'BoundingSphere': '_qt3_d_render__ray_casting__bounding_sphere',
      'QCollisionQueryResultPrivate': '_qt3_d_render__ray_casting__q_collision_query_result_private',
      'QAbstractCollisionQueryService': '_qt3_d_render__ray_casting__q_abstract_collision_query_service',
      'QAbstractCollisionQueryServicePrivate': '_qt3_d_render__ray_casting__q_abstract_collision_query_service_private',
      'QRayCastingService': '_qt3_d_render__ray_casting__q_ray_casting_service',
      'QRayCastingServicePrivate': '_qt3_d_render__ray_casting__q_ray_casting_service_private',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DRender.RayCasting.QBoundingVolume'. Python calls
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
      module = importlib.import_module('...%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
