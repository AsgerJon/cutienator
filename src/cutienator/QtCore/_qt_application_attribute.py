"""
ApplicationAttribute stands for the enum 'Qt::ApplicationAttribute' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ApplicationAttribute(CuteNum):
  """
  The enum 'Qt::ApplicationAttribute' of Qt, with the 31 names Qt gives in
  it.
  """

  AA_QtQuickUseDefaultSizePolicy = Kee[int](1)
  AA_DontShowIconsInMenus = Kee[int](2)
  AA_NativeWindows = Kee[int](3)
  AA_DontCreateNativeWidgetSiblings = Kee[int](4)
  AA_PluginApplication = Kee[int](5)
  AA_DontUseNativeMenuBar = Kee[int](6)
  AA_MacDontSwapCtrlAndMeta = Kee[int](7)
  AA_Use96Dpi = Kee[int](8)
  AA_DisableNativeVirtualKeyboard = Kee[int](9)
  AA_DontUseNativeMenuWindows = Kee[int](10)
  AA_SynthesizeTouchForUnhandledMouseEvents = Kee[int](11)
  AA_SynthesizeMouseForUnhandledTouchEvents = Kee[int](12)
  AA_UseHighDpiPixmaps = Kee[int](13)
  AA_ForceRasterWidgets = Kee[int](14)
  AA_UseDesktopOpenGL = Kee[int](15)
  AA_UseOpenGLES = Kee[int](16)
  AA_UseSoftwareOpenGL = Kee[int](17)
  AA_ShareOpenGLContexts = Kee[int](18)
  AA_SetPalette = Kee[int](19)
  AA_EnableHighDpiScaling = Kee[int](20)
  AA_DisableHighDpiScaling = Kee[int](21)
  AA_UseStyleSheetPropagationInWidgetStyles = Kee[int](22)
  AA_DontUseNativeDialogs = Kee[int](23)
  AA_SynthesizeMouseForUnhandledTabletEvents = Kee[int](24)
  AA_CompressHighFrequencyEvents = Kee[int](25)
  AA_DontCheckOpenGLContextThreadAffinity = Kee[int](26)
  AA_DisableShaderDiskCache = Kee[int](27)
  AA_DontShowShortcutsInContextMenus = Kee[int](28)
  AA_CompressTabletEvents = Kee[int](29)
  AA_DisableSessionManager = Kee[int](31)
  AA_AttributeCount = Kee[int](32)
