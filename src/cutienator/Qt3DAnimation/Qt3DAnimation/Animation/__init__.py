"""
The namespace 'Qt3DAnimation::Animation' of Qt, a package of 'cutienator.Qt3DAnimation':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DAnimation import Qt3DAnimation
  Qt3DAnimation.Animation.AnimationCallbackAndValue

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from ..._qt3_d_animation__animation import Animation as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'AnimationCallbackAndValue',
    'AnimationClipLoaderManager',
    'AnimationRecord',
    'AnimatorEvaluationData',
    'BezierEvaluator',
    'BlendedClipAnimatorManager',
    'ChannelMapperManager',
    'ChannelMappingManager',
    'ClipAnimatorManager',
    'ClipEvaluationData',
    'ClipFormat',
    'ClockManager',
    'ComponentValue',
    'FunctionRangeFinder',
    'Keyframe',
    'MappingData',
    'SkeletonManager',
    'AbstractEvaluateClipAnimatorJob',
    'BuildBlendTreesJob',
    'ClipBlendNodeManager',
    'ClipBlendNodeVisitor',
    'FindRunningClipAnimatorsJob',
    'Handler',
    'LoadAnimationClipJob',
    'EvaluateBlendClipAnimatorJob',
    'EvaluateClipAnimatorJob',
    'ChannelNameAndType',
    'Channel',
    'ChannelComponent',
    'FCurve',
    'BackendNode',
    'AnimationClip',
    'BlendedClipAnimator',
    'ChannelMapper',
    'ChannelMapping',
    'ClipAnimator',
    'ClipBlendNode',
    'Clock',
    'GLTFImporter',
    'AdditiveClipBlend',
    'ClipBlendValue',
    'LerpClipBlend',
    'Skeleton',
    'JobTypes',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._qt3_d_animation__animation__animation_callback_and_value import AnimationCallbackAndValue
  from ..._qt3_d_animation__animation__animation_clip_loader_manager import AnimationClipLoaderManager
  from ..._qt3_d_animation__animation__animation_record import AnimationRecord
  from ..._qt3_d_animation__animation__animator_evaluation_data import AnimatorEvaluationData
  from ..._qt3_d_animation__animation__bezier_evaluator import BezierEvaluator
  from ..._qt3_d_animation__animation__blended_clip_animator_manager import BlendedClipAnimatorManager
  from ..._qt3_d_animation__animation__channel_mapper_manager import ChannelMapperManager
  from ..._qt3_d_animation__animation__channel_mapping_manager import ChannelMappingManager
  from ..._qt3_d_animation__animation__clip_animator_manager import ClipAnimatorManager
  from ..._qt3_d_animation__animation__clip_evaluation_data import ClipEvaluationData
  from ..._qt3_d_animation__animation__clip_format import ClipFormat
  from ..._qt3_d_animation__animation__clock_manager import ClockManager
  from ..._qt3_d_animation__animation__component_value import ComponentValue
  from ..._qt3_d_animation__animation__function_range_finder import FunctionRangeFinder
  from ..._qt3_d_animation__animation__keyframe import Keyframe
  from ..._qt3_d_animation__animation__mapping_data import MappingData
  from ..._qt3_d_animation__animation__skeleton_manager import SkeletonManager
  from ..._qt3_d_animation__animation__abstract_evaluate_clip_animator_job import AbstractEvaluateClipAnimatorJob
  from ..._qt3_d_animation__animation__build_blend_trees_job import BuildBlendTreesJob
  from ..._qt3_d_animation__animation__clip_blend_node_manager import ClipBlendNodeManager
  from ..._qt3_d_animation__animation__clip_blend_node_visitor import ClipBlendNodeVisitor
  from ..._qt3_d_animation__animation__find_running_clip_animators_job import FindRunningClipAnimatorsJob
  from ..._qt3_d_animation__animation__handler import Handler
  from ..._qt3_d_animation__animation__load_animation_clip_job import LoadAnimationClipJob
  from ..._qt3_d_animation__animation__evaluate_blend_clip_animator_job import EvaluateBlendClipAnimatorJob
  from ..._qt3_d_animation__animation__evaluate_clip_animator_job import EvaluateClipAnimatorJob
  from ..._qt3_d_animation__animation__channel_name_and_type import ChannelNameAndType
  from ..._qt3_d_animation__animation__channel import Channel
  from ..._qt3_d_animation__animation__channel_component import ChannelComponent
  from ..._qt3_d_animation__animation__f_curve import FCurve
  from ..._qt3_d_animation__animation__backend_node import BackendNode
  from ..._qt3_d_animation__animation__animation_clip import AnimationClip
  from ..._qt3_d_animation__animation__blended_clip_animator import BlendedClipAnimator
  from ..._qt3_d_animation__animation__channel_mapper import ChannelMapper
  from ..._qt3_d_animation__animation__channel_mapping import ChannelMapping
  from ..._qt3_d_animation__animation__clip_animator import ClipAnimator
  from ..._qt3_d_animation__animation__clip_blend_node import ClipBlendNode
  from ..._qt3_d_animation__animation__clock import Clock
  from ..._qt3_d_animation__animation__g_l_t_f_importer import GLTFImporter
  from ..._qt3_d_animation__animation__additive_clip_blend import AdditiveClipBlend
  from ..._qt3_d_animation__animation__clip_blend_value import ClipBlendValue
  from ..._qt3_d_animation__animation__lerp_clip_blend import LerpClipBlend
  from ..._qt3_d_animation__animation__skeleton import Skeleton
  from . import JobTypes
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'AnimationCallbackAndValue': '_qt3_d_animation__animation__animation_callback_and_value',
      'AnimationClipLoaderManager': '_qt3_d_animation__animation__animation_clip_loader_manager',
      'AnimationRecord': '_qt3_d_animation__animation__animation_record',
      'AnimatorEvaluationData': '_qt3_d_animation__animation__animator_evaluation_data',
      'BezierEvaluator': '_qt3_d_animation__animation__bezier_evaluator',
      'BlendedClipAnimatorManager': '_qt3_d_animation__animation__blended_clip_animator_manager',
      'ChannelMapperManager': '_qt3_d_animation__animation__channel_mapper_manager',
      'ChannelMappingManager': '_qt3_d_animation__animation__channel_mapping_manager',
      'ClipAnimatorManager': '_qt3_d_animation__animation__clip_animator_manager',
      'ClipEvaluationData': '_qt3_d_animation__animation__clip_evaluation_data',
      'ClipFormat': '_qt3_d_animation__animation__clip_format',
      'ClockManager': '_qt3_d_animation__animation__clock_manager',
      'ComponentValue': '_qt3_d_animation__animation__component_value',
      'FunctionRangeFinder': '_qt3_d_animation__animation__function_range_finder',
      'Keyframe': '_qt3_d_animation__animation__keyframe',
      'MappingData': '_qt3_d_animation__animation__mapping_data',
      'SkeletonManager': '_qt3_d_animation__animation__skeleton_manager',
      'AbstractEvaluateClipAnimatorJob': '_qt3_d_animation__animation__abstract_evaluate_clip_animator_job',
      'BuildBlendTreesJob': '_qt3_d_animation__animation__build_blend_trees_job',
      'ClipBlendNodeManager': '_qt3_d_animation__animation__clip_blend_node_manager',
      'ClipBlendNodeVisitor': '_qt3_d_animation__animation__clip_blend_node_visitor',
      'FindRunningClipAnimatorsJob': '_qt3_d_animation__animation__find_running_clip_animators_job',
      'Handler': '_qt3_d_animation__animation__handler',
      'LoadAnimationClipJob': '_qt3_d_animation__animation__load_animation_clip_job',
      'EvaluateBlendClipAnimatorJob': '_qt3_d_animation__animation__evaluate_blend_clip_animator_job',
      'EvaluateClipAnimatorJob': '_qt3_d_animation__animation__evaluate_clip_animator_job',
      'ChannelNameAndType': '_qt3_d_animation__animation__channel_name_and_type',
      'Channel': '_qt3_d_animation__animation__channel',
      'ChannelComponent': '_qt3_d_animation__animation__channel_component',
      'FCurve': '_qt3_d_animation__animation__f_curve',
      'BackendNode': '_qt3_d_animation__animation__backend_node',
      'AnimationClip': '_qt3_d_animation__animation__animation_clip',
      'BlendedClipAnimator': '_qt3_d_animation__animation__blended_clip_animator',
      'ChannelMapper': '_qt3_d_animation__animation__channel_mapper',
      'ChannelMapping': '_qt3_d_animation__animation__channel_mapping',
      'ClipAnimator': '_qt3_d_animation__animation__clip_animator',
      'ClipBlendNode': '_qt3_d_animation__animation__clip_blend_node',
      'Clock': '_qt3_d_animation__animation__clock',
      'GLTFImporter': '_qt3_d_animation__animation__g_l_t_f_importer',
      'AdditiveClipBlend': '_qt3_d_animation__animation__additive_clip_blend',
      'ClipBlendValue': '_qt3_d_animation__animation__clip_blend_value',
      'LerpClipBlend': '_qt3_d_animation__animation__lerp_clip_blend',
      'Skeleton': '_qt3_d_animation__animation__skeleton',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('JobTypes',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DAnimation.Animation.AnimationCallbackAndValue'.
    Python calls this for a name the package does not hold yet, and what it
    gives is kept here for the next time.

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
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
