"""
Option stands for the flags enum 'QAbstractFileIconProvider::Option' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qabstractfileiconprovider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Option(CuteFlags):
  """
  The flags enum 'QAbstractFileIconProvider::Option' of Qt, with the 1 names
  Qt gives in it. Qt names the type of its combinations
  'QAbstractFileIconProvider::Options'.
  """

  DontUseCustomDirectoryIcons = 0x1
