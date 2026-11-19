"""
ApplicationState stands for the flags enum 'Qt::ApplicationState' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ApplicationState(CuteFlags):
  """
  The flags enum 'Qt::ApplicationState' of Qt, with the 4 names Qt gives in
  it. Qt names the type of its combinations 'Qt::ApplicationStates'.
  """

  ApplicationSuspended = 0x0
  ApplicationHidden = 0x1
  ApplicationInactive = 0x2
  ApplicationActive = 0x4
