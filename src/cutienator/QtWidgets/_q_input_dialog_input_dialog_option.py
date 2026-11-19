"""
InputDialogOption stands for the flags enum 'QInputDialog::InputDialogOption'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qinputdialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class InputDialogOption(CuteFlags):
  """
  The flags enum 'QInputDialog::InputDialogOption' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QInputDialog::InputDialogOptions'.
  """

  NoButtons = 0x1
  UseListViewForComboBoxItems = 0x2
  UsePlainTextEditForTextInput = 0x4
