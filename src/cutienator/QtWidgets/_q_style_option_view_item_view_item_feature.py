"""
ViewItemFeature stands for the flags enum
'QStyleOptionViewItem::ViewItemFeature' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ViewItemFeature(CuteFlags):
  """
  The flags enum 'QStyleOptionViewItem::ViewItemFeature' of Qt, with the 8
  names Qt gives in it. Qt names the type of its combinations
  'QStyleOptionViewItem::ViewItemFeatures'.
  """

  NULL = 0x0
  WrapText = 0x1
  Alternate = 0x2
  HasCheckIndicator = 0x4
  HasDisplay = 0x8
  HasDecoration = 0x10
  IsDecoratedRootColumn = 0x20
  IsDecorationForRootColumn = 0x40
