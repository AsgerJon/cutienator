"""
QQmlSA stands for the namespace 'QQmlSA' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QQmlSA:
  """
  The namespace 'QQmlSA' of Qt, which holds no objects. It holds the 7 enums
  Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AccessSemantics(CuteNum, scoped=True):
    """
    The enum 'QQmlSA::AccessSemantics' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Reference = Kee[int](0)
    Value = Kee[int](1)
    NULL = Kee[int](2)
    Sequence = Kee[int](3)

  class BindingType(CuteNum, scoped=True):
    """
    The enum 'QQmlSA::BindingType' of Qt, with the 14 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Invalid = Kee[int](0)
    BoolLiteral = Kee[int](1)
    NumberLiteral = Kee[int](2)
    StringLiteral = Kee[int](3)
    RegExpLiteral = Kee[int](4)
    Null = Kee[int](5)
    Translation = Kee[int](6)
    TranslationById = Kee[int](7)
    Script = Kee[int](8)
    Object = Kee[int](9)
    Interceptor = Kee[int](10)
    ValueSource = Kee[int](11)
    AttachedProperty = Kee[int](12)
    GroupProperty = Kee[int](13)

  class Flag(CuteNum, scoped=True):
    """
    The enum 'QQmlSA::Flag' of Qt, with the 11 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Creatable = Kee[int](1)
    Composite = Kee[int](2)
    Singleton = Kee[int](4)
    Script = Kee[int](8)
    CustomParser = Kee[int](16)
    Array = Kee[int](32)
    InlineComponent = Kee[int](64)
    WrappedInImplicitComponent = Kee[int](128)
    HasBaseTypeError = Kee[int](256)
    HasExtensionNamespace = Kee[int](512)
    IsListProperty = Kee[int](1024)

  class MethodType(CuteNum, scoped=True):
    """
    The enum 'QQmlSA::MethodType' of Qt, with the 4 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Signal = Kee[int](0)
    Slot = Kee[int](1)
    Method = Kee[int](2)
    StaticMethod = Kee[int](3)

  class ScopeType(CuteNum, scoped=True):
    """
    The enum 'QQmlSA::ScopeType' of Qt, with the 8 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    JSFunctionScope = Kee[int](0)
    JSLexicalScope = Kee[int](1)
    QMLScope = Kee[int](2)
    GroupedPropertyScope = Kee[int](3)
    AttachedPropertyScope = Kee[int](4)
    EnumScope = Kee[int](5)
    BindingFunctionScope = Kee[int](6)
    SignalHandlerFunctionScope = Kee[int](7)

  class ScriptBindingKind(CuteNum, scoped=True):
    """
    The enum 'QQmlSA::ScriptBindingKind' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Invalid = Kee[int](0)
    PropertyBinding = Kee[int](1)
    SignalHandler = Kee[int](2)
    ChangeHandler = Kee[int](3)

  class WarningSeverity(CuteNum, scoped=True):
    """
    The enum 'QQmlSA::WarningSeverity' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Disable = Kee[int](100)
    Info = Kee[int](4)
    Warning = Kee[int](1)
    Error = Kee[int](2)
