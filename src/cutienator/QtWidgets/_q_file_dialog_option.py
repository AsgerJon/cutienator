"""
Option stands for the flags enum 'QFileDialog::Option' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qfiledialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Option(CuteFlags):
  """
  The flags enum 'QFileDialog::Option' of Qt, with the 7 names Qt gives in
  it. Qt names the type of its combinations 'QFileDialog::Options'.
  """

  ShowDirsOnly = 0x1
  DontResolveSymlinks = 0x2
  DontConfirmOverwrite = 0x4
  DontUseNativeDialog = 0x8
  ReadOnly = 0x10
  HideNameFilterDetails = 0x20
  DontUseCustomDirectoryIcons = 0x40
