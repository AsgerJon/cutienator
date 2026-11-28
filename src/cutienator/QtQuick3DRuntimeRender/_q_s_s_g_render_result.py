"""
QSSGRenderResult stands for the namespace 'QSSGRenderResult' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QSSGRenderResult:
  """
  The namespace 'QSSGRenderResult' of Qt, which holds no objects. It holds
  the 1 enums Qt writes in it, each under its name, and the 0 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class Key(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderResult::Key' of Qt, with the 13 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    AoTexture = Kee[int](0)
    DepthTexture = Kee[int](1)
    ScreenTexture = Kee[int](2)
    NormalTexture = Kee[int](3)
    MotionVectorTexture = Kee[int](4)
    AccumTexture = Kee[int](5)
    RevealageTexture = Kee[int](6)
    ABufferImage = Kee[int](5)
    AuxiliaryImage = Kee[int](6)
    DepthTextureMS = Kee[int](7)
    CounterImage = Kee[int](8)
    SkyMaterialBackgroundTexture = Kee[int](9)
    RenderResultCount = Kee[int](10)
