"""
WizardOption stands for the flags enum 'QWizard::WizardOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class WizardOption(CuteFlags):
  """
  The flags enum 'QWizard::WizardOption' of Qt, with the 18 names Qt gives in
  it. Qt names the type of its combinations 'QWizard::WizardOptions'.
  """

  IndependentPages = 0x1
  IgnoreSubTitles = 0x2
  ExtendedWatermarkPixmap = 0x4
  NoDefaultButton = 0x8
  NoBackButtonOnStartPage = 0x10
  NoBackButtonOnLastPage = 0x20
  DisabledBackButtonOnLastPage = 0x40
  HaveNextButtonOnLastPage = 0x80
  HaveFinishButtonOnEarlyPages = 0x100
  NoCancelButton = 0x200
  CancelButtonOnLeft = 0x400
  HaveHelpButton = 0x800
  HelpButtonOnRight = 0x1000
  HaveCustomButton1 = 0x2000
  HaveCustomButton2 = 0x4000
  HaveCustomButton3 = 0x8000
  NoCancelButtonOnLastPage = 0x10000
  StretchBanner = 0x20000
