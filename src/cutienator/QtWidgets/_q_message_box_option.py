"""
Option stands for the flags enum 'QMessageBox::Option' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qmessagebox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Option(CuteFlags, scoped=True):
  """
  The flags enum 'QMessageBox::Option' of Qt, with the 1 names Qt gives in
  it. Qt names the type of its combinations 'QMessageBox::Options'. C++ keeps
  these names inside the enum, so the class that holds the enum does not have
  them.
  """

  DontUseNativeDialog = 0x1
