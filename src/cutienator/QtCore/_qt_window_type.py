"""
WindowType stands for the flags enum 'Qt::WindowType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class WindowType(CuteFlags, number='unsigned int'):
  """
  The flags enum 'Qt::WindowType' of Qt, with the 40 names Qt gives in it. Qt
  names the type of its combinations 'Qt::WindowFlags'.
  """

  Widget = 0x0
  Window = 0x1
  Dialog = 0x3
  Sheet = 0x5
  Drawer = 0x7
  Popup = 0x9
  Tool = 0xb
  ToolTip = 0xd
  SplashScreen = 0xf
  Desktop = 0x11
  SubWindow = 0x12
  ForeignWindow = 0x21
  CoverWindow = 0x41
  WindowType_Mask = 0xff
  MSWindowsFixedSizeDialogHint = 0x100
  MSWindowsOwnDC = 0x200
  BypassWindowManagerHint = 0x400
  X11BypassWindowManagerHint = 0x400
  FramelessWindowHint = 0x800
  WindowTitleHint = 0x1000
  WindowSystemMenuHint = 0x2000
  WindowMinimizeButtonHint = 0x4000
  WindowMaximizeButtonHint = 0x8000
  WindowMinMaxButtonsHint = 0xc000
  WindowContextHelpButtonHint = 0x10000
  WindowShadeButtonHint = 0x20000
  WindowStaysOnTopHint = 0x40000
  WindowTransparentForInput = 0x80000
  WindowOverridesSystemGestures = 0x100000
  WindowDoesNotAcceptFocus = 0x200000
  MaximizeUsingFullscreenGeometryHint = 0x400000
  ExpandedClientAreaHint = 0x400000
  NoTitleBarBackgroundHint = 0x800000
  CustomizeWindowHint = 0x2000000
  WindowStaysOnBottomHint = 0x4000000
  WindowCloseButtonHint = 0x8000000
  MacWindowToolBarButtonHint = 0x10000000
  BypassGraphicsProxyWidget = 0x20000000
  NoDropShadowWindowHint = 0x40000000
  WindowFullscreenButtonHint = 0x80000000
