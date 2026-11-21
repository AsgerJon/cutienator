"""
FrameFeature stands for the flags enum 'QStyleOptionFrame::FrameFeature' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class FrameFeature(CuteFlags):
  """
  The flags enum 'QStyleOptionFrame::FrameFeature' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QStyleOptionFrame::FrameFeatures'.
  """

  NULL = 0x0
  Flat = 0x1
  Rounded = 0x2
