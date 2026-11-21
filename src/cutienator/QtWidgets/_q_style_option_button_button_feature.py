"""
ButtonFeature stands for the flags enum 'QStyleOptionButton::ButtonFeature'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ButtonFeature(CuteFlags):
  """
  The flags enum 'QStyleOptionButton::ButtonFeature' of Qt, with the 6 names
  Qt gives in it. Qt names the type of its combinations
  'QStyleOptionButton::ButtonFeatures'.
  """

  NULL = 0x0
  Flat = 0x1
  HasMenu = 0x2
  DefaultButton = 0x4
  AutoDefaultButton = 0x8
  CommandLinkButton = 0x10
