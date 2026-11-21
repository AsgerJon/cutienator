"""
IconEngineHook stands for the enum 'QIconEngine::IconEngineHook' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qiconengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class IconEngineHook(CuteNum):
  """
  The enum 'QIconEngine::IconEngineHook' of Qt, with the 2 names Qt gives in
  it.
  """

  IsNullHook = Kee[int](3)
  ScaledPixmapHook = Kee[int](4)
