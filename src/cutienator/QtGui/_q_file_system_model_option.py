"""
Option stands for the flags enum 'QFileSystemModel::Option' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qfilesystemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Option(CuteFlags):
  """
  The flags enum 'QFileSystemModel::Option' of Qt, with the 3 names Qt gives
  in it. Qt names the type of its combinations 'QFileSystemModel::Options'.
  """

  DontWatchForChanges = 0x1
  DontResolveSymlinks = 0x2
  DontUseCustomDirectoryIcons = 0x4
