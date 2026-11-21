"""
SubmitPolicy stands for the enum 'QDataWidgetMapper::SubmitPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qdatawidgetmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SubmitPolicy(CuteNum):
  """
  The enum 'QDataWidgetMapper::SubmitPolicy' of Qt, with the 2 names Qt gives
  in it.
  """

  AutoSubmit = Kee[int](0)
  ManualSubmit = Kee[int](1)
