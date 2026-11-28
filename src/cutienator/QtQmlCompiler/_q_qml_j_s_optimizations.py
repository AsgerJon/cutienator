"""
QQmlJSOptimizations binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsoptimizations_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSOptimizations to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QQmlJSOptimizations(QQmlJSCompilePass):
  """
  The cute side of Qt's QQmlJSOptimizations: a plain Python object standing
  in front of one C++ QQmlJSOptimizations.

  It is built on the cute 'QQmlJSCompilePass', as Qt's QQmlJSOptimizations is
  built on Qt's QQmlJSCompilePass, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJSOptimizations that has a ritual and that
  Python can call so far, 7 names in all: 'run', 'endInstruction',
  'populateBasicBlocks', 'populateReaderLocationsTrackedTypes',
  'populateReaderLocationsReadersAndConversions', 'adjustTypes',
  'removeDeadStoresUntilStable'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSOptimizations::QQmlJSOptimizations(const
    QV4::Compiler::JSUnitGenerator *unitGenerator, const QQmlJSTypeResolver
    *typeResolver, QQmlJSLogger *logger, const BasicBlocks &basicBlocks,
    const InstructionAnnotations &annotations, QList<ObjectOrArrayDefinition>
    objectAndArrayDefinitions)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmlJSOptimizations::~QQmlJSOptimizations()': the destructor:
    Python never removes a C++ QQmlJSOptimizations.
  - Qt's 'QV4::Moth::ByteCodeHandler::Verdict
    QQmlJSOptimizations::startInstruction(QV4::Moth::Instr::Type a0)': gives
    the enum 'QV4::Moth::ByteCodeHandler::Verdict', whose class cannot be
    named here.
  - Qt's 'bool QQmlJSOptimizations::canMove(int instructionOffset, const
    RegisterAccess &access) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QQmlJSOptimizations::removeReadsFromErasedInstructions(const
    QFlatMap<int, InstructionAnnotation>::const_iterator &it)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 13 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QQmlJSOptimizations is created at the first use, not by
    'QQmlJSOptimizations(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSOptimizations.
  - Each name of Qt's QQmlJSOptimizations that has no cute function yet,
    '__init__', 'canMove', 'eraseDeadStore',
    'removeReadsFromErasedInstructions', holds a function that raises
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
  __qt_class__ = 'QQmlJSOptimizations'

  #  A C++ QQmlJSOptimizations Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSOptimizations'

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
    Qt's 'QQmlJSOptimizations::QQmlJSOptimizations(const
    QV4::Compiler::JSUnitGenerator *unitGenerator, const QQmlJSTypeResolver
    *typeResolver, QQmlJSLogger *logger, const BasicBlocks &basicBlocks,
    const InstructionAnnotations &annotations, QList<ObjectOrArrayDefinition>
    objectAndArrayDefinitions)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlJSOptimizations.__init__' has no cute function yet. Qt's "
        "'QQmlJSOptimizations::QQmlJSOptimizations(const "
        "QV4::Compiler::JSUnitGenerator *unitGenerator, const "
        "QQmlJSTypeResolver *typeResolver, QQmlJSLogger *logger, const "
        "BasicBlocks &basicBlocks, const InstructionAnnotations "
        "&annotations, QList<ObjectOrArrayDefinition> "
        "objectAndArrayDefinitions)': takes a type Python has no way to "
        "hand over yet.")

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
    Calls Qt's 'BlocksAndAnnotations QQmlJSOptimizations::run(const Function
    *function)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsoptimizations.html#run

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
    #  BlocksAndAnnotations QQmlJSOptimizations::run(const Function
    #      *function)
    address = self.uglySide.call(
        'ritual_ZN19QQmlJSOptimizations3runEPKN17QQmlJSCompilePass8Function'
        'E',
        self._addressOf(function),
    )
    return QQmlJSCompilePass.BlocksAndAnnotations._cuteOwning(address)

  @overload(QV4.Moth.Instr.Type)
  def endInstruction(self, a0: QV4.Moth.Instr.Type) -> None:
    """
    Calls Qt's 'void
    QQmlJSOptimizations::endInstruction(QV4::Moth::Instr::Type a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsoptimizations.html#endInstruction

    Parameters
    ----------

    a0 : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  void QQmlJSOptimizations::endInstruction(QV4::Moth::Instr::Type a0)
    ritual = (
        'ritual_ZN19QQmlJSOptimizations14endInstructionEN3QV44Moth5Instr4Ty'
        'peE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSOptimizations14endInstructionEN3QV44Moth5In'
          'str4TypeE')
    self.uglySide.call(ritual, a0.value)

  def populateBasicBlocks(self) -> None:
    """
    Calls Qt's 'void QQmlJSOptimizations::populateBasicBlocks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsoptimizations.html#populateBasicBlocks
    """
    #  void QQmlJSOptimizations::populateBasicBlocks()
    self.uglySide.call(
        'ritual_ZN19QQmlJSOptimizations19populateBasicBlocksEv',
    )

  def populateReaderLocationsTrackedTypes(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSOptimizations::populateReaderLocationsTrackedTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsoptimizations.html
    """
    #  void QQmlJSOptimizations::populateReaderLocationsTrackedTypes()
    self.uglySide.call(
        'ritual_ZN19QQmlJSOptimizations35populateReaderLocationsTrackedType'
        'sEv',
    )

  def populateReaderLocationsReadersAndConversions(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSOptimizations::populateReaderLocationsReadersAndConversions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsoptimizations.html
    """
    #  void
    #      QQmlJSOptimizations::populateReaderLocationsReadersAndConversions(
    #      )
    self.uglySide.call(
        'ritual_ZN19QQmlJSOptimizations44populateReaderLocationsReadersAndC'
        'onversionsEv',
    )

  def adjustTypes(self) -> None:
    """
    Calls Qt's 'void QQmlJSOptimizations::adjustTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsoptimizations.html#adjustTypes
    """
    #  void QQmlJSOptimizations::adjustTypes()
    self.uglySide.call('ritual_ZN19QQmlJSOptimizations11adjustTypesEv')

  def removeDeadStoresUntilStable(self) -> None:
    """
    Calls Qt's 'void QQmlJSOptimizations::removeDeadStoresUntilStable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsoptimizations.html
    """
    #  void QQmlJSOptimizations::removeDeadStoresUntilStable()
    self.uglySide.call(
        'ritual_ZN19QQmlJSOptimizations27removeDeadStoresUntilStableEv',
    )

  @staticmethod
  def canMove(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSOptimizations::canMove(int instructionOffset, const
    RegisterAccess &access) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlJSOptimizations.canMove' has no cute function yet. Qt's 'bool "
        "QQmlJSOptimizations::canMove(int instructionOffset, const "
        "RegisterAccess &access) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def eraseDeadStore(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSOptimizations::eraseDeadStore(const
    InstructionAnnotations::iterator &it, bool &erasedReaders)': the compiler
    refuses its ritual as it would be written here: use of undeclared
    identifier 'InstructionAnnotations'; did you mean
    'CuteQQmlJSOptimizations::InstructionAnnotations'?.
    """
    raise NotImplementedError(
        "'QQmlJSOptimizations.eraseDeadStore' has no cute function yet. "
        "Qt's 'bool QQmlJSOptimizations::eraseDeadStore(const "
        "InstructionAnnotations::iterator &it, bool &erasedReaders)': the "
        "compiler refuses its ritual as it would be written here: use of "
        "undeclared identifier 'InstructionAnnotations'; did you mean "
        "'CuteQQmlJSOptimizations::InstructionAnnotations'?.")

  @staticmethod
  def removeReadsFromErasedInstructions(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSOptimizations::removeReadsFromErasedInstructions(const
    QFlatMap<int, InstructionAnnotation>::const_iterator &it)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSOptimizations.removeReadsFromErasedInstructions' has no "
        "cute function yet. Qt's 'void "
        "QQmlJSOptimizations::removeReadsFromErasedInstructions(const "
        "QFlatMap<int, InstructionAnnotation>::const_iterator &it)': takes "
        "a type Python has no way to hand over yet.")
