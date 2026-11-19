"""
WritingSystem stands for the enum 'QFontDatabase::WritingSystem' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qfontdatabase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class WritingSystem(CuteNum):
  """
  The enum 'QFontDatabase::WritingSystem' of Qt, with the 36 names Qt gives
  in it.
  """

  Any = Kee[int](0)
  Latin = Kee[int](1)
  Greek = Kee[int](2)
  Cyrillic = Kee[int](3)
  Armenian = Kee[int](4)
  Hebrew = Kee[int](5)
  Arabic = Kee[int](6)
  Syriac = Kee[int](7)
  Thaana = Kee[int](8)
  Devanagari = Kee[int](9)
  Bengali = Kee[int](10)
  Gurmukhi = Kee[int](11)
  Gujarati = Kee[int](12)
  Oriya = Kee[int](13)
  Tamil = Kee[int](14)
  Telugu = Kee[int](15)
  Kannada = Kee[int](16)
  Malayalam = Kee[int](17)
  Sinhala = Kee[int](18)
  Thai = Kee[int](19)
  Lao = Kee[int](20)
  Tibetan = Kee[int](21)
  Myanmar = Kee[int](22)
  Georgian = Kee[int](23)
  Khmer = Kee[int](24)
  SimplifiedChinese = Kee[int](25)
  TraditionalChinese = Kee[int](26)
  Japanese = Kee[int](27)
  Korean = Kee[int](28)
  Vietnamese = Kee[int](29)
  Symbol = Kee[int](30)
  Other = Kee[int](30)
  Ogham = Kee[int](31)
  Runic = Kee[int](32)
  Nko = Kee[int](33)
  WritingSystemsCount = Kee[int](34)
