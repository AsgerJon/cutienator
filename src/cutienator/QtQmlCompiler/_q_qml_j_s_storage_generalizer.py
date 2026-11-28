"""
QQmlJSStorageGeneralizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsstoragegeneralizer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSStorageGeneralizer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQml import QV4
from . import QQmlJSCompilePass

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSStorageGeneralizer(QQmlJSCompilePass):
  """
  The cute side of Qt's QQmlJSStorageGeneralizer: a plain Python object
  standing in front of one C++ QQmlJSStorageGeneralizer.

  It is built on the cute 'QQmlJSCompilePass', as Qt's
  QQmlJSStorageGeneralizer is built on Qt's QQmlJSCompilePass, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJSStorageGeneralizer that has a ritual and that
  Python can call so far, 2 names in all: 'run', 'endInstruction'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSStorageGeneralizer::QQmlJSStorageGeneralizer(const
    QV4::Compiler::JSUnitGenerator *jsUnitGenerator, const QQmlJSTypeResolver
    *typeResolver, QQmlJSLogger *logger, const BasicBlocks &basicBlocks,
    const InstructionAnnotations &annotations)': takes a type Python has no
    way to hand over yet.
  - Qt's 'Verdict
    QQmlJSStorageGeneralizer::startInstruction(QV4::Moth::Instr::Type a0)':
    gives the enum 'QV4::Moth::ByteCodeHandler::Verdict', whose class cannot
    be named here.

  What to expect
  --------------

  - The C++ QQmlJSStorageGeneralizer is created at the first use, not by
    'QQmlJSStorageGeneralizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSStorageGeneralizer.
  - Each name of Qt's QQmlJSStorageGeneralizer that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSStorageGeneralizer'

  #  A C++ QQmlJSStorageGeneralizer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSStorageGeneralizer'

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
    Qt's 'QQmlJSStorageGeneralizer::QQmlJSStorageGeneralizer(const
    QV4::Compiler::JSUnitGenerator *jsUnitGenerator, const QQmlJSTypeResolver
    *typeResolver, QQmlJSLogger *logger, const BasicBlocks &basicBlocks,
    const InstructionAnnotations &annotations)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSStorageGeneralizer.__init__' has no cute function yet. Qt's "
        "'QQmlJSStorageGeneralizer::QQmlJSStorageGeneralizer(const "
        "QV4::Compiler::JSUnitGenerator *jsUnitGenerator, const "
        "QQmlJSTypeResolver *typeResolver, QQmlJSLogger *logger, const "
        "BasicBlocks &basicBlocks, const InstructionAnnotations "
        "&annotations)': takes a type Python has no way to hand over yet.")

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

  @overload(QQmlJSCompilePass.Function)
  @overload(NoneType)
  def run(
      self,
      function: Optional[QQmlJSCompilePass.Function],
  ) -> QQmlJSCompilePass.BlocksAndAnnotations:
    """
    Calls Qt's 'BlocksAndAnnotations QQmlJSStorageGeneralizer::run(const
    Function *function)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsstoragegeneralizer.html#run

    Parameters
    ----------

    function : Optional[QQmlJSCompilePass.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlJSCompilePass.BlocksAndAnnotations
      A new cute QQmlJSCompilePass::BlocksAndAnnotations around the copy Qt
      gave back. Python owns it.
    """
    #  BlocksAndAnnotations QQmlJSStorageGeneralizer::run(const Function
    #      *function)
    address = self.uglySide.call(
        'ritual_ZN24QQmlJSStorageGeneralizer3runEPKN17QQmlJSCompilePass8Fun'
        'ctionE',
        self._addressOf(function),
    )
    return QQmlJSCompilePass.BlocksAndAnnotations._cuteOwning(address)

  @overload(QV4.Moth.Instr.Type)
  def endInstruction(self, a0: QV4.Moth.Instr.Type) -> None:
    """
    Calls Qt's 'void
    QQmlJSStorageGeneralizer::endInstruction(QV4::Moth::Instr::Type a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsstoragegeneralizer.html#endInstruction

    Parameters
    ----------

    a0 : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  void QQmlJSStorageGeneralizer::endInstruction(QV4::Moth::Instr::Type
    #      a0)
    ritual = (
        'ritual_ZN24QQmlJSStorageGeneralizer14endInstructionEN3QV44Moth5Ins'
        'tr4TypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlJSStorageGeneralizer14endInstructionEN3QV44Mo'
          'th5Instr4TypeE')
    self.uglySide.call(ritual, a0.value)
