"""
The 'cutienator.QtQuickParticles' package provides the cute classes of
the part of Qt named QtQuickParticles, under the name PySide6 has for
it.

  from cutienator.QtQuickParticles import Color4ub, ColoredPointVertex

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
    'Color4ub',
    'ColoredPointVertex',
    'ColoredVertex',
    'DeformableVertex',
    'QQuickParticleDataHeapNode',
    'SimplePointVertex',
    'SpriteVertex',
    'WanderData',
    'QQuickDirection',
    'QQuickItemParticleAttached',
    'QQuickParticleExtruder',
    'QQuickAngleDirection',
    'QQuickCumulativeDirection',
    'QQuickEllipseExtruder',
    'QQuickLineExtruder',
    'QQuickMaskExtruder',
    'QQuickPointDirection',
    'QQuickRectangleExtruder',
    'QQuickParticleData',
    'QQuickParticleSystem',
    'QQuickV4ParticleData',
    'QQuickParticleAffector',
    'QQuickParticleEmitter',
    'QQuickParticleGroup',
    'QQuickParticleGroupData',
    'QQuickParticlePainter',
    'QQuickTargetDirection',
    'ImageMaterial',
    'QQuickAgeAffector',
    'QQuickAttractorAffector',
    'QQuickCustomAffector',
    'QQuickFrictionAffector',
    'QQuickGravityAffector',
    'QQuickGroupGoalAffector',
    'QQuickImageParticle',
    'QQuickItemParticle',
    'QQuickParticleDataHeap',
    'QQuickParticleSystemAnimation',
    'QQuickSpriteGoalAffector',
    'QQuickTrailEmitter',
    'QQuickTurbulenceAffector',
    'QQuickWanderAffector',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._color4ub import Color4ub
  from ._colored_point_vertex import ColoredPointVertex
  from ._colored_vertex import ColoredVertex
  from ._deformable_vertex import DeformableVertex
  from ._q_quick_particle_data_heap_node import QQuickParticleDataHeapNode
  from ._simple_point_vertex import SimplePointVertex
  from ._sprite_vertex import SpriteVertex
  from ._wander_data import WanderData
  from ._q_quick_direction import QQuickDirection
  from ._q_quick_item_particle_attached import QQuickItemParticleAttached
  from ._q_quick_particle_extruder import QQuickParticleExtruder
  from ._q_quick_angle_direction import QQuickAngleDirection
  from ._q_quick_cumulative_direction import QQuickCumulativeDirection
  from ._q_quick_ellipse_extruder import QQuickEllipseExtruder
  from ._q_quick_line_extruder import QQuickLineExtruder
  from ._q_quick_mask_extruder import QQuickMaskExtruder
  from ._q_quick_point_direction import QQuickPointDirection
  from ._q_quick_rectangle_extruder import QQuickRectangleExtruder
  from ._q_quick_particle_data import QQuickParticleData
  from ._q_quick_particle_system import QQuickParticleSystem
  from ._q_quick_v4_particle_data import QQuickV4ParticleData
  from ._q_quick_particle_affector import QQuickParticleAffector
  from ._q_quick_particle_emitter import QQuickParticleEmitter
  from ._q_quick_particle_group import QQuickParticleGroup
  from ._q_quick_particle_group_data import QQuickParticleGroupData
  from ._q_quick_particle_painter import QQuickParticlePainter
  from ._q_quick_target_direction import QQuickTargetDirection
  from ._image_material import ImageMaterial
  from ._q_quick_age_affector import QQuickAgeAffector
  from ._q_quick_attractor_affector import QQuickAttractorAffector
  from ._q_quick_custom_affector import QQuickCustomAffector
  from ._q_quick_friction_affector import QQuickFrictionAffector
  from ._q_quick_gravity_affector import QQuickGravityAffector
  from ._q_quick_group_goal_affector import QQuickGroupGoalAffector
  from ._q_quick_image_particle import QQuickImageParticle
  from ._q_quick_item_particle import QQuickItemParticle
  from ._q_quick_particle_data_heap import QQuickParticleDataHeap
  from ._q_quick_particle_system_animation import QQuickParticleSystemAnimation
  from ._q_quick_sprite_goal_affector import QQuickSpriteGoalAffector
  from ._q_quick_trail_emitter import QQuickTrailEmitter
  from ._q_quick_turbulence_affector import QQuickTurbulenceAffector
  from ._q_quick_wander_affector import QQuickWanderAffector
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'Color4ub': '_color4ub',
      'ColoredPointVertex': '_colored_point_vertex',
      'ColoredVertex': '_colored_vertex',
      'DeformableVertex': '_deformable_vertex',
      'QQuickParticleDataHeapNode': '_q_quick_particle_data_heap_node',
      'SimplePointVertex': '_simple_point_vertex',
      'SpriteVertex': '_sprite_vertex',
      'WanderData': '_wander_data',
      'QQuickDirection': '_q_quick_direction',
      'QQuickItemParticleAttached': '_q_quick_item_particle_attached',
      'QQuickParticleExtruder': '_q_quick_particle_extruder',
      'QQuickAngleDirection': '_q_quick_angle_direction',
      'QQuickCumulativeDirection': '_q_quick_cumulative_direction',
      'QQuickEllipseExtruder': '_q_quick_ellipse_extruder',
      'QQuickLineExtruder': '_q_quick_line_extruder',
      'QQuickMaskExtruder': '_q_quick_mask_extruder',
      'QQuickPointDirection': '_q_quick_point_direction',
      'QQuickRectangleExtruder': '_q_quick_rectangle_extruder',
      'QQuickParticleData': '_q_quick_particle_data',
      'QQuickParticleSystem': '_q_quick_particle_system',
      'QQuickV4ParticleData': '_q_quick_v4_particle_data',
      'QQuickParticleAffector': '_q_quick_particle_affector',
      'QQuickParticleEmitter': '_q_quick_particle_emitter',
      'QQuickParticleGroup': '_q_quick_particle_group',
      'QQuickParticleGroupData': '_q_quick_particle_group_data',
      'QQuickParticlePainter': '_q_quick_particle_painter',
      'QQuickTargetDirection': '_q_quick_target_direction',
      'ImageMaterial': '_image_material',
      'QQuickAgeAffector': '_q_quick_age_affector',
      'QQuickAttractorAffector': '_q_quick_attractor_affector',
      'QQuickCustomAffector': '_q_quick_custom_affector',
      'QQuickFrictionAffector': '_q_quick_friction_affector',
      'QQuickGravityAffector': '_q_quick_gravity_affector',
      'QQuickGroupGoalAffector': '_q_quick_group_goal_affector',
      'QQuickImageParticle': '_q_quick_image_particle',
      'QQuickItemParticle': '_q_quick_item_particle',
      'QQuickParticleDataHeap': '_q_quick_particle_data_heap',
      'QQuickParticleSystemAnimation': '_q_quick_particle_system_animation',
      'QQuickSpriteGoalAffector': '_q_quick_sprite_goal_affector',
      'QQuickTrailEmitter': '_q_quick_trail_emitter',
      'QQuickTurbulenceAffector': '_q_quick_turbulence_affector',
      'QQuickWanderAffector': '_q_quick_wander_affector',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuickParticles import QQuickWanderAffector'. Python calls
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
