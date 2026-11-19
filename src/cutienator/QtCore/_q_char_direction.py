"""
Direction stands for the enum 'QChar::Direction' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Direction(CuteNum):
  """
  The enum 'QChar::Direction' of Qt, with the 23 names Qt gives in it.
  """

  DirL = Kee[int](0)
  DirR = Kee[int](1)
  DirEN = Kee[int](2)
  DirES = Kee[int](3)
  DirET = Kee[int](4)
  DirAN = Kee[int](5)
  DirCS = Kee[int](6)
  DirB = Kee[int](7)
  DirS = Kee[int](8)
  DirWS = Kee[int](9)
  DirON = Kee[int](10)
  DirLRE = Kee[int](11)
  DirLRO = Kee[int](12)
  DirAL = Kee[int](13)
  DirRLE = Kee[int](14)
  DirRLO = Kee[int](15)
  DirPDF = Kee[int](16)
  DirNSM = Kee[int](17)
  DirBN = Kee[int](18)
  DirLRI = Kee[int](19)
  DirRLI = Kee[int](20)
  DirFSI = Kee[int](21)
  DirPDI = Kee[int](22)
