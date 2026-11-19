"""
UserInputResolutionOption stands for the flags enum
'QUrl::UserInputResolutionOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qurl.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class UserInputResolutionOption(CuteFlags):
  """
  The flags enum 'QUrl::UserInputResolutionOption' of Qt, with the 2 names Qt
  gives in it. Qt names the type of its combinations
  'QUrl::UserInputResolutionOptions'.
  """

  DefaultResolution = 0x0
  AssumeLocalFile = 0x1
