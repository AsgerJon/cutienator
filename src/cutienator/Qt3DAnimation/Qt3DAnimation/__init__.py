"""
The namespace 'Qt3DAnimation' of Qt, a package of 'cutienator.Qt3DAnimation':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DAnimation import Qt3DAnimation
  Qt3DAnimation.QAbstractChannelMappingData

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
    'QAbstractChannelMappingData',
    'QAbstractClipAnimatorData',
    'QAdditiveClipBlendData',
    'QAnimationClipChangeData',
    'QAnimationClipLoaderData',
    'QCallbackMappingData',
    'QChannelMapperData',
    'QChannelMappingData',
    'QClipBlendValueData',
    'QClockData',
    'QLerpClipBlendData',
    'QSkeletonMappingData',
    'QBlendedClipAnimatorData',
    'QClipAnimatorData',
    'QAnimationClipData',
    'QChannel',
    'QChannelComponent',
    'QAnimationCallback',
    'QAnimationControllerPrivate',
    'QAnimationGroupPrivate',
    'QMorphTargetPrivate',
    'QAbstractAnimation',
    'QAbstractAnimationClip',
    'QAbstractAnimationClipPrivate',
    'QAbstractAnimationPrivate',
    'QAbstractChannelMapping',
    'QAbstractClipBlendNode',
    'QAbstractClipBlendNodePrivate',
    'QAnimationAspect',
    'QAnimationAspectPrivate',
    'QChannelMapper',
    'QChannelMapperPrivate',
    'QClock',
    'QClockPrivate',
    'QKeyframeAnimationPrivate',
    'QMorphingAnimationPrivate',
    'QVertexBlendAnimationPrivate',
    'QAbstractChannelMappingPrivate',
    'QAbstractClipAnimator',
    'QAbstractClipAnimatorPrivate',
    'QAdditiveClipBlend',
    'QAdditiveClipBlendPrivate',
    'QAnimationClip',
    'QAnimationClipLoader',
    'QAnimationClipLoaderPrivate',
    'QAnimationClipPrivate',
    'QAnimationGroup',
    'QCallbackMapping',
    'QChannelMapping',
    'QClipBlendValue',
    'QClipBlendValuePrivate',
    'QLerpClipBlend',
    'QLerpClipBlendPrivate',
    'QSkeletonMapping',
    'QAnimationController',
    'QBlendedClipAnimator',
    'QBlendedClipAnimatorPrivate',
    'QCallbackMappingPrivate',
    'QChannelMappingPrivate',
    'QClipAnimator',
    'QClipAnimatorPrivate',
    'QKeyFrame',
    'QSkeletonMappingPrivate',
    'QKeyframeAnimation',
    'QMorphTarget',
    'QMorphingAnimation',
    'QVertexBlendAnimation',
    'Animation',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt3_d_animation__q_abstract_channel_mapping_data import QAbstractChannelMappingData
  from .._qt3_d_animation__q_abstract_clip_animator_data import QAbstractClipAnimatorData
  from .._qt3_d_animation__q_additive_clip_blend_data import QAdditiveClipBlendData
  from .._qt3_d_animation__q_animation_clip_change_data import QAnimationClipChangeData
  from .._qt3_d_animation__q_animation_clip_loader_data import QAnimationClipLoaderData
  from .._qt3_d_animation__q_callback_mapping_data import QCallbackMappingData
  from .._qt3_d_animation__q_channel_mapper_data import QChannelMapperData
  from .._qt3_d_animation__q_channel_mapping_data import QChannelMappingData
  from .._qt3_d_animation__q_clip_blend_value_data import QClipBlendValueData
  from .._qt3_d_animation__q_clock_data import QClockData
  from .._qt3_d_animation__q_lerp_clip_blend_data import QLerpClipBlendData
  from .._qt3_d_animation__q_skeleton_mapping_data import QSkeletonMappingData
  from .._qt3_d_animation__q_blended_clip_animator_data import QBlendedClipAnimatorData
  from .._qt3_d_animation__q_clip_animator_data import QClipAnimatorData
  from .._qt3_d_animation__q_animation_clip_data import QAnimationClipData
  from .._qt3_d_animation__q_channel import QChannel
  from .._qt3_d_animation__q_channel_component import QChannelComponent
  from .._qt3_d_animation__q_animation_callback import QAnimationCallback
  from .._qt3_d_animation__q_animation_controller_private import QAnimationControllerPrivate
  from .._qt3_d_animation__q_animation_group_private import QAnimationGroupPrivate
  from .._qt3_d_animation__q_morph_target_private import QMorphTargetPrivate
  from .._qt3_d_animation__q_abstract_animation import QAbstractAnimation
  from .._qt3_d_animation__q_abstract_animation_clip import QAbstractAnimationClip
  from .._qt3_d_animation__q_abstract_animation_clip_private import QAbstractAnimationClipPrivate
  from .._qt3_d_animation__q_abstract_animation_private import QAbstractAnimationPrivate
  from .._qt3_d_animation__q_abstract_channel_mapping import QAbstractChannelMapping
  from .._qt3_d_animation__q_abstract_clip_blend_node import QAbstractClipBlendNode
  from .._qt3_d_animation__q_abstract_clip_blend_node_private import QAbstractClipBlendNodePrivate
  from .._qt3_d_animation__q_animation_aspect import QAnimationAspect
  from .._qt3_d_animation__q_animation_aspect_private import QAnimationAspectPrivate
  from .._qt3_d_animation__q_channel_mapper import QChannelMapper
  from .._qt3_d_animation__q_channel_mapper_private import QChannelMapperPrivate
  from .._qt3_d_animation__q_clock import QClock
  from .._qt3_d_animation__q_clock_private import QClockPrivate
  from .._qt3_d_animation__q_keyframe_animation_private import QKeyframeAnimationPrivate
  from .._qt3_d_animation__q_morphing_animation_private import QMorphingAnimationPrivate
  from .._qt3_d_animation__q_vertex_blend_animation_private import QVertexBlendAnimationPrivate
  from .._qt3_d_animation__q_abstract_channel_mapping_private import QAbstractChannelMappingPrivate
  from .._qt3_d_animation__q_abstract_clip_animator import QAbstractClipAnimator
  from .._qt3_d_animation__q_abstract_clip_animator_private import QAbstractClipAnimatorPrivate
  from .._qt3_d_animation__q_additive_clip_blend import QAdditiveClipBlend
  from .._qt3_d_animation__q_additive_clip_blend_private import QAdditiveClipBlendPrivate
  from .._qt3_d_animation__q_animation_clip import QAnimationClip
  from .._qt3_d_animation__q_animation_clip_loader import QAnimationClipLoader
  from .._qt3_d_animation__q_animation_clip_loader_private import QAnimationClipLoaderPrivate
  from .._qt3_d_animation__q_animation_clip_private import QAnimationClipPrivate
  from .._qt3_d_animation__q_animation_group import QAnimationGroup
  from .._qt3_d_animation__q_callback_mapping import QCallbackMapping
  from .._qt3_d_animation__q_channel_mapping import QChannelMapping
  from .._qt3_d_animation__q_clip_blend_value import QClipBlendValue
  from .._qt3_d_animation__q_clip_blend_value_private import QClipBlendValuePrivate
  from .._qt3_d_animation__q_lerp_clip_blend import QLerpClipBlend
  from .._qt3_d_animation__q_lerp_clip_blend_private import QLerpClipBlendPrivate
  from .._qt3_d_animation__q_skeleton_mapping import QSkeletonMapping
  from .._qt3_d_animation__q_animation_controller import QAnimationController
  from .._qt3_d_animation__q_blended_clip_animator import QBlendedClipAnimator
  from .._qt3_d_animation__q_blended_clip_animator_private import QBlendedClipAnimatorPrivate
  from .._qt3_d_animation__q_callback_mapping_private import QCallbackMappingPrivate
  from .._qt3_d_animation__q_channel_mapping_private import QChannelMappingPrivate
  from .._qt3_d_animation__q_clip_animator import QClipAnimator
  from .._qt3_d_animation__q_clip_animator_private import QClipAnimatorPrivate
  from .._qt3_d_animation__q_key_frame import QKeyFrame
  from .._qt3_d_animation__q_skeleton_mapping_private import QSkeletonMappingPrivate
  from .._qt3_d_animation__q_keyframe_animation import QKeyframeAnimation
  from .._qt3_d_animation__q_morph_target import QMorphTarget
  from .._qt3_d_animation__q_morphing_animation import QMorphingAnimation
  from .._qt3_d_animation__q_vertex_blend_animation import QVertexBlendAnimation
  from . import Animation
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'QAbstractChannelMappingData': '_qt3_d_animation__q_abstract_channel_mapping_data',
      'QAbstractClipAnimatorData': '_qt3_d_animation__q_abstract_clip_animator_data',
      'QAdditiveClipBlendData': '_qt3_d_animation__q_additive_clip_blend_data',
      'QAnimationClipChangeData': '_qt3_d_animation__q_animation_clip_change_data',
      'QAnimationClipLoaderData': '_qt3_d_animation__q_animation_clip_loader_data',
      'QCallbackMappingData': '_qt3_d_animation__q_callback_mapping_data',
      'QChannelMapperData': '_qt3_d_animation__q_channel_mapper_data',
      'QChannelMappingData': '_qt3_d_animation__q_channel_mapping_data',
      'QClipBlendValueData': '_qt3_d_animation__q_clip_blend_value_data',
      'QClockData': '_qt3_d_animation__q_clock_data',
      'QLerpClipBlendData': '_qt3_d_animation__q_lerp_clip_blend_data',
      'QSkeletonMappingData': '_qt3_d_animation__q_skeleton_mapping_data',
      'QBlendedClipAnimatorData': '_qt3_d_animation__q_blended_clip_animator_data',
      'QClipAnimatorData': '_qt3_d_animation__q_clip_animator_data',
      'QAnimationClipData': '_qt3_d_animation__q_animation_clip_data',
      'QChannel': '_qt3_d_animation__q_channel',
      'QChannelComponent': '_qt3_d_animation__q_channel_component',
      'QAnimationCallback': '_qt3_d_animation__q_animation_callback',
      'QAnimationControllerPrivate': '_qt3_d_animation__q_animation_controller_private',
      'QAnimationGroupPrivate': '_qt3_d_animation__q_animation_group_private',
      'QMorphTargetPrivate': '_qt3_d_animation__q_morph_target_private',
      'QAbstractAnimation': '_qt3_d_animation__q_abstract_animation',
      'QAbstractAnimationClip': '_qt3_d_animation__q_abstract_animation_clip',
      'QAbstractAnimationClipPrivate': '_qt3_d_animation__q_abstract_animation_clip_private',
      'QAbstractAnimationPrivate': '_qt3_d_animation__q_abstract_animation_private',
      'QAbstractChannelMapping': '_qt3_d_animation__q_abstract_channel_mapping',
      'QAbstractClipBlendNode': '_qt3_d_animation__q_abstract_clip_blend_node',
      'QAbstractClipBlendNodePrivate': '_qt3_d_animation__q_abstract_clip_blend_node_private',
      'QAnimationAspect': '_qt3_d_animation__q_animation_aspect',
      'QAnimationAspectPrivate': '_qt3_d_animation__q_animation_aspect_private',
      'QChannelMapper': '_qt3_d_animation__q_channel_mapper',
      'QChannelMapperPrivate': '_qt3_d_animation__q_channel_mapper_private',
      'QClock': '_qt3_d_animation__q_clock',
      'QClockPrivate': '_qt3_d_animation__q_clock_private',
      'QKeyframeAnimationPrivate': '_qt3_d_animation__q_keyframe_animation_private',
      'QMorphingAnimationPrivate': '_qt3_d_animation__q_morphing_animation_private',
      'QVertexBlendAnimationPrivate': '_qt3_d_animation__q_vertex_blend_animation_private',
      'QAbstractChannelMappingPrivate': '_qt3_d_animation__q_abstract_channel_mapping_private',
      'QAbstractClipAnimator': '_qt3_d_animation__q_abstract_clip_animator',
      'QAbstractClipAnimatorPrivate': '_qt3_d_animation__q_abstract_clip_animator_private',
      'QAdditiveClipBlend': '_qt3_d_animation__q_additive_clip_blend',
      'QAdditiveClipBlendPrivate': '_qt3_d_animation__q_additive_clip_blend_private',
      'QAnimationClip': '_qt3_d_animation__q_animation_clip',
      'QAnimationClipLoader': '_qt3_d_animation__q_animation_clip_loader',
      'QAnimationClipLoaderPrivate': '_qt3_d_animation__q_animation_clip_loader_private',
      'QAnimationClipPrivate': '_qt3_d_animation__q_animation_clip_private',
      'QAnimationGroup': '_qt3_d_animation__q_animation_group',
      'QCallbackMapping': '_qt3_d_animation__q_callback_mapping',
      'QChannelMapping': '_qt3_d_animation__q_channel_mapping',
      'QClipBlendValue': '_qt3_d_animation__q_clip_blend_value',
      'QClipBlendValuePrivate': '_qt3_d_animation__q_clip_blend_value_private',
      'QLerpClipBlend': '_qt3_d_animation__q_lerp_clip_blend',
      'QLerpClipBlendPrivate': '_qt3_d_animation__q_lerp_clip_blend_private',
      'QSkeletonMapping': '_qt3_d_animation__q_skeleton_mapping',
      'QAnimationController': '_qt3_d_animation__q_animation_controller',
      'QBlendedClipAnimator': '_qt3_d_animation__q_blended_clip_animator',
      'QBlendedClipAnimatorPrivate': '_qt3_d_animation__q_blended_clip_animator_private',
      'QCallbackMappingPrivate': '_qt3_d_animation__q_callback_mapping_private',
      'QChannelMappingPrivate': '_qt3_d_animation__q_channel_mapping_private',
      'QClipAnimator': '_qt3_d_animation__q_clip_animator',
      'QClipAnimatorPrivate': '_qt3_d_animation__q_clip_animator_private',
      'QKeyFrame': '_qt3_d_animation__q_key_frame',
      'QSkeletonMappingPrivate': '_qt3_d_animation__q_skeleton_mapping_private',
      'QKeyframeAnimation': '_qt3_d_animation__q_keyframe_animation',
      'QMorphTarget': '_qt3_d_animation__q_morph_target',
      'QMorphingAnimation': '_qt3_d_animation__q_morphing_animation',
      'QVertexBlendAnimation': '_qt3_d_animation__q_vertex_blend_animation',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('Animation',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DAnimation.QAbstractChannelMappingData'. Python
    calls this for a name the package does not hold yet, and what it gives is
    kept here for the next time.

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
