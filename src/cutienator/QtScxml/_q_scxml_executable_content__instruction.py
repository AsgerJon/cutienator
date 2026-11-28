"""
QScxmlExecutableContent::Instruction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlExecutableContent::Instruction to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute


class Instruction(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScxmlExecutableContent::Instruction: a plain Python
  object standing in front of one C++ QScxmlExecutableContent::Instruction.

  C++ hands a QScxmlExecutableContent::Instruction around as a copy, so every
  C++ QScxmlExecutableContent::Instruction behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  No function of Qt's QScxmlExecutableContent::Instruction yet. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlExecutableContent::Instruction::~Instruction()': the
    destructor: Python removes its C++ QScxmlExecutableContent::Instruction
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QScxmlExecutableContent::Instruction is created at the first use,
    not by 'QScxmlExecutableContent::Instruction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlExecutableContent::Instruction back gives a
    copy the ritual made for Python, in a new cute
    QScxmlExecutableContent::Instruction.
  """

  #  The enums Qt writes inside QScxmlExecutableContent::Instruction, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class InstructionType(CuteNum):
    """
    The enum 'QScxmlExecutableContent::Instruction::InstructionType' of Qt,
    with the 12 names Qt gives in it.
    """

    Sequence = Kee[int](1)
    Sequences = Kee[int](2)
    Send = Kee[int](3)
    Raise = Kee[int](4)
    Log = Kee[int](5)
    JavaScript = Kee[int](6)
    Assign = Kee[int](7)
    Initialize = Kee[int](8)
    If = Kee[int](9)
    Foreach = Kee[int](10)
    Cancel = Kee[int](11)
    DoneData = Kee[int](12)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlExecutableContent::Instruction'

  #  Qt's '~QScxmlExecutableContent::Instruction()'. Naming it makes this a
  #  value class: Python owns every C++ QScxmlExecutableContent::Instruction
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QScxmlExecutableContent11InstructionD1Ev'

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
