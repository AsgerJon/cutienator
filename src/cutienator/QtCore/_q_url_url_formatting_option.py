"""
UrlFormattingOption stands for the enum 'QUrl::UrlFormattingOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qurl.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class UrlFormattingOption(CuteNum):
  """
  The enum 'QUrl::UrlFormattingOption' of Qt, with the 13 names Qt gives in
  it.
  """

  NULL = Kee[int](0)
  RemoveScheme = Kee[int](1)
  RemovePassword = Kee[int](2)
  RemoveUserInfo = Kee[int](6)
  RemovePort = Kee[int](8)
  RemoveAuthority = Kee[int](30)
  RemovePath = Kee[int](32)
  RemoveQuery = Kee[int](64)
  RemoveFragment = Kee[int](128)
  PreferLocalFile = Kee[int](512)
  StripTrailingSlash = Kee[int](1024)
  RemoveFilename = Kee[int](2048)
  NormalizePathSegments = Kee[int](4096)
