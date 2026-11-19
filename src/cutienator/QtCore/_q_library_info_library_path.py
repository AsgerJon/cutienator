"""
LibraryPath stands for the enum 'QLibraryInfo::LibraryPath' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlibraryinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class LibraryPath(CuteNum):
  """
  The enum 'QLibraryInfo::LibraryPath' of Qt, with the 15 names Qt gives in
  it.
  """

  PrefixPath = Kee[int](0)
  DocumentationPath = Kee[int](1)
  HeadersPath = Kee[int](2)
  LibrariesPath = Kee[int](3)
  LibraryExecutablesPath = Kee[int](4)
  BinariesPath = Kee[int](5)
  PluginsPath = Kee[int](6)
  QmlImportsPath = Kee[int](7)
  Qml2ImportsPath = Kee[int](7)
  ArchDataPath = Kee[int](8)
  DataPath = Kee[int](9)
  TranslationsPath = Kee[int](10)
  ExamplesPath = Kee[int](11)
  TestsPath = Kee[int](12)
  SettingsPath = Kee[int](100)
