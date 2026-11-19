"""
ResolveProperties stands for the enum 'QFont::ResolveProperties' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ResolveProperties(CuteNum):
  """
  The enum 'QFont::ResolveProperties' of Qt, with the 22 names Qt gives in
  it.
  """

  NoPropertiesResolved = Kee[int](0)
  FamilyResolved = Kee[int](1)
  SizeResolved = Kee[int](2)
  StyleHintResolved = Kee[int](4)
  StyleStrategyResolved = Kee[int](8)
  WeightResolved = Kee[int](16)
  StyleResolved = Kee[int](32)
  UnderlineResolved = Kee[int](64)
  OverlineResolved = Kee[int](128)
  StrikeOutResolved = Kee[int](256)
  FixedPitchResolved = Kee[int](512)
  StretchResolved = Kee[int](1024)
  KerningResolved = Kee[int](2048)
  CapitalizationResolved = Kee[int](4096)
  LetterSpacingResolved = Kee[int](8192)
  WordSpacingResolved = Kee[int](16384)
  HintingPreferenceResolved = Kee[int](32768)
  StyleNameResolved = Kee[int](65536)
  FamiliesResolved = Kee[int](131072)
  FeaturesResolved = Kee[int](262144)
  VariableAxesResolved = Kee[int](524288)
  AllPropertiesResolved = Kee[int](1048575)
