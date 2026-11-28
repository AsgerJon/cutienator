"""
QtGraphs3D stands for the namespace 'QtGraphs3D' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QtGraphs3D:
  """
  The namespace 'QtGraphs3D' of Qt, which holds no objects. It holds the 10
  enums Qt writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class CameraPreset(CuteNum, scoped=True):
    """
    The enum 'QtGraphs3D::CameraPreset' of Qt, with the 25 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoPreset = Kee[int](0)
    FrontLow = Kee[int](1)
    Front = Kee[int](2)
    FrontHigh = Kee[int](3)
    LeftLow = Kee[int](4)
    Left = Kee[int](5)
    LeftHigh = Kee[int](6)
    RightLow = Kee[int](7)
    Right = Kee[int](8)
    RightHigh = Kee[int](9)
    BehindLow = Kee[int](10)
    Behind = Kee[int](11)
    BehindHigh = Kee[int](12)
    IsometricLeft = Kee[int](13)
    IsometricLeftHigh = Kee[int](14)
    IsometricRight = Kee[int](15)
    IsometricRightHigh = Kee[int](16)
    DirectlyAbove = Kee[int](17)
    DirectlyAboveCW45 = Kee[int](18)
    DirectlyAboveCCW45 = Kee[int](19)
    FrontBelow = Kee[int](20)
    LeftBelow = Kee[int](21)
    RightBelow = Kee[int](22)
    BehindBelow = Kee[int](23)
    DirectlyBelow = Kee[int](24)

  class DragMode(CuteNum, scoped=True):
    """
    The enum 'QtGraphs3D::DragMode' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Rotate = Kee[int](0)
    Pan = Kee[int](1)

  class ElementType(CuteNum, scoped=True):
    """
    The enum 'QtGraphs3D::ElementType' of Qt, with the 6 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    Series = Kee[int](1)
    AxisXLabel = Kee[int](2)
    AxisYLabel = Kee[int](3)
    AxisZLabel = Kee[int](4)
    CustomItem = Kee[int](5)

  class GridLineType(CuteNum, scoped=True):
    """
    The enum 'QtGraphs3D::GridLineType' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Shader = Kee[int](0)
    Geometry = Kee[int](1)

  class OptimizationHint(CuteNum, scoped=True):
    """
    The enum 'QtGraphs3D::OptimizationHint' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Default = Kee[int](0)
    Legacy = Kee[int](1)

  class RenderingMode(CuteNum, scoped=True):
    """
    The enum 'QtGraphs3D::RenderingMode' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    DirectToBackground = Kee[int](0)
    Indirect = Kee[int](1)

  class SelectionFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QtGraphs3D::SelectionFlag' of Qt, with the 10 names Qt
    gives in it. Qt names the type of its combinations
    'QtGraphs3D::SelectionFlags'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    NULL = 0x0
    Item = 0x1
    Row = 0x2
    ItemAndRow = 0x3
    Column = 0x4
    ItemAndColumn = 0x5
    RowAndColumn = 0x6
    ItemRowAndColumn = 0x7
    Slice = 0x8
    MultiSeries = 0x10

  SelectionFlags = SelectionFlag

  class ShadowQuality(CuteNum, scoped=True):
    """
    The enum 'QtGraphs3D::ShadowQuality' of Qt, with the 7 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    Low = Kee[int](1)
    Medium = Kee[int](2)
    High = Kee[int](3)
    SoftLow = Kee[int](4)
    SoftMedium = Kee[int](5)
    SoftHigh = Kee[int](6)

  class SliceCaptureType(CuteNum, scoped=True):
    """
    The enum 'QtGraphs3D::SliceCaptureType' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoImage = Kee[int](0)
    RowImage = Kee[int](1)
    ColumnImage = Kee[int](2)

  class TransparencyTechnique(CuteNum, scoped=True):
    """
    The enum 'QtGraphs3D::TransparencyTechnique' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Default = Kee[int](0)
    Approximate = Kee[int](1)
    Accurate = Kee[int](2)
