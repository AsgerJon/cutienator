"""
WizardButton stands for the enum 'QWizard::WizardButton' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class WizardButton(CuteNum):
  """
  The enum 'QWizard::WizardButton' of Qt, with the 13 names Qt gives in it.
  """

  BackButton = Kee[int](0)
  NextButton = Kee[int](1)
  CommitButton = Kee[int](2)
  FinishButton = Kee[int](3)
  CancelButton = Kee[int](4)
  HelpButton = Kee[int](5)
  CustomButton1 = Kee[int](6)
  CustomButton2 = Kee[int](7)
  CustomButton3 = Kee[int](8)
  Stretch = Kee[int](9)
  NoButton = Kee[int](-1)
  NStandardButtons = Kee[int](6)
  NButtons = Kee[int](9)
