"""
StandardButton stands for the flags enum 'QDialogButtonBox::StandardButton'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qdialogbuttonbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class StandardButton(CuteFlags):
  """
  The flags enum 'QDialogButtonBox::StandardButton' of Qt, with the 21 names
  Qt gives in it. Qt names the type of its combinations
  'QDialogButtonBox::StandardButtons'.
  """

  NoButton = 0x0
  Ok = 0x400
  Save = 0x800
  SaveAll = 0x1000
  Open = 0x2000
  Yes = 0x4000
  YesToAll = 0x8000
  No = 0x10000
  NoToAll = 0x20000
  Abort = 0x40000
  Retry = 0x80000
  Ignore = 0x100000
  Close = 0x200000
  Cancel = 0x400000
  Discard = 0x800000
  Help = 0x1000000
  Apply = 0x2000000
  Reset = 0x4000000
  RestoreDefaults = 0x8000000
  FirstButton = 0x400
  LastButton = 0x8000000
