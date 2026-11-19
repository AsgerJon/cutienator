"""
Filter stands for the flags enum 'QDir::Filter' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qdir.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Filter(CuteFlags):
  """
  The flags enum 'QDir::Filter' of Qt, with the 20 names Qt gives in it. Qt
  names the type of its combinations 'QDir::Filters'.
  """

  Dirs = 0x1
  Files = 0x2
  Drives = 0x4
  NoSymLinks = 0x8
  AllEntries = 0x7
  TypeMask = 0xf
  Readable = 0x10
  Writable = 0x20
  Executable = 0x40
  PermissionMask = 0x70
  Modified = 0x80
  Hidden = 0x100
  System = 0x200
  AccessMask = 0x3f0
  AllDirs = 0x400
  CaseSensitive = 0x800
  NoDot = 0x2000
  NoDotDot = 0x4000
  NoDotAndDotDot = 0x6000
  NoFilter = -1
