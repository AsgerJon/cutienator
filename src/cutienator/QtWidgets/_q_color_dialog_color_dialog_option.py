"""
ColorDialogOption stands for the flags enum 'QColorDialog::ColorDialogOption'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qcolordialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ColorDialogOption(CuteFlags):
  """
  The flags enum 'QColorDialog::ColorDialogOption' of Qt, with the 4 names Qt
  gives in it. Qt names the type of its combinations
  'QColorDialog::ColorDialogOptions'.
  """

  ShowAlphaChannel = 0x1
  NoButtons = 0x2
  DontUseNativeDialog = 0x4
  NoEyeDropperButton = 0x8
