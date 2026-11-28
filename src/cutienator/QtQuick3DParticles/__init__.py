"""
The 'cutienator.QtQuick3DParticles' package provides the cute classes of
the part of Qt named QtQuick3DParticles, under the name PySide6 has for
it.

  from cutienator.QtQuick3DParticles import Color4ub, QPRand

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
    'QPRand',
    'QQuick3DParticleData',
    'QQuick3DParticleDataCurrent',
    'QQuick3DParticleEmitBurstData',
    'Vector3b',
    'QQuick3DParticleAbstractShape',
    'QQuick3DParticleDirection',
    'QQuick3DParticleEmitBurst',
    'QQuick3DParticleShapeDataUtils',
    'QQuick3DParticleSpriteSequence',
    'QQuick3DParticleSystemLogging',
    'QQuick3DParticleCustomShape',
    'QQuick3DParticleDynamicBurst',
    'QQuick3DParticleShape',
    'QQuick3DParticleTargetDirection',
    'QQuick3DParticleVectorDirection',
    'QQuick3DParticleModelShape',
    'QQuick3DParticle',
    'QQuick3DParticleEmitter',
    'QQuick3DParticleModelBlendParticle',
    'QQuick3DParticleModelParticle',
    'QQuick3DParticleAffector',
    'QQuick3DParticleSpriteParticle',
    'QQuick3DParticleSystem',
    'QQuick3DParticleAttractor',
    'QQuick3DParticleGravity',
    'QQuick3DParticleLineParticle',
    'QQuick3DParticlePointRotator',
    'QQuick3DParticleRepeller',
    'QQuick3DParticleScaleAffector',
    'QQuick3DParticleSystemAnimation',
    'QQuick3DParticleSystemUpdate',
    'QQuick3DParticleTrailEmitter',
    'QQuick3DParticleWander',
    'QQuick3DParticleSceneShape',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._color4ub import Color4ub
  from ._q_p_rand import QPRand
  from ._q_quick3_d_particle_data import QQuick3DParticleData
  from ._q_quick3_d_particle_data_current import QQuick3DParticleDataCurrent
  from ._q_quick3_d_particle_emit_burst_data import QQuick3DParticleEmitBurstData
  from ._vector3b import Vector3b
  from ._q_quick3_d_particle_abstract_shape import QQuick3DParticleAbstractShape
  from ._q_quick3_d_particle_direction import QQuick3DParticleDirection
  from ._q_quick3_d_particle_emit_burst import QQuick3DParticleEmitBurst
  from ._q_quick3_d_particle_shape_data_utils import QQuick3DParticleShapeDataUtils
  from ._q_quick3_d_particle_sprite_sequence import QQuick3DParticleSpriteSequence
  from ._q_quick3_d_particle_system_logging import QQuick3DParticleSystemLogging
  from ._q_quick3_d_particle_custom_shape import QQuick3DParticleCustomShape
  from ._q_quick3_d_particle_dynamic_burst import QQuick3DParticleDynamicBurst
  from ._q_quick3_d_particle_shape import QQuick3DParticleShape
  from ._q_quick3_d_particle_target_direction import QQuick3DParticleTargetDirection
  from ._q_quick3_d_particle_vector_direction import QQuick3DParticleVectorDirection
  from ._q_quick3_d_particle_model_shape import QQuick3DParticleModelShape
  from ._q_quick3_d_particle import QQuick3DParticle
  from ._q_quick3_d_particle_emitter import QQuick3DParticleEmitter
  from ._q_quick3_d_particle_model_blend_particle import QQuick3DParticleModelBlendParticle
  from ._q_quick3_d_particle_model_particle import QQuick3DParticleModelParticle
  from ._q_quick3_d_particle_affector import QQuick3DParticleAffector
  from ._q_quick3_d_particle_sprite_particle import QQuick3DParticleSpriteParticle
  from ._q_quick3_d_particle_system import QQuick3DParticleSystem
  from ._q_quick3_d_particle_attractor import QQuick3DParticleAttractor
  from ._q_quick3_d_particle_gravity import QQuick3DParticleGravity
  from ._q_quick3_d_particle_line_particle import QQuick3DParticleLineParticle
  from ._q_quick3_d_particle_point_rotator import QQuick3DParticlePointRotator
  from ._q_quick3_d_particle_repeller import QQuick3DParticleRepeller
  from ._q_quick3_d_particle_scale_affector import QQuick3DParticleScaleAffector
  from ._q_quick3_d_particle_system_animation import QQuick3DParticleSystemAnimation
  from ._q_quick3_d_particle_system_update import QQuick3DParticleSystemUpdate
  from ._q_quick3_d_particle_trail_emitter import QQuick3DParticleTrailEmitter
  from ._q_quick3_d_particle_wander import QQuick3DParticleWander
  from ._q_quick3_d_particle_scene_shape import QQuick3DParticleSceneShape
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'Color4ub': '_color4ub',
      'QPRand': '_q_p_rand',
      'QQuick3DParticleData': '_q_quick3_d_particle_data',
      'QQuick3DParticleDataCurrent': '_q_quick3_d_particle_data_current',
      'QQuick3DParticleEmitBurstData': '_q_quick3_d_particle_emit_burst_data',
      'Vector3b': '_vector3b',
      'QQuick3DParticleAbstractShape': '_q_quick3_d_particle_abstract_shape',
      'QQuick3DParticleDirection': '_q_quick3_d_particle_direction',
      'QQuick3DParticleEmitBurst': '_q_quick3_d_particle_emit_burst',
      'QQuick3DParticleShapeDataUtils': '_q_quick3_d_particle_shape_data_utils',
      'QQuick3DParticleSpriteSequence': '_q_quick3_d_particle_sprite_sequence',
      'QQuick3DParticleSystemLogging': '_q_quick3_d_particle_system_logging',
      'QQuick3DParticleCustomShape': '_q_quick3_d_particle_custom_shape',
      'QQuick3DParticleDynamicBurst': '_q_quick3_d_particle_dynamic_burst',
      'QQuick3DParticleShape': '_q_quick3_d_particle_shape',
      'QQuick3DParticleTargetDirection': '_q_quick3_d_particle_target_direction',
      'QQuick3DParticleVectorDirection': '_q_quick3_d_particle_vector_direction',
      'QQuick3DParticleModelShape': '_q_quick3_d_particle_model_shape',
      'QQuick3DParticle': '_q_quick3_d_particle',
      'QQuick3DParticleEmitter': '_q_quick3_d_particle_emitter',
      'QQuick3DParticleModelBlendParticle': '_q_quick3_d_particle_model_blend_particle',
      'QQuick3DParticleModelParticle': '_q_quick3_d_particle_model_particle',
      'QQuick3DParticleAffector': '_q_quick3_d_particle_affector',
      'QQuick3DParticleSpriteParticle': '_q_quick3_d_particle_sprite_particle',
      'QQuick3DParticleSystem': '_q_quick3_d_particle_system',
      'QQuick3DParticleAttractor': '_q_quick3_d_particle_attractor',
      'QQuick3DParticleGravity': '_q_quick3_d_particle_gravity',
      'QQuick3DParticleLineParticle': '_q_quick3_d_particle_line_particle',
      'QQuick3DParticlePointRotator': '_q_quick3_d_particle_point_rotator',
      'QQuick3DParticleRepeller': '_q_quick3_d_particle_repeller',
      'QQuick3DParticleScaleAffector': '_q_quick3_d_particle_scale_affector',
      'QQuick3DParticleSystemAnimation': '_q_quick3_d_particle_system_animation',
      'QQuick3DParticleSystemUpdate': '_q_quick3_d_particle_system_update',
      'QQuick3DParticleTrailEmitter': '_q_quick3_d_particle_trail_emitter',
      'QQuick3DParticleWander': '_q_quick3_d_particle_wander',
      'QQuick3DParticleSceneShape': '_q_quick3_d_particle_scene_shape',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuick3DParticles import QQuick3DParticleSceneShape'. Python calls
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
