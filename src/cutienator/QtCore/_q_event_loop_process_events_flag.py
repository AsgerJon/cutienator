"""
ProcessEventsFlag stands for the flags enum 'QEventLoop::ProcessEventsFlag'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qeventloop.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ProcessEventsFlag(CuteFlags):
  """
  The flags enum 'QEventLoop::ProcessEventsFlag' of Qt, with the 8 names Qt
  gives in it. Qt names the type of its combinations
  'QEventLoop::ProcessEventsFlags'.
  """

  AllEvents = 0x0
  ExcludeUserInputEvents = 0x1
  ExcludeSocketNotifiers = 0x2
  WaitForMoreEvents = 0x4
  X11ExcludeTimers = 0x8
  EventLoopExec = 0x20
  DialogExec = 0x40
  ApplicationExec = 0x80
