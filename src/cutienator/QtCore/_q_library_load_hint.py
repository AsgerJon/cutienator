"""
LoadHint stands for the flags enum 'QLibrary::LoadHint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlibrary.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class LoadHint(CuteFlags):
  """
  The flags enum 'QLibrary::LoadHint' of Qt, with the 5 names Qt gives in it.
  Qt names the type of its combinations 'QLibrary::LoadHints'.
  """

  ResolveAllSymbolsHint = 0x1
  ExportExternalSymbolsHint = 0x2
  LoadArchiveMemberHint = 0x4
  PreventUnloadHint = 0x8
  DeepBindHint = 0x10
