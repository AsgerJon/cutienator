"""
ButtonRole stands for the enum 'QDialogButtonBox::ButtonRole' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qdialogbuttonbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ButtonRole(CuteNum):
  """
  The enum 'QDialogButtonBox::ButtonRole' of Qt, with the 11 names Qt gives
  in it.
  """

  InvalidRole = Kee[int](-1)
  AcceptRole = Kee[int](0)
  RejectRole = Kee[int](1)
  DestructiveRole = Kee[int](2)
  ActionRole = Kee[int](3)
  HelpRole = Kee[int](4)
  YesRole = Kee[int](5)
  NoRole = Kee[int](6)
  ResetRole = Kee[int](7)
  ApplyRole = Kee[int](8)
  NRoles = Kee[int](9)
