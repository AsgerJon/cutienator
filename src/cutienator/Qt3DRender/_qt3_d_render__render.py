"""
Render stands for the namespace 'Qt3DRender::Render' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class Render:
  """
  The namespace 'Qt3DRender::Render' of Qt, which holds no objects. It holds
  the 3 enums Qt writes in it, each under its name, and the 1 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class RebuildFlag(CuteFlags):
    """
    The flags enum 'Qt3DRender::Render::RebuildFlag' of Qt, with the 4 names
    Qt gives in it. Qt names the type of its combinations
    'Qt3DRender::Render::RebuildFlagSet'.
    """

    FullCommandRebuild = 0x1
    LayerCacheRebuild = 0x2
    MaterialCacheRebuild = 0x4
    LightCacheRebuild = 0x8

  RebuildFlagSet = RebuildFlag

  class StateMask(CuteNum):
    """
    The enum 'Qt3DRender::Render::StateMask' of Qt, with the 22 names Qt
    gives in it.
    """

    BlendStateMask = Kee[int](1)
    StencilWriteStateMask = Kee[int](2)
    StencilTestStateMask = Kee[int](4)
    ScissorStateMask = Kee[int](8)
    DepthTestStateMask = Kee[int](16)
    DepthWriteStateMask = Kee[int](32)
    CullFaceStateMask = Kee[int](64)
    AlphaTestMask = Kee[int](128)
    FrontFaceStateMask = Kee[int](256)
    DitheringStateMask = Kee[int](512)
    AlphaCoverageStateMask = Kee[int](1024)
    PolygonOffsetStateMask = Kee[int](2048)
    ColorStateMask = Kee[int](4096)
    ClipPlaneMask = Kee[int](8192)
    StencilOpMask = Kee[int](16384)
    PointSizeMask = Kee[int](32768)
    SeamlessCubemapMask = Kee[int](65536)
    MSAAEnabledStateMask = Kee[int](131072)
    BlendEquationArgumentsMask = Kee[int](262144)
    LineWidthMask = Kee[int](524288)
    DepthRangeMask = Kee[int](1048576)
    RasterModeMask = Kee[int](2097152)

  class UniformType(CuteNum):
    """
    The enum 'Qt3DRender::Render::UniformType' of Qt, with the 32 names Qt
    gives in it.
    """

    Float = Kee[int](0)
    Vec2 = Kee[int](1)
    Vec3 = Kee[int](2)
    Vec4 = Kee[int](3)
    Double = Kee[int](4)
    DVec2 = Kee[int](5)
    DVec3 = Kee[int](6)
    DVec4 = Kee[int](7)
    Int = Kee[int](8)
    IVec2 = Kee[int](9)
    IVec3 = Kee[int](10)
    IVec4 = Kee[int](11)
    UInt = Kee[int](12)
    UIVec2 = Kee[int](13)
    UIVec3 = Kee[int](14)
    UIVec4 = Kee[int](15)
    Bool = Kee[int](16)
    BVec2 = Kee[int](17)
    BVec3 = Kee[int](18)
    BVec4 = Kee[int](19)
    Mat2 = Kee[int](20)
    Mat3 = Kee[int](21)
    Mat4 = Kee[int](22)
    Mat2x3 = Kee[int](23)
    Mat3x2 = Kee[int](24)
    Mat2x4 = Kee[int](25)
    Mat4x2 = Kee[int](26)
    Mat3x4 = Kee[int](27)
    Mat4x3 = Kee[int](28)
    Sampler = Kee[int](29)
    Image = Kee[int](30)
    Unknown = Kee[int](31)
