"""
QV4::JIT::BaselineJIT binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4baselinejit_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::JIT::BaselineJIT to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class BaselineJIT(QV4.Moth.ByteCodeHandler):
  """
  The cute side of Qt's QV4::JIT::BaselineJIT: a plain Python object standing
  in front of one C++ QV4::JIT::BaselineJIT.

  It is built on the cute 'QV4::Moth::ByteCodeHandler', as Qt's
  QV4::JIT::BaselineJIT is built on Qt's QV4::Moth::ByteCodeHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::JIT::BaselineJIT that has a ritual and that
  Python can call so far, 5 names in all: 'generate_Debug', 'generate_Yield',
  'generate_YieldStar', 'generate_Resume', 'endInstruction'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has no ritual
  ------------------

  133 of the 138 functions Qt declares: 74 leans on 'QV4; 59 Qt's library has
  no name for it, and its code in Qt's source does not compile apart from its
  file.

  What to expect
  --------------

  - The C++ QV4::JIT::BaselineJIT is created at the first use, not by
    'QV4::JIT::BaselineJIT(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::JIT::BaselineJIT.
  - Each name of Qt's QV4::JIT::BaselineJIT that has no cute function yet,
    '__init__', 'generate', holds a function that raises
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
  __qt_class__ = 'QV4::JIT::BaselineJIT'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QV4::JIT::BaselineJIT::BaselineJIT(QV4::Function *a0)': leans on
    'QV4::JIT::BaselineJIT::generate_As(int)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineJIT.__init__' has no cute function yet. Qt's "
        "'QV4::JIT::BaselineJIT::BaselineJIT(QV4::Function *a0)': leans on "
        "'QV4::JIT::BaselineJIT::generate_As(int)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def generate_Debug(self) -> None:
    """
    Calls Qt's 'void QV4::JIT::BaselineJIT::generate_Debug()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jit-baselinejit.html#generate_Debug
    """
    #  void QV4::JIT::BaselineJIT::generate_Debug()
    self.uglySide.call('ritual_ZN3QV43JIT11BaselineJIT14generate_DebugEv')

  def generate_Yield(self) -> None:
    """
    Calls Qt's 'void QV4::JIT::BaselineJIT::generate_Yield()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jit-baselinejit.html#generate_Yield
    """
    #  void QV4::JIT::BaselineJIT::generate_Yield()
    self.uglySide.call('ritual_ZN3QV43JIT11BaselineJIT14generate_YieldEv')

  def generate_YieldStar(self) -> None:
    """
    Calls Qt's 'void QV4::JIT::BaselineJIT::generate_YieldStar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jit-baselinejit.html#generate_YieldStar
    """
    #  void QV4::JIT::BaselineJIT::generate_YieldStar()
    self.uglySide.call(
        'ritual_ZN3QV43JIT11BaselineJIT18generate_YieldStarEv',
    )

  @overload(int)
  def generate_Resume(self, a0: int) -> None:
    """
    Calls Qt's 'void QV4::JIT::BaselineJIT::generate_Resume(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jit-baselinejit.html#generate_Resume

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QV4::JIT::BaselineJIT::generate_Resume(int a0)
    self.uglySide.call(
        'ritual_ZN3QV43JIT11BaselineJIT15generate_ResumeEi', a0,
    )

  @overload(QV4.Moth.Instr.Type)
  def endInstruction(self, instr: QV4.Moth.Instr.Type) -> None:
    """
    Calls Qt's 'void QV4::JIT::BaselineJIT::endInstruction(Moth::Instr::Type
    instr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jit-baselinejit.html#endInstruction

    Parameters
    ----------

    instr : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  void QV4::JIT::BaselineJIT::endInstruction(Moth::Instr::Type instr)
    self.uglySide.call(
        'ritual_ZN3QV43JIT11BaselineJIT14endInstructionENS_4Moth5Instr4Type'
        'E',
        instr.value,
    )

  @staticmethod
  def generate(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineJIT::generate()': leans on
    'QV4::JIT::BaselineAssembler::generateEpilogue()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineJIT.generate' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineJIT::generate()': leans on "
        "'QV4::JIT::BaselineAssembler::generateEpilogue()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
