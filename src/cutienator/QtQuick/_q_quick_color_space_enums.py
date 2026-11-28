"""
QQuickColorSpaceEnums stands for the namespace 'QQuickColorSpaceEnums' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QQuickColorSpaceEnums:
  """
  The namespace 'QQuickColorSpaceEnums' of Qt, which holds no objects. It
  holds the 3 enums Qt writes in it, each under its name, and the 0 names Qt
  has for the combinations of a flags enum, each holding the class of that
  enum. It is never made into an object.
  """

  class NamedColorSpace(CuteNum):
    """
    The enum 'QQuickColorSpaceEnums::NamedColorSpace' of Qt, with the 6 names
    Qt gives in it.
    """

    Unknown = Kee[int](0)
    SRgb = Kee[int](1)
    SRgbLinear = Kee[int](2)
    AdobeRgb = Kee[int](3)
    DisplayP3 = Kee[int](4)
    ProPhotoRgb = Kee[int](5)

  class Primaries(CuteNum, scoped=True):
    """
    The enum 'QQuickColorSpaceEnums::Primaries' of Qt, with the 5 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Custom = Kee[int](0)
    SRgb = Kee[int](1)
    AdobeRgb = Kee[int](2)
    DciP3D65 = Kee[int](3)
    ProPhotoRgb = Kee[int](4)

  class TransferFunction(CuteNum, scoped=True):
    """
    The enum 'QQuickColorSpaceEnums::TransferFunction' of Qt, with the 5
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Custom = Kee[int](0)
    Linear = Kee[int](1)
    Gamma = Kee[int](2)
    SRgb = Kee[int](3)
    ProPhotoRgb = Kee[int](4)
