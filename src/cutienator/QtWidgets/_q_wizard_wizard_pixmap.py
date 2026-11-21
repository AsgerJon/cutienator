"""
WizardPixmap stands for the enum 'QWizard::WizardPixmap' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class WizardPixmap(CuteNum):
  """
  The enum 'QWizard::WizardPixmap' of Qt, with the 5 names Qt gives in it.
  """

  WatermarkPixmap = Kee[int](0)
  LogoPixmap = Kee[int](1)
  BannerPixmap = Kee[int](2)
  BackgroundPixmap = Kee[int](3)
  NPixmaps = Kee[int](4)
