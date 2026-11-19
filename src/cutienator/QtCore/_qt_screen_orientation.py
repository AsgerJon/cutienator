"""
ScreenOrientation stands for the flags enum 'Qt::ScreenOrientation' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ScreenOrientation(CuteFlags):
  """
  The flags enum 'Qt::ScreenOrientation' of Qt, with the 5 names Qt gives in
  it. Qt names the type of its combinations 'Qt::ScreenOrientations'.
  """

  PrimaryOrientation = 0x0
  PortraitOrientation = 0x1
  LandscapeOrientation = 0x2
  InvertedPortraitOrientation = 0x4
  InvertedLandscapeOrientation = 0x8
