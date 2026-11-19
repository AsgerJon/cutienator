"""
StandardLocation stands for the enum 'QStandardPaths::StandardLocation' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qstandardpaths.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class StandardLocation(CuteNum):
  """
  The enum 'QStandardPaths::StandardLocation' of Qt, with the 23 names Qt
  gives in it.
  """

  DesktopLocation = Kee[int](0)
  DocumentsLocation = Kee[int](1)
  FontsLocation = Kee[int](2)
  ApplicationsLocation = Kee[int](3)
  MusicLocation = Kee[int](4)
  MoviesLocation = Kee[int](5)
  PicturesLocation = Kee[int](6)
  TempLocation = Kee[int](7)
  HomeLocation = Kee[int](8)
  AppLocalDataLocation = Kee[int](9)
  CacheLocation = Kee[int](10)
  GenericDataLocation = Kee[int](11)
  RuntimeLocation = Kee[int](12)
  ConfigLocation = Kee[int](13)
  DownloadLocation = Kee[int](14)
  GenericCacheLocation = Kee[int](15)
  GenericConfigLocation = Kee[int](16)
  AppDataLocation = Kee[int](17)
  AppConfigLocation = Kee[int](18)
  PublicShareLocation = Kee[int](19)
  TemplatesLocation = Kee[int](20)
  StateLocation = Kee[int](21)
  GenericStateLocation = Kee[int](22)
