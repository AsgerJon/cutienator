"""
EchoMode stands for the enum 'QLineEdit::EchoMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qlineedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class EchoMode(CuteNum):
  """
  The enum 'QLineEdit::EchoMode' of Qt, with the 4 names Qt gives in it.
  """

  Normal = Kee[int](0)
  NoEcho = Kee[int](1)
  Password = Kee[int](2)
  PasswordEchoOnEdit = Kee[int](3)
