"""
Notation stands for the enum 'QDoubleValidator::Notation' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Notation(CuteNum):
  """
  The enum 'QDoubleValidator::Notation' of Qt, with the 2 names Qt gives in
  it.
  """

  StandardNotation = Kee[int](0)
  ScientificNotation = Kee[int](1)
