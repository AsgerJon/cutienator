"""
RequestSoftwareInputPanel stands for the enum
'QStyle::RequestSoftwareInputPanel' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class RequestSoftwareInputPanel(CuteNum):
  """
  The enum 'QStyle::RequestSoftwareInputPanel' of Qt, with the 2 names Qt
  gives in it.
  """

  RSIP_OnMouseClickAndAlreadyFocused = Kee[int](0)
  RSIP_OnMouseClick = Kee[int](1)
