"""
Roles stands for the enum 'QFileSystemModel::Roles' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qfilesystemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Roles(CuteNum):
  """
  The enum 'QFileSystemModel::Roles' of Qt, with the 5 names Qt gives in it.
  """

  FileIconRole = Kee[int](1)
  FileInfoRole = Kee[int](252)
  FilePathRole = Kee[int](257)
  FileNameRole = Kee[int](258)
  FilePermissions = Kee[int](259)
