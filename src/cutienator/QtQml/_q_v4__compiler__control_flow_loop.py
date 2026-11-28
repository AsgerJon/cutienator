"""
QV4::Compiler::ControlFlowLoop binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compilercontrolflow_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::Compiler::ControlFlowLoop to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ControlFlowLoop(QV4.Compiler.ControlFlowUnwindCleanup):
  """
  The cute side of Qt's QV4::Compiler::ControlFlowLoop: a plain Python object
  standing in front of one C++ QV4::Compiler::ControlFlowLoop.

  It is built on the cute 'QV4::Compiler::ControlFlowUnwindCleanup', as Qt's
  QV4::Compiler::ControlFlowLoop is built on Qt's
  QV4::Compiler::ControlFlowUnwindCleanup, and has everything that class has.

  C++ hands a QV4::Compiler::ControlFlowLoop around as a copy, so every C++
  QV4::Compiler::ControlFlowLoop behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::Compiler::ControlFlowLoop that has a ritual and
  that Python can call so far, 1 name in all: 'label'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Compiler::ControlFlowLoop::~ControlFlowLoop()': the
    destructor: Python removes its C++ QV4::Compiler::ControlFlowLoop by it,
    and has no other use for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QV4::Compiler::ControlFlowLoop is created at the first use, not
    by 'QV4::Compiler::ControlFlowLoop(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Compiler::ControlFlowLoop back gives a copy the
    ritual made for Python, in a new cute QV4::Compiler::ControlFlowLoop.
  - Each name of Qt's QV4::Compiler::ControlFlowLoop that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Compiler::ControlFlowLoop'

  #  A C++ QV4::Compiler::ControlFlowLoop Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QV4_Compiler_ControlFlowLoop'

  #  Qt's '~QV4::Compiler::ControlFlowLoop()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::Compiler::ControlFlowLoop behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV48Compiler15ControlFlowLoopD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def label(self) -> str:
    """
    Calls Qt's 'QString QV4::Compiler::ControlFlowLoop::label() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-controlflowloop.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Compiler::ControlFlowLoop::label() const
    ritual = 'ritual_ZNK3QV48Compiler15ControlFlowLoop5labelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK3QV48Compiler15ControlFlowLoop5labelEv'
    return self.uglySide.call(ritual)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QV4::Compiler::ControlFlowLoop::ControlFlowLoop(Codegen *cg,
    BytecodeGenerator::Label *breakLabel, BytecodeGenerator::Label
    *continueLabel, std::function<void ()> cleanup)': the compiler refuses
    its ritual as it would be written here: use of undeclared identifier
    'BytecodeGenerator'; did you mean
    'CuteQV4_Compiler_ControlFlowLoop::BytecodeGenerator'?.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ControlFlowLoop.__init__' has no cute function yet. "
        "Qt's 'QV4::Compiler::ControlFlowLoop::ControlFlowLoop(Codegen *cg, "
        "BytecodeGenerator::Label *breakLabel, BytecodeGenerator::Label "
        "*continueLabel, std::function<void ()> cleanup)': the compiler "
        "refuses its ritual as it would be written here: use of undeclared "
        "identifier 'BytecodeGenerator'; did you mean "
        "'CuteQV4_Compiler_ControlFlowLoop::BytecodeGenerator'?.")

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
