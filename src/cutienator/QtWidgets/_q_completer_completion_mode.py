"""
CompletionMode stands for the enum 'QCompleter::CompletionMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qcompleter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class CompletionMode(CuteNum):
  """
  The enum 'QCompleter::CompletionMode' of Qt, with the 3 names Qt gives in
  it.
  """

  PopupCompletion = Kee[int](0)
  UnfilteredPopupCompletion = Kee[int](1)
  InlineCompletion = Kee[int](2)
