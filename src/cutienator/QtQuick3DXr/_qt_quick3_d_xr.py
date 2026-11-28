"""
QtQuick3DXr stands for the namespace 'QtQuick3DXr' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QtQuick3DXr:
  """
  The namespace 'QtQuick3DXr' of Qt, which holds no objects. It holds the 6
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class Controller(CuteNum, scoped=True):
    """
    The enum 'QtQuick3DXr::Controller' of Qt, with the 5 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    LeftController = Kee[int](0)
    RightController = Kee[int](1)
    UnknownController = Kee[int](2)
    LeftHand = Kee[int](0)
    RightHand = Kee[int](1)

  class FoveationLevel(CuteNum):
    """
    The enum 'QtQuick3DXr::FoveationLevel' of Qt, with the 4 names Qt gives
    in it.
    """

    NoFoveation = Kee[int](0)
    LowFoveation = Kee[int](1)
    MediumFoveation = Kee[int](2)
    HighFoveation = Kee[int](3)

  class HandPoseSpace(CuteNum, scoped=True):
    """
    The enum 'QtQuick3DXr::HandPoseSpace' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    GripPose = Kee[int](0)
    AimPose = Kee[int](1)
    PinchPose = Kee[int](2)
    PokePose = Kee[int](3)

  class Handedness(CuteNum, scoped=True):
    """
    The enum 'QtQuick3DXr::Handedness' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Left = Kee[int](0)
    Right = Kee[int](1)
    Unknown = Kee[int](2)

  class ReferenceSpace(CuteNum, scoped=True):
    """
    The enum 'QtQuick3DXr::ReferenceSpace' of Qt, with the 4 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    ReferenceSpaceUnknown = Kee[int](0)
    ReferenceSpaceLocal = Kee[int](1)
    ReferenceSpaceStage = Kee[int](2)
    ReferenceSpaceLocalFloor = Kee[int](3)

  class XrSpaceId(CuteNum, scoped=True):
    """
    The enum 'QtQuick3DXr::XrSpaceId' of Qt, with the 1 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Invalid = Kee[int](0)
