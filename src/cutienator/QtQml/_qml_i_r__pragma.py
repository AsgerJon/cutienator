"""
QmlIR::Pragma binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::Pragma to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute


class Pragma(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QmlIR::Pragma: a plain Python object standing in
  front of one C++ QmlIR::Pragma.

  C++ hands a QmlIR::Pragma around as a copy, so every C++ QmlIR::Pragma
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QmlIR::Pragma yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QmlIR::Pragma::~Pragma()': the destructor: Python removes its C++
    QmlIR::Pragma by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QmlIR::Pragma is created at the first use, not by
    'QmlIR::Pragma(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QmlIR::Pragma back gives a copy the ritual made for
    Python, in a new cute QmlIR::Pragma.
  """

  #  The enums Qt writes inside QmlIR::Pragma, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ComponentBehaviorValue(CuteNum):
    """
    The enum 'QmlIR::Pragma::ComponentBehaviorValue' of Qt, with the 2 names
    Qt gives in it.
    """

    Unbound = Kee[int](0)
    Bound = Kee[int](1)

  class FunctionSignatureBehaviorValue(CuteNum):
    """
    The enum 'QmlIR::Pragma::FunctionSignatureBehaviorValue' of Qt, with the
    2 names Qt gives in it.
    """

    Ignored = Kee[int](0)
    Enforced = Kee[int](1)

  class ListPropertyAssignBehaviorValue(CuteNum):
    """
    The enum 'QmlIR::Pragma::ListPropertyAssignBehaviorValue' of Qt, with the
    3 names Qt gives in it.
    """

    Append = Kee[int](0)
    Replace = Kee[int](1)
    ReplaceIfNotDefault = Kee[int](2)

  class NativeMethodBehaviorValue(CuteNum):
    """
    The enum 'QmlIR::Pragma::NativeMethodBehaviorValue' of Qt, with the 2
    names Qt gives in it.
    """

    AcceptThisObject = Kee[int](0)
    RejectThisObject = Kee[int](1)

  class PragmaType(CuteNum):
    """
    The enum 'QmlIR::Pragma::PragmaType' of Qt, with the 8 names Qt gives in
    it.
    """

    Singleton = Kee[int](0)
    Strict = Kee[int](1)
    ListPropertyAssignBehavior = Kee[int](2)
    ComponentBehavior = Kee[int](3)
    FunctionSignatureBehavior = Kee[int](4)
    NativeMethodBehavior = Kee[int](5)
    ValueTypeBehavior = Kee[int](6)
    Translator = Kee[int](7)

  class ValueTypeBehaviorValue(CuteFlags):
    """
    The flags enum 'QmlIR::Pragma::ValueTypeBehaviorValue' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QmlIR::Pragma::ValueTypeBehaviorValues'.
    """

    Copy = 0x1
    Addressable = 0x2
    Assertable = 0x4

  ValueTypeBehaviorValues = ValueTypeBehaviorValue

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlIR::Pragma'

  #  Qt's '~QmlIR::Pragma()'. Naming it makes this a value class: Python owns
  #  every C++ QmlIR::Pragma behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN5QmlIR6PragmaD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
