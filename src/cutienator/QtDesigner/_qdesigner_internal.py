"""
qdesigner_internal stands for the namespace 'qdesigner_internal' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class qdesigner_internal:
  """
  The namespace 'qdesigner_internal' of Qt, which holds no objects. It holds
  the 6 enums Qt writes in it, each under its name, and the 0 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class AuxiliaryItemDataRoles(CuteNum):
    """
    The enum 'qdesigner_internal::AuxiliaryItemDataRoles' of Qt, with the 1
    names Qt gives in it.
    """

    ItemFlagsShadowRole = Kee[int](322372945)

  class ContainerType(CuteNum):
    """
    The enum 'qdesigner_internal::ContainerType' of Qt, with the 3 names Qt
    gives in it.
    """

    PageContainer = Kee[int](0)
    MdiContainer = Kee[int](1)
    WizardContainer = Kee[int](2)

  class IncludeType(CuteNum):
    """
    The enum 'qdesigner_internal::IncludeType' of Qt, with the 2 names Qt
    gives in it.
    """

    IncludeLocal = Kee[int](0)
    IncludeGlobal = Kee[int](1)

  class ObjectNamingMode(CuteNum):
    """
    The enum 'qdesigner_internal::ObjectNamingMode' of Qt, with the 2 names
    Qt gives in it.
    """

    CamelCase = Kee[int](0)
    Underscore = Kee[int](1)

  class TextPropertyValidationMode(CuteNum):
    """
    The enum 'qdesigner_internal::TextPropertyValidationMode' of Qt, with the
    7 names Qt gives in it.
    """

    ValidationMultiLine = Kee[int](0)
    ValidationRichText = Kee[int](1)
    ValidationStyleSheet = Kee[int](2)
    ValidationSingleLine = Kee[int](3)
    ValidationObjectName = Kee[int](4)
    ValidationObjectNameScope = Kee[int](5)
    ValidationURL = Kee[int](6)

  class UicLanguage(CuteNum, scoped=True):
    """
    The enum 'qdesigner_internal::UicLanguage' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Cpp = Kee[int](0)
    Python = Kee[int](1)
