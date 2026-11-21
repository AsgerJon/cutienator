"""
FontDialogOption stands for the flags enum 'QFontDialog::FontDialogOption' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qfontdialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class FontDialogOption(CuteFlags):
  """
  The flags enum 'QFontDialog::FontDialogOption' of Qt, with the 6 names Qt
  gives in it. Qt names the type of its combinations
  'QFontDialog::FontDialogOptions'.
  """

  NoButtons = 0x1
  DontUseNativeDialog = 0x2
  ScalableFonts = 0x4
  NonScalableFonts = 0x8
  MonospacedFonts = 0x10
  ProportionalFonts = 0x20
