"""
The 'cutienator.Qt3DQuickAnimation' package provides the cute classes of
the part of Qt named Qt3DQuickAnimation, under the name PySide6 has for
it.

  from cutienator.Qt3DQuickAnimation import QAbstractAnimationClipForeign, QAbstractAnimationForeign

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
    'QAbstractAnimationClipForeign',
    'QAbstractAnimationForeign',
    'QAbstractChannelMappingForeign',
    'QAbstractClipAnimatorForeign',
    'QAbstractClipBlendNodeForeign',
    'QAdditiveClipBlendForeign',
    'QAnimationClipForeign',
    'QAnimationClipLoaderForeign',
    'QAnimationControllerForeign',
    'QAnimationGroupForeign',
    'QBlendedClipAnimatorForeign',
    'QChannelMapperForeign',
    'QChannelMappingForeign',
    'QClipAnimatorForeign',
    'QClipBlendValueForeign',
    'QClockForeign',
    'QKeyframeAnimationForeign',
    'QLerpClipBlendForeign',
    'QMorphTargetForeign',
    'QMorphingAnimationForeign',
    'QSkeletonMappingForeign',
    'QVertexBlendAnimationForeign',
    'Qt3DQuick3DAnimationPlugin',
    'Qt3DAnimation',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_abstract_animation_clip_foreign import QAbstractAnimationClipForeign
  from ._q_abstract_animation_foreign import QAbstractAnimationForeign
  from ._q_abstract_channel_mapping_foreign import QAbstractChannelMappingForeign
  from ._q_abstract_clip_animator_foreign import QAbstractClipAnimatorForeign
  from ._q_abstract_clip_blend_node_foreign import QAbstractClipBlendNodeForeign
  from ._q_additive_clip_blend_foreign import QAdditiveClipBlendForeign
  from ._q_animation_clip_foreign import QAnimationClipForeign
  from ._q_animation_clip_loader_foreign import QAnimationClipLoaderForeign
  from ._q_animation_controller_foreign import QAnimationControllerForeign
  from ._q_animation_group_foreign import QAnimationGroupForeign
  from ._q_blended_clip_animator_foreign import QBlendedClipAnimatorForeign
  from ._q_channel_mapper_foreign import QChannelMapperForeign
  from ._q_channel_mapping_foreign import QChannelMappingForeign
  from ._q_clip_animator_foreign import QClipAnimatorForeign
  from ._q_clip_blend_value_foreign import QClipBlendValueForeign
  from ._q_clock_foreign import QClockForeign
  from ._q_keyframe_animation_foreign import QKeyframeAnimationForeign
  from ._q_lerp_clip_blend_foreign import QLerpClipBlendForeign
  from ._q_morph_target_foreign import QMorphTargetForeign
  from ._q_morphing_animation_foreign import QMorphingAnimationForeign
  from ._q_skeleton_mapping_foreign import QSkeletonMappingForeign
  from ._q_vertex_blend_animation_foreign import QVertexBlendAnimationForeign
  from ._qt3_d_quick3_d_animation_plugin import Qt3DQuick3DAnimationPlugin
  from . import Qt3DAnimation
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QAbstractAnimationClipForeign': '_q_abstract_animation_clip_foreign',
      'QAbstractAnimationForeign': '_q_abstract_animation_foreign',
      'QAbstractChannelMappingForeign': '_q_abstract_channel_mapping_foreign',
      'QAbstractClipAnimatorForeign': '_q_abstract_clip_animator_foreign',
      'QAbstractClipBlendNodeForeign': '_q_abstract_clip_blend_node_foreign',
      'QAdditiveClipBlendForeign': '_q_additive_clip_blend_foreign',
      'QAnimationClipForeign': '_q_animation_clip_foreign',
      'QAnimationClipLoaderForeign': '_q_animation_clip_loader_foreign',
      'QAnimationControllerForeign': '_q_animation_controller_foreign',
      'QAnimationGroupForeign': '_q_animation_group_foreign',
      'QBlendedClipAnimatorForeign': '_q_blended_clip_animator_foreign',
      'QChannelMapperForeign': '_q_channel_mapper_foreign',
      'QChannelMappingForeign': '_q_channel_mapping_foreign',
      'QClipAnimatorForeign': '_q_clip_animator_foreign',
      'QClipBlendValueForeign': '_q_clip_blend_value_foreign',
      'QClockForeign': '_q_clock_foreign',
      'QKeyframeAnimationForeign': '_q_keyframe_animation_foreign',
      'QLerpClipBlendForeign': '_q_lerp_clip_blend_foreign',
      'QMorphTargetForeign': '_q_morph_target_foreign',
      'QMorphingAnimationForeign': '_q_morphing_animation_foreign',
      'QSkeletonMappingForeign': '_q_skeleton_mapping_foreign',
      'QVertexBlendAnimationForeign': '_q_vertex_blend_animation_foreign',
      'Qt3DQuick3DAnimationPlugin': '_qt3_d_quick3_d_animation_plugin',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('Qt3DAnimation',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.Qt3DQuickAnimation import Qt3DQuick3DAnimationPlugin'. Python calls
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
