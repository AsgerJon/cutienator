"""
ExclusionPolicy stands for the enum 'QActionGroup::ExclusionPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qactiongroup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ExclusionPolicy(CuteNum, scoped=True):
  """
  The enum 'QActionGroup::ExclusionPolicy' of Qt, with the 3 names Qt gives
  in it. C++ keeps these names inside the enum, so the class that holds the
  enum does not have them.
  """

  NULL = Kee[int](0)
  Exclusive = Kee[int](1)
  ExclusiveOptional = Kee[int](2)
