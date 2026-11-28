"""
JobTypes stands for the namespace 'Qt3DAnimation::Animation::JobTypes' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class JobTypes:
  """
  The namespace 'Qt3DAnimation::Animation::JobTypes' of Qt, which holds no
  objects. It holds the 1 enums Qt writes in it, each under its name, and the
  0 names Qt has for the combinations of a flags enum, each holding the class
  of that enum. It is never made into an object.
  """

  class JobType(CuteNum):
    """
    The enum 'Qt3DAnimation::Animation::JobTypes::JobType' of Qt, with the 5
    names Qt gives in it.
    """

    BuildBlendTree = Kee[int](8192)
    EvaluateBlendClipAnimator = Kee[int](8193)
    EvaluateClipAnimator = Kee[int](8194)
    LoadAnimationClip = Kee[int](8195)
    FindRunningClipAnimator = Kee[int](8196)
