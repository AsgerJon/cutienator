"""
Type stands for the enum 'QEasingCurve::Type' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qeasingcurve.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Type(CuteNum):
  """
  The enum 'QEasingCurve::Type' of Qt, with the 49 names Qt gives in it.
  """

  Linear = Kee[int](0)
  InQuad = Kee[int](1)
  OutQuad = Kee[int](2)
  InOutQuad = Kee[int](3)
  OutInQuad = Kee[int](4)
  InCubic = Kee[int](5)
  OutCubic = Kee[int](6)
  InOutCubic = Kee[int](7)
  OutInCubic = Kee[int](8)
  InQuart = Kee[int](9)
  OutQuart = Kee[int](10)
  InOutQuart = Kee[int](11)
  OutInQuart = Kee[int](12)
  InQuint = Kee[int](13)
  OutQuint = Kee[int](14)
  InOutQuint = Kee[int](15)
  OutInQuint = Kee[int](16)
  InSine = Kee[int](17)
  OutSine = Kee[int](18)
  InOutSine = Kee[int](19)
  OutInSine = Kee[int](20)
  InExpo = Kee[int](21)
  OutExpo = Kee[int](22)
  InOutExpo = Kee[int](23)
  OutInExpo = Kee[int](24)
  InCirc = Kee[int](25)
  OutCirc = Kee[int](26)
  InOutCirc = Kee[int](27)
  OutInCirc = Kee[int](28)
  InElastic = Kee[int](29)
  OutElastic = Kee[int](30)
  InOutElastic = Kee[int](31)
  OutInElastic = Kee[int](32)
  InBack = Kee[int](33)
  OutBack = Kee[int](34)
  InOutBack = Kee[int](35)
  OutInBack = Kee[int](36)
  InBounce = Kee[int](37)
  OutBounce = Kee[int](38)
  InOutBounce = Kee[int](39)
  OutInBounce = Kee[int](40)
  InCurve = Kee[int](41)
  OutCurve = Kee[int](42)
  SineCurve = Kee[int](43)
  CosineCurve = Kee[int](44)
  BezierSpline = Kee[int](45)
  TCBSpline = Kee[int](46)
  Custom = Kee[int](47)
  NCurveTypes = Kee[int](48)
