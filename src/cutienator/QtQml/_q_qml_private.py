"""
QQmlPrivate stands for the namespace 'QQmlPrivate' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QQmlPrivate:
  """
  The namespace 'QQmlPrivate' of Qt, which holds no objects. It holds the 5
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AutoParentResult(CuteNum):
    """
    The enum 'QQmlPrivate::AutoParentResult' of Qt, with the 3 names Qt gives
    in it.
    """

    Parented = Kee[int](0)
    IncompatibleObject = Kee[int](1)
    IncompatibleParent = Kee[int](2)

  class QmlRegistrationWarning(CuteNum):
    """
    The enum 'QQmlPrivate::QmlRegistrationWarning' of Qt, with the 3 names Qt
    gives in it.
    """

    UnconstructibleType = Kee[int](0)
    UnconstructibleSingleton = Kee[int](1)
    NonQObjectWithAtached = Kee[int](2)

  class RegistrationType(CuteNum):
    """
    The enum 'QQmlPrivate::RegistrationType' of Qt, with the 11 names Qt
    gives in it.
    """

    TypeRegistration = Kee[int](0)
    InterfaceRegistration = Kee[int](1)
    AutoParentRegistration = Kee[int](2)
    SingletonRegistration = Kee[int](3)
    CompositeRegistration = Kee[int](4)
    CompositeSingletonRegistration = Kee[int](5)
    QmlUnitCacheHookRegistration = Kee[int](6)
    TypeAndRevisionsRegistration = Kee[int](7)
    SingletonAndRevisionsRegistration = Kee[int](8)
    SequentialContainerRegistration = Kee[int](9)
    SequentialContainerAndRevisionsRegistration = Kee[int](10)

  class SingletonConstructionMode(CuteNum, scoped=True):
    """
    The enum 'QQmlPrivate::SingletonConstructionMode' of Qt, with the 5 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    Constructor = Kee[int](1)
    Factory = Kee[int](2)
    FactoryWrapper = Kee[int](3)
    ExplicitNone = Kee[int](4)

  class ValueTypeCreationMethod(CuteNum, scoped=True):
    """
    The enum 'QQmlPrivate::ValueTypeCreationMethod' of Qt, with the 3 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    Construct = Kee[int](1)
    Structured = Kee[int](2)
