"""
UnixProcessFlag stands for the flags enum 'QProcess::UnixProcessFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class UnixProcessFlag(CuteFlags, number='unsigned int', scoped=True):
  """
  The flags enum 'QProcess::UnixProcessFlag' of Qt, with the 8 names Qt gives
  in it. Qt names the type of its combinations 'QProcess::UnixProcessFlags'.
  C++ keeps these names inside the enum, so the class that holds the enum
  does not have them.
  """

  ResetSignalHandlers = 0x1
  IgnoreSigPipe = 0x2
  CloseFileDescriptors = 0x10
  UseVFork = 0x20
  CreateNewSession = 0x40
  DisconnectControllingTerminal = 0x80
  ResetIds = 0x100
  DisableCoreDumps = 0x200
