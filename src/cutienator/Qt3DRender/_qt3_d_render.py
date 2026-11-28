"""
Qt3DRender stands for the namespace 'Qt3DRender' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Qt3DRender:
  """
  The namespace 'Qt3DRender' of Qt, which holds no objects. It holds the 1
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class API(CuteNum, scoped=True):
    """
    The enum 'Qt3DRender::API' of Qt, with the 6 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    OpenGL = Kee[int](0)
    Vulkan = Kee[int](1)
    DirectX = Kee[int](2)
    Metal = Kee[int](3)
    RHI = Kee[int](4)
    Null = Kee[int](5)
