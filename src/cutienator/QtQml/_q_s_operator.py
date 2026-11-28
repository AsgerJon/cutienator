"""
QSOperator stands for the namespace 'QSOperator' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QSOperator:
  """
  The namespace 'QSOperator' of Qt, which holds no objects. It holds the 1
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class Op(CuteNum):
    """The enum 'QSOperator::Op' of Qt, with the 40 names Qt gives in it."""

    Add = Kee[int](0)
    And = Kee[int](1)
    InplaceAnd = Kee[int](2)
    Assign = Kee[int](3)
    BitAnd = Kee[int](4)
    BitOr = Kee[int](5)
    BitXor = Kee[int](6)
    InplaceSub = Kee[int](7)
    Div = Kee[int](8)
    InplaceDiv = Kee[int](9)
    Equal = Kee[int](10)
    Exp = Kee[int](11)
    InplaceExp = Kee[int](12)
    Ge = Kee[int](13)
    Gt = Kee[int](14)
    In = Kee[int](15)
    InplaceAdd = Kee[int](16)
    InstanceOf = Kee[int](17)
    Le = Kee[int](18)
    LShift = Kee[int](19)
    InplaceLeftShift = Kee[int](20)
    Lt = Kee[int](21)
    Mod = Kee[int](22)
    InplaceMod = Kee[int](23)
    Mul = Kee[int](24)
    InplaceMul = Kee[int](25)
    NotEqual = Kee[int](26)
    Or = Kee[int](27)
    InplaceOr = Kee[int](28)
    RShift = Kee[int](29)
    InplaceRightShift = Kee[int](30)
    StrictEqual = Kee[int](31)
    StrictNotEqual = Kee[int](32)
    Sub = Kee[int](33)
    URShift = Kee[int](34)
    InplaceURightShift = Kee[int](35)
    InplaceXor = Kee[int](36)
    As = Kee[int](37)
    Coalesce = Kee[int](38)
    Invalid = Kee[int](39)
