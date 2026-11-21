"""
WizardStyle stands for the enum 'QWizard::WizardStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class WizardStyle(CuteNum):
  """
  The enum 'QWizard::WizardStyle' of Qt, with the 5 names Qt gives in it.
  """

  ClassicStyle = Kee[int](0)
  ModernStyle = Kee[int](1)
  MacStyle = Kee[int](2)
  AeroStyle = Kee[int](3)
  NStyles = Kee[int](4)
